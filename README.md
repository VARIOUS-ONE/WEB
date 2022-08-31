# 11st Ecommerce Website With Django + React



# Features
* Full featured shopping cart
* Product reviews and ratings
* Top products carousel
* Product pagination
* Product search feature
* User profile with orders
* Admin product management
* Admin user management
* Admin Order details page
* Mark orders as delivered option
* Checkout process (shipping, payment method, etc)
* PayPal / credit card integration


# Download & Setup Instructions

### Backend

```shell
$ cd backend
$ virtualenv myenv # 안 만든 경우 
$ source myenv/bin/activate
$ pip install —upgrade pip
$ pip install -r requirements.txt
$ pip install git+https://git@github.com/SKTBrain/KoBERT.git@master
$ git lfs install
$ git lfs pull
$ pip install konlpy
$ pip install sentence-transformers
$ pip install transformers
$ cd backend
$ python manage.py runserver # 좀 느림 특히 최초실행, 너무 안된다 싶음 컨트롤 시 하고 재실행.
```

### frontend
 
```shell
$ cd frontend
$ virtualenv myenv # 안 만든 경우 
$ source myenv/bin/activate
$ npm install
$ npm start
```
