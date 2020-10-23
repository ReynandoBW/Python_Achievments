<<<<<<< HEAD
import os
nummer1 = 0
nummer2 = 0
antwoord = 0
watTeDoen = ""
isRunning = True

print("toets een nummer in")
nummer1 = int(input())
os.system("cls")

print(nummer1)
print("wat wil je gaan doen?")
watTeDoen = input()
os.system("cls")

print(nummer1, watTeDoen)
print("toets nog een nummer in")
nummer2 = int(input())
os.system("cls")

while (isRunning == True):
    if (watTeDoen == "+" or watTeDoen == "plus"):
        sum = nummer1 + nummer2
        antwoord = sum
        print(nummer1, watTeDoen, nummer2, "=")
        print(antwoord)
    
    elif (watTeDoen == "-" or watTeDoen == "min"):
        sum = nummer1 - nummer2
        antwoord = sum
        print(nummer1, watTeDoen, nummer2, "=")
        print(antwoord)
    
    elif (watTeDoen == "*" or watTeDoen == "x" or watTeDoen == "keer"):
        sum = nummer1 * nummer2
        antwoord = sum
        print(nummer1, watTeDoen, nummer2, "=")
        print(antwoord)
    
    elif (watTeDoen == "/" or watTeDoen == "gedeeld door" or watTeDoen == "delen"):
        sum = nummer1 / nummer2
        antwoord = sum
        print(nummer1, watTeDoen, nummer2, "=")
        print(antwoord)
    
    elif (watTeDoen == "%" or watTeDoen == "molulo"):
        sum = nummer1 % nummer2
        antwoord = sum
        print(nummer1, watTeDoen, nummer2, "=")
        print(antwoord)

    else:
        print("invalid input")
        break
    
    print("wat wil je doen?")
    watTeDoen = input()
    os.system("cls")

    if (watTeDoen == "quit"):
        break

    nummer1 = antwoord
    print(nummer1, watTeDoen)

    print("toets nog een nummer in")
    nummer2 = int(input())
    os.system("cls")
=======
import os
nummer1 = 0
nummer2 = 0
antwoord = 0
watTeDoen = ""
isRunning = True

print("toets een nummer in")
nummer1 = int(input())
os.system("cls")

print(nummer1)
print("wat wil je gaan doen?")
watTeDoen = input()
os.system("cls")

print(nummer1, watTeDoen)
print("toets nog een nummer in")
nummer2 = int(input())
os.system("cls")

while (isRunning == True):
    if (watTeDoen == "+" or watTeDoen == "plus"):
        sum = nummer1 + nummer2
        antwoord = sum
        print(nummer1, watTeDoen, nummer2, "=")
        print(antwoord)
    
    elif (watTeDoen == "-" or watTeDoen == "min"):
        sum = nummer1 - nummer2
        antwoord = sum
        print(nummer1, watTeDoen, nummer2, "=")
        print(antwoord)
    
    elif (watTeDoen == "*" or watTeDoen == "x" or watTeDoen == "keer"):
        sum = nummer1 * nummer2
        antwoord = sum
        print(nummer1, watTeDoen, nummer2, "=")
        print(antwoord)
    
    elif (watTeDoen == "/" or watTeDoen == "gedeeld door" or watTeDoen == "delen"):
        sum = nummer1 / nummer2
        antwoord = sum
        print(nummer1, watTeDoen, nummer2, "=")
        print(antwoord)
    
    elif (watTeDoen == "%" or watTeDoen == "molulo"):
        sum = nummer1 % nummer2
        antwoord = sum
        print(nummer1, watTeDoen, nummer2, "=")
        print(antwoord)

    else:
        print("invalid input")
        break
    
    print("wat wil je doen?")
    watTeDoen = input()
    os.system("cls")

    if (watTeDoen == "quit"):
        break

    nummer1 = antwoord
    print(nummer1, watTeDoen)

    print("toets nog een nummer in")
    nummer2 = int(input())
    os.system("cls")
>>>>>>> b970f5bc7237e514d5a902e0996bde9266fa4fa6
