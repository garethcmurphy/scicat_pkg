#!/usr/bin/env bash

rm -rf dist scicat.egg-info build



python3 setup.py sdist bdist_wheel

python3 -m twine upload  dist/*