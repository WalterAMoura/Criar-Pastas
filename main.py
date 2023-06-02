import os
import json
import shutil
from datetime import datetime
from unidecode import unidecode
import re
import locale
import logging
import logging.handlers
import time

def copy_files(source_path, destination_path):
    """
    Copia um arquivo de origem para o destino.

    Args:
        source_path (str): Caminho do arquivo de origem.
        destination_path (str): Caminho de destino do arquivo.
    """
    try:
        shutil.copy2(source_path, destination_path)
        logging.info(f'Arquivo {source_path} copiado para {destination_path}')
    except Exception as e:
        logging.error(f'Erro ao copiar o arquivo {source_path}: {str(e)}')

def copy_config_files(root_path, config):
    """
    Copia os arquivos listados no arquivo de configuração.

    Args:
        root_path (str): Caminho da pasta raiz.
        config (dict): Configurações do script.
    """
    for entry in config['filesCopy']:
        source_path = format_path(entry['source'], config)
        destination_path = format_path(entry['destination'], config)
        file_name = format_file_name(entry['fileName'], config)

        source_files = find_files_with_regex(source_path, file_name)
        for file_path in source_files:
            dest_file_path = os.path.join(root_path, destination_path, os.path.basename(file_path))
            copy_files(file_path, dest_file_path)

def create_subfolders(root_path, subfolders):
    """
    Cria as subpastas no caminho especificado.

    Args:
        root_path (str): Caminho da pasta raiz.
        subfolders (list): Lista de nomes de subpastas a serem criadas.
    """
    for subfolder in subfolders:
        subfolder_path = os.path.join(root_path, subfolder)
        os.makedirs(subfolder_path, exist_ok=True)
        logging.info(f'Criada subpasta: {subfolder_path}')

def format_path(path, config):
    """
    Formata o caminho substituindo os placeholders pelos valores correspondentes.

    Args:
        path (str): Caminho a ser formatado.
        config (dict): Configurações do script.

    Returns:
        str: Caminho formatado.
    """
    now = datetime.now()
    placeholders = {
        '{{ano}}': now.year,
        '{{numeroMes}}': f'{now.month:02d}',
        '{{nomeMes}}': now.strftime('%B').capitalize(),
        '{{dia}}': f'{now.day:02d}',
        '{{hora}}': f'{now.hour:02d}',
        '{{minuto}}': f'{now.minute:02d}',
        '{{segundo}}': f'{now.second:02d}',
    }
    for placeholder, value in placeholders.items():
        path = path.replace(placeholder, str(value))
    logging.info(f'Caminho formatado: {path}')
    return path

def format_file_name(file_name, config):
    """
    Formata o nome do arquivo substituindo os placeholders pelos valores correspondentes.

    Args:
        file_name (str): Nome do arquivo a ser formatado.
        config (dict): Configurações do script.

    Returns:
        str: Nome do arquivo formatado.
    """
    now = datetime.now()
    placeholders = {
        '{{ano}}': now.year,
        '{{numeroMes}}': f'{now.month:02d}',
        '{{nomeMes}}': now.strftime('%B').capitalize(),
        '{{dia}}': f'{now.day:02d}',
        '{{hora}}': f'{now.hour:02d}',
        '{{minuto}}': f'{now.minute:02d}',
        '{{segundo}}': f'{now.second:02d}',
        '{{nomeArquivo}}': os.path.splitext(os.path.basename(file_name))[0],
    }
    for placeholder, value in placeholders.items():
        file_name = file_name.replace(placeholder, str(value))
    logging.info(f'Nome do arquivo formatado: {file_name}')
    return file_name

def find_files_with_regex(source_path, file_name_pattern):
    """
    Encontra os arquivos que correspondem ao padrão de nome de arquivo usando expressões regulares.

    Args:
        source_path (str): Caminho da pasta de origem.
        file_name_pattern (str): Padrão do nome do arquivo usando expressões regulares.

    Returns:
        list: Lista de caminhos dos arquivos correspondentes.
    """
    try:
        matching_files = []
        escaped_file_name_pattern = re.escape(file_name_pattern)
        for file_name in os.listdir(source_path):
            if re.match(escaped_file_name_pattern, file_name):
                file_path = os.path.join(source_path, file_name)
                matching_files.append(file_path)
        return matching_files
    except FileNotFoundError as e:
        logging.error(f'Erro ao encontrar o diretório {source_path}: {str(e)}')
        return []

def main():
    # Define o idioma para o formato de data em português
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')

    # Configura o logging
    log_filename = 'log.txt'
    log_handler = logging.handlers.RotatingFileHandler(
        log_filename, maxBytes=10 * 1024 * 1024, backupCount=10)
    log_formatter = logging.Formatter(
        '%(asctime)s [%(funcName)s]:[%(levelname)s] - %(message)s',
        datefmt='%Y%m%d-%H:%M:%S')
    log_handler.setFormatter(log_formatter)
    logging.root.addHandler(log_handler)
    logging.root.setLevel(logging.INFO)

    # Log de início do script
    logging.info('--- Início do script ---')

    # Obtém a data atual
    now = datetime.now()
    formatted_date = now.strftime('%A %d DE %B %Y').upper()
    logging.info(f'Data atual: {formatted_date}')

    # Lê as configurações do arquivo config.json
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path) as file:
        config = json.load(file)

    # Verifica se o dia da semana está habilitado para a execução
    weekday = now.strftime('%a').lower()
    weekday_name_complete = now.strftime('%A').upper()
    if weekday not in config['dayOfExecution']:
        logging.info(f'O script não está configurado para ser executado no dia: {weekday_name_complete}.')
        logging.info('Execução cancelada.')
        return

    # Obtém o caminho da pasta raiz a partir do arquivo de configuração
    root_path = config['rootPath']
    root_path = os.path.join(root_path, formatted_date)

    # Remove a acentuação do nome da pasta raiz
    root_path_normalized = unidecode(root_path)

    # Verifica se a pasta raiz já existe
    if os.path.exists(root_path_normalized):
        logging.info(f'A pasta raiz {root_path_normalized} já existe.')
        confirm = input(f'Deseja prosseguir e sobrescrever o conteúdo da pasta? (S/N) ')
        if confirm.lower() != 's':
            logging.info('Execução cancelada pelo usuário.')
            return

    # Cria a pasta raiz
    os.makedirs(root_path_normalized, exist_ok=True)
    logging.info(f'Criada pasta raiz: {root_path_normalized}')

    # Cria as subpastas
    create_subfolders(root_path_normalized, config['subFolders'])

    # Copia os arquivos de configuração
    copy_config_files(root_path_normalized, config)

    # Log de finalização do script
    logging.info('--- Fim do script ---')

if __name__ == '__main__':
    main()
