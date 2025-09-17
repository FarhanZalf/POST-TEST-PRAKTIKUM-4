class Main:
    def __init__(self):
        pass
    def main(self):
        pass
    def uiLogin(self):
        pass
    def uiMenu(self):
        pass
    def uiHitungPembayaran(self):
        pass
    def uiCetakStruk(self):
        pass

class HitungPembayaran:
    def __init__(self, idMenu: str = "", namaMenu: str = "", harga: float = 0.0, jumlah: int = 0):
        self.idMenu = idMenu
        self.namaMenu = namaMenu
        self.harga = harga
        self.jumlah = jumlah
        self.totalHarga = self.harga * self.jumlah

    def insertPembayaran(self):
        pass
    def updatePembayaran(self):
        pass
    def deleteDataPembayaran(self):
        pass
    def cariDataPembayaranByIdMenu(self):
        pass

class PembayaranTunai:
    def __init__(self):
        pass
    def hitungTotalHarga(self, total_belanja: float, uang_dibayar: str) -> float:
        if uang_dibayar.strip() == "":
            print("Transaksi dibatalkan. Uang tidak diisi.")
            return 0

        uang_dibayar = float(uang_dibayar)
        if uang_dibayar < total_belanja:
            print(f"Uang tidak cukup! Total belanja Rp {total_belanja:,.2f}, uang dibayar Rp {uang_dibayar:,.2f}")
            return 0
        else:
            kembalian = uang_dibayar - total_belanja
            print(f"Total Belanja : Rp {total_belanja:,.2f}")
            print(f"Uang Dibayar  : Rp {uang_dibayar:,.2f}")
            print(f"Kembalian     : Rp {kembalian:,.2f}")
            return total_belanja

class PembayaranByCard:
    def __init__(self):
        pass
    def hitungTotalHarga(self, total_belanja: float) -> float:
        no_kartu = input("Masukkan nomor kartu: ")
        nama_bank = input("Masukkan nama bank: ")

        if no_kartu.strip() == "" or nama_bank.strip() == "":
            print("Transaksi dibatalkan. Nomor kartu atau nama bank tidak diisi.")
            return 0
        
        biaya_admin = total_belanja * 0.015
        total_akhir = total_belanja + biaya_admin
        print(f"Pembayaran dengan kartu {nama_bank} ({no_kartu}) berhasil.")
        print(f"Biaya Admin (1.5%): Rp {biaya_admin:,.2f}")
        print(f"Total Akhir: Rp {total_akhir:,.2f}")
        return total_akhir

class CetakStruk:
    def __init__(self):
        pass
    def cetakStruk(self, data_struk):
        if data_struk.totalHarga <= 0:
            print("Tidak ada transaksi untuk dicetak.")
            return
        print("\n========= STRUK PEMBAYARAN =========")
        print(f"No. Struk   : {data_struk.noStruk}")
        print(f"Total Harga : Rp {data_struk.totalHarga:,.2f}")
        print("Terima kasih telah berbelanja.")
        print("=======================================")


class TCetakStruk:
    def __init__(self, noStruk: str = "", totalHarga: float = 0.0):
        self.noStruk = noStruk
        self.totalHarga = totalHarga
class LoginKasir:
    def __init__(self, username: str = "", password: str = ""):
        self.username = username
        self.password = password
    def validasiLogin(self):
        return self.username == "admin" and self.password == "12345"
    def logout(self):
        pass


class KoneksiDatabase:
    def __init__(self, host: str = "", database: str = "", userName: str = "", password: str = ""):
        self.host = host
        self.database = database
        self.userName = userName
        self.password = password
    def membukaKoneksi(self):
        pass
    def eksekusiQuerySelect(self):
        pass
    def eksekusiQueryInsert(self):
        pass
    def eksekusiQueryUpdate(self):
        pass
    def eksekusiQueryDelete(self):
        pass
    def tutupKoneksi(self):
        pass

class TabelHitungPembayaran:
    def __init__(self, idMenu: str = "", namaMenu: str = "", harga: float = 0.0, jumlah: int = 0):
        self._idMenu = idMenu
        self._namaMenu = namaMenu
        self._harga = harga
        self._jumlah = jumlah
        self._totalHarga = self._harga * self._jumlah

    def setIdMenu(self, idMenu: str): self._idMenu = idMenu
    def getIdMenu(self) -> str: return self._idMenu

    def setNamaMenu(self, namaMenu: str): self._namaMenu = namaMenu
    def getNamaMenu(self) -> str: return self._namaMenu

    def setHarga(self, harga: float): self._harga = harga
    def getHarga(self) -> float: return self._harga

    def setJumlah(self, jumlah: int): self._jumlah = jumlah
    def getJumlah(self) -> int: return self._jumlah

    def setTotalHarga(self, totalHarga: float): self._totalHarga = totalHarga
    def getTotalHarga(self) -> float:
        self._totalHarga = self._harga * self._jumlah
        return self._totalHarga

class TabelPembayaranByCard:
    def __init__(self, idCard: str = "", jenisCard: str = "", namaBank: str = "", totalHarga: float = 0.0):
        self._idCard = idCard
        self._jenisCard = jenisCard
        self._namaBank = namaBank
        self._totalHarga = totalHarga

    def setIdCard(self, idCard: str): self._idCard = idCard
    def getIdCard(self) -> str: return self._idCard

    def setJenisCard(self, jenisCard: str): self._jenisCard = jenisCard
    def getJenisCard(self) -> str: return self._jenisCard

    def setNamaBank(self, namaBank: str): self._namaBank = namaBank
    def getNamaBank(self) -> str: return self._namaBank

    def setTotalHarga(self, totalHarga: float): self._totalHarga = totalHarga
    def getTotalHarga(self) -> float: return self._totalHarga

# Main Program
if __name__ == "__main__":
    login_attempt = LoginKasir("admin", "12345")
    if login_attempt.validasiLogin():
        print("Login Kasir berhasil.")

        keranjang = [
            HitungPembayaran(idMenu="M01", namaMenu="Basreng", harga=12000, jumlah=2),
            HitungPembayaran(idMenu="M02", namaMenu="Cimol", harga=8000, jumlah=2),
            HitungPembayaran(idMenu="M02", namaMenu="Keripik Kaca", harga=5000, jumlah=2)
        ]

        total_belanja = sum(item.totalHarga for item in keranjang)
        print("\nKeranjang Belanja:")
        for item in keranjang:
            print(f"- {item.namaMenu} (x{item.jumlah}) = Rp {item.totalHarga:,.2f}")
        print(f"Total Belanja: Rp {total_belanja:,.2f}")

        print("\n===== Metode Pembayaran =====")
        metode = input("Pilih (1: Tunai, 2: Kartu): ")

        final_total = 0
        if metode == "1":
            print("\nPembayaran Tunai")
            uang = input("Masukkan uang yang dibayar: ")
            pembayaran_tunai = PembayaranTunai()
            final_total = pembayaran_tunai.hitungTotalHarga(total_belanja, uang)
        elif metode == "2":
            print("\nPembayaran dengan Kartu")
            pembayaran_card = PembayaranByCard()
            final_total = pembayaran_card.hitungTotalHarga(total_belanja)

        struk = TCetakStruk(noStruk="STRK001", totalHarga=final_total)
        printer = CetakStruk()
        printer.cetakStruk(struk)
    else:
        print("Login gagal. Username/password salah.")
