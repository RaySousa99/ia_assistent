import pyttsx3

# Inicializa motor de voz com voz feminina (ajuste automático)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    if 'female' in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

def speak(text):
    print(f"Cire: {text}")  # Mostra no terminal também
    engine.say(text)
    engine.runAndWait()

def confirmar():
    while True:
        resposta = input("Confirma? (sim/não): ").strip().lower()
        if resposta in ['sim', 's', 'yes', 'y']:
            return True
        elif resposta in ['não', 'nao', 'n', 'no']:
            return False
        else:
            speak("Não entendi. Por favor, digite sim ou não.")
