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
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.tree import DecisionTreeClassifier
import pickle
import utils
import sys
import random

def extract_features(imgs, cspace='RGB', orient=9, pix_per_cell=8, cell_per_block=2,
                    hog_channel=0, size=(32,32), space_feat=True, color_feat=True, hog_feat=True, flip=True):
    features = []
    for f in imgs:
        image = cv2.imread(f)
        image = image.astype(np.float32)/255
        if flip:
            flipped = cv2.flip(image,1)
            images = [image, flipped]
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
            converted = image.astype(np.float32)/255
            # If I have time let's try to play around with those parameters
            if space_feat:
                spatial_features = utils.bin_spatial(converted, size=size)
                image_feat.append(spatial_features)
                #print("Spatial feature = ", spatial_features.shape)
            if color_feat:
                color_features = utils.color_hist(converted, nbins=32)
                image_feat.append(color_features)
                #print("Color feature = ", color_features.shape)
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
                #print("Hog features = ", hog_features.shape)
                image_feat.append(hog_features)
            features.append(np.concatenate(image_feat))
        #print("All features = ", np.concatenate(image_feat).shape)
    return np.array(features, dtype=np.float64)


def classify(cars, notcars, test_cars, test_noncars, cspace, orient, pix_per_cell, cell_per_block, hog_channel,
            filter_features = False):
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
    print(round(t2-t, 2), 'Seconds to extract HOG features...for training set')

    # Testing set
    t=time.time()
    t_car_features = extract_features(test_cars, cspace=cspace, orient=orient,
                        pix_per_cell=pix_per_cell, cell_per_block=cell_per_block,
                        hog_channel=hog_channel, space_feat=True, color_feat=True, hog_feat=True, flip=False)
    t_notcar_features = extract_features(test_noncars, cspace=cspace, orient=orient,
                        pix_per_cell=pix_per_cell, cell_per_block=cell_per_block,
                        hog_channel=hog_channel, space_feat=True, color_feat=True, hog_feat=True, flip=False)
    t2 = time.time()
    print(round(t2-t, 2), 'Seconds to extract HOG features...for testing set')

    # Create an array stack of feature vectors
    X_train = np.vstack((car_features, notcar_features))
    # Define the labels vector
    y_train = np.hstack((np.ones(len(car_features)), np.zeros(len(notcar_features))))

    # Create an array stack of feature vectors
    X_test = np.vstack((t_car_features, t_notcar_features))
    # Define the labels vector
    y_test = np.hstack((np.ones(len(t_car_features)), np.zeros(len(t_notcar_features))))


    # X = np.vstack((car_features, notcar_features))
    # # Define the labels vector
    # y = np.hstack((np.ones(len(car_features)), np.zeros(len(notcar_features))))
    #
    # # Split train and test set
    # # Split up data into randomized training and test sets
    # rand_state = 555 #np.random.randint(0, 100)
    # X_train, X_test, y_train, y_test = train_test_split(
    #      X, y, test_size=0.30, random_state=rand_state)

    print('We have ', len(X_train), ' training samples and train Feature vector length:', len(X_train[0]))
    print('We have ', len(X_test), ' test samples and test Feature vector length:', len(X_test[0]))

    # Fit a per-column scaler
    X_scaler = StandardScaler().fit(X_train)
    # Apply the scaler to X
    scaled_train_X = X_scaler.transform(X_train)

    if filter_features:
        # Feature Importance
        from sklearn import metrics
        from sklearn.ensemble import ExtraTreesClassifier
        # load the iris datasets
        # fit an Extra Trees model to the data
        forest = ExtraTreesClassifier(n_estimators=250,
                                      random_state=0)
        forest.fit(scaled_train_X, y_train)
        # display the relative importance of each attribute
        # # Feature Importance
        # clf = DecisionTreeClassifier(random_state=666, min_samples_split=20)
        # clf.fit(scaled_train_X, y_train)
        importances = forest.feature_importances_
        std = np.std([tree.feature_importances_ for tree in forest.estimators_],
                axis=0)
        indices = np.argsort(importances)[::-1]

        # Print the feature ranking
        print("Feature ranking:")

        for f in range(scaled_train_X.shape[1]):
                print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

        # Plot the feature importances of the forest
        # plt.figure()
        # plt.title("Feature importances")
        # #plt.bar(range(scaled_train_X.shape[1]), importances[indices],
        # #       color="r", yerr=std[indices], align="center")
        # plt.bar(range(scaled_train_X.shape[1]), importances[indices],
        #     color="r", yerr=None, align="center")
        # plt.xticks(range(scaled_train_X.shape[1]), indices)
        # plt.xlim([-1, scaled_train_X.shape[1]])
        # plt.show()
        # print("feature importance params ",np.max(clf.feature_importances_), np.min(clf.feature_importances_), np.mean(clf.feature_importances_))
        # plt.hist(clf.feature_importances_)
        # plt.show()
        feat_filter = 0.0001
        filter_mask = np.array([val >= feat_filter for val in importances])

        X_train_filtered = scaled_train_X[:,filter_mask]

        X_test_filtered = X_scaler.transform(X_test)[:, filter_mask]
    else:
        X_train_filtered = scaled_train_X
        X_test_filtered = X_scaler.transform(X_test)
        filter_mask = None

    print("We have", X_train_filtered.shape[1], " features ")
    # Use a linear SVC
    svc = LinearSVC(max_iter=2500, verbose=1)
    # Check the training time for the SVC
    t=time.time()
    svc.fit(X_train_filtered, y_train)
    t2 = time.time()
    print(round(t2-t, 2), 'Seconds to train SVC...')
    # Check the score of the SVC
    acc = round(svc.score(X_test_filtered, y_test), 4)
    y_pred = svc.predict(X_test_filtered)
    f1_sc = round(f1_score(y_test, y_pred),4)
    precision = round(precision_score(y_test, y_pred),4)
    recall = round(recall_score(y_test, y_pred),4)
    print('Test Accuracy of SVC = ', acc, ' f1 score = ', f1_sc,
        ' precision = ', precision, ' recall = ', recall)

    return svc, (acc, f1_sc, precision, recall), X_scaler, filter_mask



