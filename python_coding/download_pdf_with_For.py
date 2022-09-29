#불량영어 자료 다운로드 url의 이미지 파일 넘버만 바꿔서 다운로드
import wget  
for i in range(4,36):
    i +=1
    url =  (f"https://cdn.podbbang.com/data1/yoon/EP{i}.pdf")
    wget.download(url)
    #범위를 주고 없으면 에러 처리 할 수 있으면 더 좋겠음.
