import random
a,b,c=map(str, input("첫번째, 두번째에는 이름, 세번째에는 종목을 공백으로 입력하세요.").split())
conln=["성공","실패"]
a1=random.choice(conln)
if a1=="성공":
  b1="실패"
else:
  b1="성공"
print(c+" 에서, "+a+"님은 "+a1+"하셨고 "+b+"님은 "+b1+"하셨습니다!")