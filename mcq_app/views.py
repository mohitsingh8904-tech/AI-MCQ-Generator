from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UploadedNotes, QuizResult
from .forms import UploadNotesForm
from .utils import extract_text_from_pdf
from .mcq_logic import generate_mcqs_from_text
from .ai_utils import run_flan_t5
from blog.models import BlogPost
from .pdf_utils import render_to_pdf
from django.utils import timezone


@login_required(login_url="login")
def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        if not username or not password:
            messages.error(request, "Username and password are required.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Account created. Please log in.")
            return redirect("login")

    return render(request, "register.html")



@login_required(login_url="login")
def upload_notes(request):
    """
    Upload PDF, extract text, generate MCQs, keep them in session
    then redirect to quiz page.
    """
    if request.method == "POST":
        form = UploadNotesForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            text = extract_text_from_pdf(obj.file.path)

           
            text = text[:2000]

            mcqs = generate_mcqs_from_text(text)

            request.session["mcqs"] = mcqs
            return redirect("quiz")
    else:
        form = UploadNotesForm()

    return render(request, "upload.html", {"form": form})


@login_required(login_url="login")
def quiz_view(request):
    mcqs = request.session.get("mcqs", [])
    if not mcqs:
        return redirect("upload")

    if request.method == "POST":
        score = 0
        results = []

        for i, mcq in enumerate(mcqs, start=1):
            user_answer = request.POST.get(f"q{i}")
            correct_answer = mcq["answer"]
            explanation = mcq.get("explanation", "")

            if user_answer == correct_answer:
                score += 1

            results.append({
                "question": mcq["question"],
                "user_answer": user_answer,
                "correct_answer": correct_answer,
                "options": mcq["options"],
                "explanation": explanation,
            })

        QuizResult.objects.create(
            user=request.user,
            score=score,
            total=len(mcqs),
            subject="",
        )

        context = {"results": results, "score": score, "total": len(mcqs)}
        return render(request, "result.html", context)

    return render(request, "quiz.html", {"mcqs": mcqs})




@login_required(login_url="login")
def result_view(request):
    return render(request, "result.html")



@login_required(login_url="login")
def about_view(request):
    return render(request, "about.html")


@login_required(login_url="login")
def blog_view(request):
    posts = BlogPost.objects.all()
    return render(request, "blog.html", {"posts": posts})



@login_required(login_url="login")
def generate_mcq(request):
    text = request.GET.get("text", "")
    prompt = f"Create 3 multiple choice questions from this text:\n{text}"
    result = run_flan_t5(prompt)
    return JsonResponse({"mcq": result})


@login_required(login_url="login")
def my_tests(request):
    history = QuizResult.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "my_tests.html", {"history": history})

@login_required(login_url="login")
def download_result_pdf(request, result_id):
    mcqs = request.session.get("mcqs", [])
    if not mcqs:
        return redirect("my_tests")

    try:
        qr = QuizResult.objects.get(id=result_id, user=request.user)
    except QuizResult.DoesNotExist:
        return redirect("my_tests")

    context = {
        "user": request.user,
        "score": qr.score,
        "total": qr.total,
        "date": qr.created_at,
        "subject": qr.subject,
    }
    return render_to_pdf("result_pdf.html", context, filename=f"quiz_{qr.id}.pdf")



