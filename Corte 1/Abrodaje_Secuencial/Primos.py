## 1 decima corte 1
a = 1
value = input('Ingrese un valor: ')
value = int(value)

while a == 1:
    for i in range(1,value+1):
        count = 0
        for n in range(1, i+1):
            residue = i%n
            if residue == 0:
                count = count + 1
            
          
    if count == 2:
       print(f'{i} Es un numero primo')
       print("\n")
    else:
       print(f'{i} No es un numero primo')
       print("\n")

    print('Desea continuar?. Presione 1 para hacerlo')
    a = input()
    a = int(a)

    if a != 1:
        break

    value = input('Ingrese un valor: ')
    value = int(value)
