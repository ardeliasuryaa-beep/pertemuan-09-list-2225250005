
# Latihan 5: Filter Kelulusan
# Batas kelulusan adalah 60

nilai = [75, 55, 80, 60, 45, 90]
lulus = []

for x in nilai:
    if x >= 60:
        lulus.append(x)

print("Nilai lulus:", lulus)
print("Jumlah lulus:", len(lulus))
