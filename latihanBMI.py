tinggi_badan = float(input("masukkan tinggi badan(dalam meter): "))
berat_badan = float(input("masukkan berat badan(dalam kg): "))

BMI = berat_badan / tinggi_badan**2 

if BMI < 23.9:
    print("anda termasuk normal")
elif BMI >= 24:
    print("anda termasuk overweight")
else:
    print("anda anomali")





