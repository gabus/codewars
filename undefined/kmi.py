def bmi_calculator():
    print("Enter your weight in kg:")
    weight = float(input())
    print("Enter your height cm (176) or m (1.76):")
    height = float(input())

    # hint: https://en.wikipedia.org/wiki/Robert_Wadlow
    if height >= 2.72:
        height = height / 100

    # weight - kg, height - m
    kmi = round(weight / height ** 2)

    if kmi < 18.5:
        return 'Underweight'
    elif 18.5 <= kmi < 25:
        return "Normal"
    elif 25 <= kmi < 30:
        return "Overweight"
    else:
        return "Obesity"
        
        
kmii = bmi_calculator()
print(kmii)

