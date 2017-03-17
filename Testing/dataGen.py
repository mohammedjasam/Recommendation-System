### Scripted by Mohammed Jasam
### mnqnd@mst.edu

##########---Generates Fold Performance of the Algorithms!!!---###########
import csv

l=[]
def extract(filename)
    f=filename
with open("Item.csv", "r") as fp_in:
    reader = csv.reader(fp_in, delimiter="\t")
    header = next(reader)

    for row in reader:
        x=row[0]
        l.append(x[8:].split())## Removes the Initial String
xa=[]
for i in range(len(l)):
    xa.append([float(x) for x in l[i]])
print(xa)

def f1():
    RMSE=0.0
    MAE=0.0
    print("Fold 1 values")
    print("=============")
    for x in range(len(xa)):
        if x==0:
            print("RMSE "+str(xa[x][0]))
            RMSE=xa[x][0]
        elif x==1:
            print("MAE  "+str(xa[x][0]))
            MAE=xa[x][0]
    return RMSE,MAE
def f2():
    RMSE=0.0
    MAE=0.0
    print("Fold 2 values")
    print("=============")
    for x in range(len(xa)):
        if x==0:
            print("RMSE "+str(xa[x][0]))
            RMSE=xa[x][0]
        elif x==1:
            print("MAE  "+str(xa[x][0]))
            MAE=xa[x][0]
    return RMSE, MAE
def f3():
    RMSE=0.0
    MAE=0.0
    print("Fold 3 values")
    print("=============")
    for x in range(len(xa)):
        if x==0:
            print("RMSE "+str(xa[x][0]))
            RMSE=xa[x][0]
        elif x==1:
            print("MAE  "+str(xa[x][0]))
            MAE=xa[x][0]
    return RMSE, MAE
def fmean():
    RMSE=0.0
    MAE=0.0
    print("Mean of 3- values")
    print("=================")
    for x in range(len(xa)):
        if x==0:
            print("RMSE "+str(xa[x][0]))
            RMSE=xa[x][0]
        elif x==1:
            print("MAE  "+str(xa[x][0]))
            MAE=xa[x][0]
    return RMSE, MAE



### Call the function name!!! ###
### The function returns RMSE and MAE Values!! ###
a,b=f( )
print(a,b)
