# 19. If you were on the moon now, your weight will be 16,5% of your earth weight.
# To calculate it you have to multiple to 0,165.
# If next 15 years your weight will increase 1 kg each year.
# What will be your weight each year  on the moon next 15 years?


earth_weight = int(input("Enter You weight in kg: "))
moon_weight = earth_weight * 0.165
next15years = (earth_weight + 15) * 0.165
print("On the moon next 15 years, Your weight will: " + str(next15years) + " kg")