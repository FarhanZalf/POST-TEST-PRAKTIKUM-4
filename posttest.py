class main:
    """Kelas utama yang berfungsi sebagai controller untuk alur aplikasi."""
    def __init__(self):
        """Constructor untuk kelas main."""
        pass

    def main(self):
        """Metode utama untuk menjalankan aplikasi."""
        pass

    def uiLogin(self):
        """Menampilkan antarmuka untuk login pengguna."""
        pass

    def uiMenu(self):
        """Menampilkan menu utama aplikasi."""
        pass

    def uiHitungPembayaran(self):
        """Menampilkan antarmuka untuk proses perhitungan pembayaran."""
        pass

    def uiCetakStruk(self):
        """Menampilkan antarmuka untuk mencetak struk."""
        pass


class HitungPembayaran:
    """Mewakili satu item dalam transaksi, menghitung subtotal."""
    def __init__(self, idMenu: str = "", namaMenu: str = "", harga: float = 0.0, jumlah: int = 0):
        self.idMenu = idMenu
        self.namaMenu = namaMenu
        self.harga = harga
        self.jumlah = jumlah
        self.totalHarga = self.harga * self.jumlah

    def insertPembayaran(self):
        """Menyisipkan data pembayaran baru (misalnya ke database)."""
        pass

    def updatePembayaran(self):
        """Memperbarui data pembayaran yang ada."""
        pass

    def deleteDataPembayaran(self):
        """Menghapus data pembayaran."""
        pass

    def cariDataPembayaranByIdMenu(self):
        """Mencari data pembayaran berdasarkan ID menu."""
        pass


class PembayaranTunai:
    """Mengelola logika untuk proses pembayaran tunai."""
    def __init__(self):
        """Constructor untuk kelas PembayaranTunai."""
        pass

    def hitungTotalHarga(self):
        """Menghitung total harga untuk pembayaran tunai."""
        pass


class PembayaranByCard:
    """Mengelola logika untuk proses pembayaran dengan kartu."""
    def __init__(self):
        """Constructor untuk kelas PembayaranByCard."""
        pass

    def hitungTotalHarga(self, total_belanja: float) -> float:
        """Menghitung total harga untuk pembayaran kartu, dengan biaya admin 1.5%."""
        biaya_admin = total_belanja * 0.015
        total_akhir = total_belanja + biaya_admin
        print(f"Biaya Admin (1.5%): Rp {biaya_admin:,.2f}")
        return total_akhir


class CetakStruk:
    """Bertanggung jawab untuk memformat dan mencetak struk."""
    def __init__(self):
        """Constructor untuk kelas CetakStruk."""
        pass

    def cetakStruk(self, data_struk):
        """Mencetak detail struk berdasarkan data yang diberikan."""
        print("--- Struk Pembayaran ---")
        print(f"No. Struk: {data_struk.noStruk}")
        print(f"Total Harga: Rp {data_struk.totalHarga}")
        print("Terima kasih!")
        print("-" * 20)


class TCetakStruk:
    """Model data yang menyimpan informasi final untuk dicetak pada struk."""
    def __init__(self, noStruk: str = "", totalHarga: float = 0.0):
        self.noStruk = noStruk
        self.totalHarga = totalHarga


class LoginKasir:
    """Mengelola data dan validasi untuk login kasir."""
    def __init__(self, username: str = "", password: str = ""):    
        self.username = username
        self.password = password

    def validasiLogin(self):
        """Memvalidasi kredensial pengguna."""
        return self.username == "admin" and self.password == "12345"

    def logout(self):
        """Melakukan proses logout."""
        pass


class KoneksiDatabase:
    """Mengelola koneksi dan eksekusi query ke database."""
    def __init__(self, host: str = "", database: str = "", userName: str = "", password: str = ""):
        self.host = host
        self.database = database
        self.userName = userName
        self.password = password

    def membukaKoneksi(self):
        """Membuka koneksi ke database."""
        pass

    def eksekusiQuerySelect(self):
        """Mengeksekusi query SELECT."""
        pass

    def eksekusiQueryInsert(self):
        """Mengeksekusi query INSERT."""
        pass

    def eksekusiQueryUpdate(self):
        """Mengeksekusi query UPDATE."""
        pass

    def eksekusiQueryDelete(self):
        """Mengeksekusi query DELETE."""
        pass

    def tutupKoneksi(self):
        """Menutup koneksi database."""
        pass


