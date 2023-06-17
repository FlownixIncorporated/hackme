from flask import Flask, render_template, request, redirect

webapp = Flask("Hacking Playground")

@webapp.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        name = request.form.get('name')
        password = request.form.get('password')
        
        if name == "admin" and password == "admin2023+":
            return redirect("/dash")
        
    
    return render_template("index.html")

@webapp.route("/dash")
def dash():
    return """<script>alert('HI');window.location.href = "/";</script>"""

webapp.run("0.0.0.0", 80, debug=True)
