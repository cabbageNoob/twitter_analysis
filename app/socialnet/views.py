from . import socialnet
from flask import render_template


@socialnet.route('/socialnetindex')
def socialnetindex():
    return render_template('socialnet/socialnetindex.html')

@socialnet.route('/socialman',methods=['GET', 'POST'])
def manQuery():
    pass