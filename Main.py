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
def Viz(l,v):
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
    if v=='SVD':
        plt.title('RMSE and MAE Values on Different Folds using SVD Algorithm')
    elif v=='PMF':
        plt.title('RMSE and MAE Values on Different Folds using PMF Algorithm')
    elif v=='NMF':
        plt.title('RMSE and MAE Values on Different Folds using NMF Algorithm')
    elif v=='User':
        plt.title('RMSE and MAE Values on Different Folds using User Algorithm')
    elif v=='Item':
        plt.title('RMSE and MAE Values on Different Folds using Item Algorithm')

    plt.xticks(y_pos + bar_width, ("Fold 1","Fold 2","Fold 3","Fold Mean"))
    plt.legend()
    plt.tight_layout()
    plt.show()
##########################################################################################################################

# v=[]
##########---Generates Fold Performance of the Algorithms!!!---###########
#Code which is used to extract Folds!
def extract(filename,query):
    v=[]
    with open(filename, "r") as fp_in:
        reader = csv.reader(fp_in, delimiter="\t")
        header = next(reader)

        for row in reader:
            x=row[0]
            l.append(x[8:].split())## Removes the Initial String
    xa=[]
    for i in range(len(l)):
        xa.append([float(x) for x in l[i]])
    v=xa
    if query=='f1':
        RMSE=0.0
        MAE=0.0
        for x in range(len(xa)):
            if x==0:
                # print("RMSE "+str(xa[x][0]))
                RMSE=xa[x][0]
            elif x==1:
                # print("MAE  "+str(xa[x][0]))
                MAE=xa[x][0]
        del l[:]
        return v,RMSE,MAE

    elif query=='f2':
        RMSE=0.0
        MAE=0.0
        for x in range(len(xa)):
            if x==0:
                # print("RMSE "+str(xa[x][1]))
                RMSE=xa[x][1]
            elif x==1:
                # print("MAE  "+str(xa[x][1]))
                MAE=xa[x][1]
        del l[:]
        return v,RMSE, MAE

    elif query=='f3':
        RMSE=0.0
        MAE=0.0
        for x in range(len(xa)):
            if x==0:
                # print("RMSE "+str(xa[x][2]))
                RMSE=xa[x][2]
            elif x==1:
                # print("MAE  "+str(xa[x][2]))
                MAE=xa[x][2]
        del l[:]
        return v,RMSE, MAE

    elif query=='fmean':
        RMSE=0.0
        MAE=0.0
        for x in range(len(xa)):
            if x==0:
                # print("RMSE "+str(xa[x][3]))
                RMSE=xa[x][3]
            elif x==1:
                # print("MAE  "+str(xa[x][3]))
                MAE=xa[x][3]
        del l[:]
        return v,RMSE, MAE


        ### Call the function name!!! ###
### The function returns RMSE and MAE Values!! ###
## To print, pass f1,f2,f3 or fmean below for respective FOLD values ###

Fold1=[]
Fold2=[]
Fold3=[]
FoldMeans=[]
'''-------------------------------------------------------------------------------------------------------'''
print("                    Calculating RMSE and MAE of SVD Algorithm")
print("====================================================================================")
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Algorithms/")
subprocess.call('python SVD.py',shell=True)
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Outputs/")
v,SVD_f1_a,SVD_f1_b=extract("SVD.csv",'f1')    ### Parameters: f1=FOLD1 ;  f2=FOLD2  ;  f3=FOLD3  ;  fmean=Mean of 3-FOLDS
# Fold1.append([SVD_f1_a,SVD_f1_b])
v,SVD_f2_a,SVD_f2_b=extract("SVD.csv",'f2')
# Fold2.append([SVD_f2_a,SVD_f2_b])
v,SVD_f3_a,SVD_f3_b=extract("SVD.csv",'f3')
# Fold3.append([SVD_f3_a,SVD_f3_b])
v,SVD_fmean_a,SVD_fmean_b=extract("SVD.csv",'fmean')
# FoldMeans.append([SVD_fmean_a,SVD_fmean_b])


print("\nFold 1 values")
print("=====================")
print("RMSE "+str(SVD_f1_a))
print("MAE  "+str(SVD_f1_b))
print("\nFold 2 values")
print("=====================")
print("RMSE "+str(SVD_f2_a))
print("MAE  "+str(SVD_f2_b))
print("\nFold 3 values")
print("=====================")
print("RMSE "+str(SVD_f3_a))
print("MAE  "+str(SVD_f3_b))
print("\nMean of 3-Fold values")
print("=====================")
print("RMSE "+str(SVD_fmean_a))
print("MAE  "+str(SVD_fmean_b))
Viz(v,'SVD')
'''-------------------------------------------------------------------------------------------------------'''


