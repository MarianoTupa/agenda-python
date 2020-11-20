print('AGENDA DE CONTATO 0.1')
print('#####################')

agenda = {}

def exibir_agenda():
    for contato in agenda:
       buscar_contato(contato)
       print('-------------------')

def buscar_contato(contato):
        print(contato)
        print('tell:', agenda[contato]['tell: '])
        print('email:', agenda[contato]['email: '])
        print('end:', agenda[contato]['end: '])

    

def add_edit_contato(contato, tell, email, end):
    agenda[contato] = {
        'tell: ': tell,
        'email: ': email,
        'end: ': end,
    }
    salvar()
    print('---contato {} adicionado/editado com sucesso---'.format(contato))

def dell_contato(contato):
    try:
        agenda.pop(contato)
        salvar()
        print('---contato {} excluido com sucesso---'.format(contato))
    except KeyError as error:
        print('Contato inexistente')
    except Exception as error:
        print(error)
        print('>>>Erro inesperado')
        
def export_contato():#                                  criar arquivo.txt e escrever os contatos dentro
    try:
        with open('agenda.csv', 'w') as arquivo:
            for contato in agenda:
                tell = agenda[contato]['tell: ']
                email = agenda[contato]['email: ']
                end = agenda[contato]['end: ']              
                arquivo.write("{},{},{},{}\n".format(contato, tell, email, end))
        print('>>>>agenda exportada com sucesso!')
    except Exception as error:
        print('>>>>erro ao exportar contatos')
        print(error)    



def import_contato(arquivo_nome):
    try:
        with open(arquivo_nome, 'r') as arquivo:
            linhas = arquivo.readlines()
        for linha in linhas:
            detalhes = (linha.strip().split(','))

            nome = detalhes[0]
            tell = detalhes[1]
            email = detalhes[2]
            end = detalhes[3]

    except FileNotFoundError:
        print('Arquivo não encontrado')
    except Exception as error:
        print('Ocorreu um erro: ' + error)

def salvar():
    try:
        with open('database.csv', 'w') as arquivo:
            for contato in agenda:
                tell = agenda[contato]['tell: ']
                email = agenda[contato]['email: ']
                end = agenda[contato]['end: ']              
                arquivo.write("{},{},{},{}\n".format(contato, tell, email, end))
        print('>>>>agenda exportada com sucesso!')
    except Exception as error:
        print('>>>>erro ao exportar contatos')
        print(error)    


def carregar():
    try: 
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                tell = detalhes[1]
                email = detalhes[2]
                end = detalhes[3]
                agenda[nome] = {
                    'tell': tell,
                    'email': email,
                    'end': end
                }
            
        print('>>>>database carregado com sucesso!')
        print('>>>> {} contatos carregados'.format(len(agenda)))
    except FileNotFoundError:
        print('>>>>Arquivo database.csv não encontrado')
    except Exception as error:
        print('algum erro ocorreu')

def menu():
    print('---------------------------------')
    print('1 - MOSTRAR TODOS OS CONTATOS')
    print('2 - BUSCAR CONTATO')
    print('3 - ADICIONAR/EDITAR UM CONTATO')
    print('4 - EXCLUIR CONTATO')
    print('5 - EXPORTAR AGENDA CSV')
    print('6 - IMPORTAR AGENDA CSV')
    print('0 - SAIR DO PROGRAMA')
    print('\n')  
    print('---------------------------------')

    print('---------------------------------')

while True:
    menu()
    opcao_menu = input('ESCOLHA UMA OPCAO: ') 
    if opcao_menu == '1':
        exibir_agenda()

    elif opcao_menu == '2':
        contato = input('digite o nome do contato: ')
        print('-------------')
        buscar_contato(contato)
        print('\n -------------')
        buscar_contato(contato)
   
    elif opcao_menu == '3':
        contato = input('nome: ')
        tell = input('tell: ')
        email = input('email: ')
        end = input('end: ')
        add_edit_contato(contato, tell, email, end)
            
    elif opcao_menu == '4':
        contato = input('nome do contato: ')
        dell_contato(contato)
        exibir_agenda
        dell_contato(contato)
   
    elif opcao_menu == '5':
        export_contato()

    elif opcao_menu == '6':
        arquivo_nome = input('Nome do arquivo a ser importado: ')
        import_contato(arquivo_nome)

        print('>>>> PROGRAMA FECHADO')
        
    elif opcao_menu == '0':
        print('>>>ENCERRANDO PROGRAMA')
        break

    else:
        print('>>>> Erro inesperado')
