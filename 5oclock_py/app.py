from flask import Flask, jsonify, redirect, url_for
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin

#
import random
from datetime import datetime
from pytz import timezone, all_timezones

def filter_time_zones(all_time_zones):
    excluded_time_zones = [
    'CET', 'CST6CDT', 'EET', 'EST', 'EST5EDT', 'GB', 'GB-Eire', 'GMT', 'GMT+0', 'GMT-0', 'GMT0',
    'HST', 'MET', 'MST', 'MST7MDT', 'UCT', 'UTC', 'W-SU', 'WET', 'Etc/GMT', 'Etc/GMT+0', 'Etc/GMT+1',
    'Etc/GMT+10', 'Etc/GMT+11', 'Etc/GMT+12', 'Etc/GMT+2', 'Etc/GMT+3', 'Etc/GMT+4', 'Etc/GMT+5',
    'Etc/GMT+6', 'Etc/GMT+7', 'Etc/GMT+8', 'Etc/GMT+9', 'Etc/GMT-0', 'Etc/GMT-1', 'Etc/GMT-10',
    'Etc/GMT-11', 'Etc/GMT-12', 'Etc/GMT-13', 'Etc/GMT-14', 'Etc/GMT-2', 'Etc/GMT-3', 'Etc/GMT-4',
    'Etc/GMT-5', 'Etc/GMT-6', 'Etc/GMT-7', 'Etc/GMT-8', 'Etc/GMT-9', 'Etc/GMT0', 'Etc/Greenwich',
    'Etc/UCT', 'Etc/UTC', 'Etc/Universal', 'Etc/Zulu', 'Universal', 'Zulu', 'PST8PDT'
]

    # Loop through time zones and exclude those in the exclusion list
    filtered_time_zones = [tz for tz in all_time_zones if tz not in excluded_time_zones]

    return filtered_time_zones

def get_random_location_at_5pm():
    # Get the current time in UTC
    utc_time = datetime.utcnow()

    # Define a list to store locations where it's 5 PM
    locations_at_5pm = []

    filtered_time_zones = filter_time_zones(all_timezones)

    for time_zone_name in filtered_time_zones:
        time_zone = timezone(time_zone_name)
        localized_time = utc_time.replace(tzinfo=timezone('UTC')).astimezone(time_zone)
        if localized_time.strftime('%H') == '17':
            # Split the time zone name and take only the last part (the location)
            parts = time_zone_name.split('/')
            if len(parts) > 1:
                location_name = parts[-1].replace("_", " ")
                region = parts[-2].replace("_", " ")
                full_region = f"{location_name}, {region}"
                locations_at_5pm.append((full_region, localized_time))

    if locations_at_5pm:
        # Randomly select one location from the list
        selected_location, selected_time = random.choice(locations_at_5pm)

        return selected_location, selected_time
    else:
        return None
    
# 



# from main import get_random_location_at_5pm  # Updated import

app = Flask(__name__, static_folder='../5o_clock_somewhere_ui/build')

CORS(app)

@app.route('/api/getRandomLocation', methods=['GET'])
@cross_origin()

def get_random_location():
    result = get_random_location_at_5pm()  # Call the function
    if result:
        selected_location, selected_time = result
        random_location = {
            "location": selected_location,
            "time": selected_time.strftime('%I:%M %p')
        }
        return jsonify(random_location)
    else:
        return jsonify({"error": "No locations found where it's currently 5 PM."})

@app.route('/')
@cross_origin()
def default_route():
    return redirect(url_for('get_random_location'))

@app.route('/serve')
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
