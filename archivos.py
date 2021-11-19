from csv import *
from equipo import *
from pokemon import *

def guardar_equipos(equipos):
    with open('equipos_guardados.csv', 'w') as salida:
        for equipo in equipos:
            string_pokemones = f'{equipo.nombre};'
            for pokemon in equipo.pokemones:
                string_pokemones += f"{pokemon.numero}-{','.join(pokemon.movimientos)};"

            string_pokemones = string_pokemones[:-1]
            salida.write(f'{string_pokemones}\n')

def traer_equipos():
        equipos = []
        pokemones_id, _ = traer_pokemones_archivo()
             
        with open('equipos_guardados.csv') as entrada:
            datos = reader(entrada, delimiter=';')
            for fila in datos:
                nombre = fila[0]
                equipo = Equipo(nombre)
                pokemones = fila[1:]
                for pokemon_datos in pokemones:
                    id_pokemon, movimientos = pokemon_datos.split('-')
                    id_pokemon = int(id_pokemon)
                    nombre = pokemones_id[id_pokemon]['nombre'] 
                    pokemon = Pokemon(id_pokemon, nombre)
                    pokemon.movimientos = movimientos.split(',')
                    equipo.pokemones.append(pokemon)
                 
                equipos.append(equipo)
        
        return equipos
 
 
def traer_movimientos():
    '''
    Devuelve un diccionario que tiene como clave al nombre del pokemon 
    y como valor una lista con sus movimientos 
    '''
    dicc_movimientos = {}
    with open('movimientos.csv') as entrada:
        datos = DictReader(entrada, delimiter=';')

        for fila in datos:
            dicc_movimientos[fila['pokemon']] = fila['movimientos'].split(',')

    return dicc_movimientos


def traer_pokemones_archivo():
    '''
    Devuelve:
     Un diccionario que tiene; clave: 'id de pokemon', valor: diccionario de la forma "{ 'estadistica' : 'valor' }"
     y un diccionario de la forma "{ 'pokemon' : 'id_pokemon' }"
    '''
    dicc_pokemones_id = {}
    dicc_pokemones_nombre = {}
    with open('pokemons.csv') as entrada:
        datos = DictReader(entrada, delimiter = ';')

        for fila in datos:
            numero = int(fila['numero'])
            dicc_pokemones_id[numero] = {}
            dicc_pokemones_id[numero]['nombre'] = fila['nombre'] 
            dicc_pokemones_id[numero]['imagen'] = fila['imagen']
            dicc_pokemones_id[numero]['tipos'] = fila['tipos']
            dicc_pokemones_id[numero]['hp'] = fila['hp']
            dicc_pokemones_id[numero]['atk'] = fila['atk']
            dicc_pokemones_id[numero]['def'] = fila['def']
            dicc_pokemones_id[numero]['spa'] = fila['spa']
            dicc_pokemones_id[numero]['spd'] = fila['spd']
            dicc_pokemones_id[numero]['spe'] = fila['spe']

            dicc_pokemones_nombre[fila['nombre']] = numero

    return dicc_pokemones_id, dicc_pokemones_nombre
    