from lista_lista import Lista
from random import randint


# Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas.
# Y además la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo.
# Se pide resolver
# las siguientes actividades utilizando lista de lista implementando las funciones necesarias:







class Entrenador():

    def __init__(self, nombre, ct_ganados, cb_perdidas, cb_ganadas):
        self.nombre = nombre
        self.ct_ganados = ct_ganados
        self.cb_perdidas = cb_perdidas
        self.cb_ganadas = cb_ganadas

    def __str__(self):
        return f'{self.nombre} --> ctg:{self.ct_ganados}-cbg:{self.cb_ganadas}-cbp:{self.cb_perdidas}'

class Pokemon():

    def __init__(self, nombre, tipo, nivel=1, subtipo=None):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f'{self.nombre}-{self.nivel}-{self.tipo}-{self.subtipo}'


e1 = Entrenador('Juan', randint(1, 10), 2, 8)
e2 = Entrenador('Maria', randint(1, 10), 2, 7)
e3 = Entrenador('Ana', randint(1, 10), 38 , 7)

entrenadores = [e1, e2, e3]

lista_entrenadores = Lista()

p1 = Pokemon('pikachu', 'electrico', randint(1, 20))
p2 = Pokemon('jolteon', 'electrico', randint(1, 20))
p3 = Pokemon('vaporeon', 'agua', randint(1, 20), 'volador')
p4 = Pokemon('flareon', 'fuego', randint(1, 20), 'planta')
p5 = Pokemon('leafeon', 'planta', randint(1, 20))
p6 = Pokemon('pikachu', 'electrico', randint(1, 20))
p7 = Pokemon('tyrantrum', 'electrico', randint(1, 20))
p8 = Pokemon('terrakion', 'electrico', randint(1, 20))
p9 = Pokemon('wingull', 'electrico', randint(1, 20))
pokemons = [p1, p2, p3, p4, p5, p6, p7, p8, p9]

#! lista principal
for entrenador in entrenadores:
    lista_entrenadores.insert(entrenador, 'nombre')

#! lista secundaria
for pokemon in pokemons:
    numero_entrenador = randint(0, lista_entrenadores.size()-1)
    entrenador = lista_entrenadores.get_element_by_index(numero_entrenador)
    entrenador[1].insert(pokemon, 'nombre')


lista_entrenadores.barrido_entrenadores()
print()

# a. obtener la cantidad de Pokémons de un determinado entrenador;
def cantidadPokemons(lista_entrenadores, quien):
    esta = lista_entrenadores.search(quien, 'nombre')    
    if esta != None:
        value = lista_entrenadores.get_element_by_index(esta)
        entrenado, sublista = value[0], value[1]
        print(f"{entrenado.nombre} tiene {sublista.size()} pokemons")
    else:
        print('el entrenador solicitado no se a encontrado')

