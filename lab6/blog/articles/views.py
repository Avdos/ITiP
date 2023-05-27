from .models import Article
from .models import User
from .models import authenticate
from .models import login
from .models import logout
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})
def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404
def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
        # обработать данные формы, если метод POST
            if Article.objects.filter(title=request.POST["title"]).count() == 0: 
                form = {
                    'text': request.POST["text"], 'title': request.POST["title"]
                }
            # в словаре form будет храниться информация, введенная пользователем
                if form["text"] and form["title"]:
            # если поля заполнены без ошибок
                    article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                    return redirect('get_article', article_id=article.id)
                # перейти на страницу поста
                else:
            # если введенные данные некорректны
                    form['errors'] = u"Не все поля заполнены"
                    return render(request, 'create_post.html', {'form': form})
            else:
                form = {}
                form['errors'] = u"Статья с таким названием уже существует"
                return render(request, 'create_post.html', {'form': form})
                
        else:
        # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})
    else:
        return redirect('archive')

def create_user(request):
    if request.method == "POST":
        if User.objects.filter(username=request.POST["login"]).count() == 0:
            form = {'email': request.POST["email"], 'username': request.POST["login"], 'password': request.POST["psw"]}
            if form["email"] and form["username"] and form["password"]:
                user=User.objects.create(username=form["username"], email=form["email"], password=form["password"])
                user.set_password(form["password"])
                user.save()
                return redirect('login')
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_user.html', {'form': form})
            
        else:
            form ={}
            form['errors'] = u"Пользователь с таким именем уже есть"
            return render(request, 'create_user.html', {'form': form})

    else:
        # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_user.html', {})

def login_user(request):
    if request.user.is_authenticated:
                return redirect('archive')
        
    if request.method == "POST":
        if User.objects.filter(username=request.POST["login"]).count() != 0:
            form = {'username': request.POST["login"], 'password': request.POST["password"]}
            if form["username"] and form["password"]:
                user=authenticate(username=form["username"], password=form["password"])
                if user is not None:
                    login(request, user)
                    return redirect('archive')
                else:
                    form['errors'] = u"Неправильный логин или пароль"
                    return render(request, 'login_user.html', {'form': form})
                    
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'login_user.html', {'form': form})
            
        else:
            form ={}
            form['errors'] = u"Пользователя с таким именем не существует"
            return render(request, 'login_user.html', {'form': form})

    else:
        # просто вернуть страницу с формой, если метод GET
            return render(request, 'login_user.html', {})

def logout_user(request):
    logout(request)
    return redirect('login')
    
    
    

    


