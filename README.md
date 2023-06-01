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

| Campo            | Descrição                                          | Tipo     | Exemplo                                                      |
|------------------|----------------------------------------------------|----------|--------------------------------------------------------------|
| rootPath         | Caminho raiz onde as pastas serão criadas           | String   | "C:\\Users\\usuario\\Desktop\\"                             |
| dayOfExecution   | Dias da semana em que o script pode ser executado   | Lista    | ["dom", "qua", "sab"]                                       |
| subFolders       | Lista de subpastas a serem criadas                  | Lista    | ["A", "B", "C"]                                             |
| filesCopy        | Lista de arquivos a serem copiados                  | Lista    | Veja a tabela de arquivos a serem copiados abaixo            |

### Tabela de arquivos a serem copiados:

| Campo       | Descrição                                  | Tipo   | Exemplo com Placeholders                                          | Exemplo sem Placeholders                           |
|-------------|--------------------------------------------|--------|------------------------------------------------------------------|---------------------------------------------------|
| source      | Caminho da pasta de origem dos arquivos    | String | "C:\\Caminho\\Origem\\{{ano}}\\{{nomeMes}}\\"                     | "C:\\Caminho\\Origem\\subpasta\\"                  |
| fileName    | Padrão de nome do arquivo usando regex     | String | "{{dia}}_[A-Za-z]+\\.mp4"                                        | "file[0-9]+\\.txt"                                |
| destination | Subpasta de destino para o arquivo         | String | "{{numeroMes}}_{{nomeMes}}\\"                                     | "A\\"                                             |

#### Exemplos:
1. Arquivo com placeholders:
   - source: "C:\\Caminho\\Origem\\{{ano}}\\{{nomeMes}}\\"
   - fileName: "{{dia}}_[A-Za-z]+\\.mp4"
   - destination: "{{numeroMes}}_{{nomeMes}}\\"

2. Arquivo sem placeholders:
   - source: "C:\\Caminho\\Origem\\subpasta\\"
   - fileName: "file[0-9]+\\.txt"
   - destination: "A\\"

3. Arquivo com placeholders misturados:
   - source: "C:\\Caminho\\Origem\\{{ano}}\\subpasta\\"
   - fileName: "file_{{nomeMes}}_[0-9]+\\.txt"
   - destination: "{{numeroMes}}_{{nomeMes}}\\"

- O campo `fileName` permite o uso de expressões regulares para encontrar arquivos correspondentes.
- Os placeholders disponíveis para uso em `source`, `fileName` e `destination` são: {{ano}}, {{numeroMes}}, {{nomeMes}}, {{dia}}, {{hora}}, {{minuto}}, {{segundo}}, {{nomeArquivo}}.


Certifique-se de fornecer os caminhos corretos para as pastas e arquivos no arquivo config.json antes de executar o script.

#### Exemplo config.json:
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
      "fileName": "{{dia}}.*.mp4",
      "destination": "Subpasta4\\"
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
