# Data dictionary berisi username dan password mahasiswa
data_mahasiswa = {
    'riska': '1234',
    'titin': '2345',
    'nabila': '3456',
    'diva': '4567',
    'caca': '5678',
    'maulidia': '6789',
    'nia': '7890',
    'acha': '8901',
    'lia': '9012',
    'serli': '0123'
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


# Menjalankan sistem login
if __name__ == "__main__":
    login_system()
