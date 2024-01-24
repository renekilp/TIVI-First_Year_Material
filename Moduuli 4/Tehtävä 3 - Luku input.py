user_numb = 0
highest_numb = float('-inf')
lowest_numb = float('inf')

while True:
    user_input = input("Syötä luku (tyhjä rivi lopettaa):\n")
    if user_input == "":
        break
    else :
        user_numb = int(user_input)
        if user_numb > highest_numb:
            highest_numb = user_numb
        if user_numb < lowest_numb:
            lowest_numb = user_numb

print(f"Suurin syöttämäsi luku oli:\n{highest_numb}\nja alhaisin luku oli:\n{lowest_numb}")
