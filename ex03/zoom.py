from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    """Display info and zoom in image"""
    try:
        img = ft_load("animal.jpeg")
        print(img)
        h = img.shape[0]
        w = img.shape[1]
        zoomed = img[h // 4: h // 4 + 400, w // 4: w // 4 + 400]
        print(f"New shape after slicing: {zoomed.shape}")
        plt.imshow(zoomed.squeeze())
        plt.savefig("zoomed.png")
        print(np.array(zoomed))
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
