const csv = require("csv-writer");
const express = require("express");
const fs = require("fs");
const json2csv = require("json2csv").parse

// global variables
const header = [
    "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM",
    "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", 
    "LSTAT", "MEDV"
];

var d = [{}];
for (i = 0; i < header.length; i++) {
    d[0][header[i]] = 0.1;
}

// csv functions
const write = async (fileName, fields, data) => {
    var rows;
    if (!fs.existsSync(fileName)) {
        rows = json2csv(data, {header: true});
    } else {
        rows = json2csv(data, {header: false});
    }
    fs.appendFileSync(fileName, rows);
    fs.appendFileSync(fileName, "\r\n");
}

// app
const app = express();
const port = 3000;

app.get('/', (request, response) => {
    // write("copy.csv", header, d);
    response.send("Hello world!");
})

app.listen(port, () => {
    console.log("Listening");
})