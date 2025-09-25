#!/usr/bin/env bash

# For an explanation of the build system, see this notebook entry:
# https://github.com/cps-vip/cps-cosimulation-env/wiki/Kaden-McCartney's-Notebook#0922---0928

set -e

if [ ! -d "venv" ]; then
    uv venv --python 3.14 venv
fi
source venv/bin/activate

cd dnp3-module

uv pip install --verbose .

