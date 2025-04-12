//var szamok = new Array(-66, 5, 80, 43);
var szamok = new Array(-65, 5, 80, 43);
var tulajdonsag = 2;
var index;

function kivalasztas(x, t, sorszam) {
    let i = 0;

    while (x[i] % t != 0) {
        i = i + 1;
    }

    sorszam = i;

    return sorszam;
}

console.log("Itt van-e! : " + kivalasztas(szamok, tulajdonsag, index));
