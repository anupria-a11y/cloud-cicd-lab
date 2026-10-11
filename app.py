
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Cloud CI/CD Lab</h1>
    <p>Experiment 5: Jenkins Pipeline</p>
    <p>Version 1 - Deployment successful!</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
