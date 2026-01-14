//var szamok = new Array(2, 5, -8, 55);
var szamok = new Array(1, 5, -7, 55);
var tulajdonsag = 2;
var van = false;

function eldontes(tomb, t, v) {
    i = 0;

    while (i < tomb.length && tomb[i] % t != 0) {
        i = i + 1;
    }

    if (i < tomb.length) {
        v = true;
    }

    return v;
}

console.log("Van-e olyan, ami osztható " + tulajdonsag + "-val/-vel? : " + eldontes(szamok, tulajdonsag, van));
