
size = 30

for i in range(0, size):
    if i == 0 :
        print("★".center(size, ' '))
    elif i % 2 == 0 and i > 0:
        print(('*'*i).center(size, ' '))
    else :
        print(("'"*(i-1)).center(size, " "))
for y in range(1,6):
    print(" "*(size-16) + "|||")
