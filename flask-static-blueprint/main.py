from flask import Flask, url_for, render_template
from admin.second import second

app = Flask(__name__)
app.register_blueprint(second, url_prefix="/admin")

@app.route("/home")
@app.route("/")
def teste():
  return "<h1>Test</h1>"

if __name__ == "__main__":
  app.run(debug=True)
