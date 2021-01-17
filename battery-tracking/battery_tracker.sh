#!/bin/sh

echo "--------------------------------------------------------------------------------------------------------"
echo "`date` Starting program.."
BASEDIR=$(dirname $0)
export PATH=/usr/local/bin:$PATH
export DISPLAY=:0
echo "`date` Sleeping to some time to let the display get ready"
sleep 120
echo "`date` launching battery tracker.."
cd $BASEDIR
pwd

pipenv run python battery_tracker.py
