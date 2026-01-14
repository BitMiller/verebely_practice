import math
x = input 
szam = float(input("Szia, kérlek, add meg a kör sugarát és én kiszámolom neked a területét és kerületét:" ))
'''
print ("Kerület:"+ str(float(2*szam*math.pi)))
print ("Terület:"+ str(float(szam*math.pi)))
'''

print("Kerület:",end=" ")
print (2*szam*math.pi)
print("Terület:", end=" ")
print (szam*math.pi)

# @GaPe:
# Én ezt így csinálnám:
'''
print ("Kerület: " + str(float(2*szam*math.pi)) + "cm")
print ("Terület: " + str(float(szam*math.pi)) + "cm")
'''
kerulet=2*szam*3.14
print(f'A kör kerülete: {kerulet} cm')

input("Szerenéd, hogy átváltsam másik mértékegységbe?")
