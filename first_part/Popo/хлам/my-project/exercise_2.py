#  Программа вирахування площі прямокутного трикутника та гіпотенузи коли відомі його катети 
print("Вітаю друже ця программа допоможе тобі дізнатися площу та гіпотенузу прямокутного трикутника знаючи його катети")
while True:

 catet_1 = float(input("Enter lenght of the legs,Введи перший катет :"))
 catet_2 = float(input("Enter length of the legs,Введи другий катет :"))
 area_triangles = (catet_1 * catet_2) / 2
 gipotenusa_triangles = (catet_1 ** 2 + catet_2 ** 2 )* 0.5

 print(f"Площа трикутника дорівнює:{area_triangles}сантиметри")
 print(f"Гіпотенуза прямокутника дорівнює: {gipotenusa_triangles}сантиментри")