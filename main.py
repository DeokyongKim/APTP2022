'''
참고사항
1. 주어진 변수 외에 본인이 사용하거나 main 동작 중에 입력받으면 좋겠다 하는 함수가 있으면 변수를 추가하셔도 좋습니다!
2. 기본적으로 세팅한 변수는 각 클래스의 __init__에 명시되어 있으니 참고하시면 되겠습니다!
3. 이 .py 파일의 main 부분은 나중에 추가해서 다시 업로드 하겠습니담.. 일단 함수 만들어주세용...
4. 여러분들 깃에 commit 하기 전에 꼭 카톡방에 다 했다 올려주시고 대기해주세용...! (제일 중요중요)
    >> 최악의 경우는 충돌 생겨서 처음부터 다시 할 수도...
'''

import random
import numpy
import pygame

# 구분선 출력 함수
def printLine():
    for i in range(50):
        print("-", end='')
    print("\n", end='')

# 게임 시작 전 게정 생성 및 로그인 하는 객체
class Login:
    def __init__(self):
        # 계정이 서버에 있는지 체크하기 위해 입력된 값은 저장하는 곳
        self.id_temp = ""
        self.passWord_temp = ""

        # 계정 체크 후 추후 계정 정보 출력할 때 사용할 계정 데이터 저장 딕셔너리
        self.idSave = {'id': "", 'passWord': "", 'turn': -1}  # turn은 플레이어의 순서 지정을 위해 만든 index, 초깃값은 -1

    # 데이터 리스트에 계정이 있는지 확인하는 함수
    def accountCheck(self, ID, PassWord):
        if '''계정이 서버에 있는지 체크하는 조건''':
            return True
        else:
            return False

    # 계정 생성하는 함수
    def getId(self):
        self.idSave['id'] = input("아이디 생성: ")
        self.idSave['passWord'] = input("비밀번호 생성: ")
        # 텍스트 파일에 입력된 데이터 저장하는 부분 추가 예정

#구이연's part
# 참가자의 순서를 정하는 함수
# 함수 input하는 매개변수는 원하는 대로 추가하셔도 됩니다.
def indexSet():
    # delete "pass" and write the code here
    pass


class Block:
    # 1~4번째 순서의 사람들이 가질 블럭들 저장하는 변수들 선언, 파이썬은 포인터가 없어서 딕셔너리로 구현해주시면 될 것 같습니다.
    # Ex, Block.blockLine_1[num] == "1-233479", Block.blockLine_3[color] == "검검흰검흰흰", Block.blockLine_2[open] = "TFFTTTFF"
    # index 설명 >> num: 숫자 & 조커 값을 문자열로 저장(순차적으로), color: 블럭이 흰색인지 검은색인지 저장하는 문자열, open: 블럭이 open 됐는지 여부를 저장하는 문자열
    def __init__(self):
        self.blockLine_0 = {"num": "", "color": "", "open": ""}
        self.blockLine_1 = {"num": "", "color": "", "open": ""}
        self.blockLine_2 = {"num": "", "color": "", "open": ""}
        self.blockLine_3 = {"num": "", "color": "", "open": ""}
        self.blockLeft = {"num": "", "color": ""}  # 분배하고 나중에 하나씩 가져갈 블럭들 넣어놓는 곳

    # 이정현's part
    # 난수 발생시켜서 네명의 사용자에게 블럭들 주는 함수
    def giveBlock(self):
        # delete "pass" and write your code here
        pass

    #박강우's part
    # 블럭들을 게임 시작전 배분하고 나서, 블럭을 정렬하는 함수 (처음 정렬할 때에는 조커블럭의 위치는 사용자가 정할 수 있도록 할 것!)
    def alignBlock(self):
        # delete "pass" and write your code here
        pass

    # 박강우's part
    # 현재 오픈된 블럭을 포함하는 모든 플레이어의 블럭 열을 상대방에게 보여주는 함수
    def showBlock(self):
        # delete "pass" and write your code here
        pass

    #김현준's part
    # 새로운 블럭을 본인의 블럭 열로 가져오는 함수
    def addNew(self):
        # delete "pass" and write your code here
        pass


class Game:
    # 본인이 함수를 작성하시고 필요한 변수는 여기에 초기화해서 선언하기!!
    # 단, 블럭 열이나 사용자의 정보 또는 함수는 Block 클래스와 Login 클래스의 내용들 사용하기! 추가하지 말고
    def __init__(self):
        pass

    #이정현's part
    # 자신의 차례인 사람이 누구의 블럭을 지목할지, 그 플레이어를 고르는 함수
    def pickPlayer(self):
        # delete "pass" and write your code here
        pass

    #구이연's part
    # 지목한 플레이어의 블럭이 내가 생각한 블럭이 맞나 확인하는 함수
    def checkBlock(self):
        # delete "pass" and write your code here
        pass

    #김다운's part
    # 자신의 턴을 마칠지, 아니면 주가적으로 블럭을 맞추러 갈지 고르는 함수
    #return 값은 true or false
    def checkBlockAgain(self):
        # delete "pass" and write your code here
        pass

    #김다운's part
    # 승패자가 결정 되었는지 확인하는 함수
    # return 값은 true or false
    def isWinner(self):
        # delete "pass" and write your code here
        pass

    #김현준's part
    # 재시작 여부 확인하는 함수
    # return 값은 true or false
    def restart(self):
        # delete "pass" and write your code here
        pass


# main

# 계정 생성 또는 로그인을 하는 부분
printLine()
while True:
    print("계정을 생성하거나, 로그인을 진행 해주세요.")
    choose = input("1. 계정 생성, 2. 로그인: ")
    if choose == '1':
        Login.getId()
        break
    elif choose == '2':
        if Login.accountCheck():
            break
    else:
        print("올바른 입력을 다시 주세요.")
        continue
printLine()
print("\n게임을 시작합니다!")
print("블럭은 배분하고 있습니다...")
Block.giveBlock()
Block.alignBlock()
Block.showBlock()
printLine()
while (Game.isWinner() != True):
    for i in range(0, 3):


