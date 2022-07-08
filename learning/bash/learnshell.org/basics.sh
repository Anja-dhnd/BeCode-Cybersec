#!/bin/bash

echo "Hello, World!";

# VARIABLES
# Variable name is case sensitive and can consist of a combination of letters and the underscore "_".PRICE_PER_APPLE=5
MyFirstLetters=ABC
greeting='Hello        world!' 

# Encapsulating the variable name with ${} is used to avoid ambiguity

MyFirstLetters=ABC
echo "The first 10 letters in the alphabet are: ${MyFirstLetters}DEFGHIJ"

# Encapsulating the variable name with "" will preserve any white space values

greeting='Hello        world!'
echo $greeting" now with spaces: $greeting"

# Variables can be assigned with the value of a command output. This is referred to as substitution. 
# Substitution can be done by encapsulating the command with `` (known as back-ticks) or with $()

FILELIST=`ls`
FileWithTimeStamp=/tmp/my-dir/file_$(/bin/date +%Y-%m-%d).txt

# EXERCISE

# The target of this exercise is to create a string, an integer, and a complex variable using command substitution. 
# The string should be named BIRTHDATE and should contain the text "Jan 1, 2000". 
# The integer should be named Presents and should contain the number 10. 
# The complex variable should be named BIRTHDAY and should contain the full weekday name of the day 
# matching the date inariable BIRTHDATE e.g. Saturday. 
# Note that the 'date' command can be used to convert a date format into a different date format. 
# For example, to convert date value, $date1, to day of the week of date1, use

date -d "$date1" +%A

BIRTHDATE = "Jan 1, 2000"
Presents = 10
BIRTHDAY = date -d "$BIRTHDATE" +%A