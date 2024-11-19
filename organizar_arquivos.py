import os

def mkdir_path(file_extension, file_extension_list):
    ''' Cria diretórios para organização dos arquivos '''
    if file_extension in file_extension_list:
        folder_name = file_extension_list[file_extension]
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

def move_file(file_name, folder_name):
    ''' Move o arquivo para a pasta especificada '''
    caminho_origem = os.path.join(os.getcwd(), file_name)
    caminho_destino = os.path.join(os.getcwd(), folder_name, file_name)
    os.rename(caminho_origem, caminho_destino)

cwd = os.getcwd()
list_file = os.listdir(cwd)
file_extension_list = {
    '.txt': 'texto',
    '.pdf': 'documento',
    '.docx': 'documento',
    '.jpg': 'imagem',
    '.jpeg': 'imagem',
    '.png': 'imagem',
    '.mp3': 'musica',
    '.mp4': 'vídeo',
    '.csv': 'csv'
}

for file in list_file:
    file_name, file_extension = os.path.splitext(file)
    
    if file_extension in file_extension_list:
        mkdir_path(file_extension, file_extension_list)
        move_file(file, file_extension_list[file_extension])
    elif file_extension == '.py':
        print('Esse arquivo é um script Python (.py)')
    elif file_extension == '':
        print('Este é um diretório ou arquivo sem extensão')
    else:
        print(f"Tipo de arquivo desconhecido: {file_extension}")