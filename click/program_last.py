import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import datetime
import json

def main():
    chrome_option = Options()
    chrome_option.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_option)
    current_datetime = datetime.datetime.now()
    num_search_engine=random.randint(0,len(Environment['search_engine_name'])-1)
    num_search_engine = 1
    driver.get(Environment['search_engine_name'][num_search_engine]["liulanqi"])
    path_log = os.path.join(os.getcwd(), 'log')  # 日志文件夹的创建地址
    if not os.path.exists(path_log):
        os.makedirs(path_log)
        print('log 创建成功')
    else:
        print('log文件夹已经存在')
    Now_time = current_datetime.strftime("%Y-%m-%d-%H-%M")
    log_file_name = os.path.join(path_log, f'{Now_time}')
    file = open(f'{log_file_name}.txt', 'w')  # 创建日志文件
    x = 1
    file.write(f'开始打开{Environment["search_engine_name"][num_search_engine]["liulanqi"]}\n')
    file.flush()
    wait = WebDriverWait(driver, 10)
    for key in Environment['search_words']:
        textbox = driver.find_element(by=By.ID, value=f'{Environment["search_engine_name"][num_search_engine]["id"]}')
        submit_button = driver.find_element(by=By.ID, value=f'{Environment["search_engine_name"][num_search_engine]["buttom"]}')
        textbox.clear()
        textbox.send_keys(key['kw'])
        try:
            submit_button.click()
        except:
            textbox.submit()
        file.write(f'开始搜索第{x}个关键词{key["kw"]}\n')
        file.flush()
        ye_num = 1
        while True:
                time.sleep(Environment['time'])  # 必要的延时，加载数据，才能获取目标
                try:
                    parament_s = driver.find_elements(by=By.XPATH, value="//*[@class='%s']//a[@href]" % Environment["search_engine_name"][num_search_engine]["filter"])  # 获得所有超链接
                except:
                    file.write(f'第{x}个关键词当前第{ye_num}页面获取链接失败\n')
                    file.flush()
                    continue
                lenth_p = len(parament_s)
                file.write(f'进入第{ye_num}页,含{lenth_p}个选项\n')
                file.flush()
                for parament in range(0, lenth_p):
                    time.sleep(random.randint(Environment['time']-2, Environment['time']))
                    driver.execute_script(f'window.scrollBy(0,{random.randint(300, 700)})')  # 模拟滑动
                    x_1 = 0
                    while True:
                        try:
                            x_1 = x_1 + 1
                            time.sleep(random.randint(Environment['time']-2,Environment['time']))
                            parament_s = driver.find_elements(by=By.XPATH, value="//*[@class='%s']//a[@href]" %
                                                                                 Environment["search_engine_name"][
                                                                                     num_search_engine]["filter"]) # 所在超链接的关键字
                            break
                        except:
                            if x_1 < 10:
                                file.write(f'第{x}个关键词当前第{ye_num}页面第{parament}个参数获取链接失败\n')
                                file.flush()
                                continue
                            else :
                                exit(1)
                    url = parament_s[parament].get_attribute('href')
                    text = parament_s[parament].get_attribute('innerText')
                    if key['target']['type'] == 'word':  # 匹配关键字
                        for value in key["target"]["value"]:
                            if value in text:
                                file.write(f'找到匹配关键词{value}   在标题{text}中\n')
                                file.flush()
                                x_2 = 0
                                while True:
                                    try:
                                        x_2 = x_2 + 1
                                        driver.get(url)
                                        time.sleep(random.randint(Environment['time'] - 2, Environment['time']))
                                        file.write(f'打开链接{url}\n')
                                        file.write(f'当前窗口标题为{text}的页面中\n')
                                        file.flush()
                                        driver.execute_script(f'window.scrollBy(0,{random.randint(500, 700)})')
                                        time.sleep(random.randint(Environment["target_see_time"]-3, Environment["target_see_time"]+3))
                                        driver.execute_script("var q=document.documentElement.scrollTop=0")
                                        break
                                    except:
                                        if x_2 < 10:
                                            file.write(
                                                f'第{x}个关键词当前第{ye_num}页面第{parament}个参数跳转链接失败，继续尝试\n')
                                            continue
                                        else:
                                            exit(1)
                                try:
                                    driver.back()  # 返回主页面
                                    file.write('关闭窗口\n')
                                except:
                                    file.write(f'第{x}个关键词当前第{ye_num}页面第{parament}个参数返回失败,,,,,,,\n')
                                    file.flush()
                                    exit(1)  # 遇到问题直接重启,这种一般是遇到机器人检测了
                                break
                            else:
                                x = random.randint(0,6)
                                if x>=5:
                                    x_3 = 0
                                    while True:
                                        try:
                                            x_3 = x_3 + 1
                                            driver.get(url)
                                            time.sleep(random.randint(Environment['time'] - 2, Environment['time']))
                                            file.write(f'打开链接{url}\n')
                                            file.write(f'当前窗口标题为{text}的页面中\n')
                                            file.flush()
                                            driver.execute_script(f'window.scrollBy(0,{random.randint(500, 700)})')
                                            time.sleep(random.randint(Environment["target_see_time"]-3, Environment["target_see_time"]+3))
                                            driver.execute_script("var q=document.documentElement.scrollTop=0")
                                            break
                                        except:
                                            if x_3 <10:
                                                file.write(
                                                    f'第{x}个关键词当前第{ye_num}页面第{parament}个参数跳转链接失败，继续尝试\n')
                                                continue
                                            else :
                                                exit(1)
                                    try:
                                        driver.back()  # 返回主页面
                                        file.write('关闭窗口\n')
                                    except:
                                        file.write(f'第{x}个关键词当前第{ye_num}页面第{parament}个参数返回失败,,,,,,,\n')
                                        file.flush()
                                        exit(1)  # 遇到问题直接重启,这种一般是遇到机器人检测了
                    else:
                        print('匹配只能word格式')
                        exit(1)
                time.sleep(2)
                try:
                    if num_search_engine == 1:
                        next_page_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "下一页 >")))
                        # xiayiye = driver.find_elements(by=By.XPATH, value="//*[@class='%s']//a[@class='%s']" %(Environment["search_engine_name"][num_search_engine]["the_next_first"],Environment["search_engine_name"][num_search_engine]["the_next_second"]))
                    else:
                        next_page_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.sb_pagN")))
                        # xiayiye = driver.find_element(by=By.XPATH, value="//*[@class='%s']//a[@class='%s']" %(Environment["search_engine_name"][num_search_engine]["the_next_first"],Environment["search_engine_name"][num_search_engine]["the_next_second"]))
                except:
                    file.write(f'第{x}个关键词当前第{ye_num}页面获取下一页失败\n')
                    file.flush()
                    break
                next_page_button.click()
                x_4 = 0
                while True:
                    try:
                        x_4 = x_4 + 1
                        if num_search_engine == 1:
                            wait.until(EC.presence_of_element_located((By.ID, "content_left")))
                        else:
                            wait.until(EC.presence_of_element_located((By.ID, "b_content")))
                        time.sleep(2)  # 等待2秒以确保页面完全加载
                        break
                    except:
                        if x_4 <10:
                            file.write(f'第{x}个关键词当前第{ye_num}页面跳转下一页失败\n')
                            continue
                        else:
                            exit(1)
                ye_num = ye_num + 1
        x = x + 1  # 换成下一个匹配策略
    file.close()
    driver.delete_all_cookies()
    driver.close()

