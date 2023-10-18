const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
        res.send('Hello DevOps team!');
        console.log(res);
});

app.get('/kss', (req, res) => {
    res.send('This is a demo for Apprunner KSS');
    console.log(res);
});

app.listen(port, () => {
    console.log(`This app is listing at http://localhost:${port}`);
});
