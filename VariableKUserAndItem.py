### Scripted by Mohammed Jasam
### mnqnd@mst.edu

import matplotlib.pyplot as plt
import numpy as np
import subprocess
import csv
import os
import matplotlib.pylab as plt
import seaborn as sns
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

l=[]
# ################################################# Main Body ##################################################
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
                RMSE=xa[x][0]
            elif x==1:
                MAE=xa[x][0]
        del l[:]
        return v,RMSE,MAE

    elif query=='f2':
        RMSE=0.0
        MAE=0.0
        for x in range(len(xa)):
            if x==0:
                RMSE=xa[x][1]
            elif x==1:
                MAE=xa[x][1]
        del l[:]
        return v,RMSE, MAE

    elif query=='f3':
        RMSE=0.0
        MAE=0.0
        for x in range(len(xa)):
            if x==0:
                RMSE=xa[x][2]
            elif x==1:
                MAE=xa[x][2]
        del l[:]
        return v,RMSE, MAE

    elif query=='fmean':
        RMSE=0.0
        MAE=0.0
        for x in range(len(xa)):
            if x==0:
                RMSE=xa[x][3]
            elif x==1:
                MAE=xa[x][3]
        del l[:]
        return v,RMSE, MAE
# ############################################## End of Main ##########################################

VarV,Item_VarK_a,Item_VarK_b=[],[],[]
'''-------------------------------------------------------------------------------------------------------'''
print("                    Calculating RMSE and MAE of Item K Algorithm")
print("====================================================================================")
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Algorithms/")
subprocess.call('python ItemVarK.py',shell=True)
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Outputs/VarK/Item/")

for i in range(1,21):
    v,a,b=extract("ItemVarK" + str(i)+ ".csv",'fmean')
    VarV.append(v)
    Item_VarK_a.append(a)
    Item_VarK_b.append(b)

#############################################  Using K #####################################################
VarV,User_VarK_a,User_VarK_b=[],[],[]
print("                    Calculating RMSE and MAE of User K Algorithm")
print("====================================================================================")
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Algorithms/")
subprocess.call('python UserVarK.py',shell=True)
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Outputs/VarK/User/")

for i in range(1,20):
    v,a,b=extract("UserVarK" + str(i)+ ".csv",'fmean')
    VarV.append(v)
    User_VarK_a.append(a)
    User_VarK_b.append(b)

import matplotlib.pylab as plt
import seaborn as sns
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

####################################### Visualization in 3D ##############################################
x1,x2,x3,x4,y1,y2,y3,y4=[],[],[],[],[],[],[],[]
for i in range(len(User_VarK_a)):
    x1.append(i+1)
    y1.append(0)
for i in range(len(Item_VarK_a)):
    x2.append(i+1)
    y2.append(10)
for i in range(len(User_VarK_b)):
    x3.append(i+1)
    y3.append(0)
for i in range(len(Item_VarK_b)):
    x4.append(i+1)
    y4.append(10)


plt.figure(figsize=(10,6))
plt.plot(range(1,20),User_VarK_a, color = 'red',linestyle = 'dashed', marker = 'o', markerfacecolor='red',markersize=10)
plt.plot(range(1,20),User_VarK_b, color = 'blue',linestyle = 'dashed', marker = '*', markerfacecolor='blue',markersize=10)

plt.title('Error Rate vs. Value of K for User Based Collaborative Filtering Algorithm')
plt.xlabel('Value of K')
plt.ylabel('Error Rate')
plt.show()

plt.figure(figsize=(10,6))
plt.plot(range(1,20),User_VarK_a, color = 'red',linestyle = 'dashed', marker = 'o', markerfacecolor='red',markersize=10)
plt.plot(range(1,20),User_VarK_b, color = 'blue',linestyle = 'dashed', marker = '*', markerfacecolor='blue',markersize=10)

plt.title('Error Rate vs. Value of K for Item Based Collaborative Filtering Algorithm')
plt.xlabel('Value of K')
plt.ylabel('Error Rate')
plt.show()


fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')

ax.plot_wireframe(x1,y1,User_VarK_a, label='User Algo RMSE for Varying K',linestyle='--', color='red')
ax.plot_wireframe(x2,y2,Item_VarK_a,label='User Algo RMSE for Varying K')
ax.plot_wireframe(x3,y3,User_VarK_b,label='User Algo RMSE for Varying K', color='red', linestyle='--')
ax.plot_wireframe(x4,y4,Item_VarK_b,label='User Algo RMSE for Varying K')

plt.show()
