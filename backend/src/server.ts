import { Response } from "express";
import { PictureRequest } from "../types";

const express = require("express");
const cors = require("cors");
const request = require("request");

const app = express();
app.use(express.json({ limit: "100mb" })); // increasing size limit
app.use(cors());
app.use(express.json()); // ✅ Middleware to parse JSON request body

app.post("/", (req: PictureRequest, res: Response) => {
  console.log("Post was called");
  console.log(req.body); // ✅ This should now correctly log the request body

  request.post(
    {
      headers: { "Content-Type": "application/json" },
      url: "https://innovaite2025-trashcan-api.onrender.com/submitImage",
      body: JSON.stringify(req.body),
    },
    function (error: any, response: { statusCode: number }, body: string) {
      if (error) {
        console.error("Error in forwarding request:", error);
        return res.status(500).json({ error: "Error forwarding request" });
      }

      // Log the response body for debugging
      console.log("Response from external API:", body);

      // Ensure the response body is valid JSON before parsing
      try {
        const parsedBody = JSON.parse(body);
        res.status(response.statusCode).json(parsedBody);
      } catch (jsonError) {
        console.error("Failed to parse response body:", jsonError);
        res.status(500).json({ error: "Error parsing response body" });
      }
    }
  );
});

app.listen(3000, () => {
  console.log("Server has started on port 3000");
});

module.exports = app;
