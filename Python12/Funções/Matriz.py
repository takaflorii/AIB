def cria_matriz(num_linhas, num_colunas, valor):
    '''Cria uma matriz com "num_linhas" linhas e "num_colunas" colunas, inicializadas com o valor dado.'''
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = 0
            linha.append(valor)
        matriz.append(linha)

    return matriz

def le_matriz(matriz):
    '''Lê os valores de uma matriz e retorna a matriz preenchida.'''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            valor = int(input(f'Insira o valor para a posição [{i}][{j}]: '))
            matriz[i][j] = valor
    return matriz


if __name__ == "__main__":
    # exemplo: cria e imprime cada linha em separado (uma linha por print)
    m = cria_matriz(3, 4, 0)
    for linha in m:
        print(linha)