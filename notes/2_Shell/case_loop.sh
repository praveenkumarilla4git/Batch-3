#!/bin/bash

read -p "Enter a duration (day/night):" duration

case $duration in
        day)
                echo "Go to Work!"
                ;;
        night)
                echo "Go to Sleep"
                ;;
        *)
                echo "Invalid entry"
esac
