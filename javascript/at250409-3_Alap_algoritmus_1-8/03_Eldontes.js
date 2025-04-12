//var szamok = new Array(66, 4, -9, 3);
var szamok = new Array(65, 3, -9, 3);
var tulajdonsag = 2;
var van_e = false;

function eldontes(x, t, van) {
    let i = 0;

    while (i < x.length && x[i] % t != 0) {
        i = i + 1;
    }

    if (i < x.length) {
        van = true;
    }

    return van;
}

console.log("Van-e? : " + eldontes(szamok, tulajdonsag, van_e));
