#Escreva um programa que leia 6 notas diferentes
# e faça a média do aluno

#Leitura de dados
print('Vamos calcular a média das notas dos 6 alunos de uma escola X!')

nota_1 = int(input('Digite a 1° nota: '))
nota_2 = int(input('Digite a 2° nota: '))
nota_3 = int(input('Digite a 3° nota: '))
nota_4 = int(input('Digite a 4° nota: '))
nota_5 = int(input('Digite a 5° nota: '))
nota_6 = int(input('Digite a 6° nota: '))

media = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5 + nota_6) / 6

#Retorno de informações
print(f'A média de suas 6 notas são: {media}')