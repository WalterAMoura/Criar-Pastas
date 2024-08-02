# Script de Criação de Pastas e Cópia de Arquivos

Este script em Python cria uma estrutura de pastas e copia arquivos de acordo com as configurações fornecidas em um arquivo JSON.

## Execução

Certifique-se de ter o Python 3 instalado em seu ambiente de execução.

1. Faça o download do código-fonte do script para sua máquina.

2. Abra um terminal ou prompt de comando e navegue até o diretório onde o código-fonte do script foi salvo.

3. Execute o seguinte comando para instalar as dependências necessárias:

```
pip install unidecode
pip install pytube3
```

4. Certifique-se de ter um arquivo JSON de configuração (config.json) preparado com as informações corretas. Veja a seção abaixo para detalhes sobre o arquivo config.json.

5. Execute o script usando o seguinte comando:

6. O script criará a estrutura de pastas e copiará os arquivos de acordo com as configurações fornecidas no arquivo config.json.

7. Após a execução bem-sucedida, a estrutura de pastas será criada e os arquivos serão copiados para suas respectivas pastas.

## Configuração (config.json)

O arquivo config.json contém as configurações para o script. Ele deve estar localizado no mesmo diretório do script (main.py). O arquivo config.json possui a seguinte estrutura:

| Campo            | Descrição                                         | Tipo     | Suporte Placeholders | Suporte Regex | Exemplo                                           |
|------------------|---------------------------------------------------|----------|----------------------|---------------|----------------------------------------------------|
| rootPath         | Caminho raiz onde as pastas serão criadas         | String   | false                | false         |"C:\\Users\\usuario\\Desktop\\"                    |
| dayOfExecution   | Dias da semana em que o script pode ser executado | Lista    | false                | false         |["dom", "qua", "sab"]                              |
| subFolders       | Lista de subpastas a serem criadas                | Lista    | false                | false         |["A", "B", "C"]                                    |
| filesCopy        | Lista de arquivos a serem copiados                | Lista    | -                    | -             |Veja a tabela 1 de arquivos a serem copiados abaixo |
| ytDownloads        | Lista de arquivos a serem baixados do YouTube     | Lista    | -                  | -             | Veja a tabela 2 de arquivos a serem copiados abaixo |

### Tabela 1 de arquivos a serem copiados:

| Campo       | Descrição                                  | Tipo   | Suporte Placeholders | Suporte Regex |Exemplo com Placeholders                      | Exemplo sem Placeholders                           |
|-------------|--------------------------------------------|--------|----------------------|---------------|-----------------------------------------------|---------------------------------------------------|
| source      | Caminho da pasta de origem dos arquivos    | String | true                 | false         |"C:\\Caminho\\Origem\\{{ano}}\\{{nomeMes}}\\" | "C:\\Caminho\\Origem\\subpasta\\"                  |
| fileName    | Padrão de nome do arquivo usando regex     | String | true                 | true          |"[r]{{dia}}_[A-Za-z]+\\.mp4"                  | "file[0-9]+\\.txt"                                |
| destination | Subpasta de destino para o arquivo         | String | true                 | false         |"{{numeroMes}}_{{nomeMes}}\\"                 | "A\\"                                             |

### Tabela 2 de arquivos a serem baixados do YouTube:

| Campo       | Descrição                                                                                                                   | Tipo    | Suporte Placeholders | Suporte Regex | Exemplo com Placeholders                        | Exemplo sem Placeholders            |
|-------------|-----------------------------------------------------------------------------------------------------------------------------|---------|----------------------|---------------|-------------------------------------------------|-------------------------------------|
| videoTitle  | Nome do video a ser baixado                                                                                                 | String  | true                 | false         | "Video Download \| {{dia}} {{nomeMes}} {{ano}}" | "Video Download \| 01 Janeiro 2001" |
| destination | Subpasta de destino para o arquivo                                                                                          | String  | true                 | false         | "{{numeroMes}}_{{nomeMes}}\\"                   | "A\\"                               |
| match       | Verifica correspondencia do nome arquivo, use 'true' para correspondência exata e use 'false' para **correspondecia parcial | Boolean | false                | false         | N/A                                             | true                                |

