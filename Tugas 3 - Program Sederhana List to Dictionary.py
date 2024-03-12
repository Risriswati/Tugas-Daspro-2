def lists_to_dict(keys, values):
    if len(keys) != len(values):
        raise ValueError("Panjang kedua list harus sama")

    result_dict = {}
    for i in range(len(keys)):
        result_dict[keys[i]] = values[i]
    
    return result_dict

# Contoh penggunaan
list_kunci = ["Nama", "Usia", "Kota"]
list_nilai = ["Riska", 21, "Ternate"]

hasil_dict = lists_to_dict(list_kunci, list_nilai)
print(hasil_dict)