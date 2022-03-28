# APTP 2022 - **{팀명}**
구성원: 아스터 | 리스크 | 홍길동

## 1. 주제
{주제 작성}

## 2. 동기
{동기 작성}

## 3. 프로그램 사용 대상
{사용 대상 작성}

## 4. 목적
{목적 }

## 5. 주요기능
1. 숫자가 적혀있는 상자들이 상하좌우로 움직일 수 있다.
2. 상자끼리 만날 때 같은 숫자로 이루어진 상자이면 두 상자가 하나로 합쳐지고 숫자가 두 배가 된다. 
3. 다른 숫자의 상자이면 색이 다르다. 
4. 상자가 벽을 만나면 움직이지 않는다. 
5. 다른 숫자의 상자가 만나면 벽처럼 작용해 서로 합쳐지지 않고 막는다.
6. 16칸이 상자로 다 차고 더 합칠 수 있는 상자가 없을 때 게임이 종료된다.
7. 칸의 개수를 4x4~8x8개까지 설정할 수 있다.
8. 점수를 저장하고 최고 점수를 표시할 수 있다.
9. 서버를 통해 최고 점수를 비교해 랭크를 만들 수 있다.

## 6. 프로젝트 핵심
1. 각 상자를 객체로 구현하는 것이 중요하다. 이를 통해 상자의 숫자, 움직임 등 겹치는 것이 많은 기능이 class를 통해 구현이 가능할 것으로 보인다
2. 서버를 통해 점수를 저장하고 랭크를 표시하는 기능이 필요하다. 또한 사용자에 따라 최고점수가 갱신되면 서버에서도 갱신된 점수를 사용자 점수에 넣어야 하기 때문에 이를 바꾸는 것도 필요할 것으로 보인다.
3. GUI를 구현할 때 판의 크기에 따라 상자의 크기 등이 달라져야 하므로 이 부분 또한 생각이 필요하다고 생각한다.

## 7. 구현에 필요한 라이브러리나 기술
{pygame, sys, socket, time, random, threading}

## 8. **분업 계획**
김덕용: GUI 구현, board 구현
이영채: 상자 Class 구현
김예건: 서버 및 클라이언트 구현

## 9. 기타


1. 서버에 점수를 올리고 싶다면 server.py를 먼저 실행시킨 후 board.py를 실행시키세요. 서버를 사용하기 전에 client.py의 IP와 server.py의 IP를 같게 수정하세요. 기본값은 127.0.0.1입니다. IP는 HOST변수에 들어있습니다. ip_check.py를 통해 IP를 알아낼 수 있습니다.
2. 만약 오프라인으로 즐기고 싶다면 board.py를 실행시키세요

<hr>

#### readme 작성관련 참고하기 [바로가기](https://heropy.blog/2017/09/30/markdown/)

#### 예시 계획서 [[예시 1]](https://docs.google.com/document/d/1hcuGhTtmiTUxuBtr3O6ffrSMahKNhEj33woE02V-84U/edit?usp=sharing) | [[예시 2]](https://docs.google.com/document/d/1FmxTZvmrroOW4uZ34Xfyyk9ejrQNx6gtsB6k7zOvHYE/edit?usp=sharing) | [[예시 3]](https://github.com/goldmango328/2018-OOP-Python-Light) | [[예시4]](https://github.com/ssy05468/2018-OOP-Python-lightbulb) | [[모두보기]](https://github.com/kadragon/oop_project_ex/network/members)



