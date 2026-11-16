from resume_chatbot.rag import classifier

cases = [
    ("Any more projects on the way?", "future"),
    ("Making any more?", "future"),
    ("Do you have anything in the works?", "future"),
    ("What are you building next?", "future"),
    ("Anything about to drop?", "future"),
    ("Got any others in the making?", "future"),
    ("Planning any new projects?", "future"),
    ("What's your next big thing?", "future"),
    ("Is there a new project coming soon?", "future"),
    ("Are you working on anything new right now?", "future"),
    ("What projects have you built?", "now"),
    ("Do you have any other projects?", "now"),
    ("Tell me about your Resume RAG project.", "now"),
    ("What was your role in the Support System?", "now"),
    ("What are your skills?", "now"),
    ("Where did you study?", "now"),
    ("How can I contact you?", "now"),
    ("Which cloud platforms have you used?", "now"),
    ("What did you do at LoveWorld Canada?", "now"),
    ("Which of your projects is live?", "now"),
]

held_out = [
    # future
    ("Any side projects cooking?", "future"),
    ("Will there be a v2 of the chatbot?", "future"),
    ("Is anything new launching soon?", "future"),
    ("What's cooking in your lab these days?", "future"),
    ("Do you have a project you're currently developing?", "future"),
    ("Are you tinkering with anything at the moment?", "future"),
    ("Any big releases planned for next year?", "future"),
    ("What can we expect from you next?", "future"),
    ("Is there something you're about to ship?", "future"),
    ("Working on anything exciting?", "future"),
    # now
    ("What's the latest thing you shipped?", "now"),
    ("Have you worked on any side projects before?", "now"),
    ("Was there a v1 of the chatbot, or did you start with this one?", "now"),
    ("What did you learn from building the Support System?", "now"),
    ("Which project took the longest?", "now"),
    ("Are you open to new roles?", "now"),
    ("What are you currently studying?", "now"),
    ("How was the chatbot deployed?", "now"),
]

score = 0
for question, expectation in cases:
    prediction = classifier(question)
    if prediction == expectation:
        score += 1
    else:
        print(f"WRONG: {question!r} expected {expectation}, got {prediction}")

print("CASES")
print(f"{score}/{len(cases)} correct ({100 * score // len(cases)}%)")


score = 0
for question, expectation in cases:
    prediction = classifier(question)
    if prediction == expectation:
        score += 1
    else:
        print(f"WRONG: {question!r} expected {expectation}, got {prediction}")
print("HELD OUT")
print(f"{score}/{len(cases)} correct ({100 * score // len(cases)}%)")