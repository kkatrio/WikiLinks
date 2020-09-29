#!/usr/bin/env bash
echo Preparing to run python webbot...
source ./venv/bin/activate
./post_update.py
deactivate
