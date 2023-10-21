import sys
sys.path.append('../Codes/')
from main_Class import *

dir_file = '../Dars 7/'


A = ["آن", "باران", "نَم نَم", "نور", "اَنار", "مَن", "او", "تَنور", "دانا", "نادان", "آدامس", 
     "نَبات", "تاس", "آسان", "ماست", "راست", "درس", "مو", "بَدَن", "موم", "برادر", "سوت", "بو", ""]

D = [
     "باران نم نم آمد.",
     "در تنور نان است.",
     "دانا ادب دارد.",
     "آن آدامس بو دارد.",
     "من آب نبات دوست دارم."
   ]

def addrs(name):
   return f"Media/{name}.gif"

B = [
     [{'w': "دَندان" , 'img' :  addrs("Dandaan")}],
     [{'w': "دامَن" , 'img' :  addrs("Daaman")}],
     [{'w': "آبان" , 'img' : -1}],
     [{'w': "نام" , 'img' : -1}],
     [{'w': "دارم    ندارم" , 'img' : -1}, {'w': "من نان ندارم." , 'img' : -1} ],
     [{'w': "دارد    ندارد" , 'img' : -1}, {'w': "نادان ادب ندارد." , 'img' : -1} ],
     [{'w': "بَندَر" , 'img' : addrs("Bandar")}],
     [{'w':  "توران", 'img' :  -1}],
     [{'w': "" , 'img' :  addrs("Start")}], #### Start photo
     [{'w': "ي#  ي    ي#  ي" , 'img' : -1}],
     [{'w': "دير" , 'img' : addrs("Dir")}],
     [{'w': "سير" , 'img' : addrs("Sir1")}, {'w': "" , 'img' : addrs("Sir2")}],
     [{'w': "تير" , 'img' : -1}, {'w': "" , 'img' : addrs("Tir")}],     
     [{'w': "آبي" , 'img' : addrs("Aabi")}],
     [{'w': "سينا    مينا" , 'img' : -1}, {'w': "ماني    اَمين" , 'img' : -1}, {'w': "نيما" , 'img' : -1}],
     [{'w': "ايمان" , 'img' : -1}],
     [{'w': "بيدار" , 'img' : addrs("Bidaar")}],
     [{'w': "بيمار" , 'img' : addrs("Bimaar")}],
     [{'w': "آسيب" , 'img' : addrs("Aasib")}],
     [{'w': "ديد" , 'img' : addrs("Did")}, {'w': "ديدَم" , 'img' : -1}],
     [{'w': "بينا" , 'img' : -1}, {'w': "نابينا" , 'img' : addrs("Naabinaa")}],
     [{'w': "بي" , 'img' : -1}, {'w': "بي ادب" , 'img' : -1}, {'w': "بي دندان" , 'img' : addrs("Bidandaan")}],
     [{'w': "سيني" , 'img' : addrs("Sini1")}, {'w': "" , 'img' : addrs("Sini2")}]
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
RS1.time_delay = 10
RS1.speed1 = 'fast'
RV1.speed1 = 'normal'
NL1.speed2 = 'slowest'


RV1.write_words(A)
RS1.write_sentences(D)
NL1.write_words(B, dir_file)

print("finished")      


















