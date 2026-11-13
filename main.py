from cliente import Cliente
from reserva import ReservaSala
from logger import registrar_log

from excepciones import(
    ClienteInvalidoError,
    ServicioInvalidoError
)
try:

    cliente1 = Cliente(
        "Juan Perez",
        "123456",
        "juan@gmail.com"
    )
    servicio1 = ReservaSala(
        "Sala Premium",
        50000
    )
    print(cliente1.mostrar())
    costo = servicio1.calcular_costo(3)
        
    print(
        f"Servicio: {servicio1.descripcion()}"
    )

    print(
        f"Costo total:{costo}"
    )

    registrar_log(
        "Cliente registrado correctamente"
    )
    registrar_log(
        "Reserva creada correctamente"
    )
    
except(
    ClienteInvalidoError,
    ServicioInvalidoError
) as error:
    
    print(f"Error:{error}")

    registrar_log(
        f"ERROR:{error}"
    )

finally:
    registrar_log(
        "Fin de ejecucion del sistema"
    )