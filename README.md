# Calenar Color Coder
A script that connects to your Google Calendar and color codes all the events with a given set of keywords.

## How To Use
1. Download the Release fiels.
2. Schedule the exe in Windows Scheduler.
3. Go to Google Calendar, enter the settings of the calendar you wish to edit, and copy the "Calendar ID".
    You can add multiple calendars,seperated by comma, like this: ```"calender_ids": ["<calendar id>", "<calendar id>"]```
4. Open the ```settings.json``` file and Replace ```<calendar_id>``` with your calendar id in the desired row. REMOVE THE ```<>```!
5. under the setting ```color_coding```, add the keyword you want the script to find, and the color you want. 
    the keyword needs to appear in the title or the description of the event in order for the event to be modified. 
    Add a new keyword like this:
    ```
    {  
         "keywords": ["Some keyword"],
         "color":"Tomato"
    },
    ```
    You can add multiple keywords to the same color, seperated by comma. 
  
    for example:
    ```
    {     
         "keywords": ["First key", "Second key"],
         "color":"Tangerine"
    },
    ```
    **Color Options**: Lavender, Sage, Grape, Flamingo, Banana, Tangerine, Peacock, Graphite, Basil, Blueberry, Tomato
5. Generate a Credentials JSON File from the Google Calendar API:

    a. Enter https://console.developers.google.com/?pli=1

    b. Create a New Project

    c. Enable API And Services 

    d. Search for Google Calendar API and enable it.

    e. o to Credentials -> Create Credentials -> OAuth Client ID -> Other

    f. Download the file and put in the same folder as the script.

6. Run the script manually once, at the first run of the script you will be prompted to a web browser to give permissions to your calendar. none of your information will be saved anywhere.


© Dana Griff
