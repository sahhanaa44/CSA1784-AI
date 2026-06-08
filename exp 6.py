rooms = {
    'A': input("Enter status of Room A (Clean/Dirty): "),
    'B': input("Enter status of Room B (Clean/Dirty): ")
}

location = 'A'

while True:
    if rooms[location] == "Dirty":
        print("Cleaning Room", location)
        rooms[location] = "Clean"

    if location == 'A':
        location = 'B'
    else:
        break

print("\nFinal Status:")
print(rooms)