> ** A busca parcial, irá fazer o download do primeiro item que for encontrado com parte do nome especificado.

### Placeholders suportados

| Placeholder         | Descrição                                            |
|---------------------|------------------------------------------------------|
| {{ano}}             | Ano atual com 4 dígitos                              |
| {{numeroMes}}       | Mês atual com 2 dígitos (preenchido com zero)        |
| {{nomeMes}}         | Nome do mês atual (inicial maiúscula)                |
| {{nomeMesReduzido}} | Nome do mês atual reduzido (inicial maiúscula)       |
| {{dia}}             | Dia do mês atual com 2 dígitos (preenchido com zero) |
| {{hora}}            | Hora atual com 2 dígitos (preenchido com zero)       |
| {{minuto}}          | Minuto atual com 2 dígitos (preenchido com zero)     |
| {{segundo}}         | Segundo atual com 2 dígitos (preenchido com zero)    |
| {{nomeArquivo}}     | Nome do arquivo original (sem extensão)              |

#### Exemplos:
1. Arquivo com placeholders:
   - source: "C:\\Caminho\\Origem\\{{ano}}\\{{nomeMes}}\\"
   - fileName: "[r]{{dia}}_[A-Za-z]+\\.mp4"
   - destination: "{{numeroMes}}_{{nomeMes}}\\"

2. Arquivo sem placeholders:
   - source: "C:\\Caminho\\Origem\\subpasta\\"
   - fileName: "[r]file[0-9]+\\.txt"
   - destination: "A\\"

3. Arquivo com placeholders misturados:
   - source: "C:\\Caminho\\Origem\\{{ano}}\\subpasta\\"
   - fileName: "[r]file_{{nomeMes}}_[0-9]+\\.txt"
   - destination: "{{numeroMes}}_{{nomeMes}}\\"

- O script utiliza regex para buscar arquivos que correspondam ao padrão especificado no campo fileName. O uso do sufixo __"[r]"__ indica que o campo fileName será tratado como uma expressão regular. Caso não seja fornecido o sufixo "[r]", o campo fileName será tratado como uma correspondência exata de nome de arquivo.
- O campo `fileName` permite o uso de expressões regulares para encontrar arquivos correspondentes.
- Os placeholders disponíveis para uso em `source`, `fileName` e `destination` são: {{ano}}, {{numeroMes}}, {{nomeMes}}, {{dia}}, {{hora}}, {{minuto}}, {{segundo}}, {{nomeArquivo}}.

### Sufixos [REGEX]

| Sufixo | Descrição                                                          | Exemplo de Padrão de Nome                        | Comportamento Previsto                                     |
|--------|--------------------------------------------------------------------|---------------------------------------------------|-----------------------------------------------------------|
| [r]    | Indica que o padrão de nome de arquivo usa uma expressão regular. | "[r]video_[0-9]+\\.mp4"                           | Correspondência com arquivos que atendam ao padrão regex.   |
| [s]    | Indica que o padrão de nome de arquivo é sensível a maiúsculas e minúsculas. | "Video_[0-9]+\\.mp4"                   | Correspondência apenas com arquivos cujos nomes sejam exatamente iguais, incluindo diferenciação entre maiúsculas e minúsculas.   |
| [i]    | Indica que o padrão de nome de arquivo é insensível a maiúsculas e minúsculas. | "[i]video_[0-9]+\\.mp4"                        | Correspondência com arquivos que atendam ao padrão regex, ignorando a diferenciação entre maiúsculas e minúsculas. |
| [w]    | Indica que o padrão de nome de arquivo permite correspondência em palavras completas. | "[w]video\\.mp4"                          | Correspondência apenas com arquivos cujos nomes sejam palavras completas, não apenas em parte do nome. |

Exemplos:

