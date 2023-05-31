import os
import json
import shutil
from datetime import datetime
from unidecode import unidecode
import locale

def copy_files(source_path, destination_path):
    try:
        shutil.copy2(source_path, destination_path)
        print(f'Arquivo copiado: {source_path} -> {destination_path}')
    except FileNotFoundError:
        print(f'Erro ao copiar arquivo: {source_path} -> {destination_path}')

def copy_config_files(root_path):
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')

    with open(config_path) as file:
        config = json.load(file)

    for entry in config['filesCopy']:
        source_path = os.path.join(config['rootPath'], entry['source'])
        destination_path = os.path.join(root_path, entry['destination'])

        copy_files(source_path, destination_path)

def create_subfolders(root_path):
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')

    with open(config_path) as file:
        config = json.load(file)

    for subfolder in config['subFolders']:
        subfolder_path = os.path.join(root_path, subfolder)
        os.makedirs(subfolder_path, exist_ok=True)

def main():
    # Defina o idioma para o formato de data em português
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')

    # Obtenha a data atual
    now = datetime.now()
    formatted_date = now.strftime('%A %d DE %B %Y').upper()

    # Verifique se o dia da semana está na lista de dias de execução
    weekday = now.strftime('%a').lower()
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')

    with open(config_path) as file:
        config = json.load(file)

    if weekday not in config['dayOfExecution']:
        print('O script não está configurado para ser executado hoje.')
        return

    # Crie a pasta raiz com a data formatada
    root_path = os.path.join(config['rootPath'], formatted_date)

    # Remova a acentuação do nome da pasta raiz
    root_path_normalized = unidecode(root_path)

    # Crie as subpastas
    create_subfolders(root_path_normalized)

    # Copie os arquivos de configuração
    copy_config_files(root_path_normalized)

    print('Estrutura de pastas criada com sucesso!')

if __name__ == '__main__':
    main()
