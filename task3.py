import math
a=[int(i) for i in input().split()]
n = len(a)
b = [ [0,0,0] for i in range(int(n*(n-1)/2))]

for i in range(n-1):
    for j in range(i+1,n):
        b[int(n*i - (i*(i+1)/2) + j - i-1)] = [a[i], a[j], abs(a[i] + a[j])]

my_list = [int(b[i][2]) for i in range(int(n*(n-1)/2))]
my_list.sort()
x = my_list[0]

ind_list = []
for i in range(int(n*(n-1)/2)):
    if b[i][2] == x:
        ind_list.append(i)
diff_list = []
for i in ind_list:
    d = abs(b[i][0] - b[i][1])
    diff_list.append(d)
diff_list.sort()
s_d = diff_list[0]
for i in ind_list:
    if s_d == abs(b[i][0] - b[i][1]):
        print(b[i][0], b[i][1])
    break


  





