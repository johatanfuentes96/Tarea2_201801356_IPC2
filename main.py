from ListaCircularDoblementeEnlazada import ListaCircularDoblementeEnlazada

listaNumero = ListaCircularDoblementeEnlazada()

listaNumero.agregarUltimo(2)
listaNumero.agregarUltimo(7)
listaNumero.agregarUltimo(5)
listaNumero.agregarUltimo(11)
listaNumero.agregarUltimo(4)

listaNumero.recorre()

buscarNumero = int(input("INGRESE EL NUMERO A BUSCAR = "))


valor = listaNumero.buscar(buscarNumero)   # -->  Valor tiene = return ---> temp, -1

if valor == -1:
    print("NO SE ENCONTRO EL NUMERO INGRESADO")
else:
    print(f"  ---> Seleccione Numero = {valor.numero}")
    print("")
    print(f"    ---> Siguiente =  {valor.siguiente.numero}")
    print(f"    ---> Anterior =  {valor.anterior.numero}")
    print(f"    ---> Actual =  {valor.numero}")
    print("".center(50,"-"))

