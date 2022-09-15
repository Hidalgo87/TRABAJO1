"""
Registrar ropa
Alquilar ropa
Mostrar un grupo de prendas relacionadas con el clima
"""


class Prenda:

    def __init__(self, codigo: int, nombre: str, clima: str,
                 valor_prenda: int, valor_alquiler: int):
        self.codigo = codigo
        self.nombre = nombre
        self.disponibilidad_renta = True
        self.clima = clima
        self.valor_prenda = valor_prenda
        self.valor_alquiler = valor_alquiler
        self.rentas_mes = 0


class Renta:

    def __init__(self, tiempo: int, entregar_prenda: bool, estado: bool):
        self.tiempo = tiempo
        self.entregar_prenda = entregar_prenda
        self.estado = estado


class Usuario:

    def __init__(self, cedula: int, correo: str, numero_rentas: int, deuda: int, orden: Renta):
        self.cedula = cedula
        self.correo = correo
        self.numero_rentas = numero_rentas
        self.deuda = deuda
        self.orden = orden

    def comprobar_planes(self, cedula: int) -> bool:
        pass


class Tienda:

    def __init__(self):
        self.prendas: list[Prenda] = []
        self.usuarios: dict[int:Renta] = {}

    def registrar_ropa(self) -> list[Prenda]:
        self.prendas[0] = Prenda(0, "Saco de Juanma", "INVIERNO", 40000, 100)
        self.prendas[1] = Prenda(1, "Pantaloneta", "VERANO", 20000, 40)
        self.prendas[2] = Prenda(2, "Jordans", "TODAS", 150000, 270)
        return self.prendas

    def alquilar_prenda(self, cedula: int, prenda: Prenda, tiempo: int) -> Prenda:
        """El tiempo es en días"""
