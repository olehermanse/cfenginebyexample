#!/usr/bin/env python3
import os
import sys

def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)

mkdir("web")

def read_file(path):
    with open(path, "r") as f:
        return f.read()

def save_file(path, data):
    with open(path, "w") as f:
        f.write(data)

def ls(path):
    return os.listdir(path)

def render_markdown(md, html):
    os.system("cat examples/{} | pandoc -f markdown_github -t html > {}".format(md, html))

css = read_file("partials/style.css")
template = read_file("partials/template.html")
template = template.replace("{ css }", css)
index = template
examples_md = list(ls("examples"))
examples_md.sort()

mkdir("tmp")
examples_html = []
for md in examples_md:
    html = "tmp/" + md.replace(".md", ".html")
    render_markdown(md, html)
    md_html = read_file(html)
    md_html = md_html.replace("<pre><code>", "<pre><code>\n")
    md_html = md_html.replace("</code></pre>", "\n</code></pre>")
    md_html = md_html.replace("</code></pre>", "\n</code></pre>")
    output_path = html.replace("tmp/", "web/")
    rendered_example = template
    rendered_example = rendered_example.replace("{ content }", md_html)
    save_file(output_path, rendered_example)
    examples_html.append(output_path.replace("web/", ""))

names = [f[3:].replace("_", " ").replace(".html", "") for f in examples_html]
names = [n[0].upper() + n[1:] for n in names]
links = zip(examples_html, names)
links = ['<li><a href="{}">{}</a></li>'.format(u, n) for u,n in links]
links =  "\n".join(links)
links = "<ol>\n" + links + "</ol>\n"

index = index.replace("{ content }", links)

save_file("web/index.html", index)
print(index)
