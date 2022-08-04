from flask import Flask, render_template, request
import blog


def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == 'POST':
        if 'form1' in request.form:
            prompt = request.form['blogTopic']
            blogT = blog.generateBlogTopics(prompt)
            blogTopicIdeas = blogT.replace('\n', '<br>')

        if 'form2' in request.form:
            prompt = request.form['blogSection']
            blogT = blog.generateBlogSections(prompt)
            blogSectionIdeas = blogT.replace('\n', '<br>')

        if 'form3' in request.form:
            prompt = request.form['blogExpander']
            blogT = blog.blogSectionExpander(prompt)
            blogExpanded = blogT.replace('\n', '<br>')


    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)