# '''-------------------------------------------------------------------------------------------------------'''
print("                    Calculating RMSE and MAE of PMF Algorithm")
print("====================================================================================")
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Algorithms/")
subprocess.call('python PMF.py',shell=True)
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Outputs/")
v,PMF_f1_a,PMF_f1_b=extract("PMF.csv",'f1')    ### Parameters: f1=FOLD1 ;  f2=FOLD2  ;  f3=FOLD3  ;  fmean=Mean of 3-FOLDS
# Fold1.append([PMF_f1_a,PMF_f1_b])
v,PMF_f2_a,PMF_f2_b=extract("PMF.csv",'f2')
# Fold2.append([PMF_f2_a,PMF_f2_b])
v,PMF_f3_a,PMF_f3_b=extract("PMF.csv",'f3')
# Fold3.append([PMF_f3_a,PMF_f3_b])
v,PMF_fmean_a,PMF_fmean_b=extract("PMF.csv",'fmean')
# FoldMeans.append([PMF_fmean_a,PMF_fmean_b])
print("\nFold 1 values")
print("=====================")
print("RMSE "+str(PMF_f1_a))
print("MAE  "+str(PMF_f1_b))
print("\nFold 2 values")
print("=====================")
print("RMSE "+str(PMF_f2_a))
print("MAE  "+str(PMF_f2_b))
print("\nFold 3 values")
print("=====================")
print("RMSE "+str(PMF_f3_a))
print("MAE  "+str(PMF_f3_b))
print("\nMean of 3-Fold values")
print("=====================")
print("RMSE "+str(PMF_fmean_a))
print("MAE  "+str(PMF_fmean_b))
Viz(v,'PMF')
# '''-------------------------------------------------------------------------------------------------------'''
#
#
# '''-------------------------------------------------------------------------------------------------------'''
print("                    Calculating RMSE and MAE of NMF Algorithm")
print("====================================================================================")
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Algorithms/")
subprocess.call('python NMF.py',shell=True)
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Outputs/")
v,NMF_f1_a,NMF_f1_b=extract("NMF.csv",'f1')    ### Parameters: f1=FOLD1 ;  f2=FOLD2  ;  f3=FOLD3  ;  fmean=Mean of 3-FOLDS
# Fold1.append([NMF_f1_a,NMF_f1_b])
v,NMF_f2_a,NMF_f2_b=extract("NMF.csv",'f2')
# Fold2.append([NMF_f2_a,NMF_f2_b])
v,NMF_f3_a,NMF_f3_b=extract("NMF.csv",'f3')
# Fold3.append([NMF_f3_a,NMF_f3_b])
v,NMF_fmean_a,NMF_fmean_b=extract("NMF.csv",'fmean')
# FoldMeans.append([NMF_fmean_a,NMF_fmean_b])
print("\nFold 1 values")
print("=====================")
print("RMSE "+str(NMF_f1_a))
print("MAE  "+str(NMF_f1_b))
print("\nFold 2 values")
print("=====================")
print("RMSE "+str(NMF_f2_a))
print("MAE  "+str(NMF_f2_b))
print("\nFold 3 values")
print("=====================")
print("RMSE "+str(NMF_f3_a))
print("MAE  "+str(NMF_f3_b))
print("\nMean of 3-Fold values")
print("=====================")
print("RMSE "+str(NMF_fmean_a))
print("MAE  "+str(NMF_fmean_b))
Viz(v,'NMF')
'''-------------------------------------------------------------------------------------------------------'''
#
#
'''-------------------------------------------------------------------------------------------------------'''
print("                    Calculating RMSE and MAE of User Algorithm")
print("====================================================================================")
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Algorithms/")
subprocess.call('python User.py',shell=True)
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Outputs/")
v,User_f1_a,User_f1_b=extract("User.csv",'f1')    ### Parameters: f1=FOLD1 ;  f2=FOLD2  ;  f3=FOLD3  ;  fmean=Mean of 3-FOLDS
# Fold1.append([User_f1_a,User_f1_b])
v,User_f2_a,User_f2_b=extract("User.csv",'f2')
# Fold2.append([User_f2_a,User_f2_b])
v,User_f3_a,User_f3_b=extract("User.csv",'f3')
# Fold3.append([User_f3_a,User_f3_b])
v,User_fmean_a,User_fmean_b=extract("User.csv",'fmean')
# FoldMeans.append([User_fmean_a,User_fmean_b])
print("\nFold 1 values")
print("=====================")
print("RMSE "+str(User_f1_a))
print("MAE  "+str(User_f1_b))
print("\nFold 2 values")
print("=====================")
print("RMSE "+str(User_f2_a))
print("MAE  "+str(User_f2_b))
print("\nFold 3 values")
print("=====================")
print("RMSE "+str(User_f3_a))
print("MAE  "+str(User_f3_b))
print("\nMean of 3-Fold values")
print("=====================")
print("RMSE "+str(User_fmean_a))
print("MAE  "+str(User_fmean_b))
Viz(v,'User')
'''-------------------------------------------------------------------------------------------------------'''


