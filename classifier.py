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
from sklearn.tree import DecisionTreeClassifier
import pickle
import utils

def extract_features(imgs, cspace='RGB', orient=9, pix_per_cell=8, cell_per_block=2,
                    hog_channel=0, size=(32,32), space_feat=True, color_feat=True, hog_feat=True):
    features = []
    for f in imgs:
        image_feat = []
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
    return np.array(features, dtype=np.float64)


def classify(cars, notcars, cspace, orient, pix_per_cell, cell_per_block, hog_channel):
    print('Using colorspace:', cspace, ' orientations:', orient,
        ' pixels per cell:', pix_per_cell, ' cell_per_block:', cell_per_block,
        'hog_channel:', hog_channel)

    t=time.time()
    car_features = extract_features(cars, cspace=cspace, orient=orient,
                            pix_per_cell=pix_per_cell, cell_per_block=cell_per_block,
                            hog_channel=hog_channel, space_feat=True, color_feat=True, hog_feat=True)
    notcar_features = extract_features(notcars, cspace=cspace, orient=orient,
                            pix_per_cell=pix_per_cell, cell_per_block=cell_per_block,
                            hog_channel=hog_channel, space_feat=True, color_feat=True, hog_feat=True)
    t2 = time.time()
    print(round(t2-t, 2), 'Seconds to extract HOG features...')
    # Create an array stack of feature vectors
    X = np.vstack((car_features, notcar_features))
    # Define the labels vector
    y = np.hstack((np.ones(len(car_features)), np.zeros(len(notcar_features))))

    # Split train and test set
    # Split up data into randomized training and test sets
    rand_state = 666 #np.random.randint(0, 100)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=rand_state)

    print('Train Feature vector length:', len(X_train[0]))
    print('Test Feature vector length:', len(X_test[0]))

    # Fit a per-column scaler
    X_scaler = StandardScaler().fit(X_train)
    # Apply the scaler to X
    scaled_train_X = X_scaler.transform(X_train)

    # Feature Importance
    clf = DecisionTreeClassifier(random_state=666, min_samples_split=20)
    clf.fit(scaled_train_X, y_train)
    print("feature importance params ",np.max(clf.feature_importances_), np.min(clf.feature_importances_), np.mean(clf.feature_importances_))
    feat_filter = 0
    filter_mask = np.array([val > feat_filter for val in clf.feature_importances_])
    print("We will keep ", np.sum(filter_mask), "/", scaled_train_X.shape[1], " features ")

    X_train_filtered = scaled_train_X[:,filter_mask]

    X_test_filtered = X_scaler.transform(X_test)[:, filter_mask]

    # Use a linear SVC
    svc = LinearSVC()
    # Check the training time for the SVC
    t=time.time()
    svc.fit(X_train_filtered, y_train)
    t2 = time.time()
    print(round(t2-t, 2), 'Seconds to train SVC...')
    # Check the score of the SVC
    acc = round(svc.score(X_test_filtered, y_test), 4)
    print('Test Accuracy of SVC = ', acc)

    return svc, acc, X_scaler, filter_mask



def grid_search(cars, notcars):
    ### TODO: Tweak these parameters and see how the results change.
    colorspaces = ['RGB', 'HSV', 'LUV', 'HLS', 'YUV', 'YCrCb']
    orient = 9
    pix_per_cells = [8, 16]
    cell_per_blocks = [1,2]
    hog_channels = [-1, 0, 1, 2] # Can be 0, 1, 2, or -1 that stands for alla channels
    color_feats = [ True, False]
    hog_feats = [True, False]
    space_feats = [True, False]
    max_acc = 0
    for clspcs in colorspaces:
        for h_chan in hog_channels:
            for cell_per_block in cell_per_blocks:
                for pix_per_cell in pix_per_cells:
                    kwargs = {'cspace':clspcs, 'orient':orient, 'pix_per_cell':pix_per_cell,
                        'cell_per_block':cell_per_block, 'hog_channel':h_chan}
                    model, acc, scaler, filter_mask = classify(cars, notcars, **kwargs)
                    if acc > max_acc:
                        with open('model_parameter.txt', 'w') as fm:
                            #file_name = 'Accuracy: ' + str(acc) + ' colorspace: ' + clspcs + ' orient: ' + str(orient) + ' pix_cell: ', str(pix_per_cell), + ' cell_block: ' + str(cell_per_block) + ' hog:' + str(h_chan)
                            fm.write("Accuracy " + str(acc) + '\n')
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
                        max_acc = acc
                    file_name = 'model_' + clspcs + '_orient_' + str(orient) + '_pix_cell_' + str(pix_per_cell) \
                                + '_cell_block_' + str(cell_per_block) + '_hog_' + str(h_chan) + '.pkl'
                    with open(file_name, 'wb') as fid:
                        pickle.dump(model, fid)
                        pickle.dump(filter_mask, fid)
                        pickle.dump(scaler, fid)


if __name__ == "__main__":
    # Divide up into cars and notcars
    images = glob.glob('./data_set/*/*/*.png')
    cars = []
    notcars = []
    for image in images:
        if 'non-vehicles' in image:
            notcars.append(image)
        else:
            cars.append(image)

    print("Data summary: ")
    print("We have ", len(notcars), " not car images and ", len(cars),
        " car images and the ratio is ", float(len(notcars))/len(cars))
    # sample_size = 100
    # cars = cars[0:sample_size]
    # notcars = notcars[0:sample_size]
    grid_search(cars, notcars)
