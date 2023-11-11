class Reserva:
    def ___init__ (self, nombre, telefono, fecha, hora, email):
        self.nombre = nombre
        self.telefono = telefono
        self.fecha = fecha
        self.hora = hora
        self.email = email
    def __str__(self):
        return f"""Nombre: {self.nombre}, Telefono: {self.telefono}, fecha: {self.fecha}, hora: {self.hora}, y email: {self.email}"""
nombre_talia = Reserva("talia", "3014348535", "19/10/2023", "10:15", "taliaberri9@gmail.com")
print (nombre_talia)