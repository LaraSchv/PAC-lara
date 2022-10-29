lista_columnas_fijas = [
        'marca temporal',
        'nombre de usuario',
        'retirar',
        'fechas entrega'
]

lista_columnas_productos = [
        'choclo',
        'palta',
        'tomate perita',
        'morron verde',
        'uva',
        'berenjena agroecologica',
        'ajo',
        'ciruela',
        'manzana roja',
        'limon',
        'pera',
        'naranja',
        'durazno',
        'morron rojo',
        'zapallito redondo',
        'tomate cherry',
        'mandarina',
        'frutillas',
        'banana',
        'mango',
        'arandanos',
        'jengibre'
]

lista_nombres_nuevos = lista_columnas_fijas + lista_columnas_productos

dict_nombres_nuevos = {
        'bolson de verduras verdes': 'bolson de verdes',
        'bolson de pesadas': 'bolson de pesadas',
        'combo bolson': 'combo bolson verdes pesadas',
        'combo citrico': 'bolson citricos'
}

lista_nombres_nuevos.remove('fechas entrega')
lista_columnas_necesarias = lista_nombres_nuevos + list(dict_nombres_nuevos.values())

barrios = ['Palermo', 'Villa Urquiza', 'Villa Crespo']

#prueba commit Lenny

#prueba Lenny 3
