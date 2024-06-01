import concurrent.futures

def calculate_max_lectures(n, k1, k2, days):
    # dp[i][j] will represent the maximum number of lectures for the first i days,
    # where j is the number of lectures on the i-th day.
    dp = [[-1] * (k1 + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        if days[i - 1] == '0':
            for j in range(k1 + 1):
                dp[i][0] = max(dp[i][0], dp[i - 1][j])
        else:
            for j in range(k1 + 1):
                for k in range(k1 + 1):
                    if j + k <= k2 and dp[i - 1][k] != -1:
                        dp[i][j] = max(dp[i][j], dp[i - 1][k] + j)

    return max(dp[n])

def process_test_case(test_case):
    n, k1, k2, days = test_case
    return calculate_max_lectures(n, k1, k2, days)

def main():
    print("Please enter your input:")
    t = int(input().strip())
    test_cases = []

    for _ in range(t):
        n, k1, k2 = map(int, input().strip().split())
        days = input().strip()
        test_cases.append((n, k1, k2, days))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(process_test_case, test_cases))


    print("\n")
    for result in results:
        
        print(result)

if __name__ == "__main__":
    main()