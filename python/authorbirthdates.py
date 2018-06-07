birth_dates = {
    "Tom Hanks": 1864,
    "Steven Spielberg": 1923,
    "Mark Twain": 1857,
    "Kirk Douglas": 1944,
    "Sia": 1932,
    "Oscar the Grouch": 1922,
    "Elmo": 1832,
    }

nineteenth_count = 0
twentieth_count = 0

for person, birthdate in birth_dates.items():
    if birthdate < 1900:
        nineteenth_count += 1
    if birthdate > 1900:
        twentieth_count += 1

print("There are " + str(nineteenth_count) + " 19th c. births and " + str(twentieth_count) + " 20th c. births in my collection.")
