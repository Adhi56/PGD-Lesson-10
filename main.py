import pgzrun

WIDTH=870
HEIGHT=650

marquee_box = Rect(0,0, 880, 80)
question_box = Rect(0,0,650,150)
timer_box= Rect(0,0,150,150)
skip_box = Rect(0,0,150,350)
answer_box1= Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)

timer_box.move_ip(700,100)
skip_box.move_ip(700,270)

answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)

score = 0

time_left = 10

is_game_over = False

question_file_name = "questions.txt"

marquee_message = " "

answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]

questions = []

question_count = 0  #total number of qn
question_index = 0  #current qn

def draw():
    global marquee_message

    screen.clear()
    screen.fill("black")

    screen.draw.filled_rect(marquee_box,"black")
    screen.draw.filled_rect(question_box," midnight blue")
    screen.draw.filled_rect(skip_box,"navy blue")
    screen.draw.filled_rect(timer_box,"steel blue")

    for i in answer_boxes:
        screen.draw.filled_rect(i,"light blue")
    
    marquee_message = "Welcome to quizmaster, " + f"Q: {question_index} of {question_count}"

    screen.draw.textbox(marquee_message, marquee_box, color = "white")
    screen.draw.textbox("SKIP", skip_box, color = "white")     #writes all boxes
    screen.draw.textbox(str(time_left), timer_box, color = "white")
    screen.draw.textbox(question[0].strip(),question_box ,color = "white")

    index = 1

    for answerbox in answer_boxes:
        screen.draw.textbox(question[index].strip(), answerbox, color = "white" )
        index = index +1

def move_marquee():
    marquee_box.x= marquee_box.x - 2
    if marquee_box.right < 0:
        marquee_box.left = WIDTH

def update():
    move_marquee()

def read_question_file():
    global question_count, questions
    question_file= open(question_file_name, "r")
    for question in question_file:
        questions.append(question)
        question_count= question_count +1
    question_file.close()

def read_next_question():
    global question_index
    question_index = question_index +1
    return questions.pop(0).split("|")

def on_mouse_down(pos):
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            if index is int(question[5]):
                correct_answer()
            else:
                 game_over()
        index = index +1
    if skip_box.collidepoint(pos):
        skip_questions()
        
def correct_answer():
    global score, question,time_left, questions
    score  = score+1
    if questions:
        question = read_next_question()
        time_left = 10
    else:
        game_over()

def game_over():
    global question, time_left, is_game_over
    message = f"Game Over! \nYou got {score} questions correct!"
    question = [message, "-","-","-","-", 5]
    time_left = 0
    is_game_over = True

def skip_questions():
    global question, time_left
    if questions and not is_game_over:
        question = read_next_question()
        time_left =10
    else:
        game_over()

def update_time_left():
    global time_left
    if time_left:
        time_left = time_left - 1
    else:
        game_over()

        
    







    






read_question_file()
question = read_next_question()
#question = ["Question...","ans1","ans2","ans3","ans4","3"]   
pgzrun.go()