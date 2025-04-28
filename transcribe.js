const express = require("express");
const multer = require("multer");
const fs = require("fs");
const axios = require("axios");

const upload = multer({ dest: "uploads/" });
const app = express();

app.post("/transcribe", upload.single("audio"), async (req, res) => {
    if (!req.file) {
        return res.status(400).json({ error: "❌ No audio file received! Please upload a valid file." });
    }

    try {
        const audioPath = req.file.path;

        // Send file to Whisper AI for transcription
        const response = await axios.post("https://api.whisper.ai/transcribe", {
            file: fs.createReadStream(audioPath),
        });

        res.json({ transcription: response.data.transcription });
    } catch (error) {
        console.error("❌ Transcription failed:", error);
        res.status(500).json({ error: "Transcription service is down!" });
    }
});

app.listen(3000, () => console.log("🚀 Transcribe API running on port 3000"));
