from modulos import calculadora as calc, estatistica as esta, geometria as geo

isOn = True

while isOn:
    print('Calculadora\n\nEscolha qual tipo de calculadora deseja usar:\n1 - Comum\n2 → Geométrica\n3 → Estatística\n')
    tipo = int(input())

    match tipo:
        #Calculadora Comum
        case 1:
            print('\nCalculadora Comum\n\nEscolha qual tipo de operação deseja realizar:\n1 - Soma\n2 → Subtração\n3 → Multiplicação\n4 → Divisão\n5 → Potêncição\n6 → Raiz Quadrada\n7 → Porcentagem\n')
            op = int(input())

            match op:
                case 1:
                    calc.Soma()
                case 2:
                    calc.Subtracao()
                case 3:
                    calc.Multiplicacao()
                case 4:
                    calc.Divisao()
                case 5:
                    calc.Potencia()
                case 6:
                    calc.RaizQuadrada()
                case 7:
                    calc.Porcentagem()
                case _:
                    print('\nValor inválido! Tente novamente.\n')

        #Calculadora Geométrica
        case 2:
            print('\nCalculadora Geomértrica\n\nEscolha qual tipo de operação deseja realizar:\n1 → Area do Quadrado\n2 → Área do Circulo\n3 → Área do Triângulo\n4 → Volume do Cubo\n5 → Volume da Esfera\n6 → Volume do Pirâmide\n')
            op = int(input())

            match op:
                case 1:
                    geo.AreaQuadrado()
                case 1:
                    geo.AreaQuadrado()
                case 1:
                    geo.AreaQuadrado()
                case 1:
                    geo.AreaQuadrado()
                case 1:
                    geo.AreaQuadrado()
                case 1:
                    geo.AreaQuadrado()
                
        
        case _:
            print('\nValor inválido! Tente novamente.\n')