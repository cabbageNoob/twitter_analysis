from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ShortestPathForm(FlaskForm):
    name1 = StringField('请输入政要名字1：', validators=[DataRequired()])
    name2 = StringField('请输入政要名字2：', validators=[DataRequired()])
    submit = SubmitField('查询政要之间最短路径')
