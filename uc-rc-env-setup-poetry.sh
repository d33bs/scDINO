#!/bin/bash
# Used for reproducing environment on University of Colorado RC system.

# load compute node
acompile
# load python
module load python/3.10.2
# install poetry
# see: https://python-poetry.org/docs/#installation
curl -sSL https://install.python-poetry.org | python3 -
# export poetry path
export PATH="$HOME/.local/bin:$PATH"
# install poetry env
poetry install
