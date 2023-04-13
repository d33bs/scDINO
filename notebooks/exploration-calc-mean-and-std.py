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

# # Exploration of Existing Usecases for scDINO - Calculate Dataset Mean and STD
#
# Preparation work for scDINO existing usecases.

# +
import json
import pathlib

import numpy as np
import tifffile
import torch
import torchvision.transforms as transforms
from PIL import Image
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder
# -

# build local filepaths
data_dir = "./data"
imageset_unzipped_path = f"{data_dir}/DeepPhenotype_PBMC_ImageSet_YSeverin"
destination_mean_and_std_file = (
    f"{data_dir}/DeepPhenotype_PBMC_ImageSet_YSeverin.Test.mean_and_std.json"
)


# !python -m tifffile ./data/DeepPhenotype_PBMC_ImageSet_YSeverin/Test/Donor01/Control/B/B-0001-Test-Ctrl-E01-D01.tiff

# custom class to get around pillow limitations with reading data files
class TIFFImageFolder(ImageFolder):
    def __init__(self, root, transform=None, target_transform=None):
        super(TIFFImageFolder, self).__init__(root, transform, target_transform)

    def __getitem__(self, index):
        # Override the __getitem__ method to load TIFF images using tifffile
        path, target = self.samples[index]
        image = tifffile.imread(path)

        # Convert numpy array to PIL Image

        channels = {
            f"channel{num}": Image.fromarray(image[:, :, num]) if self.transform is None
            # Apply any necessary preprocessing using self.transform, if provided
            else self.transform(Image.fromarray(image[:, :, num]))
            for num in range(5)
        }

        return channels


# build imagefolder for parsing the images
testdata = TIFFImageFolder(
    root=f"{imageset_unzipped_path}/Test",
    transform=transforms.ToTensor(),
)
testdata

# +
# load data given the imagefolder
loader = DataLoader(testdata, batch_size=1)

# calculate the mean and std from loader
data = next(iter(loader))
mean_and_std_dict = {
    "mean": tuple(
        [np.mean(data[f"channel{num}"].view(-1).numpy()) for num in range(5)]
    ),
    "std": tuple([np.std(data[f"channel{num}"].view(-1).numpy()) for num in range(5)]),
}
mean_and_std_dict
# -

# write data to json file
with open(destination_mean_and_std_file, "w") as file:
    file.write(json.dumps(mean_and_std_dict))
