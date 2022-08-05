from flask import Flask, render_template, request
import blog

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == 'POST':
        if 'form1' in request.form:
            prompt = request.form['blogTopic']
            blogT = blog.generateideas1(prompt)
            blogTopicIdeas = blogT.replace('\n', '<br>')

        if 'form2' in request.form:
            prompt = request.form['blogSection']
            blogT = blog.generateideas2(prompt)
            blogSectionIdeas = blogT.replace('\n', '<br>')

        if 'form3' in request.form:
            prompt = request.form['blogExpander']
            blogT = blog.generateideas3(prompt)
            blogExpanded = blogT.replace('\n', '<br>')


    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.debug = True
    app.run()
