import json
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def search_by_index (data, word_index):
    try:
        os.system('cls||clear')
        print(f"Palavra {word_index}: "  + data.get(f'{word_index}'))
    except TypeError:
        print("Escolha uma opção válida")
    return(0)

def search_by_name (data, name):
    os.system('cls||clear')
    for key in data.keys():
        if data[key] == name:
            print(f"{key} : {name}")
            return(1)
        
    print("Palavra não encontrada")
    return(0)

def open_file ():
    try:
        with open(resource_path("BIP39_.json"), "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return(0)
    return(data)

def menu(data):
    option = 0
    while option != "9": 
        print("xxxxxxxxxxxxxxxxxxxxx MENU xxxxxxxxxxxxxxxxxxxxx")
        option = input("1 - Buscar palavra (index) \n2 - Buscar palavra (nome) \n9 - Sair\n")
        if option == "1":
            op = 1
            os.system('cls||clear')
            while op != "0":
                op = input("Numero da palavra (0 - Voltar): ")
                if op != "0":
                    search_by_index(data, op)
                else:
                    os.system('cls||clear')
        elif option == "2":
            name = 1
            os.system('cls||clear')
            while (name != "0"):
                name = input("Nome da palavra (0 - Voltar): ")
                if (name != "0"):
                    search_by_name(data, name)
                else:
                    os.system('cls||clear')
        elif option != "9":
            os.system('cls||clear') 
            print("Escolha uma opção válida")
        else:
            os.system('cls||clear') 
            print("Obrigado por usar o programa!")
    return(0)

data = open_file()

if data != 0:       
    menu(data)
        
    
    

