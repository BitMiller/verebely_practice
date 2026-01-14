var szamok = new Array(5, 8, 10, 11);
var tulajdonsag = 2;
var darab;

function megszamlalas(tomb, t, db) {
    db = 0;

    for (let i = 0; i < tomb.length; i++) {
        if (tomb[i] % t == 0) {
            db = db + 1;
        }
    }

    return db;
}

console.log("Ennyi szám osztható " + tulajdonsag + "-val/-vel: " + megszamlalas(szamok, tulajdonsag, darab));


