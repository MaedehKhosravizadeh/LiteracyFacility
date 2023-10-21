import sys
sys.path.append('../Codes/')
from main_Class import *

dir_file = '../Dars 4/'

A = ["برادر", "تار", "مرام", "آرام","تاب", "بَدتر", "اَبر", "تَر",
     "تمام", "تَبَر", "مات", "درآمد", "آمدم", "تبر", "رَد", "دَم" ]

fd = "Media/"
B = [[{'w': "اَرباب" , 'img' :  -1}],
     [{'w': "دامدار" , 'img' :  fd + "Daamdaar.gif"}],
     [{'w': "مادر    آمد" , 'img' :  -1}, {'w': "مادر آمد." , 'img' :  -1}],
     [{'w': "بابا    بادام" , 'img' :  -1}, {'w': "دارد" , 'img' :  -1}, {'w': "بابا بادام دارد." , 'img' :  -1}],
     [{'w': "باد    آمد" , 'img' :  -1}, {'w': "باد آمد." , 'img' :  -1}],
     [{'w': "ابر    با" , 'img' :  -1}, {'w': "باد    آمد" , 'img' :  -1}, {'w': "ابر با باد آمد." , 'img' :  -1}],
     [{'w': "" , 'img' :  fd + "Start.gif"}], #### Start photo
     [{'w': "س# س   س# س" , 'img' :  -1}], 
     [{'w': "سَر" , 'img' :  -1}],
     [{'w': "سَرد"  , 'img': -1}, {'w': "سَرما"  , 'img': -1}],
     [{'w': "سَم" , 'img' :  fd + "Sam.gif"}],
     [{'w': "دَست" , 'img' :  fd + "Dast.gif"}],
     [{'w': "سَبَد" , 'img' :  fd + "Sabad.gif"}],
     [{'w': "داس" , 'img' :  fd + "Daas.gif"}],
     [{'w': "اَست" , 'img' :  -1}],
     [{'w': "آب    در" , 'img' :  -1}, {'w': "دست    اَست" , 'img' :  -1}, {'w': "آب در دست اَست." , 'img' :  -1}],
     [{'w': "بابا آمد. بابا داس" , 'img' : -1},{'w': "در دست دارد." , 'img' : -1}
      ,{'w': "بابا با داس آمد." , 'img' : -1}],
     [{'w': "بست" , 'img' :  -1},{'w': "مادر در را بَست." , 'img' : -1}],
     [{'w': "تَرس" , 'img' : -1},{'w': "مار ترس دارد." , 'img' :  -1}] ,
     [{'w': "بَس" , 'img' :  -1},{'w': "دَرس" , 'img' :  -1},{'w': "درس بس است." , 'img' :  -1}]
     ]
RV1 = review()
NL1 = learn()

'''
RV1.speed_A = 'normal'
RV1.width_pen_A = 4
RV1.sz_pen_A = .8
RV1.clrLineA = "#FCE6C9"
RV1.clrWordA = "#00C957"
RV1.time_delay_A = 6


NL1.speed_B = 'fastest'
NL1.width_pen_B = 4
NL1.sz_pen_B = .3
NL1.clrLineB = "black"
NL1.clrWordB = "black"
NL1.time_delay_B = .1
'''

RV1.speed_A = 'fastest'
RV1.time_delay_A = .1
RV1.write_words_A(A)
NL1.write_words_B(B, dir_file)

print("finished")      


















