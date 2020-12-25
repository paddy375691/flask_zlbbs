
from wtforms import Form


class BaseForm(Form):
    def get_error(self):
        message = self.errors.popitem()[1][0]  # 只想获取字典的任何一项
        return message
