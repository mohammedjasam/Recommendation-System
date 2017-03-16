from surprise import SVD
from surprise import NMF
from surprise import KNNBasic
from surprise import Dataset
from surprise import evaluate, print_perf

from surprise import  Reader
import os

#load data from a file
file_path = os.path.expanduser('restaurant_ratings.txt')
reader = Reader(line_format='user item rating timestamp', sep='\t')
data = Dataset.load_from_file(file_path, reader=reader)

#splitting data into 3 folds
data.split(n_folds=3)

#SVD Algorithm
algo = SVD()
#--------------------------------------------------------------------------------#
#PMF Algorithm
# algo = SVD(biased=False)
#--------------------------------------------------------------------------------#
#NMF Algorithm
# algo = NMF()
#--------------------------------------------------------------------------------#
#User Based Collaborative Filtering Algorithm
# algo = KNNBasic(sim_options = {'user_based': True})
#Using the value of K
# algo = KNNBasic(k=20, sim_options = {'name':’MSD’, 'user_based': True })

#To used MSD in User Based Algorithm
# algo = KNNBasic(sim_options = {'name':’MSD’,'user_based': True })
#To used Cosine in User Based Algorithm
#algo = KNNBasic(sim_options = {'name':’cosine’,'user_based': True })
#To used Pearson in User Based Algorithm
#algo = KNNBasic(sim_options = {'name':’pearson’,'user_based': True })
#--------------------------------------------------------------------------------#
#Item based Collaborative Filtering algorithm.
#algo = KNNBasic(sim_options = {'user_based': False})
#Using the value of K
# algo = KNNBasic(k=20, sim_options = {'name':’MSD’, 'user_based': True })

#To used MSD in Item Based Algorithm
# algo = KNNBasic(sim_options = {'name':’MSD’,'user_based': False })
#To used Cosine in Item Based Algorithm
#algo = KNNBasic(sim_options = {'name':’cosine’,'user_based': False })
#To used Pearson in Item Based Algorithm
#algo = KNNBasic(sim_options = {'name':’pearson’,'user_based': False })
#--------------------------------------------------------------------------------#

perf = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf)
