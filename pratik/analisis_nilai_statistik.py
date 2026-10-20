
# Program Praktik: Analisis Nilai Mahasiswa
# Input: List nilai mahasiswa
# Proses: Menghitung statistik dan menentukan kelulusan
# Output: Ringkasan data nilai mahasiswa

def rata_rata(data):
    """Menghitung rata-rata data."""
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    """Mengembalikan list nilai yang memenuhi batas kelulusan."""
    hasil = []

    for x in data:
        if x >= batas:
            hasil.append(x)

    return hasil


# Data nilai mahasiswa
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Mengolah data
banyak = len(nilai)
total = sum(nilai)
rata = rata_rata(nilai)
minimum = min(nilai) if banyak > 0 else 0
maksimum = max(nilai) if banyak > 0 else 0

lulus = nilai_lulus(nilai)
jumlah_lulus = len(lulus)
belum_lulus = banyak - jumlah_lulus

# Menampilkan hasil
print("=== ANALISIS NILAI MAHASISWA ===")
print("Data nilai      :", nilai)
print("Banyak data     :", banyak)
print("Total nilai     :", total)
print(f"Rata-rata       : {rata:.2f}")
print("Nilai minimum   :", minimum)
print("Nilai maksimum  :", maksimum)
print("Nilai lulus     :", lulus)
print("Jumlah lulus    :", jumlah_lulus)
print("Belum lulus     :", belum_lulus)
