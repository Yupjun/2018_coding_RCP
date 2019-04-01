# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 12:42:24 2018
@author: 김준엽
## This py file is dummy for selecting codes
## do not run this file
## 함수 쓰는 법
## def 함수를 복사해서
## player 나 player1 클래스에 붙여넣기합니다.
1. 가위 =x 바위 =y 보 = z 확률로 돌리는 함수
    def show_me_your_hand(self,r2):
        setting = ['gawi','bawi']
        chosen = setting[np.random.choice(3,1,p=[0.2,0.5,0.3])[0]]
        self.game_record.append(chosen)
        return chosen
2.  상대방의 전 시행과 똑같이 내는 함수
    def show_me_your_hand(self,r2):
        self.game_record.append(r2)
        return r2
        
        
3.  난 그냥 랜덤으로 낼래요
    def show_me_your_hand(self,r2):
        chosen = choice(['gawi','bawi'])
        self.game_record.append(chosen)
        return chosen
4.  난 그냥 주먹,가위 보중에 하나만 낼래요
 [gawi bawi bo] 중에서 하나를 지워서 복붙하시면 됩니다.
    def show_me_your_hand(self,r2):
        chosen = ['gawi','bawi','bo']
        self.game_record.append(chosen)
        return chosen
    
5.  전판에 상대가 낸걸 보고, 그것에 이기는 걸 낼래요
    def show_me_your_hand(self,r2):
        if r2 == 'gawi':
            chosen = 'bawi'
            self.game_record.append(chosen)
            return chosen
        elif r2 == 'bawi':
            chosen = 'bo'
            self.game_record.append(chosen)
            return chosen
        else:
            chosen = 'gawi'
            self.game_record.append(chosen)
            return chosen
6.  전판에 상대가 낸걸 보고, 그것에 지는걸 낼래요
    def show_me_your_hand(self,r2):
        if r2 == 'gawi':
            chosen = 'bo'
            self.game_record.append(chosen)
            return chosen
        elif r2 == 'bawi':
            chosen = 'gawi'
            self.game_record.append(chosen)
            return chosen
        else:
            chosen = 'bawi'
            self.game_record.append(chosen)
            return chosen
7. 만약 내가 전판에 이겼다면, 그대로 내고
   내가 비기거나 졌다면, 상대방이 낸거에서 이긴 걸로 낼래요
    def show_me_your_hand(self,r2):
        if self.result_record == []:
            chosen = choice(['gawi','bawi','bo'])
            return chosen
        else:
            if self.result_record[-1]==3:
                chosen = self.game_record[-1]
                self.game_record.append(chosen)
                return chosen
            else:
                if r2 == 'gawi':
                    chosen = 'bawi'
                    self.game_record.append(chosen)
                    return chosen
                elif r2 == 'bawi':
                    chosen = 'bo'
                    self.game_record.append(chosen)
                    return chosen
                else:
                    chosen = 'gawi'
                    self.game_record.append(chosen)
                    return chosen
8.  기본 AI
    def show_me_your_hand(self,r2):
        chosen = choice(['gawi','bawi','bo'])
        self.game_record.append(chosen)
        return chosen
    
9.  향상된 AI?
    def show_me_your_hand(self,r2):
        chosen = secrets.choice(['gawi','bawi','bo'])
        self.game_record.append(chosen)
        return chosen
