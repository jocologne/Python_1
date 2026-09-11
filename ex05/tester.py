from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt


def main():
    img = ft_load("landscape.jpg")
    plt.imshow(ft_invert(img))
    plt.savefig("inverted.png")
    plt.imshow(ft_red(img))
    plt.savefig("red.png")
    plt.imshow(ft_green(img))
    plt.savefig("green.png")
    plt.imshow(ft_blue(img))
    plt.savefig("blue.png")
    plt.imshow(ft_grey(img))
    plt.savefig("grey.png")


if __name__ == "__main__":
    main()
