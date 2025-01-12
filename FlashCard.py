from flask import Flask, render_template_string, request

app = Flask(__name__)

# 闪卡数据
flashcards = [
    {'front': 'Gravitational Field Strength', 'back': 'The force per unit mass experienced by a small test mass placed in a gravitational field.<br>Symbol: g<br>Unit: \\( \\text{N} \\cdot \\text{kg}^{-1} \\) or \\( \\text{m} \\cdot \\text{s}^{-2} \\)<br>Equation: \\( g = \\frac{F}{m}, g = \\frac{GM}{r^2} \\)'},
    {'front': 'Capacitance', 'back': 'The amount of charge stored per unit potential difference across a capacitor.<br>Symbol: C<br>Unit: F<br>Equation: \\( C = \\frac{Q}{V} \\)'}
]

@app.route('/')
def index():
    # 获取当前卡片的索引和是否显示背面
    current_card = int(request.args.get('card', 0))
    show_back = request.args.get('show_back', 'false') == 'true'  # 使用请求参数来决定是否显示背面
    
    # 计算下一张和上一张卡片的索引
    next_card = (current_card + 1) % len(flashcards)
    prev_card = (current_card - 1) % len(flashcards)
    
    # 切换显示背面的状态
    toggle_show_back = not show_back
    
    # 根据当前卡片决定是否显示背面
    return render_template_string("""
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Flashcards</title>
            <script type="text/javascript" async
                src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"></script>
            <style>
                body {
                    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
                    background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    flex-direction: column;
                    text-align: center;
                    padding: 20px;
                }
                .flashcard {
                    background-color: white;
                    padding: 40px;
                    border-radius: 15px;
                    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
                    text-align: center;
                    max-width: 350px;
                    width: 100%;
                    transition: transform 0.3s ease-in-out;
                    margin-bottom: 20px;
                }
                .flashcard:hover {
                    transform: scale(1.05);
                    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
                }
                .flashcard .front {
                    font-size: 1.5em;
                    font-weight: bold;
                    color: #007bff;
                    margin-bottom: 20px;
                }
                .flashcard .back {
                    font-size: 1.2em;
                    color: #333;
                    white-space: pre-line;
                }
                button {
                    padding: 12px 30px;
                    background-color: #007bff;
                    color: white;
                    border: none;
                    border-radius: 30px;
                    cursor: pointer;
                    font-size: 1.1em;
                    transition: background-color 0.3s ease;
                    margin-top: 15px;
                }
                button:hover {
                    background-color: #0056b3;
                }
                .button-container {
                    display: flex;
                    justify-content: center;
                    gap: 20px;  /* 增加按钮之间的间距 */
                    width: 350px;
                    margin-top: 20px;
                }
                .button-container button {
                    font-size: 1.1em;
                }
            </style>
        </head>
        <body>
            <div class="flashcard">
                <div class="front">{{ flashcards[current_card].front }}</div>
                {% if show_back %}
                    <div class="back">{{ flashcards[current_card].back|safe }}</div>
                {% endif %}
            </div>
            <div class="button-container">
                <button onclick="window.location.href='/?card={{ prev_card }}&show_back=false'">Previous</button>
                <button onclick="window.location.href='/?card={{ next_card }}&show_back=false'">Next</button>
                <button onclick="window.location.href='/?card={{ current_card }}&show_back={{ 'false' if show_back else 'true' }}'">
                    {{ 'Hide Back' if show_back else 'Show Back' }}
                </button>
            </div>
        </body>
        </html>
    """, flashcards=flashcards, 
        current_card=current_card, 
        show_back=show_back, 
        next_card=next_card,
        prev_card=prev_card,
        toggle_show_back=toggle_show_back)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000)
