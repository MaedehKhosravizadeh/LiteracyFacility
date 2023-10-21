import sys
sys.path.append('../Codes/')
from main_Class import *

dir_file = '../Dars 5/'

A = ["دَست", "داس", "سَر", "سرد", "سرما", "سم", "اَست", "ترس", "بَس", "بَست",
     "دارم", "آمدم", "درآمد", "تَبَر", "سبد", "تَر", "دامدار"]

D = ["مادر در را بست.",
     "مرد داس در دست دارد.",
     "آرد در سبد است.",
     "دامدار دام دارد."
   ]

fd = "Media/"

B = [
#     [{'w': "اَسب" , 'img' :  fd + "Asb.gif" }],
#     [{'w': "رام" , 'img' :  fd + "Raam.gif"}, {'w': "اسب رام است.", 'img' :  -1 }],
#     [{'w': "دَرس" , 'img' :  fd +"Dars_Khaandan.gif"},{'w': "درس بَس است.", 'img' :  -1}],
#     [{'w': "آسم" , 'img' :  fd + "Aasm.gif"}],
#     [{'w': "اَسباب" , 'img' : fd + "Asbaab.gif"}],
#     [{'w': "آدامس" , 'img' :  fd + "Aadaams.gif"}],
#     [{'w': "سَد" , 'img' :  fd + "Sad.gif"}],
#     [{'w': "" , 'img' :  fd + "Start.gif"}], #### Start photo
     [{'w': "و   و   و" , 'img' :  -1}], 
     [{'w': "بود   بود" , 'img': -1}, {'w': "باد سرد بود."  , 'img': -1}],
     [{'w': "دور" , 'img' :  -1}],
     [{'w': "رود" , 'img' :  fd + "Rood.gif"}],
     [{'w': "بور" , 'img' :  fd + "Boor.gif"}],
     [{'w': "توت" , 'img' :  fd + "Toot.gif"}],
     [{'w': "دوست" , 'img' :  -1}],
     [{'w': "او" , 'img' :  -1}, {'w': "او درس داد." , 'img' :  -1}, {'w': "او ادب دارد." , 'img' :  -1}],
     [{'w': "سود" , 'img' :  -1}, {'w': "درس سود دارد." , 'img' :  -1}],
     [{'w': "دارو" , 'img' :  -1}],
     [{'w': "آتوسا" , 'img' :  -1}],
     [{'w': "سَما" , 'img' :  -1}, {'w': "سما با آتوسا دوست است." , 'img' :  -1}],
     [{'w': "راسو" , 'img' : fd + "Raasoo.gif"}],
     [{'w': "تور" , 'img' :  fd + "Toor.gif"}],
     [{'w': "مو" , 'img' : fd + "Moo.gif"}],
     [{'w': "بو" , 'img' :  -1}, {'w': "بد بو" , 'img' :  fd + "Boo.gif"}],
     [{'w': "روستا" , 'img' : fd + "Roosta.gif"}]
     ]
RV1 = review("A")
RS1 = review("D")
NL1 = learn("B")

'''
RV1.speed1 = 'normal'
RV1.width_pen = 4
RV1.sz_pen = .8
RV1.clrLine = "#FCE6C9"
RV1.clrWord = "#00C957"
RV1.time_delay = 6

RS1.speed1 = 'normal'
RS1.width_pen = 4
RS1.sz_pen = .8
RS1.clrLine = "#FCE6C9"
RS1.clrWord = "#00C957"
RS1.time_delay = 6

NL1.speed2 = 'fastest'
NL1.width_pen = 4
NL1.sz_pen = .3
NL1.clrLine = "black"
NL1.clrWord = "black"
NL1.time_delay = .1
'''
RV1.clrLine = "#FCE6C9"
RV1.clrWord = "#00C957"
RS1.clrLine = "#BDFCC9"
RS1.clrWord = "#36648B"
RV1.time_delay = 7
RS1.time_delay = 7
RS1.speed1 = 'fast'
RV1.speed1 = 'normal'
NL1.speed2 = 'slowest'
#RV1.write_words(A)
#RS1.write_sentences(D)
NL1.write_words(B, dir_file)

print("finished")      


















