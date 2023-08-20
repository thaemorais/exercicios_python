lista = [] #cria lista vazia
continuar = 's'
def preenche_lista(lista, continuar):
    while(continuar.lower() == 's'):
        convidado = input('Digite o nome do convidado: ')
        lista.append(convidado)
        continuar = input('Deseja continuar? s ou n? ')

        if len(lista) == 10:
            print('Voce já chamou 10 pessoas, chega né? Tecle ENTER para visualizar sua lista')
            input()
            break
    return lista

lista_preenchida = preenche_lista(lista, continuar)

def imprime_lista(lista):
    lista.sort()
    print('\nSua lista de convidados é: ')
    for convidado in lista:
        print(convidado.title())

imprime_lista(lista_preenchida)


