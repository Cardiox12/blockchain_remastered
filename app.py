from flask import Flask, render_template, request
from core.blockchain import Blockchain

app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"

blockchain = Blockchain()

@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        blockchain.add_to_blockchain(request.form['data'])
    return render_template('pages/homepage.html', blocks=blockchain.blocks, root_hash=blockchain.root_hash)

@app.route('/about')
def about():
    return render_template('pages/about.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html'), 404

# if __name__ == '__main__':
app.run()