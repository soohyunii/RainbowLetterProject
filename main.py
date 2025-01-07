import sys
print(sys.executable)
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def main():
    # 사용자가 설정한 경로로 찾아가서 파일 찾음
    user_path = "C:/Users/김수현/Desktop/rainbow.txt"
    f = open(user_path, encoding='UTF-8')
    data = f.read()
    
    #메모장(txt)글씨색을 변경하는 기능은 없음...png저장으로 대체
    # with open(user_path, 'w', encoding='UTF-8') as file:
    #     file.truncate(0)
    #     file.write(data_rainbow_png)
    # f.close()
    
    # 폰트 지정
    font = ImageFont.truetype("./font/NanumGothic.ttf",25)
    # 배경이 투명인 영역의 경계 상자값(왼쪽, 위쪽, 오른쪽, 아래쪽)
    fontbox = font.getbbox(data)
    fontbox_max = max(fontbox)
    fontbox_width, fontbox_height = fontbox_max, fontbox_max
    
    # 이미지 사이즈 지정
    text_width = fontbox_width * 2
    text_height = fontbox_height * 2
    
    # 이미지 객체 생성
    canvas = Image.new('RGB', (text_width, text_height), "white")
    
    # 캔버스에 글씨 입력하기
    draw = ImageDraw.Draw(canvas)
    draw.text((text_width/3, text_height/3), data, 'red', font)
    
    #png로 저장 및 출력해서 보기
    canvas.save('rainbow.png', "PNG")
    canvas.show()
    
    




if __name__ == '__main__':
    main()