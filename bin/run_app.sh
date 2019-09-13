#!/bin/bash

pushd /code/

PYTHONPATH=/code/src python3 src/IntercomTest.py data/customers.txt

rm -fr /code/src/__pycache__

popd


