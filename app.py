from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Chat route
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")

    # Basic logic (temporary)
    if user_message:
        msg = user_message.lower()

        if "process" in msg:
            response = "Election process includes: Registration → Campaigning → Voting → Counting."
        elif "vote" in msg:
            response = "Voting is the step where citizens cast their vote to choose representatives."
        elif "timeline" in msg:
            response = "Election timeline usually includes: Announcement → Nomination → Campaign → Voting Day → Counting → Results."
        else:
            response = "I can explain election process, steps, and timelines. Ask me something!"
    else:
        response = "Please ask something."

    return jsonify({"response": response})


if __name__ == '__main__':
    app.run(debug=True)