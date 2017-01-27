from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'BBCNewsArticles'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/BBCNewsArticles'

mongo = PyMongo(app)
@app.route('/Articles', methods=['GET'])
def get_all_articles():
    Article = mongo.db.Article
    output = []
    for s in Article.find():
        output.append({'text' : s['text'], 'author' : s['author'],'headline' : s['headline'],'url' : s['url']})
    return jsonify({'result' : output})

@app.route('/Articles/<string:q>', methods = ['GET'])
def get_matching_articles(q):
    Article = mongo.db.Article
    output = []
    for s in Article.find({"text": /q/}):
        output.append({'text' : s['text'], 'author' : s['author'],'headline' : s['headline'],'url' : s['url']})
    return jsonify({'result' : output})
    
#Authentication Modeule

#Error Handling Module like 404 not found

#Token creation module
    
if __name__ == '__main__':
    app.run(debug=True)

    