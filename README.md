```plaintext
JOKER_CARD_PJ/
│
├── main.py
├── static/         <- 放 CSS、JS、圖片、音樂 等「靜態資源」
│   ├── ANI
│   │   ├── R.MOV
│   │   ├── SR.MOV
│   │   ├── SSR.MOV
│   │   └── UR.MOV
│   ├── ANI
│   │   └── 1~4.PNG
│   ├── R
│   │   ├── test.png
│   │   └── 1~29.png
│   ├── SR
│   │   └── 1~15.png
│   ├── SSR
│   │   └── 1~17.png
│   ├── UR
│   │   └── 1~12.png
│   └── test_bg.png
│
├── templates/      <- 放 HTML 檔案（要用 render_template 載入）
│    ├── index.html
│    ├── cardhere.html
│    ├── ani_r.html
│    ├── ani_sr.html
│    ├── ani_ss.html
│    ├── ani_ur.html
│    └── main_c.html
│
├── import_json.py
└── user_point.json
```
