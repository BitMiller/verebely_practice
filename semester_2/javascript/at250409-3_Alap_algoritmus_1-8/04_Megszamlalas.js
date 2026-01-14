var szamok = new Array(-7, 88, 4, 13);
var tulajdonsag = 2;
var darab;

function megszamlalas(x, t, db) {
    db = 0;

    for (let i = 0; i < x.length; i++) {
        if (x[i] % t == 0) {
            db = db + 1;
        }
    }

    return db;
}

console.log("Ennyi van: " + megszamlalas(szamok, tulajdonsag, darab));
