count = 0
total_age = 0
while True:
    age = int(input())
    if age >= 20 and age < 30:
        count += 1
        total_age += age
    else:
        break

print(f"{(total_age/count):.2f}")
    
    