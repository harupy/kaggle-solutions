#!/usr/bin/env bash

conda create \
  --yes --name ks-dev-env --channel conda-forge \
  --file requirements.txt --file requirements-dev.txt \
  --no-default-packages python=3.7
