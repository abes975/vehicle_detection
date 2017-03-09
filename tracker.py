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
import sys

#
# def extract_feature_single(image, cspace='YcrCb', orient=8, pix_per_cell=8, cell_per_block=2,
#                     hog_channel=-1, size=(32,32), space_feat=True, color_feat=True, hog_feat=True):
#     features = []
#     imgage_feat = []
#     image = cv2.imread(f)
#     resized = utils.convert_color(image, color_space=cspace)
#     # If I have time let's try to play around with those parameters
#     if space_feat:
#         spatial_features = utils.bin_spatial(resized, size=size)
#         image_feat.append(spatial_features)
#     if color_feat:
#         color_features = utils.color_hist(resized, nbins=32)
#         image_feat.append(color_features)
#     if hog_feat:
#         if hog_channel == -1:
#             hog_features = []
#             for channel in range(resized.shape[2]):
#                 hog_features.append(utils.get_hog_features(resized[:,:,channel],
#                                     orient, pix_per_cell, cell_per_block,
#                                     vis=False, feature_vec=True))
#             hog_features = np.ravel(hog_features)
#         else:
#             hog_features = utils.get_hog_features(resized[:,:,hog_channel],
#                                 orient, pix_per_cell, cell_per_block,
#                                 vis=False, feature_vec=True)
#         image_feat.append(hog_features)
#     features.append(np.concatenate(image_feat))
#     return features


