import os
from flask import Flask, render_template, request, redirect, url_for
from ascii import image_to_ascii
from PIL import Image


app = Flask(__name__)


@app.get("/")
def get_index():

    for path in os.listdir("static/"):
        os.remove(os.path.join("static", path))
    return render_template("load.html")


@app.post("/")
def post_index():

    file = request.files["file"]
    if file.filename != "":
        file.save(f"static/{file.filename}")
        return redirect(url_for("get_ascii"))
    return redirect(url_for("get_index"))


@app.get("/ascii")
def get_ascii():

    path = os.listdir("static/")[0]
    image = Image.open(f"static/{path}")
    string = image_to_ascii(image)
    return render_template("image.html", ascii=string)


if __name__ == '__main__':
    app.run()
