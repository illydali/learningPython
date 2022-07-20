from Questions import Questions

question_prompts = [
"What color is a banana?\n(a) Red\n(b) Yellow\n(c) Purple\n\n",
"What color is a durian?\n(a) Brown\n(b) Red\n(c) Green\n\n",
"What color is a mango?\n(a) Orange \n(b) Yellow\n(c) Pink\n\n"
]

questions = [
    Questions(question_prompts[0], "b"),
    Questions(question_prompts[1], "c"),
    Questions(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")

run_test(questions)