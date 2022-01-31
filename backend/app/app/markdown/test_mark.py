from mark import markdown

markdown_str = """## This is a header [with a link](http://yahoo.com) [test](http://yahoo.com) """
html_str = """<h2>This is a header <a href="http://yahoo.com">with a link</a> <a href="http://yahoo.com">test</a></h2>"""

render = markdown.render_html(markdown_str)
assert render == html_str

