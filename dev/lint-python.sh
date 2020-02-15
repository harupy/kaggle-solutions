#!/usr/bin/env bash

set -eu

flake8 --show-source tests tools
isort --check .
