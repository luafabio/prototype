def main():
    filename = 'input'
    target_sum = 2020

    my_array = read_file_to_array(filename)
    result = find_three_with_sum(my_array, target_sum)
    print(result)


def find_three_with_sum(my_array, target_sum):
    for i in range(len(my_array)):
        for j in range(i + 1, len(my_array)):
            for k in range(j + 1, len(my_array)):
                if my_array[i] + my_array[j] + my_array[k]== target_sum:
                    return my_array[i] * my_array[j] * my_array[k]

def read_file_to_array(filename):
    my_array = []
    with open(filename, 'r') as file:
        for line in file:
            my_array.append(int(line.strip()))
    return my_array

if __name__ == "__main__":
    main()
