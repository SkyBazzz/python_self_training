from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    print("Getting")
    return render_template("index.html")


@app.route("/", methods=["POST"])
def home_post():
    print("Posting")
    dim1 = request.form["first_dim"]
    dim2 = request.form["second_dim"]
    dim3 = request.form["third_dim"]

    volume = float(dim1) * float(dim2) * float(dim3)
    return render_template("index.html", volume=volume, dim_1=dim1, dim_2=dim1, dim_3=dim3)


app.run(debug=True)
