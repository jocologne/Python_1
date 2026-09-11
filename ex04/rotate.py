from load_image import ft_load_zoom
import matplotlib.pyplot as plt
import numpy as np


def main():
    try:
        img = ft_load_zoom("animal.jpeg")
        height = img.shape[0]
        width = img.shape[1]
        transposed = [[0] * height for _ in range(width)]
        for i in range(height):
            for j in range(width):
                transposed[j][i] = img[i][j]
        print(f"New shape after Transpose: ({width}, {height})")
        print(np.array(transposed))
        plt.imshow(np.array(transposed))
        plt.savefig("rotated.png")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
