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
print_perf(perf)

#Visualization
