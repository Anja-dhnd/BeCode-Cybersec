#!/bin/bash
# Write a shell script checking all the groups a user is part of and 
# for each one display <username> is part of the group <group>.

for i in `groups svanna`; do
    "$LOGNAME is part of the group $i"
done
