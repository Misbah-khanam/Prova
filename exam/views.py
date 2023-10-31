from django.shortcuts import render
import datetime
from .models import Exam, Question, Attempted

def upload_test(request):
    messages = []
    if(request.method == "POST"):
        questions = request.POST.getlist('question')
        option1 = request.POST.getlist('question_opt_1')
        option2 = request.POST.getlist('question_opt_2')
        option3 = request.POST.getlist('question_opt_3')
        option4 = request.POST.getlist('question_opt_4')
        ans = request.POST.getlist('ans')

        subject = request.POST.get('subject_name')
        user = request.user
        uploaded_date = datetime.datetime.now()
        valid_till = request.POST.get('valid_date')

        print(subject)
        print(valid_till)

        exam_obj = Exam( 
            subject_name = subject,
            user = user,
            valid_till = valid_till
        )

        exam_obj.save()

        for i in range(0, len(questions)):
            print(questions[i])
            print(option1[i])
            print(option2[i])
            print(option3[i])
            print(option4[i])
            print(ans[i])

            ques_obj = Question(
                question = questions[i],
                option_1 = option1[i],
                option_2 = option2[i],
                option_3 = option3[i],
                option_4 = option4[i],
                answer = ans[i],
                exam = exam_obj
            )

            ques_obj.save()
        messages.append("test uploaded successfully")
        print(messages)
    return render(request, "upload_test.html",{"messages" : messages})


def my_uploaded_tests(request):
    my_tests = Exam.objects.filter(user=request.user)
    context = {"my_tests": my_tests}
    return render(request, "my_uploaded_tests.html", context)


def active_tests(request):
    my_tests = Exam.objects.all()
    context = {"my_tests": my_tests}
    return render(request, "active_tests.html", context)


def my_ques(request, exam_id):
    ques = Question.objects.filter(exam__id = exam_id)
    context = {"ques" : ques}
    return render(request, "my_ques.html", context)


def attempt_ques(request, exam_id):
    ques = Question.objects.filter(exam__id = exam_id)
    messages = []
    marks = 0
    if(request.method == "POST"):
        print(request.POST)
        ques_ids = request.POST.getlist("ques_id")
        option1 = request.POST.get("option_1")
        option2 = request.POST.get("option_2")
        option3 = request.POST.get("option_3")
        option4 = request.POST.get("option_4")
        option5 = request.POST.get("option_5")

        answers = [option1, option2, option3, option4, option5]

        questions = Question.objects.filter(id__in = ques_ids)

        i = 0
        marks = 0
        for question in questions:
            if question.answer == answers[i]:
                marks = marks + 1
            i = i+1

        exam = Exam.objects.filter(id = exam_id).first()
        attempted_exam = Attempted(
            exam = exam,
            student = request.user,
            marks = marks,
            attempt_date = datetime.datetime.now()
        )

        attempted_exam.save()

        print(marks)
        messages.append("exam submitted successfully")

    context = {"ques" : ques, "exam_id":exam_id, "messages":messages, "marks":marks}
        
    return render(request, "attempt_ques.html", context)


def attempted_tests(request):
    my_tests = Attempted.objects.filter(student = request.user)
    context = {"my_tests": my_tests}
    return render(request, "attempted_tests.html", context)

def analytics_teacher(request):
    my_tests = Exam.objects.filter(user=request.user)
    attempted_users_exam = Attempted.objects.filter(exam__in =my_tests)
    context = {"attempted_users_exam": attempted_users_exam}
    return render(request, "analytics_teacher.html",context)

def analytics_student(request):
    attempted_users_exam = Attempted.objects.filter(student=request.user)
    context = {"attempted_users_exam": attempted_users_exam}
    return render(request, "analytics_student.html",context)