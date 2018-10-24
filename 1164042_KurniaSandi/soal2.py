import shapefile #mengimpor library shape pada python
w=shapefile.Writer(shapeType=1) #menulis shape file dengan tipe shape 1
w.shapeType #menggunakan tipe apa shape di buat
w.field("kolom1","C")  	#membuat file dengan nama kolom 1 dengan type character
w.field("kolom2","C")	#membuat file dengan nama kolom 2 dengan type character
w.record("ngek","satu")
w.record("ngok","dua")
w.point(1,1)
w.point(2,2)
w.save("soal2") #menyimpan file shape dengan nama soal 2