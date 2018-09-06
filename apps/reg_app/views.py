from django.shortcuts import render, redirect

# Create your views here.
def index(req):
  return render(req, 'reg_app/index.html')

def process(req):
  req.session['first_name'] = req.POST['first_name']
  req.session['last_name'] = req.POST['last_name']
  return redirect('/show')

def show(req):
  return render(req, 'reg_app/show.html')