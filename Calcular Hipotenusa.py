import math

class Calcular_Hipotenusa():
    def __init__(self):
        self.Cat1 = None 
        self.Cat2 = None 
        self.Hip = None 
    def Iniciar(self):
        self.Cat1 = input("Dê o valor do Cateto 1:")
        self.Cat2 = input("Dê o valor do Cateto 2:")
        self.Hip = math.sqrt(int(self.Cat1) ** 2 + int(self.Cat2) ** 2) 
        print(self.Hip)
        
calcular_hipotenusa = Calcular_Hipotenusa()
calcular_hipotenusa.Iniciar()
