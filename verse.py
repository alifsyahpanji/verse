import os

def load_lyrics_from_folder(folder_path):
    """Memuat semua lirik lagu dari folder."""
    lyrics_data = {}
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            with open(os.path.join(folder_path, file_name), 'r', encoding='utf-8') as file:
                lyrics_data[file_name] = file.read().lower()
    return lyrics_data

def check_verse(input_verse, lyrics_data):
    """Mengecek apakah lirik input ada di dalam data lirik lagu."""
    for file_name, lyrics in lyrics_data.items():
        if input_verse in lyrics:
            return f"Lirik ini tidak bisa digunakan, karena ada pada lagu {file_name}"
    return "Lirik ini bisa digunakan"

def main():
    print("Selamat datang di Aplikasi Verse Lagu Checker")

    # Tentukan jalur folder lirik
    folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lirik")
    print(f"Folder lirik seharusnya berada di: {folder_path}")
    
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' tidak ditemukan. Pastikan foldernya ada.")
        return

    lyrics_data = load_lyrics_from_folder(folder_path)

    while True:
        print("\nPilih opsi:")
        print("1. Mulai cek verse lagu")
        print("2. Keluar atau Tutup Aplikasi")

        choice = input("Masukkan pilihan Anda: ")
        if choice == "1":
            input_verse = input("Masukkan lirik lagu yang ingin dicek: ").strip().lower()
            if not input_verse:
                print("Lirik tidak boleh kosong. Silakan coba lagi.")
                continue

            result = check_verse(input_verse, lyrics_data)
            print(result)
        elif choice == "2":
            print("Terima kasih telah menggunakan Aplikasi Verse Lagu Checker. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
    input("Tekan Enter untuk keluar...")
