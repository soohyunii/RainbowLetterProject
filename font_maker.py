import sys
from PIL import Image, ImageDraw, ImageFont

class FontMaker():
    
    def __init__(self):
        pass
    
    def makefont(self):
        # 사용자가 설정한 경로로 찾아가서 파일 찾음
        user_path = "C:/Users/김수현/Desktop/rainbow.txt"
        f = open(user_path, encoding='UTF-8')
        #data = f.read()
        data = f.readlines()

        # 폰트 지정
        font = ImageFont.truetype("./font/NanumGothic.ttf",25)
        # 배경이 투명인 영역의 경계 상자값(왼쪽, 위쪽, 오른쪽, 아래쪽)
        fontbox = font.getbbox(''.join(data))
        fontbox_max = max(fontbox)
        fontbox_width, fontbox_height = fontbox_max, fontbox_max
        # 폰트 색깔(rainbow) 정의
        rainbow_font = ['red', 'orange', 'rgb(255,205,0)', 'green', 'blue', 'rgb(0,0,139)', 'rgb(75,0,130)']

        # 이미지 사이즈 지정
        text_width = fontbox_width * 2
        text_height = fontbox_height * 2

        # 이미지 객체 생성
        canvas = Image.new('RGB', (text_width, text_height), "white")

        # 캔버스에 글씨 입력하기 - 한글자씩
        draw = ImageDraw.Draw(canvas)
        k_idx = 0
        for idx, i in enumerate(data):
            for k,v in enumerate(i):
                k_idx = k - len(rainbow_font)*(k//len(rainbow_font))
                draw.text((text_width/9+50*k, text_height/9+50*idx), v, rainbow_font[k_idx], font)
                k_idx += 1
            
        #png로 저장 및 출력해서 보기
        canvas.save('rainbow.png', "PNG")
        canvas.show()
    