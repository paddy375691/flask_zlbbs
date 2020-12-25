
from flask import Blueprint, views, render_template, request, session, redirect, url_for
from .forms import LoginForm
from .models import CMSUser

bp = Blueprint('cms', __name__, url_prefix='/cms')


@bp.route('/')
def index():
    return 'cms index'


class LoginView(views.MethodView):
    def get(self, message=None):
        return render_template('cms/cms_login.html', message=message)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data

            # 再判断用户是否存在
            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session['user_id'] = user.id
                # 根据是否勾选remember来决定cookie的过期时间
                if remember:
                    session.permanent = True  # 默认31天过期
                return redirect(url_for('cms.index'))
            else:
                return self.get(message='邮箱或者密码错误')

        else:
            print(form.errors)
            # form.errors 是一个字典，
            message = form.errors.popitem()[1][0]
            return self.get(message=message)


bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
