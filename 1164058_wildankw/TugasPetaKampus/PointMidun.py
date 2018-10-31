import shapefile #mengimpor library shape pada python
w=shapefile.Writer() #menulis shape file dengan tipe shape 1
w.shapeType #menggun

w.field("kolom1","C")				
w.field("kolom2","C")
				
w.record("a","satu")					
w.record("b","dua")					
w.record("c","tiga")					
w.record("d","empat")
w.record("f","lima")
w.record("g","enam")
w.record("h","tujuh")
w.record("i","delapan")
w.record("j","sembilan")
w.record("k","sepuluh")	
w.record("l","sebelas")	
w.record("m","duabelas")				


			
w.point(-6.8740523,107.5753663)						
w.point(-6.8740513,107.5753564)	
w.point(-6.87404508,107.57530947)	
w.point(-6.8740435,107.5752983)
w.point(-6.8740370,107.5752506)
w.point(-6.8740358,107.5752408)
w.point(-6.8740295,107.5751959)
w.point(-6.8740284,107.5751863)
w.point(-6.8740346,107.5751493)
w.point(-6.8740398,107.5752052)
w.point(-6.8740471,107.5752617)
w.point(-6.8740546,107.5753173)

w.save("PointMidun")						