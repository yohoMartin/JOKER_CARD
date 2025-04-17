from flask import Flask, render_template, request, jsonify, url_for,make_response
import random
from import_json import new_user,get_point,new_point,new_card,get_counter,new_counter
from datetime import datetime, timedelta

app = Flask(__name__)

counter = get_counter()     #總點擊數（可在此處讀入使用者數據）
bonus = 1       #外加（點擊獲得值的倍率）
tokens = 0    #初始小丑值（可在此處讀入使用者數據）
bonus = 1
card = ''
but_img_l = ['/BUT/1.PNG', '/BUT/2.PNG', '/BUT/3.PNG', '/BUT/4.PNG']
but_img_i = 0
but_img = but_img_l[but_img_i]
rank_to_html = {"R/":'ani_r.html', "SR":'ani_sr.html', "SS":'ani_ss.html', "UR":'ani_ur.html'}

def card_c(k=1):
    card_list_g = ["R", "SR", "SSR", "UR"]
    card_list_i = {"R": 29, "SR": 15, "SSR": 17, "UR": 12}      #池內數量
    card_probability = [1, 0.5, 0.2, 0.2]     #機率控制   
    card_group = random.choices(card_list_g, card_probability, k=k)
    card_index = [random.randint(1, card_list_i[g]) for g in card_group]
    card_code = [f"{card_group[i]}/{card_index[i]}.PNG" for i in range(k)]
    return card_code

@app.route('/')
def index():
        device = request.cookies.get('device')

        if device is None or device == 'null' or not device.startswith("user_"):
        # 生成新 device id
            device = f"user_{random.randint(1000,9999)}"

            new_user(device)
            expire = datetime.now() + timedelta(days=365)  # 過期時間設置為1年

            resp = make_response(render_template(
            'index.html',
            counter=0,
            tokens=100,
            but_img=but_img_l[0]
            ))
            resp.set_cookie('device', device,expires=expire)
            return resp
        else:
            new_user(device)  # 保險一下，如果資料夾手動清掉也能自動補回來
            tokens = get_point(device)
        return render_template('index.html', counter=counter, tokens=tokens, but_img=but_img)

@app.route('/click_button', methods=['POST'])
def click_button():
    global counter, but_img_i, but_img
    device = request.cookies.get('device')
    tokens = get_point(device)
    counter += 1 * bonus
    tokens += 1 * bonus
    new_point(device,tokens) ##記錄新的小丑值
    new_counter(counter)
    if but_img_i <3:
        but_img_i+=1
    else:
        but_img_i=0
    but_img = but_img_l[but_img_i]
    return jsonify({
        'counter': counter,
        'tokens': tokens,
        'but_img': url_for('static', filename=but_img)  # 傳給前端完整路徑
    })

@app.route('/summon_clown', methods=['POST'])   #基本無用，但怕刪了出bug
def summon_clown():
    global  card
    device = request.cookies.get('device')##確定裝置
    tokens = get_point(device)
    if tokens >= 50:
        tokens -= 50
        new_point(device,tokens) ##紀錄扣除小丑值
        card_list = card_c(1)
        card = card_list[0]
        print(f'summo:{card}')
        ani_html = rank_to_html[card[:2]]
        print(ani_html)
        return render_template("cardhere.html", card=card, tokens=tokens)   #ani_html
    else:
        return jsonify({'message': '小丑值不足', 'tokens': tokens})

@app.route('/summon_clown1', methods=['POST'])
def summon_clown1():
    global  card
    device = request.cookies.get('device') ##抓cookie
    tokens = get_point(device)
    if tokens >= 50:
        tokens -= 50
        new_point(device,tokens)
        card_list = card_c(1)
        card = card_list[0]
        new_card(device,card)## 記錄抽到的卡片
        print(f'summo:{card}')
        ani_html = rank_to_html[card[:2]]   #等級檢測
        print(ani_html)
        
        return render_template(ani_html, card=card, tokens=tokens)
        
    else:
        return jsonify({'message': '小丑值不足', 'tokens': tokens})

@app.route('/goback', methods=['POST'])
def goback():
    global  counter
    device = request.cookies.get('device') ##抓cookie
    tokens = get_point(device)
    print("goback")
    return render_template('main_c.html', tokens=tokens, counter=counter, but_img=but_img)

@app.route('/show_card', methods=['POST'])
def show_card():
    global  counter, card
    device = request.cookies.get('device') ##抓cookie
    tokens = get_point(device)
    print(f"show:{card}")
    return render_template("cardhere.html", card=card, tokens=tokens, but_img=but_img)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
