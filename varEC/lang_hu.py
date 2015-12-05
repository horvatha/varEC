# -*- coding: utf-8 -*-
#  -*- Python -*-

##################################
#
#  Language section -- Hungarian
#
##################################
# 1. Environments and control sequences
env = {'exercise':'feladat',
     'solution':'megold',
     'group'   :'feladatcsoport'}

# 2. Asks
ask = {        'group_numbers':'Hány csoport legyen? ',
        'group':'%s. csoport neve? (Enter = "%s", "kk" = kilépés) ',
        'exercise':'%s. feladat sorszáma? (Enter = vége) ',
        'exercise code':'Feladat sorszáma? ',
        'file name':'Melyik fájlból? ',
        'file':'Melyik fájlból válogassak? ',
        'enter':'Nyomj >Enter<-t a folytatáshoz, vagy "k"-t a kilépéshez! ',
        'change': 'Kíván változtatni? (Enter = nem, i vagy igen = igen) ',
        'use exercise_numbers': 'Ezt használjam? (Enter = igen, n vagy nem = nem) ',
        'choice': 'Hányadikat választod? ',
        'testpapers num':'Hányféle dolgozatra lesz szükséged? '}

# 3. Messages (errors not)
mesg = {  'next':'Következő lépés: ',
        'file_names':'1. Ebben a csoportban a következő fájlok vannak:',
        'intervals':'\n2. Feladatkódszám intervallumok (pl. 12..14 jelentése: 12, 13, 14):',
        'not_uniq_main':'\n3. A megtalált többször szereplő feladatkódok:',
        'not_uniq':'%d-szer szerepel a %d-es feladatkód!',
        'bad_arg_main':'\n4. Hibás argumentumok:',
        'none':'Nincsen.',
        'group name':'A csoport neve "%s". (bin/setup_hu.py)',
        'not_num':'Nem (egész) számot írtál!\n',
        'founded_exercises':'A megtalált feladatkódszámok:',
        'not enough numbers':'A csoportban legalább egy feladatnak lennie kell!',
        'change because 4a5':'Átírtam a formátumot %s-re a 4a5 oldalstílus miatt!',
        'format':' Formátumok:\nHa pdf-et, ps-t vagy dvi-t írsz, akkor a következő programokat használom: latex - dvips - ps2pdf\n Ha pdflatex-et írsz, akkor a pdflatex programmal fordítok PDF-be.\nHa 0-át írsz vagy tex-et, akkor nem fordítok.\n',
        'with solution': '>'*55 +
                '\n\n Ha feladatokat megoldással szeretnéd kinyomtatni,\n'+
                 ' akkor a kiírt .tex  fájl(ok)ban kell átirni a megjelölt sort.\n\n' +
                '>'*55,
        'file_written':  'Kiírtam a feladatokat a "%s" fájlba.\n',
        'wrote files':  'Kiírtam a következő fájlokat:\n %s\n',
        'translate':  'Most lefordítom a fájlokat. Ez eltart egy darabig.\n',
        'found exercise_numbers': 'Találtam egy alapbeállítást a feladatsorszámokra:',
        'series_in'   :  'Beolvasom a feladatsorszámokat.\n',
        'file opened' :  'Megnyitottam a "%s" nevű fájlt.\n',
        'fixed data'  :  '**** A javított adatok ****',
        'data'  :  '**** A jelenlegi adatok ****',
        'group name'  :  'A csoport neve: "%s"',
        'modify'      : '''*** A program megszakítása nélkül is módosíthatod
*** a friss .tex fájlt. (pl. \\newpage hozzáadása vagy törlése)
*** Ha végeztél, nyomj meg valamilyen gombot, és a program folytatódik.\n''',
        'foreword'      : '''Jó munkát! www.arek.uni-obuda.hu/harp/latex/ec''',
        'group'       :  '"%s" csoport feladatai: %s',
        'version'     :  'Ehhez a programhoz legalább 3.2-es Pythonra van szükség.\n(www.python.hu, www.python.org)'}



# Errors
err = {'endless definition' :
                'Hiányzó definíció-vége sor a bemeneti fájlban.',
       'exercise missing':
                'Nincs ilyen feladatkódszám: %d!',
       'not_num':
                'Nem (egész) számot írtál!',
       'small num':
                'Túl kicsi egészet írtál (minimum %d)!',
       'large num':
                'Túl nagy egészet írtál (maximum %d)!',
       'bad_arg':
                       'Hibás argumentum a "%s" nevű fájlban a %d. sorban: "%s".',
       'bad_value':
                       'Nem jó értéket írtál!',
       'bad boolean':
                       'Ez nem "igen" vagy "nem", az eredetit hagyom meg.',
       'not enough numbers':
               'A csoportban legalább egy feladatnak lennie kell!',
       'bad filename':
               'Hibás fájlnév: "%s", írj újat. ',
       'not filename':
               'nincs megadva fájlnév',
       'file not exists':
                       'Nem létező fájlnév: "%s"',
       'not exercises':
                       'Nincsenek megadva feladatok.',
       'codes missing':
                       'Nem minden kódszám létezik, vizsgálja meg a beállításokat.',
       'code run out':
                'Nincs több szabad kódszám, kérj újat!\n<ahorvath@roik.bmf.hu>',
       'bad code'    :
                       'Hibás feladatkódszám a %d. sorban',
       'no exercise'    :
                       'Hibás feladatkódszám "%s", nincs ilyen feladat.',
       'bad code2'    :
                       'Hibás feladatkódszám, nincs ilyen a "%s" fileban',
       'not var'     :
                       'Nincs elhagyható változó a %s képletben.',
       'uncomputable':
                       'A %s-es feladatban van kiszámíthatatlan mennyiség.',
       'version'     :  'Ehhez a programhoz legalább 2.0-ás Pythonra van szükség. A jelenlegi verzió:\n%s\n(www.python.hu, www.python.org)'}

# 4. The strings, which effects sg. (e.g. interrupt sg.)
#  Usually the lowercase forms are enough.
keys = {'quit':     ['k', 'ki', 'q', 'quit'],
        'yes':    ['igen', 'i', '1', 1, 'y', 'yes'],
        'no':    ['nem', 'n', '0', 0, 'ne', 'no']}

todo = {'exercises and datas in':
        'Beolvasom a feladatsorszámokat és pár szükséges adatot',
        'test': 'Megvizsgálom a feladatkódszámokat',
        'substitute intervalls':
        'Több példányt csinálok a dolgozatokból különböző számértékekkel',
        'check again': 'Ismét megvizsgálom a feladatot',
        }

# 5. IT is useful to do a ...?

# 6. Other things (dictionary)
dictionary = {
    'exercises': 'Feladatok',
    'group_name': '%s csoport',
    'list title': 'Variációlista',
    'doctype comment':
    '''% A \\doctype értékei lehetnek: testpaper, plain és draft.\n''',
    'variation': '%d. variáció'
}
