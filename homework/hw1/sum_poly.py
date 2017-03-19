from ast import literal_eval

plus_1 = []
plus_2 =[]
plus = []
same = []

exp_1 =[]
coef_1 = []
exp_2 = []
coef_2 = []
same_coef_1 = []
same_coef_2 = []
sum_coef = []

poly_1 = literal_eval(input("polynomial 1: "))
for i in range(len(poly_1)):
    exp_1.append(poly_1[i][0])
    coef_1.append(poly_1[i][1])

list_poly_1 = list(poly_1) #튜플에 튜플로 되어 있는 것을 리스트로 바꿈 


raw_data = input("+, *, ' : ")

if (raw_data == "+") or (raw_data == "*"):
    poly_2 = literal_eval(input("polynomial 2: "))

    for i in range(len(poly_2)):
        exp_2.append(poly_2[i][0])
        coef_2.append(poly_2[i][0])

    list_poly_2 = list(poly_2)

list_poly_1 = list(poly_1)



alone_exp_1 = []
alone_coef_1 = []
alone_exp_2 = []
alone_coef_2 = []

list_mul_exp = []
list_mul_coef = []
copy_list_mul_exp = []
after_list_mul_coef = []
after_list_mul_exp = []
n1 = 0
mul_exp = 0
mul_coef = 0

der_exp = []
der_coef = []

if raw_data == "+":
    for i in range(11): #since the exp is under 10
        if (i in exp_1) and (i in exp_2):
            same.append(i)

    for i in range(len(same)):
        for j in range(len(exp_1)):
            if same[i] == exp_1[j]:
                same_coef_1.append(coef_1[j])
        for r in range(len(exp_2)):
            if same[i] == exp_2[r]:
                same_coef_2.append(coef_2[r])

    for i in range(len(same)):
        sum_coef.append(same_coef_1[i]+same_coef_2[i]) #appending the sum of the coeficient (same power)

    for i in range(len(same)):
        if same[i] == 0:
            plus.append("%d" %(sum_coef[i]))
        elif same[i] == 1:
            plus.append("%dx" %(sum_coef[i]))
        else:
            plus.append("%dx**%d" %(sum_coef[i], same[i]))

    for i in range(len(exp_1)):
        if not exp_1[i] in same:
            alone_exp_1.append(exp_1[i])
            alone_coef_1.append(exp_1[i])
    for i in range(len(exp_2)):
        if not exp_2[i] in same:
            alone_exp_2.append(exp_2[i])
            alone_coef_2.append(exp_2[i])

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


elif raw_data == "*":
    for s in range(len(list_poly_1)):
        for t in range(len(list_poly_2)):
            x,y = list_poly_1[s]
            i,j = list_poly_2[t]
            mul_exp = x + i
            mul_coef = y * j
            list_mul_exp.append(mul_exp)
            list_mul_coef.append(mul_coef)


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

    for i in range(len(after_list_mul_exp)):
        if after_list_mul_exp[i] == 0:
            plus.append("%d" %(after_list_mul_coef[i]))
        elif after_list_mul_exp[i] == 1:
            plus.append("%dx" %(after_list_mul_coef[i]))
        else:
            plus.append("%dx**%d" %(after_list_mul_coef[i], after_list_mul_exp[i]))

    print("p(x) = " + "+".join(plus))

elif raw_data == "'":
    for i in range(len(exp_1)):
        if not (exp_1[i] == 0):
            x,y = list_poly_1[i]
            new_coef = x * y
            new_exp = x-1
            der_exp.append(new_exp)
            der_coef.append(new_coef)
    for j in range(len(der_exp)):
        if der_exp[j] ==0:
            plus.append("%d" %(der_coef[j]))
        elif der_exp[j] == 1:
            plus.append("%dx" %(der_coef[j]))
        else:
            plus.append("%dx**%d" %(der_coef[j], der_exp[j]))

    print("p'(x) = " + "+".join(plus))


