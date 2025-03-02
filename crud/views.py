from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Task
from .forms import TaskForm
# Create your views here.
def task_list_and_create(request):
    form = TaskForm()
    task_completed = Task.objects.filter(completed=True)
    task_pending = Task.objects.filter(completed=False)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Tarea creada exitosamente.") 
            return redirect('crud:task_list')
        

    return render(request, 'crud/task_list.html', {
        'form': form,
        'task_completed': task_completed,
        'task_pending': task_pending,
    })

def task_update(request, pk):

    if request.method == 'POST':
        task = Task.objects.get(pk=pk)
        task.completed = not task.completed
        task.save()
        return redirect('crud:task_list')

    
def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    messages.error(request, "❌ Tarea eliminada.") 
    return redirect('crud:task_list')

def task_edit(request, pk):
    task = Task.objects.get(pk=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.info(request, "🔄 Tarea actualizada.") 
            return redirect('crud:task_list')
