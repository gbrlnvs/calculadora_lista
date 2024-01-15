n1 = float(input("Digite a primeira nota"))
n2 = float(input("Digite a segunda nota"))
resultado= ""
opcao = input("Deseja usar a calculadora? s ou n")

while opcao !="n":
    calc = int(input("1 - soma\n 2 - sub\n 3 - mult\n4 - div\n5 - pot\n6 - Resto"))
    if calc == 1:
        print(n1+n2)
        listSoma = []
        listSoma.append(n1+n2)
    elif calc ==2:
        resultado=n1-n2
        print(resultado)
        listaSub = []
        listaSub.append(resultado)
    elif calc==3:
       print(n1*n2)
       listMult = []
       listMult.append(n1*n2)
    elif calc == 4:
        print(n1 / n2)
        listDiv = []
        listDiv.append(n1/n2)
    elif calc == 5:
        print(n1 ** n2)
        listPot = []
        listPot.append(n1**n2)
    elif calc == 6:
        if n1<n2:
            print(n2%n1)
            listResto = []
            listResto.append(n1%n2)
        else:
            print(n1%n2)


