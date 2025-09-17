# Main
class main:
    def _init_(self):
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

# HitungPembayaran
class HitungPembayaran:
    def _init_(self, idMenu: str = "", namaMenu: str = "", harga: float = 0.0, jumlah: int = 0):
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

# PembayaranTunai
class PembayaranTunai:
    def _init_(self):
        pass

    def hitungTotalHarga(self):
        pass

# PembayaranByCard
class PembayaranByCard:
    def _init_(self):
        pass

    def hitungTotalHarga(self):
        pass

# CetakStruk
class CetakStruk:
    def _init_(self):
        pass

    def cetakStruk(self):
        pass

# TCetakStruk
class TCetakStruk:
    def _init_(self, noStruk: str = "", totalHarga: float = 0.0):
        self.noStruk = noStruk
        self.totalHarga = totalHarga

# LoginKasir
class LoginKasir:
    def _init_(self, username: str = "", password: str = ""):    
        self.username = username
        self.password = password

    def validasiLogin(self):
        pass

    def logout(self):
        pass

# KoneksiDatabase
class KoneksiDatabase:
    def _init_(self, host: str = "", database: str = "", userName: str = "", password: str = ""):
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

# TabelHitungPembayaran
class TabelHitungPembayaran:
    def _init_(self, idMenu: str = "", namaMenu: str = "", harga: float = 0.0, jumlah: int = 0):
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

# TabelPembayaranByCard
class TabelPembayaranByCard:
    def _init_(self, idCard: str = "", jenisCard: str = "", namaBank: str = "", totalHarga: float = 0.0):
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