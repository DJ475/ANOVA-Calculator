import numpy as np

# Author: Djibril Sylla
# One-Way ANOVA Calculator

dictData = {
        "White Collar":[3250,2700,2125,3534,1870,2900,2430,2580,4050,2640],
        "Blue Collar":[5890,7100,4820,6600,6540,6825,6244,7780,3450,4100],
        "Unemployed":[2660,3890,2450,2322,4550,1790,2150,2275,2980]
    }

sumWhite = 0
sumBlue = 0
sumUnemployed = 0

SSWWhite = 0
SSWBlue = 0
SSWUnemployed = 0

counteraSampleData = 0

for k,v in dictData.items():
    for i in v:
        if k == "White Collar":
            sumWhite+=i
            SSWWhite+=np.power(i-2807.9,2)
            # print("(" + str(i) + " - " + str(2807.9) + ")^2 = " + str((i-2807.9)) + "^2 -> " + str(np.power(i-2807.9,2)))
        if k == "Blue Collar":
            sumBlue+=i
            SSWBlue+=np.power(i-5934.9,2)
            # print("(" + str(i) + " - " + str(5934.9) + ")^2 = " + str((i-5934.9)) + "^2 -> " + str(np.power(i-5934.9,2)))
        if k == "Unemployed":
            sumUnemployed+=i
            SSWUnemployed+=np.power(i-2785.22222222,2)
            # print("(" + str(i) + " - " + str(2785.22222222) + ")^2 = " + str((i-2785.22222222)) + "^2 -> " + str(np.power(i-2785.22222222,2)))
        counteraSampleData+=1
            
    print(f"Key: {k} :::: " + f"Value: {v}")
    
totalMean = (sumWhite+sumBlue+sumUnemployed) / counteraSampleData # all sums of all groups / 29 total samples
    
print("\n")
print("Total white collar is: " + str(sumWhite))
print("Total blue collar is: " + str(sumBlue))
print("Total unemployed is: " + str(sumUnemployed) + "\n")


print("Total mean " + str(totalMean) + "\n")

print("SSW White Collar: " + str(SSWWhite))
print("SSW Blue Collar: " + str(SSWBlue))
print("SSW Unemployed: " + str(SSWUnemployed))

print("Total SSW: " + str(SSWWhite + SSWBlue + SSWUnemployed))