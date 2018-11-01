import shapefile						#mengimpor library shape pada python
w=shapefile.Writer()					#mulai menulis shape file shape
w.shapeType								#menggunakan tipe/parameter shape apa yang di buat

w.field("kolom1","C")					#membuat file dengan nama kolom 1 dengan type character
w.field("kolom2","C")					#membuat file dengan nama kolom 2 dengan type character

w.record("ngek","satu")					#membuat record dengan parameter ngek dan satu
w.record("crot","dua")					#membuat record dengan parameter crot dan dua
w.record("cret","tiga")					#membuat record dengan parameter cret dan tiga
w.record("crut","empat")				#membuat record dengan parameter crut dan empat
w.record("wan","lima")
w.record("wen","enam")
w.record("wun","tujuh")
w.record("win","delapan")
w.record("won","sembilan")
w.record("gua","sepuluh")
w.record("gue","sebelas")
w.record("aku","duabelas")


w.poly(parts=[[
	[-6.873345,107.575404], #a1
	[-6.873341,107.575392], #a2
	[-6.873353,107.575389], #a3
	[-6.873356,107.575400] #a4

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
	[-6.873356,107.575400], #a4
	[-6.873353,107.575389], #a3
	[-6.873394,107.575381], #b1
	[-6.873395,107.575395] #b2

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
	[-6.873395,107.575395], #b2
	[-6.873394,107.575381], #b1
	[-6.873436,107.575377], #c1
	[-6.873435,107.575388]  #c2

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
	[-6.873435,107.575388], #c2
	[-6.873436,107.575377], #c1
	[-6.873445,107.575375], #d1'
	[-6.873445,107.575387]  #d2

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
	[-6.873429,107.575401], #e1
	[-6.873438,107.575396], #e2
	[-6.873442,107.575423], #e3
	[-6.873434,107.575427]  #e4

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
	[-6.873434,107.575427], #e4
	[-6.873442,107.575423], #e3
	[-6.873478,107.575619], #f1''
	[-6.873470,107.575627]  #f2

]],shapeType=shapefile.POLYLINE)


w.poly(parts=[[
	[-6.873478,107.575619], #f1'
	[-6.873470,107.575627],  #f2
	[-6.873452,107.575626], #g1
	[-6.873449,107.575616]  #g2

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
	[-6.873449,107.575616],  #g2
	[-6.873452,107.575626], #g1
	[-6.873413,107.575629], #h1''
	[-6.873405,107.575620]  #h2

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
	[-6.873405,107.575620],  #h2
	[-6.873413,107.575629], #h1''
	[-6.873377,107.575633], #a''
	[-6.873376,107.575622]  #a

]],shapeType=shapefile.POLYLINE)

w.save("gpendidikan3")						#menyimpan file shape dengan nama soal 10