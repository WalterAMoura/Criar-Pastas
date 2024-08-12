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
import subprocess
from pytube import Search
from pytube import YouTube


def wait_for_user_response():
    start_time = time.time()
    while True:
        logging.info(f'waiting->{start_time}')
        if time.time() - start_time >= 30:
            return False
        user_input = input('Deseja prosseguir e sobrescrever o conteúdo da pasta? (S/N) ').lower()
        if user_input == 's':
            return True
        elif user_input == 'n':
            return False
        time.sleep(1)


def copy_files(source_path, destination_path):
    try:
        shutil.copy2(source_path, destination_path)
        logging.info(f'Arquivo {source_path} copiado para {destination_path}')
    except Exception as e:
        logging.error(f'Erro ao copiar o arquivo {source_path}: {str(e)}')


def copy_config_files(root_path, config):
    for entry in config['filesCopy']:
        source_path = format_path(entry['source'], config)
        destination_path = format_path(entry['destination'], config)
        file_name = format_file_name(entry['fileName'], config)

        if file_name is None:
            logging.warning('Padrão de nome de arquivo não definido. Ignorando a cópia.')
            continue

        source_files = find_files_with_regex(source_path, file_name)
        for file_path in source_files:
            dest_file_path = os.path.join(root_path, destination_path, os.path.basename(file_path))
            copy_files(file_path, dest_file_path)


def create_subfolders(root_path, subfolders):
    for subfolder in subfolders:
        subfolder_path = os.path.join(root_path, subfolder)
        os.makedirs(subfolder_path, exist_ok=True)
        logging.info(f'Criada subpasta: {subfolder_path}')


def sanitize_filename(filename):
    """Remove ou substitui caracteres inválidos para nomes de arquivos no Windows."""
    return re.sub(r'[<>:"/\\|?*]', '_', filename)


