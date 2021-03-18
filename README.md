# infracloud_assignment

Technologies used : Python , Django Framework 


7] Now make a get request to the shortened url . Create GET request > Enter the url (Example : localhost:8000/<shortenedurl> ) and SEND . Select Preview below and you will be redirected to the long url which you entered . 


URLS : 1] POST = localhost:8000/shorten      # To shorten url
       2] GET = localhost:8000/< shorturl >    # To open shortened url
       3] GET = localhost:8000/allurl        # To get all urls 
       4] GET = localhost:8000               # Homepage



If you have dont have docker installed.  Please Install Docker and Docker-Compose : 

Step -1] Clone the repository and cd into the directory of docker-compose 

Step -2] Run the command :    docker-compose build 

Step -3] Run the command :    docker-compose up 

Step -4] Once the server is running .Open Postman to send request to the server.

Step -5] To create a POST request : 

----- If you are using POSTMAN .
Create a POST request to the url > localhost:8000/shorten > Below select body > form-data > Enter the key as "url" and enter value as < the url you want to short > and SEND.

----- If you dont have POSTMAN use the below format . Send the curl request in the below format .

curl -X POST http://127.0.0.1:8000/shorten -d "url=test198903/abcd" -H "Content-Type= application/json"

Step -6] You will get the shortened url of 7characters in JsonResponse format.

Step -7] Now if you again create POST request using the same LONG URL which you ented earlier .If the url already exists then it will return you the SHORT URL which was created earlier for the existing LONG URL .

Step -8] Now if you to want to check the shortened url . Open your browser and use https://127.0.0.1:8000/<shortenedurl>
Example : 
         If your long url is : http://youtube.com 
         You will get a shortened url of 7characters : ab3q563 
         To test the shortened url , Open the browser and Enter url in given format: https://127.0.0.1:8000/ab3q563 
         You will be redirected to your long url : http://youtube.com  



