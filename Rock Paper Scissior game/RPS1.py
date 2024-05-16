import random

print("To chaliye shuru karte hai")
while True:
    print("\n1:Phatar \n2:Kagad \n3:Kaichi")
    choice = int(input("Bol: "))
    while choice > 3 or choice < 1:
        choice = int(input("Aagao mat chal :-) "))

    if choice == 1:
        choice_name = "Phatar"
    elif choice == 2:
        choice_name = "Kagad"
    else:
        choice_name = "Kaichi"



    print("Tum ne chuna :", choice_name)
    print("Ab opponent choose karega")
    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = "PHATAR1"
    elif comp_choice == 2:
        comp_choice_name = "KAGAD1"
    else:
        comp_choice_name = "KAICHI1"

        # Existing logic to check for tie and results
    if choice == comp_choice_name:
        print("Are Same ho gaya")
        result = "Draw"

    if (choice == 1 and comp_choice == 2):
        print("Kagad Jeet gaya ")
        result = "Kagad"
    elif (choice == 2 and comp_choice == 1):
        print("KAGAD1 Jeet gaya")
        result = "KAGAD1"

    if (choice == 1 and comp_choice == 3):
        print('Phatar jeet gaya \n')
        result = "Phatar"
    elif (choice == 3 and comp_choice == 1):
        print('PHATAR1 wins \n')
        result = "PHATAR1"

    if (choice == 2 and comp_choice == 3):
        print('Kaichi jeet gayi ')
        result = "Kaichi"
    elif (choice == 3 and comp_choice == 2):
        print('KAICHI1 jeet gayi ')
        result = "KAICHI1"

    print("Computer ne chunna \n", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)

    if result == "Draw":
        print("Tie ho gaya")
    if result == choice_name:
        print("Tum jeet gaye")
    else:
        print("Computer jeet gaya")

    # Existing logic to print result based on the outcome

    print("Fhir se khelna hai? Y/N")
    ans = input().lower()
    if ans == "n":
        break
print("Thik hai fhir bye")
