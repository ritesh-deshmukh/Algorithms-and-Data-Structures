# Given an string in roman no format (s)  your task is to convert it to integer .

roman = 'MMMCMCCIV'

dict = {
    'I': 1,
    'II': 2,
    'III': 3,
    'IV': 4,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def convert(roman, dict):
    roman_int = 0
    i = 0
    while i < len(roman):
        value1 = dict[roman[i]]

        if (i+1) < len(roman):
            value2 = dict[roman[i+1]]

            if value1 >= value2:
                roman_int += value1
                i += 1
            else:
                roman_int += value2 - value1
                i += 2
        else:
            roman_int += value1
            i += 1

    return roman_int

print(f"Given roman number: {roman}")
print(f"Roman number in integer: {convert(roman, dict)}")
