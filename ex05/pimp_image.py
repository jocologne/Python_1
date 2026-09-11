
def ft_invert(array) -> list:
    """Invert image colors"""
    result = array.copy()
    for i in range(len(array)):
        for j in range(len(array[0])):
            pixel = array[i][j]
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            result[i][j] = [255 - red, 255 - green, 255 - blue]
    return result


def ft_red(array) -> list:
    """Remove blue and green from image"""
    result = array.copy()
    for i in range(len(array)):
        for j in range(len(array[0])):
            pixel = array[i][j]
            red = pixel[0]
            result[i][j] = [red, 0, 0]
    return result


def ft_green(array) -> list:
    """Remove red and blue from image"""
    result = array.copy()
    for i in range(len(array)):
        for j in range(len(array[0])):
            pixel = array[i][j]
            green = pixel[1]
            result[i][j] = [0, green, 0]
    return result


def ft_blue(array) -> list:
    """Remove red and green from image"""
    result = array.copy()
    for i in range(len(array)):
        for j in range(len(array[0])):
            pixel = array[i][j]
            blue = pixel[2]
            result[i][j] = [0, 0, blue]
    return result


def ft_grey(array) -> list:
    """Apply grey scale to image"""
    result = array.copy()
    for i in range(len(array)):
        for j in range(len(array[0])):
            pixel = array[i][j]
            result[i][j] = pixel.mean()
    return result
