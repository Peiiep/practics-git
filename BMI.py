# BMI calculate

height = input('Input your height (cm): ')
weight = input('Input your weight (KG): ')
BMI = float(weight) /(float(height)/100)**2
print('Your BMI will be', format(BMI, '.2f'))
lose = float(weight)-(23.99*((float(height)/100)**2))

if BMI < 18.6:
	print('Weight to light')
elif BMI < 24:
	print('Normal weight, keep going.')
else :
	print('Your weight to hight, your need lose ', format(lose, '.1f'),' KG, than you will be health.')