class TabelHitungPembayaran:
    """Model data dengan getter/setter untuk data item pembayaran."""
    def __init__(self, idMenu: str = "", namaMenu: str = "", harga: float = 0.0, jumlah: int = 0):
        self._idMenu = idMenu
        self._namaMenu = namaMenu
        self._harga = harga
        self._jumlah = jumlah
        self._totalHarga = self._harga * self._jumlah

    def setIdMenu(self, idMenu: str):
        self._idMenu = idMenu

    def getIdMenu(self) -> str:
        return self._idMenu

    def setNamaMenu(self, namaMenu: str):
        self._namaMenu = namaMenu

    def getNamaMenu(self) -> str:
        return self._namaMenu

    def setHarga(self, harga: float):
        self._harga = harga

    def getHarga(self) -> float:
        return self._harga

    def setJumlah(self, jumlah: int):
        self._jumlah = jumlah

    def getJumlah(self) -> int:
        return self._jumlah

    def setTotalHarga(self, totalHarga: float):
        self._totalHarga = totalHarga

    def getTotalHarga(self) -> float:
        self._totalHarga = self._harga * self._jumlah
        return self._totalHarga


class TabelPembayaranByCard:
    """Model data dengan getter/setter untuk detail pembayaran via kartu."""
    def __init__(self, idCard: str = "", jenisCard: str = "", namaBank: str = "", totalHarga: float = 0.0):
        self._idCard = idCard
        self._jenisCard = jenisCard
        self._namaBank = namaBank
        self._totalHarga = totalHarga

    def setIdCard(self, idCard: str):
        self._idCard = idCard

    def getIdCard(self) -> str:
        return self._idCard

    def setJenisCard(self, jenisCard: str):
        self._jenisCard = jenisCard

    def getJenisCard(self) -> str:
        return self._jenisCard

    def setNamaBank(self, namaBank: str):
        self._namaBank = namaBank

    def getNamaBank(self) -> str:
        return self._namaBank

    def setTotalHarga(self, totalHarga: float):
        self._totalHarga = totalHarga

    def getTotalHarga(self) -> float:
        return self._totalHarga


if __name__ == "__main__":
    # 1. Login
    login_attempt = LoginKasir("admin", "12345")
    if login_attempt.validasiLogin():
        print("--- Login Kasir ---")
        print(f"Kasir '{login_attempt.username}' berhasil login.")
        print("-" * 20)

        # 2. Tambahan item ke keranjang
        print("<=<=< Keranjang Belanja >=>=>")
        keranjang = [
            HitungPembayaran(idMenu="M01", namaMenu="Nasi Goreng", harga=20000, jumlah=2),
            HitungPembayaran(idMenu="M03", namaMenu="Es Teh", harga=5000, jumlah=1)
        ]
        
        total_belanja = 0
        for item in keranjang:
            print(f"{item.namaMenu} (x{item.jumlah}): Rp {item.totalHarga}")
            total_belanja += item.totalHarga
        
        print(f"Total Belanja: Rp {total_belanja}")
        print("-" * 20)

        # 3. Pilih metode pembayaran
        print("===== Metode Pembayaran =====")
        final_total = total_belanja
        metode = input("Pilih metode pembayaran (1: Tunai, 2: Kartu): ")

        if metode == '2':
            print("\nMemproses Pembayaran dengan Kartu...")
            pembayaran_card = PembayaranByCard()
            final_total = pembayaran_card.hitungTotalHarga(total_belanja)
            print(f"Total Akhir setelah biaya admin: Rp {final_total:,.2f}")

        elif metode == '1':
            print("\nMemproses Pembayaran Tunai...")
            pembayaran_tunai = PembayaranTunai()
            # Logika untuk pembayaran tunai (misal: hitung kembalian) bisa ditambahkan di sini
            print(f"Total Akhir: Rp {final_total:,.2f}")
        
        else:
            print("Pilihan tidak valid. Menggunakan total belanja asli.")

        print("-" * 20)

        # 4. Cetak Struk
        struk_final = TCetakStruk(noStruk="STRK2023-001", totalHarga=final_total)
        printer_struk = CetakStruk()
        printer_struk.cetakStruk(struk_final)

    else:
        print("Login gagal. Username atau password salah.")
