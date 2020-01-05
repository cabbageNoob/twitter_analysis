from . import emotion_analyses #init
from flask import render_template

@emotion_analyses.route('/emotionindex')
def emotionanalysesindex():
    return render_template('emotion_analyses/emotionanalysesindex.html')

@emotion_analyses.route('/socialman',methods=['GET', 'POST'])
def manQuery():
    pass