import os
import json
import shutil

def copy_files(source_path, destination_path):
    shutil.copy(source_path, destination_path)

def copy_config_files(root_path):
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')

    with open(config_path) as file:
        config = json.load(file)

    for entry in config:
        source_path = entry['source']
        destination_path = os.path.join(root_path, entry['destination'])

        copy_files(source_path, destination_path)

def main():
    # Obtenha a data atual
    import datetime
    now = datetime.datetime.now()
    formatted_date = now.strftime('%A %d DE %B %Y').upper()

    # Defina o caminho da pasta raiz
    root_path = os.path.join('C:\\Users\\walte\\Desktop', formatted_date)

    # Crie as pastas
    os.makedirs(root_path, exist_ok=True)

    # Copie os arquivos de configuração
    copy_config_files(root_path)

    print('Estrutura de pastas criada com sucesso!')

if __name__ == '__main__':
    main()
