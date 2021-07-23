const {spawn} = require("child_process");
const python = spawn("python3", ["inference.py"]);
const buf = [];

// TODO: read from form data
var data = [[0.00632, 18, 2.31, 0, 0.538, 6.575,
             65.2, 4.09, 1, 296, 15.3, 396.9, 4.98]];

// send data to python inference code
python.stdin.write(JSON.stringify(data));
python.stdin.end();

// get the response
// TODO: return to frontend
python.stdout.on("data", (output) => {
    buf.push(output);
})
python.stdout.on("end", () => {
    console.log(JSON.parse(buf));
})