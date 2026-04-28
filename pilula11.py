def especialidadeTop(consultas):
    cont = {}
    for c in consultas:
        esp = c['especialidade']
        if esp not in cont:
            cont[esp] = 0 
    maior_esp = ''
    max_valor = -1
    for esp in cont:
        if cont[esp] > max_valor:
            max_valor = cont[esp]
            maior_esp = esp
    return maior_esp    

def main():
    consultar = [
        {'paciente': 'Ana', 'especialidade': 'Cardiologia'},
        {'paciente': 'Bianca', 'especialidade': 'Cardiologia'},
        {'paciente': 'Bruna', 'especialidade': 'Cardiologia'},
        {'paciente': 'Roger', 'especialidade': 'Cardiologia'}
    ]
    print(especialidadeTop(consultar))
main()
