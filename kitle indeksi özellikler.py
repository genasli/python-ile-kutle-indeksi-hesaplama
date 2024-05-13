kilo = float(input("Kilonuzu giriniz : "))
boy = float(input("Boyunuzu giriniz cm cinsinden gir : "))
mboy = boy / 100
sonuç = kilo / (mboy ** 2)
print("Vücut kitle indeksiniz : {:.2f} kg/m**2".format(sonuç))
if(sonuç < 18,5 ):
    print("İdeal kilonun altındasınız...")
elif(18,5 <= sonuç <= 24,9):
    print("Tebrikler ideal kilodasınız.")
elif(25 <= sonuç <= 29,9):
    print("İdeal kilonun üstesindesiniz")
elif(30 <= sonuç < 39,9):
    print("İdeal kilonun çok üstünde,obezsiniz")
elif(40 <= sonuç):
    print("İdeal kilonun çok çok üstünde, morbid obezsiniz")


    
