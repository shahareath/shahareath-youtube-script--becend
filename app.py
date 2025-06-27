from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/api/process", methods=["POST"])
def process_video():
    data = request.json
    video_url = data.get("url")
    
    return jsonify({
        "summary": "This video is about something very interesting.",
        "script": "Full transcription of the video goes here.",
        "thumbnail": "https://via.placeholder.com/400x200?text=Thumbnail",
        "main_image": "https://via.placeholder.com/400x200?text=Main+Image"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
