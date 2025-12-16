from flask import Flask, request

main_page = '''
<html>
    <head>
    <title></title>
    <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.min.css">
    </head>
<body>
<form class="form-horizontal" method="post" action="/calc">
<fieldset>
<legend>Multiplier</legend>

<div class="form-group">
  <label class="col-md-4 control-label">Number</label>  
  <div class="col-md-4">
    <input type="number" name="number" placeholder="Enter a number" class="form-control">
  </div>
</div>

<div class="form-group">
  <div class="col-md-4 col-md-offset-4">
    <button class="btn btn-primary">Calculate</button>
  </div>
</div>

</fieldset>
</form>
</body>
</html>
'''

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return main_page

@app.route("/calc", methods=["POST"])
def calc():
    number = request.form.get("number", type=float)
    if number is None:
        return "<h1>Invalid input</h1>"
    return f"<h1>Result: {number * 5}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
