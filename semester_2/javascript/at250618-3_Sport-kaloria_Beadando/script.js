/*
Hibája még @250621-6-2310
Paste-zés után nem triggerelődik az input event, így nem hívódik meg a calculate(), és a kcal mezőt nem számolja le az adott sornál.
*/

var e_calcBody                = document.getElementById("id_calcBody");
var e_tableScaler             = document.getElementById("id_tableScaler");
var e_in_kcalPerH_sum         = undefined;
var e_in_min_sum              = undefined;
var e_in_kcal_sum             = undefined;
var e_span_dailyCaloryPercent = undefined;
var e_bt_clearData            = undefined;

class Sport {
    e_min    = undefined;
    e_kcal   = undefined;
    name     = undefined;
    kcalPerH = undefined;
    e_name   = undefined;

    constructor(name, kcalPerH, e_name) {
        this.name     = name;
        this.kcalPerH = kcalPerH;
        this.e_name   = e_name;
    }
}

var tableColumns = ["Sport, mozgás", "kcal/óra", "perc", "kcal"];
var sports = [
    new Sport("Futás",       680,  "futas"),             // Hupás
    new Sport("Focizás",     550,  "focizas"),          // H*kizás
    new Sport("Bringázás",   480,  "bringazas"),       // Ingázás
    new Sport("Hegymászás",  430,  "hegymaszas"),     // Gyámbászás
    new Sport("Lovaglás",    360,  "lovaglas"),      // Vonaglás
    new Sport("Túrázás",     350,  "turazas"),      // Turházás
    new Sport("Kajakozás",   330,  "kajakozas")    // Kakajózás
//  new Sport("Bérmálkozás", 9001, "bermalkozas") // Over 9000 !!!!! :O :O :O
];

initTable();

/* ******** */
/* ******** */
/* ******** */

function initTable() {
    let table = document.createElement("table");
    table.id = "id_calcTable";

// Spawn table header:

    let tableRow = document.createElement("tr");

    for (let i = 0; i < tableColumns.length; i++) {
        let tableCell = document.createElement("th");
        tableCell.innerHTML = tableColumns[i];
        tableRow.appendChild(tableCell);
    }

    table.appendChild(tableRow);

// Spawn table main body with the sports' data:

    for (let i = 0; i < sports.length; i++) {
        tableRow = document.createElement("tr");

        let tableCell = document.createElement("td");
        tableCell.innerHTML = sports[i].name;
        tableRow.appendChild(tableCell);

        tableCell = document.createElement("td");
        let input = document.createElement("input");
        input.type = "text";
        input.readOnly = true;
        input.value = sports[i].kcalPerH;
        input.classList.add("cl_in_kcalPerH");
        tableCell.appendChild(input);
        tableRow.appendChild(tableCell);

        tableCell = document.createElement("td");
        input = document.createElement("input");
        sports[i].e_min = input;
        input.addEventListener("keydown", filterInput);
        input.addEventListener("paste", filterPaste);
        input.addEventListener("input", calculate);
        //input.style.backgroundColor = "red";
        input.type = "text";
        input.value = 0;
        input.id = "id_in_min_" + sports[i].e_name;
        input.classList.add("cl_in_min");
        tableCell.appendChild(input);
        tableRow.appendChild(tableCell);

        tableCell = document.createElement("td");
        input = document.createElement("input");
        sports[i].e_kcal = input;
        input.type = "text";
        input.readOnly = true;
        input.value = 0;
        input.id = "id_in_kcal_" + sports[i].e_name;
        input.classList.add("cl_in_kcal");
        tableCell.appendChild(input);
        tableRow.appendChild(tableCell);

        table.appendChild(tableRow);
    }

// Spawn the summarizing row:

    tableRow = document.createElement("tr");

    let tableCell = document.createElement("td");
    tableCell.innerHTML = "Összesen:";
    tableRow.appendChild(tableCell);

    tableCell = document.createElement("td");
    let input = document.createElement("input");
    e_in_kcalPerH_sum = input;
    input.type = "text";
    input.readOnly = true;
    input.value = 0;
    input.classList.add("cl_in_kcalPerH_sum");
    tableCell.appendChild(input);
    tableRow.appendChild(tableCell);

    tableCell = document.createElement("td");
    input = document.createElement("input");
    e_in_min_sum = input;
    input.type = "text";
    input.readOnly = true;
    input.value = 0;
    input.id = "id_in_min_sum";
    input.classList.add("cl_in_min_sum");
    tableCell.appendChild(input);
    tableRow.appendChild(tableCell);

    tableCell = document.createElement("td");
    input = document.createElement("input");
    e_in_kcal_sum = input;
    input.type = "text";
    input.readOnly = true;
    input.value = 0;
    input.id = "id_in_kcal_sum";
    input.classList.add("cl_in_kcal_sum");
    tableCell.appendChild(input);
    tableRow.appendChild(tableCell);

    table.appendChild(tableRow);

// Spawn the calory percent part:

    tableRow = document.createElement("tr");
    tableCell = document.createElement("td");
    tableCell.colSpan = 4;
    //tableCell.style.backgroundColor = "red";
    tableCell.style.paddingLeft = "10px";
    tableCell.style.paddingRight = "20px";
    tableCell.style.paddingTop = "20px";
    tableCell.style.paddingBottom = "20px";
    tableCell.style.fontSize = "95%";
    tableCell.style.textAlign = "left";

    let newSpan = document.createElement("span");
    newSpan.innerHTML = "Napi energiaszükséglet (2000 kcal) arányában:&nbsp;&nbsp;";
    tableCell.appendChild(newSpan);

    newSpan = document.createElement("span");
    newSpan.id = "id_span_dailyCaloryPercent";
    e_span_dailyCaloryPercent = newSpan;
    newSpan.textContent = "0";
    tableCell.appendChild(newSpan);

    newSpan = document.createElement("span");
    newSpan.classList.add("cl_bold");
    newSpan.innerHTML = "&nbsp;%";
    tableCell.appendChild(newSpan);

    tableRow.appendChild(tableCell);

    table.appendChild(tableRow);

// Spawn the data clearing button:

    tableRow = document.createElement("tr");
    tableCell = document.createElement("td");
    tableCell.colSpan = 4;
    tableCell.style.textAlign = "center";
    let newButton = document.createElement("button");
    newButton.id = "id_bt_clearData";
    e_bt_clearData = newButton;
    newButton.textContent = "Adatok törlése";
    newButton.addEventListener("click", zeroOutData);

    tableCell.appendChild(newButton);
    tableRow.appendChild(tableCell);

    table.appendChild(tableRow);

    //e_calcBody.appendChild(table);
    e_tableScaler.appendChild(table);
}

