class Sınıf():
    __gizli = 'gizli'

    def örnek_metodu(self):
        print(self.__gizli)
        print('örnek metodu')

    @classmethod
    def sınıf_metodu(cls):
        print('sınıf metodu')

    @staticmethod
    def statik_metot():
        print('statik metot')
