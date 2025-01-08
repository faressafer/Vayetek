def extract(file_path):
    somme = 0
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            numbers = [char for char in line if char.isdigit()]
            if len(numbers) == 0:
                continue 
            first = numbers[0]
            last = numbers[-1]
            Nombre = int(first + last)
            print(f"Line: '{line}', Extracted Number: {Nombre}")
            somme += Nombre
    return somme
file_path = "document.txt"
result = extract(file_path)
print("somme sum:", result)
