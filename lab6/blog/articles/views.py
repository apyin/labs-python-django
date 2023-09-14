from .models import Article
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import redirect
from django.shortcuts import render

# Create your views here.
def add_user(request):
	if not request.user.is_authenticated:
		if request.method == "POST":
			# обработать данные формы, если метод POST
			form = {
			'login': request.POST["login"],
			'email': request.POST["email"],
			'password': request.POST["password"],
			}
			if form["login"] and form["email"] and form["password"]:
				# если все поля заполнены
				try:
					User.objects.get(username=form["login"])
					# если логин занят, то ошибки не произойдет и
					# программа удачно доберется до следующей строчки
					form['errors'] = u"Пользователь с таким именем уже есть"
					return render(request, 'add_user.html', {'form': form})
				except User.DoesNotExist:
					try:
						User.objects.get(email=form["email"])
						# если e-mail занят, то ошибки не произойдет и
						# программа удачно доберется до следующей строчки
						form['errors'] = u"Пользователь с таким e-mail уже есть"
						return render(request, 'add_user.html', {'form': form})
					except User.DoesNotExist:
						User.objects.create_user(form["login"], form["email"], form["password"])
						return redirect('archive')
			else:
				# если введенные данные некорректны
				form['errors'] = u"Не все поля заполнены"
				return render(request, 'add_user.html', {'form': form})
		else:
			# просто вернуть страницу с формой, если метод GET
			return render(request, 'add_user.html', {})
	else:
		# если пользователь авторизован, ему не нужно выдавать форму регистрации
		raise Http404
						
def archive(request):
   return render(request, 'archive.html', {"posts": Article.objects.all()})
  
def auth_login(request):
	if not request.user.is_authenticated:
		if request.method == "POST":
			# обработать данные формы, если метод POST
			form = {
			'login': request.POST["login"],
			'password': request.POST["password"]
			}
			if form["login"] and form["password"]:
				# если все поля заполнены
				user = authenticate(username=form["login"], password=form["password"])
				if user is None:
					form['errors'] = u"Такого аккаунта не существует"
					return render(request, 'auth_login.html', {'form': form})
				else:
					login(request, user)
					# перейти на страницу всех записей
					return redirect('archive')
			else:
				# если введенные данные некорректны
				form['errors'] = u"Не все поля заполнены"
				return render(request, 'auth_login.html', {'form': form})
		else:
			# просто вернуть страницу с формой, если метод GET
			return render(request, 'auth_login.html', {})
	else:
		# если пользователь авторизован, ему не нужно выдавать форму аутентификации
		raise Http404	
								
def create_post(request):
	if not request.user.is_anonymous:
		if request.method == "POST":
			# обработать данные формы, если метод POST
			form = {
			'text': request.POST["text"],
			'title': request.POST["title"]
			}
			# в словаре form будет храниться информация, введенная пользователем
			if form["text"] and form["title"]:
				# если все поля заполнены
				try:
					Article.objects.get(title=form["title"])
					form['errors'] = u"Статья с таким названием уже есть"
					return render(request, 'create_post.html', {'form': form})
				except Article.DoesNotExist:
					article = Article.objects.create(text=form["text"],
					title=form["title"], author=request.user)					
					return redirect('get_article', article_id=article.id)
				# перейти на страницу поста
			else:
				# если введенные данные некорректны
				form['errors'] = u"Не все поля заполнены"
				return render(request, 'create_post.html', {'form': form})
		else:
			# просто вернуть страницу с формой, если метод GET
			return render(request, 'create_post.html', {})
	else:
		raise Http404
		
def get_article(request, article_id):
	try:
		post = Article.objects.get(id=article_id)
		return render(request, 'article.html', {"post": post})
	except Article.DoesNotExist:
		raise Http404