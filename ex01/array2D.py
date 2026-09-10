import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slices a 2D list"""
    try:
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("star and end must be int")
        if not isinstance(family, list) or len(family) == 0:
            raise TypeError("Input must be a list")
        if not all(isinstance(line, list) for line in family):
            raise TypeError("Input must be a list of lists")
        for line in family:
            if len(line) != len(family[0]):
                raise AssertionError("Input list with different sizes")
        arr = np.array(family)
        print(f"My shape is : {arr.shape}")
        sliced = arr[start:end]
        print(f"My new shape is : {sliced.shape}")
        return sliced.tolist()
    except (AssertionError, TypeError, IndexError) as error:
        print("Error:", error)
        return[]