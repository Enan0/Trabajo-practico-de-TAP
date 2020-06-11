from entorno.Tableros_especiales.TableroCuadrado import TableroCuadrado


class Celda_test(object):
    def __repr__(self):
        return f"cordenadas x:{self.posicionX} y:{self.posicionY}"

    def __str__(self):
        return f" x:{self.posicionX} y:{self.posicionY}"

    def __init__(self, posicionX, posicionY):
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.personajes = []

    def agregar_personaje(self, personaje):
        self.personajes.append(personaje)


class Tablero_test(object):
    def __init__(self, dimension):
        self.dimension = dimension
        self.celdas = {}

    def crear_tabla(self):
        for posX in range(self.dimension):
            for posY in range(self.dimension):
                self.celdas[f"x{posX}"] = []
                self.celdas[f"y{posY}"] = []

    def agregar_celdas(self):
        """FILA"""
        for y in range(self.dimension):
            """Columna"""
            for x in range(self.dimension):
                celda = Celda_test(x, y)
                self.celdas[f"x{x}"].append(celda)
                self.celdas[f"y{y}"].append(celda)

    def dame_tabla(self):
        return self.celdas

    def dame_celda(self, posX, posY):
        try:
            response = self.celdas[f"x{posX}"][posY]
        except IndexError:
            raise Exception("Esa celda no esta disponible o no existe")

        return response

    def construir_tablero(self):
        self.crear_tabla()
        self.agregar_celdas()


tablero = Tablero_test(4)

tablero.construir_tablero()


class Personaje_test(object):
    def __repr__(self):
        return self.nombre

    def __str__(self):
        return self.nombre

    def __init__(self, posX, posY, tablero, nombre):
        self.nombre = str(nombre)
        self.tablero = tablero
        self.x = int(posX)
        self.y = int(posY)
        self.celda = self.tablero.dame_celda(self.x, self.y)

    def entrar_a_celda(self):
        celda = self.tablero.dame_celda(self.x, self.y)
        celda.agregar_personaje(self)


juansito777 = Personaje_test(1, 1, tablero, "juansito_xXx")

celda_1_1 = tablero.dame_celda(1, 1)

juansito777.entrar_a_celda()


print(celda_1_1.personajes)
