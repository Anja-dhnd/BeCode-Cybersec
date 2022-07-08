#!/bin/bash


PS3='Hi! Choose your option:'

options=("Date" "Calculator" "Jokes" "Quit") 
select option in "${options[@]}"; do 
    case $option in 
        "Date")
        echo "Current date is $(date)"
        ;;
        "Calculator")
        set a b operation;
        echo -e "Select operation type: + - * /";
        read -r operation;
        echo "a=";
        read -r a;
        echo "b=";
        read -r b;

        echo "Result:" $(($a$operation$b));
        ;;
        "Jokes")
        COLOR='\033[0;32m' 
        JOKE=$(curl -s 'http://api.icndb.com/jokes/random' | python3 -c "import sys, json; print(json.load(sys.stdin)['value']['joke'])")
        printf "${COLOR}$JOKE%s\n"
        ;;
        "Quit")
	    echo "User requested exit"
	    exit
	    ;;
        *) echo "invalid option $REPLY";;
    esac
done