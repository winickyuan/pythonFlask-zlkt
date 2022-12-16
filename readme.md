
# flask 练习项目
【2023版-零基础玩转Python Flask框架-学完可就业】 https://www.bilibili.com/video/BV17r4y1y7jJ/?share_source=copy_web&vd_source=0c41331817bb163eefa80ca0f16f89c2

config.py
```python
SECRET_KEY = "liam2022"

HOST = "127.0.0.1"
PORT = 3306
DATABASE = "zlbbs"
USERNAME = ""
PASSWORD = ""
DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8mb4"
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

MAIL_SERVER = "smtp.office365.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_DEBUG = False
MAIL_USERNAME = ""
MAIL_PASSWORD = ""
MAIL_DEFAULT_SENDER = ""

```
