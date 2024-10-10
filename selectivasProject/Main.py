# Simple
a = 33
b = 200

if b > a:
    print(b,"es mayor que",a)

# Doble
y = 200
z = 333

if y  >  z:
    print(y,"es mayor que",z)
else:
    print(y,"es mayor que",z)

#Multiple
k = 200
t = 207
if k > t:
    print(k,"es mayor que",t)
elif k < t:
    print(k,"es menor que",t)
else:
    print(k,"es igualque",t)

#ENLAZADAS
x = 28

if x > 10:
    print("por encima de diez,")
    if x > 20:
        print("y tambien por encima de 20!")
    else:
        print("pero no por emcima de 20.")


#PARÁMETROS END
print("Estudiar los sabados", end=' ')
print("es genial")

#print("Estudiar los sabados")
#print("es genial")

#PARÁMETROS SEP
print("Daniela","Luis","Carlos","Camila") #Agregar un espacio por defecto
print("Daniela","Luis","Carlos","Camila",sep="") #Quita el espacio
print("Daniela","Luis","Carlos","Camila",sep=",") #Agrega una coma

print("Daniela","Luis","Carlos","Camila",sep = "_", end="_Curso_Python") #Implementacion end y sep
