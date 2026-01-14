//var szamok = new Array(99, 97, 50, 25);
var szamok = new Array(99, 97, 51, 25);
var tulajdonsag = 2;
var index;

function kereses(x, t, sorszam) {
    let i = 0;

    while (i < x.length && x[i] % t != 0) {
        i = i + 1;
    }

    if (i < x.length) {
        sorszam = i;
    }

    else {
        sorszam = -1;
    }

    return sorszam;
}

console.log("Hol van (-1 = nincs) : " + kereses(szamok, tulajdonsag, index));
