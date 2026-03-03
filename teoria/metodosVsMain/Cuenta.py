class Cuenta:
  def __init__(self, saldo, tipo, fecha_creacion):
    self.saldo = saldo
    self.tipo = tipo
    self.fecha_creacion = fecha_creacion
  def informacion(self):
    print("Cantidad:", self.saldo)
    print("Tipo:", self.tipo)
    print("Fecha de creación:", self.fecha_creacion)
  def retirar(self, cantidad):
    self.saldo = self.saldo - cantidad
  def depositar(self, cantidad):
    self.saldo = self.saldo + cantidad