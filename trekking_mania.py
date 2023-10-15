mussala_count = 0
monblan_count = 0
kilimandjaro_count = 0
k2_count = 0
everest_count = 0
num_group = int(input())


for _ in range(num_group):
    num_climbers = int(input())
    if num_climbers < 6:
        mussala_count += num_climbers
    elif num_climbers < 13:
        monblan_count += num_climbers
    elif num_climbers < 26:
        kilimandjaro_count += num_climbers
    elif num_climbers < 41:
        k2_count += num_climbers
    elif num_climbers >= 41:
        everest_count += num_climbers
total_climbers = mussala_count + monblan_count + kilimandjaro_count + k2_count + everest_count
mussala_percent = mussala_count / total_climbers * 100
monblan_percent = monblan_count / total_climbers * 100
kilimandjaro_percent = kilimandjaro_count / total_climbers * 100
k2_percent = k2_count / total_climbers * 100
everest_percent = everest_count / total_climbers * 100

print(f"{mussala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimandjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")


