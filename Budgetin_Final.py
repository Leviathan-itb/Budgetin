"""
Tugas Besar - 1 Matakuliah KU1102 Pengenalan Komputasi
Semester 2 2023/2024

"Budgetin"
Sistem pencatatan pemasukan dan pengeluaran sebagai solusi 
penganggaran dana harian Mahasiswa

Oleh :
Nansha Hernanda                 [16723425]: Software Engineer and Gui Designer
Muhammad Iqra Al Farel          [16723383]: xxx
Dzakwan Rashif Putera Insani    [16723401]: xxx
Hauna Azzahra Afifa Nur         [16723365]: xxx
Nirmala Avie Cena               [16723353]: xxx
Karissa Maheswari               [16723397]: xxx nanti diisi
"""
# KAMUS
## Daftar variabel 
# master                   : Tk            : Tkinter window utama
# transactions             : list          : Daftar transaksi yang disubmit
# balance                  : int           : Saldo saat ini
# total_income             : int           : Total pemasukan
# total_expense            : int           : Total pengeluaran
# label_name               : Label         : Label untuk nama transaksi
# entry_name               : Entry         : Entry untuk memasukkan nama transaksi
# label_amount             : Label         : Label untuk jumlah transaksi
# entry_amount             : Entry         : Entry untuk memasukkan jumlah transaksi
# label_type               : Label         : Label untuk jenis transaksi
# transaction_type         : StringVar     : StringVar untuk jenis transaksi
# option_type              : OptionMenu    : OptionMenu untuk memilih jenis transaksi
# label_date               : Label         : Label untuk tanggal transaksi
# entry_date               : Entry         : Entry untuk memasukkan tanggal transaksi
# submit_button            : Button        : Button untuk men-submit transaksi
# label_balance            : Label         : Label untuk menampilkan saldo saat ini
# label_income             : Label         : Label untuk menampilkan total pemasukan
# label_expense            : Label         : Label untuk menampilkan total pengeluaran
# plot_button              : Button        : Button untuk menampilkan grafik
# transaction_history_tree : Treeview      : Treeview untuk menampilkan riwayat transaksi

## fungsi/prosedur
# __init__(self, master)            : Inisialisasi objek Budgetin.
#   - master                        : Tkinter GUI window utama.
# submit_transaction(self)          : Menambahkan transaksi baru.
#   - name                          : Nama transaksi.
#   - amount                        : Jumlah transaksi.
#   - transaction_type              : Jenis transaksi ("Pemasukan" atau "Pengeluaran").
#   - date                          : Tanggal transaksi (dalam format "DD-MM-YYYY").
# update_labels(self)               : Memperbarui label saldo, total pemasukan, dan total pengeluaran.
# update_transaction_history(self)  : Memperbarui riwayat transaksi pada Treeview.
# plot_graph(self)                  : Menampilkan grafik pie dari total pemasukan dan pengeluaran(dengan module matplotlib).
# main()                            : Fungsi utama untuk menjalankan program.

# ALGORITMA

# import module
import sys
sys.path.append(r'C:\Users\User\AppData\Local\Programs\Python\Python311\Lib\site-packages')
# Mengimpor modul tkinter dan memberikannya alias "tk" sebagai Graphical User Interface program ini.
import tkinter as tk
# Mengimpor fungsi "messagebox" dan modul "ttk" dari modul tkinter.
from tkinter import messagebox, ttk
# Mengimpor fungsi "datetime" dari modul datetime yang akan digunakan untuk tanggal dan waktu pada program.
from datetime import datetime
# Mengimpor modul "pyplot" dari library matplotlib dan memberikannya alias "plt" yang akan digunakan pada pembuatan grafik
import matplotlib.pyplot as plt

