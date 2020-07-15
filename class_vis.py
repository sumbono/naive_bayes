#!/usr/bin/python

import warnings
warnings.filterwarnings("ignore")
import matplotlib 
matplotlib.use('agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import base64
import json
import subprocess

def prettyPicture(clf, accuracy, X_test, y_test):
    x_min = 0.0; x_max = 1.0
    y_min = 0.0; y_max = 1.0

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    h = .01  # step size in the mesh
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    
    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.pcolormesh(xx, yy, Z, cmap=plt.get_cmap('seismic'))
    
    # Plot also the test points
    grade_sig = [X_test[ii][0] for ii in range(0, len(X_test)) if y_test[ii]==0]
    bumpy_sig = [X_test[ii][1] for ii in range(0, len(X_test)) if y_test[ii]==0]
    grade_bkg = [X_test[ii][0] for ii in range(0, len(X_test)) if y_test[ii]==1]
    bumpy_bkg = [X_test[ii][1] for ii in range(0, len(X_test)) if y_test[ii]==1]

    blue_patch = plt.scatter(grade_sig, bumpy_sig, color = "b", label="fast")
    red_patch = plt.scatter(grade_bkg, bumpy_bkg, color = "r", label="slow")
    accuracy = mpatches.Patch(color="grey", label=f"accuracy: {accuracy}")
    plt.legend(handles=[blue_patch, red_patch, accuracy])
    
    plt.xlabel("bumpiness")
    plt.ylabel("grade")
    plt.savefig("test.png")

def output_image(name, format, bytes):
    # image_start = "BEGIN_IMAGE_f9825uweof8jw9fj4r8"
    # image_end = "END_IMAGE_0238jfw08fjsiufhw8frs"
    data = {}
    data['name'] = name
    data['format'] = format
    data['bytes'] = base64.encodestring(bytes)