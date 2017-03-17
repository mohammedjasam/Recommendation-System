import os  # We need this module
import subprocess
### Scripted by Mohammed Jasam
### mnqnd@mst.edu

##########---Generates Fold Performance of the Algorithms!!!---###########
import csv

l=[]
# i=0
def extract(filename,query):
    with open(filename, "r") as fp_in:
        reader = csv.reader(fp_in, delimiter="\t")
        header = next(reader)

        for row in reader:
            x=row[0]
            l.append(x[8:].split())## Removes the Initial String
    xa=[]
    for i in range(len(l)):
        xa.append([float(x) for x in l[i]])
    print(xa)

    if query=='f1':
        RMSE=0.0
        MAE=0.0
        print("\nFold 1 values")
        print("=============")
        for x in range(len(xa)):
            if x==0:
                print("RMSE "+str(xa[x][0]))
                RMSE=xa[x][0]
            elif x==1:
                print("MAE  "+str(xa[x][0]))
                MAE=xa[x][0]
        del l[:]
        return RMSE,MAE

    elif query=='f2':
        RMSE=0.0
        MAE=0.0
        print("\nFold 2 values")
        print("=============")
        for x in range(len(xa)):
            if x==0:
                print("RMSE "+str(xa[x][1]))
                RMSE=xa[x][1]
            elif x==1:
                print("MAE  "+str(xa[x][1]))
                MAE=xa[x][1]
        del l[:]
        return RMSE, MAE

    elif query=='f3':
        RMSE=0.0
        MAE=0.0
        print("\nFold 3 values")
        print("=============")
        for x in range(len(xa)):
            if x==0:
                print("RMSE "+str(xa[x][2]))
                RMSE=xa[x][2]
            elif x==1:
                print("MAE  "+str(xa[x][2]))
                MAE=xa[x][2]
        del l[:]
        return RMSE, MAE

    elif query=='fmean':
        RMSE=0.0
        MAE=0.0
        print("\nMean of 3-Fold values")
        print("=================")
        for x in range(len(xa)):
            if x==0:
                print("RMSE "+str(xa[x][3]))
                RMSE=xa[x][3]
            elif x==1:
                print("MAE  "+str(xa[x][3]))
                MAE=xa[x][3]
        del l[:]
        return RMSE, MAE



### Call the function name!!! ###
### The function returns RMSE and MAE Values!! ###
print("====================================================================================")
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Algorithms/")
subprocess.call('python SVD.py',shell=True)
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Outputs/")
a,b=extract("SVD.csv",'f1')

print("====================================================================================")
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Algorithms/")
subprocess.call('python PMF.py',shell=True)
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Outputs/")
a,b=extract("PMF.csv",'fmean')

print("====================================================================================")
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Algorithms/")
subprocess.call('python NMF.py',shell=True)
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Outputs/")
a,b=extract("NMF.csv",'f1')
#
print("====================================================================================")
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Algorithms/")
subprocess.call('python User.py',shell=True)
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Outputs/")
a,b=extract("User.csv",'fmean')
# #
print("====================================================================================")
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Algorithms/")
subprocess.call('python Item.py',shell=True)
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Outputs/")
a,b=extract("User.csv",'fmean')
