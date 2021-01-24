from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .models import task
from .forms import Todoforms



class tasklistview(ListView):
    model=task
    template_name = 'taskview.html'
    context_object_name = 'obj1'

class covdetail(DetailView):
    model=task
    template_name = 'detail.html'
    context_object_name = 'i'

class taskupdateview(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('covdetail',kwargs={'pk':self.object.id})

class taskdeleteview(DeleteView):
    model = task
    template_name ='delete.html'
    success_url = reverse_lazy('covtask',)





# Create your views here.
def taskview(request):
    obj1=task.objects.all()
    if request.method=="POST":
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        obj=task(name=name,priority=priority,date=date)
        obj.save()

    return render(request,'taskview.html',{'obj1':obj1})
# def Task(request):
#     if request.method=="POST":
#         name=request.POST.get('name')
#         priority=request.POST.get('priority')
#         obj=task(name=name,priority=priority)
#         obj.save()
#     return render(request,"Task.html")
def delete(request,id):
    Task=task.objects.get(id=id)
    if request.method == "POST":
        Task.delete()
        return redirect('/')

    return render(request,'delete.html',{'Task':Task})
def update(request,id):
    Task=task.objects.get(id=id)
    form=Todoforms(request.POST or None,instance=Task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'Task':Task,'form':form})


