#!/bin/bash
# Used for reproducing environment on University of Colorado RC system.

# load compute node
acompile
# install pyenv
curl https://pyenv.run | bash

# install python 3.9 through pyenv
pyenv install 3.9
# set python local global to python3.9
pyenv global 3.9

# install poetry
# see: https://python-poetry.org/docs/#installation
curl -sSL https://install.python-poetry.org | python3 -
# export poetry path
export PATH="$HOME/.local/bin:$PATH"

# set poetry cache for storage
poetry config cache-dir "/scratch/alpine/$USER/.cache/pypoetry"

# use python3.9
poetry env use python3.9

# cd to scratch space
cd /scratch/alpine/$USER

# install poetry env
poetry install

