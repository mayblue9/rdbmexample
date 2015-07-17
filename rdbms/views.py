#coding: utf-8
from django.shortcuts import render
# from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection

from rdbms.models import Member

# Create your views here.

def sample1(request):

    if request.method == 'GET' :
        return render(request, "sample1.html", {
            "method": request.method
        })
    else :
        cursor = connection.cursor()
        # row = None;

        print request.POST.get("q")

        cursor.execute(request.POST.get("q"))

        if request.POST.get("q")[0:1].lower() == 's' :
            rows = cursor.fetchall()
        else :
            rows = None


        return render(request, "sample1.html", {
            "rows": rows,
            "method": request.method
        })


def sample2(request):
    if request.method == 'GET' :
        cursor = connection.cursor()
        cursor.execute('select * from rdbms_member');
        rows = cursor.fetchall()

        return render(request, "sample2.html", {
            "rows": rows,
        })
    else :
        cursor = connection.cursor()
        # row = None;

        q = 'insert into rdbms_member (user_id, user_name, user_email, password) values ("' + request.POST.get("user_id") + '", "' + request.POST.get("user_name") + '", "' + request.POST.get("email") + '", "' + request.POST.get("password") + '")'
        cursor.execute(q)


    return HttpResponseRedirect("/2/")

def sample3(request):

    if request.method == 'GET' :

        rows = Member.objects.all();

        return render(request, "sample3.html", {
            "rows": rows,
        })
    else :

        print request.POST.get('password')
        _memberForm = Member()
        _memberForm.user_id    = request.POST.get('user_id')
        _memberForm.user_name  = request.POST.get('user_name')
        _memberForm.user_email = request.POST.get('email')
        _memberForm.password   = request.POST.get('password')

        _memberForm.save()

        return HttpResponseRedirect("/3/")


#insert into rdbms_member_1 (name, birth, email) values ("noggong", "jeng", "noggong@gmail.com")
#insert into member (user_id, user_name, user_email, password) values ("noggong", "우준호", "noggong@gmail.com", "12345")
# select * from rdbms_member_1