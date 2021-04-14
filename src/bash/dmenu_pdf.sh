#! /usr/bin/env bash

# -----------------------------------------------------------------------------
# dmenu script to open a pdf in zathura
#
# It looks for all pdf files in the home directory, pipes them into dmenu, and
# opens the selected one in zathura.
# -----------------------------------------------------------------------------

pdf_file=`locate $HOME/*pdf \
    | sed -e "s#$HOME/##g" \
    | dmenu -i -l 20 -p "Which PDF?"` \
&& zathura $HOME/$pdf_file

