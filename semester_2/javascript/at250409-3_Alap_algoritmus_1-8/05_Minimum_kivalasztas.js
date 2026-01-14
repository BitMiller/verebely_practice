var szamok = new Array(6, 5, 4, 3);
var min_index;

function minimum_kivalasztas(x, min) {
    min = 0;

    for (let i = 1; i < x.length; i++) {
        if (x[i] < x[min]) {
            min = i;
        }
    }

    return min;
}

console.log("Mini: " + minimum_kivalasztas(szamok, min_index));
