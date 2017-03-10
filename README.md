##Writeup Template
###You can use this file as a template for your writeup if you want to submit it as a markdown file, but feel free to use some other method and submit a pdf if you prefer.

---

**Vehicle Detection Project**

The goals / steps of this project are the following:

* Perform a Histogram of Oriented Gradients (HOG) feature extraction on a labeled training set of images and train a classifier Linear SVM classifier
* Optionally, you can also apply a color transform and append binned color features, as well as histograms of color, to your HOG feature vector.
* Note: for those first two steps don't forget to normalize your features and randomize a selection for training and testing.
* Implement a sliding-window technique and use your trained classifier to search for vehicles in images.
* Run your pipeline on a video stream (start with the test_video.mp4 and later implement on full project_video.mp4) and create a heat map of recurring detections frame by frame to reject outliers and follow detected vehicles.
* Estimate a bounding box for vehicles detected.

[//]: # (Image References)
[image1]: ./output_images/1902.png
[image2]: ./output_images/hog_1902.png
[image3]: ./output_images/extra1902.png
[image4]: ./output_images/hog_extra1902.png
[image5]: ./output_images/feature_importances_2.png
[image6]: ./output_images/search_area.png
[image7]: ./output_images/car_and_hog.jpg
[image8]: ./output_images/detected.png
[image9]: ./output_images/detected_2.png
[image10]: ./output_images/detected_3.png
[image11]: ./output_images/heatmap.png
[image12]: ./output_images/heatmap_2.png
[image13]: ./output_images/total_heatmap.png
[image14]: ./output_images/result.png



[video1]: ./project_video_out.mp4


## [Rubric](https://review.udacity.com/#!/rubrics/513/view) Points
### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---
### Histogram of Oriented Gradients (HOG)

#### 1. Explain how (and identify where in your code) you extracted HOG features from the training images.
I extracted the HOG gradient using the code developed during the lessons.
For every image the scikit image library hog function is called.
In order to choose the parameter for the hog,(i.e. orient, pix_per_cell, cell_per_block)
I performed a grid search training several SVM classifier and choosing the one with the
best performance.
Here is an example using the `HLS` color space and HOG parameters of `orientations=9`, `pixels_per_cell=(8, 8)` and `cells_per_block=(2, 2)`:

Car image

![alt text][image1]

Hog feature for L channel of Car image

![alt text][image2]

Non car image

![alt text][image3]

Hog feature for L channel of non car image

![alt text][image4]


#### 2. Explain how you settled on your final choice of HOG parameters.
In order to decide which hog parameters works the best I decided to perfom a grid search
(the code for the grid search is in the `grid_search` function inside the `classifier.py` file
training different linear SVM classifier and the parameter that performed best were:

`colorspace=YCrcb`
`orientation=9`
`pixels_per_cell=(8, 8)`
`cells_per_block=(2, 2)`

#### 3. Describe how (and identify where in your code) you trained a classifier using your selected HOG features (and color features if you used them).

I trained a linear SVM using the model selection function GridSearchCv provided
by the scikit learn library.
The tuned parameter was the C parameter of the classifier where I tried values 1, 10, 100.
In order to augment the data set used for the trained I used the udacity data set
cropping the car images following the annotation included and for every image in the training set I
filled it vertically in order to have a bigger training set.
Beside the udacity data set I used the KITTI_extracted dataset and the Extra data set as training set.

As a test set I used the GTI* data set.
Before training the classifier the number of car and non car examples were equalized for the training
set and the exceeding elements were added to the training set.

The grid search is in the `classify` function inside the `classifier.py` file.

#### Here's a snippet of the grid search output

    Data summary:
    We have  11955  not car images and  11955  car images and the ratio is  1.0
    Testing set: We have  5899  not car images and  5966  car images and the ratio is  0.988769694937982
    Using colorspace: HLS  orientations: 9  pixels per cell: 8  cell_per_block: 2 hog_channel: -1
    /home/seba/Projects/Private/scikit-image/skimage/feature/_hog.py:119: skimage_deprecation: Default value of `block_norm`==`L1` is deprecated and will be changed to `L2-Hys` in v0.15
      'be changed to `L2-Hys` in v0.15', skimage_deprecation)
    224.72 Seconds to extract HOG features...for training set
    58.52 Seconds to extract HOG features...for testing set
    We have  47820  training samples and train Feature vector length: 8460
    We have  11865  test samples and test Feature vector length: 8460
    After selecting feature we have  (47820, 1508)
    Starting a SVM grid search
    ........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................
    optimization finished, #iter = 10000

    WARNING: reaching max number of iterations
    Using -s 2 may be faster (also see FAQ)

    Objective value = -6084.402680
    nSV = 10936
    /usr/lib64/python3.4/site-packages/sklearn/svm/base.py:920: ConvergenceWarning: Liblinear failed to converge, increase the number of iterations.
      "the number of iterations.", ConvergenceWarning)
    [LibLinear]1556.2 Seconds to Grid search SVC...
    Test Accuracy of SVC =  0.8172  f1 score =  0.8421  precision =  0.7444  recall =  0.9692
    Using colorspace: YCrCb  orientations: 9  pixels per cell: 8  cell_per_block: 2 hog_channel: -1
    /home/seba/Projects/Private/scikit-image/skimage/feature/_hog.py:119: skimage_deprecation: Default value of `block_norm`==`L1` is deprecated and will be changed to `L2-Hys` in v0.15
      'be changed to `L2-Hys` in v0.15', skimage_deprecation)
    815.79 Seconds to extract HOG features...for training set
    228.78 Seconds to extract HOG features...for testing set
    We have  47820  training samples and train Feature vector length: 8460
    We have  11865  test samples and test Feature vector length: 8460
    After selecting feature we have  (47820, 1609)
    Starting a SVM grid search
    ........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................
    optimization finished, #iter = 10000

    WARNING: reaching max number of iterations
    Using -s 2 may be faster (also see FAQ)

    Objective value = -5700.099888
    nSV = 10291
    /usr/lib64/python3.4/site-packages/sklearn/svm/base.py:920: ConvergenceWarning: Liblinear failed to converge, increase the number of iterations.
      "the number of iterations.", ConvergenceWarning)
    [LibLinear]1569.8 Seconds to Grid search SVC...
    Test Accuracy of SVC =  0.7388  f1 score =  0.784  precision =  0.671  recall =  0.9428


