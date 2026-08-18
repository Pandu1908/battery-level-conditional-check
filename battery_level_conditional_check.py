battery = int(input("Enter battery percentage: "))

if battery <= 10:
    print("🔴 Critical battery!")
    print("🔌 Connect charger.")
elif battery <= 30:
    print("🟡 Battery is low.")
else:
    print("🟢 Battery level is good.")