1. Arquivo com sufixo [r]:
   - Padrão de Nome: "[r]video_[0-9]+\.mp4"
   
2. Arquivo com sufixo [s]:
   - Padrão de Nome: "Video_[0-9]+\.mp4"

3. Arquivo com sufixo [i]:
   - Padrão de Nome: "[i]video_[0-9]+\.mp4" 
   
4. Arquivo com sufixo [w]:
   - Padrão de Nome: "[w]video\.mp4"

Certifique-se de fornecer os caminhos corretos para as pastas e arquivos no arquivo config.json antes de executar o script.

### Exemplos config.json:

#### Exemplo 1:
```
{
  "rootPath": "C:\\caminho\\para\\pasta\\raiz\\",
  "dayOfExecution": ["seg", "qua", "sex"],
  "subFolders": [
    "Subpasta1",
    "Subpasta2",
    "Subpasta3",
    "Subpasta4"
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
    },
    {
      "source": "C:\\caminho\\para\\arquivos\\PASTA {{ano}}\\{{numeroMes}}_{{nomeMes}}\\",
      "fileName": "[r]{{dia}}.*.mp4",
      "destination": "Subpasta4\\"
    }
  ],
  "ytDownloads" : [
    {
      "videoTitle" : "Video Download | 01 Janeiro 2001",
      "destination": "Subpasta4\\",
      "match": true
    },
    {
      "videoTitle" : "Video Download",
      "destination": "Subpasta4\\",
      "match": false
    }
  ]
}

```

#### Exemplo 2:
```
{
  "rootPath": "C:\\Users\\usuario\\Desktop\\",
  "dayOfExecution": ["dom", "qua", "sab"],
  "subFolders": ["A", "B", "C"],
  "filesCopy": [
    {
      "source": "C:\\Caminho\\Origem\\{{ano}}\\{{nomeMes}}\\",
      "fileName": "[r]{{dia}}_[A-Za-z]+\\.mp4",
      "destination": "{{numeroMes}}_{{nomeMes}}\\"
    },
    {
      "source": "C:\\Caminho\\Origem\\subpasta\\",
      "fileName": "[r][s]file[0-9]+\\.txt",
      "destination": "{{numeroMes}}_{{nomeMes}}\\"
    },
    {
      "source": "C:\\Caminho\\Origem\\{{ano}}\\subpasta\\",
      "fileName": "[r][i]file_{{nomeMes}}_[0-9]+\\.txt",
      "destination": "{{numeroMes}}_{{nomeMes}}\\"
    },
    {
      "source": "C:\\Caminho\\Origem\\{{ano}}\\{{nomeMes}}\\",
      "fileName": "[r][w]relatorio\\.xlsx",
      "destination": "{{numeroMes}}_{{nomeMes}}\\"
    }
  ],
  "ytDownloads" : [
    {
      "videoTitle" : "Video Download | {{dia}} {{nomeMes}} {{ano}}",
      "destination": "Subpasta4\\",
      "match": true
    },
    {
      "videoTitle" : "Video Download",
      "destination": "Subpasta4\\",
      "match": false
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
pyinstaller  --add-data "config.json;." --onedir main.py
```
* Ou compile com o comando abaixo:
```
python -m PyInstaller --hidden-import pytube.Search  --add-data "config.json;." --onedir main.py
```
__Isso criará um executável na pasta dist com o nome nome_do_script.exe (no Windows) ou nome_do_script (no Linux/macOS)..__

__Agora você pode executar o arquivo main.exe (no Windows) ou main (no Linux/macOS), e o programa utilizará as configurações do arquivo config.json para criar a estrutura de pastas e copiar os arquivos conforme especificado.__

__Aqui note que também usei o "--add-data" para especificar um arquivo que necessário para execução do meu script, como isso complilador ira copiar o arquivo.__

> <font color="grey">__Obs.: Após compilar deve-se copiar o arquivo</font> <font color="red">__config.json__</font> <font color="grey"> para o diretório raiz do executável.__
