import turtle


turtle.shape('turtle')


k=1
fi_rad=0.1
fi_degr=fi_rad*(180/3.14)
for i in range (0,1000):
    r=k*fi_rad
    turtle.forward(r)
    turtle.left(fi_degr)
    fi_rad+=0.1
    r+=r
