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
else:
	print('Your weight to hight, your need lose ', round(lose, 1),' KG, than you will be health.')

while True :
	target_BMI = input('Input your BMI target: ')
	target_weight = float(target_BMI)*((float(height)/100)**2)
	target_lose = float(weight)-(float(target_BMI)*((float(height)/100)**2))
	# print(target_lose)

	if target_lose > 0:
		AM = str('-')
	else:
		AM = str('+')

	print('Your target weight will be', round(target_weight, 2), '. You should ', AM, abs(round(target_lose, 2)), 'KG your weight')
	corq = input('input continue(c) or quite(q):')
	if corq == 'q':
		break
	else:
		continue