# mendefinisikan class utama berisi gui dan program yang akan digunakan pada aplikasi Budgetin
class Budgetin:
# def __init__()= fungsi inisialisasi atribut dan widget GUI yang diperlukan Budgetin
# (self)        = mengikat/mengaitkan atribut dan metode dalam kode dibawah kepada class Budgetin, agar saat
#                 mengakses suatu atribut seperi self.balance, kita mengakses atribut balance dari Budgetin, begitu pula pada atribut lain
# (master)      = tkinter window utama GUI Budgetin nantinya akan ditampilkan
    def __init__(self, master):
        self.master = master
        self.master.title("Budgetin!") # membuat judul window utama apllikasi ini benjadi "Budgetn"

        self.transactions = []  # deklarasi array/list kosong untuk menyimpan transaksi yang ada
        self.balance = 0        # deklarasi dan inisialisasi saldo(balance) awal, yaitu 0
        self.total_income = 0   # deklarasi dan inisialisasi total pemasukan(income) awal, yaitu 0
        self.total_expense = 0  # deklarasi dan inisialisasi total pengeluaran(expense) awal, yaitu 0

        self.label_name = tk.Label(master, text="Nama Transaksi:") # membuat label "nama transaksi"
        self.label_name.grid(row=0, column=0) # posisi label nama transaksi ada di baris 0 dan kolom 0 pada GUI window Budgetin

        self.entry_name = tk.Entry(master) # membuat entry widget untuk menginput nama transaksi dari user
        self.entry_name.grid(row=0, column=1) # posisi entry widget untuk nama transaksi ada di baris 0 dan kolom 0 pada window

# untuk dibawah ini, saya tidak akan menjelaskan dengan panjang lagi untuk label dan entry, karena kurang lebih
# sama seperti deskripsi label dan entry pada nama transaksi. saya hanya akan memberikan info" singkat

        self.label_amount = tk.Label(master, text="Jumlah (Rupiah):") # jumlah transaksi
        self.label_amount.grid(row=1, column=0) # baris 1 kolom 0

        self.entry_amount = tk.Entry(master) # entry jumlah transaksi
        self.entry_amount.grid(row=1, column=1) # baris 1 kolom 1

        self.label_type = tk.Label(master, text="Jenis Transaksi:") # jenis transaksi
        self.label_type.grid(row=2, column=0) # baris 2 kolom 0

        self.transaction_type = tk.StringVar(master) # stringvar untuk menyimpan perubahan jenis transaksi
        self.transaction_type.set("Pemasukan") # set jenis transaksi default/awal menjadi "pemasukan"
        self.option_type = tk.OptionMenu(master, self.transaction_type, "Pemasukan", "Pengeluaran") # option jenis transaksi, yaitu pemasukan dan pengeluaran
        self.option_type.grid(row=2, column=1) # baris 2 kolom 1

        self.label_date = tk.Label(master, text="Tanggal (DD-MM-YYYY):") # label tanggal transaksi dengan format DD-MM-YYYY
        self.label_date.grid(row=3, column=0)

        self.entry_date = tk.Entry(master) # entry tanggal transaksi dengan format DD-MM-YYYY
        self.entry_date.grid(row=3, column=1)

        self.submit_button = tk.Button(master, text="Submit", command=self.submit_transaction) # membuat tombol "submit" untuk menambah transaksi baru
        self.submit_button.grid(row=4, column=1)

        self.label_balance = tk.Label(master, text="Saldo Saat Ini: Rp0 ") # membuat label yang menampilkan saldo saat ini(Rp0 di awal)
        self.label_balance.grid(row=5, column=0)

        self.label_income = tk.Label(master, text="Total Pemasukan: Rp0 ") # membuat label yang menampilkan total pemasukan(Rp0 di awal)
        self.label_income.grid(row=6, column=0)

        self.label_expense = tk.Label(master, text="Total Pengeluaran: Rp0 ") # membuat label yang menampilkan total pengeluaran(Rp0 di awal)
        self.label_expense.grid(row=7, column=0)

        self.plot_button = tk.Button(master, text="Tampilkan Grafik", command=self.plot_graph) # tombol untuk menampilkan grafik pemasukan dan pengeluaran dengan matplotlib
        self.plot_button.grid(row=6, column=1) # fungsi untuk plot_graph ada dibawah ya

        # widget untuk menampilkan riwayat transaksi, dengan "Nama", "Jumlah", "Jenis", "Tanggal" sebagai kolom untuk treeview riwayat transaksi
        self.transaction_history_tree = ttk.Treeview(master, columns=("Nama", "Jumlah", "Jenis", "Tanggal")) 
        # menetapkan judul untuk masing2 kolom, seperti kolom "Nama" yang judulnya menjadi "Nama Transaksi"
        self.transaction_history_tree.heading("#0", text="Nomor Transaksi")
        self.transaction_history_tree.heading("Nama", text="Nama Transaksi")
        self.transaction_history_tree.heading("Jumlah", text="Jumlah Transaksi")
        self.transaction_history_tree.heading("Jenis", text="Jenis Transaksi")
        self.transaction_history_tree.heading("Tanggal", text="Tanggal Transaksi")
        self.transaction_history_tree.grid(row=9, column=0, columnspan=2) # posisi dari treeview riwayat transaksi, baris 9 kolom 0 dan mengambil 2 kolom

