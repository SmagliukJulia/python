import numpy as np

print("y=np.log(1)+x**2( (1/(np.e)**(np.sin(x))+1)/(5/4+1/x**15) )")

x=1

a=np.log(1)
b=x**2
c=(1/(np.e)**(np.sin(x))+1)
d=(5/4+1/x**15)
result=a+b*(c/d)
print("y(1)= ", result)


x1=10

a1=np.log(1)
b1=x1**2
c1=(1/(np.e)**(np.sin(x1))+1)
d1=(5/4+1/x1**15)
result1=a1+b1*(c1/d1)
print("y(10)= ", result1)


x2=1000

a2=np.log(1)
b2=x2**2
c2=(1/(np.e)**(np.sin(x2))+1)
d2=(5/4+1/x2**15)
result2=a2+b2*(c2/d2)
print("y(1000)= ", result2)
