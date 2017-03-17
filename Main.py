### Scripted by Mohammed Jasam
### mnqnd@mst.edu


import csv
import os
import subprocess

import numpy as np
import matplotlib.pyplot as plt

l=[]
viz=[]



########################################## VISUALIZATION ##########################################
def Viz(l):
    a=l[0]
    b=l[1]

    # data to plot
    n_groups = 4
    # create plot

    objects = ("Fold 1","Fold 2","Fold 3","Fold Mean")#(1,2,3,4)
    y_pos = np.arange(len(objects))
    fig, ax = plt.subplots()
    # index = np.arange(n_groups)
    bar_width = 0.3
    opacity = 0.8

    rects1 = plt.bar(y_pos, a, bar_width,
                     alpha=opacity,
                     color='b',
                     label='RMSE')
    rects3 = plt.bar(y_pos + bar_width, b, bar_width,
                     alpha=opacity,
                     color='g',
                     label='MAE')

    plt.xlabel('Folds')
    plt.ylabel('Accuracy')
    plt.title('RMSE and MAE Values on different folds')
    plt.xticks(y_pos + bar_width, ("Fold 1","Fold 2","Fold 3","Fold Mean"))
    plt.legend()
    plt.tight_layout()
    plt.show()
##########################################################################################################################


##########---Generates Fold Performance of the Algorithms!!!---###########
#Code which is used to extract Folds!
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
    Viz(xa)

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
        print("=====================")
        for x in range(len(xa)):
            if x==0:
                print("RMSE "+str(xa[x][3]))
                RMSE=xa[x][3]
            elif x==1:
                print("MAE  "+str(xa[x][3]))
                MAE=xa[x][3]
        del l[:]
        return RMSE, MAE
    # viz=xa
    print(xa)
    return(viz)



        ### Call the function name!!! ###
### The function returns RMSE and MAE Values!! ###
## To print, pass f1,f2,f3 or fmean below for respective FOLD values ###

FoldList=[]
'''-------------------------------------------------------------------------------------------------------'''
print("                    Calculating RMSE and MAE of SVD Algorithm")
print("====================================================================================")
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Algorithms/")
subprocess.call('python SVD.py',shell=True)
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Outputs/")
SVD_a,SVD_b=extract("SVD.csv",'fmean')    ### Parameters: f1=FOLD1 ;  f2=FOLD2  ;  f3=FOLD3  ;  fmean=Mean of 3-FOLDS
print()
# FoldList.append([a,b])
'''-------------------------------------------------------------------------------------------------------'''


'''-------------------------------------------------------------------------------------------------------'''
print("                    Calculating RMSE and MAE of PMF Algorithm")
print("====================================================================================")
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Algorithms/")
subprocess.call('python PMF.py',shell=True)
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Outputs/")
PMF_a,PMF_b=extract("PMF.csv",'fmean')    ### Parameters: f1=FOLD1 ;  f2=FOLD2  ;  f3=FOLD3  ;  fmean=Mean of 3-FOLDS
print()
# FoldList.append([a,b])
'''-------------------------------------------------------------------------------------------------------'''


'''-------------------------------------------------------------------------------------------------------'''
print("                    Calculating RMSE and MAE of NMF Algorithm")
print("====================================================================================")
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Algorithms/")
subprocess.call('python NMF.py',shell=True)
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Outputs/")
NMF_a,NMF_b=extract("NMF.csv",'fmean')    ### Parameters: f1=FOLD1 ;  f2=FOLD2  ;  f3=FOLD3  ;  fmean=Mean of 3-FOLDS
print()
# FoldList.append([a,b])
'''-------------------------------------------------------------------------------------------------------'''


'''-------------------------------------------------------------------------------------------------------'''
print("                    Calculating RMSE and MAE of User Algorithm")
print("====================================================================================")
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Algorithms/")
subprocess.call('python User.py',shell=True)
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Outputs/")
User_a,User_b=extract("User.csv",'fmean')   ### Parameters: f1=FOLD1 ;  f2=FOLD2  ;  f3=FOLD3  ;  fmean=Mean of 3-FOLDS
print()
# FoldList.append([a,b])
'''-------------------------------------------------------------------------------------------------------'''


'''-------------------------------------------------------------------------------------------------------'''
print("                    Calculating RMSE and MAE of Item Algorithm")
print("====================================================================================")
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Algorithms/")
subprocess.call('python Item.py',shell=True)
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Outputs/")
Item_a,Item_b=extract("User.csv",'fmean')   ### Parameters: f1=FOLD1 ;  f2=FOLD2  ;  f3=FOLD3  ;  fmean=Mean of 3-FOLDS
print()
# FoldList.append([a,b])
'''-------------------------------------------------------------------------------------------------------'''

FoldList.append([SVD_a,PMF_a,NMF_a,User_a,Item_a])
FoldList.append([SVD_b,PMF_b,NMF_b,User_b,Item_b])


print(FoldList)
def VizCompare(FL):
    a,b=FL[0],FL[1]
    # data to plot
    n_groups = 4
    # create plot

    objects = ("a","b",'c','d','e')#(1,2,3,4)
    y_pos = np.arange(len(objects))
    fig, ax = plt.subplots()
    # index = np.arange(n_groups)
    bar_width = 0.3
    opacity = 0.8

    rects1 = plt.bar(y_pos, a, bar_width,
                     alpha=opacity,
                     color='b',
                     label='RMSE')
    rects3 = plt.bar(y_pos + bar_width, b, bar_width,
                     alpha=opacity,
                     color='g',
                     label='MAE')

    plt.xlabel('Algorithms')
    plt.ylabel('Value of RMSE & MAE')
    plt.title('Comparing RMSE and MAE for different Algorithms on Fold 1')
    plt.xticks(y_pos + bar_width, ("SVD","PMF","NMF","User","Item"))
    plt.legend()
    plt.tight_layout()
    plt.show()
# print(FoldList)
VizCompare(FoldList)

# print(viz)
