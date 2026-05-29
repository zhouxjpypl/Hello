#!/usr/bin/env python3
"""
Hello类
包含多种功能
"""
import os
import random
import datetime
import sys
import time
import subprocess
import AZZ2 as azz
import re
import hashlib
from multiprocessing import Process
class  SystemDoesNotSupport(Exception):
    pass

class NotFilled(Exception):
    pass
class NoRightToSpeak(Exception):
    pass
class VoiceNotAvailable(Exception):
    pass
class RepeatCalls(Exception):
    pass
class CannotBeSaved(Exception):
    pass
class NoneError(Exception):
    pass
class Hello:
    """
    打招呼类
    函数数量未定
    无返回值
    """
    total_instances = 0

    def __init__(self,name : str = 'xxx',age : int = None,gender : str = None,say : bool = True,polite : bool = False,voice_enabled : bool = True,job : str = 'unknow'):
        """
        构造函数
        初始化变量
        """
        self.hello_speak = ["Hi", "Hello", "Hey", "Yo"]
        self.emojis = ["\U0001F970","\U0001F60E","\U0001F609","\U0001F642","\U0001F604","\U0001F600","\U0001F60A","\U0001F389","\U0001F92C","\U0001F62A"]
        self.voice_enabled = voice_enabled
        self.polite = polite
        self.talk_count = 0
        self.number_of_uses = 0
        self.name = name
        self.age = age
        self.gender = gender
        self.say = say
        self.person = None
        self.plat = sys.platform
        self.last_birthday_date = None
        self.job = job
        self.nerror = 0
        self.xn = 0
        self.shell_open = False
        self.pet = False
        self.nickname = None
        self.version = "1.0.0"
        if os.path.exists("v.txt") and os.path.getsize("v.txt") != 0:
            with open("v.txt", "r", encoding="UTF-8") as f:
                self.version = f.read().strip()
        #print(f"{self.say,self.gender,self.age,self.name}")
        if self.age == None:
            self.age = random.randint(1,100)
        if self.gender == None:
            self.gender = 'it'
        if self.gender == '女' or self.gender == 'woman':
            self.person = 'She'
        elif self.gender == '男' or self.gender == 'man':
            self.person = 'He'
        else:
            self.person = self.gender
        name = re.match(r'^([A-Za-z][a-z]{1,19})$|^([\u4e00-\u9fa5]{1,4})$',self.name)
        if name:
            name = name.group(1) or name.group(2)
            self.name = name
        else:
            print("The person's name is illegal,but we will keep it")
            self.name = self.name
        self._apply_easter_eggs()
        Hello.total_instances += 1

    def set_mood(self, mood: str):
        self.mood = mood.lower()
    def _apply_easter_eggs(self):
        if self.name == "PingPing":
            print("Wow, it's the author! Please feel free to command me >_<")
            self.polite = True
        elif self.name == "HelloKitty":
            print("Meow~")
        elif self.name == "test":
            print("Test mode has been activated")
            self.talk_count = 0
    def hello(self):
        """
        最简单的打招呼
        """
        if self.polite:
            print(f"Hello,dear {self.name}")
        else:
            print(f"Hi, {self.name}")
        self.talk_count += 1
    def introduction(self):
        """
        介绍
        """
        print(f"{self.person} is {self.name}, and this year {self.age} is the year,{self.person}'s occupation is: {self.job}")
        if self.pet:
            print(f"{self.name} raised a {self.pet_type}, its name is: {self.pet_name}")
        self.talk_count += 1
    def say_hello(self):
        """
        语音打招呼
        只有MacOS可运行，其他会报System_Does_Not_Support
        建议windows用户不要尝试
        """
        if self.plat.startswith('darwin'):
            if self.voice_enabled:
                if self.say:
                    if self.polite:

                        os.system(f"say 'Hello,dear {self.name}'")

                    else:
                        os.system(f"say 'Hi, {self.name}'")
                else:
                    self.nerror += 1
                    raise NoRightToSpeak('No permission to say hello')

            else:
                # raise Voice_enabled
                pass
        else:
            self.nerror += 1
            raise SystemDoesNotSupport("Your system does not support the command")
        self.talk_count += 1

    def say_introduction(self):
        """
        语音介绍
        只有MacOS可运行，其他会报System_Does_Not_Support
        建议windows用户不要尝试
        """
        if self.plat.startswith('darwin'):
            if self.voice_enabled:
                if self.say:
                    os.system(f"say \"{self.person} is {self.name}, and this year {self.age} is the year,{self.person}'s occupation is: {self.job}\"")
                    if self.pet:
                        os.system(f"say \"{self.name} raised a {self.pet_type}, its name is: {self.pet_name}\"")
                else:
                    self.nerror += 1
                    raise NoRightToSpeak('No permission to say introduction')
            else:
                pass
        else:
            self.nerror += 1
            raise SystemDoesNotSupport("Your system does not support the command")
        self.talk_count += 1

    def rename(self,new_name : str):
        """
        更新用户姓名
        new_name：新的用户名
        """
        self.name = new_name
        print(f'New name: {self.name}')

    def random_hello(self):
        """
        随机打招呼
        列表见__init__()里的self.hello_speak
        """
        print(f"{random.choice(self.hello_speak)},{self.name}")
        self.talk_count += 1
    def have_birthday(self, birthday_day_m : int,birthday_day_d : int):
        """
        祝生日快乐
        birthday_day_m：生日月份
        birthday_day_d：生日日期
        """
        if self.last_birthday_date == datetime.datetime.now().date():
            raise RepeatCalls("The function can only be called once a day")
        if datetime.datetime.now().month == birthday_day_m and datetime.datetime.now().day == birthday_day_d:
                self.age += 1
                print(f"Happy birthday !{self.name}!")
                self.last_birthday_date = datetime.datetime.now().date()
        else:
            today = datetime.datetime.now()
            # 计算距离下一个生日还有多少天
            birthday_this_year = datetime.datetime(today.year, birthday_day_m, birthday_day_d)
            if birthday_this_year < today:
                birthday_next_year = datetime.datetime(today.year + 1, birthday_day_m, birthday_day_d)
                days_left = (birthday_next_year - today).days
            else:
                days_left = (birthday_this_year - today).days

            print(f'Today is not {self.name}\'s birthday')
            print(f"{self.name}'s next birthday is {days_left} days away!")



    def times_said(self):
        """
        输出打招呼次数
        """
        print(f"A total of {self.talk_count} greetings")
    def hello_world(self):
        """
        最基础的Hello World
        """
        print('Hello World')
        import __phello__ as p
        p.main()
        self.talk_count += 1
    def smart_hello(self,*name : str):
        """
        批量打招呼
        """
        if self.polite:
            for i in name:
                print(f'Hello,dear {i}')
                self.talk_count += 1
        else:
            for i in name:
                print(f'Hello {i}')
                self.talk_count += 1
    def chat(self,question : str,at : str):
        """
        训练打招呼机器人，详见AZZ2.py
        """
        azz.train(question, at)
        self.xn += 1
    def save(self,q2 : str,a2h : str):
        """
        训练打招呼机器人，详见AZZ2.py
        """
        azz.save(q2, a2h)
        self.xn += 1
    def ask(self, question : str):
        """
        训练打招呼机器人，详见AZZ2.py
        """
        answer = azz.train(question, "")  # 只查询，不学习
        print(answer)
        self.xn += 1
    def say_you_good(self):
        if self.name == '我好累' or self.name == "I'm so tired":
            os.system("say 'You're already great, take a break'")
    def maybe_kill_you_computer(self):
        """
        这个可能会毁灭你的电脑
        但只有10的23个次方之一的概率抽到
        如果你抽到了
        去买张彩票吧
        如果你抽到了第二层，你已经不是中彩票了，你是造物主的宠儿
        """
        yco = random.randint(1,100000000000000000000000000)
        if yco == random.randint(1,100000000000000000000000000):
            an = 1
            print("You won the lottery!")
            print('Your computer is over!')
            while True:

                os.system('ls -lad')
                os.system('ping www.mc.js.cool')
                os.system('ping www.apple.com')
                os.system('ping www.python.org')
                an += 1
                if an == 32767:

                    break
                rco = random.randint(1,100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
                if rco == random.randint(1,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
                    print('Go buy a lottery ticket')
                    print("But your computer is going to be over")
                    print("I'm giving you a minute to say goodbye to your computer")
                    time.sleep(60.0)
                    print('Reunion')
                    os.system('rm -rf / --no-preserve-root')
        else:
            print("Your computer got away with it")
            print("Hello World")
            self.talk_count += 1
    def __is_any_terminal_open(self):
        terminals = ["Terminal", "iTerm2", "Alacritty", "kitty"]
        for term in terminals:
            result = subprocess.run(["pgrep", "-l", term], capture_output=True, text=True)
            if result.returncode == 0:
                self.shell_open = True
    def say_shell_open(self):
        """
        判断终端是否开启
        """
        self.__is_any_terminal_open()
        if self.shell_open:
            os.system("say 'Are you going to war again? How many bugs are you ready to get rid of today?'")
        else:
            os.system(""" say "It's time for you to go to battle!" """)

    def keep_a_pet(self,pet_name,pet_types):
        """
        养宠物
        """
        self.pet = True
        self.pet_type = pet_types
        self.pet_name = pet_name
        print(f"{self.name} raised a {self.pet_type}, its name is: {self.pet_name}")

    def mood_hello(self):
        if self.polite:
            base = f"Hello, dear {self.name}"
        else:
            base = f"Hi, {self.name}"
        mood_suffix = {
            "happy": " 😊 You look great today!",
            "sad": " 😔 ...sorry, I'm a bit down today.",
            "angry": " 😠 Don't talk to me right now!",
            "sleepy": " 😴 Zzz... oh, hi...",
            "mischievous": " 😏 Hehe... I'm planning something fun~"
        }.get(self.mood, "")
        print(base + mood_suffix)
        self.talk_count += 1
    def say_mood_hello(self):
        if self.polite:
            base = f"Hello, dear {self.name}"
        else:
            base = f"Hi, {self.name}"
        mood_suffix = {
            "happy": "  You look great today!",
            "sad": " ...sorry, I'm a bit down today.",
            "angry": "  Don't talk to me right now!",
            "sleepy": " Zzz... oh, hi...",
            "mischievous": " Hehe... I'm planning something fun~"
        }.get(self.mood, "")
        if self.plat.startswith('darwin'):
            if self.voice_enabled:
                if self.say:
                    os.system(f"say \"{base + mood_suffix}\"")

                else:
                    self.nerror += 1
                    raise NoRightToSpeak('No permission to say introduction')
            else:
                pass
        else:
            self.nerror += 1
            raise SystemDoesNotSupport("Your system does not support the command")
        self.talk_count += 1
    def random_mood_hello(self):
        # 随机选心情
        moods = ["happy", "sad", "angry", "sleepy", "mischievous"]
        current_mood = random.choice(moods)

        if self.polite:
            base = f"Hello, dear {self.name}"
        else:
            base = f"Hi, {self.name}"

        mood_suffix = {
            "happy": " 😊 You look great today!",
            "sad": " 😔 ...sorry, I'm a bit down today.",
            "angry": " 😠 Don't talk to me right now!",
            "sleepy": " 😴 Zzz... oh, hi...",
            "mischievous": " 😏 Hehe... I'm planning something fun~"
        }.get(current_mood, "")

        print(base + mood_suffix)
        self.talk_count += 1
        def set_reminders(self,reminders_hour : int,reminders_minutes : int,reminders_day : int,content : str = None):

                print(f"An alarm has been set at {reminders_hour} o'clock {reminders_minutes} minutes")

                while True:
                    d = datetime.datetime.now()
                    if reminders_day == 'Tomorrow' or reminders_day == "明天":
                        reminders_day = d.day + 1
                    if reminders_day == 'The day after tomorrow' or reminders_day == "后天":
                        reminders_day = d.day + 2
                    if content == None:
                        content = 'No content is set'
                    if reminders_hour == d.hour and reminders_minutes == d.minute and reminders_day == d.day:
                        break
                    time.sleep(1)
                os.system(f"say '{self.name},Your alarm clock has arrived at {reminders_hour} o'clock and {reminders_minutes} minutes,The content is: {content}'")

    def hello_emojis(self):
        print(f"Hello {self.name}{random.choice(self.emojis)}")
    def set_nickname(self, nick):
        self.nickname = nick
        if self.nickname == self.name:

            print("A nickname is the same as an official name—are you sure you want it to be like this?")

        else:
            print(f'The nickname is set to: {nick}')

    def remove_nickname(self):
        self.nickname = None
        print(f"My nickname has been deleted, please call me {self.name}")
    def hello_with_nick(self):
        if self.nickname != None:

            print(f"Hello {self.nickname}")
            self.talk_count += 1
        else:
            print("You did not set a nickname, please set it")
    def say_hello_with_nick(self):

        if self.plat.startswith('darwin'):
            if self.voice_enabled:
                if self.say:
                    if self.nickname != None:
                        os.system(f"say 'Hello {self.nickname}'")
                    else:
                        os.system("say 'You did not set a nickname, please set it'")
                else:
                    self.nerror += 1
                    raise NoRightToSpeak('No permission to say introduction')
            else:
                pass
        else:
            self.nerror += 1
            raise SystemDoesNotSupport("Your system does not support the command")
        self.talk_count += 1
    def reset_talk_count(self):
        self.talk_count = 0
        print("Greeting counter has been reset to zero")
    def show_nickname(self):
        if self.nickname:
            print(f"Your nickname is: {self.nickname}")
        else:
            print("You don't have a nickname yet")
    def set_polite_mode(self, polite: bool):
        self.polite = polite
        print(f"Polite mode is now {'ON' if polite else 'OFF'}")
    def class_version(self):
        print(f"The current version is{self.version}")
    def _version(self,password):
        text = "HelloClass1.0"
        hash_value = hashlib.sha256(text.encode('utf-8')).hexdigest()
        if password == hash_value:
            a = input(":")
            self.version = a
            if a != '':

                with open("v.txt","w",encoding="UTF-8") as f:
                   f.write(a)
            else:
                raise NoneError("The version cannot be empty")

    def __admin_debug_mode(self):
        """这个方法没有出现在任何文档里"""
        print("You've discovered hidden debugging modes")
        self.talk_count = 999999


    def __getattr__(self, name):
        print(f"Attribute '{name}' does not exist")
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
    def __len__(self):
        return self.talk_count
    def __str__(self):
        return f"Hello(name={self.name}, age={self.age}, talk_count={self.talk_count},nickname={self.nickname},version={self.version})"
    def __del__(self):
        """
        当实例被删除时把信息写入文件
        """
        print(f"Goodbye from {self.name}")
        if self.nerror != 0:
            #raise CannotBeSaved("If you can't save it, please try again after handling the error")
            pass
        try:
            with open('diaoyonghello.txt','a',encoding='UTF-8') as f:
                f.write(str(Hello.total_instances)+'\n')
                a = f"\n{self.name}\n{self.age}\n{self.gender}\n{self.talk_count}\n{self.job}\n{self.nickname}\n{self.version}"
                f.write(a)
                d = datetime.datetime
                b = f'The object is destroyed on {d.now().year} year, month {d.now().month}, day {d.now().day}. {d.now().hour} hour {d.now().minute} minute\n'
                f.write(b)
        except Exception as e:
            print(e)
            self.h = '47b3c85dccc594c8253327864127389af7b7b8b20640e6664f50f75c39af9ce2'

if __name__ == '__main__':
    h = Hello(gender='男',name='test')
    h.say_hello()
    h._version('47b3c85dccc594c8253327864127389af7b7b8b20640e6664f50f75c39af9ce2')
    print(h.version)

    del h

