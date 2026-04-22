class Cuenta:
   def __init__(self, saldo,tipo,nombre_titular):
      self.saldo = float(saldo)
      self.tipo = str(tipo)
      self.nombre_titular = str(nombre_titular)