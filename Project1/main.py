from flask import Flask, render_template
app = Flask('hehe', template_folder='/home/sukrit/Mount/NewVolD/Projects/Project1')

@app.route('/')
def home():
    return render_template('index.html')

def run():
    app.run(host='0.0.0.0', port=1024)
run()