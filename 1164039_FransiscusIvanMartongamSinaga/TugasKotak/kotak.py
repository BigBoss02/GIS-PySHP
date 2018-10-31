import shapefile      #mengimpor library shape pada python
w=shapefile.Writer()     #mulai menulis shape file shape
w.shapeType        #menggunakan tipe/parameter shape apa yang di buat

w.field("kolom1","C")     #membuat file dengan nama kolom 1 dengan type character
w.field("kolom2","C")     #membuat file dengan nama kolom 2 dengan type character

w.record("ngek","satu")     #membuat record dengan parameter ngek dan satu
w.record("crot","dua")     #membuat record dengan parameter crot dan dua
w.record("cret","tiga")     #membuat record dengan parameter cret dan tiga
w.record("crut","empat")    #membuat record dengan parameter crut dan empat

w.poly(parts=[[
[-6.873586,107.575124],
[-6.873962,107.574683],
[-6.874439,107.575895],
[-6.873885,107.576278],
[-6.873714,107.576212]
]],shapeType=shapefile.POLYGON)

w.save("gandariamidun")      #menyimpan file shape dengan nama soal 10