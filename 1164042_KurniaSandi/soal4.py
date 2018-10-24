import shapefile						#mengimpor library shape pada python
w=shapefile.Writer(shapefile.POINTM)	#menulis shape file dengan dengan parameter POINTM
w.shapeType								#menggunakan tipe/parameter shape apa yang di buat
 
w.field("kolom1","C") 					#membuat file dengan nama kolom 1 dengan type character
w.field("kolom2","C")					#membuat file dengan nama kolom 2 dengan type character

w.record("ngek","satu") 				#membuat record dengan parameter ngek dan satu
w.record("ngok","dua") 					#membuat record dengan parameter ngok dan dua

w.point(1,1) 							#memberikan koordinat untuk membuat line pada 1 di sumbu x dan 1 di sumbu y
w.point(2,2)							#memberikan koordinat untuk membuat line pada 2 di sumbu x dan 2 di sumbu y
	
w.save("soal4") 						#menyimpan file shape dengan nama soal 4
 