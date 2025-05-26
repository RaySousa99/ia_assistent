import os
from utils import speak, confirmar
import assistant

COMANDOS = [
    "criar pasta",
    "criar arquivo",
    "abrir navegador",
    "abrir youtube / yt",
    "abrir pasta",
    "esvaziar lixeira",
    "abrir (programa/arquivo/jogo)",
    "pesquisa (termo)",
    "ajuda",
    "sair"
]

def mostrar_ajuda():
    speak("Aqui estão os comandos disponíveis:")
    for cmd in COMANDOS:
        print(f"- {cmd}")
    speak("Você pode digitar o comando começando com 'cire' ou direto o comando.")

def main():
    speak("Assistente Cire iniciada. Digite o comando quando ouvir 'Cire'.")
    while True:
        comando = input("Você (digite o comando): ").lower().strip()
        if comando == "":
            continue
        
        if comando.startswith("cire"):
            comando = comando[5:].strip()  # Remove "cire "

        if "sair" in comando:
            speak("Encerrando assistente. Até logo!")
            break

        elif "ajuda" in comando:
            mostrar_ajuda()

        elif "criar pasta" in comando:
            speak("Onde deseja criar a pasta? (Digite o caminho completo ou caminho relativo)")
            local_base = input("Local base: ").strip()
            speak("Qual o nome da pasta que deseja criar?")
            nome_pasta = input("Nome da pasta: ").strip()
            assistant.criar_pasta(local_base, nome_pasta)

        elif "criar arquivo" in comando:
            speak("Quer criar o arquivo em uma pasta já criada? Sim ou não?")
            if confirmar():
                pasta = input("Caminho da pasta: ").strip()
                nome_arquivo = input("Nome do arquivo (sem extensão): ").strip()
                caminho_arquivo = os.path.join(pasta, f"{nome_arquivo}.py")
                assistant.criar_arquivo(caminho_arquivo)
            else:
                caminho_arquivo = input("Digite o caminho completo para criar o arquivo (incluindo nome e extensão .py): ").strip()
                if not caminho_arquivo.endswith('.py'):
                    caminho_arquivo += '.py'
                assistant.criar_arquivo(caminho_arquivo)

        elif "abrir navegador" in comando:
            assistant.abrir_navegador()

        elif "abrir youtube" in comando or "abrir yt" in comando:
            assistant.abrir_youtube()

        elif "abrir pasta" in comando:
            caminho = input("Qual o caminho da pasta que deseja abrir? ").strip()
            assistant.abrir_pasta(caminho)

        elif "esvaziar lixeira" in comando:
            assistant.esvaziar_lixeira()

        elif comando.startswith("abrir "):
            nome_programa = comando.replace("abrir", "").strip()
            assistant.abrir_programa(nome_programa)

        elif comando.startswith("pesquisa "):
            termo = comando.replace("pesquisa", "").strip()
            assistant.pesquisar_google(termo)

        else:
            speak("Comando não reconhecido. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
