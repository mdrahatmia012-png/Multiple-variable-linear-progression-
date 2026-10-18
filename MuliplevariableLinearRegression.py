x = [1, 2, 3, 4, 5, 6, 7]
y = [3, 1, 5, 2, 7, 4, 6]

z = [2*x[i] + 3*y[i] + 1 for i in range(7)]
z=[2*x[i]+3*y[i]+1 for i in range (7)]
s=0.01
w1=0.01
w2=0.01
b=0.0
for _ in range(100):
    for i in range(len(x)):
        e=z[i]-w1*x[i]-w2*y[i]-b
        w1=w1+e*s*x[i]
        w2=w2+e*s*y[i]
        b=b+s*e

print("weight1 :",w1,"weight2 :",w2,"constant :", b)
for i in range (len(x)):
    print("Real value :",z[i],"Predicted value :",w1*x[i]+w2*y[i]+b)
