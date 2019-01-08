#!/usr/bin/fish
echo Preparing to run python webbot...
source nbot27/bin/activate.fish
python post_update.py
deactivate