# b. listar los entrenadores que hayan ganado más de tres torneos;
def gano_mas_tres(lista_entrenadores):
    for i in range(0, lista_entrenadores.size()):
        value = lista_entrenadores.get_element_by_index(i)
        if value[0].ct_ganados > 3:
            print(value[0]) 

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
def mayorTorneosNivel(lista_entrenadores):
    mayor_cantidad = lista_entrenadores.get_element_by_index(0)[0].ct_ganados
    pos_mayor = 0

    for pos in range(1, lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(pos)[0]
        if entrenador.ct_ganados > mayor_cantidad:
            pos_mayor = pos
            mayor_cantidad = entrenador.ct_ganados

    valor = lista_entrenadores.get_element_by_index(pos_mayor)
    entrenador, sublista = valor[0], valor[1]

    if sublista.size() > 0:
        pokemon_mayor = sublista.get_element_by_index(0)
        for pos in range(1, sublista.size()):
            pokemon = sublista.get_element_by_index(pos)
            if pokemon.nivel > pokemon_mayor.nivel:
                pokemon_mayor = pokemon
    print(f'El pokemon de mayor nivel del entrenador {entrenador.nombre} es {pokemon_mayor.nombre} {pokemon_mayor.nivel} ')
# d. mostrar todos los datos de un entrenador y sus Pokémos; 
def unEntrenador(lista_entrenadores, a):
    esto = lista_entrenadores.search(a, 'nombre')    
    if esto != None:
        value = lista_entrenadores.get_element_by_index(esto)
        entrenado, sublista = value[0], value[1]
        print(f"{entrenado.nombre} tiene estos pokemones")
        sublista.barrido()
    else:
        print('el entrenador solicitado no se a encontrado')      

# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
def porcentajesetentaynueve(lista_entrenadores):  
    for i in range(0, lista_entrenadores.size()):
            value = lista_entrenadores.get_element_by_index(i)
            total_batallas = value[0].cb_ganadas + value[0].cb_perdidas
            porcentaje = total_batallas * 0.79
            if value[0].cb_ganadas > porcentaje:
                print(value[0])

# g. el promedio de nivel de los Pokémons de un determinado entrenador;
def promediar(lista_entrenadores, e): 
    promedio = 0 
    cont = 0
    esto = lista_entrenadores.search(e, 'nombre')    
    
    if esto != None:
        value = lista_entrenadores.get_element_by_index(esto)
        for i in range(0, value[1].size()):
            valor = value[1].get_element_by_index(i)
                
            promedio = promedio + valor.nivel
            cont += 1    
              
        if cont > 0:
            final = promedio / cont  
            print(final)
        else:
            print('el entrenador no tiene pokemons')     

# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
def determinadoPokemon(lista_entrenadores, u):
    # lista_entrenadores.order_by('nombre')
    for i in range(0, lista_entrenadores.size()):
        
        value = lista_entrenadores.get_element_by_index(i)
        # value[1].barrido()
        # print(value[1].size())
        for j in range(0, value[1].size()):
            valor = value[1].get_element_by_index(j)
            # print(valor.nombre)
            if valor.nombre in u:
                print(value[0].nombre)

# i. mostrar los entrenadores que tienen Pokémons repetidos;
def pokemonsRepetidos(lista_entrenadores):
    
    for i in range (0, lista_entrenadores.size()):
        print('-----------------------------------------')
        value = lista_entrenadores.get_element_by_index(i)
        print(value[0].nombre)
        valor = value[1].get_element_by_index(i)
        cont=0
        print(valor.nombre)
        for j in range (0, value[1].size()):
            valore = value[1].get_element_by_index(j)
            print(valore.nombre)
        # for j in (value[1].nombre):
            
# f. (Mostrar supongo) los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);
def mostrar_tipo(lista_entrenadores):
    for i in range(0, lista_entrenadores.size()):
        
        valor = lista_entrenadores.get_element_by_index(i)
        for j in range(0, valor[1].size()):
            value = valor[1].get_element_by_index(j)
            if (value.tipo in 'agua' and value.subtipo in 'volador') or (value.tipo == 'fuego' and value.subtipo == 'planta')  :
                print(f'{valor[0].nombre} tiene su pokemon {value.nombre} tipo: {value.tipo} y subtipo: {value.subtipo}') 

#  j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;
def determinarPokemons(lista_entrenadores):
    for i in range(0, lista_entrenadores.size()):
        
        value = lista_entrenadores.get_element_by_index(i)
        # value[1].barrido()
        # print(value[1].size())
        for j in range(0, value[1].size()):
            valor = value[1].get_element_by_index(j)
            # print(valor.nombre)
            if valor.nombre in 'tyrantrum':
                print(f'{value[0].nombre} tiene a {valor.nombre}')
            if valor.nombre in 'terrakion':
                print(f'{value[0].nombre} tiene a {valor.nombre}')
            if valor.nombre in 'wingull':
                print(f'{value[0].nombre} tiene a {valor.nombre}')
            else:
                None
                
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;
def ingresoDatos(lista_entrenadores, nombreentrenador, nombrepokemon):
    esto = lista_entrenadores.search(nombreentrenador, 'nombre')    
    if esto != None:
        value = lista_entrenadores.get_element_by_index(esto)
        entrenado, sublista = value[0], value[1]
        # print(f"{entrenado.nombre} tiene estos pokemones")
        # sublista.barrido()
        cont = 0
        for j in range(0, sublista.size()):
            valor = sublista.get_element_by_index(j)
            # print(valor.nombre)
            if valor.nombre in nombrepokemon:
                cont += 1
                print(f'estos son los datos del entrenador: {entrenado}')
                print(f'estos son los datos del pokemon: {valor}')
        if cont == 0:       
            print(f'no se encontro el pokemon {nombrepokemon}')
                



print()
print('Recuerde que el nombre de cada entrenador debe empezar con mayuscula')
print('----------------------------------------------------------------------')
print()
quien = input('ingrese a la persona q desea saber la cantidad de pokemones:   ')
cantidadPokemons(lista_entrenadores, quien)
print()
print('----------------------------------------------------------------------')
print('Lista de entrenadores con mas de 3 torneeos ganados')
gano_mas_tres(lista_entrenadores)
print()
print('----------------------------------------------------------------------')
print('Entrenador con mas campeonatos y mejor pokemon')
mayorTorneosNivel(lista_entrenadores)
print()
print('----------------------------------------------------------------------')
print()
a = input('listado de pokemons de el entrenador:   ')
unEntrenador(lista_entrenadores, a)
print()
print('----------------------------------------------------------------------')
print('Entrenadores q ganaron el 79 por ciento sus las peleas')
porcentajesetentaynueve(lista_entrenadores)
print()
print('----------------------------------------------------------------------')
print()
e = input('promedio del nivel de los pokemons, del entrenador escrito en pantalla: ')
promediar(lista_entrenadores, e)
print()
print('----------------------------------------------------------------------')
print()
u = input('Deseas ver q entrenadores tienen el pokemon:  ')
print(f'Entrenedores con el pokemon: {u}')
determinadoPokemon(lista_entrenadores, u)
print()
print('----------------------------------------------------------------------')
print('Entrenadores con pokemon tipo agua o fuego y subtipo volador o planta ')
# pokemonsRepetidos(lista_entrenadores)
mostrar_tipo(lista_entrenadores)
print()
print('----------------------------------------------------------------------')
print()
determinarPokemons(lista_entrenadores)
print()
print('----------------------------------------------------------------------')
print()
nombreentrenador = input('Que entrenedor desea buscar?')
nombrepokemon = input('Que pokemon decea buscar?')
ingresoDatos(lista_entrenadores, nombreentrenador, nombrepokemon)








# esto = lista_entrenadores.search(a, 'nombre')    
#     if esto != None:
#         value = lista_entrenadores.get_element_by_index(esto)
#         value[1].order_by('nivel')
#         value[1].barrido()


#! A
# pos = lista_entrenadores.search('Juan', 'nombre')
# if pos is not None:
#     valor = lista_entrenadores.get_element_by_index(pos)
#     entrenador, sublista = valor[0], valor[1]
#     print(f'{entrenador.nombre} tiene {sublista.size()} pokemons')

# print()
# #! B
# lista_entrenadores.barrido_cantidad_torneos_ganados(6)

# print()
# #! C
# mayor_cantidad = lista_entrenadores.get_element_by_index(0)[0].ct_ganados
# pos_mayor = 0

# for pos in range(1, lista_entrenadores.size()):
#     entrenador = lista_entrenadores.get_element_by_index(pos)[0]
#     if entrenador.ct_ganados > mayor_cantidad:
#         pos_mayor = pos
#         mayor_cantidad = entrenador.ct_ganados

# valor = lista_entrenadores.get_element_by_index(pos_mayor)
# entrenador, sublista = valor[0], valor[1]

# if sublista.size() > 0:
#     pokemon_mayor = sublista.get_element_by_index(0)
#     for pos in range(1, sublista.size()):
#         pokemon = sublista.get_element_by_index(pos)
#         if pokemon.nivel > pokemon_mayor.nivel:
#             pokemon_mayor = pokemon

# print(f'El pokemon de mayor nivel del entrenador {entrenador.nombre} es {pokemon_mayor.nombre} {pokemon_mayor.nivel} ')