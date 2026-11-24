weather = (1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1)
sunny = 0
rainy = 0
for i in range(0,15):
    if (weather[i] == 0):
        sunny += 1
    else:
        rainy += 1
        
if (sunny > rainy):
    print("Sunny days are more than rainy days")
else:
    print("Rainy days are more than sunny days")