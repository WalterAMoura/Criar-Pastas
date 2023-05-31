import os
import shutil
import datetime
import locale
import json

def delete_directory(path):
    shutil.rmtree(path)

def create_folders(root_path):
    # Obter a data atual
    now = datetime.datetime.now()

    # Definir a configuração para o idioma brasileiro
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

    # Formatar a data para o nome da pasta raiz
    folder_name = now.strftime("%A %d DE %B %Y").upper()

    # Verificar se a pasta raiz já existe
    root_folder_path = os.path.join(root_path, folder_name)

    if os.path.exists(root_folder_path):
        # Pasta raiz já existe, solicitar confirmação do usuário
        confirm = input("A pasta raiz já existe. Deseja sobrescrevê-la? (S/N): ")

        if confirm.upper() != "S":
            # O usuário não confirmou, encerrar o programa
            print("Programa encerrado.")
            return

        delete_directory(root_folder_path)

    # Criar a pasta raiz
    os.makedirs(root_folder_path)

    # Criar as subpastas
    subfolders = [
        "01 - ESCOLA SABATINA",
        "02 - ANÚNCIOS",
        "03 - SAÚDE",
        "04 - PROVAI E VEDE",
        "05 - MENSAGEM MUSICAL",
        "06 - CULTO DIVINO",
        "07 - FUNDO MUSICAL"
    ]

    for subfolder in subfolders:
        subfolder_path = os.path.join(root_folder_path, subfolder)

        # Verificar se a subpasta já existe e removê-la se necessário
        if os.path.exists(subfolder_path):
            delete_directory(subfolder_path)

        os.makedirs(subfolder_path)

def copy_files(source_path, destination_path):
    shutil.copy(source_path, destination_path)

def copy_config_files(config_file_path, destination_path):
    with open(config_file_path, "r") as file:
        files_to_copy = json.load(file)

    for file_info in files_to_copy:
        source_file_path = file_info["source"]
        destination_file_path = os.path.join(destination_path, os.path.basename(source_file_path))

        copy_files(source_file_path, destination_file_path)

def main():
    root_path = "C:\\Users\\walte\\Desktop"
    config_file_path = os.path.join(os.path.dirname(__file__), "config.json")

    create_folders(root_path)

    # Obter a data atual
    now = datetime.datetime.now()

    # Definir a configuração para o idioma brasileiro
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

    # Formatar a data para o nome da pasta raiz
    folder_name = now.strftime("%A %d DE %B %Y").upper()

    # Caminho completo da pasta raiz
    root_folder_path = os.path.join(root_path, folder_name)

    copy_config_files(config_file_path, root_folder_path)

    print("Estrutura de pastas criada com sucesso!")

if __name__ == "__main__":
    main()
