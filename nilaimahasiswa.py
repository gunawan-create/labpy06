daftar_mahasiswa = []

def tambah(nama, nilai):
    """Fungsi untuk menambah data mahasiswa."""
    mahasiswa = {'nama': nama, 'nilai': nilai}
    daftar_mahasiswa.append(mahasiswa)
    print(f"Data {nama} berhasil ditambahkan.")

def tampilkan():
    """Fungsi untuk menampilkan daftar mahasiswa."""
    print("\nDaftar Mahasiswa:")
    if not daftar_mahasiswa:
        print("Belum ada data mahasiswa.")
    else:
        for n in daftar_mahasiswa:
            print(f"Nama: {n['nama']}, Nilai: {n['nilai']}")

def hapus(nama):
    """Fungsi untuk menghapus data mahasiswa berdasarkan nama."""
    global daftar_mahasiswa
    daftar_mahasiswa = [n for n in daftar_mahasiswa if n['nama'] != nama]
    print(f"Data {nama} berhasil dihapus.")

def ubah(nama, nilai_baru):
    """Fungsi untuk mengubah data mahasiswa berdasarkan nama."""
    for n in daftar_mahasiswa:
        if n['nama'] == nama:
            n['nilai'] = nilai_baru
            print(f"Data {nama} berhasil diubah menjadi nilai {nilai_baru}.")
            return
    print(f"Data {nama} tidak ditemukan.")

def main():
    while True:
        print("\nMenu:")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Hapus Data Mahasiswa")
        print("4. Ubah Data Mahasiswa")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            nama = input("Masukkan nama mahasiswa: ")
            nilai = input("Masukkan nilai mahasiswa: ")
            tambah(nama, nilai)
        
        elif pilihan == '2':
            tampilkan()
        
        elif pilihan == '3':
            nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
            hapus(nama)
        
        elif pilihan == '4':
            nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
            nilai_baru = input("Masukkan nilai baru: ")
            ubah(nama, nilai_baru)
        
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

if __name__ == "__main__":
    main()