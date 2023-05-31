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

lua
Copy code

6. O script criará a estrutura de pastas e copiará os arquivos de acordo com as configurações fornecidas no arquivo config.json.

7. Após a execução bem-sucedida, a estrutura de pastas será criada e os arquivos serão copiados para suas respectivas pastas.

## Configuração (config.json)

O arquivo config.json contém as configurações para o script. Ele deve estar localizado no mesmo diretório do script (main.py). O arquivo config.json possui a seguinte estrutura:

| Campo       | Descrição                                                  | Tipo   | Exemplo                              |
|-------------|------------------------------------------------------------|--------|--------------------------------------|
| rootPath    | Caminho completo para a pasta raiz                         | String | "C:\\caminho\\para\\pasta\\raiz\\"   |
| subFolders  | Lista de nomes das subpastas a serem criadas               | Array  | ["subpasta1", "subpasta2"]            |
| filesCopy   | Lista de objetos com informações sobre os arquivos a copiar | Array  | Ver detalhes abaixo                   |

Cada objeto dentro da lista filesCopy possui a seguinte estrutura:

| Campo        | Descrição                                             | Tipo   | Exemplo                              |
|--------------|-------------------------------------------------------|--------|--------------------------------------|
| source       | Caminho completo para o arquivo de origem a ser copiado | String | "caminho\\para\\arquivo1.txt"         |
| destination  | Caminho relativo da subpasta de destino para o arquivo | String | "subpasta1\\"                        |

Certifique-se de fornecer os caminhos corretos para as pastas e arquivos no arquivo config.json antes de executar o script.

```
{
  "rootPath": "C:\\Users\\walte\\Desktop\\",
  "subFolders": [
    "01 - ESCOLA SABATINA",
    "02 - ANUNCIOS",
    "03 - SAUDE",
    "04 - PROVAI E VEDE",
    "05 - MENSAGEM MUSICAL",
    "06 - CULTO DIVINO",
    "07 - FUNDO MUSICAL"
  ],
  "filesCopy": [
    {
      "source": "E:\\Projetos\\Igreja\\pastas-copy-paste\\file1.txt",
      "destination": "01 - ESCOLA SABATINA\\file1.txt"
    },
    {
      "source": "E:\\Projetos\\Igreja\\pastas-copy-paste\\file2.txt",
      "destination": "02 - ANUNCIOS\\file2.txt"
    },
    {
      "source": "E:\\Projetos\\Igreja\\pastas-copy-paste\\file3.txt",
      "destination": "03 - SAUDE\\file3.txt"
    }
  ]
}
```

## Compilação para Executável (opcional)

Você pode compilar o script Python em um executável independente usando ferramentas como PyInstaller, cx_Freeze ou Py2exe. Isso permitirá que você execute o script em um ambiente sem a necessidade de ter o Python instalado.

Instale o PyInstaller:

### PyInstaller

```
pip install pyinstaller
```
### Navegue até o diretório onde o seu script Python está localizado:

```
cd /caminho/para/o/diretorio
```

### Compile o script usando o PyInstaller:
```
pyinstaller --add-data "config.json;." nome_do_script.py
```

__Isso criará um executável na pasta dist com o nome nome_do_script.exe (no Windows) ou nome_do_script (no Linux/macOS).
Copie o arquivo config.json para o mesmo diretório do executável criado.__

__Agora você pode executar o arquivo nome_do_script.exe (no Windows) ou nome_do_script (no Linux/macOS), e o programa utilizará as configurações do arquivo config.json para criar a estrutura de pastas e copiar os arquivos conforme especificado.
Certifique-se de substituir nome_do_script pelo nome do seu script Python real.__

__Aqui note que também usei o "--add-data" para especificar um arquivo que necessário para execução do meu script, como isso complilador ira copiar o arquivo.__

> <font color="grey">Obs.: Após compilar deve-se copiar o arquivo</font> <font color="red">__config.json__</font> <font color="grey"> para o diretório raiz do executável
