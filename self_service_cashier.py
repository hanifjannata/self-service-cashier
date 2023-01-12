import pandas as pd

class Transaction:
    
    def __init__(self):
        self.data_belanja = {}

    def add_item(self, nama_item, jumlah_item, harga_item):
        '''
        Fungsi untuk menambahkan nama item, jumlah, dan harga ke dalam dictionary.

        Parameter:
        nama_item   : str   nama item
        jumlah_item : int   jumlah barang
        harga_item  : int   harga per item
        '''
        total_harga = jumlah_item * harga_item
        self.data_belanja.update({nama_item: [jumlah_item, harga_item, total_harga]})
        print(f"Item yang dibeli adalah: {self.data_belanja}")

    def update_item_name(self, nama_item, nama_item_baru): 
        '''
        Fungsi untuk mengubah nama item.

        Parameter:
        nama_item       : str   nama item lama
        nama_item_baru  : str   nama item baru
        '''
        
        temporary = self.data_belanja[nama_item]
        self.data_belanja.clear()
        self.data_belanja.update({nama_item_baru: temporary})

    def update_item_quantity(self, nama_item, jumlah_item_baru):
        '''
        Fungsi untuk mengubah jumlah item dalam daftar belanja.

        Parameter:
        nama_item           : str   nama_item
        jumlah_item_baru    : int   jumlah barang yang baru
        '''

        self.data_belanja[nama_item][0] = jumlah_item_baru

    def update_item_price(self, nama_item, harga_item_baru):
        '''
        Fungsi untuk mengubah harga item dalam daftar belanja.

        Parameter:
        nama_item          : str   nama item
        harga_item_baru : int   harga item yang baru
        '''

        self.data_belanja[nama_item][1] = harga_item_baru

    def total_price(self):
        '''Fungsi untuk menjumlahkan total biaya semua item yang ada dalam daftar belanja.'''

        total = 0
        for i in self.data_belanja:
            total += self.data_belanja[i][2]

        if total > 200000:
            total = total - (total * 0.05)
            print(f"Total belanja yang anda bayarkan: Rp. {total:.0f}") 
        elif total > 300000:
            total = total - (total * 0.08)
            print(f"Total belanja yang anda bayarkan: Rp. {total:.0f}")
        elif total > 500000:
            total = total - (total - 0.1)
            print(f"Total belanja yang anda bayarkan: Rp. {total:.0f}")
        else:
            raise Exception("Anda tidak mendapat diskon")

    def delete_item(self, nama_item):
        '''
        Fungsi untuk menghapus item dalam daftar belanja.
        
        Parameter:
        nama_item   : str   nama item
        '''

        self.data_belanja.pop(nama_item)
        print(f"Daftar belanja: {self.data_belanja}")

    def reset_transaction(self):
        '''Fungsi untuk menghapus seluruh item dalam daftar belanja.'''

        self.data_belanja.clear()
        print("Semua item dalam daftar belanja telah dihapus")

    def check_data_belanja(self):
        '''Fungsi untuk memerika apakah input yang diberikan sudah benar dan menampilkan data buku dalam bentuk tabel.'''

        for i in self.data_belanja:
            if type(i) == str:
                if type(self.data_belanja[i][0]) == int:
                    if type(self.data_belanja[i][1]) == int:
                        print("Pemesanan sudah benar")
            else:
                print("Terdapat kesalahan input")

        data = pd.DataFrame(self.data_belanja).T
        data.columns = ['Jumlah Item', 'Harga Item', 'Total Harga']
        print(data.to_markdown())




    
