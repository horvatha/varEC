# -*- coding: utf-8 -*-
#  -*- Python -*-

##################################
#
#en #  Language section -- English
#  Language section -- Hungarian
#
##################################
# 1. Environments and control sequences
#en env={'exercise':'exercise',
env={'exercise':'feladat',
#en      'solution':'solution',
     'solution':'megold',
#en      'group'   :'exercisegroup'}
     'group'   :'feladatcsoport'}

# 2. Asks
#en ask={        'group_numbers':'How many groups do you want? ',
ask={        'group_numbers':'Hány csoport legyen? ',
#en        'group':'The name of group %s (Enter = "%s", "kk" = exit) ',
        'group':'%s. csoport neve? (Enter = "%s", "kk" = kilépés) ',
#en        'exercise':'The code of exercise %s? (Enter = end) ',
        'exercise':'%s. feladat sorszáma? (Enter = vége) ',
#en        'exercise code':'The code of exercise? ',
        'exercise code':'Feladat sorszáma? ',
#en        'file name':'From which file? ',
        'file name':'Melyik fájlból? ',
#en        'file':'Which file search I from? ',
        'file':'Melyik fájlból válogassak? ',
#en         'enter':'Push >Enter< to continue, or "q" to quit! ',
        'enter':'Nyomj >Enter<-t a folytatáshoz, vagy "k"-t a kilépéshez! ',
#en         'change': 'Do you want to change? (Enter = no, y or yes = yes)',
        'change': 'Kíván változtatni? (Enter = nem, i vagy igen = igen) ',
#en         'use exercise_numbers': 'Can I use it? (Enter = yes, n or no = no )',
        'use exercise_numbers': 'Ezt használjam? (Enter = igen, n vagy nem = nem) ',
#en         'choice': 'Give the number, what do you want? ',
        'choice': 'Hányadikat választod? ',
#en         'testpapers num':'How many types of testpapers do you need?  '}
        'testpapers num':'Hányféle dolgozatra lesz szükséged? '}

