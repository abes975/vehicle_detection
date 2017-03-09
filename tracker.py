# Sliding window
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.ndimage.measurements import label
import pickle
import os.path
import glob
import utils
from moviepy.editor import VideoFileClip

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


def extract_feature_single(image, cspace='YcrCb', orient=9, pix_per_cell=8, cell_per_block=2,
                    hog_channel=-1, size=(32,32), space_feat=True, color_feat=True, hog_feat=True):
    features = []
    imgage_feat = []
    image = cv2.imread(f)
    resized = utils.convert_color(image, color_space=cspace)
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


# def find_car(image, windows, clf, scaler, feat_filter):
#     found_windows = []
#     for win in windows:
#         interesting_img = cv2.resize(image[window[0][1]:win[1,1], win[0][0]:win[1][0]])
#         features = extract_feature_single(interesting_img)
#         features_scaled = scaler.transform(np.array(features).resize(-1,1))[:,feat_filter]
#         prediction = clf.predict(features_scaled)
#         if prdiction == 1:
#             found_windows.append(win)
#     return found_windows


# Define a single function that can extract features using hog sub-sampling and make predictions
def find_cars(img, ystart, ystop, scale, clf, X_scaler, feature_filter, orient=9,
                pix_per_cell=8, cell_per_block=2, hist_bins=32, spatial_size=(32,32)):
    heatmap = np.zeros_like(img[:,:,0])
    img_boxes = []
    draw_img = np.copy(img)
    img = img.astype(np.float32)/255

    img_tosearch = img[ystart:ystop,:,:]
    ctrans_tosearch = utils.convert_color(img_tosearch, color_space='YCrCb')
    ctrans_tosearch = ctrans_tosearch.astype(np.float32)/255
    if scale != 1:
        imshape = ctrans_tosearch.shape
        new_size = (np.int(imshape[1]/scale), np.int(imshape[0]/scale))
        ctrans_tosearch = cv2.resize(ctrans_tosearch, new_size)
    # cv2.imshow("Search space", ctrans_tosearch)
    # cv2.waitKey(0)
    ch1 = ctrans_tosearch[:,:,0]
    ch2 = ctrans_tosearch[:,:,1]
    ch3 = ctrans_tosearch[:,:,2]

    # Define blocks and steps as above
    nxblocks = (ch1.shape[1] // pix_per_cell)-1
    nyblocks = (ch1.shape[0] // pix_per_cell)-1
    nfeat_per_block = orient*cell_per_block**2
    # 64 was the orginal sampling rate, with 8 cells and 8 pix per cell
    window = 64
    nblocks_per_window = (window // pix_per_cell)-1
    cells_per_step = 1  # Instead of overlap, define how many cells to step
    nxsteps = (nxblocks - nblocks_per_window) // cells_per_step
    nysteps = (nyblocks - nblocks_per_window) // cells_per_step
    if nxsteps == 0 or nysteps == 0:
        print("The used scale is too small...we cannot fit even a single window")
    #print("MA xke tu non funzioni", nxsteps, " ", nysteps)
    # Compute individual channel HOG features for the entire image
    hog1 = utils.get_hog_features(ch1, orient, pix_per_cell, cell_per_block, feature_vec=False)
    hog2 = utils.get_hog_features(ch2, orient, pix_per_cell, cell_per_block, feature_vec=False)
    hog3 = utils.get_hog_features(ch3, orient, pix_per_cell, cell_per_block, feature_vec=False)
    #print("hog1 ", hog1.shape)
    #debug = np.copy(ctrans_tosearch)
    for xb in range(nxsteps):
        for yb in range(nysteps):
            ypos = yb*cells_per_step
            xpos = xb*cells_per_step
            #print("merda ", ypos, xpos)
            # Extract HOG for this patch
            hog_feat1 = hog1[ypos:ypos+nblocks_per_window, xpos:xpos+nblocks_per_window].ravel()
            hog_feat2 = hog2[ypos:ypos+nblocks_per_window, xpos:xpos+nblocks_per_window].ravel()
            hog_feat3 = hog3[ypos:ypos+nblocks_per_window, xpos:xpos+nblocks_per_window].ravel()
            hog_features = np.hstack((hog_feat1, hog_feat2, hog_feat3))

            xleft = xpos*pix_per_cell
            ytop = ypos*pix_per_cell
            #print("Sto guardando le posizioni", ytop, ytop+window, xleft,xleft+window)
            # Extract the image patch
            subimg = cv2.resize(ctrans_tosearch[ytop:ytop+window, xleft:xleft+window], (64,64))
            # cv2.rectangle(debug, (xleft,ytop), (xleft+window,ytop+window),(255,0,0),1)
            # cv2.imshow("subimage", mah)
            # cv2.waitKey(0)
            #print("subimage.shape", subimg.shape)

            # Get color features
            spatial_features = utils.bin_spatial(subimg, size=spatial_size)

            hist_features = utils.color_hist(subimg, nbins=hist_bins)
            features = np.hstack((spatial_features, hist_features, hog_features))
            # Scale features and make a prediction
            if feature_filter is not None:
                test_features = X_scaler.transform(np.hstack((spatial_features, hist_features, hog_features)).reshape(1, -1))[:,feature_filter]
            else:
                test_features = X_scaler.transform(np.hstack((spatial_features, hist_features, hog_features)).reshape(1, -1))
            #print("Mah, test_feature", test_features.shape)
            test_prediction = clf.predict(test_features)

            #print("Fine predizone")
            if test_prediction == 1:
                xbox_left = np.int(xleft * scale)
                ytop_draw = np.int(ytop * scale)
                win_draw = np.int(window * scale)
                cv2.rectangle(draw_img,(xbox_left, ytop_draw+ystart),(xbox_left+win_draw,ytop_draw+win_draw+ystart),(255,0,0),3)
                img_boxes.append(((xbox_left, ytop_draw+ystart),(xbox_left+win_draw,ytop_draw+win_draw+ystart)))
                heatmap[ytop_draw + ystart:ytop_draw + win_draw + ystart, xbox_left:xbox_left + win_draw] += 1
                # cv2.imshow("Detected partial ", draw_img)
                # cv2.waitKey(0)
    # cv2.imshow("Detected", draw_img)
    # cv2.waitKey(0)
    return draw_img, heatmap, img_boxes


def heatmap_threshold(heatmap, threshold):
    heatmap[heatmap <= threshold] = 0
    return heatmap

def draw_labeled_bboxes(img, labels):
    # Iterate through all detected cars
    for car_number in range(1, labels[1]+1):
        # Find pixels with each car_number label value
        nonzero = (labels[0] == car_number).nonzero()
        # Identify x and y values of those pixels
        nonzeroy = np.array(nonzero[0])
        nonzerox = np.array(nonzero[1])
        # Define a bounding box based on min/max x and y
        bbox = ((np.min(nonzerox), np.min(nonzeroy)), (np.max(nonzerox), np.max(nonzeroy)))
        # Draw the box on the image
        cv2.rectangle(img, bbox[0], bbox[1], (0,0,255), 3)
    # cv2.imshow("draw_boxes", img)
    # cv2.waitKey(0)
    # Return the image
    return img


def process_image(img):
    global heatmap_sum
    global heatmaps
    ystart = 400
    ystop = 656
    scale = 1.5
    out_img, heatmap, boxes = find_cars(img, ystart, ystop, scale, clf, scaler, feat_filter)
    heatmap_sum += heatmap
    # plt.imshow(heatmap, cmap='hot')
    # plt.title("Partial heatmap")
    # plt.show()


    heatmaps.append(heatmap)
    if len(heatmaps)>=15:
        old_heatmap = heatmaps.pop(0)
        heatmap_sum -= old_heatmap
        # plt.imshow(heatmap_sum, cmap='hot')
        # plt.title("Thresholded Total heatmap")
        # plt.show()
    t_heatmap = heatmap_threshold(heatmap_sum, 30)
    labels = label(t_heatmap)
    draw_img = draw_labeled_bboxes(np.copy(img), labels)
    return draw_img


if __name__ == '__main__':
    filename = './model_dati_easy1/model_YCrCb_orient_9_pix_cell_8_cell_block_2_hog_-1.pkl'
    #filename = './model_dati_easy/best_model.pkl'
    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            pkl = pickle.load(f)
            clf = pkl['model']
            feat_filter = pkl['filter_mask']
            scaler = pkl['scaler']
            # clf = pickle.load(f)
            # feat_filter = pickle.load(f)
            # scaler = pickle.load(f)

    # print(type(clf))
    # print(type(feat_filter))
    # print(type(scaler))
    # ystart = 400
    # ystop = 656
    # scale = 2
    #
    # Read video frame
    heatmaps = []
    heatmap_sum = np.ones((720,1280)).astype(np.int32)

    # test_images = glob.glob('./test_images/test_frame*')
    # for test_img in test_images:
    #     img = cv2.imread(test_img)
    #     res = process_image(img)
    #     cv2.imshow("Result", res)
    #     cv2.waitKey(0)
        #print("max = ", np.max(img), " min = ", np.min(img))
    #     out_img, heatmap, boxes = find_cars(img, ystart, ystop, scale, clf, scaler, feat_filter)
    #     # cv2.imshow("vediamo qui", out_img)
    #     # cv2.waitKey(0)
    #     t_heatmap = heatmap_threshold(heatmap, 1)
    #     labels = label(t_heatmap)
    #     # plt.imshow(t_heatmap, cmap='hot')
    #     # plt.show()
    #     out_img = draw_labeled_bboxes(img, labels)
    #     cv2.imshow("vediamo qui dopo filter", out_img)
    #     cv2.waitKey(0)


    # output_movie = 'project_video_out.mp4'
    # clip = VideoFileClip('project_video.mp4')
    output_movie = 'test_video_out.mp4'
    clip = VideoFileClip('test_video.mp4')
    # for i in range(0,100):
    #     timeframe = "00:00:00." + '{num:02d}'.format(num=i)
    #     clip.save_frame("./test_images/test_frame" + timeframe + ".png", t=timeframe)
    test_clip = clip.fl_image(process_image)
    test_clip.write_videofile(output_movie, audio=False)

    # # #find car...
    #images = glob(...)
    #for image_file in images:
    #    img = cv2.imread(image_file)
    #    windows = slide_window(...)
        # found_win = find_car(img, windows, clf, scaler, filter_mask)
        # draw_boxes(img, found_wind, color=(0,0,255), thick=6)
        # cv2.imshow(img)
        # cv2.waitKey(0)
