print('=== Gestor de Tempo ===')

tempo_total = 0
dias_semana = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
gastos = []

for i in range(7):
    horas = float(input(f'Digite as horas gastas na {dias_semana[i]}: '))
    gasto = int(horas * 60)
    gastos.append(gasto)
    tempo_total += gasto
    print(f'Dia {i+1}: você gastou {gasto} minutos.\n')
    
media = tempo_total / 7

print('\n=== Relatório da Semana ===')
for i in range(7):
    print(f'Dia {i+1} ({dias_semana[i]}): {gastos[i]} minutos')
    
print(f'\nTempo total gasto: {tempo_total} minutos ({tempo_total//60}h {tempo_total%60} min)')
print(f'Média diária: {media:.1f} minutos ({media/60:.2f}h por dia)')

if media > 240:
    print('ALERTA: Você está gastando MUITO TEMPO! Mais de 4h por dia em média.')
elif media > 180:
    print('Sua média está razoável, mas já é bastante tempo, entre 3h e 4h por dia.')   
elif media > 60:
    print('Bom controle! Vocè fica entre 1h e 3h por dia em média.')
else:
    print('Excelente disciplina! Você está passando menos de 1h por dia.')     