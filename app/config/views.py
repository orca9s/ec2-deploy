from django.shortcuts import render


def index(request):
	# TEMPLATE설정에 app/template폴더 추가
	# templates폴더에 'index.html'추가

	# STATICFILES_DIRS에 app/static폴더 추가
	# static/css폴더에 Bootstrap CSS파일(css/bootst
	return render(request, 'index.html')