import sys
sys.path.append('../Codes/')
from main import *

dir_file = '../Dars 3/'

A = ["ما", "دار", "بام", "مادر","بادام", "بَد", "دام", "بار",
     "بابا", "دارَم", "مار", "آمد", "آمدم", "مَرد", "درد" ]

fd = "Media/"
B = [[{'w': "اَبر" , 'img' :  fd + "Abr.gif"}],
     [{'w': "بَرادَر  برادَر" , 'img' :  -1}],
     [{'w': "آرام" , 'img' :  -1}],
     [{'w': "مَرام" , 'img' :  -1}, {'w': "با مَرام" , 'img' :  -1}],
     [{'w': "در    آمد" , 'img' :  -1}, {'w': "درآمد" , 'img' :  fd + "DarAmad.gif"}],
     [{'w': "" , 'img' :  -1}], #### Start photo
     [{'w': "ت# ت  ت# ت" , 'img' :  -1}],
     [{'w': "تا"  , 'img': -1}],
     [{'w': "تاب" , 'img' : fd + "Taab.gif"}] ,
     [{'w': "تار" , 'img' :  fd + "Taar.gif"} ,{'w': "", 'img': fd + "Taar cheshm.gif"}],
     [{'w': "مات" , 'img' :  fd + "Maat.gif"}],
     [{'w': "تَر" , 'img' :  fd + "Tar.gif"},{'w': "بدتَر" , 'img' :  -1}],
     [{'w': "تَب" , 'img' :  fd + "Tab.gif"}],
     [{'w': "تَبَر" , 'img' :  fd + "Tabar.gif"}],
     [{'w': "تَمام" , 'img' :  -1}]
     ]
review(A)
learn(B,dir_file)




















