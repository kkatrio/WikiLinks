#!/usr/bin/fish
echo Preparing to run python webbot...
source /home/kon/webbot/nbot27/bin/activate.fish
/home/kon/webbot/post_update.py
deactivate
