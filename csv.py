import csv

with open("zadanie2.csv", newline='') as file:
    reader = csv.reader(file, delimiter=',')
    header = next(reader)

wiersze = []
for row in reader:
    if row[1] != "":
        wiersze.append(row)

wiersze.sort(key=lambda x: int(x[0]) if x[0].isdigit() else -1)


poprzednie_id = None
for row in wiersze:
    obecne_id = int(row[0])
    if poprzednie_id is not None and poprzednie_id >= obecne_id:
        obecne_id = poprzednie_id + 1
        row[0] = str(obecne_id)
        poprzednie_id = obecne_id


for row in wiersze:
        row[1] = row[1].lower()

usuniete_slowa = []
for row in wiersze:
        slowa = row[1].split()
        nowe_slowa = []
        for word in slowa:
            add_word = True
            for i in range(len(word)-1):
                if abs(ord(word[i]) - ord(word[i+1])) == 1:
                    usuniete_slowa.append((row[0], word))
                    add_word = False
                    break
            if add_word:
                nowe_slowa.append(word)
        row[1] = ' '.join(nowe_slowa)

with open('rezultat.csv', mode='w', newline='') as out_file:
    writer = csv.writer(out_file, delimiter=',')
    writer.writerow(header)
    writer.writerows(wiersze)

print("Usunięte wyrazy:")
for word in usuniete_slowa:
    print(f"{word[0]}: {word[1]}")