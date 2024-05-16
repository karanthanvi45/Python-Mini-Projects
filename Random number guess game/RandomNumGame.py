import random, math
itte = int(input("chota number dal:- "))
seitta = int(input("badiya ab bada numer daal:- "))
computerKaRandomNumber = random.randint(itte, seitta)
CKRN = computerKaRandomNumber
print(f"tere pass ", round(math.log(seitta-itte+1, 2)), "bar tukka marne ka chance hai....chal chalu karte")
count = 0
while count < math.log(seitta-itte+1, 2):
    count += 1
    tukka = int(input("number bol "))
    if CKRN == tukka:
        print("Sahi pakde hai....Badhai ho", count," chance me sahi kiya tune")
        break
    elif CKRN > tukka:
        print("are bohat chota ho gaya tere number")
    elif CKRN < tukka:
        print("are bohat bada ho gaya tera number")

if count >= math.log(seitta-itte+1, 2):
    print("\nkya bate number hai "+str(CKRN))
    print("Chal koi bat nahi algi baar sahi try marna...khush rah")