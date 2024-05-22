def max_chipriota(arr):
    n = len(arr)
    dp = [[-float('inf')]*(n+1) for _ in range(n+1)]
    divs = [[[] for _ in range(n+1)] for _ in range(n+1)]
    prefix_sum = [0]*(n+1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + arr[i]
    dp[0][0] = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            for k in range(i):
                val = dp[k][j-1] + j*(prefix_sum[i]-prefix_sum[k])
                if val > dp[i][j]:
                    dp[i][j] = val
                    div = divs[k][j-1] + [arr[k:i]]
                    divs[i][j] = div
    max_j = max(range(n+1), key=lambda j: dp[n][j])
    return dp[n][max_j], divs[n][max_j]

# Ejemplo de entrada
arr = [-3, -4, 2, -5, 1, 10, 17, 23]
max_val, max_div = max_chipriota(arr)
print(f"Valor Chipriota Máximo: {max_val}, Divisiones: {max_div}")









