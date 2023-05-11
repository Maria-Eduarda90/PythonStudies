class Argentina():
    def capital(self):
        print('Buenos Aires é a capitap da Argentina')
    def lingua_oficial(self):
        print('O espanhol é a lingua oficial da Argentina')

class Brasil():
    def capital(self):
        print('Brasilia é a capitap do Brasil')
    def lingua_oficial(self):
        print('O português é a lingua oficial do Brasil')

obj_arg = Argentina()
obj_bra = Brasil()
for pais in(obj_arg, obj_bra):
    pais.capital()
    pais.lingua_oficial()