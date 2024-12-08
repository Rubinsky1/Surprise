from collections import Counter

def filter_frequent_numbers(input_file, threshold=13):
    try:

        with open(input_file, "r") as file:
            numbers = [int(line.strip()) for line in file if line.strip().isdigit()]

        # Tel de frequentie van elk getal
        frequency = Counter(numbers)

        # Filter de getallen die minder dan of gelijk aan de threshold voorkomen
        filtered_numbers = [num for num in numbers if frequency[num] <= threshold]

        return(filtered_numbers)

    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")

# Gebruik de functie
banaan = filter_frequent_numbers("test.txt")
text = ''.join(chr(value) for value in banaan)
print(text)