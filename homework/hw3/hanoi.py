def hanoi(n,a,b,c):
    if n == 1:
        print("move 1 disk from %c to %c" %(a,c))
    else:
        hanoi(n-1,a,c,b)
        print("move %d disk from %c to %c" %(n, a, c))
        hanoi(n-1,b,a,c)

num_disks = int(input("number of the disks : "))
hanoi(num_disks,'A','B','C')

