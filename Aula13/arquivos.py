import os

# Para criar arquivos no método antigo usava o comando de (%%writefile nome.extenção)

# Para criar um arquivo no método atual basta criar uma variável onde esse aquivo ficará aberto/alocado e com o comando open() passar 2 parâmetro o nome do arquivo + sua extenção e o formato de trabalho deste arquivo

'''
r  → Apenas leitura;
w  → Apenas escrita (caso voce abra novamente esse arquivo como apenas escrita você vai substituir todo o conteúdo do arquivo);
a  → Incrementar 
r+ → Leitura e escrita
'''

arquivo1 = open("Aula13/texto.txt", 'w')
arquivo1.write("Meu Primeiro Arquivo\n") # Sempre escreve na mesma linha até acabar o espaço da linha
arquivo1.writelines("Este é um arquivo de texto gerado por um código python") # Sempre escreve em uma linha nova
arquivo1.close() # Fecha o arquivo para o código parar de processar ele

arquivo1 = open("Aula13/texto.txt", "a")
arquivo1.writelines("\nAbrindo o arquivo pela segunda vez")
arquivo1.close()

nomeArquivo = "Aula13/teste.txt"

try:
    f = open(nomeArquivo, "r")
    print(f.read())
    f.seek(0)
    print(f.readline())
    f.seek(0)
    print(f.readlines())
    print(f.readable())
except FileNotFoundError:
    f = open(nomeArquivo, 'w')
    f.write("Meu segundo arquivo")
    f.write("\nEste arquivo é um arquivo de teste")
    f.write("\nEle contem múltiplas linhas")
finally:
    f.close()

op = input("Você deseja escluir algum arquivo:\ns → sim\nn → não\n")

if op == 's' or op == 'S':
    file = input("Escreva o nome do arquivo que deseja excluir: ")
    file_path = "Aula13/"+file
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f'Arquivo {file} foi deletado com sucesso.')
    else:
        print(f'Arquivo {file} não encontrado')
else:
    print('Ok, nenhum arquivo será deletado')