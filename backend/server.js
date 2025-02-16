// fileName : server.js 
// Example using the http module
const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());

app.post('/', (req, res) => {
    console.log("Post was called");
    res.send('post');
    //STUB
});

app.listen(3000, () => {
    console.log("Server has started on port 3000");
});

export {};