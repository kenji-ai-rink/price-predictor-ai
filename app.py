import pickle
from flask import Flask, request, render_template

# モデル読み込み
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    price = None
    if request.method == 'POST':
        area = float(request.form['area'])
        age = float(request.form['age'])
        prediction = model.predict([[area, age]])
        price = round(prediction[0], 1)
    return render_template('index.html', price=price)

if __name__ == '__main__':
    app.run(debug=True)
