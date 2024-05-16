import random

nam = input("Naam bol tera: ")
print("Kya bolte ", nam)
words = ["karan", "aniket", "abhishek", "kamlesh", "amol", "swaraj", "deepak", "anurag", "sarvesh"]
word = random.choice(words)
print("Ye star k jagah word aaeg apna")
guesses = " "
bari = 10
while bari > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("*")
            failed += 1
    if failed == 0:
        print("jeet gaya bhai tu")
        print("word hai ye bhai ka naam: ", word)
        break
    print()
    guess = input("jo word ho sakta vo type kar: ")
    guesses += guess
    if guess not in word:
        bari -= 1
        print("galat")
        print("tere to sirf " + str(bari), " bar tukka laga sakta")
        if bari == 0:
            print("Bass ho aya maaf karna muze har gaya tu!")
