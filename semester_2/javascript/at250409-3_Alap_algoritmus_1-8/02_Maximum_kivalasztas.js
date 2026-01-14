var szamok = new Array(56, 7, -24, 3);
var max_index;

function maximum_kivalasztas(x, max) {
    max = 0;

    for (let i = 1; i < x.lenght; i++) {
        if (x[i] > x[max]) {
            max = i;
        }
    }

    return max;
}

console.log("Max index: " + maximum_kivalasztas(szamok, max_index));
