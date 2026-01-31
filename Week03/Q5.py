from itertools import count

contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}
print(contacts["Alice"])
contacts["Diana"] = "555-4321"
contacts.update({"Bob": "555-0000"})
del contacts["Charlie"]
print(contacts.keys())
print(contacts.values())
print(len(contacts))

