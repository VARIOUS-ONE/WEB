### Input : 리뷰 내용, 사용자 ID를 입력받음
### Output : 리뷰내용 검증을 통해 정상 리뷰 판정이 되면 skip, 가짜리뷰면 리뷰내용과 id를 output으로 보냄
### 추가 설명 : 기존에 데이터를 array로 저장한 파일을 통하여 sqlite DB파일을 생성, 그 후 db파일 내 데이터를 통해 가짜리뷰 예측 진행함.
### 추가적으로 db파일 내 black_list 테이블에 가짜 리뷰로 식별된 유저의 유사도 점수, ID, 리뷰 내용을 저장함.

import numpy as np
from sentence_transformers import SentenceTransformer
import sqlite3
import io
import os
from base.models import Blacklist
import datetime
# print(os.getcwd())
import pytz
import time
sentencebert_model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')

def cosine(a,b):
  return np.dot(a,b) / np.sqrt(np.dot(a, a) * np.dot(b, b))

def adapt_array(arr):
    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    return sqlite3.Binary(out.read())   

def convert_array(text):
    out = io.BytesIO(text)
    out.seek(0)
    return np.load(out)

class fake_review():
    def predict(id, text):
        #train_vector = np.load("C:/Users/ssw97/models/train_2020.npy") # 저장된 numpy 파일 불러옴. 이거는 sqlite로 불러오는 걸로 바꿔야 함.
        
        sqlite3.register_adapter(np.ndarray, adapt_array)
        sqlite3.register_converter("array", convert_array) # 이거 두 줄이 중요함. 이거없으면 배열 불러올때 오류걸려서 개같음
        # train = pd.read_csv('./train_spam.csv', encoding='cp949')
        # review = pd.read_csv('./dummy.csv')
        # ebd = sentencebert_model.encode(train['리뷰'].astype('str'))
        # review_ebd = sentencebert_model.encode(review['comment'].astype('str'))
        # ebd = np.append(ebd, review_ebd, axis = 0)

        con = sqlite3.connect("./base/views/sangwon/train.sqlite3", detect_types=sqlite3.PARSE_DECLTYPES)
        #con = sqlite3.connect("./train.sqlite3", detect_types=sqlite3.PARSE_DECLTYPES)
        cur = con.cursor()

        
        cur.execute("create table if not exists train_vector (arr array)") ### array를 저장할 테이블 생성
        # cur.execute("insert into train_vector (arr) values (?)", (ebd,))
        # cur.execute("drop table black_list")
        cur.execute("create table if not exists black_list (score text, userid text, review text, datetime text, product_id text)") # blacklist 저장할 테이블 생성
        
        # cur.execute("insert into train_vector (arr) values (?)", (train_vector))

        cur.execute("select arr from train_vector")
        #data = np.frombuffer(cur.fetchone()[0], dtype = 'float64').reshape(shape)
        data = cur.fetchone()[0]
        print(data.shape)


        review = text # text 입력
        ID = id # id 입력
        product_id = 2

        review_ebd = sentencebert_model.encode(review)

        score = 0
        for i in range(len(data)):
            if score <= cosine(review_ebd, data[i,:]):
                score = cosine(review_ebd, data[i,:])
        if score >= 0.95 and len(review) >= 15:
            print("해당 리뷰는 가짜리뷰 일 수 있습니다!")
            cur.execute('insert into black_list VALUES(?,?,?,?,?);', (str(score), ID, review, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str(product_id)))

            # blacklist 객체 생성

            #newdb
            Blacklist.objects.create(score = score*100, review = review,datetime=datetime.datetime.now(pytz.timezone('Asia/Seoul')),product_id = str(product_id))
            time.sleep(2)


            #cur.execute("select * from black_list")
            #data = cur.fetchone()
            #print(data)
                # db blacklist 테이블에 유사도 점수, 유저ID, 리뷰 내용 추가
        else:
            print(score)
            print("해당 리뷰는 정상 리뷰로 분류됩니다!")
        data = np.append(data, review_ebd.reshape(1,-1), axis=0)
        cur.execute('DELETE FROM train_vector')
        cur.execute('insert into train_vector (arr) VALUES(?)',(data,))

        con.commit() # db 변경요소 저장
        cur.close()  #   Cursorls
        con.close()
#fake_review.predict("kktk", "fhewufhweofhewufgewuif")