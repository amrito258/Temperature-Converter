print('''Options:

1. K to C
2. F to C
3. C to F
4. K to F
5. C to K
6. F to K
''')
op_num = input('Enter the option number you have chosen: ')

if '1' in op_num:
  K = float(input('Enter the value of Kelvin(K): '))
  C = K - 273.15
  C = round(C, 2)
  print(f'{K}K = {C}°C')

elif '2' in op_num:
  F = float(input('Enter the value of Fahrenheit(°F): '))
  C = (5 * (F - 32)) / 9
  C = round(C, 2)
  print(f'{F}°F = {C}°C')

elif '3' in op_num:
  C = float(input('Enter the value of Celsius(°C): '))
  F = ((9 * C) / 5) + 32
  F = round(F, 2)
  print(f'{C}°C = {F}°F')

elif '4' in op_num:
  K = float(input('Enter the value of Kelvin(K): '))
  F = (((9 * K) - 2458.35) / 5) + 32
  F = round(F, 2)
  print(f'{K}K = {F}°F')

elif '5' in op_num:
  C = float(input('Enter the value of Celsius(°C): '))
  K = C + 273.15
  K = round(K, 2)
  print(f'{C}°C = {K}K')

elif '6' in op_num:
  F = float(input('Enter the value of Fahrenheit(°F): '))
  K = (((5 * F) - 160) / 9) + 273.15
  K = round(K, 2)
  print(f'{F}°F = {K}K')