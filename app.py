from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "⚔️ Zero Day Shield está rodando!"

if __name__ == "__main__":
    print("[LOG] Subindo servidor Flask...")
    app.run(debug=True)

# 🔒 Simulando um vazamento proposital
AWS_ACCESS_KEY_ID = "AKIA1234567890EXAMPLE"
AWS_SECRET_ACCESS_KEY = "abc123SECRET/fakeKEYdeEXEMPLO"
