import matplotlib.pyplot as plt


def show_img_with_mask(img, mask, figsize=(14, 8)):
    """Shows image and mask.

    Parameters
    ----------
    img : np.ndarray
        Image.
    mask : np.ndarray
        Mask.
    figsize : tuple of 2 int, optional (default=(14, 8))
        Figure size.

    """
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=figsize)
    ax1.imshow(img)
    ax2.imshow(mask)
    ax1.axis("off")
    ax2.axis("off")
    plt.show()

# helper function for data visualization
def visualize(**images):
    """PLot images in one row."""
    n = len(images)
    plt.figure(figsize=(16, 5))
    for i, (name, image) in enumerate(images.items()):
        plt.subplot(1, n, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.title(' '.join(name.split('_')).title())
        plt.imshow(image)
    plt.show()
