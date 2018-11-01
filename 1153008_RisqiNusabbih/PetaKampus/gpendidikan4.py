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

w.point(-6.873349,107.575397)
w.point(-6.873365,107.575390)
w.point(-6.873385,107.575386)
w.point(-6.873421,107.575383)
w.point(-6.873437,107.575410)

w.point(-6.873441,107.575440)
w.point(-6.873442,107.575452)
w.point(-6.873446,107.575486)

w.point(-6.873462,107.575616)
w.point(-6.873428,107.575617)
w.point(-6.873389,107.575622)

w.save("gpendidikan4")