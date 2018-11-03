"""
    TODO: ADD CODE DESCRIPTION
"""
import json
import sys
import os
import datetime
import time

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file as my_file
from oauth2client import client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'
COLORS = {'BLUE' : 1,
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

def color_event(event, data, service, calendar_id):
    found = False
    event_id = event['id']
    counter = 0
    summary_and_description = event.get('summary', '') + event.get('description', '')
    
    if summary_and_description:
        for color in data["color_coding"]:
            keywords = color["keywords"].split(",")
            if filter(lambda x: x in summary_and_description,keywords):
                modified_event = {'colorId': COLORS[color["color"]]}
                found = True
                break
                
        if found:
            service.events().patch(calendarId=calendar_id, 
                                   eventId=event_id, 
                                   body=modified_event).execute()
            counter += 1
    return counter


def print_result(counter):
    if counter == 0:
        print 'no events were updated'
    elif counter == 1:
        print 'One event was updated successfully!'
    else:
        print '{0} {1}'.format(counter, 'Events were updated successfully!')

        
def full_path(file_name):
    dir_path = os.path.dirname(__file__)
    return os.path.join(dir_path, file_name)

    
def retrieve_settings():
    with open(full_path('settings.json')) as settings_file:
        try:
            json_data = json.load(settings_file)
            return json_data
        except ValueError:
            print 'The JSON File is corrupted, modify the file and re-run the script'
            sys.exit()

            
def calendar_service():
    store = my_file.Storage(full_path('token.json'))
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(full_path('credentials.json'), SCOPES)
        creds = tools.run_flow(flow, store)
    return build('calendar',
                 'v3',
                 http=creds.authorize(Http()))
    
    
def main(data):
    calendar_id = data["calender_id"]
    
    service = calendar_service()
    
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    
    events_result = service.events().list(calendarId=calendar_id, 
                                          timeMin=now,
                                          maxResults=200, 
                                          singleEvents=True,
                                          orderBy='startTime').execute()
                                        
    events = events_result.get('items', [])
    
    counter = 0
    if not events:
        print 'No upcoming events found.'
        sys.exit()

    for event in events:
        counter += color_event(event, data, service, calendar_id)

    print_result(counter)


if __name__ == '__main__':
    data = retrieve_settings()
    while True:
        main(data)
        time.sleep(data["sleep_time"])
