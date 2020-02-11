#!/usr/bin/env bash

pipenv run pytest tests --verbose --color=yes --durations=0 --doctest-modules tools
