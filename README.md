# Raspi-Media

Raspberry pi project which uses SQLITE database to store the tv shows name, current season and episode. 
Then a crontab executes the tv shows scipt to find available episodes scrapped from website and uses transmission torrent downloader.

The Movies script is execute from php page, where you give it the name of the movie and year and scraps the magnent.

There is also a bash script which is executes from the transmission-daemon when the download is complete.

Another package is the filebot which grabs the tv shows or movies from a certain folder, and renames them properly and moves them
to where you want.

Usefull sites:

http://maximeheckel.com/blog/2013/09/01/raspberrypi-automate-download-box/
http://www.techjawab.com/2014/08/how-to-install-transmission-on.html

