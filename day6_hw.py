import turtle as t
t.shape("turtle") #거북이 모형의 그림을 거북이로 지정한다
t.bgcolor("black") #배경색을 검정색으로 지정한다
t.color("red") #거북이의 색을 빨간색으로 지정한다
t.speed(0)#거북이의 움직임을 최대 속도로 한다

for x in range(100): #for 반복 블록을 100번 실행한다
    t.circle(x) #반지름이 x인 원을 그린다
    t.left(45) #왼쪽으로 45도 회전시킨다
    if x % 3 ==0: #번갈아 가면서 선 색을 바꾼다
        t.color("red") #빨간색으로
    if x % 3 == 1:
        t.color("yellow") #노란색으로
    if x % 3 == 2:
        t.color("orange") #주황색으로
    t.left(45) #거북이를 왼쪽으로 45도 회전시킨다
t.color("green") #거북이의 색을 초록색으로 지정한다
t.left(270) #거북이를 왼쪽으로 270도 회전시킨다
t.forward(300) #앞으로 300만큼 간다
t.left(140) #거북이를 왼쪽으로 140도 회전시킨다
for x in range(50): #for 반복 블록을 50번 실행한다
    t.circle(x) #반지름이 x인 원을 그린다
    t.color("green") #초록색
t.right(100) #거북이를 오른쪽으로 100도 회전시킨다
for x in range(50): #for 반복 블록을 50번 실행한다
    t.circle(x) #반지름이 x인 원을 그린다
    t.color("green") #초록색
