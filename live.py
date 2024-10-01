angka = int(input("angka : "))
temp=1
for i in range(1, angka+1):
    print (str(temp)*(angka))
    temp += 1
    angka-= 1
    
    if angka <= 0:
        print("masukkan angka lebih dari 0")
    
