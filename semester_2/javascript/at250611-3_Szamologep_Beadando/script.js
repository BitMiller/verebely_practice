
var e_display = document.getElementById("id_display");
var e_message = document.getElementById("id_message");

var parts = new Array(5);
var cursor;

Clear();

// ******************* //
// ******************* //
// ******************* //

function InitParts() {
    parts[0] = "+";
    parts[1] = "0";
    parts[2] = undefined;
    parts[3] = "0";
    parts[4] = undefined;
}

// ******************* //
// ******************* //
// ******************* //

function Clear() {
    ClearMessage();
    e_display.value = "0";
    cursor = 1;
    InitParts();
}

// ******************* //
// ******************* //
// ******************* //

function ClearMessage() {
    e_message.innerHTML = "&nbsp";
}

// ******************* //
// ******************* //
// ******************* //

function InsertDigit(d) {
    console.log(d + " inserted!");

    if (cursor == 1 || cursor == 3) {
        if (parts[cursor].length >= 4) {
            e_message.innerHTML = "Csak 4 számjegyig megy a Rock 'n Roll!";
        }
        else {
            ClearMessage();

            if (parts[cursor] == "0") {
                if (d != 0) {
                    parts[cursor] = d.toString();
                }
            }
            else {
                parts[cursor] += d.toString();
            }
        }
    }
    else if (cursor == 2) {
        cursor = 3;
        InsertDigit(d);
    }
    else if (cursor == 4) {
        Clear();
        InsertDigit(d);
    }

    UpdateDisplay();
}

// ******************* //
// ******************* //
// ******************* //

function InsertOperator(o) {
    console.log(o + " inserted!");

    if (o == "-" && cursor == 1 && parts[1] == "0") {
        parts[0] = parts[0] == "-" ? "+" : "-";
    }
    else {
        cursor = 3;
        parts[2] = o;
    }

    console.log("cursor: " + cursor);

    UpdateDisplay();
}

// ******************* //
// ******************* //
// ******************* //

function Evaluate() {

    if (cursor == 4) {
        e_message.innerHTML = "Másodjára sem lesz más az eredmény.";
    }
    else if (parts[2] == undefined) {
        e_message.innerHTML = "Legalább egy műveleti jelet adj be, kérlek!";
    }
    else if (parts[2] == "/" && Number(parts[3]) == 0) {
        e_message.innerHTML = "A nullával osztás feketelyukat generál Einstein sírja fölött!";
    }
    else {
        e_message.innerHTML = "&nbsp;";

        parts[4] = "=";
        cursor = 4;

        let result = Number(parts[1]);
        if (parts[0] == '-') {
            result *= -1;
            //result = -result;
            //result -= result * 2;
        }

        switch (parts[2]) {
            case "/":
                result /= Number(parts[3]);
                break;
            case "*":
                result *= Number(parts[3]);
                break;
            case "-":
                result -= Number(parts[3]);
                break;
            case "+":
                result += Number(parts[3]);
                break;
            default:
                break;
        }

        UpdateDisplay();
        e_display.value += " " + Math.round(result, 3);
        e_display.scrollLeft = e_display.scrollWidth;
    }
}

// ******************* //
// ******************* //
// ******************* //

function UpdateDisplay() {
    e_display.value = "";
    let i = 0;
    if (parts[0] == "+") {
        i = 1;
    }

    while (i < parts.length && parts[i] != undefined) {
        if (!(i == 3 && parts[3] == 0 && parts[4] == undefined)) {
            e_display.value += parts[i];
        }
        i++;
    }
}




