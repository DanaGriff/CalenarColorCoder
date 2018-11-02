from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import json
import sys
from pprint import pprint
import os

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar' 

def print_result(counter):
    if counter == 0:
        print('no events were updated')
    elif counter == 1:
        print(counter, 'Event was updated successfully!')
    else:
        print(counter, 'Events were updated successfully!')


def full_path(file_name):
    dir_path = os.path.dirname(__file__)
    return os.path.join(dir_path, file_name)


def main():
    with open(full_path('color_coding_settings.json')) as f:
        try:
            data = json.load(f)
        except:
            print('The JSON File is corrupted, modify the file and re-run the script')
            sys.exit()

    CALENDER_ID = data["calender_id"]
    
    store = file.Storage(full_path('token.json'))
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(full_path('credentials.json'), SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))
    
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId=CALENDER_ID, timeMin=now,
                                        maxResults=200, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    colors = service.colors().get().execute()
    found = 0
    counter = 0
    colors_dict = {'BLUE' : 1,
                    'GREEN' : 2,
                    'PURPLE' : 3,
                    'RED' : 4,
                    'YELLOW' : 5,
                    'ORANGE' : 6,
                    'TURQUOISE' : 7,
                    'GREY' : 8,
                    'BOLD_BLUE' : 9,
                    'BOLD_GREEN' : 10,
                    'BOLD_RED' : 11}
    
    if not events:
        print('No upcoming events found.')
        sys.exit()
        
    for event in events:
        found = 0
        EVENT_ID = event['id']
        
        try:
            summary = event[data["tag_location"]] 
        except:
            summary = ''
        
        if summary != '':
            for color in data["color_coding"]:
                if color["tag"] in summary:
                    EVENT={'colorId': colors_dict[color["color"]]}
                    found = 1
                    break
                    
            if found != 1:
                continue
            
            service.events().patch(calendarId=CALENDER_ID, eventId=EVENT_ID, body=EVENT).execute()
            counter = counter + 1;
            
            
        else:
            continue
            
    print_result(counter)
    
if __name__ == '__main__':
    main()
