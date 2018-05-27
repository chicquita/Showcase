import funkce
import kategorie

tabulka_zasob = funkce.select_all(
	"SELECT z.id, z.baleni, p.nazev, p.kj, mj.zkratka, z.baleni * p.kj FROM zasoby z JOIN potraviny p on z.id_potraviny = p.id JOIN merna_jednotka mj on p.id_merna_jednotka = mj.id")
#print (tabulka_zasob)

denni_prijem_kj = funkce.select_single_value("SELECT u.denni_prijem_kj FROM uzivatel u WHERE id = 1")
#print(denni_prijem_kj)

kj_potrebne_snidane = int(denni_prijem_kj/100*20)
#kj_potrebne_snidane = 100000															# doporucene rozlozeni chodu: snidane 20-25%
kj_potrebne_svacina1 = int(denni_prijem_kj/100*10)			# svacina 10-15%
kj_potrebne_obed = int(denni_prijem_kj/100*35)				# obed 30-35%
kj_potrebne_svacina2 = int(denni_prijem_kj/100*15)			# svacina 10-15%
kj_potrebne_vecere = int(denni_prijem_kj/100*20)			# vecere 15-20%


kj_potrebne_snidane_K1 = kj_potrebne_snidane*0.5
#kj_potrebne_snidane_K1 = 2000000

kategorie.TABULKA_ZASOB = funkce.velky_select()
#print(logika_vypoctu(kategorie.snidane["slane_pecivo"], 700))

print("KJ potrebne ke snidani: {}".format(kj_potrebne_snidane))
#print("KJ potrebne ke snidani K1: {}".format(kj_potrebne_snidane_K1))

funkce.vytvor_snidani(kj_potrebne_snidane)

print("KJ potrebne ke obedu: {}".format(kj_potrebne_obed))


funkce.vytvor_obed(kj_potrebne_obed)



#kdyz to vybere kategorii, kde nic nemam v zasobach, musi to vybrat jinou kategorii!!!!
# opravit salaty!!!!
# krati to porce u veci, co jsou na kus (chce to vzit napr 0,8 ks, coz se zaokrouhlenim 
#vypise jako nula a pak se i kalorie nasobi nulou,takze vychazi nula )