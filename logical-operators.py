# LOGICAL OPERATORS (and, or) = used to check if 2 or more conditional statements are trew
temp = float(input('What is the temperature outside?: '))
if temp >= 0 and temp <= 15:
    print('going frozen yarn pota')
elif temp >= 16 and temp <= 29:
    print('wow baguio yern???')
elif temp >= 30 and temp <= 40:
    print('welcome to the philippines!')
elif temp <= -50 or temp >= 41:
    print('TEH DEDS NA TAYO NYAN???')
elif not (temp >0): #ginawa ko lang greater than 0 para may example yung NOT hehe
    print('paranas naman ng snow bhie')
else: #LAGAY KO LANG KAHIT DI NAMAN MAGAGAMIT HEHEHE
    print('inEt pa rin dto samin')
    print('yaw q na here')