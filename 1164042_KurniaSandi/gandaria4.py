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
	[-6.873942,107.575165], #f''
	[-6.873837,107.575186]

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

w.save("gandaria4")						#menyimpan file shape dengan nama soal 10