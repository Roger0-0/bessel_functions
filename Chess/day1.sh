#!/bin/bash
INPUT=input.txt
TotalLines=$(wc -l < $INPUT)
main(){
    LineCount=1
    myList=()
    while read i ; do
        if [ -z $i ];then
            myList+=($cals)
            cals=0
        else
            cals=$(( $cals + $i ))
            if [[ $LineCount -eq $TotalLines ]];then
                myList+=($cals)
            fi
        fi
        if [[ $cals -gt $most_cals ]];then
            most_cals=$cals
        fi
        LineCount=$(( $LineCount + 1 ))
    done < $INPUT
    second_most_cals=$(printf "%s\n" ${myList[@]} | sort -rn | sed -e "2!d")
    third_most_cals=$(printf "%s\n" ${myList[@]} | sort -rn | sed -e "3!d")
    top3=$(( $most_cals + $second_most_cals + $third_most_cals ))
    echo "Answer to part 1 is : $most_cals"
    echo "Answer to part 2 is : $top3" 
}
main