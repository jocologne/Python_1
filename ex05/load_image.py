import os
import numpy as np
from PIL import Image


def ft_load(path: str) -> list:
    """Load image from path and return as an array"""
    try:
        if not path.lower().endswith((".jpg", ".jpeg")):
            raise AssertionError("Supported formats are JPG and JPEG")
        if not os.path.exists(path):
            raise AssertionError(f"File not found: {path}")
        img = Image.open(path)
        return np.array(img)
    except AssertionError as error:
        print(f"Error: {error}")
        return []
