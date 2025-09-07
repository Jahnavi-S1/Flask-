from flask import Flask, request, jsonify
import hashlib, time

app = Flask(__name__)

store = []  # temporary in-memory storage

@app.post("/ingest")
def ingest():
    data = request.get_data()
    sha = hashlib.sha256(data).hexdigest()
    store.append({
        "ts": time.time(),
        "raw": data.decode(),
        "sha256": sha
    })
    return jsonify({"ok": True, "sha256": sha})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
print ("welcome")
print ("Flaskbranch")
print ("Flask")
