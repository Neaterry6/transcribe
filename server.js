const express = require("express");
const transcribe = require("./transcribe");

const app = express();
app.use(express.json());

app.post("/transcribe", transcribe);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`🚀 Transcribe API running on http://localhost:${PORT}`))
