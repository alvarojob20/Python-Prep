class operaciones_lista:
    def __init__(self, lista):
        if (type(lista) != list):
            self.lista = []
            raise ValueError('Se ha ingresado un parametro incorrecto. Se esperaba una lista de núemeros enteros')  
        else:
            self.lista = lista
    
    def es_primo(self):
        lista_primos = []
        for numero in self.lista:
            if self.__es_primo(numero):
                lista_primos.append(True)
            else:
                lista_primos.append(False)
        return lista_primos
    
    def convertir_temperatura(self, origen, destino):
        '''
        Ingrese los siguientes valores en los parámetros para 
        indicar el tipo de sistema de medición de temperatura:

        Celsius: 'C'
        Farenheit: 'F' 
        Kelvin: 'K'
        '''
        valores_esperados = ['C','F','K']
        lista_temperaturas = []
        
        if origen not in valores_esperados:
            raise ValueError("Verifique valor ingresado en grados de origen. Valores esperados: 'C' 'F' 'K'")
        elif destino not in valores_esperados:
            raise ValueError("Verifique valor ingresado en grados de destino. Valores esperados: 'C' 'F' 'K'")
        else:
            for temperatura in self.lista:
                lista_temperaturas.append(self.__convertir_temperatura(temperatura,origen,destino))
        return lista_temperaturas
    
    def factorial(self):
        lista_factoriales = []
        for numero in self.lista:
            lista_factoriales.append(self.__factorial(numero))
        return lista_factoriales

    def __es_primo (self, numero):
        
        primo = True
        if numero > 1 :
            i = 1
            while numero - i > 1:        
                if numero % (numero - i) == 0 :
                    primo = False
                    break
                i += 1
        else:
            primo = False
        return primo
    
    def moda_mayor_menor (self,mayor = True):
        '''
        Si hay mas de un valor modal, se mostrará el valor mayor por defecto.
        Para mostrar el valor menor ingrese el parámetro 'mayor = False'
        '''

        rep = 1
        for numero in self.lista:
            if self.lista.count(numero) > rep:
                rep = self.lista.count(numero)

        mas_reps = []
        for numero in self.lista:
            if (self.lista.count(numero) == rep) and not(numero in mas_reps):
                mas_reps.append(numero)

        if len(mas_reps) <= 1:
            moda = mas_reps[0]        
        else:
            print('Hay mas de un valor modal')
            if mayor:
                i = 1
                num = mas_reps[i-1]
                while i < len(mas_reps):
                    if mas_reps[i] > num:
                        num = mas_reps[i]
                    i += 1   
                moda = num    
            else :
                i = 1
                num = mas_reps[i-1]
                while i < len(mas_reps):
                    if mas_reps[i] < num:
                        num = mas_reps[i]
                    i += 1   
                moda = num
        return moda, self.lista.count(moda)
    
    def __convertir_temperatura(self, temperatura,grados_origen, grados_destino):

        conversion = None
        
        if (grados_origen == 'C'):

            if (grados_destino == 'C'):
                conversion = temperatura
            elif (grados_destino == 'F'):
                conversion = (temperatura * (9/5)) + 32
            elif (grados_destino == 'K'):
                conversion = temperatura + 273.15 
            else:
                print('Verifique valor ingresado en grados de destino')

        elif (grados_origen == 'F'):
            if (grados_destino == 'F'):
                conversion = temperatura
            elif (grados_destino == 'C'):
                conversion = (temperatura - 32) * (5/9)
            elif (grados_destino == 'K'):
                c = (temperatura - 32) * (5/9)
                conversion = c + 273.15
            else:
                print('Verifique valor ingresado en grados de destino')
        
        elif (grados_origen == 'K'):

            if (grados_destino == 'K'):
                conversion = temperatura
            elif (grados_destino == 'C'):
                conversion = temperatura - 273.15
            elif (grados_destino == 'F'):
                c = temperatura - 273.15
                conversion = (c * (9/5)) + 32
            else:
                print('Verifique valor ingresado en grados de destino')
        else:
            print('Verifique valor ingresado en grados de origen')
        return conversion
    
    def __factorial (self,numero):
        '''
        Devuelve el factorial
        '''

        if type(numero) != int: 
            return 'Verique que el valor ingresado es un entero'
        if numero < 1:
            return 'Verique que el valor ingresado es positivo'
        
        if numero > 2:
            numero = numero * self.__factorial(numero - 1)
        return numero
