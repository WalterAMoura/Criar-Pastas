# Script de Criação de Pastas e Cópia de Arquivos

Este script em Python cria uma estrutura de pastas e copia arquivos de acordo com as configurações fornecidas em um arquivo JSON.

## Execução

Certifique-se de ter o Python 3 instalado em seu ambiente de execução.

1. Faça o download do código-fonte do script para sua máquina.

2. Abra um terminal ou prompt de comando e navegue até o diretório onde o código-fonte do script foi salvo.

3. Execute o seguinte comando para instalar as dependências necessárias:

```
pip install unidecode
```

4. Certifique-se de ter um arquivo JSON de configuração (config.json) preparado com as informações corretas. Veja a seção abaixo para detalhes sobre o arquivo config.json.

5. Execute o script usando o seguinte comando:

6. O script criará a estrutura de pastas e copiará os arquivos de acordo com as configurações fornecidas no arquivo config.json.

7. Após a execução bem-sucedida, a estrutura de pastas será criada e os arquivos serão copiados para suas respectivas pastas.

## Configuração (config.json)

O arquivo config.json contém as configurações para o script. Ele deve estar localizado no mesmo diretório do script (main.py). O arquivo config.json possui a seguinte estrutura:

| Campo | Descrição | Tipo | Exemplo |
| --- | --- | --- | --- |
| rootPath | O diretório raiz onde serão criadas as pastas e copiados os arquivos. Certifique-se de usar barras duplas (`\\`) no lugar de barras simples (`\`). | String | "C:\\caminho\\para\\pasta\\raiz\\" |
| dayOfExecution | Lista dos dias da semana em que o script pode ser executado e as pastas podem ser criadas. Use a abreviação de três letras para o dia (por exemplo, "seg", "ter", "qua"). | Lista de Strings | ["seg", "qua", "sex"] |
| subFolders | Lista de nomes fictícios das subpastas a serem criadas dentro da pasta raiz. Certifique-se de usar o formato correto para os nomes das subpastas. | Lista de Strings | ["Subpasta1", "Subpasta2", "Subpasta3"] |
| filesCopy | Lista dos arquivos fictícios a serem copiados para suas respectivas subpastas. Cada item da lista deve conter os campos source, fileName e destination. Certifique-se de usar barras duplas (`\\`) no lugar de barras simples (`\`). | Lista de Objetos JSON | [  {     "source": "C:\\caminho\\para\\arquivos\\",    "fileName": "arquivo1.txt",     "destination": "Subpasta1\\"   },  {    "source": "C:\\caminho\\para\\arquivos\\",    "fileName": "arquivo2.txt",    "destination": "Subpasta2\\"  },  {    "source": "C:\\caminho\\para\\arquivos\\",    "fileName": "arquivo3.txt",    "destination": "Subpasta3\\"  }] |

Certifique-se de fornecer os caminhos corretos para as pastas e arquivos no arquivo config.json antes de executar o script.

```
{
  "rootPath": "C:\\caminho\\para\\pasta\\raiz\\",
  "dayOfExecution": ["seg", "qua", "sex"],
  "subFolders": [
    "Subpasta1",
    "Subpasta2",
    "Subpasta3"
  ],
  "filesCopy": [
    {
      "source": "C:\\caminho\\para\\arquivos\\",
      "fileName": "arquivo1.txt",
      "destination": "Subpasta1\\"
    },
    {
      "source": "C:\\caminho\\para\\arquivos\\",
      "fileName": "arquivo2.txt",
      "destination": "Subpasta2\\"
    },
    {
      "source": "C:\\caminho\\para\\arquivos\\",
      "fileName": "arquivo3.txt",
      "destination": "Subpasta3\\"
    }
  ]
}

```

## Compilação para Executável (opcional)

Você pode compilar o script Python em um executável independente usando ferramentas como PyInstaller, cx_Freeze ou Py2exe. Isso permitirá que você execute o script em um ambiente sem a necessidade de ter o Python instalado.

## Instale e compile usando o PyInstaller:

* PyInstaller

```
pip install pyinstaller
```
* Navegue até o diretório onde o seu script Python está localizado:

```
cd /caminho/para/o/diretorio
```

* Compile o script usando o PyInstaller:
```
ppyinstaller --onefile --add-data "config.json;." main.py
```
 
__Isso criará um executável na pasta dist com o nome nome_do_script.exe (no Windows) ou nome_do_script (no Linux/macOS)..__

__Agora você pode executar o arquivo main.exe (no Windows) ou main (no Linux/macOS), e o programa utilizará as configurações do arquivo config.json para criar a estrutura de pastas e copiar os arquivos conforme especificado.__

__Aqui note que também usei o "--add-data" para especificar um arquivo que necessário para execução do meu script, como isso complilador ira copiar o arquivo.__

> <font color="grey">__Obs.: Após compilar deve-se copiar o arquivo</font> <font color="red">__config.json__</font> <font color="grey"> para o diretório raiz do executável.__
