# microservice exercise
This is a microservice for fetching weather data from api. 

To test this you need to:
- Insert api key to services/constants.py
- Install required modules with 'pip install -r requirements.txt'
- Run the program with 'flask --app services/weatherservice run'

Then you can send GET request to http://localhost:5000/{city} to get weather data for the city
