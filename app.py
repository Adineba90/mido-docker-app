from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head><title>Mido Docker App</title></head>
    <body style="font-family:Arial; text-align:center; padding:50px; background:#f4f4f4;">
        <div style="background:white; padding:40px; border-radius:16px; max-width:500px; margin:auto; box-shadow:0 4px 20px rgba(0,0,0,0.1);">
            <h1 style="color:#4F46E5;">🐳 Mido Docker App</h1>
            <p style="color:#555;">Built by <strong>Adineba Kweku</strong></p>
            <p style="color:#555;">Running inside a Docker container</p>
            <p style="color:#555;">Deployed via GitHub Actions to GHCR</p>
            <div style="margin-top:20px;">
                <span style="background:#EEF2FF; color:#4F46E5; padding:6px 14px; border-radius:20px; margin:4px; display:inline-block;">Docker</span>
                <span style="background:#EEF2FF; color:#4F46E5; padding:6px 14px; border-radius:20px; margin:4px; display:inline-block;">Flask</span>
                <span style="background:#EEF2FF; color:#4F46E5; padding:6px 14px; border-radius:20px; margin:4px; display:inline-block;">GitHub Actions</span>
                <span style="background:#EEF2FF; color:#4F46E5; padding:6px 14px; border-radius:20px; margin:4px; display:inline-block;">GHCR</span>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)