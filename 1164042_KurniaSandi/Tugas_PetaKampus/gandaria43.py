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

w.point(-6.8738479,107.575408)
w.point(-6.8738475,107.575404)
w.point(-6.8738470,107.575400)

w.point(-6.8738439,107.575358)
w.point(-6.8738435,107.575354)
w.point(-6.8738430,107.575350)

w.point(-6.8738409,107.575294)
w.point(-6.8738405,107.575290)
w.point(-6.8738400,107.575286)

w.point(-6.8738369,107.575242)
w.point(-6.8738365,107.575238)
w.point(-6.8738360,107.575234)

w.save("gandaria43")