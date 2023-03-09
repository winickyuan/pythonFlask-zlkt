from flask import Flask, session, g
import config
from exts import mail, db
from flask_migrate import Migrate

from apps.qa import bp as qa_bp
from apps.user import bp as user_bp

from models import UserModel, EmailCaptchaMode, AnswerModel, QuestionModel

app = Flask(__name__)

app.config.from_object(config)

db.init_app(app)
mail.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(qa_bp)
app.register_blueprint(user_bp)


@app.before_request
def befor_request():
    user_id = session.get("user_id")
    if user_id:
        user = UserModel.query.get(user_id)
        setattr(g, "user", user)
    else:
        setattr(g, "user", None)

#测试
@app.context_processor
def context_processor():
    return {"user": g.user}


if __name__ == '__main__':
    app.run(debug=True)
