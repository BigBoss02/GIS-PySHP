import shapefile      
w=shapefile.Writer()     
w.shapeType        

w.field("kolom1","C")     
w.field("kolom2","C")     

w.record("ngek","satu")     
w.record("crot","dua")     
w.record("cret","tiga")     
w.record("crut","empat")
w.record("crat","lima") 
w.record("mpret","enam")  
w.record("mprot","tujuh")     
w.record("coy","delapan")     
w.record("cay","sembilan")     
w.record("cuy","sapuluh")  
w.record("cap","sebelas")
w.record("asd","asd")

w.poly(parts=[[
 [-6.873931,107.575158], 
 [-6.873922,107.575101], 
 [-6.873851,107.575112],
 [-6.873858,107.575168], 
 [-6.873931,107.575158]

]],shapeType=shapefile.POLYGON) 

w.poly(parts=[[
 [-6.873922,107.575101], 
 [-6.873913,107.575043], 
 [-6.873840,107.575056],
 [-6.873851,107.575112], 
 [-6.873922,107.575101]

]],shapeType=shapefile.POLYGON) 

w.poly(parts=[[
 [-6.873913,107.575043], 
 [-6.873904,107.574986], 
 [-6.873831,107.574999],
 [-6.873840,107.575056], 
 [-6.873913,107.575043]

]],shapeType=shapefile.POLYGON) 

w.poly(parts=[[
 [-6.873931,107.575158], 
 [-6.873954,107.575155], 
 [-6.873943,107.575097],
 [-6.873922,107.575101], 
 [-6.873931,107.575158]

]],shapeType=shapefile.POLYGON) 

w.poly(parts=[[
 [-6.873943,107.575097], 
 [-6.873932,107.575039], 
 [-6.873913,107.575043],
 [-6.873922,107.575101], 
 [-6.873943,107.575097]

]],shapeType=shapefile.POLYGON) 

w.poly(parts=[[
 [-6.873932,107.575039], 
 [-6.873923,107.574984], 
 [-6.873904,107.574986],
 [-6.873913,107.575043], 
 [-6.873932,107.575039]

]],shapeType=shapefile.POLYGON) 

w.poly(parts=[[
 [-6.873948,107.575123], 
 [-6.873943,107.575095], 
 [-6.873922,107.575101],
 [-6.873926,107.575129], 
 [-6.873948,107.575123]

]],shapeType=shapefile.POLYGON) 

w.poly(parts=[[
 [-6.873943,107.575095], 
 [-6.873937,107.575066], 
 [-6.873917,107.575070],
 [-6.873922,107.575101], 
 [-6.873943,107.575095]

]],shapeType=shapefile.POLYGON) 

w.poly(parts=[[
 [-6.873937,107.575066], 
 [-6.873932,107.575036], 
 [-6.873913,107.575043],
 [-6.873917,107.575070], 
 [-6.873937,107.575066]

]],shapeType=shapefile.POLYGON) 

w.poly(parts=[[
 [-6.873932,107.575036], 
 [-6.873927,107.575010], 
 [-6.873908,107.575013],
 [-6.873913,107.575043], 
 [-6.873932,107.575036]

]],shapeType=shapefile.POLYGON) 

w.poly(parts=[[
 [-6.873927,107.575010], 
 [-6.873924,107.574984], 
 [-6.873904,107.574986],
 [-6.873908,107.575013], 
 [-6.873927,107.575010]

]],shapeType=shapefile.POLYGON) 

w.poly(parts=[[
 [-6.873929,107.575067], 
 [-6.873927,107.575057], 
 [-6.873920,107.575058],
 [-6.873922,107.575068], 
 [-6.873929,107.575067]

]],shapeType=shapefile.POLYGON) 

 #===========================================================================================================


w.save("gandariajis")