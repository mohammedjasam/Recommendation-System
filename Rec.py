from surprise import Dataset
from surprise import Reader
import os


from surprise import SVD
from surprise import Dataset
from surprise import evaluate, print_perf
import osfrom surprise import  Reader

#load data from a file
file_path = os.path.expanduser('restaurant_ratings.txt')
reader = Reader(line_format='user item rating timestamp', sep='\t')
data = Dataset.load_from_file(file_path, reader=reader)

#splitting data into 3 folds
data.split(n_folds=3)
algo = SVD()
#unbiased version of SVD is PMF Algorithm
# algo = SVD(biased=False)
perf = evaluate(algo, data, measures=['RMSE', 'MAE'])
print_perf(perf)