And so then I decided to use ONLY the GTI and KTTI data to fit the model
(also doing a grid search). I Always augmented the data using the flipping technique

    Data summary:
    We have  8968  not car images and  8792  car images and the ratio is  1.0200181983621475
    Using colorspace: HLS  orientations: 9  pixels per cell: 8  cell_per_block: 2 hog_channel: -1
    /home/seba/Projects/Private/scikit-image/skimage/feature/_hog.py:119: skimage_deprecation: Default value of `block_norm`==`L1` is deprecated and will be changed to `L2-Hys` in v0.15
      'be changed to `L2-Hys` in v0.15', skimage_deprecation)
    461.41 Seconds to extract HOG features...for training set
    We have  37296  training samples and train Feature vector length: 8460
    We have  15984  test samples and test Feature vector length: 8460
    After selecting feature we have  (37296, 1303)
    Starting a SVM grid search
    ........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................
    optimization finished, #iter = 10000

    WARNING: reaching max number of iterations
    Using -s 2 may be faster (also see FAQ)

    Objective value = -374.613339
    nSV = 1324
    /usr/lib64/python3.4/site-packages/sklearn/svm/base.py:920: ConvergenceWarning: Liblinear failed to converge, increase the number of iterations.
      "the number of iterations.", ConvergenceWarning)
    [LibLinear]146.97 Seconds to Grid search SVC...
    Test Accuracy of SVC =  0.9746  f1 score =  0.9743  precision =  0.9732  recall =  0.9754

    Using colorspace: HSV  orientations: 9  pixels per cell: 8  cell_per_block: 2 hog_channel: -1
    /home/seba/Projects/Private/scikit-image/skimage/feature/_hog.py:119: skimage_deprecation: Default value of `block_norm`==`L1` is deprecated and will be changed to `L2-Hys` in v0.15
      'be changed to `L2-Hys` in v0.15', skimage_deprecation)
    332.61 Seconds to extract HOG features...for training set
    We have  37296  training samples and train Feature vector length: 8460
    We have  15984  test samples and test Feature vector length: 8460
    After selecting feature we have  (37296, 1351)
    Starting a SVM grid search
    ........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................
    optimization finished, #iter = 10000

    WARNING: reaching max number of iterations
    Using -s 2 may be faster (also see FAQ)

    Objective value = -121.404891
    nSV = 1175
    /usr/lib64/python3.4/site-packages/sklearn/svm/base.py:920: ConvergenceWarning: Liblinear failed to converge, increase the number of iterations.
      "the number of iterations.", ConvergenceWarning)
    [LibLinear]118.24 Seconds to Grid search SVC...
    Test Accuracy of SVC =  0.978  f1 score =  0.9778  precision =  0.9806  recall =  0.975

    Using colorspace: YCrCb  orientations: 9  pixels per cell: 8  cell_per_block: 2 hog_channel: -1
    /home/seba/Projects/Private/scikit-image/skimage/feature/_hog.py:119: skimage_deprecation: Default value of `block_norm`==`L1` is deprecated and will be changed to `L2-Hys` in v0.15
      'be changed to `L2-Hys` in v0.15', skimage_deprecation)
    661.23 Seconds to extract HOG features...for training set
    We have  37296  training samples and train Feature vector length: 8460
    We have  15984  test samples and test Feature vector length: 8460
    After selecting feature we have  (37296, 1363)
    Starting a SVM grid search
    ................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................*........................................................................................................................................
    optimization finished, #iter = 10000

    WARNING: reaching max number of iterations
    Using -s 2 may be faster (also see FAQ)

    Objective value = -53.637501
    nSV = 999
    /usr/lib64/python3.4/site-packages/sklearn/svm/base.py:920: ConvergenceWarning: Liblinear failed to converge, increase the number of iterations.
      "the number of iterations.", ConvergenceWarning)
    [LibLinear]98.87 Seconds to Grid search SVC...
    Test Accuracy of SVC =  0.983  f1 score =  0.9829  precision =  0.9844  recall =  0.9815


