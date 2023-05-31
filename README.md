# Script de Criação de Pastas e Cópia de Arquivos

Este script em Python cria uma estrutura de pastas e copia arquivos de acordo com as configurações fornecidas em um arquivo JSON.

## Execução

Certifique-se de ter o Python 3 instalado em seu ambiente de execução.

1. Faça o download do código-fonte do script para sua máquina.

2. Abra um terminal ou prompt de comando e navegue até o diretório onde o código-fonte do script foi salvo.

3. Execute o seguinte comando para instalar as dependências necessárias:

pip install unidecode

arduino
Copy code

4. Certifique-se de ter um arquivo JSON de configuração (config.json) preparado com as informações corretas. Veja a seção abaixo para detalhes sobre o arquivo config.json.

5. Execute o script usando o seguinte comando:

python main.py

swift
Copy code

6. O script criará a estrutura de pastas e copiará os arquivos de acordo com as configurações fornecidas no arquivo config.json.

7. Após a execução bem-sucedida, a estrutura de pastas será criada e os arquivos serão copiados para suas respectivas pastas.

## Configuração (config.json)

O arquivo config.json contém as configurações para o script. Ele deve estar localizado no mesmo diretório do script (main.py). O arquivo config.json possui a seguinte estrutura:

```json
{
"rootPath": "C:\\caminho\\para\\pasta\\raiz\\",
"subFolders": [
 "subpasta1",
 "subpasta2",
 "subpasta3"
],
"filesCopy": [
 {
   "source": "caminho\\para\\arquivo1.txt",
   "destination": "subpasta1\\"
 },
 {
   "source": "caminho\\para\\arquivo2.txt",
   "destination": "subpasta2\\"
 },
 {
   "source": "caminho\\para\\arquivo3.txt",
   "destination": "subpasta3\\"
 }
]
}
rootPath (string): O caminho completo para a pasta raiz onde a estrutura de pastas será criada.

subFolders (array): Uma lista de nomes das subpastas que serão criadas dentro da pasta raiz.

filesCopy (array): Uma lista de objetos que contêm informações sobre os arquivos a serem copiados. Cada objeto possui os seguintes campos:

source (string): O caminho completo para o arquivo de origem que será copiado.
destination (string): O caminho relativo da subpasta de destino onde o arquivo será copiado.
Certifique-se de fornecer os caminhos corretos para as pastas e arquivos no arquivo config.json antes de executar o script.

Compilação para Executável (opcional)
Você pode compilar o script Python em um executável independente usando ferramentas como PyInstaller, cx_Freeze ou Py2exe. Isso permitirá que você execute o script em um ambiente sem a necessidade de ter o Python instalado.

Consulte a documentação das ferramentas de compilação para obter mais informações sobre como compilar o script em um executável.

bash
Copy code

Lembre-se de substituir os caminhos e nomes de arquivo mencionados no exemplo pelo seu próprio caminho e nomes de arquivo relevantes.

Espero que isso ajude!