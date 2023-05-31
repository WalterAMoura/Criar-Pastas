import os
import json
import shutil
from datetime import datetime
from unidecode import unidecode
import locale

def copy_files(source_path, destination_path):
    try:
        shutil.copy2(source_path, destination_path)
        print(f'Arquivo {source_path} copiado para {destination_path}')
    except Exception as e:
        print(f'Erro ao copiar o arquivo {source_path}: {str(e)}')

def copy_config_files(root_path, config):
    for entry in config['filesCopy']:
        source_path = os.path.join(entry['source'], entry['fileName'])
        destination_path = os.path.join(root_path, entry['destination'], entry['fileName'])

        copy_files(source_path, destination_path)

def create_subfolders(root_path, subfolders):
    for subfolder in subfolders:
        subfolder_path = os.path.join(root_path, subfolder)
        os.makedirs(subfolder_path, exist_ok=True)

def main():
    # Define o idioma para o formato de data em português
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')

    # Obtém a data atual
    now = datetime.now()
    formatted_date = now.strftime('%A %d DE %B %Y').upper()

    # Lê as configurações do arquivo config.json
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path) as file:
        config = json.load(file)

    # Obtém o caminho da pasta raiz a partir do arquivo de configuração
    root_path = config['rootPath']
    root_path = os.path.join(root_path, formatted_date)

    # Remove a acentuação do nome da pasta raiz
    root_path_normalized = unidecode(root_path)

    # Obtém a lista de subpastas a partir do arquivo de configuração
    subfolders = config['subFolders']

    # Cria as subpastas
    create_subfolders(root_path_normalized, subfolders)

    # Copia os arquivos de configuração
    copy_config_files(root_path_normalized, config)

    print('Estrutura de pastas criada com sucesso!')

if __name__ == '__main__':
    main()