# mendefinisikan fungsi submit_transaction() yang akan dipanggil saat user menekan tombol "sumbit"
    def submit_transaction(self):
        # variabel" di bawah akan megambil nilai dari entry yang ada pada class budgetin, dengan nilai yang diinput user pada window
        name = self.entry_name.get() # mengambil nilai dari entry nama transaksi dan memasukkannya ke variabel "name"
        amount = int(self.entry_amount.get()) # mengambil nilai dari entry nilai transaksi dan memasukkannya ke variabel "amount"
        transaction_type = self.transaction_type.get() # mengambil nilai dari entry jenis transaksi dan memasukkannya ke variabel "transaction_type"
        date = self.entry_date.get() # mengambil nilai dari entry datetime dan memasukkannya ke varaibel "date"

        # jika name/amount/date kosong, maka akan muncul pesan error melalui messagebox seperti dibawah
        if not name or not amount or not date:
            messagebox.showerror("Error", "Mohon lengkapi semua kolom!")
            return # membuat program berhenti jika name/amount/date kosong

# pada bagian ini meggunakan algoritma try-except untuk menangani error yang mungkin terjadi
        try:
            datetime.strptime(date, "%d-%m-%Y")
        # mengonversi string date menjadi objek datetime dengan fungsi 'strptime' dari module datetime
        # jika string date tidak sesuai dengan format DD-MM-YYYY, akan terjadi ValueError
        except ValueError: # maka jika terjadi ValueError, messagebox error dibawah akan dimunculkan
            messagebox.showerror("Error", "Format tanggal tidak valid! Gunakan format DD-MM-YYYY!")
            return # menghentikan fungsi dieksekusi lebih lanjut jika date tidak sesuai format

    # percabangan untuk jenis transaksi yang dipilih pengguna pada OptionMenu
        # jika jenisnya adalah Pemasukan, maka:
        if transaction_type == "Pemasukan":
            self.total_income += amount # menambahkan nilai input ke total pemasukan
            self.balance += amount # menambahkan saldo dengan nilai yang diinput
        else:
        # jika jenisnya adalah Pengeluaran, maka:
            self.total_expense += amount # menambahkan nilai input ke total pengeluaran
            self.balance -= amount # mengurangi saldo dengan nilai yang diinput

        # append/menambahkan dictionary yang berisi name,amount,transaction_type, dan date ke dalam array/list transcation
        self.transactions.append({"name": name, "amount": amount, "type": transaction_type, "date": date})
        self.update_labels() # memanggil fungsi update_labels(fungsinya di bawah) untuk memperbarui label saldo, pendapatan, dan pengeluaran pada Budgetin
        self.update_transaction_history() # memanggil fungsi update_transaction_history(fungsinya ada di bawah) untuk memperbarui tampilan riwayat transaksi

    # fungsi untuk memperbarui label saldo, pendapatan, dan pengeluaran pada Budgetin
    def update_labels(self):
        # .config digunakan untuk mengatur properti dalam widget yang terkait
        self.label_balance.config(text=f"Saldo Saat Ini: Rp{self.balance} ")
        # mengatur "label_balance" untuk menampilkan saldo saat ini, yang diambil dari "self.balance"
        self.label_income.config(text=f"Total Pemasukan: Rp{self.total_income} ")
        # mengatur "label_income" untuk menampilkan total pemasukan, yang diambil dari "self.total_income"
        self.label_expense.config(text=f"Total Pengeluaran: Rp{self.total_expense} ")
        # mengatur "label_expense" untuk menampilkan total pem=ngeluaran, yang diambil dari "self.total_expense"

    # fungsi untuk memperbarui tampilan riwayat transaksi pada treeview di GUI Budgetin
    def update_transaction_history(self):
        self.transaction_history_tree.delete(*self.transaction_history_tree.get_children()) # menghapus semua entry yang ada pada treeview 'transaction_history_tree'
        # penghapusan entry sebelum menambahkan entry baru diperlukan untuk menghindari duplikasi riwayat transaksi pada treeview 'transaction_history_tree'
        # melakukan looping melalui setiap elemen dalam list "self.transaction", yang berisi name,amount,type, dan date
        # "enumerate" digunakan untuk mendapatkan indeks, yang pada kode ini dimulai dari 1(transaksi ke-1)
        for i, transaction in enumerate(self.transactions, start=1):
        # memasukkan entry baru ke dalam treeview transaction_history_tree, dengan setiap entry memiliki nomor str(i) yang dimulai dari 1,
        # dan elemen" "self.transaction" yang berisi name, amount, type, dan date
            self.transaction_history_tree.insert("", "end", text=str(i), values=(transaction["name"], transaction["amount"], transaction["type"], transaction["date"]))

    # fungsi untuk menampilkan diagram piechart pemasukan dan pengeluaran pada GUI Budgetin
    def plot_graph(self):
        labels = ['Pemasukan', 'Pengeluaran'] # deklarasi label pada bagian bagian diagram lingkaran berdasarkan jenis transaksi(pemasukan dan pengeluaran)
        sizes = [self.total_income, self.total_expense] # menyimpan nilai total pemasukan dan total pengeluaran ke dalam array 'sizes'
                                                        # array 'sizes' akan menentukan proporsi masing" jenis transaksi dalam piechart
        colors = ['#66b3ff', '#ff9999'] # menengatur warna untuk bagian pemasukan(biru) dan pengeluaran(merah)
        explode = (0.1, 0) # menentukan nilai seberapa jauh bagian yang kecil pada lingkaran akan "meledak" keluar lingkaran, sejauh 0.1 dari jari-jari lingkaran

        plt.figure(figsize=(6, 4)) # membuat figure dengan ukuran 6x4 inch untuk menampung diagram lingkaran yang akan ditampilkan
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=0)
        # membuat diagram lingkaran dengan data-data yang telah dibuat pada fungsi diatas ini
        # autopct='%1.1f%%' berguna untuk menambah label persentasi proporsi bagian dalam diagram lingkaran
        # startangle=0 menentukan sudut awal dimana diagram dimulai
        plt.axis('equal') # mengatur sumbu x dan y agar sama sehingga menghasilkan bentuk lingkaran(matematika irisan kerucut heheh)
        plt.title('Diagram Pemasukan dan Pengeluaran Budgetin!') # menambahkan judul/nama untuk diagram lingkaran
        plt.show() # menampilkan diagram lingkaran pada layar(saat user menekan tombol "tampilkan grafik")

