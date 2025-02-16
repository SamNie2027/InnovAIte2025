// fileName : server.js 
// Example using the http module
const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());

app.post('/', (req: Request, res: Response) => {
    console.log("Post was called");
    //STUB
});

app.listen(3000, () => {
    console.log("Server has started on port 3000");
});

export default app;