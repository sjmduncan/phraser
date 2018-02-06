#!/usr/bin/python

import markov
from bottle import route, run, template
n=0
@route('/')
def index():
    global n
    names=[]
    names+=model3.genPhrases(8)
    names.sort(key=lambda s:-len(s))
    n+= len(names)
    st='<html><head>\
    <title>What Would Markov Say?</title></head>\
    <style>\
    p{padding:0;margin:0.5em;}\
    a{color:dodgerblue;text-decoration:none;}\
    a:visited{color:dodgerblue;}</style>\
    <body style="font-size:2.0em;font-family:sans-serif;\
    color:#555;text-align:center;">'

    for s in names:
        st+='<p><b>'+s+'</b></p>'
    st+='<p><a href="/">more</a></p>'
    st+='<p><a href="https://github.com/sjmduncan/phraser">\
    <small>(code)</small></a></p>'

    return st+'</body></html>'


model3=markov.phraser('english.txt',3,norepeat=True,norepeat_buffer=300)

run(host='localhost', port=8080)
