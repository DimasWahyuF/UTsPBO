for val in "bahasa":
 if val == "h":
    continue
    break
 print (val)

#break statement. Statement ini berfungsi untuk keluar dari loop secara paksa. Dengan kata lain 
#ketika terdapat statement break maka baris selanjutnya tidak akan dijalankan dan perulangan 
#dinyatakan selesai. Ketika break dipanggil maka perintah dibawahnya (dalam kasus ini print ) 
#tidak akan dieksekusi. Bukan hanya itu saja, perulangan juga dianggap selesai. Tidak hanya 
#untuk for loop saja, statement break juga dapat digunakan pada while loop. Pada kasus nyata, 
#enggunaan break ini sangat berguna ketika kita ingin keluar dari infinite loop.

#continue yang fungsinya adalah untuk lompat ke iterasi selanjutnya tanpa harus mengeksekusi 
#sisa kode yang ada di bawahnya. Perbedaan utama dari break dan continue adalah 
#jika break akan menghentikan perulangan secara total, sedangkan continue hanya akan lompat 
#ke iterasi selanjutnya. Ketika dipanggil, keduanya sama-sama akan mengabaikan semua perintah 
#yang ada di bawahnya. Hal ini disebabkan karena pemanggilan perintah continue . Jadi ketika 
#kita memasuki kondisi dimana i sama dengan 5, maka perintah continue akan dijalankan.
