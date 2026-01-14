var szamok = new Array(8, 9, 5, -6);
var tulajdonsag = 2;
var valogatott = new Array();

function kivalogatas(x, t, y) {
    let szamlalo = 0;

    for (let i = 0; i < x.length; i++) {
        if (x[i] % t == 0) {
            y[szamlalo] = x[i];
            // y.push(x[i]);
            szamlalo = szamlalo + 1;
        }
    }

    return y;
}

console.log("Ezek már csak ilyenek: " + kivalogatas(szamok, tulajdonsag, valogatott));
