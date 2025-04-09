var szamok = new Array(-2, 3, 53, 8);
var szum = 0;

function osszegzes(tomb, s) {
    s = 0;

    for (let i = 0; i < tomb.length; i++) {
        s = s + tomb[i];
    }

    return s;
}

console.log("Az összeg: " + osszegzes(szamok, szum));

