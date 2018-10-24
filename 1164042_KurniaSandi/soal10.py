import shapefile
w=shapefile.Writer()
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("ngek","satu")
w.record("crot","dua")
w.record("cret","tiga")
w.record("crut","empat")

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
]],shapeType=shapefile.POLYLINE)

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
]],shapeType=shapefile.POLYLINE)

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
]],shapeType=shapefile.POLYLINE)

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
]],shapeType=shapefile.POLYLINE)

w.save("soal10")