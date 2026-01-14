const szamok1 = new Array(4, 63, 3, 76, 15, 63, 2, 5, 87, 29);
const szamok2 = new Array(1, 63, 3, 75, 15, 63, 7, 5, 87, 29);

var szamok = szamok1;

function doncsed_van_e_paros(szam_tomb) {
    let i = 0;

    while (i < szam_tomb.length && szam_tomb[i] % 2 == 1) {
        i++;
    }

    let van = false;
    if (i < szam_tomb.length) { van = true; }
    return van;
//    return i < szam_tomb.length;

}

console.log("Van-e páros szám a " + szamok + " között? : " + (doncsed_van_e_paros(szamok) ? "jesz" : "nyet"));
