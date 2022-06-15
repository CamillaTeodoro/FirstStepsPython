# Trabalho de c-like
# Acelerador de particulas

print("Digite a distancia percorrida pela particula.")
distance = int(input())  # input returns a string2

if distance >= 6 and distance <= 800008:
    if distance % 8 == 0:
        print('A particula atingiu o sensor 3.')
    elif distance % 8 == 7:
        print('A particula atingiu o sensor 2.')
    elif distance % 8 == 6:
        print('A particula atingiu o sensor 1.')
    else:
        print('A particula não atingiu nenhum dos sensores.')
else:
    print("Distância fora dos parametros.")
