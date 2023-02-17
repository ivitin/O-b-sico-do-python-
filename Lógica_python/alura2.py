from random import randrange

def verifica_valores(valor):
    for valor in Valores:
        if valor >= 30:
            print(f'\n\t{valor} -  Valor adequado !!!') 
            Permissoes.append(True)   
            print(f'\t{Permissoes}')
            for permissao in Permissoes:
                if permissao == True:
                     print(f'\n\t Permissão - {permissao} - concedida')
                else:
                    print(f'\n\t Permissão - {permissao} - negada')
            
        elif valor<30:
            print(f'\n\t{valor} - Valor abaixo do esperado...')
            Permissoes.append(False)
            print(f'\t{Permissoes}') 
            for permissao in Permissoes:
                    if permissao == True:
                        print(f'\n\t Permissão - {permissao} - concedida')
                    else:
                        print(f'\n\t Permissão - {permissao} - negada')

Valores = [21,2,33,14]
informacoes = ['Vitinho',21,True,'21']
Permissoes = []
print(type(Valores))
print(Valores[1:3])
print(Valores[-1])
notas = []

for nota in range (8):
    notas.append(randrange(0,11))
    print(notas)


for info in informacoes:
    print(f'O tipo da informação {info} é ',type(info))

verifica_valores(Valores and Permissoes)
