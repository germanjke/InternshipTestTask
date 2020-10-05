## Test Tech Task to MIPT Machine Intelligence Laboratory (part-time job) by German Abramov

The task was to make a segmentation of cigarette butts thrown on the ground. 

**Task:** segmentation model.  
  
**Input:** photo 512x512x3

**Output:** mask of cig butt 512x512 

**Metric:** [Dice coefficient](https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient).

**Score:** [IoU](https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/).


#### For this, the organizers' basseline was used. The following functions have been added to it, wrapped in Python modules (libs folder): 
- `download_masks` for downloading masks from exist images and annotations;
- `visualize`, `visualize_losses` for visualize images and loss history;
- `Dataset` for constructing dataset;
- `get_training_augmentation`, `get_validation_augmentation`, `to_tensor`, `get_preprocessing` for augmentations by `albumentations` lib

### Results
The result is presented in a [notebook](https://github.com/germanjke/segmentation_of_cigg_butts/blob/master/cigarette_butt_segmentation/notebooks/please_dont_smoke.ipynb) (notebooks folder), as well as in an archive of photos (results folder), and as well `csv` file with predictions.

### Why this model?
A lot has been learned for segmentation, but I settled on `Unet`. If we talk about the architecture of the encoder, then I do not see any great advantage in a particular encoder for this task. For a task with multi-class segmentation, it is better to use an `efficient` network, but for a binary as such, there is no difference in the encoder. So i chose standart `resnet34`. You can check validaiton loss below:

![valloss](https://github.com/germanjke/segmentation_of_cigg_butts/blob/master/cigarette_butt_segmentation/loss_function_visuaalize/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202020-10-05%2021-45-57.png)

### Example of a result
![img](https://github.com/germanjke/segmentation_of_cigg_butts/blob/master/cigarette_butt_segmentation/results/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%D0%BE%D1%82%202020-10-05%2021-50-11.png)

### Data
I made a few changes to the data. First, I changed the extension of the validation files to jpg. Second, I did not use the built-in function to display the mask, but the already existing pictures (for this I wrote a function to download them). This was needed for my dataset structure. All data you can check [here](https://drive.google.com/drive/folders/1eYlaoGxwuzo9B0WVmLErkwtoL7Ib7XHr?usp=sharing) on my Google Disk.
