def toplama(x, y):
   return x + y

 
def cikarma(x, y):
   return x - y


def carpma(x, y):
   return x * y


def bolme(x, y):
   return x / y

def kalan(x, y):
   return x % y

print("Islem sec.")
print("1.toplama")
print("2.cikarma")
print("3.carpma")
print("4.bolme")
print("5.kalan")


choice = input("secim yap(1/2/3/4/5):")

num1 = int(input("Ilk sayiyi giriniz: "))
num2 = int(input("Ikinci sayiyi giriniz: "))

if choice == '1':
   print(num1,"+",num2,"=", toplama(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", cikarma(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", carpma(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", bolme(num1,num2))

elif choice == '5':
   print(num1,"%",num2,"=", kalan(num1,num2))
else:
   print("Hatali giris")
