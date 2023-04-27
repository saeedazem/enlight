# enlight

The Solution for this assignment is based on flask framework for python,
the main page is task.py which runs the wep app and initialize the connection to firebase and defines 4 routes:
1) '/' => main page
2) '/search' => answer for part1
3) '/text_search' => answer for part2
4) '/confluence_search' => answer for bonus

How to run the web app:
1) run the command "flask --app task.py run" (or for dev mode: "flask --app example_app.py --debug run")
2) To connect to the web app GUI got the browser and eneter the url link: http://127.0.0.1:5000/ , it will render the template of file 'home.html'
3) A web page with 3 cards will be open, each card for each part of assignment that contains title, text box and button
3.1.) The Card with title "Search Engine - Task1" is about part1 so if you enter text and press the button another web page will be open(render template of file 'results.html') with the results page shownig the number of queries asked in real time on the screen.
3.2) The Card with title "Search Engine - Task2" is about part2 so if you enter keyword and press the button another web page will be open(render template of file 'results.html') with the results page displaying if the keyword exists in the database text files in firebase
3.1) The Card with title "Search Engine - Bonus" is about bonus so if you enter keyword and press the button another web page will be open(render template of file 'results.html') with the results page displaying if the keyword exists in confluence pages in space 'Exercise'

General Notes:
1) firebase is the technology used for the database, i used one nosql Realtime Database with two json objects, one for part1 with key 'queries' containing a list of all words that got searched(the key for it is random string and the value is the searched word), 
the other json object is for part2 which it's key is 'text_files' and it's value a list of key/value for the path of text files(the key is string defines whose the path and the value contains the path to text file which saved in firebase storage)
2) templates folder conatins all html pages that the app gonna render
3) an example of the web app GUI can be seen in the screenshots attached to the repo in the folder 'screenshots' which contanis the images:
3.1) 'enlight-main-page.png' => main page of the app
3.2) 'enlight-part1-result.png' -> valid result of part1
3.3) 'enlight-part2-result.png' -> valid result of part2
3.4) 'enlight-bonus-result.png' -> valid result of bonus task
3.5) 'enlight-no-result-page.png' -> in case there's no results found for part2 or for the bonus task
4) the certificate file 'enlight-9e07c-firebase-adminsdk-degv3-381019d016.json' values must be filled so the app could connect to firebase database(didn't add those values cause it's a public repo), those values will be found in the attached file to the email
5) the parameter 'confluence_password' in file task.py must be filled with confluence api token(didn't add it  cause it's a public repo),
it's value will be found in the email
6) to style the frontened of web pages i used Bootstrap
