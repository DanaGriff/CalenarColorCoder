# Calenar Color Coder
A script that connects to your Google Calendar and color codes all the events with a given set of keywords.

## How To Use
1. Download the binary file that's compatible to your computer.
2. add the file to the startup folder. This way when the computer is turned on, the script will run periodically and update the events.
3. Go to Google Calendar, enter the settings of the calendar you wish to edit, and copy the "Calendar ID".
4. Open the settings.json file and paste your calendar_id in the desired row.
5. under the setting "color_coding", add the keyword you want the script to find, and the color you want. 
    the keyword needs to appear in the title or the description of the event. see examples in the file.
    Optional Colors: BLUE,GREEN,PURPLE,RED,YELLOW,ORANGE,TURQUOISE,GREY,BOLD_BLUE,BOLD_GREEN,BOLD_RED
6. the script runs periodically every x seconds. the seconds are defined in the setting "sleep_time".

## License
© Dana Griff
