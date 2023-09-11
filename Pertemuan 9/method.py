class XII_RPL_4() :
    def __init__(self, nama, absen, alamat) :
        self.nama = nama
        self.absen = absen
        self.alamat = alamat

    def perkenalan(self) :
        print('Hai saya ', self.nama)
        print('Absen', self.absen)
        print('rumah saya di ', self.alamat)

siswa1 = XII_RPL_4('Aditya', 1, 'Wonoayu')
siswa2 = XII_RPL_4('Rezzi', 18, 'Prambon')

siswa1.perkenalan()
siswa2.perkenalan()
