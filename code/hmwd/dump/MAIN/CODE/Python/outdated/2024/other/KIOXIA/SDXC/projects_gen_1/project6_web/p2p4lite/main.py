from flask import Flask, render_template_string, request
from flask import Flask, render_template_string, request, redirect, url_for
import main_back
app = Flask(__name__)

# HTML Template
html_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>localhost</title>
</head>
<body>
    <h1>Enter Command</h1>
    <form method="POST">
        <label for="user_input">Input:</label>
        <input type="text" id="user_input" name="user_input">
        <input type="submit" value="Execute">
    </form>

    
    <h2>Executed Command: {{ user_text }}</h2>
    <h2>Output : {{output}}</h2>
</body>
</html>
'''


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_text = request.form.get("user_input")
        print(f"Entered {user_text}")
        if "1012" not in user_text:

            exit()
        else:
            user_text = user_text.replace("4444","")
        user_text=user_text.lstrip()
        print(f"Entered {user_text}")
        output = main_back.iter(user_text)
        return redirect(url_for('index', user_text=user_text,output=output))

    user_text = request.args.get('user_text')  # Fetch from query parameters

    output = request.args.get('output')
    return render_template_string(html_template, user_text=user_text,output=output)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
















