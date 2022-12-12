def hanoi():
    def mova(n, origem, destino, aux, jogada):
        def mexerdisco(de, para, jogada):
            print(f"Jogada {jogada:>3}: Torre {de} --> Torre {para}")
            return jogada + 1 # atualiza para a próxima jogada

        if n == 1:
            jogada = mexerdisco(origem, destino, jogada)
        else:
            jogada = mova(n - 1, origem, aux, destino, jogada)
            jogada = mexerdisco(origem, destino, jogada)
            jogada = mova(n - 1, aux, destino, origem, jogada)

        return jogada
    print (" --------------------------------------------------------")
    print(" ------ Trabalho matemática Torre de hanoi ----------- ")
    print (" --------------------------------------------------------")
    n = int(input("<@_@>-- Quantidade de discos ? -- <(@_@)> \n         -- Digite aqui -->"))
    print (" -------------------------")
    print(f"Solução ({2 ** n - 1} Movimetações):")
    print (" -------------------------")
    
    mova(n, "1", "3", "2", 1)


    
hanoi()
