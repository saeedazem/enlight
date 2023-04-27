from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, db, storage
import os
from atlassian import Confluence

# Initialize Flask app
app = Flask(__name__, template_folder=os.path.join(os.path.abspath(os.getcwd()), 'templates'))

# Initialize Firebase app
cred = credentials.Certificate(os.path.join(os.path.abspath(os.getcwd()), "enlight-9e07c-firebase-adminsdk-degv3-381019d016.json"))
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://enlight-9e07c-default-rtdb.europe-west1.firebasedatabase.app/',
    'storageBucket': 'enlight-9e07c.appspot.com'  
})

# Define the route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Define the route for the search box
@app.route('/search', methods=['POST'])
def search():
    # Get the query entered by the user
    query = request.form['query']
    num_queries = None
    if query:
        # Save the query in the Firebase database
        ref = db.reference('queries')
        ref.push().set(query)
        # Get the number of queries in the Firebase database
        num_queries = len(ref.get())

    # Render the results page with the number of queries
    return render_template('results.html', title='Search Results', num_queries=num_queries)

# Define the route for the text file search
@app.route('/text_search', methods=['POST'])
def text_search():
    # Get the keyword entered by the user
    keyword = request.form['keyword']
    keyword_exists_in_db = False
    if keyword:
        # Get a reference to the collection
        ref = db.reference('text_files')

        # Retrieve all the items in the collection
        all_items = ref.get()

        # Loop through the items and compare the text files values in db with the keyword
        for item_key, item_val in all_items.items():
            bucket = storage.bucket(app=firebase_admin.get_app())
            output_str = os.path.basename(item_val)
            blob = bucket.blob(output_str)

            # Download the file as a string
            file_content = blob.download_as_string()

            # Convert the file content to a string (assuming it's UTF-8 encoded)
            file_content_str = file_content.decode('utf-8')
            # compare the keyword with the file content
            if keyword.lower() in file_content_str.lower():
                keyword_exists_in_db = True
                break

    output_str = output_str if keyword_exists_in_db else None
    # render the results page
    return render_template('results.html', title='Keywrod Search Result', keyword=keyword, file_name=output_str)

# Define the route for the confluence page search
@app.route('/confluence_search', methods=['POST'])
def confluence_search():
    # Get the keyword entered by the user
    keyword = request.form['keyword']
    output_str = None
    if keyword:
        confluence_login = 'saeedazem1993@gmail.com'
        confluence_password =  ''
        #init confluence object
        confluence = Confluence(
        url='https://enlight-exercise.atlassian.net',
        username = confluence_login,
        password = confluence_password,
        verify_ssl = False,
        timeout=180,
        )
        space_key = 'Exercise'
        limit = 50
        content_type = 'page'
        #Get space content (configuring by the expand property)
        spcae_content = confluence.get_space_content(space_key)
        # Fetch pages from the Confluence REST API
        pages = confluence.get_all_pages_from_space(space_key, limit=limit, content_type=content_type)
        if pages:
            # compare the confluence pages conetnt with keyword
            for page in pages:
                for result in spcae_content["page"]["results"]:
                    if page['id'] == result['id']:
                        content = result['body']['storage']['value'].lower()
                        if keyword.lower() in content:
                            output_str = page['title']
    
    # render the results page
    return render_template('results.html', title='Keywrod Search Result', keyword=keyword, file_name=output_str)

if __name__ == '__main__':
    app.run()
