import shapefile						#mengimpor library shape pada python
w=shapefile.Writer()					#mulai menulis shape file shape
w.shapeType								#menggunakan tipe/parameter shape apa yang di buat

w.field("kolom1","C")					#membuat file dengan nama kolom 1 dengan type character
w.field("kolom2","C")					#membuat file dengan nama kolom 2 dengan type character

w.record("ngek","satu")					#membuat record dengan parameter ngek dan satu
w.record("crot","dua")					#membuat record dengan parameter crot dan dua
w.record("cret","tiga")					#membuat record dengan parameter cret dan tiga
w.record("crut","empat")				#membuat record dengan parameter crut dan empat


w.poly(parts=[[
	[-6.873837,107.575186], #f'
	[-6.873853,107.575419], #t
	[-6.873962,107.575394], #u
	[-6.873942,107.575165] #f''

]],shapeType=shapefile.POLYLINE)			#membuat polygon dengan 9 koordinat dengan type polyline

w.save("gandaria4")						#menyimpan file shape dengan nama soal 10