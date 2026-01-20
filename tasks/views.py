from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = TaskForm()
	
	to_do = Task.objects.filter(completed=False).order_by('-due_date', '-created_at')
	done = Task.objects.filter(completed=True).order_by('-due_date', '-created_at')
	return render(request, 'tasks/index.html', {
		'to_do': to_do,
		'done': done,
		'form': form,
	})

# Create your views here.
