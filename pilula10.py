def ranking(pacientes):
    ranking_paciente = []
    for paciente in pacientes:
        pontos = 0
        if paciente['gravidade'] >= 4:
            pontos += 3
        elif paciente['gravidade'] >= 2:
            pontos += 2 
        
        if paciente['idade'] >= 60:
            pontos += 2
            
        ranking_paciente.append({'nome' : paciente['nome'],
                        'pontos': pontos })
    #bubble sort
    for i in range(len(ranking_paciente)):
        for j in range(i+1, len(ranking_paciente)):
            if ranking_paciente[i]['pontos'] < ranking_paciente[j]['pontos']:
                ranking_paciente[i], ranking_paciente[j] = ranking_paciente[j],ranking_paciente[i]
          
        #print
    for item in range(len(ranking_paciente)):
        print(f'{ranking_paciente[item]['nome']}, {ranking_paciente[item]['pontos']}')      

def main():
    pacientes = [
        {'nome': 'Ana', 'idade': 70, 'gravidade' : 3},
        {'nome': 'Roger', 'idade': 40, 'gravidade' : 2},
        {'nome': 'Claudia', 'idade': 15, 'gravidade':4},
    ]
    ranking(pacientes)
    
main()