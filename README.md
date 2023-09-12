# 빅데이터 기반 도서추천 및 독서모임 관리 서비스 개발
- 수행기간 : 2023.06.19 ~ 2023.07.31
- 구성원 : 4명(데이터 수집, 전처리, 모델링 / 웹개발)
  
## 프로젝트 배경
실제 운영되는 독서모임 규모가 확대되면서 모임 운영에 있어서 도서 선정의 어려움 해결, 여러 도서 비교 기능과 모임 운영 시스템의 필요성 대두

## 주요 업무
- 도서의 세분화된 새로운 카테고리 생성을 위한 도서 정보 데이터 활용 토픽모델링
- 컨텐츠 기반 추천시스템을 사용한 도서 정보 활용 회원 맞춤 도서 추천 시스템 구현 
- 감성 분류기를 사용하여 리뷰 데이터 분석을 통한 추천된 도서에 대한 알라딘 독자의 평가를 예측  
- 독서모임 회원들이 로그인, 도서 추천, 도서 상세 정보 등의 기능을 사용할 수 있도록 웹 서비스 구현

## 데이터 파이프라인(ETL 구조)
![데이터 파이프라인](chack-it-out2/데이터파이프라인.png)

![데이터 처리 흐름도]([chack-it-out2/데이터처리흐름도.png](https://github.com/Final-Project-Multi-DS24/chack-it-out-2/blob/develop/%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%E1%84%8E%E1%85%A5%E1%84%85%E1%85%B5%E1%84%92%E1%85%B3%E1%84%85%E1%85%B3%E1%86%B7%E1%84%83%E1%85%A9.png?raw=true)https://github.com/Final-Project-Multi-DS24/chack-it-out-2/blob/develop/%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%E1%84%8E%E1%85%A5%E1%84%85%E1%85%B5%E1%84%92%E1%85%B3%E1%84%85%E1%85%B3%E1%86%B7%E1%84%83%E1%85%A9.png?raw=true)

## ERD 
![ERD](./ERD.png)

## 데이터 출처
- 도서 정보 데이터 : 알라딘 OpenAPI
- 도서 리뷰 데이터 : 알라딘 web
> 저작권 문제로 해당 데이터는 업로드하지 않음

## 개발 환경
- Python
- Django

## 파일 설명

### 추천
web > data > recommend.py
```python
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# 추천 함수
def getRecommend(df,tfidf_matrix,isbn_list):
	
  # 최근에 읽은도서 3권만 추천에 반영
  isbn_list=isbn_list[-1:-4:-1]
  indices = pd.Series(df.index, index=df['isbn'])
  ...
  # 점수를 기준으로 내림차순 정렬
  sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
  ...
  # 가장 유사한 책 8권의 인덱스
  book_indices = [i[0] for i in sim_scores]
  
  return list(df.iloc[book_indices]['isbn'])
```
