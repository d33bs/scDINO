#!/bin/bash
# Used for reproducing environment on University of Colorado RC system.

# create custom conda config
cat <<EOT >> ~/.condarc
pkgs_dirs:
  - /projects/$USER/.conda_pkgs
envs_dirs:
  - /projects/$USER/software/anaconda/envs
EOT

# load compute node
acompile
# load python
module load anaconda/2022.10
# setup alternative pip cache for storage with installs
mkdir /projects/$USER/.pipcache
export PIP_CACHE_DIR=/projects/$USER/.pipcache
# create and activate conda environment
conda env create -n scdinoenv --file conda-env-scdino.yml
conda activate scdinoenv
