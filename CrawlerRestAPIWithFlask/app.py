from flask import Flask, request, render_template
from flask import jsonify
from pymongo import MongoClient

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'BBCNewsArticles'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/BBCNewsArticles'

mongo = MongoClient('mongodb://localhost:27017/')
mydb = mongo['BBCNewsArticles']

@app.route('/', methods=['GET'])
def get_home():
    return "Welcome to the BBC news Search Application !!!"
    
@app.route('/Articles', methods=['GET'])
def get_all_articles():
    output = []
    for s in mydb.Article.find({}):  
        print "abc"
        output.append({'text' : s['text'], 'author' : s['author'],'headline' : s['headline'],'url' : s['url']})
    return jsonify({'result' : output})
    #return render_template('search.html', res=jsonify({'result' : output}))

@app.route('/Articles/<string:q>', methods = ['GET'])
def get_matching_articles(q):
    output = []
    #mydb.Article.createIndex({"text":"text"})
    for s in mydb.Article.find( { "$text": { "$search": q } } ):
        output.append({'text' : s['text'], 'author' : s['author'],'headline' : s['headline'],'url' : s['url']})
    return jsonify({'result' : output})
    
#Authentication Modeule

#Error Handling Module like 404 not found

#Token creation module
    
if __name__ == '__main__':
    app.run(debug=True)

    