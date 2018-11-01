import shapefile						#mengimpor library shape pada python
w=shapefile.Writer()					#mulai menulis shape file shape
w.shapeType								#menggunakan tipe/parameter shape apa yang di buat

w.field("kolom1","C")					#membuat file dengan nama kolom 1 dengan type character
w.field("kolom2","C")					#membuat file dengan nama kolom 2 dengan type character

w.record("p","satu")					#membuat record dengan parameter ngek dan satu
w.record("i","dua")					#membuat record dengan parameter crot dan dua
w.record("u","tiga")					#membuat record dengan parameter cret dan tiga
w.record("w","empat")				#membuat record dengan parameter crut dan empat
w.record("w","empat")

w.poly(parts=[[
	[-6.873170,107.575258], #f'
	[-6.873234,107.575817], #t
	[-6.873668,107.575757], #u
	[-6.873592,107.575192]

]],shapeType=shapefile.POLYLINE)			#membuat polygon dengan 9 koordinat dengan type polyline

w.save("gpendidikan1")						#menyimpan file shape dengan nama soal 10