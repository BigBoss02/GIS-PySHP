import shapefile #mengimpor library shape pada python
w=shapefile.Writer() #menulis shape file
w.shapeType #menggunakan tipe apa shape di buat
w.field("kolom1","C") #membuat file dengan nama kolom 1 dengan type character
w.field("kolom2","C") #membuat file dengan nama kolom 2 dengan type character
w.record("poly1","satu")
w.record("poly2","dua") #membuat record dengan isi kolom 1 "ngek" dan kolom dua "satu"
w.record("poly3","tiga")
w.record("poly4","empat")
w.record("poly5","lima")
w.record("poly6","enam")
w.record("poly7","tujuh")
w.record("poly8","delapan")
w.record("poly9","sembilan")
w.poly(parts=[[[-6.8743818854,107.5758058245],[-6.8743548537,107.5757940612]]], shapeType=shapefile.POLYLINE) #membuat shapetype dengan jenis POLYLINE dengan menentukan 2 koordinatnya
w.poly(parts=[[[-6.8743427079,107.5757885562],[-6.8743186039,107.5757774981]]], shapeType=shapefile.POLYLINE) #membuat shapetype dengan jenis POLYLINE dengan menentukan 2 koordinatnya
w.poly(parts=[[[-6.8741366313,107.5757763039],[-6.8740677785,107.575793053]]], shapeType=shapefile.POLYLINE) #membuat shapetype dengan jenis POLYLINE dengan menentukan 2 koordinatnya
w.poly(parts=[[[-6.874216569,107.5757545932],[-6.8741588967,107.5757712535]]], shapeType=shapefile.POLYLINE) #membuat shapetype dengan jenis POLYLINE dengan menentukan 2 koordinatnya
w.poly(parts=[[[-6.8740333032,107.5757274866],[-6.8740126264,107.5755878652]]], shapeType=shapefile.POLYLINE) #membuat shapetype dengan jenis POLYLINE dengan menentukan 2 koordinatnya
w.poly(parts=[[[-6.8740040705,107.5755376014],[-6.8739833937,107.57539798]]], shapeType=shapefile.POLYLINE) #membuat shapetype dengan jenis POLYLINE dengan menentukan 2 koordinatnya
w.poly(parts=[[[-6.8739436253,107.5759295436],[-6.8738891721,107.5759968406]]], shapeType=shapefile.POLYLINE) #membuat shapetype dengan jenis POLYLINE dengan menentukan 2 koordinatnya
w.poly(parts=[[[-6.8738713841,107.5760176932],[-6.8737691935,107.5761461474]]], shapeType=shapefile.POLYLINE) #membuat shapetype dengan jenis POLYLINE dengan menentukan 2 koordinatnya
w.poly(parts=[[[-6.8742697387,107.5757582459],[-6.8742454704,107.5757504358]]], shapeType=shapefile.POLYLINE) #membuat shapetype dengan jenis POLYLINE dengan menentukan 2 koordinatnya

w.save("poly") #menyimpan file dengan nama "poly"