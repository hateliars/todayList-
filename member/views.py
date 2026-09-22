from django.shortcuts import render, redirect
from django.db import connection

# Create your views here.

def _fetch_all_(sql, params = None) :
    with connection.cursor() as cursor :
        cursor.execute(sql, params or [])
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
def home(request):
    return render(request, 'members/home.html')


def insert_form(request) :
    return render(request, "members/register.html")

def insert(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        birth_date = request.POST.get('birth_date') or None
        age = request.POST.get('age') or None
        points = request.POST.get('points') or 0
        height = request.POST.get('height') or None
        bio = request.POST.get('bio')

        if birth_date:
            birth_date = birth_date.replace("T", " ")
        sql = """INSERT INTO members (username,password, email, birth_date, age, points, height, bio)
                 VALUES (%s,%s, %s, %s, %s, %s, %s, %s)"""
        
        params = (username,password, email, birth_date, age, points, height, bio)
        with connection.cursor() as cursor :
            cursor.execute(sql,params)


    return render(request, 'members/login.html')

def list_members(request) :
    members = _fetch_all_("SELECT id, username, email, birth_date, age, points, height, bio, created_at, updated_at "
                          "FROM MEMBERS ORDER BY id desc")
    return render(request,"members/list.html", {"members" : members})

def update_form(request) :
    return render(request, "members/update.html")

def update(request) :
    if request.method == "POST" :
        id = request.POST.get('id')
        username = request.POST.get('username')
        email = request.POST.get('email')
        birth_date = request.POST.get('birth_date') or None
        age = request.POST.get('age') or None
        points = request.POST.get('points') or 0
        height = request.POST.get('height') or None
        bio = request.POST.get('bio')    

        if birth_date :
            birth_date = birth_date.replace("T", " ")
        sql = """UPDATE members SET username = %s, email = %s, birth_date = %s, age = %s, points = %s, height = %s, bio = %s
                 WHERE id = %s""" 
        params = (username,email,birth_date,age,points,height,bio,id)
        with connection.cursor() as cursor :
            cursor.execute(sql,params)  

    return render(request, 'members/home.html')

def delete_form(request) :
    return render(request, 'members/delete.html')

def delete(request,member_id) :
    if request.method == "POST" :
        #id = request.POST.get('id')  
        sql = """DELETE FROM members WHERE id = %s""" 
        with connection.cursor() as cursor :
            cursor.execute(sql,[member_id])  

    return render(request, 'members/home.html')


def login_form(request) :
    return render(request, 'members/login.html')

def login(request) :
    if request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')

        sql = """SELECT ID,USERNAME,PASSWORD FROM MEMBERS WHERE USERNAME = %s AND PASSWORD = %s"""


        with connection.cursor() as cursor:
            cursor.execute(sql, [username, password])
            member = cursor.fetchone()

        if member:
            # 로그인 성공
            request.session['username'] = member[1]
            request.session['id'] = member[0]
            print("로그인 직후:", request.session.items())
            return redirect('todo:todo')
        else:
            # 로그인 실패
            return render(request, 'members/login.html', {
                'error': '아이디 또는 비밀번호가 잘못되었습니다.'
            })


def logout(request) :
    request.session.flush()

    return redirect('/member/')

def mypage(request):

    member_id = request.session.get('id')

    if not member_id:
        return redirect('/member/')

    sql = """
        SELECT id, username, password, email,
               birth_date, age, points, height, bio
        FROM members
        WHERE id = %s
    """

    with connection.cursor() as cursor:
        cursor.execute(sql, [member_id])
        member = cursor.fetchone()

    return render(request, 'members/mypage.html', {
        'member': member
    })

def mypageUpdate(request):

    member_id = request.session.get('id')

    if not member_id:
        return redirect('/member/')

    if request.method == "POST":

        password = request.POST.get('password')
        email = request.POST.get('email')
        birth_date = request.POST.get('birth_date')
        age = request.POST.get('age')
        height = request.POST.get('height')
        bio = request.POST.get('bio')

        if password:
            sql = """
                UPDATE members
                SET password = %s,
                    email = %s,
                    birth_date = %s,
                    age = %s,
                    height = %s,
                    bio = %s
                WHERE id = %s
            """

            params = (
                password,
                email,
                birth_date,
                age,
                height,
                bio,
                member_id
            )

        else:
            sql = """
                UPDATE members
                SET email = %s,
                    birth_date = %s,
                    age = %s,
                    height = %s,
                    bio = %s
                WHERE id = %s
            """

            params = (
                email,
                birth_date,
                age,
                height,
                bio,
                member_id
            )

        with connection.cursor() as cursor:
            cursor.execute(sql, params)

        return redirect('/todo/')

    return redirect('/todo/')


def mypageDelete(request):

    member_id = request.session.get('id')

    if not member_id:
        return redirect('/member/')

    if request.method == "POST":


        # 회원 삭제
        member_sql = """DELETE FROM membersWHERE id = %s"""

        with connection.cursor() as cursor:

            cursor.execute(member_sql, [member_id])

        request.session.flush()

        return redirect('/member/')

    return redirect('/member/mypage/')

            