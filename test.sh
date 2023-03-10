#!/bin/bash

set -e

cleanup() {
    rm -f base.log demo.log
}
trap cleanup EXIT

int_arg=1
str_arg=cat
float_kwarg=2.3

python ./base.py -h > base.log
python ./demo.py -h > demo.log
diff base.log demo.log
if [ $? != 0 ]; then
    echo "Help comparison failed"
    exit 1
fi

python ./base.py ${int_arg} ${str_arg} --float_kwarg ${float_kwarg} > base.log
python ./demo.py ${int_arg} ${str_arg} --float_kwarg ${float_kwarg} > demo.log
diff base.log demo.log
if [ $? != 0 ]; then
    echo "Result comparison failed"
    exit 1
fi

echo "All tests passed"