# Bolzano Method

> Praktikum 1 Komputasi Numerik

## **Kelompok 9**
- Java Kanaya Prada - 5025211112
- Adrian Ismu Arifianto - 5025211116
- Afiq Fawwaz Haidar - 5025211246

## Penjelasan Metode Bolzano
Metode `Bolzano` / `Biseksi (Bagi Dua)` / `Pembagian Interval` adalah metode yang digunakan untuk mencari akar-akar persamaan non linear melalui persamaan iterasi `f(X)`. Dalam Metode Bolzano, diperlukan 2 Nilai X sebelum memulai iterasi

> `X1` dengan `f(X1)` > 0\
`X2` dengan `f(X2)` < 0

Lalu kita akan mencari Nilai X3 dengan menggunakan Rumus

>`X3` = (`X1` + `X2`) / 2

Nilai yang `X3` yang diperoleh akan menggantikan nilai `X1` atau `X2` pada iterasi selanjutnya dengan syarat

> jika `f(X3) * f(X2) > 0`, maka `X2 = X3`\
jika `f(X3) * f(X2) < 0`, maka `X1 = X3`

Satu putaran iterasi telah selesai, iterasi tersebut dilakukan hingga `f(X3)` yang diperoleh  mendekati atau sama dengan 0 sehingga didapatkan akar - akar dari persamaan `f(X)`

## Implementasi Algoritma Metode Bolzano dalam Bahasa Python






Implementasi metode bolzano, untuk mencari solusi dari suatu persamaan matematika.

![image_2022-10-27_07-16-38](https://user-images.githubusercontent.com/87474722/198162620-5c12e87b-78bc-43b6-923c-d787b75d11f6.png)
