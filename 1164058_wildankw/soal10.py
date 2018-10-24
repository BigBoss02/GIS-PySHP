import shapefile # Mengimport modul shape file
w=shapefile.Writer() # Mendeklarasi variabel
w.shapeType #Menjalankan perintah dari pendeklarasian variabel

w.field("kolom1","C") # Membuat kolom dengan tipe data character
w.field("kolom2","C") # Membuat kolom dengan tipe data character

w.record("dan","satu") # Mengisi record ke kolom yang sudah di buat tadi
w.record("din","dua") # Mengisi record ke kolom yang sudah di buat tadi
w.record("dun","tiga") # Mengisi record ke kolom yang sudah di buat tadi
w.record("den","empat") # Mengisi record ke kolom yang sudah di buat tadi
w.record("don","lima") # Mengisi record ke kolom yang sudah di buat tadi


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
]],shapeType=shapefile.POLYGON) # Membuat POLYGON

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
]],shapeType=shapefile.POLYGON)  # Membuat POLYGON

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
]],shapeType=shapefile.POLYGON)  # Membuat POLYGON

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
]],shapeType=shapefile.POLYGON)  # Membuat POLYGON

w.poly(parts=[[
	[5,3],
	[6,3], 
	[6,2],
	[5,2],
	[5,3],
	[6,2],
	[5,2],
	[6,3],
	[5,3]
]],shapeType=shapefile.POLYGON)  # Membuat POLYGON



w.save("soal10") # Untuk save menjadi shp file
