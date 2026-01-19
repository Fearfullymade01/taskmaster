from django.shortcuts import render
from .models import Task


def index(request):
	to_do = Task.objects.filter(completed=False).order_by('-due_date', '-created_at')
	done = Task.objects.filter(completed=True).order_by('-due_date', '-created_at')
	return render(request, 'tasks/index.html', {
		'to_do': to_do,
		'done': done,
	})

# Create your views here.
