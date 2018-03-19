from pymongo import MongoClient

mongo_uri="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)
db = client.get_default_database()

posts = db['posts']

post_cua_nhi = {
   "title":"Giới thiệu bản thân",
   "author":"Nhi",
   "content":"""Mình rất nhạt nhẽo và hay đi loăn quăn
dạo này loăn quăn đến tận teckids
thấy mình đỡ nhạt nhẽo và loăn quoăn hơn
recommend cho các bạn đến sau
"""
}

posts.insert_one(post_cua_nhi)
