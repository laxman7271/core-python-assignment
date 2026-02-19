def fare(km):
    return 50 + km * 10
trips = [5, 10, 3]
total = 0

for i in range(3):
    f = fare(trips[i])
    total += f
    print("Trip", i+1, ": $"+str(f))
print("Total Fare: $"+str(total))