var szamok = new Array(7, 44, -32, 19);
var osszeg;

function osszegzes(x, s) {
    s = 0;

    for (let i = 0; i < x.length; i++) {
        s = s + x[i];
    }

    return s;
}

console.log("Összeg: " + osszegzes(szamok, osszeg));
