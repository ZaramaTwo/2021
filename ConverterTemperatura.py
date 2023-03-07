class Converter_Temperatura:
    def __init__(self):
        self.Temp_C = None
        self.Temp_F = None
    def Iniciar(self):
        self.Temp_C = float(input("Informe a Temperatura em Celsius:"))
        self.Temp_F = (9 * self.Temp_C + 160) / 5
        print("A temperatura em Fahrenheit é" + str(self.Temp_F))      
        self.Iniciar()
        
temperatura = Converter_Temperatura()        
temperatura.Iniciar()
