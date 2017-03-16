import os  # We need this module
import subprocess
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Algorithms/")
subprocess.call('python Item.py',shell=True)




os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Outputs/")
with open('test.txt','w') as fo:
    print('Working',file=fo)
