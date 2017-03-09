import numpy as np
import cv2
import glob
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import time
from skimage.feature import hog
from sklearn.svm import LinearSVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import pickle
import utils
import sys
import random

def extract_features(img_files, cspace='', orient=9, pix_per_cell=8, cell_per_block=2,
                    hog_channel=0, size=(32,32), space_feat=True, color_feat=True, hog_feat=True, flip=True, rotate = False):
    features = []
    for f in img_files:
        image = cv2.imread(f)
        if flip == True:
            flipped = cv2.flip(image,1)
            images = [image, flipped]
            if rotate == True:
                angle = (15 - 2) * np.random.random_sample() + 2
                pos_neg = random.randint(0,1)
                if pos_neg == 0:
                    angle = -1 * angle
                M = cv2.getRotationMatrix2D((image.shape[1]/2,image.shape[0]/2), angle, 1)
                rotated = cv2.warpAffine(image, M, (image.shape[1],image.shape[0]))
                images.append(rotated)
        else:
            images = [image]

        for img in images:
            image_feat = []
            converted = utils.convert_color(img, color_space=cspace)
            # If I have time let's try to play around with those parameters
            if space_feat:
                spatial_features = utils.bin_spatial(converted, size=size)
                image_feat.append(spatial_features)
            if color_feat:
                color_features = utils.color_hist(converted, nbins=32)
                image_feat.append(color_features)
            if hog_feat:
                if hog_channel == -1:
                    hog_features = []
                    for channel in range(converted.shape[2]):
                        hog_features.append(utils.get_hog_features(converted[:,:,channel],
                                            orient, pix_per_cell, cell_per_block,
                                            vis=False, feature_vec=True))
                    hog_features = np.ravel(hog_features)
                else:
                    hog_features = utils.get_hog_features(converted[:,:,hog_channel],
                                        orient, pix_per_cell, cell_per_block,
                                        vis=False, feature_vec=True)
                image_feat.append(hog_features)
            features.append(np.concatenate(image_feat))
    return features


def classify(cars, notcars, test_cars, test_noncars, cspace, orient, pix_per_cell,
            cell_per_block, hog_channel, filter_features = True):
    print('Using colorspace:', cspace, ' orientations:', orient,
        ' pixels per cell:', pix_per_cell, ' cell_per_block:', cell_per_block,
        'hog_channel:', hog_channel)

    t=time.time()
    car_features = extract_features(cars, cspace=cspace, orient=orient,
                            pix_per_cell=pix_per_cell, cell_per_block=cell_per_block,
                            hog_channel=hog_channel, space_feat=True, color_feat=True,
                            hog_feat=True, flip = True, rotate=True)
    notcar_features = extract_features(notcars, cspace=cspace, orient=orient,
                            pix_per_cell=pix_per_cell, cell_per_block=cell_per_block,
                            hog_channel=hog_channel, space_feat=True, color_feat=True,
                            hog_feat=True, flip=True, rotate=True)
    t2 = time.time()
    print(round(t2-t, 2), 'Seconds to extract HOG features...for training set')

    X = np.vstack((car_features, notcar_features)).astype(np.float64)
    # Define the labels vector
    y = np.hstack((np.ones(len(car_features)), np.zeros(len(notcar_features))))

    # Split train and test set
    # Split up data into randomized training and test sets
    rand_state = np.random.randint(0, 100)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=rand_state)

    print('We have ', len(X_train), ' training samples and train Feature vector length:', len(X_train[0]))
    print('We have ', len(X_test), ' test samples and test Feature vector length:', len(X_test[0]))

    if filter_features:
        # Feature Importance
        from sklearn import metrics
        from sklearn.ensemble import ExtraTreesClassifier
        # load the iris datasets
        # fit an Extra Trees model to the data
        forest = ExtraTreesClassifier(n_estimators=50, random_state=666)
        forest.fit(X_train, y_train)

        sel_model = SelectFromModel(forest, prefit=True)
        X_train_filtered = sel_model.transform(X_train)
        print("After selecting feature we have ", X_train_filtered.shape)
        # Get the filter mask
        filter_mask = sel_model.get_support()

        X_test_filtered = X_test[:, filter_mask]
    else:
        X_train_filtered = scaled_train_X
        X_test_filtered = scaled_test_X
        filter_mask = None

    # Fit a per-column scaler
    X_scaler = StandardScaler().fit(X_train_filtered)
    # Apply the scaler to X
    X_train_scaled = X_scaler.transform(X_train_filtered)
    X_test_scaled = X_scaler.transform(X_test_filtered)

    #print("We have", X_train_filtered.shape[1], " features ")
    # Use a linear SVC
    print("Starting a SVM grid search")
    # param_grid = { 'C':[1.0,10.0,100.0] }
    # svc = GridSearchCV(LinearSVC(max_iter=5000, verbose=0),param_grid, n_jobs=5, pre_dispatch=4)
    # svc = svc.fit(X_train_scaled, y_train)
    # print("Best estimator found by grid search:")
    # print(svc.best_estimator_)
    svc = LinearSVC(max_iter=10000, verbose=1)
    # Check the training time for the SVC
    t=time.time()
    svc.fit(X_train_scaled, y_train)
    t2 = time.time()
    print(round(t2-t, 2), 'Seconds to Grid search SVC...')

    # Check the score of the SVC
    acc = round(svc.score(X_test_scaled, y_test), 4)
    y_pred = svc.predict(X_test_scaled)
    f1_sc = round(f1_score(y_test, y_pred),4)
    precision = round(precision_score(y_test, y_pred),4)
    recall = round(recall_score(y_test, y_pred),4)
    print('Test Accuracy of SVC = ', acc, ' f1 score = ', f1_sc,
        ' precision = ', precision, ' recall = ', recall, "\n")

    return svc, (acc, f1_sc, precision, recall), X_scaler, filter_mask
    #return svc, (acc, f1_sc), X_scaler, filter_mask


