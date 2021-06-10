#!/bin/bash

int_arg=1
str_arg=cat
float_kwarg=2.3

echo "REFERENCE HELP"
python ./reference.py -h

echo
echo "DEMO HELP"
python ./demo.py -h

echo
echo "REFERENCE RESULT"
python ./reference.py ${int_arg} ${str_arg} --float_kwarg ${float_kwarg}

echo
echo "DEMO RESULT"
python ./demo.py ${int_arg} ${str_arg} --float_kwarg ${float_kwarg}
