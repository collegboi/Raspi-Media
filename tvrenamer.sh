#!/bin/bash

DATE_STAMP=` date +%d-%m-%Y-%T`
echo ${DATE_STAMP}

/home/pi/filebot/opt/share/filebot/bin/filebot.sh -rename /media/usbstick/Torrent_complete/* –format “/media/usbstick/Film_rename/{n}/Season {s}/{n} – {sxe} – {t}” –db thetvdb -non-strict