def grid_search(cars, notcars, test_cars, test_noncars):
    ### TODO: Tweak these parameters and see how the results change.
    #colorspaces = ['YCrCb', 'HLS', , 'RGB', 'YUV', 'LUV']
    colorspaces = ['HLS', 'HSV', 'YCrCb', 'RGB' ]
    #orients = [6,8,9]
    orients = [9]
    pix_per_cells = [8]
    cell_per_block = 2
    #hog_channels = [-1, 0, 1, 2] # Can be 0, 1, 2, or -1 that stands for alla channels
    hog_channels = [-1]
    color_feats = [ True, False]
    hog_feats = [True, False]
    space_feats = [True, False]

    # colorspaces = ['YCrCb']
    # orient = 9
    # pix_per_cells = [8]
    # cell_per_blocks = [2]
    # hog_channels = [-1] # Can be 0, 1, 2, or -1 that stands for alla channels
    # color_feats = [True, False]
    # hog_feats = [True, False]
    # space_feats = [True, False]

    max_acc = 0
    for clspcs in colorspaces:
        for h_chan in hog_channels:
            for orient in orients:
                for pix_per_cell in pix_per_cells:
                    kwargs = {'cspace':clspcs, 'orient':orient, 'pix_per_cell':pix_per_cell,
                        'cell_per_block':cell_per_block, 'hog_channel':h_chan}
                    model, metrics, scaler, filter_mask = classify(cars, notcars, test_cars, test_noncars,  **kwargs)
                    if metrics[1] > max_acc:
                        with open('./model_solo_gti/model_parameter.txt', 'w') as fm:
                            #file_name = 'Accuracy: ' + str(acc) + ' colorspace: ' + clspcs + ' orient: ' + str(orient) + ' pix_cell: ', str(pix_per_cell), + ' cell_block: ' + str(cell_per_block) + ' hog:' + str(h_chan)
                            fm.write("Accuracy " + str(metrics[0]) + '\n')
                            fm.write("F1 score " + str(metrics[1]) + '\n')
                            fm.write("Precision " + str(metrics[2]) + '\n')
                            fm.write("Recall " + str(metrics[3]) + '\n')
                            fm.write("Color Space " + str(clspcs) + '\n')
                            fm.write("Orient " + str(orient) + '\n')
                            fm.write("Pixel Per Cell " + str(pix_per_cell) + '\n')
                            fm.write("Cell Block " + str(cell_per_block) + '\n')
                            if h_chan == -1:
                                value = 'ALL'
                            else:
                                value = h_chan
                            fm.write("Hog " + str(value) + '\n')
                            #fm.write(file_name)
                        max_acc = metrics[1]
                        file_name='./model_solo_gti/best_model.pkl'
                        with open(file_name, 'wb') as fid:
                            data_bundle = {'model': model, 'filter_mask': filter_mask, 'scaler': scaler}
                            pickle.dump(data_bundle, fid)

                    file_name = './model_solo_gti/model_' + clspcs + '_orient_' + str(orient) + '_pix_cell_' + str(pix_per_cell) \
                                + '_cell_block_' + str(cell_per_block) + '_hog_' + str(h_chan) + '.pkl'
                    with open(file_name, 'wb') as fid:
                        data_bundle = {'model': model, 'filter_mask': filter_mask, 'scaler': scaler}
                        pickle.dump(data_bundle, fid)


if __name__ == "__main__":
    # Divide up into cars and notcars
    car_images = glob.glob('./data/vehicles/*/*.png')
    notcar_images = glob.glob('./data/non-vehicles/*/*.png')

    cars = []
    notcars = []
    test_cars = []
    test_notcars = []
    for image in car_images:
        cars.append(image)
    for image in notcar_images:
        notcars.append(image)

    print("Data summary: ")
    print("We have ", len(notcars), " not car images and ", len(cars),
        " car images and the ratio is ", float(len(notcars))/len(cars))

    # sample_size = 30
    # cars_tmp = cars_tmp[0:sample_size]
    # notcars_s = notcars_s[0:sample_size]
    # test_cars_s = test_cars_s[0:sample_size//3]
    # test_notcars_s = test_notcars_s[0:sample_size//3]
    grid_search(cars, notcars, None, None)
