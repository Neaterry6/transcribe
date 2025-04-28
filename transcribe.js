const multer = require("multer");
const axios = require("axios");
const fs = require("fs");

const upload = multer({ dest: "uploads/" });

const transcribe = async (req, res) => {
  try {
    if (!req.file) return res.status(400).json({ error: "No audio file uploaded!" });

    const audioPath = req.file.path;

    // Send file to Whisper AI for transcription
    const response = await axios.post("https://api.whisper.ai/transcribe", {
      file: fs.createReadStream(audioPath),
    });

    res.json({ transcription: response.data.transcription });
  } catch (error) {
    console.error("Transcription failed:", error);
    res.status(500).json({ error: "Transcription failed!" });
  }
};

module.exports = upload.single("audio"), transcribe;