'''-------------------------------------------------------------------------------------------------------'''
print("                    Calculating RMSE and MAE of Item Algorithm")
print("====================================================================================")
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Algorithms/")
subprocess.call('python Item.py',shell=True)
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Outputs/")
v,Item_f1_a,Item_f1_b=extract("Item.csv",'f1')    ### Parameters: f1=FOLD1 ;  f2=FOLD2  ;  f3=FOLD3  ;  fmean=Mean of 3-FOLDS
# Fold1.append([Item_f1_a,Item_f1_b])
v,Item_f2_a,Item_f2_b=extract("Item.csv",'f2')
# Fold2.append([Item_f2_a,Item_f2_b])
v,Item_f3_a,Item_f3_b=extract("Item.csv",'f3')
# Fold3.append([Item_f3_a,Item_f3_b])
v,Item_fmean_a,Item_fmean_b=extract("Item.csv",'fmean')
# FoldMeans.append([Item_fmean_a,Item_fmean_b])
print("\nFold 1 values")
print("=====================")
print("RMSE "+str(Item_f1_a))
print("MAE  "+str(Item_f1_b))
print("\nFold 2 values")
print("=====================")
print("RMSE "+str(Item_f2_a))
print("MAE  "+str(Item_f2_b))
print("\nFold 3 values")
print("=====================")
print("RMSE "+str(Item_f3_a))
print("MAE  "+str(Item_f3_b))
print("\nMean of 3-Fold values")
print("=====================")
print("RMSE "+str(Item_fmean_a))
print("MAE  "+str(Item_fmean_b))
Viz(v,'Item')
# '''-------------------------------------------------------------------------------------------------------'''

Fold1.append([SVD_f1_a,PMF_f1_a,NMF_f1_a,User_f1_a,Item_f1_a])
Fold1.append([SVD_f1_b,PMF_f1_b,NMF_f1_b,User_f1_b,Item_f1_b])

Fold2.append([SVD_f2_a,PMF_f2_a,NMF_f2_a,User_f2_a,Item_f2_a])
Fold2.append([SVD_f2_b,PMF_f2_b,NMF_f2_b,User_f2_b,Item_f2_b])

Fold3.append([SVD_f3_a,PMF_f3_a,NMF_f3_a,User_f3_a,Item_f3_a])
Fold3.append([SVD_f3_b,PMF_f3_b,NMF_f3_b,User_f3_b,Item_f3_b])

FoldMeans.append([SVD_fmean_a,PMF_fmean_a,NMF_fmean_a,User_fmean_a,Item_fmean_a])
FoldMeans.append([SVD_fmean_b,PMF_fmean_b,NMF_fmean_b,User_fmean_b,Item_fmean_b])

# print(Fold1)
##################################################### VIZ COMPARE ######################################################
def VizCompare(FL,v):
    # print(FL)
    a,b=FL[0],FL[1]
    # data to plot
    n_groups = 4
    # create plot

    objects = ("a","b","c","d","e")#(1,2,3,4)
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
    if v=='f1':
        plt.title('RMSE and MAE Values of Various Algorithms on Fold 1')
    elif v=='f2':
        plt.title('RMSE and MAE Values of Various Algorithms on Fold 2')
    elif v=='f3':
        plt.title('RMSE and MAE Values of Various Algorithms on Fold 3')
    elif v=='fmean':
        plt.title('RMSE and MAE Values of Various Algorithms on Mean of 3-Fold')

    # plt.title('Comparing RMSE and MAE for different Algorithms on Fold 1')
    plt.xticks(y_pos + bar_width, ("SVD","PMF","NMF","User","Item"))
    plt.legend()
    plt.tight_layout()
    plt.show()
# print(Fold1)
VizCompare(Fold1,'f1')
VizCompare(Fold2,'f2')
VizCompare(Fold3,'f3')
VizCompare(FoldMeans,'fmean')
