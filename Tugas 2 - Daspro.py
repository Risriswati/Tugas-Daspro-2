nama = input('Masukan nama Anda: ')
hari_kerja = int(input('Masukkan kehadiran: '))

hari_kerja_perbulan = 20
gaji_hari_kerja_perbulan = 5000000

jam_lembur = 5
upah_perjam_lembur = 10000

total_gaji_perbulan = hari_kerja / hari_kerja_perbulan + gaji_hari_kerja_perbulan
gaji_lembur = upah_perjam_lembur + jam_lembur

print("Total Keseluruhan Pendapatan anda adalah Rp.", total_gaji_perbulan + gaji_lembur)