n1, n2 = 12, 20
if (n1 > n2):
    max = n1
else:
    max = n2
print('max 1:', max)

while(True):
    if(max % n1 ==0 and max % n2 ==0):
        print(max)
        break;
    max = max +1

print('Canana: ', 20 % 20)
