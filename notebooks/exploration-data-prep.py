# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Exploration of Existing Usecases for scDINO - Data Preparations
#
# Preparation work for scDINO existing usecases.

# +
import pathlib
import shutil
import zipfile

import requests

# +
# data directory work
data_dir = "./data"

# build actual directory if it doesn't exist
pathlib.Path(data_dir).mkdir(exist_ok=True)

# +
# url reference for:
# pre-trained vit for single immune cells
# https://www.research-collection.ethz.ch/handle/20.500.11850/582208
vit_url = (
    "https://www.research-collection.ethz.ch"
    "/bitstream/handle/20.500.11850/582208/"
    "sc-ViT_checkpoint0100_vitsmall16.pth?sequence=4&isAllowed=y"
)
# url reference for:
# imageset for example work
# https://www.research-collection.ethz.ch/handle/20.500.11850/343106
imageset_url = (
    "https://www.research-collection.ethz.ch"
    "/bitstream/handle/20.500.11850/343106/"
    "DeepPhenotype_PBMC_ImageSet_YSeverin.zip?sequence=5&isAllowed=y"
)

# build local filepaths
vit_filename = pathlib.Path(vit_url).name.split("?")[0]
imageset_filename = pathlib.Path(imageset_url).name.split("?")[0]

vit_filepath = f"{data_dir}/{vit_filename}"
imageset_filepath = f"{data_dir}/{imageset_filename}"
imageset_unzipped_path = f"{data_dir}/{imageset_filename.rstrip('.zip')}"

# +
# download vit
if not pathlib.Path(vit_filepath).is_file():
    response = requests.get(vit_url, stream=True)

    with open(vit_filepath, "wb") as out_file:
        shutil.copyfileobj(response.raw, out_file)

# download imageset
if not pathlib.Path(imageset_filepath).is_file():
    response = requests.get(imageset_url, stream=True)

    with open(imageset_filepath, "wb") as out_file:
        shutil.copyfileobj(response.raw, out_file)
# -

# unzip the imageset
if not pathlib.Path(imageset_unzipped_path).is_dir():
    with zipfile.ZipFile(imageset_filepath, "r") as zipped:
        zipped.extractall(data_dir)
