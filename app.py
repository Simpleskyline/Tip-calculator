from flask import Flask, render_template, request

# Create a Flask web app instance
app = Flask(__name__)

# Define the route for the homepage and allow GET & POST methods
@app.route("/", methods=["GET", "POST"])
def tip_calculator():
    tip = None  # Initialize tip result as None
    total = None  # Initialize total bill as None
    
    # Check if the form was submitted
    if request.method == "POST":
        # Get bill amount and tip percentage from the form and convert to float
        bill = float(request.form["bill"])
        tip_percent = float(request.form["tip_percent"])
        
        # Calculate the tip and total bill
        tip = bill * (tip_percent / 100)
        total = bill + tip
    
    # Render the HTML page and pass the results
    return render_template("index.html", tip=tip, total=total)

# Run the Flask app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
