# Data dictionary berisi username dan password mahasiswa
data_mahasiswa = {
    'riska': '1234',
    'caca': '2345',
    'titin': '3456',
    'nabila': '4567',
    'diva': '5678',
    'nia': '6789',
    'arridoh': '7890',
    'salwan': '8901',
    'hasna': '9012',
    'ilham': '0123'
}

def login_system():
    # Meminta input username dan password dari pengguna
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # Memeriksa apakah username ada dalam data_mahasiswa dan password cocok
    if username in data_mahasiswa and data_mahasiswa[username] == password:
        print("Selamat datang, " + username + "!")
    else:
        print("Data yang dimasukkan salah.")