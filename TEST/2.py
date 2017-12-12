count = 0
with open("lang.tsv", encoding="utf-8") as f:
    lines = f.readlines()
for line in lines:
    line = line.split('\t')
    if "Critically endangered" in line[2]:
        count += 1
print("число языков -", count)
