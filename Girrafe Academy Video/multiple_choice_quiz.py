from question_class import Q
question_answers=["what colors are apples:\n (a) green\n (b) blue\n",
                  "what is the best day:\n (a) monday\n (b) thursday\n "]

questions=[Q(question_answers[0],'a')
          ,Q(question_answers[1],'b')]

def test(questions):
    score=0
    for question in questions:

        answer=input(question.prompt)
        if answer.lower()==question.answer:
           score+=50
    print(f"you got {score} out of 100 ")
test(questions)