import pymysql

"""
从数据库中读取用户信息,以数组格式返回
"""


def read_user_info() -> list:
    db = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='whut_health_report',
                         charset='utf8')
    cursor = db.cursor()  # 获取操作游标
    execute = cursor.execute('select student_number,id_card,nickname from report_app_user')
    lists = cursor.fetchall()
    users: list = tuple2json(lists)
    return users


"""
将tuple数组转为json数组
"""


def tuple2json(users: list) -> list:
    result: list = []
    for info in users:
        user: dict = {'student_number': info[0], 'id_card': info[1], 'nickname': info[2]}
        result.append(user)
    return result

