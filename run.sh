#!/usr/bin/env bash
echo Preparing to run python webbot...
source $(pwd)/venv/bin/activate
$(pwd)/post_update.py
deactivate
