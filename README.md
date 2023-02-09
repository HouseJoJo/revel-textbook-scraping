<h2>Revel Textbook Scraping Script</h2>

Requires: Gecko Driver(firefox), pandas, & selenium python libraries.

Description: With appropriate login credentials, this script is able to use an automated browser to collect textbook data from the online source Revel. The data is exported to "table.csv" and converted to "output.txt" in a readable format.
Page titles, subheadings and all paragraph data is retrieved.

Usage: To run program, run "app.py" in a terminal and follow prompted instructions. Resulting files will appear in same directory as "app.py"

Note: The navigation part of the program was written in context to an account with only one textbook (Revel Connections: A World History, Volume 1, 4e).
Once in the content page, the data collection portion of the program should be applicable to any textbook.
Warning: Due to the nature of Selenium and having to navigate through every single web page of the online textbook, data collection can take upwards of 40 minutes. Trying to collect the data for an entire textbook through one iteration of the program is prone to server timeouts. It is recommended to collect textbook data in pieces when it is needed.

# Demonstration
![](https://github.com/HouseJoJo/revel-textbook-scraping/blob/main/media/peekCS40Z1.gif)

Note: The gif was edited down to a ~1.5 minute demonstration. The actual process displayed took ~20 minutes (For 10 chapters worth of data).
