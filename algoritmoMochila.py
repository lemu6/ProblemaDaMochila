def Mochila(valores, pesos, capacidade):

    n = len(valores) # ou tamanho(pesos), ambos devem ser iguais

    dp = [[0] * (capacidade + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacidade + 1):
            if pesos[i - 1] > j:
                dp[i][j] = dp[i - 1][j]; # base case"se nao houver itens ou a capacidade for 0, o valor maximo é 0
            
             # Se o peso do item for maior que a capacidade, nao podemos inclui-lo
            else:
                dp[i][j] = max(dp[i - 1][j], valores[i - 1] + dp[i - 1][j - pesos[i -1 ]]) # escolhe o maximo entre incluir ou nao incluir o item

    return dp[n][capacidade] # retorna o valor maximo que pode ser obtido

#Exemplo de uso
valores = [60, 100, 120]
pesos = [10, 20, 30]
capacidade = 50
print(Mochila(valores, pesos, capacidade)) # saida esperada: 220
