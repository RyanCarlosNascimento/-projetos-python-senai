# Crie um programa que leia uma frase e mostre:
# 1. Quantas vezes aparece a letra “a”
# 2. Em que posição ela aparece a primeira vez
# 3. Em que posição ela aparece na última vez

#Leitura de dados
frase = input("Digite uma frase: ").strip() #Tiro espaços antes e depois do que foi digitado.
print()

#1. Contagem A(s)
frase = frase.upper() # Transformo a variavel frase toda em MAIUSCULA
contagem_a = (frase.count('A')) + (frase.count('Á')) + (frase.count('Ã')) + (frase.count('À')) + (frase.count('Â'))
# Agora faço a contagem de todos os A(s) Maiusculos e suas variações com acento

# Retorno de informações
print(f'Sua frase exibiu um total de: {contagem_a} letras A(s)'
      f'O primeiro A da sua frase está na {frase.find('A')}° posição.'
      f'O último A da sua frase está na {frase.rfind('A')}° posição.')



