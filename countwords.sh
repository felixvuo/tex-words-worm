#!/bin/bash
PROG="progress.csv"
WORDS=`texcount -total *tex | grep "Words in text" | grep -oE '[0-9]+'`
DATE=`date -I`

# we're going to overwrite any previous entry for today
sed -i "/${DATE}/d" $PROG

echo "${DATE},${WORDS}" >> $PROG

