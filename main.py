import os
import shutil
import time
import locale

def create_folders(root_path):
    # Obter a data atual
    now = time.localtime()
    # Configurar localização para formatar o mês no formato brasileiro
    locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
    # Formatar a data para o nome da pasta raiz
    root_folder_name = time.strftime("%A %d %B %Y", now).upper()
    root_folder_path = os.path.join(root_path, root_folder_name)

    # Verificar se a pasta raiz já existe
    if os.path.exists(root_folder_path):
        overwrite = input("A pasta raiz já existe. Deseja sobrescrevê-la? (S/N): ")
        if overwrite.lower() != 's':
            print("Processo cancelado.")
            return
        shutil.rmtree(root_folder_path)

    # Criar a pasta raiz
    os.makedirs(root_folder_path)

    # Criar as subpastas
    subfolders = [
        "01 - ESCOLA SABATINA",
        "02 - ANÚNCIOS",
        "03 - SAÚDE",
        "04 - PROVAI E VEDE",
        "05 - MENSAGEM MÚSICAL",
        "06 - CULTO DIVINO",
        "07 - FUNDO MUSICAL"
    ]

    for folder in subfolders:
        os.makedirs(os.path.join(root_folder_path, folder))

def copy_files(source_path, destination_path):
    shutil.copy(source_path, destination_path)

def copy_config_files(root_path):
    files_to_copy = [
        ("source/file1.txt", "01 - ESCOLA SABATINA/file1.txt"),
        ("source/file2.txt", "04 - PROVAI E VEDE/file2.txt"),
        ("source/file3.txt", "07 - FUNDO MUSICAL/file3.txt")
    ]

    for source, destination in files_to_copy:
        source_path = os.path.join(root_path, source)
        destination_path = os.path.join(root_path, destination)
        copy_files(source_path, destination_path)

root_path = r"C:\Users\walte\Desktop"

create_folders(root_path)
#   copy_config_files(root_path)

print("Estrutura de pastas criada com sucesso!")

