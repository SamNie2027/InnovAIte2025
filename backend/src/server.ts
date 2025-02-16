import { Response } from 'express';
import { PictureRequest } from "../types";

const express = require("express");
const cors = require("cors");
const request = require("request");

const app = express();
app.use(cors());
app.use(express.json()); // ✅ Middleware to parse JSON request body

app.post("/", (req: PictureRequest, res: Response) => {
  console.log("Post was called");
  console.log(req.body); // ✅ This should now correctly log the request body

  request.post(
    {
      headers: { "Content-Type": "application/json" },
      url: "https://innovaite2025-trashcan-api.onrender.com/postImage",
      body: JSON.stringify(req.body), // ✅ Ensure body is properly formatted
    },
    function (error: any, response: { statusCode: any; }, body: string) {
      if (error) {
        console.error("Error in forwarding request:", error);
        return res.status(500).json({ error: "Error forwarding request" });
      }
      console.log("Response from external API:", body);
      res.status(response.statusCode).json(JSON.parse(body)); // ✅ Send the response back
    }
  );
});

app.listen(3000, () => {
  console.log("Server has started on port 3000");
});

module.exports = app;
