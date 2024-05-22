import sys
import concurrent.futures

def calculate_max_cypriot_value(n, array):
    max_cypriot_value = sum((i + 1) * array[i] for i in range(n))

    # Dividir el array en subarrays de forma apropiada
    division = []
    subarray = [array[0]]
    current_sum = array[0]
    for i in range(1, n):
        if current_sum + array[i] >= 0:
            subarray.append(array[i])
            current_sum += array[i]
        else:
            division.append(subarray)
            subarray = [array[i]]
            current_sum = array[i]
    division.append(subarray)

    return max_cypriot_value, division

def process_test_case(test_case):
    n, array = test_case
    return calculate_max_cypriot_value(n, array)

def main():
    input_data = sys.stdin.read().strip().split('\n')
    t = int(input_data[0])
    test_cases = []
    index = 1
    
    for _ in range(t):
        n = int(input_data[index])
        array = list(map(int, input_data[index+1].split()))
        test_cases.append((n, array))
        index += 2

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(process_test_case, test_cases))

    for max_value, division in results:
        print("División del array:")
        for subarray in division:
            print(subarray)
        print("Sumas parciales de cada subarray:")
        for i, subarray in enumerate(division):
            subarray_sum = sum(subarray)
            weighted_sum = (i + 1) * subarray_sum
            print(f"Subarray {i + 1}: {subarray} suma: {subarray_sum}, suma ponderada: {weighted_sum}")
        print("Resultado:")
        print(max_value)
        print()  # Separador de casos de prueba

if __name__ == "__main__":
    main()

