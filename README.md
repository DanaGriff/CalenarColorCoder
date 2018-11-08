# Calenar Color Coder
A script that connects to your Google Calendar and color codes all the events with a given set of keywords.

## How To Use
1. Download the binary file that's compatible to your computer.
2. add the file to the startup folder. This way when the computer is turned on, the script will run periodically and update the events.
3. Go to Google Calendar, enter the settings of the calendar you wish to edit, and copy the "Calendar ID".
    You can add multiple calendars,seperated by comma, like this: ```"calender_id":"<calenadr id>,<calenadr id>"```
4. Open the ```settings.json``` file and Replace ```<calendar_id>``` with your calendar_id in the desired row. REMOVE THE ```<>```!
5. under the setting ```color_coding```, add the keyword you want the script to find, and the color you want. 
    the keyword needs to appear in the title or the description of the event in order for the event to be modified. 
    Add a new keyword like this:
    ```
    {  
         "keywords":"Some keyword",
         "color":"BOLD_RED"
    },
    ```
    You can add multiple keywords to the same color, seperated by comma. 
  
    for example:
    ```
    {     
         "keywords":"First key,Second key",
         "color":"TURQUOISE"
    },
    ```
    **Color Options**: BLUE,GREEN,PURPLE,RED,YELLOW,ORANGE,TURQUOISE,GREY,BOLD_BLUE,BOLD_GREEN,BOLD_RED
6. the script runs periodically every x seconds. the seconds are defined in the setting ```sleep_time```.

##Important info
at the first run of the script you will be prompted to a web browser to give permissions to your calendar.
none of your information will be saved anywhere.

## License
© Dana Griff