/* ******** */
/* ******** */
/* ******** */

function filterInput(e) {
    const allowedKeys = [
        "Backspace", "Delete", "ArrowLeft", "ArrowRight", "Tab", "Escape", "Enter", "Home", "End"
    ];
    const isDigit = e.key >= "0" && e.key <= "9";
    const isShortcut = e.ctrlKey || e.metaKey;

    if (!isDigit && !allowedKeys.includes(e.key) && !isShortcut) {
        e.preventDefault();
    }
}

/* ******** */
/* ******** */
/* ******** */

function filterPaste(e) {
    e.preventDefault();

    const pasted = e.clipboardData.getData("text");

    if (/^\d+$/.test(pasted)) {
        e.target.value = pasted.substring(0, 3); // 01234
    }
}

/* ******** */
/* ******** */
/* ******** */

function calculate() {

    let min_sum = 0;
    let kcal_sum = 0;

    for (let i = 0; i < sports.length; i++) {
        fieldCorrection(sports[i].e_min);
        if (parseInt(sports[i].e_min.value) == 0) sports[i].e_kcal.value = 0; // Avoid division by zero
        else sports[i].e_kcal.value = Math.round(sports[i].kcalPerH / 60 * sports[i].e_min.value);
        min_sum += parseInt(sports[i].e_min.value);
        kcal_sum += parseInt(sports[i].e_kcal.value);
    }

    e_in_min_sum.value = min_sum;
    e_in_kcal_sum.value = kcal_sum;
    if (parseInt(min_sum) == 0) e_in_kcalPerH_sum.value = 0; // Avoid division by zero
    else e_in_kcalPerH_sum.value = Math.round(kcal_sum * 60 / min_sum);
    e_span_dailyCaloryPercent.innerHTML = Math.round(100 / 2000 * kcal_sum);
}

/* ******** */
/* ******** */
/* ******** */

function fieldCorrection(el) {
    let intValue = parseInt(el.value);
    if (isNaN(intValue)) el.value = 0;
    else el.value = intValue.toString().substring(0, 3);
}

/* ******** */
/* ******** */
/* ******** */

function zeroOutData() {
    for (let i = 0; i < sports.length; i++) {
        sports[i].e_min.value = 0;
        sports[i].e_kcal.value = 0;
    }

    e_in_kcalPerH_sum.value = 0;
    e_in_min_sum.value = 0;
    e_in_kcal_sum.value = 0;
    e_span_dailyCaloryPercent.innerHTML = "0";
}



