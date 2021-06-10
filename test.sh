#!/bin/bash

int_arg=1
str_arg=cat
float_kwarg=2.3

echo "BASE HELP"
python ./base.py -h

echo
echo "DEMO HELP"
python ./demo.py -h

echo
echo "BASE RESULT"
python ./base.py ${int_arg} ${str_arg} --float_kwarg ${float_kwarg}

echo
echo "DEMO RESULT"
python ./demo.py ${int_arg} ${str_arg} --float_kwarg ${float_kwarg}
