from datetime import datetime

from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Todo


def home(request):
    # POST = пришла форма, создаём новую задачу
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()
        due_raw = request.POST.get("due_date", "").strip()
        is_done = bool(request.POST.get("is_done"))

        due_date = None
        if due_raw:
            try:
                # ожидаем формат от <input type="datetime-local">
                dt = datetime.fromisoformat(due_raw)
                if timezone.is_naive(dt):
                    dt = timezone.make_aware(dt, timezone.get_current_timezone())
                due_date = dt
            except ValueError:
                # если дата кривая — просто не сохраняем дедлайн
                due_date = None

        if title:
            Todo.objects.create(
                title=title,
                description=description,
                due_date=due_date,
                is_done=is_done,
            )

        # redirect (перенаправление) — чтобы не дублировать форму на перезагрузке
        return redirect("home")

    # GET = просто показываем список задач
    todos = Todo.objects.all().order_by("is_done", "due_date")
    context = {"todos": todos}  # контекст (данные для шаблона)
    return render(request, "home.html", context)
