from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Entry,Topic
from .forms import EntryForm, TopicForm

def home(request):
    
    topics=Topic.objects.all()
    entries=Entry.objects.all()
    count=Topic.objects.all().count()

    
    for topic in topics:
       

        entries=topic.entry_set.all()
            
    context= {
        
        'topics':topics,
        'entries':topic.entry_set.all(),
        'Entry':Entry
    }
    
    return render(request, 'learn/topics.html', context)

def topics(request):
    topics=Topic.objects.all()
    entries=Entry.objects.all()
    
    context= {
        
        'topics':topics
    }
    
    return render(request, 'learn/topics.html', context)

def new_topic(request):
    if request.method=='POST':
        form=TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return  redirect('home')
            
    else:   
        form=TopicForm()
    
    context={
        'form':form
    }    
    
    return render(request, 'learn/new_topic.html',context)
        
def new_entry(request,topic_id):
    if request.method=='POST':
        topic=Topic.objects.get(id=topic_id)
        text=request.POST['text']
        entry=Entry(topic=topic,text=text)
        entry.save()
        form=EntryForm(data=request.POST)
        
        
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('home') 
    else:
        form=EntryForm()  
        topic=Topic.objects.get(id=topic_id)               
    context={
        'form':form,
        'topic':topic,
        

    }   
    return render(request, 'learn/new_entry.html', context) 


def topic(request,id):
    topic=Topic.objects.get(id=id)
    entries=topic.entry_set.all()
    context={
      'topic':topic,
      'entries':entries,
 
    }
    return render(request, "learn/topic.html",context)

    




def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method == 'POST':
        form = EntryForm(request.POST,instance=entry)
        if form.is_valid():
            form.save(commit=False)
            entry.save()
            form.save()
            return redirect('home') 
    
    else:
            

        form=EntryForm(instance=entry)

    context={
        'form':form,
        'entry':entry,
        'topic': topic
    }
    return render(request, 'learn/edit_entry.html',context) 
                
            
def entry(request):
    pass 


def delete(request, id):
    pass
    