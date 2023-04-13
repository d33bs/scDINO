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

# cd to scratch space
cd /scratch/alpine/$USER

# update pip
python -m pip install --upgrade pip

# install virtualenv 
python -m pip install virtualenv
python -m virtualenv scdinoenv
source scdinoenv/bin/activate
pip install -r requirements.txt

