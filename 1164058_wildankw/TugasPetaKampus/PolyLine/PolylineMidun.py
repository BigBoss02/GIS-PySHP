import shapefile 
w=shapefile.Writer() 
w.shapeType 
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
				


w.line(parts=[[

[-6.8739861,107.5753857],
[-6.8739860,107.5753882],
[-6.8740150,107.5753833]]])

w.line(parts=[[

[-6.8740178,107.5753829],
[-6.8740444,107.5753800],
[-6.8740438,107.5753781]]])

w.line(parts=[[

[-6.87404588,107.57537957],
[-6.87406402,107.57537760],
[-6.87406370,107.57537539]]])

w.line(parts=[[

[-6.87395720,107.57515779],
[-6.87395679,107.57515602],
[-6.87398361,107.57515267]]])

w.line(parts=[[

[-6.87398625,107.57515420],
[-6.87398596,107.57515226],
[-6.87401266,107.57514873]]])

w.line(parts=[[

[-6.87401495,107.57514885],
[-6.87403750,107.57514579],
[-6.87403797,107.57514870]]])

w.line(parts=[[

[-6.8740391,107.5751789],
[-6.8740437,107.5751813],
[-6.8740464,107.5751997],
[-6.8740417,107.5752020]]])

w.line(parts=[[

[-6.8740456,107.5752314],
[-6.8740503,107.5752340],
[-6.8740530,107.5752525],
[-6.8740478,107.5752550]]])

w.line(parts=[[

[-6.8740524,107.5752900],
[-6.8740572,107.5752921],
[-6.8740599,107.5753109],
[-6.8740550,107.5753133]]])

w.line(parts=[[

[-6.8740592,107.5753448],
[-6.8740639,107.5753512],
[-6.8740666,107.5753697],
[-6.8740621,107.5753723]]])

w.save("polylineMidun") 