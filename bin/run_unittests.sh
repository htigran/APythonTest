#!/bin/bash

pushd /code/test

PYTHONPATH=/code/src python3 -m unittest TestCustoemrs.py \
                                         TestGreatCircleDistance.py

rm -fr /code/src/__pycache__
rm -fr /code/test/__pycache__

popd
