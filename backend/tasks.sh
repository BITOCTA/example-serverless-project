#!/bin/bash

# only one task at a time
if [ $# != 1 ]; then
    echo "usage: $0 <task_name>"
fi

build() {
    echo "Starting building lambda functions..."
    for lambda_function in $(ls -d api/*/); do
        echo "Building $lambda_function"
        pip3 install -r $lambda_function/requirements.txt --upgrade -t $lambda_function/lib
    done
}

case $1 in
    "build")        build;;
esac