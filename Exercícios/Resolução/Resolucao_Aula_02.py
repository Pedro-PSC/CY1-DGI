#region Q1
frase = input("Insira uma frase aqui: ")
qntEspaco = frase.count(" ")

qnt_a = frase.count("a")
qnt_A = frase.count("A")
qntMaxA = qnt_a + qnt_A

qnt_e = frase.count("e")
qnt_E = frase.count("E")
qntMaxE = qnt_e + qnt_E

qnt_i = frase.count("i")
qnt_I = frase.count("I")
qntMaxI = qnt_i + qnt_I

qnt_o = frase.count("o")
qnt_O = frase.count("O")
qntMaxO = qnt_o + qnt_O

qnt_u = frase.count("u")
qnt_U = frase.count("U")
qntMaxU = qnt_u + qnt_U

print("\nNa sua frase existem "+str(qntEspaco)+" espaços em branco.")
print("\nNa sua frase as vogais a, e, i, o, u se repetem essa quantidade de vezes:",qntMaxA,qntMaxE,qntMaxI,qntMaxO,qntMaxU)
#endregion