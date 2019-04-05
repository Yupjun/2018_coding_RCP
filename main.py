### 모듈 선언부

from random import choice
import random
import matplotlib.pyplot as plt
import numpy as np
from numpy import array
from scipy import stats, polyval
from pylab import plot, title, show, legend
# matplotlib 한글패치
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

### 변수 선언부

red_game_record = []  # red팀이 낸 손의 결과
red_result_record = []  # red 팀 결과 [3 , 0 , -1] 형태로 나타남 
red_name = ""  # 이름

blue_game_record = []  # blue팀이 낸 손의 목록
blue_result_record = []  # blue팀의 게임 결과 [ 3,0,-1] 형태로 나타남
blue_name = ""


#### 함수 선언 부

def game_rate_analysis():
    print("RED팀은 총 %d 점입니다" % (sum(red_result_record)))
    print("BLUE팀은 총 %d 점입니다" % (sum(blue_result_record)))
    options = ['승', '패', '무승부']
    x_pos = [red_result_record.count(3), red_result_record.count(1), red_result_record.count(0)]
    y_pos = np.arange(len(options))
    x_pos1 = [blue_result_record.count(3), blue_result_record.count(1), blue_result_record.count(0)]
    y_pos1 = np.arange(len(options))
    plt.figure(figsize=(10, 5))
    plt.bar(y_pos, x_pos, align='center', alpha=0.5)
    #     plt.bar(y_pos,x_pos1, 'b',align='center', alpha = 0.5)
    plt.xticks(y_pos, options)
    plt.ylabel('count')

    plt.title('RED 팀이 이기거나 지거나 비긴 확률')
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.bar(y_pos1, x_pos1, align='center', alpha=0.5)
    #     plt.bar(y_pos,x_pos1, 'b',align='center', alpha = 0.5)
    plt.xticks(y_pos1, options)
    plt.ylabel('count')

    plt.title('BLUE 팀이 이기거나 지거나 비긴 확률')
    plt.show()

    print("%s팀은 %d승,%d무,%d패로 총 %d점입니다." % (
    "RED", red_result_record.count(3), red_result_record.count(1), red_result_record.count(0), sum(red_result_record)))
    print("%s팀은 가위 : %s, 바위: %s, 보: %s 번 냈습니다." % (
    "RED", red_game_record.count('gawi'), red_game_record.count('bawi'), red_game_record.count('bo')))
    print("%s팀은 %d승,%d무,%d패로 총 %d점입니다." % (
    "BLUE", blue_result_record.count(3), blue_result_record.count(1), blue_result_record.count(0),
    sum(blue_result_record)))
    print("%s팀은 가위 : %s, 바위: %s, 보: %s 번 냈습니다." % (
    "BLUE", blue_game_record.count('gawi'), blue_game_record.count('bawi'), blue_game_record.count('bo')))
    blue_score = sum(blue_result_record)
    red_score = sum(red_result_record)
    if blue_score == red_score:
        print("둘다 %d점으로 동점입니다 승수우선제로 넘어갑니다 체크해주세요")
    elif blue_score > red_score:
        print("%s팀이 %s팀을 %d점 차이로 이겼습니다" % ("BLUE", "RED", blue_score - red_score))
    else:
        print("%s팀이 %s팀을 %d점 차이로 이겼습니다" % ("RED", "BLUE", red_score - blue_score))


# red 팀

# past = 상대가 낸 손의 목록
# record = 내가 낸 손의 목록
# output = 내가 이기고 진 기록

# 아래 함수 둘 중 하나를 골라서 자신의 것에 맞게 고치세요
# 두 함수 모두 랜덤으로 주먹 가위 보 중 하나를 선택하는 구조입니다.

def show_me_your_hand_red(past, record, output):
    chosen = choice(['gawi', 'bawi', 'bo'])
    output = chosen
    return output


# blue 팀
# 이 부분을 수정하세요
def show_me_your_hand_blue(past, record, output):
    chosen = ['gawi', 'bawi', 'bo']
    return output


# 연산하는 곳
for i in range(10000):
    BLUE = ""
    RED = ""
    r = 0
    if random.choice([True, False]):
        BLUE = show_me_your_hand_blue(red_game_record, blue_game_record, blue_result_record)
        RED = show_me_your_hand_red(blue_game_record, red_game_record, red_result_record)
    else:
        RED = show_me_your_hand_red(blue_game_record, red_game_record, red_result_record)
        BLUE = show_me_your_hand_blue(red_game_record, blue_game_record, blue_result_record)

    red_game_record.append(RED)
    blue_game_record.append(BLUE)

    if BLUE == RED:
        red_result_record.append(1)
        blue_result_record.append(1)

    # BLUE가 이겼을 때
    elif (BLUE == 'gawi' and RED == 'bo') or (BLUE == 'bawi' and RED == 'gawi') or (BLUE == 'bo' and RED == 'bawi'):
        red_result_record.append(0)
        blue_result_record.append(3)
    # RED가 이겼을 때
    else:
        red_result_record.append(3)
        blue_result_record.append(0)

game_rate_analysis()