from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')
    

@app.route('/form', methods = ['POST'])
def form():
    #nick_name = request.form.get('nick_name')
    #pdi_score =  5*(sum([float(request.form.get('pdi_1')),float(request.form.get('pdi_2')), float(request.form.get('pdi_3')), float(request.form.get('pdi_4')), float(request.form.get('pdi_5'))]))-25
    #idv_score =  5*(sum([float(request.form.get('idv_1')),float(request.form.get('idv_2')), float(request.form.get('idv_3')), float(request.form.get('idv_4')), float(request.form.get('idv_5'))]))-25
    #mas_score =  5*(sum([float(request.form.get('mas_1')),float(request.form.get('mas_2')), float(request.form.get('mas_3')), float(request.form.get('mas_4')), float(request.form.get('mas_5'))]))-25
    #uai_score =  5*(sum([float(request.form.get('uai_1')),float(request.form.get('uai_2')), float(request.form.get('uai_3')), float(request.form.get('uai_4')), float(request.form.get('uai_5'))]))-25
    #ivr_score =  5*(sum([float(request.form.get('ivr_1')),float(request.form.get('ivr_2')), float(request.form.get('ivr_3')), float(request.form.get('ivr_4')), float(request.form.get('ivr_5'))]))-25
    #lto_score =  5*(sum([float(request.form.get('lto_1')),float(request.form.get('lto_2')), float(request.form.get('lto_3')), float(request.form.get('lto_4')), float(request.form.get('lto_5'))]))-25
    
    #six_list = [pdi_score, idv_score, mas_score, uai_score, lto_score, ivr_score]
    pdi_1 = request.form.get('pdi_1').value
    print(pdi_1)


    return render_template('details.html', nick_name='nick_name', pdi_1='pdi_1', pdi_2='pdi_2', pdi_3='pdi_3', pdi_4='pdi_4', pdi_5='pdi_5', idv_1='idv_1', idv_2='idv_2', idv_3='idv_3', idv_4='idv_4', idv_5='idv_5', mas_1='mas_1', mas_2='mas_2', mas_3='mas_3', mas_4='mas_4', mas_5='mas_5',uai_1='uai_1', uai_2='uai_2', uai_3='uai_3', uai_4='uai_4', uai_5='uai_5', ivr_1='ivr_1', ivr_2='ivr_2', ivr_3='ivr_3', ivr_4='ivr_4', ivr_5='ivr_5', lto_1='lto_1', lto_2='lto_2', lto_3='lto_3', lto_4='lto_4', lto_5='lto_5')



@app.route('/details')
def detail(nick_name, six):
    nick_name = request.form.get('nick_name')
    pdi_score =  5*(sum([float(request.form.get('pdi_1')),float(request.form.get('pdi_2')), float(request.form.get('pdi_3')), float(request.form.get('pdi_4')), float(request.form.get('pdi_5'))]))-25
    idv_score =  5*(sum([float(request.form.get('idv_1')),float(request.form.get('idv_2')), float(request.form.get('idv_3')), float(request.form.get('idv_4')), float(request.form.get('idv_5'))]))-25
    mas_score =  5*(sum([float(request.form.get('mas_1')),float(request.form.get('mas_2')), float(request.form.get('mas_3')), float(request.form.get('mas_4')), float(request.form.get('mas_5'))]))-25
    uai_score =  5*(sum([float(request.form.get('uai_1')),float(request.form.get('uai_2')), float(request.form.get('uai_3')), float(request.form.get('uai_4')), float(request.form.get('uai_5'))]))-25
    ivr_score =  5*(sum([float(request.form.get('ivr_1')),float(request.form.get('ivr_2')), float(request.form.get('ivr_3')), float(request.form.get('ivr_4')), float(request.form.get('ivr_5'))]))-25
    lto_score =  5*(sum([float(request.form.get('lto_1')),float(request.form.get('lto_2')), float(request.form.get('lto_3')), float(request.form.get('lto_4')), float(request.form.get('lto_5'))]))-25
    
    six_list= []
    six_list = [pdi_score, idv_score, mas_score, uai_score, lto_score, ivr_score]
    print('total 6 dimensional score is: ', six_list)

    visitor1_dict = {'nick_name':'Hiroppi', 'pdi_score':78, 'idv_score':36, 'mas_score':51, 'uai_score':66, 'lto_score':43, 'ivr_score':40} 
    
    #import viz.py
    return render_template('details.html')



if __name__=='__main__':
    #app.run(host='0.0.0.0', debug=True)
    app.run(debug=True)