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
    
    




if __name__ == '__main__':
    main()