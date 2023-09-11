class Guru() :
    """
    Ini kelas guru
    """
    def __init__(self, nama, jk, mapel) :
        self.nama = nama
        self.jk = jk
        self.mapel = mapel

    def perkenalan(self) :
        print('Hai saya ', self.nama)
        print('Jenis Kelamin', self.jk)
        print('Mengajar ', self.mapel)



Guru1 = Guru('Aditya', 'L', 'IPS')
Guru2 = Guru('Rezzi', 'L', 'IPA')

Guru1.perkenalan()
Guru2.perkenalan()
