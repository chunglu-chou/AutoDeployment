const express = require('express');
const {spawn} = require('child_process');

const python = spawn('python3', ['-W', 'ignore', 'inference.py']);
const buf = [];

const app = express();
const port = 3001;

app.use(express.json());

app.post('/inference', (req, res) => {
    // transform data to 2D array
    data = [[]]
    for (var key in req.body) {
        data[0].push(req.body[key]);
    }

    // send data to python inference code
    python.stdin.write(JSON.stringify(data));
    python.stdin.end();

    // get the response and return
    python.stdout.on('data', (output) => {
        buf.push(output);
    })
    python.stdout.on('end', () => {
        res.send(''+JSON.parse(buf));
    })
})

app.listen(port, () => {
    console.log('listening on port: ', port);
})