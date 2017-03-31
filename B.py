RMSE_UserItemGen_VarK=[]
MAE_UserItemGen_VarK=[]
Item_VarK_a_list=[]
Item_VarK_b_list=[]
'''-------------------------------------------------------------------------------------------------------'''
print("                    Calculating RMSE and MAE of Item K Algorithm")
print("====================================================================================")
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Algorithms/")
subprocess.call('python ItemK.py',shell=True)
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Outputs/")
for i in range(1,21):
    v,Item_VarK_a,Item_VarK_b=extract("ItemVarK" + str(i)+ ".csv",'fmean')
    Item_VarK_a_list.append(Item_VarK_a)
    Item_VarK_b_list.append(Item_VarK_b)
    # print(a,b)
    VarV.append(v)
print(v)
Viz(v,'ItemK')

User_VarK_a_list=[]
User_VarK_b_list=[]
#############################################  Using K #####################################################
VarV,User_VarK_a,User_VarK_b=[],[],[]
print("                    Calculating RMSE and MAE of User K Algorithm")
print("====================================================================================")
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Algorithms/")
subprocess.call('python UserK.py',shell=True)
os.chdir("C:/Users/Stark/Desktop/Programming/Everythin_else!/Work/Current/Recommender-System/Outputs/VarK/User/")
for i in range(1,21):
    v,User_VarK_a,User_VarK_b=extract("UserVarK" + str(i)+ ".csv",'fmean')
    VarV.append(v)
    User_VarK_a_list.append(User_K_a)
    User_VarK_b_list.append(User_K_b)


# RMSE_UserItemGen_VarK=[]
# MAE_UserItemGen_VarK=[]
# Appending the Fold Values to a list to visualize!
RMSE_UserItemGen_VarK.append(User_VarK_a_list)
RMSE_UserItemGen_VarK.append(Item_VarK_a_list)

MAE_UserItemGen_VarK.append(User_VarK_b_list)
MAE_UserItemGen_VarK.append(Item_VarK_b_list)
# MAE_UserItemGen.append([User_fmean_b,User_MSD_b,User_Cosine_b,User_Pearson_b,User_K_b])
# MAE_UserItemGen.append([Item_fmean_b,Item_MSD_b,Item_Cosine_b,Item_Pearson_b,Item_K_b])
#
VizCompare(RMSE_UserItemGen_VarK,'RMSE')
