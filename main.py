import os
import json
import shutil
from datetime import datetime
from unidecode import unidecode
import locale
import re

def copy_files(source_path, destination_path):
    try:
        shutil.copy2(source_path, destination_path)
        print(f'Arquivo {source_path} copiado para {destination_path}')
    except Exception as e:
        print(f'Erro ao copiar o arquivo {source_path}: {str(e)}')

def copy_config_files(root_path):
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')

    with open(config_path) as file:
        config = json.load(file)

    for entry in config['filesCopy']:
        source_path = entry['source']
        destination_path = os.path.join(root_path, entry['destination'])

        # Obtenha o nome do arquivo original
        file_name = entry['fileName']

        # Substitua os placeholders no nome do arquivo usando regex
        placeholders = re.findall(r'\{\{(.*?)\}\}', file_name)
        for placeholder in placeholders:
            if placeholder == 'dia':
                # Obtenha o dia atual
                dia_atual = datetime.now().strftime('%d')
                file_name = file_name.replace('{{dia}}', dia_atual)
            elif placeholder == 'ano':
                # Obtenha o ano atual
                ano_atual = datetime.now().strftime('%Y')
                file_name = file_name.replace('{{ano}}', ano_atual)
            elif placeholder == 'numeroMes':
                # Obtenha o número do mês atual
                numero_mes_atual = datetime.now().strftime('%m')
                file_name = file_name.replace('{{numeroMes}}', numero_mes_atual)
            elif placeholder == 'nomeMes':
                # Obtenha o nome do mês atual
                nome_mes_atual = datetime.now().strftime('%B')
                file_name = file_name.replace('{{nomeMes}}', nome_mes_atual.upper())

        # Copie o arquivo apenas se corresponder ao padrão do regex
        if re.match(file_name, os.path.basename(source_path)):
            copy_files(source_path, destination_path)

def create_subfolders(root_path):
    subfolders = [
        '01 - ESCOLA SABATINA',
        '02 - ANUNCIOS',
        '03 - SAUDE',
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
    root_path = os.path.join('C:\\Users\\username\\Desktop', formatted_date)  # Substitua "username" pelo seu nome de usuário

    # Remova a acentuação do nome da pasta raiz
    root_path_normalized = unidecode(root_path)

    # Crie as subpastas
    create_subfolders(root_path_normalized)

    # Copie os arquivos de configuração
    copy_config_files(root_path_normalized)

    print('Estrutura de pastas criada com sucesso!')

if __name__ == '__main__':
    main()
