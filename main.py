import os
import shutil
import datetime

def create_folders(root_path):
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
        subfolder_path = os.path.join(root_path, subfolder)

        # Verificar se a subpasta já existe e removê-la se necessário
        if os.path.exists(subfolder_path):
            shutil.rmtree(subfolder_path)

        os.makedirs(subfolder_path)

def copy_files(source_path, destination_path):
    shutil.copy(source_path, destination_path)

def copy_config_files(source_path, destination_path):
    files_to_copy = [
        {"source": "file1.txt", "destination": "01 - ESCOLA SABATINA/file1.txt"},
        {"source": "file2.txt", "destination": "04 - PROVAI E VEDE/file2.txt"},
        {"source": "file3.txt", "destination": "06 - CULTO DIVINO/file3.txt"}
    ]

    for file_info in files_to_copy:
        source_file_path = os.path.join(source_path, file_info["source"])
        destination_file_path = os.path.join(destination_path, file_info["destination"])

        copy_files(source_file_path, destination_file_path)

def main():
    root_path = "C:\\Users\\walte\\Desktop"
    source_path = "E:\\Projetos\\Igreja\\pastas-copy-paste"

    # Criar a pasta raiz com base na data atual
    now = datetime.datetime.now()
    folder_name = now.strftime("%Y-%m-%d")
    destination_path = os.path.join(root_path, folder_name)

    if os.path.exists(destination_path):
        # Pasta raiz já existe, solicitar confirmação do usuário
        confirm = input("A pasta raiz já existe. Deseja sobrescrevê-la? (S/N): ")

        if confirm.upper() != "S":
            # O usuário não confirmou, encerrar o programa
            print("Programa encerrado.")
            return

        shutil.rmtree(destination_path)

    os.makedirs(destination_path)

    create_folders(destination_path)
    copy_config_files(source_path, destination_path)

if __name__ == "__main__":
    main()