# Define a single function that can extract features using hog sub-sampling and make predictions
def find_cars(img, ystart, ystop, scale, clf, X_scaler, feature_filter, colspace='YCrCb', orient=9,
                pix_per_cell=8, cell_per_block=2, hist_bins=32, spatial_size=(32,32)):
    heatmap = np.zeros_like(img[:,:,0])
    # That's very important if you use cv2 to read images and then the
    # videoclip class maybe uses matplotlib and so the image is in RGB colorspace
    # why we assumed the images are in BGR throughout the training!!!
    img_BGR = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    draw_img = np.copy(img_BGR)

    img_tosearch = img_BGR[ystart:ystop,:,:]
    ctrans_tosearch = utils.convert_color(img_tosearch, color_space=colspace)

    if scale != 1:
        imshape = ctrans_tosearch.shape
        new_size = (np.int(imshape[1]/scale), np.int(imshape[0]/scale))
        img_tosearch = cv2.resize(img_tosearch, new_size)
        ctrans_tosearch = cv2.resize(ctrans_tosearch, new_size)

    ch1 = ctrans_tosearch[:,:,0]
    ch2 = ctrans_tosearch[:,:,1]
    ch3 = ctrans_tosearch[:,:,2]

    # Define blocks and steps as above
    nxblocks = (ch1.shape[1] // pix_per_cell) - 1
    nyblocks = (ch1.shape[0] // pix_per_cell) - 1
    nfeat_per_block = orient * cell_per_block**2
    # 64 was the orginal sampling rate, with 8 cells and 8 pix per cell
    window = 64
    nblocks_per_window = (window // pix_per_cell) - 1
    ## OVERLAP
    cells_per_step = 2  # Instead of overlap, define how many cells to step

    nxsteps = (nxblocks - nblocks_per_window) // cells_per_step
    nysteps = (nyblocks - nblocks_per_window) // cells_per_step
    if nxsteps == 0 or nysteps == 0:
        print("The used scale is too small...we cannot fit even a single window")

    # Compute individual channel HOG features for the entire image
    hog1 = utils.get_hog_features(ch1, orient, pix_per_cell, cell_per_block, feature_vec=False)
    hog2 = utils.get_hog_features(ch2, orient, pix_per_cell, cell_per_block, feature_vec=False)
    hog3 = utils.get_hog_features(ch3, orient, pix_per_cell, cell_per_block, feature_vec=False)

    for xb in range(nxsteps):
        for yb in range(nysteps):
            ypos = yb*cells_per_step
            xpos = xb*cells_per_step
            # Extract HOG for this patch
            hog_feat1 = hog1[ypos:ypos+nblocks_per_window, xpos:xpos+nblocks_per_window].ravel()
            hog_feat2 = hog2[ypos:ypos+nblocks_per_window, xpos:xpos+nblocks_per_window].ravel()
            hog_feat3 = hog3[ypos:ypos+nblocks_per_window, xpos:xpos+nblocks_per_window].ravel()
            hog_features = np.hstack((hog_feat1, hog_feat2, hog_feat3))

            xleft = xpos * pix_per_cell
            ytop = ypos * pix_per_cell

            # Extract the image patch
            subimg = cv2.resize(ctrans_tosearch[ytop:ytop+window, xleft:xleft+window], (64,64))

            # Get color features
            spatial_features = utils.bin_spatial(subimg, size=spatial_size)
            hist_features = utils.color_hist(subimg, nbins=hist_bins)
            # Scale features and make a prediction
            features = np.hstack((spatial_features, hist_features, hog_features)).astype(np.float64)

            # If we selected filter during training do it again here
            if feature_filter is not None:
                test_features = features[feature_filter]
            else:
                test_features = features

            extracted_features = X_scaler.transform(test_features).reshape(1, -1)

            test_prediction = clf.predict(extracted_features)

            #print("Fine predizone")
            if test_prediction == 1:
                xbox_left = np.int(xleft * scale)
                ytop_draw = np.int(ytop * scale)
                win_draw = np.int(window * scale)
                cv2.rectangle(draw_img,(xbox_left, ytop_draw+ystart),(xbox_left+win_draw,ytop_draw+win_draw+ystart),(255,0,0),3)
                heatmap[ytop_draw + ystart:ytop_draw + win_draw + ystart, xbox_left:xbox_left + win_draw] += 1
                # cv2.imshow("Detected partial ", draw_img)
                # cv2.waitKey(0)
    # cv2.imshow("Detected", draw_img)
    # cv2.waitKey(0)
    return draw_img, heatmap


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
    return img


def process_image(img):
    global heatmap_sum
    global heatmaps
    ystart = 400
    ystop = 656
    scale = 1.5
    out_img, heatmap = find_cars(img, ystart, ystop, scale, clf, scaler, feat_filter)
    heatmap_sum += heatmap
    # plt.imshow(heatmap, cmap='hot')
    # plt.title("Partial heatmap")
    # plt.show()


    heatmaps.append(heatmap)
    if len(heatmaps)>=30:
        old_heatmap = heatmaps.pop(0)
        heatmap_sum -= old_heatmap
    t_heatmap = heatmap_threshold(heatmap_sum, 5)
    t_heatmap = np.clip(t_heatmap, 0,255)
    # plt.imshow(heatmap_sum, cmap='hot')
    # plt.title("Thresholded Total heatmap")
    # plt.show()
    labels = label(t_heatmap)
    draw_img = draw_labeled_bboxes(np.copy(img), labels)
    return draw_img


if __name__ == '__main__':

    filename = './model_solo_gti/model_YCrCb_orient_9_pix_cell_8_cell_block_2_hog_-1.pkl'
    #filename = './model_dati_easy/best_model.pkl'
    if not os.path.isfile(filename):
        print("Model file ", filename, " does not exist")
        sys.exit(1)

    with open(filename, 'rb') as f:
        pkl = pickle.load(f)
        clf = pkl['model']
        feat_filter = pkl['filter_mask']
        scaler = pkl['scaler']

    # print(type(clf))
    # print(type(feat_filter))
    # print(type(scaler))

    # Global variables where store heatmaps and heatmap_sum
    heatmaps = []
    heatmap_sum = np.zeros((720,1280)).astype(np.int32)
    #
    # test_images = glob.glob('./test_images/test_frame*')
    # for test_img in test_images:
    #     img = cv2.imread(test_img)
    #     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #     res = process_image(img)
    #     cv2.imshow("Result", cv2.cvtColor(res, cv2.COLOR_RGB2BGR))
    #     cv2.waitKey(0)

    # output_movie = 'test_video_out.mp4'
    # clip = VideoFileClip('test_video.mp4')
    # test_clip = clip.fl_image(process_image)
    # test_clip.write_videofile(output_movie, audio=False)

    output_movie = 'project_video_out.mp4'
    p_clip = VideoFileClip('project_video.mp4')
    project_clip = p_clip.fl_image(process_image)
    project_clip.write_videofile(output_movie, audio=False)
