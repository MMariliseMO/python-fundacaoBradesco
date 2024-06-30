#criar um programa para cálculo de média de notas. No programa, o usuário deverá digitar duas notas para o aluno. Na sequência, o programa irá calcular e exibir a média, informando se o aluno está aprovado (média maior ou igual a 7.0) ou reprovado.O programa deverá ter uma função para leitura das notas e outra, para cálculo da média.

def lerNotas(): #a palavra def determina o inicio da função
    nota = float(input("Digite a nota do aluno(a): "))
    return nota #é usado para retornar alguma informação para ação da função


def resultado(nota1, nota2):
    media = (nota1 + nota2)/2
    print("Nota 1: ", nota1)
    print("Nota 2: ", nota2)
    print("A média do aluno(a) é: ", media, "Resultado: ", end="") #O argumento end="" no final do print impede que uma nova linha seja adicionada após esta linha, permitindo que o resultado (aprovado ou reprovado) seja exibido na mesma linha.
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")


nota1 = lerNotas()
nota2 = lerNotas()
resultado(nota1, nota2)