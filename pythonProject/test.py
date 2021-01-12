from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app

from app.module import dbModule

test = Blueprint('test', __name__, url_prefix='/test')


def select_data():
    db_class = dbModule.Database()
    sql = "SELECT idx, test \
                FROM testTable"
    row = db_class.executeAll(sql)
    # print(row)
    return row


@test.route('/', methods=['GET'])
def index():
    return render_template('/test/test.html',
                           result=None,
                           resultData=None,
                           resultUPDATE=None)


# INSERT 함수 예제
@test.route('/insert', methods=['GET'])
def insert():
    db_class = dbModule.Database()

    sql = "INSERT INTO testTable(test) \
                VALUES('%s')" % ('testData')
    db_class.execute(sql)
    db_class.commit()

    row = select_data()

    return render_template('/test/test.html',
                           result=row,
                           resultData=None,
                           resultUPDATE=None)


# SELECT 함수 예제
@test.route('/select', methods=['GET'])
def select():
    db_class = dbModule.Database()

    row = select_data()

    return render_template('/test/test.html',
                           result=row,
                           resultData=row if len(row) < 1 else row[0],
                           resultUPDATE=None)


# SELECT 함수 예제
@test.route('/delete', methods=['GET'])
def delete():
    db_class = dbModule.Database()

    sql = "Delete FROM testTable where idx = (SELECT max(idx) FROM `testTable`) "
    db_class.execute(sql)
    db_class.commit()

    row = select_data()

    return render_template('/test/test.html',
                           result=row,
                           resultData=row if len(row) < 1 else row[0],
                           resultUPDATE=None)



# UPDATE 함수 예제
@test.route('/update', methods=['GET'])
def update():
    db_class = dbModule.Database()

    sql = "UPDATE testTable \
                SET test='%s' \
                WHERE test='testData'" % ('update_Data')
    db_class.execute(sql)
    db_class.commit()

    row = select_data()

    return render_template('/test/test.html',
                           result=row,
                           resultData=None,
                           resultUPDATE=row[0])
