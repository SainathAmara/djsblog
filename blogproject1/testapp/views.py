from django.shortcuts import render,get_object_or_404
from testapp.models import Post,Movie
from testapp.forms import EmailSentForm,SignUpForm,CommentForm,MovieForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')
def post_list_view(request):
    post_list=Post.objects.all()
    paginator=Paginator(post_list,2)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'testapp/post_list.html',{'post_list':post_list})

def detail_list_view(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,status='published',
                                          publish__year=year,
                                          publish__month=month,
                                          publish__day=day)
    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True
    else:
        form=CommentForm()
    return render(request,'testapp/post_detail.html',{'post':post,'form':form,'csubmit':csubmit,'comments':comments})


from django.core.mail import send_mail
def mail_send_view(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    sent=False
    if request.method=='POST':
        form=EmailSentForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='{}({}) recommends you to read "{}"'.format(cd['Name'],cd['Email'],post.title)
            post_url=request.build_absolute_uri(post.get_absolute_url())
            message='Read Post At:\n {}\n\n{}\'s Comments:\n{}'.format(post_url,cd['Name'],cd['Email'])
            send_mail(subject,message,'sainathamara43@gmail.com',[cd['to']])
            sent=True
    else:
        form=EmailSentForm()
    return render(request,'testapp/share_by_mail.html',{'form':form,'post':post,'sent':sent})
def sign_up_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})


def logout_view(request):
    return render(request,'testapp/logout.html')

def jobs_view(request):
    return render(request,'testapp/home1.html')

from django.shortcuts import render
from testapp.models import hydjobs,blorejobs,chennaijobs,punejobs
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')
def hyd_jobs_view(request):
    hydjobs_list=hydjobs.objects.all().order_by('date','company')
    my_dict={'jobs_list':hydjobs_list}
    return render(request,'testapp/hydjobs.html',context=my_dict)
def blore_jobs_view(request):
    hydjobs_list=blorejobs.objects.all().order_by('date','company')
    my_dict={'jobs_list':hydjobs_list}
    return render(request,'testapp/blorejobs.html',context=my_dict)
def pune_jobs_view(request):
    hydjobs_list=punejobs.objects.all().order_by('date','company')
    my_dict={'jobs_list':hydjobs_list}
    return render(request,'testapp/punejobs.html',context=my_dict)
def chennai_jobs_view(request):
    hydjobs_list=chennaijobs.objects.all().order_by('date','company')
    my_dict={'jobs_list':hydjobs_list}
    return render(request,'testapp/chennaijobs.html',context=my_dict)


def index_view(request):
    return render(request,'testapp/index.html')

def add_movie_view(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index_view(request)
    return render(request,'testapp/addmovie.html',{'form':form})

def list_view(request):
    movies_list=Movie.objects.all()
    return render(request,'testapp/listmovie.html',{'movies_list':movies_list})


from testapp.forms import FeedbackForm
# Create your views here.

def thankyou_view(request):
    return render(request,'testapp/thankyou.html')

def feedback_view(request):
    form=FeedbackForm()
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            print('Validation comleted..printing Feedback info')
            print('Student Name:',form.cleaned_data['name'])
            print('Student Rollno:',form.cleaned_data['rollno'])
            print('Student Email:',form.cleaned_data['email'])
            print('Student Feedback:',form.cleaned_data['feedback'])
            return thankyou_view(request)
    return render(request,'testapp/feedback.html',{'form':form})
