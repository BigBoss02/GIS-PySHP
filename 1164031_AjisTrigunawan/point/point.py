import shapefile
w=shapefile.Writer()
w.shapeType
w.field("kolom1","C")
w.field("kolom2","C")
w.record("point1","satu")
w.record("point2","dua")
w.record("point3","tiga")
w.record("point4","empat")
w.record("point5","lima")
w.record("point6","enam")
w.record("point7","tujuh")
w.record("point8","delapan")
w.record("point9","sembilan")
w.record("point10","sepuluh")

w.point(-6.873938,107.575113)
w.point(-6.873934,107.575081)
w.point(-6.873923,107.575023)

w.save("titikgandaria")