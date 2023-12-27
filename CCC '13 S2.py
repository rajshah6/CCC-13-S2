totalWeight = int(input())
carsOnBridge = []
cars = 0
ans = 0

for _ in range(int(input())):
    car = int(input())
    carsOnBridge.append(car)
    weight = sum(carsOnBridge)

    if weight > totalWeight:
        break

    cars += 1
    ans += 1

    if cars == 4:
        del carsOnBridge[0]
        cars -= 1

print(ans)
