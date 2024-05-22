import concurrent.futures

def max_chipriota(arr):
    n = len(arr)
    dp = [[-float('inf')]*(n+1) for _ in range(n+1)]
    divs = [[[] for _ in range(n+1)] for _ in range(n+1)]
    prefix_sum = [0]*(n+1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + arr[i]
    dp[0][0] = 0

    def calculate_dp_and_divs(i, j):
        for k in range(i):
            val = dp[k][j-1] + j*(prefix_sum[i]-prefix_sum[k])
            if val > dp[i][j]:
                dp[i][j] = val
                div = divs[k][j-1] + [arr[k:i]]
                divs[i][j] = div

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i in range(1, n+1):
            for j in range(1, i+1):
                executor.submit(calculate_dp_and_divs, i, j)

    max_j = max(range(n+1), key=lambda j: dp[n][j])
    return dp[n][max_j], divs[n][max_j]

# Leer la entrada
num_arrays = int(input())
arrays = []
for _ in range(num_arrays):
    length = int(input())
    array = list(map(int, input().split()))
    arrays.append(array)

# Calcular y mostrar los resultados
for arr in arrays:
    max_val, max_div = max_chipriota(arr)
    print(f"{max_val}")











