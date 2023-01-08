import pickle

class Vehiculo:
    tipo = ""
    costo = 0.0

    def __init__(self, tipo, costo):
        self.tipo = tipo
        self.costo = costo

    def getTipo(self):
        return self.tipo

v = Vehiculo("carro", 10000)
f = open("datos.bin" , "wb")
pickle.dump(v, f)
f.close()

f = open("datos.bin" , "rb")
vehiculo = pickle.load(f)
f.close()

print(f"{vehiculo.getTipo()} {vehiculo.costo}")
