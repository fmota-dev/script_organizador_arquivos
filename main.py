import os
import shutil
import tkinter as tk
from tkinter import filedialog

# Função para organizar os arquivos


def organizar_arquivos(diretorio):
    # Dicionário com tipos de arquivos e suas extensões
    tipos_de_arquivos = {
        "Documentos": [
            ".pdf",
            ".txt",
            ".docx",
            ".xlxs",
            ".xls",
            ".pptx",
            ".odt",
            ".rtf",
            ".epub",
            ".log",
            ".csv",
        ],
        "Imagens": [
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".bmp",
            ".tiff",
            ".svg",
            ".webp",
            ".ico",
        ],
        "Vídeos": [
            ".mp4",
            ".mkv",
            ".avi",
            ".mov",
            ".wmv",
            ".flv",
            ".webm",
            ".mpg",
            ".mpeg",
        ],
        "Áudios": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma"],
        "Arquivos compactados": [
            ".zip",
            ".rar",
            ".tar",
            ".gz",
            ".7z",
            ".tar.gz",
            ".xz",
        ],
        "Códigos": [
            ".py",
            ".java",
            ".cpp",
            ".js",
            ".html",
            ".css",
            ".php",
            ".ts",
            ".rb",
        ],
        "Outros": [],
    }
    
    # Criar as pastas de destino, se não existirem
    for pasta in tipos_de_arquivos.keys():
        pasta_destino = os.path.join(diretorio, pasta)
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

    # Organizar os arquivos
    for arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, arquivo)

        if os.path.isfile(caminho_arquivo):  # Verifica se é um arquivo
            # Identifica a extensão do arquivo
            extensao = os.path.splitext(arquivo)[1].lower()

            # Encontra o tipo do arquivo de acordo com sua extensão
            pasta_destino = "Outros"  # Padrão
            for tipo, extensoes in tipos_de_arquivos.items():
                if extensao in extensoes:
                    pasta_destino = tipo
                    break

            # Mover o arquivo para a pasta correspondente
            caminho_destino = os.path.join(diretorio, pasta_destino, arquivo)
            shutil.move(caminho_arquivo, caminho_destino)
            print(f'Arquivo "{arquivo}" movido para a pasta "{pasta_destino}".')


# Função para abrir o seletor de pastas


def selecionar_pasta():
    root = tk.Tk()
    root.wm_withdraw() 
    caminho_pasta = filedialog.askdirectory(title="Escolha a pasta a ser organizada")

    if caminho_pasta:
        organizar_arquivos(caminho_pasta)
        print(f"Arquivos organizados na pasta: {caminho_pasta}")
    else:
        print("Nenhuma pasta foi escolhida.")


# Chamar a função para selecionar a pasta
selecionar_pasta()
