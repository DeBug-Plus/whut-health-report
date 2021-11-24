import os
import time

import requests
import random
import json
import read_user_info
def request_sessionId(json_data):
    url = "https://zhxg.whut.edu.cn/yqtjwx/api/login/checkBind"
    useragentlist = [
        "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; MI 6 Build/NXTHUAWEI) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/9.9 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 baiduboxapp/0_01.5.2.8_enohpi_6311_046/5.3.9_1C2%8enohPi/1099a/7D4BD508A31C4692ACC31489A6AA6FAA3D5694CC7OCARCEMSHG/1",
        "Mozilla/5.0 (Linux; U; Android 4.4.4; en-us; vivo X5Max Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.5.0) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 baiduboxapp/0_01.5.2.8_enohpi_8022_2421/2.01_2C2%8enohPi/1099a/05D5623EBB692D46C9C9659B23D68FBD5C7FEB228ORMNJBQOHM/1",
        "Mozilla/5.0 (Linux; Android 8.0.0; BKL-AL00 Build/HUAWEIBKL-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.19 SP-engine/2.15.0 baiduboxapp/11.19.5.10 (Baidu; P1 8.0.0)",
        "Mozilla/5.0 (Linux; Android 8.1.0; vivo X20 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.19 SP-engine/2.15.0 baiduboxapp/11.19.5.10 (Baidu; P1 8.1.0)",
        "Mozilla/5.0 (Linux; Android 9; DUK-AL20 Build/HUAWEIDUK-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.19 SP-engine/2.15.0 baiduboxapp/11.19.5.10 (Baidu; P1 9)"
    ]
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "content-type": "application/json",
        "Referer": "https://servicewechat.com/wxa0738e54aae84423/17/page-frame.html",
        "X-Tag": "flyio",
        "Content-Length": "100",
        "Accept-Language": "zh-cn",
        "Connection": "keep - alive",
        "Host": "zhxg.whut.edu.cn"
    }
    headers['User-Agent'] = random.choice(useragentlist)
    r = requests.post(url=url, headers=headers, json=json_data, verify=False)
    result = json.loads(r.text)
    sessionId = result['data']['sessionId']
    return str(sessionId)


def request_bindUserInfo(sessionId, json_data) -> bool:
    url = "https://zhxg.whut.edu.cn/yqtjwx/api/login/bindUserInfo"
    useragentlist = [
        "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; MI 6 Build/NXTHUAWEI) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/9.9 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 baiduboxapp/0_01.5.2.8_enohpi_6311_046/5.3.9_1C2%8enohPi/1099a/7D4BD508A31C4692ACC31489A6AA6FAA3D5694CC7OCARCEMSHG/1",
        "Mozilla/5.0 (Linux; U; Android 4.4.4; en-us; vivo X5Max Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.5.0) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 baiduboxapp/0_01.5.2.8_enohpi_8022_2421/2.01_2C2%8enohPi/1099a/05D5623EBB692D46C9C9659B23D68FBD5C7FEB228ORMNJBQOHM/1",
        "Mozilla/5.0 (Linux; Android 8.0.0; BKL-AL00 Build/HUAWEIBKL-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.19 SP-engine/2.15.0 baiduboxapp/11.19.5.10 (Baidu; P1 8.0.0)",
        "Mozilla/5.0 (Linux; Android 8.1.0; vivo X20 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.19 SP-engine/2.15.0 baiduboxapp/11.19.5.10 (Baidu; P1 8.1.0)",
        "Mozilla/5.0 (Linux; Android 9; DUK-AL20 Build/HUAWEIDUK-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.19 SP-engine/2.15.0 baiduboxapp/11.19.5.10 (Baidu; P1 9)"
    ]
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "content-type": "application/json",
        "Referer": "https://servicewechat.com/wxa0738e54aae84423/17/page-frame.html",
        "Cookie": "JSESSIONID=%s" % (sessionId),
        "Accept": "*/*",
        "X-Tag": "flyio",
        "Content-Length": "2",
        "Accept-Language": "zh-cn",
        "Connection": "keep - alive",
        "Host": "zhxg.whut.edu.cn"
    }
    headers['User-Agent'] = random.choice(useragentlist)
    response = requests.post(url=url, headers=headers, json=json_data, verify=False)
    response_json = response.json()
    if response_json['status'] == True:
        return True
    else:
        return False


