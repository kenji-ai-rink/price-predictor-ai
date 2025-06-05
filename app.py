import pickle
from flask import Flask, request, render_template_string

# モデル読み込み
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Flaskアプリ作成
app = Flask(__name__)

# HTMLテンプレート
template = '''
<!DOCTYPE html>
<html>
<head>
    <title>住宅価格予測AI</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            background-color: #f4f4f4; 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            height: 100vh; 
            margin: 0;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            text-align: center;
        }
        input {
            padding: 10px;
            margin: 5px;
            width: 80%;
            font-size: 16px;
        }
        input[type="submit"] {
            background-color: #007BFF;
            color: white;
            border: none;
            cursor: pointer;
            width: 50%;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>住宅価格予測AI</h1>
        <form method="post">
            <input type="number" name="area" placeholder="面積 (㎡)" step="0.1" required><br>
            <input type="number" name="age" placeholder="築年数 (年)" step="0.1" required><br>
            <input type="submit" value="予測する">
        </form>

        {% if price is not none %}
            <h2>予測価格: {{ price }} 万円</h2>
        {% endif %}
    </div>
</body>
</html>
'''

# ルーティング
@app.route('/', methods=['GET', 'POST'])
def home():
    price = None
    if request.method == 'POST':
        area = float(request.form['area'])
        age = float(request.form['age'])
        prediction = model.predict([[area, age]])
        price = round(prediction[0], 1)
    return render_template_string(template, price=price)

if __name__ == '__main__':
    app.run(debug=True)
