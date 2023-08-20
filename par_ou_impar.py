from operacoes import soma

# pede par ou impar jogador 1
jog_1 = input('Jogador 1, par ou impar? ')

# dá a outra opção pro jogador 2
if jog_1.lower() == 'par':
    jog_2 = 'impar'
elif jog_1.lower() == 'impar':
    jog_2 = 'par'

# pergunta o numero do jogador 1
num_jog_1 = int(input('\nJOGADOR 1 Jogue um número: '))

# pergunta o numero do jogador 2
num_jog_2 = int(input('\nJOGADOR 2 Jogue um número: '))

# faz a soma
soma = soma(num_jog_1, num_jog_2)

# exibe o resultado
if soma % 2 == 0:
    if jog_1.lower() == 'par':
        print('\nJogador 1 ganhou! Parabéns!')
    else:
        print('\nJogador 2 ganhou! Parabéns!')
else:
    if jog_1.lower() == 'impar':
        print('\nJogador 1 ganhou! Parabéns!')
    else:
        print('\nJogador 2 ganhou! Parabéns!')