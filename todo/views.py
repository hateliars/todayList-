from django.shortcuts import render, redirect
from django.db import connection
from datetime import datetime


# Create your views here.

def todo(request):
    member_id = request.session.get('id')

    if not member_id:
        return redirect('/member/')

    sql = """
        SELECT todoId, todoName, startDate, endDate, todoOrder, completed
        FROM todos
        WHERE memberId = %s
        ORDER BY todoOrder
    """

    with connection.cursor() as cursor:
        cursor.execute(sql, [member_id])
        todos = cursor.fetchall()

    print("Todo 진입:", request.session.items())
    username = request.session.get('username')

    # 날짜 비교 

    todo_list = []

    for todo in todos :
        urgent = isUrgent(todo[3], todo[5])

        todo_list.append((todo[0],todo[1],todo[2],todo[3],todo[4],todo[5],urgent))


    return render(request, 'todo/todo.html', {
        'todos': todo_list,
        'username': username
    })

def todoInsert(request):

    member_id = request.session.get('id')

    if not member_id:
        return redirect('/member/')

    if request.method == "POST":

        todoName = request.POST.get("todoName")
        startDate = request.POST.get("startDate")
        endDate = request.POST.get("endDate")

        if startDate == '':
            startDate = None

        if endDate == '':
            endDate = None

        sql = """
            INSERT INTO todos
                (memberId, todoName, startDate, endDate, todoOrder, completed)
            VALUES
                (%s, %s, %s, %s, %s, %s)
        """

        order_sql = """
            SELECT COALESCE(MAX(todoOrder), 0) + 1
            FROM todos
            WHERE memberId = %s
        """

        with connection.cursor() as cursor:

            cursor.execute(order_sql, [member_id])
            todoOrder = cursor.fetchone()[0]
            params= (member_id,todoName,startDate,endDate,todoOrder,0)

            cursor.execute(sql,params)

        return redirect('/todo/')

    return redirect('/todo/')


def todoUpdate(request) :
    member_id = request.session.get('id')

    if not member_id :
        return redirect('/member/')

    if request.method == "POST":
        todoId = request.POST.get('todoId')
        todoName = request.POST.get("todoName")

        sql = "UPDATE todos SET todoName = %s WHERE todoId = %s AND memberId = %s"

        params = (todoName, todoId, member_id)

        with connection.cursor() as cursor:
            cursor.execute(sql, params)

        return redirect('/todo/')

    return redirect('/todo/')


def todoDelete(request):

    member_id = request.session.get('id')

    if not member_id:
        return redirect('/member/')

    if request.method == "POST":

        todoId = request.POST.get('todoId')

        sql = """
            DELETE FROM todos
            WHERE todoId = %s
            AND memberId = %s
        """

        with connection.cursor() as cursor:
            cursor.execute(sql, [todoId, member_id])

        return redirect('/todo/')

    return redirect('/todo/')

def todoComplete(request):

    member_id = request.session.get('id')

    if not member_id:
        return redirect('/member/')

    if request.method == "POST":

        todoId = request.POST.get('todoId')
        completed = request.POST.get('completed')

        sql = """
            UPDATE todos
            SET completed = %s
            WHERE todoId = %s
            AND memberId = %s
        """

        with connection.cursor() as cursor:
            cursor.execute(
                sql,
                [completed, todoId, member_id]
            )

        return redirect('/todo/')

    return redirect('/todo/')


def isUrgent(endDate, completed) :

    if not endDate or completed : 
        return False 

    now = datetime.now()
    remaining = endDate - now

    if 0 < remaining.total_seconds() <= 86400 :
        return True 

    return False 


    
    