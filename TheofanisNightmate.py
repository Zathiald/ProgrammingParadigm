import sys
import concurrent.futures

def calculate_max_cypriot_value(n, array):
    max_cypriot_value = sum((i + 1) * array[i] for i in range(n))

    # Dividimos el array en subarrays de un solo elemento
    division = [[array[i]] for i in range(n)]

    return max_cypriot_value, division

def process_test_case(test_case):
    n, array = test_case
    return calculate_max_cypriot_value(n, array)

def main():
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    test_cases = []
    
    for _ in range(t):
        n = int(data[index])
        array = list(map(int, data[index+1:index+1+n]))
        test_cases.append((n, array))
        index += n + 1

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(process_test_case, test_cases))
    
    for result in results:
        max_value, division = result
        print(max_value)
        for subarray in division:
            print(subarray)

if __name__ == "__main__":
    main()
