# infracloud_assignment

Technologies used : Python , Django Framework . To check the result use POSTMAN


1] Using the githublink . clone the repositiory. 

2] Open the cmd and cd into the directory having manage.py file of the project

3] Create a virtual environment and activate it .

4] Run the command > pip install requirements.txt #This will install all the dependancies required for the project. Now run the command < manage.py runserver >

5] Once the server is running .Open Postman to send request to the server.

6] Create a POST request to the url > localhost:8000/shorten > Below select body > form-data > Enter the key as "url" and enter value as <the url you want to short> and SEND.
  
7] You will get the shortened url of 7characters in JsonResponse format.

8] Now make a get request to the shortened url . Create GET request > Enter the url (Example : localhost:8000/<shortenedurl> ) and SEND . Select Preview below and you will be redirected to the long url which you entered . 
  
9] Now if you again create post request using the same LONG URL which you ented earlier .If the url al4ready exists then it will return you the SHORT URL which was created earlier for the existing LONG URL



URLS : 1] POST = localhost:8000/shorten      # To shorten url
       2] GET = localhost:8000/<shorturl>    # To open shortened url
       3] GET = localhost:8000/allurl        # To get all urls 
       4] GET = localhost:8000               # Homepage


-----OR-----
If you have docker installed : 

1] Clone the repository and cd into the directory of docker-compose 

2] Run the command < docker-compose build >

3] Run < docker-compose up >
