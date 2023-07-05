from colorama import init, Fore, Back, Style
init(autoreset=True)

opcao_do_menu = 0

def menu():
  print(Fore.GREEN + 35*"=")
  print(Back.GREEN + "** Bem-vindo a Agenda de Tarefas **")
  print(Fore.GREEN + 35*"=")
  print("[1] ---> Incluir nova tarefa")
  print("[2] ---> Ver lista de tarefas")
  print("[3] ---> Excluir tarefa salva")
  print("[4] ---> Sair")
  print(Fore.GREEN + 35*"=")

menu()
lista_de_tarefas = []
opcao_do_menu = int(input("\nDigite a opção desejada: "))

while True:
  if opcao_do_menu == 1:
    print(Fore.GREEN + "Opção escolhida: 1 - Incluir nova tarefa")
    opcao_do_menu = 0
    tarefa = input("Digite tarefa a ser adicionada: ")
    lista_de_tarefas.append(tarefa)
    print("\nSua lista de tarefas")
    print(lista_de_tarefas)
    print("\n")
    menu()
    opcao_do_menu = int(input("\nDigite a opção desejada: "))

  elif opcao_do_menu == 2:
    print(Fore.GREEN + "Opção escolhida: 2 - Ver lista de tarefas")
    print("\nSua lista de tarefas: ")
    print(lista_de_tarefas)
    print("\n")
    opcao_do_menu = 0
    menu()
    opcao_do_menu = int(input("\nDigite a opção desejada: "))

  elif opcao_do_menu == 3:
    print(Fore.GREEN + "Opção escolhida: 3 - Excluir tarefa salva")
    print("\nSua lista de tarefas: ")
    print(lista_de_tarefas)
    print("\n")
    tarefa_a_ser_removida = input("Digite a tarefa a ser removida: ")
    lista_de_tarefas.remove(tarefa_a_ser_removida)
    print("\nSua Lista de tarefas: ")
    print(lista_de_tarefas)
    print("\n")
    opcao_do_menu = 0
    menu()
    opcao_do_menu = int(input("\nDigite a opção desejada: "))

  elif opcao_do_menu == 4:
    print(Fore.GREEN + "Opçaõ escolhida: 4 - Sair")
    resposta_de_saida = input("Deseja mesmo sair? (S/N) ").upper()
    if (resposta_de_saida == "S") or (resposta_de_saida == "SIM"):
      break
    else:
      print("\n")
      menu()
      opcao_do_menu = 0
      opcao_do_menu = int(input("\nDigite a opção desejada: "))