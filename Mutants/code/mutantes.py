class MutantDetector(object):

    def isMutant(self,dna):
        
        isMutant = False
        n = len(dna)  #Dimension

        count_equalSecuences = 0

        count_equalSecuences,isMutant = self.checkHorizontal(dna,n,count_equalSecuences)

        if(isMutant):
            return isMutant

        count_equalSecuences,isMutant = self.checkVertical(dna,n,count_equalSecuences)

        if(isMutant):
            return isMutant

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
