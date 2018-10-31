import shapefile #mengimpor library shape pada python
w=shapefile.Writer() #menulis shape file
w.shapeType #menggunakan tipe apa shape di buat
w.field("kolom1","C") #membuat file dengan nama kolom 1 dengan type character
w.field("kolom2","C") #membuat file dengan nama kolom 2 dengan type character
w.record("line1","satu")
w.record("line2","dua")
w.record("line3","tiga")
w.record("line4","empat")
w.line(parts=[[[-6.8743901794,107.57582112],[-6.8742404509,107.5757617658],[-6.8740486876,107.575817996],[-6.87375,107.5762]]]) #memberikan koordinat untuk membuat line
w.line(parts=[[[-6.8743924337,107.5758005192],[-6.8742400642,107.5757367221],[-6.87405,107.57578],[-6.87398,107.5753]]]) #memberikan koordinat untuk membuat line
w.line(parts=[[[-6.87396,107.5753],[-6.8740309305,107.5757943296],[-6.8737401594,107.5761551673]]]) #memberikan koordinat untuk membuat line

w.save("polyline") #menyimpan file shape dengan nama soal5