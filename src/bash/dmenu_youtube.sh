#! /usr/bin/env bash

# -----------------------------------------------------------------------------
# dmenu script to play a youtube (playlist/video) in mpv.
#
# It relies on a csv file that lists youtube videos/playlists. The file has to
# be located in $HOME/multimedia/music/playlists/ and must be called
# youtube.csv. The content of the file has to look like this:
#
# title,url
# <TITLE_1>,<URL_1>
# <TITLE_2>,<URL_2>
# ...
#
# The <TITLE>s will be showen in dmenu. After selecting one the url will be
# passed to mpv.
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# constants
# -----------------------------------------------------------------------------

PLAYLIST_PATH="$HOME/multimedia/music/playlists/youtube.csv"


# -----------------------------------------------------------------------------
# actual script
# -----------------------------------------------------------------------------

playlist_name=`tail +2 $PLAYLIST_PATH \
    | cut -d ',' -f1 \
    | dmenu -i -l 20 -p "Which playlist/video"` \
&& url=`grep "$playlist_name" $PLAYLIST_PATH | cut -d ',' -f2` \
&& mpv $url

