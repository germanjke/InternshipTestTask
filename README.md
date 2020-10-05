### Test Tech Task to MIPT Machine Intelligence Laboratory (part-time job) by German Abramov

The task was to make a segmentation of cigarette butts thrown on the ground. 

**Need to do:** segmentation model.  
  
**Input:** photo 512x512x3.

**Output:** mask of cig butt 512x512. 

**Metric:** [Dice coefficient](https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient).

**Score:** [IoU](https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/).


### For this, the organizers' basseline was used. The following functions have been added to it, wrapped in Python modules (libs folder): 
- `download_masks` for downloading masks from exist images and annotations;
- `visualize`, `visualize_losses` for visualize images and loss history;
- `Dataset` for constructing dataset;
- `get_training_augmentation`, `get_validation_augmentation`, `to_tensor`, `get_preprocessing` for augmentations by `albumentations` lib

### Results:
The result is presented in a laptop (notebooks folder), as well as in an archive of photos (results folder)

### Why this model?:

### Example of a result:

### Data:
I made a few changes to the data. First, I changed the extension of the validation files to jpg. Second, I did not use the built-in function to display the mask, but the already existing pictures (for this I wrote a function to download them). This was needed for my dataset structure. All data you can check [here]() on my Google Disk.
