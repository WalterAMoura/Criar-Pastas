import os
import json
import shutil
from datetime import datetime
import locale

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

def create_subfolders(root_path):
    subfolders = [
        '01 - ESCOLA SABATINA',
        '02 - ANÚNCIOS',
        '03 - SAÚDE',
        '04 - PROVAI E VEDE',
        '05 - MENSAGEM MUSICAL',
        '06 - CULTO DIVINO',
        '07 - FUNDO MUSICAL'
    ]

    for subfolder in subfolders:
        subfolder_path = os.path.join(root_path, subfolder)
        os.makedirs(subfolder_path, exist_ok=True)

def main():
    # Defina o idioma para o formato de data em português
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')

    # Obtenha a data atual
    now = datetime.now()
    formatted_date = now.strftime('%A %d DE %B %Y').upper()

    # Crie a pasta raiz com a data formatada
    root_path = os.path.join('C:\\Users\\walte\\Desktop', formatted_date)

    # Crie as subpastas
    create_subfolders(root_path)

    # Copie os arquivos de configuração
    copy_config_files(root_path)

    print('Estrutura de pastas criada com sucesso!')

if __name__ == '__main__':
    main()