def format_path(path, config):
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
    now = datetime.now()
    placeholders = {
        '{{ano}}': now.year,
        '{{numeroMes}}': f'{now.month:02d}',
        '{{nomeMes}}': now.strftime('%B').capitalize(),
        '{{nomeMesReduzido}}': now.strftime('%b').capitalize(),
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
    try:
        matching_files = []
        for file_name in os.listdir(source_path):
            if file_name_pattern.startswith('[r]'):
                regex_pattern = file_name_pattern[3:]
                if re.match(regex_pattern, file_name):
                    logging.info(f'Aplica regex: {file_name} -> {regex_pattern}')
                    file_path = os.path.join(source_path, file_name)
                    matching_files.append(file_path)
            else:
                if file_name == file_name_pattern:
                    logging.info(f'Não aplica regex: {file_name} -> {file_name_pattern}')
                    file_path = os.path.join(source_path, file_name)
                    matching_files.append(file_path)
        logging.info(f'Arquivos encontrados com regex: {matching_files}')
        return matching_files
    except FileNotFoundError as e:
        logging.error(f'Erro ao encontrar o diretório {source_path}: {str(e)}')
        return []


def download_youtube_videos(root_path_normalized, config):
    for entry in config['ytDownloads']:
        video_title = format_file_name(entry['videoTitle'], config)
        root_path = root_path_normalized
        destination_path = format_path(entry['destination'], config)
        try:
            videos = Search(video_title)
            results = ''
            if entry['match'] == 1:
                logging.info(f'Busca pela correspondência exata: {video_title}')
                results = [i.video_id for i in videos.results if i.title.upper() == video_title.upper()]
            else:
                logging.info(f'Busca pela correspondência parcial: {video_title}')
                results = [i.video_id for i in videos.results if video_title.upper() in i.title.upper()]
            if len(results) > 0:
                try:
                    logging.info(f'ID_VIDEO -> "{results[0]}".')
                    url = "https://youtube.com/watch?v=" + results[0]
                    logging.info(f'URL_DOWNLOAD -> "{url}".')
                    youtube = YouTube(url)
                    logging.info(f'Retorno YouTube -> "{youtube}')
                    # video = youtube.streams.first()
                    # video = youtube.streams.get_by_itag(1)
                    video = youtube.streams.get_highest_resolution()
                    logging.info(f'"{video}"')
                    dest_file_path = os.path.join(root_path, destination_path)
                    video.download(output_path=dest_file_path)
                    logging.info(f'Vídeo do YouTube "{video.title}" baixado e copiado para "{dest_file_path}".')
                except Exception as e:
                    logging.error(f'Erro ao realizar download do video {video_title}: {str(e)}')
            else:
                logging.warning(f'Video do YouTube "{video_title}" não foi encontrado.')
        except Exception as e:
            logging.error(f'Erro ao realizar download do video {video_title}: {str(e)}')


def download_youtube_videos_v2(root_path_normalized, config):
    for entry in config['ytDownloads']:
        video_title = format_file_name(entry['videoTitle'], config)

        # channel_name = entry['channelName']
        root_path = root_path_normalized
        destination_path = format_path(entry['destination'], config)
        # busca video pelo canal e titulo
        search_command = f'yt-dlp ytsearch:"{video_title}" --get-id'
        try:
            video_id = subprocess.check_output(search_command, shell=True).decode().strip()
            logging.info(f'ID_VIDEO -> "{video_id}".')
            if video_id:
                dest_file_path = os.path.join(root_path, destination_path)
                url = f"https://youtube.com/watch?v={video_id}"

                # Comando para recuperar o título do video
                original_title_command_video = f'yt-dlp {url} --get-title'
                original_title_video = subprocess.check_output(original_title_command_video, shell=True).decode().strip()
                logging.info(f'ORIGINAL_TITLE_VIDEO -> "{original_title_video}".')

                # Nome base sanitizado para os arquivos
                if original_title_command_video:
                    base_filename = sanitize_filename(original_title_video)
                else:
                    base_filename = sanitize_filename(video_title)

                # Comando para baixar o vídeo e o áudio separadamente
                download_command_video = f'yt-dlp -f bestvideo[ext=mp4] -o "{dest_file_path}video.mp4" {url}'
                download_command_audio = f'yt-dlp -f bestaudio[ext=m4a] -o "{dest_file_path}audio.m4a" {url}'

                subprocess.call(download_command_video, shell=True)
                subprocess.call(download_command_audio, shell=True)

                # Comando para mesclar vídeo e áudio usando ffmpeg
                video_file = f"{dest_file_path}video.mp4"
                audio_file = f"{dest_file_path}audio.m4a"
                logging.info(f'ffmpeg -i "{dest_file_path}video.mp4" -i "{dest_file_path}audio.m4a" -c copy "{dest_file_path}{base_filename}.mp4" -y')
                merge_command = f'ffmpeg -i "{dest_file_path}video.mp4" -i "{dest_file_path}audio.m4a" -c copy "{dest_file_path}{base_filename}.mp4" -y'

                try:
                    subprocess.call(merge_command, shell=True)
                    logging.info(f'Download e mesclagem concluídos!')
                    # Apagar arquivos temporários de vídeo e áudio
                    try:
                        os.remove(video_file)
                        os.remove(audio_file)
                        logging.info(f'Arquivos temporários apagados com sucesso.')
                    except OSError as e:
                        logging.error(f'Erro ao apagar arquivos temporários: {e}')
                except subprocess.CalledProcessError as e:
                    logging.error(f'Erro ao mesclar audio e video {video_title}: {str(e)}')

            else:
                logging.warning(f'Video do YouTube "{video_title}" não foi encontrado.')
        except subprocess.CalledProcessError as e:
            logging.error(f'Erro ao realizar download do video {video_title}: {str(e)}')


def main():
    # Define o idioma para o formato de data em português
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')

    # Configura o logging
    log_filename = 'log.txt'
    log_handler = logging.handlers.RotatingFileHandler(
        log_filename, mode='a', maxBytes=10 * 1024 * 1024, backupCount=10, encoding='utf-8')
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
        if not wait_for_user_response():
            logging.info('Execução cancelada pelo usuário.')
            return

    # Cria a pasta raiz
    os.makedirs(root_path_normalized, exist_ok=True)
    logging.info(f'Criada pasta raiz: {root_path_normalized}')

    # Cria as subpastas
    create_subfolders(root_path_normalized, config['subFolders'])

    # Copia os arquivos de configuração
    copy_config_files(root_path_normalized, config)

    # Baixa videos do youtube
    download_youtube_videos_v2(root_path_normalized, config)

    # Log de finalização do script
    logging.info('--- Fim do script ---')


if __name__ == '__main__':
    main()
