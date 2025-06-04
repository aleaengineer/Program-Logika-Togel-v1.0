# -*- coding: utf-8 -*-
"""
Program untuk menghitung serangkaian angka berdasarkan logika tertentu
dari input angka pengguna.
"""
from typing import List, Union, Tuple

def _jumlahkan_digit_dalam_string(angka_str: str) -> int:
    """
    Fungsi bantuan untuk menjumlahkan semua digit dalam sebuah string.
    Contoh: "123" -> 1 + 2 + 3 = 6
    """
    return sum(int(digit) for digit in angka_str)

def hitung_angka_dengan_rincian_v2(input_angka: str) -> Union[List[int], str]:
    """
    Menghitung serangkaian angka berdasarkan input angka pengguna dengan logika tertentu.

    Args:
        input_angka (str): String yang berisi digit-digit angka (misal: "2345").

    Returns:
        Union[List[int], str]: Sebuah list berisi 7 angka hasil perhitungan,
                               atau pesan error jika input tidak valid.
    
    Logika Perhitungan:
    1. Validasi input: harus berupa string digit.
    2. Hitung `total_awal`: jumlah semua digit dari `input_angka`.
    3. Hitung `patokan`: jumlah semua digit dari `total_awal`.
    4. `angka_a` = (`patokan` + 1) % 10
    5. `angka_b` = (`patokan` + 2) % 10
    6. `angka_d` = (`angka_a` - 3) % 10  (wrap-around jika negatif)
    7. `angka_c` = (`angka_d` - 1) % 10  (wrap-around jika negatif)
    8. `angka_e` = (`angka_b` + 3) % 10
    9. `angka_f` = (`angka_e` + 1) % 10
    10. Hasil akhir adalah list: [`patokan`, `angka_a`, `angka_b`, `angka_c`, `angka_d`, `angka_e`, `angka_f`]
    """
    # 1. Pastikan input berupa string digit
    if not input_angka.isdigit():
        return "Input harus berupa angka saja (hanya digit 0-9)."

    # 2. Jumlahkan semua digit dari input untuk mendapatkan total_awal
    total_awal: int = _jumlahkan_digit_dalam_string(input_angka)

    # 3. Jumlahkan digit dari total_awal untuk mendapatkan patokan
    #    Ubah total_awal (int) ke string dulu untuk bisa diiterasi digitnya
    patokan: int = _jumlahkan_digit_dalam_string(str(total_awal))

    # 4. Ambil dua angka setelah patokan (dalam rentang 0–9 dengan wrap-around)
    #    Saya mengganti nama variabel angka6 -> angka_a, angka7 -> angka_b dst.
    #    agar lebih generik dan tidak terikat pada nomor urut yang mungkin membingungkan
    #    jika urutan di hasil akhir berbeda.
    angka_a: int = (patokan + 1) % 10
    angka_b: int = (patokan + 2) % 10

    # 5. Proses angka_a: kurangi 3, lalu kurangi 1 (dengan wrap-around jika < 0)
    #    angka4 -> angka_d
    #    angka3 -> angka_c
    angka_d: int = (angka_a - 3) % 10 
    angka_c: int = (angka_d - 1) % 10

    # 6. Proses angka_b: tambah 3, lalu tambah 1 (dengan wrap-around jika > 9)
    #    angka5 -> angka_e
    #    angka6_akhir -> angka_f
    angka_e: int = (angka_b + 3) % 10
    angka_f: int = (angka_e + 1) % 10

    # 7. Hasil akhir diurutkan sesuai permintaan awal:
    #    patokan, angka_a (dulu angka6), angka_b (dulu angka7), 
    #    angka_c (dulu angka3), angka_d (dulu angka4), 
    #    angka_e (dulu angka5), angka_f (dulu angka6_akhir)
    hasil_perhitungan: List[int] = [
        patokan, 
        angka_a, 
        angka_b, 
        angka_c, 
        angka_d, 
        angka_e, 
        angka_f
    ]
    
    return hasil_perhitungan

# Program utama
if __name__ == "__main__":
    print("=" * 40)
    print("    Program Logika Togel (v1.0)")
    print("BY : Aleaxl | Github : aleaengineer")
    print("=" * 40)
    
    while True:
        input_user: str = input("Masukkan angka (contoh: 2345 atau 54321): ").strip()
        
        if not input_user:
            print("Input tidak boleh kosong. Silakan coba lagi.")
            continue

        hasil: Union[List[int], str] = hitung_angka_dengan_rincian_v2(input_user)

        if isinstance(hasil, str):
            # Ini berarti ada pesan error yang dikembalikan
            print(f"Error: {hasil}")
            # Tanya apakah mau coba lagi
            ulangi = input("Apakah Anda ingin mencoba lagi? (y/n): ").strip().lower()
            if ulangi != 'y':
                break
        else:
            # Hasil adalah List[int]
            print(f"\nInput Angka: {input_user}")
            print(f"Hasil Perhitungan: {hasil}")
            
            # Memberikan rincian jika diperlukan (opsional, bisa di-uncomment)
            # print("\nRincian Variabel Internal (untuk debugging/pemahaman):")
            # total_awal_debug = _jumlahkan_digit_dalam_string(input_user)
            # patokan_debug = _jumlahkan_digit_dalam_string(str(total_awal_debug))
            # print(f"  - Total Awal (jumlah digit input): {total_awal_debug}")
            # print(f"  - Patokan (jumlah digit dari Total Awal): {patokan_debug} -> ini angka ke-1")
            # print(f"  - Angka ke-2 (patokan + 1): {hasil[1]}")
            # print(f"  - Angka ke-3 (patokan + 2): {hasil[2]}")
            # print(f"  - Angka ke-5 (Angka ke-2 - 3): {hasil[4]}")
            # print(f"  - Angka ke-4 (Angka ke-5 - 1): {hasil[3]}")
            # print(f"  - Angka ke-6 (Angka ke-3 + 3): {hasil[5]}")
            # print(f"  - Angka ke-7 (Angka ke-6 + 1): {hasil[6]}")
            
            ulangi = input("\nApakah Anda ingin menghitung angka lain? (y/n): ").strip().lower()
            if ulangi != 'y':
                break
        print("-" * 40) # Pemisah antar percobaan

    print("\nTerima kasih. Utamakan prediksi anda!")