### Snippet of the used data and grid Search

In order to reduce the number of feature a feature selection was performed
training a forest of decision tree and then filtering the features using the
feature_importances_ parameter of the ExtraTreesClassifier provided by scikit-learn
The feature selection code is inside `classify` function. I selected the feature
whose importance is bigger then the average value of the importances

![alt text][image5]

So I reduced the number of feature used, speeding up the classifier without
loosing much in accuracy


### Sliding Window Search

#### 1. Describe how (and identify where in your code) you implemented a sliding window search.  How did you decide what scales to search and how much to overlap windows?

The sliding window implementation is the one found during the lesson.
The scale and the overlap was decided extracting some frames from the test_video
and trying to identify cars in there.
I also reduced the space where the image is searched as is useless to search for
cars in the sky or over the horizon line.

Search area

![alt text][image6]


#### 2. Show some examples of test images to demonstrate how your pipeline is working.  What did you do to optimize the performance of your classifier?

I searched on two scales using YCrCb 3-channel HOG features plus spatially binned color and histograms of color in the feature vector, which provided a nice result even if
some false positives are still present. Probably doing more grid search and selecting better training and test frame can lead to better performances.

Here are some example images:

Detected cars (with false positive)

![alt text][image8]

Detected cars

![alt text][image9]

---

### Video Implementation

#### 1. Provide a link to your final video output.  Your pipeline should perform reasonably well on the entire project video (somewhat wobbly or unstable bounding boxes are ok as long as you are identifying the vehicles most of the time with minimal false positives.)

Here's a [link to my video result](./project_video.mp4)


#### 2. Describe how (and identify where in your code) you implemented some kind of filter for false positives and some method for combining overlapping bounding boxes.

I recorded the positions of positive detections in each frame of the video.  From the positive detections I created a heatmap and then thresholded that map to identify vehicle positions.  I then used `scipy.ndimage.measurements.label()` to identify individual blobs in the heatmap.  I then assumed each blob corresponded to a vehicle.  I constructed bounding boxes to cover the area of each blob detected.  
I integrated the last 30 heatmaps keeping them in a circular buffer. These maps are summed and then thresholded in order to keep points that continue to have a positive match throughout different frames. If no car were successfully detected previous frame was
used.
This prevent frame to disappear in 30 frames :)

Here's an example result showing the heatmap from a series of frames of video, the result of `scipy.ndimage.measurements.label()` and the bounding boxes then overlaid on the last frame of video:


### Here some frames and their corresponding heatmaps:

#### Frame 1

![alt text][image8]
![alt text][image11]

#### Frame 2

![alt text][image9]
![alt text][image12]



### Here is the output of `scipy.ndimage.measurements.label()` on the integrated heatmap from previous frames:

#### Integrated heatmap

![alt text][image13]

### Here the resulting bounding boxes are drawn onto the last frame in the series:
![alt text][image14]



---

### Discussion

#### 1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

My implemntation is far from be perfect.
Sometimes cars are not detected and still lots of false positive are present.
I think the classifier is still the weakest point in this implementation.
- Lot of work can be done to increase the performances. (grid search, augment dataset,
get rid of fimeframes inside the current dataset)
- More work can also be done on the bounding boxes in order to better fit the
corrisponding detected object.
- Speed also is a problem...but with a more precise classifier the overlap between
windows can be increased hence resulting in less windows to search and more speed.
- I could not succeeded in fitting a good model using also udacity data...
  model accuracy was always too low and lot of false negatives..so probably in
  this case is better a model that overfits a bit and then using filtering
  of false positives a lot
