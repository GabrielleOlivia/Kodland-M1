meme_dict = {
    "CRINGE": "sesuatu yang aneh atau memalukan",
    "LOL": "tanggapan terhadap sesuatu yang lucu",
    "ROLF": "tanggapan terhadap lelucon",
    "SHEESH": "sedikit ketidaksetujuan",
    "CREEPY": "menakutkan, tidak menyenangkan",
    "AGGRO": "untuk menjadi agresif/marah"
}
while True:
    word = input("Kata apa yang gak tidak dimengerti?(tulis all caps): ")

    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Maaf kata ini tidak ada di kamus kami atau coba dengan penulisan yang benar.")
