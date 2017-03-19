from ast import literal_eval

exp = []
coef= []
plus = []
poly_1 = literal_eval(input("polynomial 1: "))


for x,y in poly_1:
    if x==0:
        plus.append("%d" %y)
    elif x==1:
        plus.append("%dx" %y)
    else:
        plus.append("%dx**%d" %(y,x))


poly = "+".join(plus)
print("p(x) = " + poly)
