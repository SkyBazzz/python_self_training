def bubble_sort(dataset: list):
    for i in range(len(dataset) - 1, 0, -1):
        for j in range(i):
            if dataset[i] < dataset[j + 1]:
                temp = dataset[i]
                dataset[i] = dataset[j + 1]
                dataset[j + 1] = temp
        print(f"Current result: {dataset}")


def merge_sort(dataset: list):
    size = len(dataset)
    if size > 1:
        mid = size // 2
        left_arr = dataset[:mid]
        right_arr = dataset[mid:]
        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0
        j = 0
        k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                dataset[k] = left_arr[i]
                i += 1
            else:
                dataset[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            dataset[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            dataset[k] = right_arr[j]
            j += 1
            k += 1


def main():
    numbers = [6, 28, 8, 19, 56, 23, 87, 41, 49, 53]
    print(f"Starting point  {numbers}")
    print("Bubble sort starts")
    bubble_sort(numbers)
    print("Bubble sort finishes")
    print(f"Result:         {numbers}")
    numbers = [6, 28, 8, 19, 56, 23, 87, 41, 49, 53]
    print(f"Starting point  {numbers}")
    print(f"Merge sort starts")
    merge_sort(numbers)
    print("Merge sort finishes")
    print(f"Result:         {numbers}")


if __name__ == "__main__":
    main()
