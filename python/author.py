authors = {"Charles Dickens": "1870", "William Thackeray": "1863", "Anthony Trollope": "1882", "Gerard Manley Hopkins": "1889"}
for author, date in authors.items():
        print(author + " kicked the bucket in " + date)

birth_dates = {
"Maupassant": 1827,
"Voltaire": 1802,
"Beaudelaire": 1844,
"Camus": 1922,
"Levy": 1975,
"Kadra": 1951,
"Pancol": 1982}

nineteenth_c = 0
twentieth_c = 0

for author, date in birth_dates.items():
    if date < 1900:
        nineteenth_c += 1
    else:
        twentieth_c += 1

print("There are " + str(nineteenth_c) + " 19th-c births and " + str(twentieth_c) + " 20th-c births in my collection.")