"""





from random import choice
import random
import matplotlib.pyplot as plt
import time
from tqdm import tqdm
import numpy as np
from numpy import array
from scipy import stats, polyval
from pylab import plot, title, show, legend
#matplotlib 한글패치
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

class Red:
    def __init__(self,name):
        seeds = choice(['gawi','bawi','bo'])
        self.game_record = [seeds] # 내가 냈던 기록
        self.result_record = [] #나의 승패 기록
        self.name = name
        
    # 가위바위보 알고리즘
    def show_me_your_hand(self,past,record,output):
        chosen = choice(['gawi','bawi','bo'])
        self.game_record.append(chosen)
        return chosen

    def get_my_record(self):
        return self.game_record

    def get_result_record(self):
        return self.result_record
    
    def result_adder(self,result):
        self.result_record.append(result)
        
    # 팀 이름
    
    def name(self):
        return self.name
    
    # 총점 리턴
    def score(self):        
        return sum(self.result_record)
    
class Blue:
    def __init__(self,name):
        seeds = choice(['gawi','bawi','bo'])
        self.game_record = [seeds] # 내가 냈던 기록
        self.result_record = [] #나의 승패 기록
        self.name = name
        
    # 가위바위보 알고리즘
    def show_me_your_hand(self,past,record,output):
        chosen = choice(['gawi','bawi','bo'])
        self.game_record.append(chosen)
        return chosen

    def get_my_record(self):
        return self.game_record

    def get_result_record(self):
        return self.result_record
    
    def result_adder(self,result):
        self.result_record.append(result)
        
    # 팀 이름
    
    def name(self):
        return self.name
    
    # 총점 리턴
    def score(self):        
        return sum(self.result_record)
        
        
        
########### 팀 세팅
        
hello = Red("테스트계정")
world = Blue("랜덤모듈")


#점수 넣는 곳      
def calculator(p1,p2,result):
    if result==1:
        p1.result_adder(3)
        p2.result_adder(0)
    elif result==-1:
        p1.result_adder(0)
        p2.result_adder(3)
    else:
        p1.result_adder(1)
        p2.result_adder(1)
        


#연산하는 곳
#tdqm이 없는 경우 range(10)으로 바꿔주시면 됩니다.
for i in range(10000):
    if random.choice([True, False]):
        h1 = hello.show_me_your_hand(world.game_record[i],hello.get_my_record,hello.get_result_record)
        h2 = world.show_me_your_hand(hello.game_record[i],world.get_my_record,world.get_result_record)
    else:
        h2 = world.show_me_your_hand(hello.game_record[i],world.get_my_record,world.get_result_record)
        h1 = hello.show_me_your_hand(world.game_record[i],hello.get_my_record,hello.get_result_record)
    if h1==h2:
        r =0
    elif (h1 == 'gawi' and h2 == 'bo') or (h1 == 'bawi' and h2 == 'gawi') or (h1 == 'bo' and h2 == 'bawi'):
        r = 1
    else:
        r = -1

    calculator(hello,world,r)
    


    
def game_rate_analysis(a):
    options = ['승','패','무승부']
    lr=[a.get_result_record().count(3),a.get_result_record().count(1),a.get_result_record().count(0)]
    y_pos = np.arange(len(options))
    plt.figure(figsize=(10,5))
    plt.bar(y_pos,lr, align='center', alpha = 0.5)
    plt.xticks(y_pos,options)
    plt.ylabel('count')
    
    plt.title('%s 팀이 이기거나 지거나 비긴 확률'%a.name)
    plt.show()
    print("%s 팀은 총 %d 점입니다"%(a.name,a.score()))
    
def result_show(a,b):
    print("%s팀은 %d승,%d무,%d패로 총 %d점입니다."%(a.name,a.result_record.count(3),a.result_record.count(1),a.result_record.count(0),a.score()))
    print("%s팀은 가위 : %s, 바위: %s, 보: %s 번 냈습니다."%(a.name,a.game_record.count('gawi'),a.game_record.count('bawi'),a.game_record.count('bo')))
    print("%s팀은 %d승,%d무,%d패로 총 %d점입니다."%(b.name,b.result_record.count(3),b.result_record.count(1),b.result_record.count(0),b.score()))
    print("%s팀은 가위 : %s, 바위: %s, 보: %s 번 냈습니다."%(b.name,b.game_record.count('gawi'),b.game_record.count('bawi'),b.game_record.count('bo')))
    if a.score() == b.score():
        print("둘다 %d점으로 동점입니다 승수우선제로 넘어갑니다 체크해주세요")
    elif a.score() > b.score():
        print("%s팀이 %s팀을 %d점 차이로 이겼습니다" %(a.name,b.name,a.score()-b.score()))
    elif a.score() < b.score():
        print("%s팀이 %s팀을 %d점 차이로 이겼습니다" %(b.name,a.name,b.score()-a.score()))
    else:
        print("오류가 발생했습니다")
        
# a = class b = start_num

def sum_y(a,start_num):
    p = a.result_record
    k = 0 
    for i in range(start_num,start_num+100):
        k+=p[i]
    return [k]

def np_list(a):
    tmp = []
    for i in range(0,10000,100):
        temp = sum_y(a,i)
        tmp+= temp
    y_axis = array(tmp)
    return y_axis

def graph_show(a):
    t1 = np.arange(0,10000,100)
    t2 = np_list(a)
    plt.figure(figsize=(10,5))
    plt.plot(t1,t2)
    plt.title('%s 1000회당 합계점수 그래프'%a.name)
    plt.show()

def sum1_y(a,start_num):
    p = a.result_record
    k = 0 
    for i in range(0,start_num+100):
        k+=p[i]
    return [k]

def np1_list(a):
    tmp = []
    for i in range(0,100000,100):
        temp = sum1_y(a,i)
        tmp+= temp
    y_axis = array(tmp)
    return y_axis





game_rate_analysis(hello)
game_rate_analysis(world)
result_show(hello,world)
graph_show(hello)
graph_show(world)