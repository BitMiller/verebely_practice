
var szamok = new Array(5, 9, 3, 4);
var tulajdonsag = 3;
var index = 0;

function kivalasztas(x, t, sorszam) {
    let i = 0;

    while (x[i] != t) {
        i++;
    }

    sorszam = i;

    return sorszam;
}

console.log(kivalasztas(szamok, tulajdonsag, index));
