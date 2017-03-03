# Sliding window
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image = mpimg.imread('bbox-example-image.jpg')

# Here is your draw_boxes function from the previous exercise
def draw_boxes(img, bboxes, color=(0, 0, 255), thick=6):
    # Make a copy of the image
    imcopy = np.copy(img)
    # Iterate through the bounding boxes
    for bbox in bboxes:
        # Draw a rectangle given bbox coordinates
        cv2.rectangle(imcopy, bbox[0], bbox[1], color, thick)
    # Return the image copy with boxes drawn
    return imcopy


# Define a function that takes an image,
# start and stop positions in both x and y,
# window size (x and y dimensions),
# and overlap fraction (for both x and y)
def slide_window(img, x_start_stop=[None, None], y_start_stop=[None, None],
                    xy_window=(64, 64), xy_overlap=(0.5, 0.5)):
    # If x and/or y start/stop positions not defined, set to image size
    if x_start_stop[0] == None:
        x_start = 0
    if x_start_stop[1] == None:
        x_end = img.shape[1]
    if y_start_stop[0] == None:
        y_start = 0
    if y_start_stop[1] == None:
        y_end = img.shape[0]
    # Compute the span of the region to be searched
    x_span = x_end - x_start
    y_span = y_end - y_start
    # Compute the number of pixels per step in x/y
    pixel_step_x = np.int(xy_window[0] * (1 - xy_overlap[0]))
    pixel_step_y = np.int(xy_window[1] * (1 - xy_overlap[1]))
    # Compute the number of windows in x/y
    x_buffer = np.int(xy_window[0]*(xy_overlap[0]))
    y_buffer = np.int(xy_window[1]*(xy_overlap[1]))
    num_win_x = np.int((x_span - x_buffer)/pixel_step_x)
    num_win_y = np.int((y_span - y_buffer)/pixel_step_y)
    # Initialize a list to append window positions to
    window_list = []
    # Loop through finding x and y window positions
    #     Note: you could vectorize this step, but in practice
    #     you'll be considering windows one by one with your
    #     classifier, so looping makes sense
        # Calculate each window position
        # Append window position to list
    # Return the list of windows
    for ys in range(num_win_y):
        for xs in range(num_win_x):
            # Calculate window position
            startx = xs * pixel_step_x + x_start
            endx = startx + xy_window[0]
            starty = ys* pixel_step_y + y_start
            endy = starty + xy_window[1]
            # Append window position to list
            window_list.append(((startx, starty), (endx, endy)))
    return window_list


def extract_feature_single(image, cspace='RGB', orient=9, pix_per_cell=8, cell_per_block=2,
                    hog_channel=0, size=(32,32), space_feat=True, color_feat=True, hog_feat=True):

    features = []
    imgage_feat = []
    image = cv2.imread(f)
    resized = utils.convert_color_and_reshape(image, color_space=cspace, size=size)
    # If I have time let's try to play around with those parameters
    if space_feat:
        spatial_features = utils.bin_spatial(resized, size=size)
        image_feat.append(spatial_features)
    if color_feat:
        color_features = utils.color_hist(resized, nbins=32)
        image_feat.append(color_features)
    if hog_feat:
        if hog_channel == -1:
            hog_features = []
            for channel in range(resized.shape[2]):
                hog_features.append(utils.get_hog_features(resized[:,:,channel],
                                    orient, pix_per_cell, cell_per_block,
                                    vis=False, feature_vec=True))
            hog_features = np.ravel(hog_features)
        else:
            hog_features = utils.get_hog_features(resized[:,:,hog_channel],
                                orient, pix_per_cell, cell_per_block,
                                vis=False, feature_vec=True)
        image_feat.append(hog_features)
    features.append(np.concatenate(image_feat))
    return features


def find_car(image, windows, clf, scaler, feat_filter):
    found_windows = []
    for win in windows:
        interesting_img = cv2.resize(image[window[0][1]:win[1,1], win[0][0]:win[1][0]])
        features = extract_feature_single(interesting_img, feat_filter)
        features_scaled = scaler.transform(np.array(features).resize(-1,1))
        prediction = clf.predict(features_scaled)
        if prdiction == 1:
            found_windows.append(win)
    return found_windows


if __name__ == '__main__':
    if os.path('model.pkl'):
        with open('model.pkl') as f:
            model, filter_mask, scaler = pickle.load(f)
    # Read video frame
    #find car...

windows = slide_window(image, x_start_stop=[None, None], y_start_stop=[None, None],
                    xy_window=(128, 128), xy_overlap=(0.5, 0.5))

window_img = draw_boxes(image, windows, color=(0, 0, 255), thick=6)
plt.imshow(window_img)
