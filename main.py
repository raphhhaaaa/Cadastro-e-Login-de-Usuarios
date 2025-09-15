from db import *
import hashlib

def main():
    init_db()
    while True:
        opcao = None
        menu()
        try:
            opcao = int(input('>> '))
        except ValueError as e:
            print('=-' * 25)
            print(f'Opção inválida: {e}')
            print('=-' * 25)
        if opcao == 1:
            cadastro()

        elif opcao == 2:
            login()

        elif opcao == 3:
            print('=-' * 25)
            print(f'{"Programa encerrado":.^50}')
            print('=-' * 25)
            break

        elif opcao == 98:
            __listar_usuarios__()

        elif opcao == 99:
            usuarios = mostrar_usuarios()
            if not usuarios:
                print('=-' * 25)
                print('Nenhum usuário cadastrado.')
                print('=-' * 25)
            else:
                __listar_usuarios__()
                __apaga_cadastro__()
        
        elif opcao == 100:
            update()

        input(f'{"<< ENTER para voltar ao menu >> ":.<100}')

def menu():
    print('=-' * 25)
    print('BEM-VINDO AO {NOME DO APLICATIVO}!!'.center(50))
    print('=-' * 25, '\nPor favor escolha uma opção:', end='\n')
    print('1. Cadastro (\033[1;32mC\033[mRUD)\n2. Login\n3. Sair')
    print('=-' * 25)
    print('98. Listar dados de usuarios (C\033[1;34mR\033[mUD)\n99. Apagar usuário (CRU\033[1;31mD\033[m)\n100. Atualizar dados (CRU\033[1;33mD\033[m)')
    print('=-' * 25)

def cadastro():
    print('=-' * 25)
    print('Seja bem-vindo ao cadastro! Por favor insira suas informações:')
    usuario = str(input('Nome de usuário:\n>> '))
    nascimento = input('Ano de nascimento:\n>> ')
    sexo = str(input('Sexo: [M/F]\n>> ')).upper()
    nacionalidade = str(input('Nacionalidade:\n>> ')).capitalize()
    senha = input('Crie uma senha:\n>> ')
    hash = __gera_hash_sha256__(senha)
    if cadastro_usuario(usuario, nascimento, sexo, nacionalidade, hash):
        print('=-' * 25)
        print('Cadastro realizado com sucesso!!')
        print('=-' * 25)

def login():
    print('=-' * 25)
    print('Seja bem-vindo ao login! Por favor insira suas informações:')
    usuario = str(input('Nome de usuário: '))
    senha = input('senha:  ')
    if pega_hashsenha(usuario) == __gera_hash_sha256__(senha):
        print('=-' * 25)
        print('Login efetuado com sucesso.')
        print('=-' * 25)
        tela_usuario(usuario)
    else:
        print('=-' * 25)
        print('Erro no login. Nome de usuário ou senha incorretos.')
        print('=-' * 25)

def tela_usuario(usuario):
    print(f'Olá {usuario} !'.center(50))
    print('=-' * 25)
    print("""Olá,\n
            Essa foi uma demonstração de uma interface de login simples, feita usando Python + banco de dados persistente sql integrado (SQlite3).
          Meu principal objetivo com este projeto foi exercitar fundamentos de desenvolvimento de software, com enfoque na parte back-end
          de um sistema, buscando alcançar características como: estabilidade, funcionabilidade, escalabilidade e segurança. Bem como, praticar conceitos
          de boas práticas em todo o ciclo de desenvolvimento, desde a implementação, até a documentação e ao commit no GitHub.
          Se chegou até aqui e ainda não explorou as outras funcionalidades do sistema, por favor, fique à vontade.
          Ademais, agradeço a qualquer que seja a pessoa que dedicou sua atenção ao meu projeto, sou apenas um estudante
          ambicioso e apaixonado, portanto sinta-se livre para relatar críticas construtivas.
                            Obrigado pelo seu tempo :)\n
          - Raphael  """)
    print('=-' * 25)

def __listar_usuarios__():
    usuarios = mostrar_usuarios()
    if not usuarios:
        print('=-' * 25)
        print('Nenhum usuário cadastrado.')
        print('=-' * 25)
    else:
        print('=-' * 50)
        for u in usuarios:
            print(f'ID.[{u[0]}], NOME_USUARIO:[{u[1]}], ANO_NASC:[{u[2]}], SEXO:[{u[3]}], NACIONALIDADE:[{u[4]}], SENHA:[{u[5]}]')
        print('=-' * 50)

def __apaga_cadastro__():
    try:
        id = int(input('Digite o id do usuario que deseja apagar:\n>> '))
        apagar_usuario(id)
        print('=-' * 25)
        print('Usuario apagado.')
        print('=-' * 25)
    except ValueError as e:
        print('=-' * 25)
        print(f'Valor inválido: {e}')
        print('=-' * 25)

def __gera_hash_sha256__(senha):
    senha_bytes = senha.encode('utf-8')
    obj_hash = hashlib.sha256()
    obj_hash.update(senha_bytes)
    hash_final = obj_hash.hexdigest()
    return hash_final

def update():
    usuarios = mostrar_usuarios()
    if not usuarios:
        print('=-' * 25)
        print('Nenhum usuário cadastrado.')
        print('=-' * 25)
    else:
        __listar_usuarios__()
        try:
            id = int(input('Digite o id do usuário que deseja modificar:\n>> '))
            print('=-' * 25)
        except ValueError as e:
            print('=-' * 25)
            print(f'Valor inválido: {e}')
            print('=-' * 25)
            return False
        if id not in mostra_ids():
            print('Nenhum usuário com o id inserido.')
            print('=-' * 25)
            return False
        while True:
            campo = int(input('Qual campo deseja alterar?\n1. Nome de usuário\n2. Ano de nascimento\n3. Sexo\n4. Nacionalidade\n>> '))
            if campo == 1:
                campo = 'usuario'
                print('=-' * 25)
                novo_valor = str(input('Digite um novo nome de usuário:\n>> '))
                break
            elif campo == 2:
                campo = 'nascimento'
                print('=-' * 25)
                novo_valor = input('Digite um novo ano de nascimento:\n>> ')
                break
            elif campo == 3:
                campo = 'sexo'
                print('=-' * 25)
                novo_valor = str(input('Digite um novo sexo [M/F]:\n>> ')).upper()
                break
            elif campo == 4:
                campo = 'nacionalidade'
                print('=-' * 25)
                novo_valor = str(input('Digite uma nova nacionalidade:\n>> '))
                break
            else:
                print('=-' * 25)
                print('ERRO: Valor inválido.')
                print('=-' * 25)
        if atualiza_dados(campo, novo_valor, id):
            print('=-' * 25)
            print('Atualização realizada com sucesso.')
            print('=-' * 25)
        

if __name__ == '__main__':
    main()