from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from django.core.paginator import Paginator # paginator를 사용하기 위해서 import해야 하는 것.
# from .form import BlogPost # 같은 폴더의 form.py라는 파일로부터 BlogPost를 import해 와라.


def home(request):
    blogs = Blog.objects
    
    #블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()

    #블로그 객체 세 개씩을 한 페이지로 나누기
    paginator = Paginator(blog_list, 3)

    #request된 페이지가 무엇인 지를 알아내고 (request 페이지를 변수에 담아내고)
    page = request.GET.get('page') # page변수에는 page의 번호가 담길 것.

    #request된 페이지를 얻어온 뒤 return 해 준다.
    posts = paginator.get_page(page) #posts에는 request에 해당하는 페이지가 담길 것.
   
    return render(request, 'home.html', {'blogs' : blogs, 'posts' : posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog' : blog_detail}) # {dictionary형 자료}를 detail.html에 담아서 보내라.

def new(request): #new.html을 띄어주는 함수
    return render(request, 'new.html')

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog() # Blog class로부터 blog 객체를 생성
    blog.title = request.GET['title'] 
    # blog객체의 title메소드에 new.html에서 title이라고하는 form에서 입력한 내용을
    # 여기로 가지고 와 준다.
    
    blog.body = request.GET['body']

    blog.pub_date = timezone.datetime.now() 
    
    # 우변: 블로그를 작성한 시간을 넣어주는 함수 - 위에 from django.utils import timezone 이거 작성해야
    
    
    blog.save()
    # 위에서의 코드를 데이터베이스에 저장하라는 뜻. (cf); 객체.delete - 객체에 해당하는 내용을 데이터베이스에서 지워라.
    
    return redirect('/blog/'+str(blog.id))
    #redirect의 뜻 : 이 url로 넘기세요 // 
    # + str의 뜻 : url은 항상 문자열 형태임. 그런데 blog.id는 int형이므로, str로 형 변환을 시켜준 것임.

    
    #redirect와 render는 교집합이 존재하지만, 배타성도 지닌다.
    #redirect와 render의 차이 : redirect는 프로젝트 외부의 url도 연결가능하다.
    #render : 파이썬 상에서 지지고볶은 데이터를 html파일에 담아서 전송하고 싶을 경우에 사용한다.

def blogpost(request):
    #1. 입력된 내용을 처리하는 기능 -> POST
    #2. 빈 페이지를 띄워주는 기능 -> GET
    if request.method == 'POST':
        form = BlogPost(request.POST) #변수 안에 입력된 내용을 받아준다.
        if form.is_valid(): # 입력된 내용이 잘 입력되었는지 검사를 거친다. (크롬에서 이 입력란을 작성하세요 같은 거)
            post = form.save(commit=False) # 
            post.pub_date = timezone.now() # 입력되지 않은 나머지 값들을 선택적으로 넣어준다. 
            post.save() #save 메소드를 통해 저장한다.
            return redirect('home') # home으로 이동해라
    else:
        form = BlogPost() #비어있는 객체를 반환
        return render(request,'new.html', {'form':form})

def about(request):
    return render(request, 'about.html')