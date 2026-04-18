#رساله ترحيبيه 
print("| Gymbot V1.2 |")
print()
print()

#اسم المستخدم 
name = input("Name : ")
print()
print("Welcome to your Gymbot," + name.capitalize() + ".")

#عمر المستخدم 
print()
age = int(input("Age : "))
print()

#السؤال عن مدة التدريب
exp = int(input("How long have you been training (1 if less than a year,2 if 1-3 years,3 if from 3-6 years,4 if more than 6 years) : "))
print()

#معالجة مدة التمرين 
if exp == 1 :
    print("You are begginer,You still have many things to know.")
    rank = "Begginer"
elif exp == 2 :
    print("You are intermediate,You are trianing so hard!")
    rank = "Intermediate"
elif exp == 3 :
    print("You are expert,You are from the top tier!")
    rank = "Expert"
elif exp == 4 :
    print("You are one of the human beasts,eatin' food and weights!")
    rank = "Human beast"
else :
    print("Invalid input")
    
#شكل جمالي 
print()
print("| --------------------------------------------------------------------- |")
print()
    
#وزن المستخدم
weight = float(input("Weight in KG : "))
weight_lbs = round(weight * 2.204 , 1)
print()
print("Your Weight in lbs is " + str(weight_lbs) + "lbs ")

#طول المستخدم
print()
height = int(input("Height : "))
height_feet = round(height / 30.84 , 1)
print()
print("Your height in feet = " + str(height_feet))

#حساب معدل الايض 
BMR = (weight * 10) + (6.25 * height) - (5 * age) + 5

#درجة نشاط المستخدم
print()
act = int(input("Enter your weekly workout session number(use numbers from 1-7) : "))

#معالجة البيانات
if act >= 1 and act <= 3 :
    BMR_Factor = 1.375
elif act >= 4 and act <=5 :
    BMR_Factor = 1.55
elif act >= 6 and act <= 7 :
    BMR_Factor = 1.725
else :
    print("Invalid input")

#حساب معدل الحرق اليومي
TDEE = round(BMR_Factor * BMR , 2)

#شكل جمالي 
print()
print("| --------------------------------------------------------------------- |")
print()

#احتياج الماكروز اليومي
print("Your daily nesscisty of calories is : " + str(TDEE) )
print()
print("Your daily nesscisty of protien is : " + str(weight * 1.6) + "gm" + " - " + str(weight * 2.2) + "gm")
print()
print("Your daily nesscisty of carbs is : " + str(weight * 4) + "gm")
print()
print("Your daily nesscisty of fat is : " + str(weight) + "gm")

#رساله ختاميه 
print()
print()
print("Thank you for using Gymbot V1.2 ," + name.capitalize() + ".")