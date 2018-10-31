import shapefile
w=shapefile.Writer()
w.shapeType
w.field("kolom1","C")
w.field("kolom2","C")
w.record("poliline1","satu")
w.record("poliline2","dua")
w.record("poliline3","tiga")
w.record("poliline4","empat")
w.record("poliline5","lima")
w.record("poliline6","enam")
w.record("poliline7","tujuh")
w.record("poliline8","delapan")
w.record("poliline9","sembilan")
w.record("poliline10","sepuluh")
w.record("poliline11","sebelas")
w.record("poliline12","dualas")

w.poly(parts=[[
 [-6.873928,107.574985], 
 [-6.873929,107.574994] 

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
 [-6.873930,107.574998], 
 [-6.873931,107.575006] 

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
 [-6.873932,107.575011], 
 [-6.873933,107.575020] 

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
 [-6.873934,107.575024], 
 [-6.873935,107.575032] 

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
 [-6.873937,107.575039], 
 [-6.873938,107.575048] 

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
 [-6.873939,107.575052], 
 [-6.873940,107.575060] 

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
 [-6.873941,107.575068], 
 [-6.873943,107.575077] 

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
 [-6.873944,107.575080], 
 [-6.873945,107.575089] 

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
 [-6.873949,107.575097], 
 [-6.873950,107.575105] 

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
 [-6.873951,107.575110], 
 [-6.873952,107.575118] 

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
 [-6.873954,107.575127], 
 [-6.873955,107.575135] 

]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[
 [-6.873956,107.575140], 
 [-6.873958,107.575150] 

]],shapeType=shapefile.POLYLINE)

w.save("garisgandaria")