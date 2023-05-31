import os
import json
import shutil
from datetime import datetime
from unidecode import unidecode
import locale

def copy_files(source_path, destination_path):
    shutil.copy2(source_path, destination_path)

def copy_config_files(root_path, config):
    for entry in config['filesCopy']:
        source_path = os.path.join(entry['source'], entry['fileName'])
        destination_path = os.path.join(root_path, entry['destination'], entry['fileName'])

        copy_files(source_path, destination_path)

def create_subfolders(root_path, subfolders):
    os.makedirs(root_path, exist_ok=True)

    for subfolder in subfolders:
        subfolder_path = os.path.join(root_path, subfolder)
        os.makedirs(subfolder_path, exist_ok=True)

def main():
    # Defina o idioma para o formato de data em português
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')

    # Obtenha a data atual
    now = datetime.now()
    formatted_date = now.strftime('%A %d DE %B %Y').upper()

    # Carregue as informações do arquivo de configuração
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path) as file:
        config = json.load(file)

    # Obtenha o diretório raiz e normalize o nome removendo a acentuação
    root_path = os.path.join(config['rootPath'], formatted_date)
    root_path_normalized = unidecode(root_path)

    # Crie as subpastas
    subfolders = config['subFolders']
    create_subfolders(root_path_normalized, subfolders)

    # Copie os arquivos de configuração
    copy_config_files(root_path_normalized, config)

    print('Estrutura de pastas criada com sucesso!')

if __name__ == '__main__':
    main()
