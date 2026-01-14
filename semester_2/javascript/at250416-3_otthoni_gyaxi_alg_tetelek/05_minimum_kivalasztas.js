
var szamok = new Array(5, -8, -12, 30);
var minimum = 0;

function minimum_kivalasztas(x, min) {
    min = 0;

    for (let i = 0; i < x.length; i++) {
        if (x[i] < x[min]) {
            min = i;
        }
    }

    return min;
}

console.log(minimum_kivalasztas(szamok, minimum));
