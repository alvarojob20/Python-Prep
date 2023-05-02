class operaciones_lista:
    def __init__(self, lista = list()):
        self.lista = lista
    
    def es_primo(self):
        for numero in self.lista:
            if self._es_primo(numero):
                print(numero,'es un numero primo')
            else:
                print(numero,'no es un numero primo')
    
    def convertir_temperatura(self, origen, destino):
        for temperatura in self.lista:
            print(temperatura, 'grados', origen, 'en grados', destino, '=', self._convertir_temperatura(temperatura,origen,destino) )
    
    def factorial(self):
        for numero in self.lista:
            print(numero, 'factorial es:', self._factorial(numero))

    def _es_primo (self, numero):
        
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
    
    def _convertir_temperatura(self, temperatura,grados_origen, grados_destino):
        '''
        Ingrese los siguientes valores en los parámetros para 
        indicar el tipo de sistema de medición de temperatura:

        Celsius: 'C'
        Farenheit: 'F' 
        Kelvin: 'K'
        '''

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
    
    def _factorial (self,numero):
        '''
        Devuelve el factorial
        '''

        if type(numero) != int: 
            return 'Verique que el valor ingresado es un entero'
        if numero < 1:
            return 'Verique que el valor ingresado es positivo'
        
        if numero > 2:
            numero = numero * self._factorial(numero - 1)
        return numero
