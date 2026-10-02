import os
import datetime
import random

def falar(texto):
    """Faz o Windows falar usando o PowerShell nativo"""
    print(f"🤖 Siri: {texto}\n")
    # Comando nativo do Windows para sintetizar voz
    comando_voz = f'PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{texto}\')"'
    os.system(comando_voz)

os.system('cls' if os.name == 'nt' else 'clear')
falar("Olá! Sou sua assistente. Digite o que você precisa ou sair para encerrar.")

while True:
    comando = input("👤 Você: ").strip().lower()

    if not comando:
        continue

    match comando:
        case _ if 'hora' in comando:
            hora_atual = datetime.datetime.now().strftime('%H:%M')
            falar(f"Agora são {hora_atual}.")

        case _ if 'data' in comando or 'dia' in comando:
            hoje = datetime.datetime.now().strftime('%d/%m/%Y')
            falar(f"Hoje é dia {hoje}.")

        case _ if 'seu nome' in comando:
            falar("Eu sou sua assistente em Python!")

        case _ if 'sair' in comando or 'tchau' in comando:
            falar("Até logo!")
            break

        case _:
            falar("Desculpe, não entendi o comando.")