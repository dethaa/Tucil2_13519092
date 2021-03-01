# Tucil2_13519092
> Program yang menyelesaikan permasalahan pembuatan rencana pengambilan mata kuliah menggunakan pendekatan _topological sort_ dan algoritma _decrease and conquer_.


## Penjelasan Algoritma
Tahapan _decrease and conquer_ yang diimplementasikan dalam program adalah sebagai berikut.
* _Decrease_: mereduksi persoalan menjadi dua upa-persoalan yaitu semua simpul dengan derajat masuk 0 dan semua simpul dengan derajat masuk lebih dari 0. Simpul yang memiliki derajat masuk 0 yang merupakan representasi mata kuliah yang tidak memiliki prerequisite diambil dan dihapus dari persoalan. Demikian juga dihapus busur yang berasal simpul tersebut sehingga derajat masuk simpul tujuan berkurang 1. Ini merupakan representasi dari penghapusan mata kuliah prerequisite dari mata kuliah yang direpresentasikan oleh simpul tujuan.
* _Conquer_: melakukan pemrosesan decrease and conquer secara rekursif terhadap satu upa-persoalan, yaitu semua simpul yang tadinya berderajat masuk lebih dari 0. Namun kali ini, pasti sudah ada simpul yang berderajat masuk 0 untuk selanjutnya di-decrease/dihapus dari persoalan.


## Teknologi
Python - version 3.7+


## Cara Menjalankan
1. Buka terminal dan arahkan pada direktori yang dikehendaki untuk menyimpan kode program 
2. Salin repository git dengan perintah ``git clone https://github.com/dethaa/Tucil2_13519092`` 
3. Jalankan file 13519092-main.py yang terdapat pada folder src, dapat melalui terminal dengan mengarahkan direktori pada folder src kemudian menjalankan perintah  ``python3 13519092-main.py``
4. Setelah diminta untuk memasukkan nama file test, masukkan nama file lengkap dengan ekstensinya. Masukan harus sesuai dengan nama file yang terdapat pada folder test. Contoh: test1.txt
5. Solusi kemudian ditampilkan ke layar


## Kontak
Sharon Bernadetha Marbun - 13519092

13519092@std.stei.itb.ac.id
