
size = 11

for i in range(0, size):
    if i == 0 :
        print("Star".center(size, ' '))
    elif i % 2 == 0 and i > 0:
        print(('*'*i).center(size, ' '))
    else :
        print(("'"*(i-1)).center(size, " "))