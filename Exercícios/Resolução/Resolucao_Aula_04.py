'''
#region Exercício 1
print("\nExercício 1 - Mês em Inglês\n")
n = int(input("Insira um mês em número de 1 a 12: "))

if n == 1:
    print("January")
elif n == 2:
    print("February")
elif n == 3:
    print("March")
elif n == 4:
    print("April")
elif n == 5:
    print("May")
elif n == 6:
    print("June")
elif n == 7:
    print("July")
elif n == 8:
    print("August")
elif n == 9:
    print("September")
elif n == 10:
    print("October")
elif n == 11:
    print("November")
elif n == 12:
    print("December")
else:
    print("O Valor inserido não corresponde a um mês.")
#endregion
'''
print("\n")

#region Exercício 2
print("Exercício 2 - Tabela de Compras\n")

print("CÓDIGO   ESPECIFICAÇÃO       PREÇO")
print("1        Cachorro Quente     R$4,00")
print("2        X-Salada            R$4,50")
print("3        X-Bacon             R$5,00")
print("4        Torrada Simples     R$2,00")
print("5        Refrigerante        R$1,50")

print("\nEscolha um dos produtos da tabela pelo código depois insira a quantidade comprada")

c = int(input("Qual o código do produto?: "))
q = int(input("Quantos deste produto será comprado?: "))

if c == 1:
    r = 4.0*q
    r = format(r,".2f") 
    print("TOTAL: R$"+str(r))
elif c == 2:
    r = 4.5*q
    r = format(r,".2f")
    print("TOTAL: R$" + str(r))
elif c == 3:
    r = 5.0*q
    r = format(r,".2f")
    print("TOTAL: R$"+str(r))
elif c == 4:
    r = 2.0*q
    r = format(r,".2f")
    print("TOTAL: R$"+str(r))
elif c == 5:
    r = 1.6*q
    r = format(r,".2f")
    print("TOTAL: R$"+str(r))
else:
    print("Código de produto inválido\nProduto inesxistente")

#endregion
