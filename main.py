import numpy as np
import matplotlib.pyplot as plt
import json
import pprint
# for equation Ax^a + By^b + Cz^c = D
print("enter the equation in the form of (Ax^a + By^b + Cz^c = D) as A B C D a b c")

#A = int(input())
#B = int(input())
#C = int(input())
#D = int(input())
#a = int(input())
#b = int(input())
#c = int(input())
A = 1
B = 1
C = 1
D = 1
a = 2
b = 2
c = 1
xlist = np.linspace(-10000,10000,1000)
ylist = np.linspace(-10000,10000,1000)
X,Y = np.meshgrid(xlist,ylist);
xa = np.power(X,a)
yb = np.power(Y,b)
Axa = A*xa
Byb = B*yb
d = np.eye(1000)*D;
#print(Axa.shape)
#print(d.shape)
Z = np.power(d-(Axa+Byb) ,1/c)
#print(X.shape)
plt.figure()
#cp = plt.contour(X,Y,Z)
#plt.show()
with open("data") as f:
    for line in f:
        for word in line.split("\n"):
            data = json.loads(word)
            for x in data:
                plt.plot(*zip(*x), marker='o', color='r', ls='')
                cp = plt.contour(X,Y,Z)
                plt.show()

#a=[[1,2],[3,3],[4,4],[5,2]]
#a=[[0,0]]
#plt.plot(*zip(*a), marker='o', color='r', ls='')
#plt.show()
