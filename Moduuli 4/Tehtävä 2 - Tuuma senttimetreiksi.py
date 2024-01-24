inch = 2.54
inch_input = 0

while inch_input >= 0 :
    inch_input = float(input("Syötä haluamasi tuumien määrä:\n"))
    print(f"Tuumien määrä senttimetreinä on {inch_input * inch} cm")

