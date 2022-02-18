from elementos import tabela_periodica


molecula = 'Ca3(PO4)2'


coeficientes = {}
MassaMolar = 0

def Qtd_Atamos(elemento, coeficiente, index):
    if len(elemento) == 2:
        if molecula[index+2].isdecimal() == True:
            coeficientes[elemento] = int(molecula[index+2])
        else:
            coeficientes[elemento] = 1
    
    elif molecula[index+1].isdecimal() == True:
        coeficientes[elemento] = int(molecula[index+1])

    else:
        coeficientes[elemento] = 1


    if '(' in molecula:
        parentese = molecula.index('(')
        fecha_parentese = molecula.index(')', parentese)

        if index > parentese and index < fecha_parentese:
            multiplicador = int(molecula[fecha_parentese+1])
            
            coeficientes[elemento] = coeficientes[elemento] * multiplicador


for elemento in tabela_periodica.keys():
    if elemento in molecula:
        index = molecula.find(elemento)

        Qtd_Atamos(elemento, coeficientes, index)
        index = 0

for elemento, n_Atamos in coeficientes.items():
    MassaAtomica = tabela_periodica[elemento]
    
    MassaMolar += n_Atamos * MassaAtomica
    

print(coeficientes)
print(f"Formula Quimica: {molecula}\nMassa Molar: {MassaMolar:.4f}g/mol")
