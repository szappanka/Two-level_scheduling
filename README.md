# Tobbszintu_utemezo

Fakultatív feladat: többszintű ütemező megvalósítása
Beadható: 2021. április 11. (vasárnap)

Becsült programozási idő: >5 óra
A feladatbeküldés általános tudnivalói

Készítsen egy programot Java vagy Python nyelven, amely egy összetett ütemező működését szimulálja!

A globálisan preemptív, statikus prioritásos ütemező az alábbi ütemezési algoritmusokat futtatja az egyes szinteken az előadáson ismertetett módon:

- 1. magas prioritású szint (prioritás = 1) SJF ütemező
- 2. alacsony prioritású szint (prioritás = 0) RR ütemező, időszelet: 2
## Bemenet (standard input, stdin)
Soronként egy (max. 10) taszk adatai. Egy sor felépítése (vesszővel elválasztva):

- a taszk betűjele (A, B, C...)
- a taszk prioritása (0 vagy 1)
- a taszk indítási ideje (egész szám >= 0), a következő időszeletben már futhat (0: az ütemező indításakor már létezik), egyszerre érkező taszkok esetén az ABC-sorrend dönt
- a taszk CPU-löketideje (egész szám >= 1)
Példa:

A,0,0,6
B,0,1,5
C,1,5,2
D,1,10,1
A bemenet végét EOF jelzi (előtte soremelés biztosan van, és üres sor is előfordulhat).

## Kimenet (standard output, stdout)
A kimenet első sorában a taszkok futási sorrendje betűjeleikkel (csak betűk, szóközök nélkül).
A második sorban a teljes várakozási idő taszkonként, érkezésük (nem feltétlenül abc-) sorrendjében, az alábbi formában (vesszővel elválasztva, szóközök nélkül):

1. taszk betűjel:várakozási idő,2. betűjel:várakozási idő, ...

Példa (a fenti bemenetre adott válasz):

ABACBADBA
A:8,B:6,C:0,D:0
## Értékelés
Összesen 3 pont jár, ha minden teszten átmegy a megoldásuk. Arányosan kevesebb pont jár, ha nem minden esetben működik helyesen a programjuk.

## Technikai információk
A programot a HF portálon kell leadni a megadott határidőig egyetlen ZIP fájlba csomagolva. A feltöltött fájlok (a ZIP és a tartalmának) neve ékezetes betűt és szóközt ne tartalmazzon!

A portál automatikusan kiértékeli a programot, és visszajelzést küld a működéséről. A kiértékelésre nincs időbeli garancia. A program bármikor újra beküldhető a határidőig. A beadási határidő leteltekor a legutolsó feltöltött program beadottá válik, annak értékelése adja a végleges pontszámot.

A beküldött Java 8 programnak tartalmaznia kell egy "Main" nevű osztályt, melynek része a feladatot megoldó "main" függvény. A program tetszőleges számú forrásfájlból állhat. A program nem használhat a standard inputon és outputon kívül semmilyen más erőforrást, így nem végezhet fájlműveleteket és nem nyithat hálózati kapcsolatokat.

Python megoldás beküldése esetén a Python 3 verzióval kompatibilis megoldásokat fogadunk el, csak standard függvények használhatók (külső könyvtár, pl. NumPy nem), és a feltöltött ZIP fájlban egy db .py fájl lehet, más nem. Itt sem végezhetnek fájlműveleteket, nem nyithatnak meg hálózati kapcsolatokat.

## Tesztadatok
Az első beküldés előtt érdemes az alábbi tesztekkel megpróbálkozni.

A,0,2,7
B,0,2,3
ABABA
A:3,B:4
Q,0,5,8
P,1,7,2
QPQ
Q:2,P:0
A,0,0,3
B,1,0,2
C,0,3,3
D,1,4,1
BADCAC
A:5,B:0,C:3,D:0
