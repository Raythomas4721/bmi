print('Please tell me what is your weight and height:')
w = input('Your weight in kg is:')
h = input('Your height in meter is:')
w = float(w)
h = float(h)
bmi = w / h / h
print('Your BMI is:' ,bmi)
if bmi < 18.5:
    print('Skinny')
elif bmi >= 18.5 and bmi < 24:
    print('Normal')
elif bmi >= 24 and bmi < 27:
    print('Slightly heavier')
elif bmi >= 27 and bmi < 30:
    print('Mild obesity')
elif bmi >= 30 and bmi < 35:
    print('Moderate obesity')
elif bmi >= 35: # 寫else: 也可以
    print('Severe obesity')