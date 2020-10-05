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
