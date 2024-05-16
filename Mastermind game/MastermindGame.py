import random
num = random.randrange(1000,10000)
n = int(input("Tukka maro 4 digit ka: "))
if (n == num):
    print("Zarbardast kaam hai tumhara bakki ek hi baar me sahi kadak: ")
else:
    tukkeNum = 0
    while (n != num):
        tukkeNum +=1
        count = 0
        n = str(n)
        num =str(num)
        sahi = ["x"]*4
        for i in range(0,4):
            if (n[i] == num[i]):
                count+=1
                sahi[i]=n
            else:
                continue

        print("galat number hai chaalo koi nahi koshish kiya bohat hai, aur ",count,"digit barabarr aaye vaise\n\n")
        n = int(input("Agla tukka mar"))

        if (count == 0):
            print("Ek bhi number match nahi hua")
            n = int(input("Agla tukka mar: "))
        if n==num:
            tukkeNum+=1
            print("Tum to mastermind ho sir")
            print("Aur tumko sirf ",tukkeNum," tukke lage")






