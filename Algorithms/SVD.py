from surprise import SVD
from surprise import NMF
from surprise import KNNBasic
from surprise import Dataset
from surprise import evaluate, print_perf
from surprise import *
from surprise import  Reader
import os
import numpy as np
from six import iteritems
from six import itervalues
from itertools import product
import csv
import pprint

def pt(performances):
        # retrieve number of folds. Kind of ugly...
    n_folds = [len(values) for values in itervalues(performances)][0]

    row_format = '{:<8}' * (n_folds + 2)
    s = row_format.format(
        '',
        *['Fold {0}'.format(i + 1) for i in range(n_folds)] + ['Mean'])
    s += '\n'
    s += '\n'.join(row_format.format(
        key.upper(),
        *['{:1.4f}'.format(v) for v in vals] +
        ['{:1.4f}'.format(np.mean(vals))])
        for (key, vals) in iteritems(performances))
    print(s)

#load data from a file
file_path = os.path.expanduser('restaurant_ratings.txt')
reader = Reader(line_format='user item rating timestamp', sep='\t', skip_lines=0)
data = Dataset.load_from_file(file_path, reader=reader)
data.folds()

#splitting data into 3 folds
data.split(n_folds=3, shuffle=False)

#SVD Algorithm
algo = SVD()

#Printing the result
perf = evaluate(algo, data, measures=['RMSE', 'MAE'])
# print()
def printSVD():
    pt(perf)
printSVD()
# print()
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Outputs/")

with open('SVD.csv','w') as fo:
    print_perf(perf,fo)
