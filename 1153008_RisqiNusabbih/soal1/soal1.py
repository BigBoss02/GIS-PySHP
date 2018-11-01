import shapefile 
 w=shapefile.Writer() 
 w.shapeType  
 w.field("Provinsi","C") 
 w.field("Kota","C")  
 w.record("Aceh","Banda Aceh") 
 w.record("Sumatera Utara","Medan")  
 w.point(1,1) 
 w.point(2,2)  
 w.save("soal1") 