def main():
  #escribe tu código abajo de esta línea
  pass
  matriz1=[]
  matriz2=[]
  suma_matriz=[]

  m1=input()
  while m1 != "":
    matriz1.append(m1.split( ))
    m1=input()

  m2=input()
  while m2 != "":
    matriz2.append(m2.split( ))
    m2=input()
  
  if len(matriz1) != len(matriz1):
    print("Las matrices no son del mismo tamaño")
  else:
    for k in range(len(matriz1)):
      suma=[]
      for j in range(len(matriz1[k])):
        suma.append(int(matriz1[k][j])+int(matriz2[k][j]))
      suma_matriz.append(suma)
    print(suma_matriz)




if __name__=='__main__':
    main()