def delDir(dir, datatime01):
    # 获取文件夹下所有文件和文件夹
    files = os.listdir(dir)
    for file in files:
        filePath = dir + "/" + file
         # 最后一次修改的时间
        last1 = os.stat(filePath).st_mtime  # 获取文件的时间戳
        filetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(last1))  # 将时间戳格式化成时间格式的字符串
        # 删除七天前的文件
        if (datatime01 > filetime):  # datatime01是当前时间7天前的时间，filetime是文件修改的时间，如果文件时间小于(早于)datatime01时间，就删除
            os.remove(filePath)
            print(filePath + " was removed!")
if __name__== '__main__':
    path_json = os.path.join(os.getcwd(), 'environment.json')
    if not os.path.exists(path_json):
        print("环境配置文件environment.log未发现\n")
        exit(0)
    file_json = open(path_json, 'r')
    content = file_json.read()
    Environment = json.loads(content)
    file_json.close()
    path = os.path.join(os.getcwd(),'log')
    # 获取过期时间
    starttime = datetime.datetime.now()
    d1 = starttime + datetime.timedelta(days=-7)
    date1 = str(d1)
    index = date1.find('.')  # 第一次出现的位置
    datatime01 = date1[:index]
    while True:
        try:
            while True:
                for i in range(Environment['num_repete']):  #一次运行num次,相隔skip_time重新运行
                    main()
                    delDir(path, datatime01)
                    time.sleep(120)
                time.sleep(Environment['skip_time'])
        except:
            continue