# 3. Messages (errors not)
#en mesg={  'next':'Next step: ',
mesg={  'next':'Következő lépés: ',
#en         'file_names':'1. The next files are in this group:',
        'file_names':'1. Ebben a csoportban a következő fájlok vannak:',
#en         'intervals':'\n2. Intervals of exercise codes (pl. 12..14 means: 12, 13, 14):',
        'intervals':'\n2. Feladatkódszám intervallumok (pl. 12..14 jelentése: 12, 13, 14):',
#en         'not_uniq_main':'\n3. Not uniq exercise codes I found:',
        'not_uniq_main':'\n3. A megtalált többször szereplő feladatkódok:',
#en         'not_uniq':'%d times is the code %d!',
        'not_uniq':'%d-szer szerepel a %d-es feladatkód!',
#en         'bad_arg_main':'\n4. Bad arguments:',
        'bad_arg_main':'\n4. Hibás argumentumok:',
#en         'none':'None.',
        'none':'Nincsen.',
#en         'group name':'The name of the group is "%s".',
        'group name':'A csoport neve "%s". (bin/setup_hu.py)',
#en         'not_num':"You didn't wrote a(n integer) number!\n",
        'not_num':'Nem (egész) számot írtál!\n',
#en         'founded_exercises':'The exercise codes I found:',
        'founded_exercises':'A megtalált feladatkódszámok:',
#en         'not enough numbers':'It must be exercise in the groups!',
        'not enough numbers':'A csoportban legalább egy feladatnak lennie kell!',
#en         'change because 4a5':'I changed the format to %s because of the pagestyles 4a5!',
        'change because 4a5':'Átírtam a formátumot %s-re a 4a5 oldalstílus miatt!',
#en         'format':' Formats:\nIf you write pdf, ps or dvi, it uses the latex - dvips - ps2pdf programs\nIf you write pdflatex, you get a pdf format with pdflatex program\n If you write 0 or tex, it will not translate.\n',
        'format':' Formátumok:\nHa pdf-et, ps-t vagy dvi-t írsz, akkor a következő programokat használom: latex - dvips - ps2pdf\n Ha pdflatex-et írsz, akkor a pdflatex programmal fordítok PDF-be.\nHa 0-át írsz vagy tex-et, akkor nem fordítok.\n',
        'with solution': '>'*55 +
#en                 '\n\n If you want to print the exercises with solutions,\n'+
#en[2]                  ' you must correct the signed row in the .tex file(s).\n\n' +
                '\n\n Ha feladatokat megoldással szeretnéd kinyomtatni,\n'+
                 ' akkor a kiírt .tex  fájl(ok)ban kell átirni a megjelölt sort.\n\n' +
                '>'*55,
#en         'file_written':  'I wrote the exercises into the file "%s".\n',
        'file_written':  'Kiírtam a feladatokat a "%s" fájlba.\n',
#en         'wrote files':  'I wrote the files:\n %s\n',
        'wrote files':  'Kiírtam a következő fájlokat:\n %s\n',
#en         'translate':  'I will translate the files. It will take a while.\n',
        'translate':  'Most lefordítom a fájlokat. Ez eltart egy darabig.\n',
#en         'found exercise_numbers': 'I found a base setting for the exercise numbers:',
        'found exercise_numbers': 'Találtam egy alapbeállítást a feladatsorszámokra:',
#en         'series_in'   :  'Type in the exercisenumbers.\n',
        'series_in'   :  'Beolvasom a feladatsorszámokat.\n',
#en         'file opened' :  'I\'ve opened the file "%s".\n',
        'file opened' :  'Megnyitottam a "%s" nevű fájlt.\n',
#en         'fixed data'  :  '**** The data in the current form ****',
        'fixed data'  :  '**** A javított adatok ****',
#en         'data'  :  '**** The data in the current form ****',
        'data'  :  '**** A jelenlegi adatok ****',
#en         'group name'  :  'The name of the group: "%s"',
        'group name'  :  'A csoport neve: "%s"',
#en        'modify'      : '''*** You can modify the brand new .tex file without brakeing the programm.
#en *** (eg. add or remove \\newpage)
#en *** If you are ready with it   PRESS >ENTER<
#en[3] *** and the programm will continue.\n''',
        'modify'      : '''*** A program megszakítása nélkül is módosíthatod
*** a friss .tex fájlt. (pl. \\newpage hozzáadása vagy törlése)
*** Ha végeztél, nyomj meg valamilyen gombot, és a program folytatódik.\n''',
#en        'foreword'      : '''Good work. www.roik.bmf.hu/harp/feladatsor''',
        'foreword'      : '''Jó munkát! www.arek.uni-obuda.hu/harp/latex/ec''',
#en         'group'       :  'The exercises of the group "%s": %s',
        'group'       :  '"%s" csoport feladatai: %s',
        'version'     :  'Ehhez a programhoz legalább 2.0-ás Pythonra van szükség.\n(www.python.hu, www.python.org)'}



