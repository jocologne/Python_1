import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slices a 2D list"""
    try:
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("Star and end must be int")
        if not isinstance(family, list):
            raise TypeError("Input must be a list")
        for line in family:
            if len(line) != len(family[0]):
                raise AssertionError("Input list with different sizes")
        print(f"My shape is : {np.array(family).shape}")
        print(f"My new shape is : {np.array(family)[start:end+1].shape}")
        return np.array(family)[start:end].tolist()
    except AssertionError as error:
        print("Error:", error)
        return ""