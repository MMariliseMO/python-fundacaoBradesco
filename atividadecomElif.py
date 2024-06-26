#classificação das idades usando o elif

idade = int(input("Informe a sua idade: "))

#classificação das idades
if idade > 18:
    print("Maior idade")
elif idade > 16:
    print("Infanto Juvenil")
else:
    print("Menor Idade")