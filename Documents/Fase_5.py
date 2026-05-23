# PROBLEMA # 2
# Gestion de precios de un menu de restaurante
# MATRIZ DEL MENU
menu = [
    ["Hamburguesa","Comida rapida",25000],
    ["Pizza","Comida rapida",32000],
    ["Ensalada","saludable",18000],
    ["Jugo natural","saludable",12000],
    ["Pasta","Italiana",28000],
    ["Lasagna","Italiana",35000]
]
# Calcula el precio final
def calcular_precio_final (categoria,precio_base,categoria_objetivo, umbral):
    descuento= 0.15 

    # CONDICION PARA APLICAR PROMOCION
    if categoria == categoria_objetivo and precio_base > umbral:
        precio_final = precio_base - (precio_base * descuento)
    else: 
        precio_final = precio_base
    return precio_final
# DATOS DE LA PROMOCION
Categoria_objetivo = "Italiana"
umbral = 30000

# RECORRER ELMENU

for producto in menu:
    nombre= producto[0]
    categoria= producto[1]
    precio_base= producto[2]

    precio_final= calcular_precio_final(
        categoria,
        precio_base,
        Categoria_objetivo,
        umbral
    )
    # MOSTRAR RESULTADOS
    print("Producto:", nombre)
    print("Categoria:",categoria)
    print("Precio Base: $", precio_base)
    print("precio final: $ ,precio_final")
    print("-------------")

    


