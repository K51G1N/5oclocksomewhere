# 5 o'clock py

The app.py handles the get request from the react front end and then calls the *get_random_location_at_5pm* method in the _main.py_ module
Once it receives feedback it creates a json object that can then be sent back to the frontend

main.py essentially gets the UTC time and gathers all_timezones (excluding some). It then iterates through each of the time zones and converts
the utc time to the timezone and checks if it's in the 17th hour. If it is it'll add it to the list of timezones/locations that are in their 17th hour.
Then it randomly selects a location and sends it to the server.