
var szamok = new Array(-5, 8, 9, 50);
var tulajdonsag = 7;
var index = 0;

function kereses(x, t, sorszam) {
    let i = 0;

    while (i < x.length && x[i] != t) {
        i++;
    }

    if (i < x.length) {
        sorszam = i;
    }
    else {
        sorszam = -1;
    }

    return sorszam;
}

console.log(kereses(szamok, tulajdonsag, index));
