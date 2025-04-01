const szamok1 = new Array(4, 63, 3, 76, 15, 63, 2, 5, 87, 29);
const szamok2 = new Array(1, 63, 3, 75, 15, 63, 7, 5, 87, 29);
const szamok3 = new Array(4, 66, 8, 76, 14, 62, 2, 6, 88, 24);

var szamok = szamok3;

function hany_paros(szam_tomb) {
    let hany = 0;

    for (let i = 0; i < szam_tomb.length; i++) {
        if (szam_tomb[i] % 2 == 0) hany++;
    }

    return hany;
}

console.log("A [" + szamok + "] számok között " + hany_paros(szamok) + " darab páros szám létezik.");