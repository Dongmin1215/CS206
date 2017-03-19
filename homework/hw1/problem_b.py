from ast import literal_eval

plus_1 = []     #다항식1에서 사용자로부터 받은 튜플을 저장하기 위한 list
plus_2 =[]      #다항식2에서 사용자로부터 받은 튜플을 저장하기 위한 list
plus = []       #최종적인 다항식
same = []       #더하기 연산시  두개의 다항식에서의 공통적인 차수

exp_1 =[]       #다항식1에서의 차수
coef_1 = []     #다항식1에서의 계수
exp_2 = []      #다항식2에서의 차수
coef_2 = []     #다항식2에서의 계수
same_coef_1 = []        #두 다항식에서 공통적인 차수의 첫번째 다항식의 차수에 해당하는 계수
same_coef_2 = []        #두 다항식에서 공통적인 차수의 두번째 다항식의 차수에 해당하는  계수
sum_coef = []

poly_1 = literal_eval(input("polynomial 1: "))      #사용자로부터 튜플의 형식으로 다항식을 입력받음 
for i in range(len(poly_1)):        #사용자로부터 입력받은 튜플(차수, 계수)를 각각의 해당하는 리스트에 append
    exp_1.append(poly_1[i][0])
    coef_1.append(poly_1[i][1])

list_poly_1 = list(poly_1) #튜플에 튜플로 되어 있는 것을 리스트로 바꿈 


raw_data = input("+, *, ' : ")      #사용자로부터 연산자를 받음

if (raw_data == "+") or (raw_data == "*"):          #사용자가 다항식간의 addition 이나 multiple을 선택했을경우 두번째 다항식을 입력받음
    poly_2 = literal_eval(input("polynomial 2: "))

    for i in range(len(poly_2)):
        exp_2.append(poly_2[i][0])
        coef_2.append(poly_2[i][1])

    list_poly_2 = list(poly_2)




alone_exp_1 = []        #add 계산시 공통적인 차수를 제외한 차수(다항식1)
alone_coef_1 = []       #add 계산시 공통적인 차수를 제외한 해당하는 계수(다항식1)
alone_exp_2 = []        #add 계산시 공통적인 차수를 제외한 차수(다항식2)
alone_coef_2 = []       #add 계산시 공통적인 차수를 제외한 해당하는 계수(다항식2)

list_mul_exp = []       #곱셈계산시의 차수 
list_mul_coef = []      #곱셈 게산시의 계수
copy_list_mul_exp = []
after_list_mul_coef = []
after_list_mul_exp = []
n1 = 0                  #곱셈후 같은 차수를 가지고 있는 것들의 계수의 합을 구하기 위한 변수
mul_exp = 0
mul_coef = 0

#미분 후의 차수와 계수
der_exp = []
der_coef = []

if raw_data == "+":
    for i in range(11): #since the exp is under 10
        if (i in exp_1) and (i in exp_2):
            same.append(i)
    #공통적인 차수에 해당하는 계수를 각각의 리스트에 append 
    for i in range(len(same)):
        for j in range(len(exp_1)):
            if same[i] == exp_1[j]:
                same_coef_1.append(coef_1[j])
        for r in range(len(exp_2)):
            if same[i] == exp_2[r]:
                same_coef_2.append(coef_2[r])

    #두개의 리스트에 있는 계수들의 합을 구한뒤 새로운 리스트(이미 선언된 리스트)에 append
    for i in range(len(same)):
        sum_coef.append(same_coef_1[i]+same_coef_2[i]) #appending the sum of the coeficient (same power)

    #다항식 형태를 갖추는 단계(공통 차수의 경우)
    for i in range(len(same)):
        if same[i] == 0:
            plus.append("%d" %(sum_coef[i]))
        elif same[i] == 1:
            plus.append("%dx" %(sum_coef[i]))
        else:
            plus.append("%dx**%d" %(sum_coef[i], same[i]))

    #공통차수를 제외한 차수를 해당하는 차수와 계수를 list에 append
    for i in range(len(exp_1)):
        if not exp_1[i] in same:
            alone_exp_1.append(exp_1[i])
            alone_coef_1.append(coef_1[i])
    for i in range(len(exp_2)):
        if not exp_2[i] in same:
            alone_exp_2.append(exp_2[i])
            alone_coef_2.append(coef_2[i])

    #공통차수제외한 부분을 다항식의 형태로 갖추기
    for i in range(len(alone_exp_1)):
        if alone_exp_1[i] == 0:
            plus.append("%d" %(alone_coef_1[i]))
        elif alone_exp_1[i] == 1:
            plus.append("%dx" %(alone_coef_1[i]))
        else:
            plus.append("%dx**%d" %(alone_coef_1[i], alone_exp_1[i]))
    for i in range(len(alone_exp_2)):
        if alone_exp_2[i] == 0:
            plus.append("%d" %(alone_coef_2[i]))
        elif alone_exp_2[i] == 1:
            plus.append("%dx" %(alone_coef_2[i]))
        else:
            plus.append("%dx**%d" %(alone_coef_2[i], alone_exp_2[i]))

    print("p(x) = " + "+".join(plus))

#사용자가 곱셈연산자를 선택했을 경우
elif raw_data == "*":

    #두개의 다항식에서 각각의 항들에 대한 곱셈을 진행한 후 해당하는 새로운 차수와 계수를 list에 append
    for s in range(len(list_poly_1)):
        for t in range(len(list_poly_2)):
            x,y = list_poly_1[s]
            i,j = list_poly_2[t]
            mul_exp = x + i
            mul_coef = y * j
            list_mul_exp.append(mul_exp)
            list_mul_coef.append(mul_coef)


    #차수가 같은 위치들을 구해서 그에 해당하는 위치에 존재하는 계수들을 더하는 과정
    for i in range(len(list_mul_exp)):
        if not (list_mul_exp[i] in after_list_mul_exp):
            targ = list_mul_exp[i]
            c = [i for i,x in enumerate(list_mul_exp) if x == targ]
            for j in range(len(c)):
                place = c[j]
                n1 += list_mul_coef[place]
            after_list_mul_coef.append(n1)
            after_list_mul_exp.append(targ)
            n1 = 0

    #다항식의 형태를 만드는 과정
    for i in range(len(after_list_mul_exp)):
        if after_list_mul_exp[i] == 0:
            plus.append("%d" %(after_list_mul_coef[i]))
        elif after_list_mul_exp[i] == 1:
            plus.append("%dx" %(after_list_mul_coef[i]))
        else:
            plus.append("%dx**%d" %(after_list_mul_coef[i], after_list_mul_exp[i]))

    print("p(x) = " + "+".join(plus))

#사용자가 미분연산자를 선택했을 경우
elif raw_data == "'":
    #미분한 후의 차수와 계수를 새로운 list에 각각 append
    for i in range(len(exp_1)):
        if not (exp_1[i] == 0):
            x,y = list_poly_1[i]
            new_coef = x * y
            new_exp = x-1
            der_exp.append(new_exp)
            der_coef.append(new_coef)

    #다항식의 형태 갖추기
    for j in range(len(der_exp)):
        if der_exp[j] ==0:
            plus.append("%d" %(der_coef[j]))
        elif der_exp[j] == 1:
            plus.append("%dx" %(der_coef[j]))
        else:
            plus.append("%dx**%d" %(der_coef[j], der_exp[j]))

    print("p'(x) = " + "+".join(plus))

