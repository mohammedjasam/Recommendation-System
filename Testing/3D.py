from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt


fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')

X,Y,Z = [1,2,3,4,5,6,7],[0,0,0,0,0,0,0],[1,2,4,6,72,3,5]
X1,Y1,Z1 = [1,2,3,4,5,6,7],[0,0,0,0,0,0,0],[2,3,6,8,2,1,3]

ax.plot_wireframe(X,Y,Z)
ax.plot_wireframe(X1,Y1,Z1)


plt.show()
