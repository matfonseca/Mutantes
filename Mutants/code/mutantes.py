#Suposiciones: 
#  - Se considera que las secuencia de 4 caracteres iguales se pueden solapar parcialmente. 
#       por ejemplo: que en una fila haya AAAAAGC se considera que las cuatro primeras A son una secuencia 
#       y de la segunda hasta la quinta otra.
#  - Dado que la secuencia debe tener 4 caracteres iguales, una matriz de dimension menor a 4x4 no podria 
#    cumplir con la condicion, por lo tanto se supone que la matriz tiene una dimension igual o mayor a 4x4.
#    En caso contrario se informara por la API que la dimension es incorrecta.

class MutantDetector(object):

    def isMutant(self,dna):
        
        isMutant = False
        n = len(dna)  #Dimension

        count_equalSecuences = 0

        #Busca secuencia de 4 caracteres iguales en posicion horizontal
        count_equalSecuences,isMutant = self.checkHorizontal(dna,n,count_equalSecuences)

        if(isMutant):
            return isMutant

        #Busca secuencia de 4 caracteres iguales en posicion vertical
        count_equalSecuences,isMutant = self.checkVertical(dna,n,count_equalSecuences)

        if(isMutant):
            return isMutant

        #Busca secuencia de 4 caracteres iguales en posicion Diagonal
        count_equalSecuences,isMutant = self.checkDiagonal(dna,n,count_equalSecuences)

        return isMutant

    def checkHorizontal(self,dna,n,count_equalSecuences):
        
        for cadena in dna:
            for index in range(0, n - 3):
                
                subcadena = cadena[index : index + 4]
                
                if(self.checkEqualCaracteres(subcadena)):
                    count_equalSecuences += 1
                    if(count_equalSecuences >= 2):
                        return count_equalSecuences,True
                    
        
        return count_equalSecuences,False

    def checkVertical(self,dna,n,count_equalSecuences):
        dna_invertido = ['' for i in range(0,n)]

        #Transpone la matriz
        for cadena in dna: 
            index_dna_invertido = 0
            for caracter in cadena:
                dna_invertido[index_dna_invertido] += caracter
                index_dna_invertido += 1
                
        return self.checkHorizontal(dna_invertido,n,count_equalSecuences)

    def checkDiagonal(self,dna,n,count_equalSecuences):
        for fila in range(0,n-3): 
            
            fila_1 = fila + 1 
            fila_2 = fila + 2 
            fila_3 = fila + 3

            #diagonal con indice de columna de menor a mayor
            # x 0 0 0
            # 0 x 0 0       x:posiciones que incluye la diagonal
            # 0 0 x 0
            # 0 0 0 x
            for colum in range(0,n-3):  

                colum_1 = colum + 1
                colum_2 = colum + 2
                colum_3 = colum + 3  

                caracter0 = dna[fila][colum]
                caracter1 = dna[fila_1][colum_1]
                caracter2 = dna[fila_2][colum_2]
                caracter3 = dna[fila_3][colum_3]

                subcadena = caracter0 + caracter1 + caracter2 + caracter3
                
                if(self.checkEqualCaracteres(subcadena)):
                    count_equalSecuences += 1               
                    if(count_equalSecuences >= 2):
                        return count_equalSecuences,True
            
            #diagonal con indice de columna de mayor a menor
            # 0 0 0 x
            # 0 0 x 0      x:posiciones que incluye la diagonal
            # 0 x 0 0
            # x 0 0 0
            for colum2 in range(0,n-3):
                
                colum2_1 = colum2 + 1
                colum2_2 = colum2 + 2
                colum2_3 = colum2 + 3  

                caracter0 = dna[fila][colum2_3]
                caracter1 = dna[fila_1][colum2_2]
                caracter2 = dna[fila_2][colum2_1]
                caracter3 = dna[fila_3][colum2]

                subcadena = caracter0 + caracter1 + caracter2 + caracter3
                
                if(self.checkEqualCaracteres(subcadena)):
                    count_equalSecuences += 1
                    if(count_equalSecuences >= 2):
                        return count_equalSecuences,True
            
            return count_equalSecuences,False

    def checkEqualCaracteres(self,subcadena):
        return subcadena[0] == subcadena[1] == subcadena[2] == subcadena[3]
