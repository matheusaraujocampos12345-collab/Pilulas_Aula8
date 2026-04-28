def processar_consultas(registro):
    tempos = {}
    cont = {}
    status = {}
    for reg in registro:
        p = reg['paciente']
        if p not in tempos:
            tempos[p]= 0
            cont[p]= 0
        tempos[p] += reg['tempo']
        cont[p] += 1
        
    for p in tempos:
        t = tempos[p]
        if t < 2:
            status[p] = 'Leve'
        elif t < 5: 
            status[p] = 'Moderado'
        else:
            status[p] = 'Critico'
    
    for p in tempos:
        print(f'{p} | Tempo: {tempos[p]} | Qtd: {cont[p]} | Status: {status[p]}')        

def main():
    registros =[
        {'pacientes': 'Ana', 'tempo' : 1},
        {'pacientes': 'Carla', 'tempo' : 2},
        {'pacientes': 'Duarda', 'tempo' : 4}
    ]
    processar_consultas(registros)