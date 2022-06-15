def collatz(number):
    if number % 2 == 0:
        newNumber = int(number/2)
        print(newNumber)

    else:
        newNumber = int(3 * number + 1)
        print(newNumber)
    return newNumber


number = int(input("Digite um valor inteiro: "))

while number != 1:
    number = collatz(number)
