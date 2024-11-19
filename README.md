# Organizador de Arquivos

Este projeto tem como objetivo organizar arquivos em um diretório, movendo-os para pastas específicas de acordo com suas extensões. Além disso, ele também pode mover arquivos de volta para o diretório raiz a partir de pastas organizadas.

## Funcionalidades

- **Organizar Arquivos**: Cria pastas baseadas na extensão dos arquivos e move os arquivos para essas pastas.
- **Mover Arquivos de Volta para a Raiz**: Permite mover arquivos de volta para o diretório raiz, removendo as pastas vazias após a operação.
  
### Estrutura de Pastas:

Os arquivos são organizados em pastas com os seguintes nomes de acordo com suas extensões:

- **Texto**: `.txt`
- **Documentos**: `.pdf`, `.docx`
- **Imagens**: `.jpg`, `.png`
- **Músicas**: `.mp3`
- **Vídeos**: `.mp4`
- **CSV**: `.csv`

## Requisitos

- Python 3.x
- Nenhuma biblioteca externa é necessária. O código utiliza apenas as bibliotecas padrão do Python (`os`).

## Como Funciona

### 1. Script (`organizar_arquivos.py`):
- Verifica as extensões dos arquivos no diretório atual.
- Cria pastas correspondentes e move os arquivos para elas.
  
### 2. Script (`mover_de_volta.py`):
- Verifica as pastas no diretório atual.
- Move os arquivos de volta para o diretório raiz e remove as pastas vazias.

## Como Usar

### 1. Organizar Arquivos:

- Execute o script para organizar os arquivos do diretório atual em pastas baseadas nas suas extensões.
  
```bash
python organizar_arquivos.py
```

### 2. Mover Arquivos de Volta para a Raiz

- Após mover os arquivos para suas respectivas pastas, você pode mover os arquivos de volta para o diretório raiz com o seguinte comando:

```bash
python mover_de_volta.py
```

## Exemplo de Uso
- Arquivos Desorganizados:

![Captura de tela 2024-11-19 090741](https://github.com/user-attachments/assets/6ad19e2c-bb2e-4a88-9dcb-05727fb08491)

- Arquivos Organizados:

![Captura de tela 2024-11-19 090628](https://github.com/user-attachments/assets/2cc7f645-4e38-404b-aae4-98f463e4da78)
