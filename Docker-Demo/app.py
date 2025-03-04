from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template for the multiplication table generator
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multiplication Table Generator</title>
</head>
<body>
    <h1>Multiplication Table Generator</h1>
    <form method="POST">
        <label for="number">Enter a number: </label>
        <input type="number" name="number" id="number" required>
        <button type="submit">Generate Table</button>
    </form>

    {% if table %}
    <h2>Multiplication Table for {{ table[0][0] }}</h2>
    <table border="1">
        <tr>
            <th>Number</th>
            <th>Multiplier</th>
            <th>Result</th>
        </tr>
        {% for row in table %}
        <tr>
            <td>{{ row[0] }}</td>
            <td>{{ row[1] }}</td>
            <td>{{ row[2] }}</td>
        </tr>
        {% endfor %}
    </table>
    {% endif %}
</body>
</html>
"""


@app.route('/', methods=['GET', 'POST'])
def generate_table():
    table = []
    if request.method == 'POST':
        number = int(request.form['number'])  # Get the number from the form
        # Generate the multiplication table
        table = [(number, i, number * i) for i in range(1, 11)]
    return render_template_string(html_template, table=table)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
