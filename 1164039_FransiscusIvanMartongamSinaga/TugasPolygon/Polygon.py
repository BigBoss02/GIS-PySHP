import shapefile      #mengimpor library shape pada python
w=shapefile.Writer()     #mulai menulis shape file shape
w.shapeType        #menggunakan tipe/parameter shape apa yang di buat

w.field("kolom1","C")     #membuat file dengan nama kolom 1 dengan type character
w.field("kolom2","C")     #membuat file dengan nama kolom 2 dengan type character

w.record("ngek","satu")     #membuat record dengan parameter ngek dan satu
w.record("crot","dua")     #membuat record dengan parameter crot dan dua
w.record("cret","tiga")     #membuat record dengan parameter cret dan tiga
w.record("crut","empat")    #membuat record dengan parameter crut dan empat
w.record("crit","lima")    #membuat record dengan parameter crut dan empat
w.record("polygon6","enam") 
w.record("polygon7","tujuh")
w.record("polygon8","delapan")
w.record("polygon9","sembilan")  
w.record("polygon10","sepuluh") 
w.record("polygon11","seebelas") 

w.poly(parts=[[
[-6.8742410203,107.575771282],
[-6.8742404509,107.5757617658],
[-6.8742148954,107.5757708507],
[-6.8742158266,107.5757774503],
[-6.8742410203,107.575771282],
]],shapeType=shapefile.POLYGON)


w.poly(parts=[[
[-6.8742158266,107.5757774503],
[-6.8742155605,107.5757715454],
[-6.8741908164,107.5757767556],
[-6.8741912155,107.5757847446],
[-6.8742158266,107.5757774503],
]],shapeType=shapefile.POLYGON)

w.poly(parts=[[
[-6.8741912155,107.5757847446],
[-6.8741908164,107.5757767556],
[-6.8741535673,107.575788218],
[-6.8741542324,107.5757965544],
[-6.8741912155,107.5757847446],
]],shapeType=shapefile.POLYGON)

w.poly(parts=[[
[-6.8741542324,107.5757965544],
[-6.8741535673,107.575788218],
[-6.8740992899,107.5758045434],
[-6.874099423,107.5758118377],
[-6.8741542324,107.5757965544],
]],shapeType=shapefile.POLYGON)

w.poly(parts=[[
[-6.8743879709,107.5757979438],
[-6.874388237,107.5757868286],
[-6.87437214,107.5757805764],
[-6.8743716079,107.5757903021],
[-6.8743879709,107.5757979438],
]],shapeType=shapefile.POLYGON)

w.poly(parts=[[
[-6.8743716079,107.5757903021],
[-6.87437214,107.5757805764],
[-6.8743503227,107.5757732821],
[-6.8743499236,107.5757826605],
[-6.8743716079,107.5757903021],
]],shapeType=shapefile.POLYGON)

w.poly(parts=[[
[-6.8743499236,107.5757826605],
[-6.8743503227,107.5757732821],
[-6.8743306338,107.5757639037],
[-6.874331166,107.5757757135],
[-6.8743499236,107.5757826605],
]],shapeType=shapefile.POLYGON)

w.poly(parts=[[
[-6.874331166,107.5757757135],
[-6.8743306338,107.5757639037],
[-6.8743121423,107.5757559147],
[-6.8743121423,107.5757666825],
[-6.874331166,107.5757757135],
]],shapeType=shapefile.POLYGON)

w.poly(parts=[[
[-6.874099423,107.5758118377],
[-6.8740988243,107.5758039485],
[-6.8740486876,107.575817996],
[-6.8740508323,107.5758282292],
[-6.874099423,107.5758118377],
]],shapeType=shapefile.POLYGON)

w.poly(parts=[[
[-6.8742883294,107.5757569568],
[-6.8742887285,107.575747231],
[-6.8742456259,107.575730211],
[-6.8742452268,107.5757388947],
[-6.8742883294,107.5757569568],
]],shapeType=shapefile.POLYGON)

w.poly(parts=[[
[-6.8738804214,107.5759773993],
[-6.87388,107.575965],
[-6.873866,107.57598],
[-6.873866,107.575995],
[-6.8738804214,107.5759773993],
]],shapeType=shapefile.POLYGON)

w.save("Polygon")