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


w.poly(parts=[[
	[-6.873837,107.575186], #f' = a
	[-6.873839,107.575217], #b
	[-6.873841,107.575247], #c
	[-6.873876,107.575239], #r
	[-6.873874,107.575209], #q
	[-6.873872,107.575178], #p
	[-6.873837,107.575186]


	#[-6.873853,107.575419], #t 	= i
	#[-6.873962,107.575394], #u	= k
	#[-6.873942,107.575165], #f'' = o
	#[-6.873837,107.575186]

	#[6.873930,107.574978], #i
	#[6.873825,107.574998], #j
	#[6.873853,107.575419], #t
	#[6.873962,107.575394], #u
	#[6.873930,107.574978]

	#[6.874045,107.575131],
	#[6.873952,107.575143], 
	#[6.873930,107.574978],
	#[6.873701,107.575023],
	#[6.873717,107.575204],
	#[6.873819,107.575190],

	#[6.873952,107.575143],
	#[6.873962,107.575394],

	#[6.873853,107.575419],
	#[6.874075,107.575376],
	#[6.874045,107.575131]
]],shapeType=shapefile.POLYGON)		#membuat polygon dengan 9 koordinat dengan type polyline

w.poly(parts=[[
	[-6.873841,107.575247], #c
	[-6.873843,107.575272], #d
	[-6.873845,107.575302], #e
	[-6.873880,107.575293], #t
	[-6.873878,107.575247], #s
	[-6.873876,107.575239], #r
	[-6.873841,107.575247]

]],shapeType=shapefile.POLYGON)

w.poly(parts=[[
	[-6.873845,107.575302], #e
	[-6.873847,107.575334], #f
	[-6.873849,107.575364], #g
	[-6.873884,107.575355], #v
	[-6.873882,107.575326], #u
	[-6.873880,107.575293], #t
	[-6.873845,107.575302]

]],shapeType=shapefile.POLYGON)

w.poly(parts=[[
	[-6.873849,107.575364], #g
	[-6.873851,107.575390], #h
	[-6.873853,107.575419], #i
	[-6.873888,107.575411], #j
	[-6.873886,107.575383], #w
	[-6.873884,107.575355], #v
	[-6.873849,107.575364]

]],shapeType=shapefile.POLYGON)

w.poly(parts=[[
	[-6.873884,107.575355], #v
	[-6.873886,107.575383], #w
	[-6.873888,107.575411], #j
	[-6.873962,107.575394], #k
	[-6.873957,107.575339], #l
	[-6.873884,107.575355]

]],shapeType=shapefile.POLYGON)

w.poly(parts=[[
	[-6.873880,107.575293], #t
	[-6.873882,107.575326], #u
	[-6.873884,107.575355], #v
	[-6.873957,107.575339], #l
	[-6.873951,107.575279], #m
	[-6.873880,107.575293]

]],shapeType=shapefile.POLYGON)

w.save("gandaria41")						#menyimpan file shape dengan nama soal 10