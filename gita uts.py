class NamaKelas:
    def __init__(self):
        self._dataPribadi = "ini adalah variabel Private"

    def __metodePribadi(self):
        return "Ini adalah methode Private"

    #Getter untuk dataPribadi untuk memanggil/mengembalikan nilai tanpa mengubah nilainya.
    def getDataPribadi(self):
        return self._dataPribadi

    #Setter untuk dataPribadi untuk mengubah dan mengatur nilai dari atribut.
    def setDataPribadi (self, nilaiBaru):
        self._dataPribadi = nilaiBaru

    #Metode publik untuk mengakses stodePribadi
    def aksesMetodePribadi(self):
        return self.__metodePribadi()


    def metodePublik(self):
        print("Ini adalah methode publik")
        #Metode publik ini bisa mengakses metode dan data pribadi print(self. metodePribadi()) print(self. dataPribadi)
        print(self.__metodePribadi())
        print(self._dataPribadi)

class TurunanNamaKelas(NamaKelas):
    def _init_(self):
        #Memanggil konstruktor kelas induk
        super().__init__()

    def demoTurunan(self):
        #Menggunakan getter dari kelas induk
        dataPribadi = self.getDataPribadi()
        print(f"Data pribadi dari kelas induk: {dataPribadi}")

        #Mengubah data pribadi melalui setter kelas induk 
        self.setDataPribadi("nilai baru dari turunan")
        dataPribadiBaru = self.getDataPribadi()
        print(f"Data pribadi setelah diubah oleh turunan: {dataPribadiBaru}")

        #Mengakses metode pribadi dari kelas induk melalui metode publik
        hasilMetodePribadi = self.aksesMetodePribadi()
        print(f"Hasil akses metode pribadi dari turunan: {hasilMetodePribadi}")

        (self.metodePublik())
      

#Membuat objek dari Turunan Namakelas dan memanggil demonya
objekTurunan = TurunanNamaKelas()
objekTurunan.demoTurunan()