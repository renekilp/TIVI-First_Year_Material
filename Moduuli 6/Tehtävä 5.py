def get_even_numbers(numbers):
    even_numbers = []           # uusi tyhjä lista
    for i in range(len(numbers)-1):     # for num in numbers:
        if numbers[i] % 2 == 0:         #   if num % 2 == 0
            even_numbers.append(numbers[i])         # lisää uuteen listaan
    return even_numbers


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 1, 3, 5]
even_numbers = get_even_numbers(numbers)
print(f"Alkuperäiset luvut:\n{numbers}\nParilliset luvut:\n{even_numbers}")