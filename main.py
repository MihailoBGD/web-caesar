from caesar import rotate_string
from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form="""<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form method="post"> 
        <label for="Rotation_number">Rotate by:</label>

        <input id="Rotation_number" type="text" name="rot"/>
        <textarea name="text" cols="30" rows="10">{0}</textarea>
        <input type="submit" />
    </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rotation_number = int(request.form['rot'])
    user_text = request.form['text']
    encrypted_text = rotate_string(user_text, rotation_number)
    return form.format(encrypted_text)




app.run()