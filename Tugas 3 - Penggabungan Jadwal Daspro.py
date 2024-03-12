# Data Dictionary Jadwal Daspro IF2
jadwal_if2 = {
    "Selasa": "Jam 08:00",
    "Rabu": ["10:50", "15:00"]
}

# Data Dictionary Jadwal Daspro IF3
jadwal_if3 = {
    "Senin": "08:00",
    "Kamis": "10:50",
    "Jumat": "08:00"
}

# Menggabungkan kedua data dictionary
jadwal_gabungan = jadwal_if3.copy()
for hari, jam in jadwal_if2.items():
    if hari in jadwal_gabungan:
        if isinstance(jadwal_gabungan[hari], list):
            jadwal_gabungan[hari].extend(jam)
        else:
            jadwal_gabungan[hari] = [jadwal_gabungan[hari], jam]
    else:
        jadwal_gabungan[hari] = jam

print(jadwal_gabungan)