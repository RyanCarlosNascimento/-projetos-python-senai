# Crie um algoritmo
# que leia um salário
# e simule um reajuste positivo de 60%.

#Leitura de dados
print('Nossa empresa irá fazer um REAJUSTE SALARIAL este mês. VAMOS DESCOBRIR SEU NOVO SALÁRIO!')

salario = float(input('Digite seu salário: R$ '))
reajuste = salario + (salario * 0.60)

#Retorno de informações
print(f'Seu novo salário reajustado em 60% é: R${reajuste}')