# akhirnya kita sampai di bagian terakhir :)))
# def main() adalah fungsi utama pada program ini, yang didalamnya memiliki beberapa elemen
def main():
    root = tk.Tk() # membuat objek TKinter "root" yang akan menjadi window utama/root window tempat semua elemen GUI Budgetin ditampilkan
    app = Budgetin(root) # membuat objek TKinter "Budgetin" dengan parameter "root", sehingga program BUdgetin ditampilkan dalam jendela "root"
    root.mainloop() # memualai loop utama TKinter, yang juga menjaga window Budgetin tetap terbuka agar user dapat memasukkan data yang dimau

# nah fungsi dibawah ini juga cukup penting, dimana saat diperiksa dan skrip ini dijalankan langsung sebagai program utama(dalam kasus program ini, ya)
# maka program akan dijalankan. Namun, jika program ini tidak dijalankan sebagai program utama, misal sebagai modul(contoh modul tkinter)
# maka yang dijalankan hanya fungsi di dalamnya saja(seperti yang kita lakukan pada modul tkinter untuk membuat GUI)
if __name__ == "__main__": # karena program ini merupakan program utama, maka main() akan dieksekusi/dijalankan
    main()
# sekian dari saya, Nansha Hernanda [16723425] sebagai software engineer dan GUI designer, maaf jika ada typo dan kesalahan minor
# mewakili kelompok saya, saya mengucapkan terima kasih telah membaca program ini :)