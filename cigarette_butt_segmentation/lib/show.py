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
    
def visualize_losses(valid_dict, model):
    """Create loss plot by dict of losses.

    Parameters
    ----------
    valid_dict : dict
    model : model
    """  

    lists_valid = valid_dict.items()
    xv, yv = zip(*lists_valid) 

    # Visualize loss history
    plt.plot(xv, yv, 'b-')
    plt.legend(['Valid Loss'])
    plt.title('Loss function', size = 18)
    plt.xlabel('Epoch', size = 16)
    plt.ylabel('Loss', size = 16)
    plt.savefig(f'/content/drive/My Drive/ciggs/model_losses/{model.name}.png')
    plt.show();
