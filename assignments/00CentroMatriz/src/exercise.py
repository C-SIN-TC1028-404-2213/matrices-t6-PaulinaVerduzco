def main():
  #escribe tu código abajo de esta línea
  pass
  r=int(input(""))
  C=int(input(""))
  matriz=[]

  for row in range(r):
    renglon=[]
    for column in range(C):
      n=int(input(""))
      renglon.append(n)
    matriz.append(renglon)
  if len(matriz)==1:
    matriz.pop(0)
    print(matriz)
  elif len (matriz)==2:
    matriz.pop(0)
    matriz.pop(-1)
    print(matriz)
  elif len(matriz)==0:
    print(matriz)
  else:
    matriz.pop(0)
    matriz.pop(-1)
    for i in range(len(matriz)):
      del matriz[0][0]
      del matriz[-1][-1]
    print(matriz)


if __name__=='__main__':
    main()
