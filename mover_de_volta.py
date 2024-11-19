import os

def move_file_back_to_root(file_name, folder_name):
    ''' Move o arquivo de volta para a raiz do diretório '''
    caminho_origem = os.path.join(os.getcwd(), folder_name, file_name)
    caminho_destino = os.path.join(os.getcwd(), file_name)
    os.rename(caminho_origem, caminho_destino)

pastas = ['texto', 'documento', 'imagem', 'musica', 'vídeo', 'csv']  # Adicione ou remova pastas conforme necessário

for folder_name in pastas:
    if os.path.exists(folder_name): 
        for file in os.listdir(folder_name): 
            move_file_back_to_root(file, folder_name)
        os.rmdir(folder_name)