from caesar import rotate_string
from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form="""<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form method="post"> 
        <label for="Rotation_number">Rotate by:</label>
        <input id="Rotation_number" type="text" name="rot"/><textarea name="textarea" name="text" id="" cols="30" rows="10"></textarea>
        <input type="submit" />
    </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    



app.run()