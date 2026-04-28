from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Chat route
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "").lower()

    if "process" in user_message:
        response = """🗳️ Election Process (Step-by-Step):

1. Voter Registration → Citizens register to vote
2. Candidate Nomination → Candidates file nominations
3. Campaigning → Candidates promote themselves
4. Voting Day → People cast their votes
5. Counting → Votes are counted
6. Results → Winners are declared"""

    elif "steps" in user_message:
        response = """📌 Main Election Steps:

• Registration
• Nomination
• Campaigning
• Voting
• Counting
• Result Declaration"""

    elif "timeline" in user_message:
        response = """📅 Election Timeline:

1. Announcement of Election
2. Filing Nominations
3. Scrutiny & Withdrawal
4. Campaign Period
5. Voting Day
6. Counting Day
7. Result Declaration"""

    elif "india" in user_message:
        response = """🇮🇳 Elections in India:

• Conducted by Election Commission of India
• Uses Electronic Voting Machines (EVMs)
• Includes Lok Sabha & State Elections
• Follows strict model code of conduct"""

    elif "vote" in user_message:
        response = """🗳️ Voting:

Voting is the process where citizens choose their representatives by casting their vote securely and privately."""

    else:
        response = """I can help you with:
✔ Election process
✔ Steps involved
✔ Timeline
✔ Elections in India

Try asking:
👉 "Explain election process"
👉 "Election timeline"
👉 "Steps of election"
👉 "How elections work in India"
"""

    return jsonify({"response": response})


if __name__ == '__main__':
    app.run(debug=True)