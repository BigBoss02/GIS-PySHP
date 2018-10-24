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
	[1,3],
	[2,3], 
	[2,2],
	[1,2],
	[1,3],
	[2,2],
	[1,2],
	[2,3],
	[1,3]
]],shapeType=shapefile.POLYLINE)		#membuat polygon dengan 9 koordinat dengan type polyline

w.poly(parts=[[
	[3,3],
	[4,3], 
	[4,2],
	[3,2],
	[3,3],
	[4,2],
	[3,2],
	[4,3],
	[3,3]
]],shapeType=shapefile.POLYLINE)		#membuat polygon dengan 9 koordinat dengan type polyline

w.poly(parts=[[
	[1,1],
	[2,1], 
	[2,0],
	[1,0],
	[1,1],
	[2,0],
	[1,0],
	[2,1],
	[1,1]
]],shapeType=shapefile.POLYLINE)		#membuat polygon dengan 9 koordinat dengan type polyline

w.poly(parts=[[
	[3,1],
	[4,1], 
	[4,0],
	[3,0],
	[3,1],
	[4,0],
	[3,0],
	[4,1],
	[3,1]
]],shapeType=shapefile.POLYLINE)		#membuat polygon dengan 9 koordinat dengan type polyline

w.save("soal10")						#menyimpan file shape dengan nama soal 10