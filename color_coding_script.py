"""
    TODO: ADD CODE DESCRIPTION
"""
from __future__ import print_function
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
COLORS = {'Lavender' : 1,
          'Sage' : 2,
          'Grape' : 3,
          'Flamingo' : 4,
          'Banana' : 5,
          'Tangerine' : 6,
          'Peacock' : 7,
          'Graphite' : 8,
          'Blueberry' : 9,
          'Basil' : 10,
          'Tomato' : 11}
COLOR_OPTIONS = list(COLORS.keys());

def color_event(event, data, service, calendar_id):
    found = False
    event_id = event['id']
    counter = 0
    summary_and_description = event.get('summary', '') + event.get('description', '')

    if summary_and_description:
        for color in data["color_coding"]:
            keywords = color["keywords"]
            if filter(lambda x: x.lower() in summary_and_description.lower(),keywords):
                if color["color"] in COLOR_OPTIONS:
                    modified_event = {'colorId': COLORS[color["color"]]}
                    found = True
                else:
                    print("{0} '{1}'. {2}".format("The JSON File contains a color that doesn't exist:", color["color"],"Please fix the JSON."))
                    sys.exit()
                break

        if found:
            service.events().patch(calendarId=calendar_id,
                                   eventId=event_id,
                                   body=modified_event).execute()
            counter += 1
    return counter


def print_result(counter):
    if counter == 0:
        print('no events were updated')
    elif counter == 1:
        print('One event was updated successfully!')
    else:
        print('{0} {1}'.format(counter, 'Events were updated successfully!'))


def full_path(file_name):
    if getattr( sys, 'frozen', False ): # running in a bundle
        dir_path = os.path.dirname(sys.executable)
        return os.path.join(dir_path, file_name)
    else : # running live
        dir_path = os.path.dirname(__file__)
        return os.path.join(dir_path, file_name)


def retrieve_settings():
    with open(full_path('settings.json')) as settings_file:
        try:
            json_data = json.load(settings_file)
            return json_data
        except ValueError:
            print('The JSON File is corrupted, modify the setting file and re-run the script')
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

    counter = 0

    try:
        calendar_ids = data["calender_ids"]
    except KeyError:
        print('The calendar id setting is missing, modify the setting file and re-run the script')
        sys.exit()

    if calendar_ids[0] == '':
        print('The calendar id is empty, modify the setting file and re-run the script')
        sys.exit()

    for calendar_id in calendar_ids:
        service = calendar_service()

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

        try:
            events_result = service.events().list(calendarId=calendar_id,
                                              timeMin=now,
                                              maxResults=200,
                                              singleEvents=True,
                                              orderBy='startTime').execute()
        except:
            print('This calendar does not exist, modify the setting file and re-run the script')
            sys.exit()

        events = events_result.get('items', [])


        if not events:
            print('{0} {1}'.format('No upcoming events found for ', calendar_id))

        for event in events:
            counter += color_event(event, data, service, calendar_id)

    print_result(counter)

if __name__ == '__main__':
    data = retrieve_settings()
    main(data)
