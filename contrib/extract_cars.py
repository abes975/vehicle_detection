import csv
import cv2
import collections
import sys
import random

def crop_and_resize(data, non_cars, size=(64,64)):
    for d in data:
        print("Processing file: ", d[0])
        img = cv2.imread(d[0])
        #print("Dimensioni = ", img.shape)
        cropped = img[int(d[1]):int(d[2]), int(d[3]):int(d[4])]
        cropped = cv2.resize(cropped, size)
        cv2.imwrite('./vehicles/cropped_' + d[0].replace(".jpg", ".png"), cropped)
        # Now try random element for x and y in order to create non car images :)
        create_non_cars(img, d[0], non_cars[d[0]], size, 50, 1)# len(non_cars[d[0]]['x']))

def compare(elem, coords, size):
    flag = True
    for c in coords:
        if elem >= c[0] and elem <= c[1]:
            #print("Elem ", elem , " >= ", c[0], " and <= ", c[1], " failed ")
            flag = False
            return flag
        if (elem + size) >= c[0] and (elem + size) <= c[1]:
            #print("Elem + size", elem + size , " >= ", c[0], " and <= ", c[1], " failed ")
            flag = False
            return flag
    #print("we were lucky and returning ", flag)
    return flag

def create_non_cars(img, name, non_cars, size, thresh, count):
    cons_err = 0
    c = 0
    new_x = -1
    new_y = -1
    while (cons_err < thresh and c < count):
        if new_x == -1:
            new_x = random.randint(0, img.shape[1])
        if new_y == -1:
            # Do not take sky picture...not so useful
            new_y = random.randint(300, img.shape[0]*0.85)
        #print("Checking new X....", new_x)
        check_x = compare(new_x, non_cars['x'], size[0])
        #print("X check Returned :", check_x)
        #print("Checking new Y....", new_y)
        check_y = compare(new_y, non_cars['y'], size[1])
        #print("Y check Returned :", check_y)
        if check_x == False:
            new_x = -1
            cons_err += 1
        elif new_y == False:
            new_y = -1
            cons_err += 1
        else:
            #print("We found a new non car image at (", new_x, ", ", new_y, ")")
            new_img = img[new_y:new_y+size[1], new_x:new_x+size[0]]
            if new_img.shape == (64,64, 3):
                cv2.imwrite('./non-vehicles/non_cars_' + str(c) + "_" + name.replace(".jpg", ".png"), new_img)
                c += 1
            else:
                cons_err += 1
            new_x = -1
            new_y = -1

#def create_non_cars(img, non_cars, size=(64,64)):
#    diff = []
#    for key, vals in non_cars.items():
#        deltas_x = []
#        deltas_y = []
#        # new x and new y will contain the beginning of the non data cars on x and y
#        new_x = []
#        nex_y = []
#        for k, val in vals.items():
#            sor_val = sorted(val)
#            sor_val.insert(0, 0)
#            if k == 'x':
#                added = deltas_x
#                sor_val.append(img.shape[1])
#                print("X =", sor_val)
#            else:
#                added = deltas_y
#                sor_val.append(img.shape[0])
#                print("Y =", sor_val)
#            for d in range(1, len(sor_val)):
#                added.append(sor_val[d] - sor_val[d-1])
#        print("for k = ", key, "\n delta_x =", deltas_x, "\n deltas_y=", deltas_y)
#        new_x = get_new_points(sor_val, deltas_x, size[0])
#        print("XXX = ", new_x)
#        sys.exit(1)
#        new_y = get_new_points(sor_val, deltas_y, size[1])
#
#        
#def get_new_points(vertex, deltas, size):       
#    points = []
#    for i in range(len(deltas)):
#        d = deltas[i]
#        quot = d//size
#        remainder = d - quot * size
#        print("delta = ", d, " quot = ", quot, " remainder = " , remainder)
#        if quot == 0 or d < size:
#            print("We cannot fit a ", size,  " because we have only ", d, " pixels")
#            continue
#        if remainder == 0:
#            print("We have a multiple, remainder was : ", remainder)
#            x = vertex[i]
#            for j in range(0,quot):
#                print("New points = ", x + j * size)
#                points.append(x + j * size)
#        if remainder != 0:
#            print("We can add some randomness ")
#            if remainder >= quot:
#                distr = int(remainder) // quot
#                print("remainder = ", remainder, " quot = ", quot, "Distributable pixels = ", distr)
#                x = vertex[i] 
#                for j in range(0,quot):
#                    print("\t we start from ", x)
#                    new_point = random.randint(x, x + distr)
#                    print("XXX New points = ", new_point)
#                    points.append(new_point)
#                    x = new_point + size
#    return points
#                    
#                
            

data = []
non_cars = {}
with open('labels.csv') as csvfile:
    labels = csv.reader(csvfile)
    # skip header
    next(labels, None)
    # Filname, x, y, width, height
    for row in labels:
        x1 = int(row[0])
        x2 = int(row[2])
        y1 = int(row[1])
        y2 = int(row[3])
        if abs(x2 - x1) > 0 and abs(y1-y2) > 0: 
            if row[5] == 'Car':
                #print(row[4], row[5], row[1], row[3], row[0], row[2])
                data.append((row[4], y1, y2, x1, x2))
            if row[4] not in non_cars:
                non_cars[row[4]] = {'x':[], 'y':[]}
            non_cars[row[4]]['x'].append((x1, x2)) 
            non_cars[row[4]]['y'].append((y1,y2))

crop_and_resize(data, non_cars, size=(64,64))



