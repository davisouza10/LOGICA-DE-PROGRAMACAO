import os
import random
import time

os.system('cls' if os.name == 'nt' else 'clear')

print('=== SIMULADOR: MÁQUINA VS MÁQUINA ===\n')

time_a = input('Nome do Time 1: ').strip() or 'Real Madrid'
time_b = input('Nome do Time 2: ').strip() or 'Barcelona'

gols_a = 0
gols_b = 0

cantos = {'1': 'Esquerda', '2': 'Meio', '3': 'Direita'}
eventos = ['gol', 'chute_fora', 'defesa', 'falta', 'nada']

print(f'\n⚽ ROLA A BOLA PARA {time_a.upper()} X {time_b.upper()}!\n')
time.sleep(1)

# ==================================================
# 1. TEMPO NORMAL (90 MINUTOS)
# ==================================================
for minuto in range(10, 91, 10):
    time.sleep(1)
    
    atacante = random.choice([time_a, time_b])
    defensor = time_b if atacante == time_a else time_a
    lance = random.choice(eventos)

    match lance:
        case 'gol':
            if atacante == time_a:
                gols_a += 1
            else:
                gols_b += 1
            print(f'⏱️ {minuto}\': GOOOOOL DO {atacante.upper()}! ⚽ ({time_a} {gols_a} x {gols_b} {time_b})')
        case 'chute_fora':
            print(f'⏱️ {minuto}\': {atacante} chutou forte pra fora!')
        case 'defesa':
            print(f'⏱️ {minuto}\': Defesaça do goleiro do {defensor}!')
        case 'falta':
            print(f'⏱️ {minuto}\': Falta no meio de campo...')
        case 'nada':
            print(f'⏱️ {minuto}\': Jogo estudado no meio de campo...')

print('\n====================================')
print(f'🏁 FIM DOS 90 MINUTOS!')
print(f'PLACAR TEMPO NORMAL: {time_a} {gols_a} X {gols_b} {time_b}')
print('====================================\n')
time.sleep(2)

# ==================================================
# 2. DISPUTA DE PÊNALTIS (EM CASO DE EMPATE)
# ==================================================
if gols_a == gols_b:
    print('⚠️ EMPATE NO TEMPO REGULAMENTAR! A DECISÃO VAI PARA OS PÊNALTIS! 🥅\n')
    time.sleep(1.5)
    
    penaltis_a = 0
    penaltis_b = 0

    # 5 Cobranças Iniciais
    for rodada in range(1, 6):
        cobrancas_restantes_a = 5 - rodada + 1
        cobrancas_restantes_b = 5 - rodada + 1

        print(f'--- {rodada}ª RODADA DE PÊNALTIS ---')
        
        # Cobrança Time A
        chute_a = random.choice(list(cantos.keys()))
        goleiro_b = random.choice(list(cantos.keys()))
        print(f'🏃 {time_a} vai para a cobrança...')
        time.sleep(1)
        if chute_a == goleiro_b:
            print(f'❌ DEFENDEU O GOLEIRO DO {time_b}!\n')
        else:
            penaltis_a += 1
            print(f'⚽ GOOOOOL DO {time_a}!\n')
        time.sleep(1)

        # Checagem se Time A já é inalcançável antes do Time B bater
        cobrancas_restantes_a -= 1
        if penaltis_a > penaltis_b + cobrancas_restantes_b or penaltis_b > penaltis_a + cobrancas_restantes_a:
            print('🏆 Fim das cobranças! Placar inalcançável!\n')
            break

        # Cobrança Time B
        chute_b = random.choice(list(cantos.keys()))
        goleiro_a = random.choice(list(cantos.keys()))
        print(f'🏃 {time_b} vai para a cobrança...')
        time.sleep(1)
        if chute_b == goleiro_a:
            print(f'❌ DEFENDEU O GOLEIRO DO {time_a}!\n')
        else:
            penaltis_b += 1
            print(f'⚽ GOOOOOL DO {time_b}!\n')
        time.sleep(1)

        cobrancas_restantes_b -= 1
        if penaltis_a > penaltis_b + cobrancas_restantes_b or penaltis_b > penaltis_a + cobrancas_restantes_a:
            print('🏆 Fim das cobranças! Placar inalcançável!\n')
            break

    print(f'PLACAR DOS PÊNALTIS (5 RODADAS): {time_a} {penaltis_a} X {penaltis_b} {time_b}')

    # Morte Súbita se persistir o empate
    if penaltis_a == penaltis_b:
        print('\n⚠️ CONTINUA EMPATADO! INICIANDO MORTE SÚBITA...\n')
        rodada_extra = 1
        
        while True:
            print(f'--- MORTE SÚBITA ({rodada_extra}ª RODADA) ---')
            
            # Time A
            chute_a = random.choice(list(cantos.keys()))
            goleiro_b = random.choice(list(cantos.keys()))
            gol_a_rodada = chute_a != goleiro_b
            if gol_a_rodada:
                penaltis_a += 1
                print(f'⚽ GOL DO {time_a}!')
            else:
                print(f'❌ {time_a} PERDEU!')
            time.sleep(1)

            # Time B
            chute_b = random.choice(list(cantos.keys()))
            goleiro_a = random.choice(list(cantos.keys()))
            gol_b_rodada = chute_b != goleiro_a
            if gol_b_rodada:
                penaltis_b += 1
                print(f'⚽ GOL DO {time_b}!\n')
            else:
                print(f'❌ {time_b} PERDEU!\n')
            time.sleep(1)

            # Na morte súbita, o jogo só termina se um fizer gol e o outro não na mesma rodada
            if gol_a_rodada != gol_b_rodada:
                break

            rodada_extra += 1

    print('====================================')
    print(f'RESULTADO FINAL NOS PÊNALTIS: {time_a} {penaltis_a} X {penaltis_b} {time_b}')
    print('====================================')

    if penaltis_a > penaltis_b:
        print(f'🏆 {time_a.upper()} VENCEU NOS PÊNALTIS!')
    else:
        print(f'🏆 {time_b.upper()} VENCEU NOS PÊNALTIS!')

else:
    # Vitória no tempo normal
    if gols_a > gols_b:
        print(f'🏆 {time_a.upper()} VENCEU NO TEMPO REGULAMENTAR!')
    else:
        print(f'🏆 {time_b.upper()} VENCEU NO TEMPO REGULAMENTAR!')