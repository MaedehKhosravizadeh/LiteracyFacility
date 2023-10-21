import sys
sys.path.append('../Codes/')
from main_Class import *

dir_file = '../Dars 6/'

A = ["او", "آدامس", "اَسباب", "بور", "سود", "درس", "بو", "سَد", "دور", "توت", "آتوسا",
     "راسو", "آسم", "سوت", "تور", "بود", "رود", "مو", "دارو", "دوست", "روستا"]

D = [
     "راسو بدبو است.",
     "سر مو دارد.",
     "او باادب است.",
     "اسب رام است.",
     "روستا دور بود."
   ]

fd = "Media/"

B = [
     [{'w': "موم" , 'img' : fd + "Moom.gif" }],
     [{'w': "بوس" , 'img' : -1}],
     [{'w': "بودَم" , 'img' : -1}],
     [{'w': "ماست" , 'img' : fd + "Maast.gif"}],
     [{'w': "تاس" , 'img' : fd + "Taas.gif"}],
     [{'w': "راست" , 'img' : -1}],
     [{'w': "سارا" , 'img' : -1}, {'w': "سارا با آتوسا دوست است." , 'img' : -1}],
     [{'w': "" , 'img' :  fd + "Start.gif"}], #### Start photo
     [{'w': "ن# ن   ن# ن" , 'img' :  -1}],
     [{'w': "مَن" , 'img' :  -1}, {'w': "من درس دارم." , 'img' :  -1}],
     [{'w': "نور" , 'img' :  -1}],
     [{'w': "اَنار" , 'img': fd + "Anaar.gif"}],
     [{'w': "نان" , 'img' : fd + "Naan.gif"}],
     [{'w': "آسان" , 'img' :  -1}],
     [{'w': "باران" , 'img' :  fd + "Baaraan.gif"}],
     [{'w': "نَم نَم" , 'img' : -1}, {'w': "باران نم نم آمد." , 'img' : -1}],
     [{'w': "نَبات" , 'img' :  fd + "Nabaat.gif"}],
     [{'w': "آن" , 'img' :  -1}, {'w': "آن مرد" , 'img' :  -1},{'w': "آن اسب" , 'img' :  -1}],
     [{'w': "تَنور" , 'img' : fd + "Tanoor.gif"}],
     [{'w': "نان   آن   تنور" , 'img' :-1}, {'w': "در آن تنور نان اَست" , 'img' : -1}],  
     [{'w': "دانا" , 'img' :  -1}, {'w': "نادان" , 'img' :  -1}, {'w': "آن مرد دانا است." , 'img' :  -1}],
     [{'w': "بَدَن" , 'img' :  -1}],
     [{'w': "دَندان" , 'img' :  fd + "Dandaan.gif"}],
     [{'w': "دامَن" , 'img' :  fd + "Daaman.gif"}],
     [{'w': "آبان" , 'img' : -1}]
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


RV1.write_words(A)
RS1.write_sentences(D)
NL1.write_words(B, dir_file)

print("finished")      


















