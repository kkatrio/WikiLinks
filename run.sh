#!/usr/bin/env bash
echo Preparing to run python webbot...
source /home/kon/webbot/venv/bin/activate
/home/kon/webbot/post_update.py
deactivate
