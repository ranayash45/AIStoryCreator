from flask import Flask, render_template, request, jsonify
from utility import content_creator
app = Flask(__name__)

def generate_extra_content(style, extra):
    """
    Returns themed content based on style and extra info.
    """
    print("start generating story")
    return content_creator.content_create(style,extra)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load_html')
def load_html():
    style = request.args.get('style')
    extra = request.args.get('extra')

    # Call the helper function
    message = generate_extra_content(style, extra)

    html_content = f"<p>{message}</p>"
    return jsonify({'html': html_content})

if __name__ == '__main__':
    app.run(debug=True)