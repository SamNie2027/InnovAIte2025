// fileName : server.js

import { PictureRequest } from "../types";

// Example using the http module
const express = require("express");
const cors = require("cors");
var request = require("request");

const app = express();
app.use(cors());

app.post("/", (req: PictureRequest, res: Response) => {
  console.log("Post was called");
  console.log(req.body);
  request.post(
    {
      headers: { "content-type": "application/json" },
      url: 'https://innovaite2025-trashcan-api.onrender.com/postImage',
      body: req.body,
    },
    function (error: Error, response: Response, body: any) {
      console.log(body);
    }
  );
});

app.listen(3000, () => {
  console.log("Server has started on port 3000");
});

export default app;
