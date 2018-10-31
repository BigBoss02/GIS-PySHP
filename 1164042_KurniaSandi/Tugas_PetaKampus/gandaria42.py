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
	[-6.873839,107.575217], #b
	[-6.873827,107.575225], #b'
	[-6.873829,107.575249], #c'
	[-6.873841,107.575247] #c

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
	[-6.873843,107.575272], #d
	[-6.873831,107.575273], #d'
	[-6.873833,107.575297], #e'
	[-6.873845,107.575302] #e

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
	[-6.873847,107.575334], #f
	[-6.873835,107.575340], #f'
	[-6.873837,107.575367], #g'
	[-6.873849,107.575364]  #g

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
	[-6.873851,107.575390], #h
	[-6.873839,107.575394], #h'
	[-6.873841,107.575411], #i'
	[-6.873853,107.575419]  #i

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
	[-6.873962,107.575394], #k
	[-6.873961,107.575397], #k''
	[-6.873854,107.575422], #i''
	[-6.873853,107.575419]  #i

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
	[-6.873849,107.575364], #g
	[-6.873847,107.575367], #g''
	[-6.873849,107.575389], #h''
	[-6.873851,107.575390]  #h

]],shapeType=shapefile.POLYLINE)


w.poly(parts=[[
	[-6.873847,107.575334], #f
	[-6.873845,107.575333], #f''
	[-6.873843,107.575303], #e''
	[-6.873845,107.575302]  #e

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
	[-6.873843,107.575272], #d
	[-6.873841,107.575271], #d''
	[-6.873839,107.575249], #c''
	[-6.873841,107.575247]  #c

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
	[-6.873839,107.575217], #b
	[-6.873837,107.575216], #b''
	[-6.873835,107.575187], #a''
	[-6.873837,107.575186]  #a

]],shapeType=shapefile.POLYLINE)

w.save("gandaria42")						#menyimpan file shape dengan nama soal 10