def request_monitorRegister(name, sessionId, province, city, county, street):
    currentAddress = str(province) + str(city) + str(county) + str(street)
    url = "https://zhxg.whut.edu.cn/yqtjwx/./monitorRegister"
    useragentlist = [
        "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; MI 6 Build/NXTHUAWEI) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/9.9 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 baiduboxapp/0_01.5.2.8_enohpi_6311_046/5.3.9_1C2%8enohPi/1099a/7D4BD508A31C4692ACC31489A6AA6FAA3D5694CC7OCARCEMSHG/1",
        "Mozilla/5.0 (Linux; U; Android 4.4.4; en-us; vivo X5Max Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.5.0) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 baiduboxapp/0_01.5.2.8_enohpi_8022_2421/2.01_2C2%8enohPi/1099a/05D5623EBB692D46C9C9659B23D68FBD5C7FEB228ORMNJBQOHM/1",
        "Mozilla/5.0 (Linux; Android 8.0.0; BKL-AL00 Build/HUAWEIBKL-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.19 SP-engine/2.15.0 baiduboxapp/11.19.5.10 (Baidu; P1 8.0.0)",
        "Mozilla/5.0 (Linux; Android 8.1.0; vivo X20 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.19 SP-engine/2.15.0 baiduboxapp/11.19.5.10 (Baidu; P1 8.1.0)",
        "Mozilla/5.0 (Linux; Android 9; DUK-AL20 Build/HUAWEIDUK-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.19 SP-engine/2.15.0 baiduboxapp/11.19.5.10 (Baidu; P1 9)"
    ]
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "content-type": "application/json",
        "Referer": "https://servicewechat.com/wxa0738e54aae84423/17/page-frame.html",
        "Cookie": "JSESSIONID=%s" % (sessionId),
        "Accept": "*/*",
        "X-Tag": "flyio",
        "Content-Length": "203",
        "Accept-Language": "zh-cn",
        "Connection": "keep - alive",
        "Host": "zhxg.whut.edu.cn"
    }
    headers['User-Agent'] = random.choice(useragentlist)
    json_data = {
        "diagnosisName": "",
        "relationWithOwn": "",
        "currentAddress": currentAddress,
        "remark": "无",
        "healthInfo": "正常",
        "isDiagnosis": 0,
        "isFever": 0,
        "isInSchool": "1",
        "isLeaveChengdu": 0,
        "isSymptom": "0",
        "temperature": "36.5°C~36.9°C",
        "province": province,
        "city": city,
        "county": county
    }
    response = requests.post(url=url, headers=headers, json=json_data, verify=False)
    response_json = response.json()
    if response_json['status'] == True:
        return True
    else:
        return False


def cancelBind(sessionId):
    url = "https://zhxg.whut.edu.cn/yqtjwx/api/login/cancelBind"
    useragentlist = [
        "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; MI 6 Build/NXTHUAWEI) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/9.9 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 baiduboxapp/0_01.5.2.8_enohpi_6311_046/5.3.9_1C2%8enohPi/1099a/7D4BD508A31C4692ACC31489A6AA6FAA3D5694CC7OCARCEMSHG/1",
        "Mozilla/5.0 (Linux; U; Android 4.4.4; en-us; vivo X5Max Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.5.0) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 baiduboxapp/0_01.5.2.8_enohpi_8022_2421/2.01_2C2%8enohPi/1099a/05D5623EBB692D46C9C9659B23D68FBD5C7FEB228ORMNJBQOHM/1",
        "Mozilla/5.0 (Linux; Android 8.0.0; BKL-AL00 Build/HUAWEIBKL-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.19 SP-engine/2.15.0 baiduboxapp/11.19.5.10 (Baidu; P1 8.0.0)",
        "Mozilla/5.0 (Linux; Android 8.1.0; vivo X20 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.19 SP-engine/2.15.0 baiduboxapp/11.19.5.10 (Baidu; P1 8.1.0)",
        "Mozilla/5.0 (Linux; Android 9; DUK-AL20 Build/HUAWEIDUK-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.19 SP-engine/2.15.0 baiduboxapp/11.19.5.10 (Baidu; P1 9)"
    ]
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "content-type": "application/json",
        "Referer": "https://servicewechat.com/wxa0738e54aae84423/17/page-frame.html",
        "Cookie": "JSESSIONID=%s" % (sessionId),
        "Connection": "keep - alive",
        "Host": "zhxg.whut.edu.cn"
    }
    headers['User-Agent'] = random.choice(useragentlist)
    requests.post(url=url, headers=headers, verify=False)


def report(sn, idCard, nickName) -> str:
    province = '湖北省'
    city = '武汉市'
    county = '洪山区'
    street = '工大路'
    json_data = {
        "sn": sn,
        "idCard": idCard,
        "nickname": nickName
    }
    sessionId = request_sessionId(json_data)
    flag = request_bindUserInfo(sessionId, json_data)
    if flag == False:
        return '该学号已被其它微信绑定，请先解除绑定'
    flag = request_monitorRegister(nickName, sessionId, province, city, county, street)
    cancelBind(sessionId)
    if flag == True:
        return '填报成功'
    else:
        return '今日已填报'


"""
@Usage:执行单个填报操作
"""


def do_report(sn, idCard, nickName):
    # 进行填报，记录填报结果
    msg = report(sn, idCard, nickName)

    # 将其写到log中，便于查看
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    log = current_time + ', ' + 'StudentNumber: ' + sn + ', ' + msg
    current_dir = os.path.join(os.path.dirname(__file__), 'report_log.txt')
    with open(current_dir, "a", encoding="UTF-8") as f:
        f.write(log + '\n')
        f.flush()


"""
@Usage:执行批量操作，从json文件中读取用户信息。
"""


def start():
    # user_info_dir = os.path.join(os.path.dirname(__file__), 'user_info.json')
    # with open(user_info_dir, 'r', encoding='utf-8') as f:
    #     users: list = json.load(f)['users']
    # 新增的从数据库中读取数据
    users = read_user_info.read_user_info()

    for user in users:
        print(user)
        sn = user['student_number']
        idCard = user['id_card']
        nickName = user['nickname']
        do_report(sn,idCard,nickName)


if __name__ == '__main__':
    start()


