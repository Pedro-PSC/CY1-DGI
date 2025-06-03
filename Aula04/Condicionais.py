# Estruturas concionais servem para na programação termos opções de comportamentos diferentes em nossos algoritimos, até agora tudo que escrevemos de comandos foram executados, porém há certos casos que queremos que taréfas específicas sejam executadas de acordo com condições específicas como por exemplo um sistema automático que identifica a nota dos alunos de uma escola e informa com base nessa nota se eles foram aprovados ou não.

# Para usar uma estrutura condicional precisamos antes compreender os operadores lógicos de comparação que existem na programação sendo eles
'''
== → Igualdade - se ambos os valores são identicos;
!= → Diferença - se ambos os valores são diferentes;
>  → Maior que - se o primeiro valor é maior que o segundo;
<  → Menor que - se o primeiro valor é menor que o segundo;
>= → Maior ou igual que - se o primeiro valor é maior ou igual ao segundo valor
<= → Maior ou igual que - se o primeiro valor é menor ou igual ao segundo valor
'''

# Lembre que os resultado dessas comparações só podem ter apenas dois valores possíveis: verdadeiro ou falso

#Para criar uma estrutura condicional basta usa o comando if (se) para iniciar e em seguindo colocar sua condição.

#Para fazer uma estrutura condicional composta pode se usar o comando elif que é a abreviação das palavras else if (senão se)

# Caso nenhuma das condições acima forem atendidas use o comando else (senão) para executar automáticamente uma tarefa

'''
Os Comparadores lógicos server para comparar mais de uma condição
* and (&&) → comparador 'e' onde o resultado final só vai ser verdadeiro se todas as condições forem verdadeiras;
* or (||) → comparador 'ou' onde o resultado final vai ser verdadeiro se uma das condições forem verdadeiras
* not (!) → busca ou inverte o resultado do valor atual 
'''
nota = 5

if nota >= 6:
    print("Aprovado! Sua nota final foi de",nota)
elif nota > 4 and nota < 6:
    print("Recuperação! Sua nota final foi de",nota)
else:
    print("Reprovado! Sua nota final foi de",nota)