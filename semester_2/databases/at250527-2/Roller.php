



- #hálózatok #házi #feladat @250519-1-1953

ab-tervezes.pdf

Bali Gábor eredetije:

#tábla: ROLLER
 roller_id
 gyártó_típus
 gyártási_év
 hatótávolság
 akkukapacitás
 karbantartás
 lokáció
 állapot

#tábla: FELHASZNÁLÓ
 felhasználó_id
 név
 telefonszám
 email_cím
 igazolványszám

#tábla: BÉRLÉS
 számla_sorszáma
 felhasználó_id
 roller_id
 bérlés_kezdete
 bérlés_vége
 ár

//1#=====//

Én megoldásom:

//=//

#tábla: #ROLLEREK
 roller_rendszám (elsődleges kulcs)
 roller_típus_id (külső kulcs)
 utolsó_szerviz_ideje
 műszaki_állapot
 akkukapacitás
 jelen_helyszín_id (külső kulcs)
 otthon_depó_id (külső kulcs)

//=//

#tábla: #ROLLER_TÍPUSOK
 roller_típus_id (elsődleges kulcs)
 gyártó
 típus
 évjárat
 hatótávolság

//=//

#tábla: #ÜGYFELEK
 ügyfél_id (elsődleges kulcs)
 név
 nicknév
 telefonszám
 email_cím
 igazolványszám
 egyenleg
 bankszámla_szám

//=//

#tábla: #BÉRLÉSEK
 számla_sorszáma (elsődleges kulcs)
 ügyfél_id (külső kulcs)
 roller_rendszám (külső kulcs)
 bérlés_kezdete
 bérlés_vége
 megtett_km
 (Ár : adódó)

//=//

#tábla: #TÁROLÓK
 tároló_id (elsődleges kulcs)
 helyszín_id (külső kulcs)
 kapacitás
 telítettség

//=//

#tábla: #HELYSZÍNEK
 helyszín_id (elsődleges kulcs)
 gps_koordináták
 cím
 típus

//=//

#tábla: #DEPÓK
 depó_id (elsődleges kulcs)
 helyszín_id (külső kulcs)
 kapacitás
 telítettség

//=//

#tábla: #TRÉLEREK
 rendszám (elsődleges kulcs)
 jelen_helyszín_id (külső kulcs)
 otthon_depó_id (külső kulcs)
 kapacitás
 telítettség

//=//

#tábla: #KARBANTARTÓK
 karbantartó_id (elsődleges kulcs)
 név
 igazolványszám
 jogosítvány
 céges_telefonszám
 privát_telefonszám
 bejelentett_lakcím

//=//

#tábla: #KARBANTARTÁSI_MUNKÁK
 karbantartási_munka_id (elsődleges kulcs)
 depó_id (külső kulcs)
 roller_rendszám (külső kulcs)
 kezdés
 végzés

//=//

#tábla: #ALKATRÉSZEK
 alkatrész_id (elsődleges kulcs)
 megnevezés
 raktáron_darabszám (kiterjeszthető: alkatrész főraktár és per depó darabszám)

//=//

#tábla: #SZERVIZ_MŰVELETEK
 szerviz_művelet_id (elsődleges kulcs)
 megnevezés
 ár
 normaidő

//1#=====//

#Kapcsolótáblák:

#kapcsoló #tábla: #CSAPAT_PER_KARBANTARTÁSI_MUNKA
 karbantartási_munka_id (külső kulcs)
 karbantartó_id (külső kulcs)

//=//

#kapcsoló #tábla: #MŰVELET_PER_KARBANTARTÁSI_MUNKA
 karbantartási_munka_id (külső kulcs)
 szerviz_művelet_id (külső kulcs)

//=//

#kapcsoló #tábla: #ALKATRÉSZ_PER_KARBANTARTÁSI_MUNKA
 karbantartási_munka_id (külső kulcs)
 alkatrész_id (külső kulcs)

//1#=====//

#Értékek:

Szerviz műveletek > Megnevezés :

csavarcsavarás
lengéscsillapító felszabályzás
dezintegrálás
váltóolaj higítás
fékfolyadék habosítás
killer paintjob
akksi felfúrás
alulvizsgálat
felvázcsere
komplett csere

felülvizsgálat
alvázcsere
deponálás/dedeponálás
mosás

//=//

Alkatrészek > Megnevezés

peres gumi
fékszíjkészlet
axiális tűs kormánycsapágy
figyegő bilimbasz
keresztszövött helikális aszinkron tekercs
ülésvégkónusz kontraktor gyűrű
aku pakk
a kupak
síkdugattyú
ballaszt homok

keresztreteszes fogasléc
dupla bekezdéses, finom zsinórmenetes, d fejű, belső kulcsnyílású, 8.8, rozsdamentes M8 csavar
jobb villogó
bal villogó


//=//

ügyfelek:

Fedél Adél
Szekeres-Nagy Lóránt
Kovács Gültem
Pitymalló Álmos
Kabinet Ilona
Retyerát Ramóna
Lándzsarázó Vilmos
Bojtor János
Fabula Katalin
Handreisz Mátyás


//=//

Karbantartók:

Bekő Antal
Gurtni Gáspár
Tudom Ányos
Kocsis Ottokár
Kardán Gergely
Whitworth Vilmos
Gályos Eszter
Kurbli Kálmán
Wankel Endzsi
Kármentő Károly

//=//

Műszaki állapot:

(lehetne bonyolítani külön táblákkal, de most: )
jó
nem rossz
nem jó
rossz

//=//

Akkukapacitás:
%-ban
bizonyos % alatt akksicserét jelez a rendszer a karbantartás számára

//=//

Helyszínek >
(legyen egy "külső / úton van / get act gps coords" rekord is)
 > GPS koordináták: N/A
 > Cím: N/A
 > Típus: helyközi

//=//

Nicknév:

Kihaennem
AnyamAddElAHazat
SpeedoPeter
kikerdezi
Anyonimusz
MucuszKutyusz
fgsdgx
MagnoliaRajongo
Eperecot
hERECEGNO

//=//

e-mail:

//=//

telefonszám:

+36 45 684 1398
+36 60 672 2948
+36 60 446 7264
+36 60 611 3539
+36 90 335 5886
+36 90 414 9233
+36 60 899 7664
+36 90 868 7786
+36 60 245 6387
+36 60 151 4928

+36 45 584 1398
+36 60 572 2948
+36 60 346 7264
+36 60 511 3539
+36 90 235 5886
+36 90 314 9233
+36 60 799 7664
+36 90 768 7786
+36 60 145 6387
+36 60 951 4928

+36 90 978 1444
+36 90 465 7912
+36 45 487 6744
+36 60 342 8524
+36 90 193 4742
+36 45 781 1885
+36 45 665 4322
+36 45 466 6732
+36 60 983 6525
+36 90 433 8768

//=//

helyszínek:

Bp. 1066, Trigon 3.
47.505246,19.063413

Bp. 1098, Négyszög körönd 256.
47.467248,19.115979

Bp. 1037, Csillagvölgyi lejtő 321.
47.560385,19.029683

Bp. 1125, Szépasszony tölgye 94/g
47.509412,19.014023

Bp. 1081, Pipi tér 14/b
47.497030,19.079786

Bp. 1125, Isten háta dűlő 4.
47.501720,19.006635

Bp. 1025, Orrfú utca 2.
47.519479,19.028562

Bp. 1125, Tündér utca 42.
47.498902,18.999240

Bp. 1026, Pasasérti út 100.
47.520561,18.999305

Bp. 1147, Zug köz 1.
47.518761,19.117764

