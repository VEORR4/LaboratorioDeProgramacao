
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    numero1, numero2 = numero2, numero1

count = 0
for num in range(numero1, numero2+1):
    if num % 2 == 0:
        count += 1

print(f"Entre {numero1} e {numero2}, há {count} números pares.")


#joao vitor tranzil amaral de souza galvao

