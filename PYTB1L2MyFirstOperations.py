nummer1 = 0
nummer2 = 0
antwoord = 0
watTeDoen = ""

print("toets een nummer in")
nummer1 = int(input())
print(nummer1)

watTeDoen = input()

prit("
print(watTeDoen)

print("toets nog een nummer in")
nummer2 = int(input())

if (watTeDoen == "+"):
    sum = nummer1 + nummer2
    print(sum)

elif (watTeDoen == "-"):
    sum = nummer1 - nummer2
    print(sum)

elif (watTeDoen == "*" or watTeDoen == "x"):
    sum = nummer1 * nummer2
    print(sum)

elif (watTeDoen == "/"):
    sum = nummer1 / nummer2
    print(sum)
