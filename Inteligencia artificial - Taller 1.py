
# coding: utf-8

# In[2]:


import statistics as stats

valores = [1, 2, 2, 4, 5, 6, 6, 6, 8, 9]

print ("ESTADISTICA BÁSICA")
print ("")
print ("Los datos almacenados son: ", valores)
print ("")

#MEDIANA
valores.sort()

if len(valores) % 2 == 0:
    n = len(valores)
    mediana = (valores[n//2-1] + valores[n//2]) // 2
else: 
    mediana = valores[len(valores)//2]
    
print ("1. La mediana es: ", mediana)


#MODA
inicial = 0
for i in valores:
    repetitivo = valores.count(i)
    if repetitivo > inicial:
        inicial = repetitivo
        
moda = []
for i in valores:
    repetitivo = valores.count(i)
    if repetitivo == inicial and i not in moda:
        moda.append(i)
        
print ("2. La moda es: ", moda)


#PROMEDIO

promedio = sum(valores)/len(valores)

print ("3. El promedio es: ", promedio)


#VARIANZA

print ("4. La varianza es: ", (stats.pvariance(valores)))


#COVARIANZA
    
print ("5. La covarianza es: ", (stats.stdev(valores)))

print ("")
print ("El total de los datos es: ", (len(valores)))