def grid_search(cars, notcars, test_cars, test_noncars):
    ### TODO: Tweak these parameters and see how the results change.
    colorspaces = ['YCrCb', 'HLS', 'HSV', 'RGB', 'YUV', 'LUV']
    #colorspaces = ['YCrCb', 'HLS' ]
    orient = 9
    pix_per_cells = [8]
    cell_per_blocks = [2]
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
            for cell_per_block in cell_per_blocks:
                for pix_per_cell in pix_per_cells:
                    kwargs = {'cspace':clspcs, 'orient':orient, 'pix_per_cell':pix_per_cell,
                        'cell_per_block':cell_per_block, 'hog_channel':h_chan}
                    model, metrics, scaler, filter_mask = classify(cars, notcars, test_cars, test_noncars,  **kwargs)
                    if int(metrics[1]) > max_acc:
                        with open('./model_dati_easy1/model_parameter.txt', 'w') as fm:
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
                        max_acc = int(metrics[1])
                        file_name='./model_dati_easy1/best_model.pkl'
                        with open(file_name, 'wb') as fid:
                            data_bundle = {'model': model, 'filter_mask': filter_mask, 'scaler': scaler}
                            pickle.dump(data_bundle, fid)

                    file_name = './model_dati_easy1/model_' + clspcs + '_orient_' + str(orient) + '_pix_cell_' + str(pix_per_cell) \
                                + '_cell_block_' + str(cell_per_block) + '_hog_' + str(h_chan) + '.pkl'
                    with open(file_name, 'wb') as fid:
                        data_bundle = {'model': model, 'filter_mask': filter_mask, 'scaler': scaler}
                        pickle.dump(data_bundle, fid)


if __name__ == "__main__":
    # Divide up into cars and notcars
    cars_images = glob.glob('./data/vehicles/*/*.png')
    notcars_images = glob.glob('./data/non-vehicles/*/*.png')

    testing_car_images = glob.glob('./object-detection-crowdai/vehicles/*.png')
    testing_notcar_images = glob.glob('./object-detection-crowdai/non-vehicles/*.png')


    cars = []
    notcars = []
    test_cars = []
    test_notcars = []
    for image in cars_images:
        cars.append(image)
    for image in notcars_images:
        notcars.append(image)

    for image in testing_car_images:
        test_cars.append(image)
    for image in testing_notcar_images:
        test_notcars.append(image)

    from sklearn.utils import shuffle
    test_cars_s = shuffle(test_cars, random_state=0)
    test_notcars_s = shuffle(test_notcars, random_state=0)

    print("Data summary: ")
    print("We have ", len(notcars), " not car images and ", len(cars),
        " car images and the ratio is ", float(len(notcars))/len(cars))
    print("Testing set: We have ", len(test_notcars_s), " not car images and ", len(test_cars_s),
        " car images and the ratio is ", float(len(test_notcars_s))/len(test_cars_s))
    # sample_size = 30
    # cars = cars[0:sample_size]
    # notcars = notcars[0:sample_size]
    # test_cars = cars[0:sample_size//3]
    # test_notcars = notcars[0:sample_size//3]
    #grid_search(cars, notcars, None, None)
    grid_search(cars, notcars, test_cars_s[:50000], test_notcars[:5000])
