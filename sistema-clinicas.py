from time import sleep


# variáveis que vão ser usadas no código:
nome = ["1", "2", "3", "4"]
dia = [1, 2, 3, 4]
mes = [1, 2, 3, 4]
HoraConsulta = [1, 2, 3, 4]
NumeroConsultas = 0
especialidades ="""
Clínica Geral
Pediatria
Ginecología
Cardiología
Dermatología"""

especialidade = ["1", "2", "3", "4"]
consulta1 = False
consulta2 = False
consulta3 = False
consulta4 = False

horario1 = False
horario2 = False
horario3 = False
horario4 = False

data1 = False
data2 = False
data3 = False
data4 = False

NumeroConsultas = 0


#programa principal:
while True:
    print("\nOlá. Seja bem vindo.\n")
    sleep(1)
    print("escolha uma ação para continuar:\n")

    print("""
        1 - Agendar nova consulta
        2 - Listar consultas agendadas
        3 - Cancelar uma consulta
        4 - Listar consultas salvas anteriormente
        5 - Apagar consultas salvas anteriormente
        6 - Sair""")

    

    while True:
        try:
            ordem = int(input("> "))
            if(ordem < 9999):
                break

        except (ValueError, TypeError):
            print("ERRO: Digite um número.")

        except:
            print("Um erro desconhecido ocorreu. Tente novamente.")

    while True:

        # Agendar nova consulta:
        if(ordem == 1):
            while True:
                if(consulta1 == False):
                    while True:
                        nome[0] = input("Digite seu nome completo: ")
                        try:
                            dia[0] = int(input("qual o dia da consulta? "))
                            mes[0] = int(input("qual o mês da consulta? "))
                            data1 = True
                            
                        except (ValueError, TypeError):
                            print("ERRO: digite números inteiros (ex: 10, 09, 04, 21).")
                        except:
                            print("Ocorreu um erro desconhecido. Tente novamente.")

                        if(data1 == True):

                            while True:
                                try:
                                    print("""Escolha um horário para sua consulta:
                                    1 - 12:00
                                    2 - 14:30
                                    3 - 17:00\n""")
                                    Consulta = int(input("> "))
                                    if(Consulta == 1):
                                        HoraConsulta[0] = "12:00"
                                        print("Horário marcado: ", HoraConsulta[0])
                                        horario1 = True
                                        consulta1 = True
                                        

                                    elif(Consulta == 2):
                                        HoraConsulta[0] = "14:30"
                                        print("Horário marcado: ", HoraConsulta[0])
                                        horario1 = True
                                        consulta1 = True
                                        

                                    elif(Consulta == 3):
                                        HoraConsulta[0] = "17:00"
                                        print("Horário marcado: ", HoraConsulta[0])
                                        horario1 = True
                                        consulta1 = True
                                        

                                    else:
                                        print("Opção inválida. tente novamente.\n")
                                except (ValueError, TypeError):
                                    print("ERRO: Digite um número inteiro.\n")

                                except:     
                                    print("Um erro desconhecido ocorreu. tente novamente.\n")

                                if(consulta1 == True):
                                    print("Escolha e ESCREVA a área que quer ser atendido:")
                                    print(especialidades)
                                    especialidade[0] = input("> ")
                                    break
                            break
                    break
                    
                    

                
                elif(consulta2 == False):
                    while True:
                        nome[1] = input("Digite seu nome completo: ")
                        try:
                            dia[1] = int(input("qual o dia da consulta? "))
                            mes[1] = int(input("qual o mês da consulta? "))
                            data2 = True
                            
                        except (ValueError, TypeError):
                            print("ERRO: digite números inteiros (ex: 10, 09, 04, 21).")
                        except:
                            print("Ocorreu um erro desconhecido. Tente novamente.")

                        if(data2 == True):

                            while True:
                                try:
                                    print("""Escolha um horário para sua consulta:
                                    1 - 12:00
                                    2 - 14:30
                                    3 - 17:00\n""")
                                    Consulta = int(input("> "))
                                    if(Consulta == 1):
                                        HoraConsulta[1] = "12:00"
                                        print("Horário marcado: ", HoraConsulta[1])
                                        horario2 = True
                                        consulta2 = True
                                        

                                    elif(Consulta == 2):
                                        HoraConsulta[1] = "14:30"
                                        print("Horário marcado: ", HoraConsulta[1])
                                        horario2 = True
                                        consulta2 = True
                                        

                                    elif(Consulta == 3):
                                        HoraConsulta[1] = "17:00"
                                        print("Horário marcado: ", HoraConsulta[1])
                                        horario2 = True
                                        consulta2 = True
                                        

                                    else:
                                        print("Opção inválida. tente novamente.\n")
                                except (ValueError, TypeError):
                                    print("ERRO: Digite um número inteiro.\n")

                                except:     
                                    print("Um erro desconhecido ocorreu. tente novamente.\n")

                                if(consulta2 == True):
                                    print("Escolha e ESCREVA a área que quer ser atendido:")
                                    print(especialidades)
                                    especialidade[1] = input("> ")
                                    break
                            break
                    break
                    
                
                elif(consulta3 == False):
                    while True:
                        nome[2] = input("Digite seu nome completo: ")
                        try:
                            dia[2] = int(input("qual o dia da consulta? "))
                            mes[2] = int(input("qual o mês da consulta? "))
                            data3 = True
                            
                        except (ValueError, TypeError):
                            print("ERRO: digite números inteiros (ex: 10, 09, 04, 21).")
                        except:
                            print("Ocorreu um erro desconhecido. Tente novamente.")

                        if(data3 == True):

                            while True:
                                try:
                                    print("""Escolha um horário para sua consulta:
                                    1 - 12:00
                                    2 - 14:30
                                    3 - 17:00\n""")
                                    Consulta = int(input("> "))
                                    if(Consulta == 1):
                                        HoraConsulta[2] = "12:00"
                                        print("Horário marcado: ", HoraConsulta[2])
                                        horario3 = True
                                        consulta3 = True
                                        

                                    elif(Consulta == 2):
                                        HoraConsulta[2] = "14:30"
                                        print("Horário marcado: ", HoraConsulta[2])
                                        horario3 = True
                                        consulta3 = True
                                        

                                    elif(Consulta == 3):
                                        HoraConsulta[2] = "17:00"
                                        print("Horário marcado: ", HoraConsulta[2])
                                        horario3 = True
                                        consulta3 = True
                                        

                                    else:
                                        print("Opção inválida. tente novamente.\n")
                                except (ValueError, TypeError):
                                    print("ERRO: Digite um número inteiro.\n")

                                except:     
                                    print("Um erro desconhecido ocorreu. tente novamente.\n")

                                if(consulta3 == True):
                                    print("Escolha e ESCREVA a área que quer ser atendido:")
                                    print(especialidades)
                                    especialidade[2] = input("> ")
                                    break
                            break
                    break
                    

                elif(consulta4 == False):
                    while True:
                        nome[3] = input("Digite seu nome completo: ")
                        try:
                            dia[3] = int(input("qual o dia da consulta? "))
                            mes[3] = int(input("qual o mês da consulta? "))
                            data3 = True
                            
                        except (ValueError, TypeError):
                            print("ERRO: digite números inteiros (ex: 10, 09, 04, 21).")
                        except:
                            print("Ocorreu um erro desconhecido. Tente novamente.")

                        if(data3 == True):

                            while True:
                                try:
                                    print("""Escolha um horário para sua consulta:
                                    1 - 12:00
                                    2 - 14:30
                                    3 - 17:00\n""")
                                    Consulta = int(input("> "))
                                    if(Consulta == 1):
                                        HoraConsulta[3] = "12:00"
                                        print("Horário marcado: ", HoraConsulta[3])
                                        horario4 = True
                                        consulta4 = True
                                        

                                    elif(Consulta == 2):
                                        HoraConsulta[3] = "14:30"
                                        print("Horário marcado: ", HoraConsulta[3])
                                        horario4 = True
                                        consulta4 = True
                                        

                                    elif(Consulta == 3):
                                        HoraConsulta[3] = "17:00"
                                        print("Horário marcado: ", HoraConsulta[3])
                                        horario4 = True
                                        consulta4 = True
                                        

                                    else:
                                        print("Opção inválida. tente ERRO novamente.\n")
                                except (ValueError, TypeError):
                                    print("ERRO: Digite um número inteiro.\n")

                                except:     
                                    print("Um erro desconhecido ocorreu. tente novamente.\n")

                                if(consulta4 == True):
                                    print("Escolha e ESCREVA a área que quer ser atendido:")
                                    print(especialidades)
                                    especialidade[3] = input("> ")
                                    break
                            break
                    break
                            


                else:
                    print("ERRO: o máximo de consultas que você pode marcar é 4.\ndesmarque uma consulta para continuar.\n")
                    sleep(1)
                    break
                


            print("Consulta marcada com sucesso!")
            NumeroConsultas +=1
            break
            

        # Listar consultas marcadas
        elif (ordem == 2):
            
            if(NumeroConsultas == 0):
                print("Nenhuma consulta marcada. Marque alguma.")
                sleep(1)
                break

            else:
                print(f"""Número de consultas marcadas: {NumeroConsultas}.
                        DADOS GERAIS:""")
                
                if(consulta1 == True):
                    print(f"""consulta 1:
                        Nome: {nome[0]};
                        Data: {dia[0]}/{mes[0]}/2025;
                        Hora da consulta: {HoraConsulta[0]};
                        Especialidade: {especialidade[0]}\n
                    """)
                else:
                    print("consulta 1:\nNão marcada.")
                
                if(consulta2 == True):
                    print(f"""consulta 2:
                        Nome: {nome[1]};
                        Data: {dia[1]}/{mes[1]}/2025;
                        Hora da consulta: {HoraConsulta[1]};
                        Especialidade: {especialidade[1]}\n
                    """)
                else:
                    print("consulta 2:\nNão marcada.")
                
                if(consulta3 == True):
                    print(f"""consulta 3:
                        Nome: {nome[2]};
                        Data: {dia[2]}/{mes[2]}/2025;
                        Hora da consulta: {HoraConsulta[2]};
                        Especialidade: {especialidade[2]}\n
                    """)
                else:
                    print("consulta 3:\nNão marcada.")

                if(consulta4 == True):
                    print(f"""consulta 4:
                        Nome: {nome[3]};
                        Data: {dia[3]}/{mes[3]}/2025;
                        Hora da consulta: {HoraConsulta[3]};
                        Especialidade: {especialidade[3]}\n
                    """)
                    sleep(1)
                else:
                    print("consulta 4:\nNão marcada.")
                    sleep(1)
                

        # Cancelar consulta
        elif(ordem == 3):
            while True:
                if(NumeroConsultas == 0):
                    print("não há consultas marcadas para serem canceladas.")
                    sleep(1)
                    break
                
                else:
                    print("Escolha uma consulta para desmarcar:\n")
                    if(consulta1 == True):
                        print(f"""consulta 1:
                        Nome: {nome[0]};
                        Data: {dia[0]}/{mes[0]}/2025;
                        Hora da consulta: {HoraConsulta[0]};
                        Especialidade: {especialidade[0]};\n""")
                    else:
                        print("consulta 1:\nNão marcada.")
                        

                    if(consulta2 == True):
                        print(f"""\nconsulta 2:
                        Nome: {nome[1]};
                        Data: {dia[1]}/{mes[1]}/2025;
                        Hora da consulta: {HoraConsulta[1]};
                        Especialidade: {especialidade[1]};\n""")
                    else:
                        print("consulta 2:\nNão marcada.")

                    if(consulta3 == True):
                        print(f"""\nconsulta 3:
                        Nome: {nome[2]};
                        Data: {dia[2]}/{mes[2]}/2025;
                        Hora da consulta: {HoraConsulta[2]};
                        Especialidade: {especialidade[2]};\n""")
                    else:
                        print("consulta 3:\nNão marcada.")

                    if(consulta4 == True):
                        print(f"""\nconsulta 4:
                        Nome: {nome[3]};
                        Data: {dia[3]}/{mes[3]}/2025;
                        Hora da consulta: {HoraConsulta[3]};
                        Especialidade: {especialidade[3]};\n""")
                        sleep(1)
                    else:
                        print("consulta 4:\nNão marcada.")
                        sleep(1)
                
                escolha = input("Digire o número da consulta para desmarcar, ou 'sair' para cancelar.\n> ")
                if(escolha == "1"):
                    consulta1 = False
                    NumeroConsultas -= 1
                    nome[0] = ""
                    dia[0] = ""
                    mes[0] = ""
                    HoraConsulta[0] = ""
                    especialidade[0] = ""
                    print("Consulta 1 desmarcada com sucesso!")
                    sleep(1)
                    break
                
                if(escolha == "2"):
                    consulta2 = False
                    NumeroConsultas -= 1
                    nome[1] = ""
                    dia[1] = ""
                    mes[1] = ""
                    HoraConsulta[1] = ""
                    especialidade[1] = ""
                    print("Consulta 2 desmarcada com sucesso!")
                    sleep(1)
                    break

                if(escolha == "3"):
                    consulta3 = False
                    NumeroConsultas -= 1
                    nome[2] = ""
                    dia[2] = ""
                    mes[2] = ""
                    HoraConsulta[2] = ""
                    especialidade[2] = ""
                    print("Consulta 3 desmarcada com sucesso!")
                    sleep(1)
                    break
                if(escolha == "4"):
                    consulta4 = False
                    NumeroConsultas -= 1
                    nome[3] = ""
                    dia[3] = ""
                    mes[3] = ""
                    HoraConsulta[3] = ""
                    especialidade[3] = ""
                    print("Consulta 4 desmarcada com sucesso!")
                    sleep(1)
                    break

                if(escolha == "sair"):
                    print("Ok. Cancelando...\n")
                    sleep(1)
                    break

                else:
                    print("Opção inválida. Escolha o NÚMERO da consulta para desmarcar ela, ou 'sair' para sair.")
                    sleep(1)
            break

        # Listar consultas salvas
        elif(ordem == 4):
            try:
                with open("Consultas.txt", "r") as lendo:
                    print("\n")
                    for linha in lendo:
                        print(linha, end= "")
                        lendo.close
            
            except(FileNotFoundError):
                print("ERRO: Arquivo não encontrado ou não existe. Salve dados para criar o arquivo.")

            except:
                print("Um erro desconhecido ocorreu. Tente novamente.")

        # Apagar os dados:
        elif(ordem == 5):
            print("Certo. Apagando...")
            sleep(1)
            try:
                with open("Consultas.txt", "w") as apagar:
                    apagar.write("""Consultas marcadas:
                                Consulta 1:
                                Não marcada.
                                Consulta 2:
                                Não marcada.
                                Consulta 3:
                                Não marcada.
                                Consulta 4:
                                Não marcada.
                                """)
                    apagar.close
                print("Dados apagados com sucesso.")

            except(FileNotFoundError):
                print("ERRO: Arquivo não encontrado. Crie o arquivo.")

            except:
                print("Um erro desconhecido ocorreu. Tente novamente.")

        
        #Caso escolha algo diferente das opções:
        elif(ordem != 6):
            print("ERRO: Escolha uma opção válida.")
            sleep(1)
        
        #Sair do programa:
        else:
            while True:
                print("deseja salvar estes dados? (Dados passados serão perdidos)\n1 - Sim\n2 - Não\n")
                while True:
                    try:
                        salvar = int(input("> "))
                        break
                    except(ValueError):
                        print("ERRO: Digite um NÚMERO.")
                    except:
                        print("Algum erro desconhecido ocorreu... Tente novamente.\n")
                if salvar == 1:
                    print("Certo. Salvando dados...")
                    try:
                        with open("Consultas.txt", "w") as dados:
                            dados.write("Consultas Marcadas:\n")
                            if consulta1:
                                dados.write(f"""consulta 1:
                                    Nome: {nome[0]};
                                    Data: {dia[0]}/{mes[0]}/2025;
                                    Hora da consulta: {HoraConsulta[0]};
                                    Especialidade: {especialidade[0]}\n
                                """)
                            else:
                                dados.write("consulta 1:\nNão marcada.\n")
                            
                            if consulta2:
                                dados.write(f"""\nconsulta 2:
                                    Nome: {nome[1]};
                                    Data: {dia[1]}/{mes[1]}/2025;
                                    Hora da consulta: {HoraConsulta[1]};
                                    Especialidade: {especialidade[1]}\n
                                """)
                            else:
                                dados.write("consulta 2:\nNão marcada.\n")
                            
                            if(consulta3 == True):
                                dados.write(f"""\nconsulta 3:
                                    Nome: {nome[2]};
                                    Data: {dia[2]}/{mes[2]}/2025;
                                    Hora da consulta: {HoraConsulta[2]};
                                    Especialidade: {especialidade[2]}\n
                                """)
                            else:
                                dados.write("consulta 3:\nNão marcada.")

                            if consulta4:
                                dados.write(f"""\nconsulta 4:
                                    Nome: {nome[3]};
                                    Data: {dia[3]}/{mes[3]}/2025;
                                    Hora da consulta: {HoraConsulta[3]};
                                    Especialidade: {especialidade[3]}\n
                                """)
                            else:
                                dados.write("consulta 4:\nNão marcada.\n")
                                dados.close

                            print("Salvamento concluído. Encerrando...")

                            
                            
                    except(FileNotFoundError):

                        try:
                            print("ERRO: Arquivo não encontrado. Não é possível salvar os dados.\n")
                            while True:
                                print("Deseja criar um novo arquivo para salvar os dados?\n1 - Sim\n2 - Não")
                                try:
                                    criar = int(input("> "))

                                except(ValueError):
                                    print("ERRO: Digite um NÚMERO.")
                                except:
                                    print("Algum erro desconhecido ocorreu... Tente novamente.\n")

                                if criar == 1:
                                    print("Certo. Criando arquivo...")
                                    sleep(1)
                                    with open("Consultas.txt", "x") as arquivo:
                                        arquivo.write("Consultas Marcadas:\n")
                                        if consulta1:
                                            arquivo.write(f"""consulta 1:
                                                Nome: {nome[0]};
                                                Data: {dia[0]}/{mes[0]}/2025;
                                                Hora da consulta: {HoraConsulta[0]};
                                                Especialidade: {especialidade[0]}\n
                                            """)
                                        else:
                                            arquivo.write("consulta 1:\nNão marcada.\n")
                                        
                                        if consulta2:
                                            arquivo.write(f"""\nconsulta 2:
                                                Nome: {nome[1]};
                                                Data: {dia[1]}/{mes[1]}/2025;
                                                Hora da consulta: {HoraConsulta[1]};
                                                Especialidade: {especialidade[1]}\n
                                            """)
                                        else:
                                            arquivo.write("consulta 2:\nNão marcada.\n")
                                        
                                        if(consulta3 == True):
                                            arquivo.write(f"""\nconsulta 3:
                                                Nome: {nome[2]};
                                                Data: {dia[2]}/{mes[2]}/2025;
                                                Hora da consulta: {HoraConsulta[2]};
                                                Especialidade: {especialidade[2]}\n
                                            """)
                                        else:
                                            arquivo.write("consulta 3:\nNão marcada.")

                                        if consulta4:
                                            arquivo.write(f"""\nconsulta 4:
                                                Nome: {nome[3]};
                                                Data: {dia[3]}/{mes[3]}/2025;
                                                Hora da consulta: {HoraConsulta[3]};
                                                Especialidade: {especialidade[3]}\n
                                            """)
                                        else:
                                            arquivo.write("consulta 4:\nNão marcada.\n")
                                            arquivo.close
                                    print("Salvamento concluído. Encerrando...\n")
                                    break

                                elif criar == 2:
                                    print("Ok. Saindo...\n")
                                    break

                                else:
                                    print("ERRO: Escolha uma opção válida.\n")


                        except(PermissionError):
                            print("ERRO: Permissão necessária para salvar ou alterar os dados nao concedida.")
                            print("Encerrando...")
                            break
                        except:
                            print("Um erro desconhecido ocorreu. Não é possivel salvar os dados.\nSaindo...")


                elif salvar == 2:
                    print("Ok. Encerrando...")
                    break
                break
            break
        break
    if(ordem == 6):
        sleep(1)
        break

print("Código encerrado com sucesso.")