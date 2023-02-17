#Definindo a primeira função de cadastro
def cadastro(primeiro_nome,segundo_nome,nome_completo,idade,cpf):
    primeiro_nome = str(input('Qual seu nome ? '))
    segundo_nome = str(input('Qual seu sobrenome ? '))
    nome_completo = primeiro_nome +' '+ segundo_nome
    cpf = str(input('Qual seu CPF ? '))
    print(f'\n\tOla {nome_completo} \n\tE seu CPF é {cpf} \n\t Sua idade é de Anos !!!\n')
    
#Iniciando o sistema inicial de um cadastro com as variáveis de escolha e cadastro    
print('\n\t Bem vindo ao nosso novo sistema deseja iniciar seu cadastro ? \n')
escolha = int(input('Digite para [1] SIM e [2] para NÃO \n[1] \n[2]\n ESCOLHA = '))
idade = int (input('\n\tMas antes de tudo qual a sua idade ? '))


if( idade >= 18):
    print('\n\t Ta suave meu bom !!!')
    if (escolha == 1):
        cadastro(str,str,str,str,int)
    else:
         print('Até mais meu amigo')            
elif(idade < 18 ):
    print ('\n\t Vai ter que esperar pra crescer !!!')   



    




