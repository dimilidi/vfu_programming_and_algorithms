# 3 зад. В час по физическо възпитание се провежда изпит по бягане. Да се напише програма, която въвежда резултатите на децата от клавиатурата до въвеждане на 0 и извежда най-слабият резултат, най-добрият резултат и на нов ред всички резултати, подредени по големина.

def enter_results():
    results = input("Enter results separated by space (or 0 to finish): ")
    results = results.split()
    return [float(result) for result in results if result != '0']

def find_min_max(results):
    if not results:
        return None, None
    return min(results), max(results)

def print_sorted_results(results):
    sorted_results = sorted(results)
    print("Sorted results:")
    for result in sorted_results:
        print(result, end=' ')
    print()

def main():
    results = enter_results()

    min_result, max_result = find_min_max(results)

    if min_result is not None and max_result is not None:
        print(f"Minimum result: {min_result}")
        print(f"Maximum result: {max_result}")
        print_sorted_results(results)
    else:
        print("No results entered.")


main()
