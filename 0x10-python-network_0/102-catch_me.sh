#!/bin/bash
# Write a bash script thatm akes request to 0.0.0.0:5000/catch_me causing the 
# server response of "You got me!"
curl -sL -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
