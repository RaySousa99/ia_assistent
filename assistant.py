import os
import webbrowser
import subprocess

from utils import speak

def criar_pasta(local_base, nome_pasta):
    caminho = os.path.join(local_base, nome_pasta)
    try:
        os.makedirs(caminho, exist_ok=True)
        speak(f"Pasta '{nome_pasta}' criada em {local_base}")
    except Exception as e:
        speak(f"Erro ao criar pasta: {e}")

def criar_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            f.write("# Arquivo criado pelo assistente\n")
        speak(f"Arquivo {caminho_arquivo} criado com sucesso")
    except Exception as e:
        speak(f"Erro ao criar arquivo: {e}")

def abrir_navegador(url="https://www.google.com.br"):
    try:
        webbrowser.open(url)
        speak(f"Abrindo navegador em {url}")
    except Exception as e:
        speak(f"Erro ao abrir navegador: {e}")

def abrir_youtube():
    abrir_navegador("https://www.youtube.com")

def abrir_pasta(caminho):
    try:
        if os.path.exists(caminho):
            os.startfile(caminho)
            speak(f"Abrindo pasta {caminho}")
        else:
            speak("Pasta não encontrada")
    except Exception as e:
        speak(f"Erro ao abrir pasta: {e}")

def esvaziar_lixeira():
    try:
        import winshell  # pip install winshell
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
        speak("Lixeira esvaziada com sucesso")
    except ImportError:
        speak("Módulo winshell não instalado. Instale com: pip install winshell")
    except Exception as e:
        speak(f"Erro ao esvaziar lixeira: {e}")

def abrir_programa(nome_programa):
    try:
        subprocess.Popen(nome_programa)
        speak(f"Abrindo {nome_programa}")
    except Exception as e:
        speak(f"Erro ao abrir {nome_programa}: {e}")

def pesquisar_google(termo):
    url = f"https://www.google.com/search?q={termo.replace(' ', '+')}"
    abrir_navegador(url)
