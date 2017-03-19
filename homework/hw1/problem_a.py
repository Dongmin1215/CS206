from ast import literal_eval

exp = []    #다항식에서의 차수
coef= []    #다항식에서의 계수
plus = []   #최종 다항식
poly_1 = literal_eval(input("polynomial 1: "))  #사용자로부터 다항식의 요소를 입력받음


for x,y in poly_1:
    if x==0:         #차수가 0인경우
        plus.append("%d" %y)
    elif x==1:       #차수가 1인 경우
        plus.append("%dx" %y)
    else:            #차수가 0,1이 아닌경우
        plus.append("%dx**%d" %(y,x))


poly = "+".join(plus)
print("p(x) = " + poly)