# Errors
err=  {'endless definition' :
#en                 'There is no end of definition at the input file.',
                'Hiányzó definíció-vége sor a bemeneti fájlban.',
       'exercise missing':
#en                 "There is no such exercise code: %d!",
                'Nincs ilyen feladatkódszám: %d!',
       'not_num':
#en                 'You didn\'t write an (integer) number!',
                'Nem (egész) számot írtál!',
       'small num':
#en                 'You have written a too small integer (minimum %d).',
                'Túl kicsi egészet írtál (minimum %d)!',
       'large num':
#en                 'You have written a too large integer (maximum %d).',
                'Túl nagy egészet írtál (maximum %d)!',
       'bad_arg':
#en                 'Bad argument in "%s" at row %d.: "%s".',
                       'Hibás argumentum a "%s" nevű fájlban a %d. sorban: "%s".',
       'bad_value':
#en                 "You didn't write good values!",
                       'Nem jó értéket írtál!',
       'bad boolean':
#en                 "It isn't 'yes ' or 'not', I use the original.",
                       'Ez nem "igen" vagy "nem", az eredetit hagyom meg.',
       'not enough numbers':
#en                'It must be minimum one exercise in a group!',
               'A csoportban legalább egy feladatnak lennie kell!',
       'bad filename':
#en                'Bad filename: "%s", write a new one. ',
               'Hibás fájlnév: "%s", írj újat. ',
       'not filename':
#en                'There is no filename',
               'nincs megadva fájlnév',
       'file not exists':
#en                        'Not an existing filename: "%s"',
                       'Nem létező fájlnév: "%s"',
       'not exercises':
#en                        'There isn\'t any exercises given.',
                       'Nincsenek megadva feladatok.',
       'codes missing':
#en                        'Not all the codes are valid, check them.',
                       'Nem minden kódszám létezik, vizsgálja meg a beállításokat.',
       'code run out':
#en                 'There is no free code number! Ask for it!\n<ahorvath@roik.bmf.hu>',
                'Nincs több szabad kódszám, kérj újat!\n<ahorvath@roik.bmf.hu>',
       'bad code'    :
#en                        'Bad exercise code at row %d',
                       'Hibás feladatkódszám a %d. sorban',
       'no exercise'    :
#en                        'Bad exercisecode, there isn\'t such a code at file "%s"',
                       'Hibás feladatkódszám "%s", nincs ilyen feladat.',
       'bad code2'    :
#en                        'Bad exercisecode "%s", there isn\'t such an exercise.',
                       'Hibás feladatkódszám, nincs ilyen a "%s" fileban',
       'not var'     :
#en                        'There isn\'t  %s képletben.',
                       'Nincs elhagyható változó a %s képletben.',
       'uncomputable':
#en                        'There are uncomputable values at the exercise number %s.',
                       'A %s-es feladatban van kiszámíthatatlan mennyiség.',
#en        'version'     :  'You need Python 2.0 or newer.\nYours is %s.\n(www.python.org)'}
       'version'     :  'Ehhez a programhoz legalább 2.0-ás Pythonra van szükség. A jelenlegi verzió:\n%s\n(www.python.hu, www.python.org)'}

# 4. The strings, which effects sg. (e.g. interrupt sg.)
#  Usually the lowercase forms are enough.
#en keys=        {'quit':     ['q', 'quit'],
keys=        {'quit':     ['k', 'ki', 'q', 'quit'],
#en          'yes':    ['1', 1, 'y', 'yes'],
         'yes':    ['igen', 'i', '1', 1, 'y', 'yes'],
#en          'no' :    ['n', '0', 0, 'no']}
         'no' :    ['nem' , 'n', '0', 0, 'ne', 'no']}

todo= {'exercises and datas in':
#en            'Give me the exercise-numbers and some other data!',
           'Beolvasom a feladatsorszámokat és pár szükséges adatot',
#en        'test' : 'I test the exercise codes',
       'test' : 'Megvizsgálom a feladatkódszámokat',
       'substitute intervalls':
#en            'I make multiple testpapers with different values',
           'Több példányt csinálok a dolgozatokból különböző számértékekkel',
#en        'check again' : 'I check this exercise again',
       'check again' : 'Ismét megvizsgálom a feladatot',
       }

# 5. IT is useful to do a ...?

# 6. Other things (dictionary)
#en dictionary={'exercises':'Exercises',
dictionary={'exercises':'Feladatok',
#en         'group_name':'Group %s',
        'group_name':'%s csoport',
        'list title':
#en             'List of variations',
            'Variációlista',
        'doctype comment' :
#en          '''% A \\doctype értékei lehetnek: testpaper, plain és draft.\n''',
         '''% A \\doctype értékei lehetnek: testpaper, plain és draft.\n''',
#en       'variation'   :'Variation %d'
      'variation'   :'%d. variáció'
}

menu_list = [('make_testpapers' , 'Feladatok kiválogatása, feladatsor(ok) készítése'),
            ('check_exercise_book', 'Egy feladatgyűjtemény ellenőrzése (kódszámok)'),
          ('check_exercise', 'Egy feladat ellenőrzése (interval)'),
          ('numberer', 'Hiányzó feladatkódszámok elkészítése'),
          ('exit', 'Kilépés')]
