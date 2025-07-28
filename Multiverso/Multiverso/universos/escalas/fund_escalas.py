frequency = 440.0    #(La4)

def crear_diccionario_notas(octava_inicio, octava_fin):
    notas = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    diccionario = {}
    
    for octave in range(octava_inicio, octava_fin + 1):
        for indice, nota in enumerate(notas):
            nombre_nota = f"{nota}{octave}"
            numero_midi = 12 + octave * 12 + indice
            frecuencia = 440 * (2 ** ((numero_midi - 69) / 12))
            
            diccionario[nombre_nota] = float(round(frecuencia, 2))  
    inverso = {float(freq): nota for nota, freq in diccionario.items()} 
    return diccionario, inverso

def nota_mas_cercana(frecuencia, inverso):
    frecuencia = float(frecuencia) 
    return min(inverso.keys(), key=lambda x: abs(x - frecuencia))

def get_intervals_mode(mode_index):
    jonic_intervals = [2, 2, 1, 2, 2, 2, 1]  # Modo Jónico 
    return jonic_intervals[mode_index:] + jonic_intervals[:mode_index]
