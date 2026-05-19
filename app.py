from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    prediction = ""

    if request.method == 'POST':

        bedrooms = int(request.form['bedrooms'])
        bathrooms = int(request.form['bathrooms'])
        area = int(request.form['area'])
        parking = int(request.form['parking'])
        year = int(request.form['year'])

        prediction = (
            bedrooms * 50000 +
            bathrooms * 30000 +
            area * 100 +
            parking * 20000 -
            (2026 - year) * 1000
        )

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)