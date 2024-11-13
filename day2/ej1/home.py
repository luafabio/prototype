import re

def main():
    filename = '/Users/lfabio/Workspace/python/prototype/day2/ej1/input'

    my_array = read_file_to_array(filename)
    result = exercise(my_array)
    print(result)

def read_file_to_array(filename):
    my_array = []
    pattern = re.compile(r'(\d+)-(\d+) (\w): (\w+)')
    with open(filename, 'r') as file:
        for line in file:
            match = pattern.match(line.strip())
            if match:
                min_val = int(match.group(1))
                max_val = int(match.group(2))
                char = match.group(3)
                password = match.group(4)
                my_array.append((min_val, max_val, char,password))
    return my_array

def exercise(my_array):
    valid_passwords = 0
    for min_val, max_val, char, password in my_array:
        count = password.count(char)
        if min_val <= count <= max_val:
                valid_passwords += 1
    return valid_passwords


if __name__ == "__main__":
    main()
