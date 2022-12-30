import flask
import kafka
import uuid
import json
import sqlite3 as sql
from functools import wraps
import threading
import subprocess
import datetime


TOPIC_NAME='food_order'
KAFKA_SERVER='localhost:9092'


app=flask.Flask(__name__)
app.config["DEBUG"]=True
app.config["TOKEN"]="bharathkarkera"
app.secret_key = "bharathkarkera"


db='orders.db'
connection=sql.connect(db)
cursor=connection.cursor()

cursor.execute("""
     DROP TABLE IF EXISTS USER_ORDER_DETAILS
     """)
     
cursor.execute("""
     DROP TABLE IF EXISTS EMAIL_TRACKER
     """)     

cursor.execute("""
     CREATE TABLE IF NOT EXISTS USER_ORDER_DETAILS(
     order_id TEXT NOT NULL UNIQUE,
     number_of_items INTEGER,
     email_id TEXT,
     cost INTEGER
     )""")

cursor.execute("""
     CREATE TABLE IF NOT EXISTS EMAIL_TRACKER(
     order_id TEXT NOT NULL UNIQUE,
     email_id TEXT,
     timestamp TEXT
     )""")
     
connection.commit()
connection.close()



def list_to_json_converter(passed_list,dict_keys):
   list_of_json=[]
   for i in range(0,len(passed_list)):
      my_dict={}
      for j in range(0,len(dict_keys)):
         my_dict[dict_keys[j]]=passed_list[i][j]
      list_of_json.append(my_dict)
   return list_of_json
   


@app.route('/')
def index_path():
   return flask.render_template("index.html") 




@app.route('/order',methods=["POST"])
def place_order():
   quantity_number=flask.request.form["quantity_no_text"]
   email_id=flask.request.form["email_id"]
   print(f"Request received for {quantity_number} orders!!")

   producer=kafka.KafkaProducer(bootstrap_servers=KAFKA_SERVER)
   order_id=str(uuid.uuid4())
   data = {
	"order_id": order_id,
	"number_of_items":int(quantity_number),
	"email_id":email_id,
	"cost": int(quantity_number)*15
   }
   producer.send(TOPIC_NAME,json.dumps(data).encode('utf-8'))
   producer.flush()
   
   connection=sql.connect(db)
   cursor=connection.cursor()
   cursor.execute("""INSERT INTO USER_ORDER_DETAILS VALUES (?,?,?,?) """,(order_id,int(quantity_number),email_id,int(quantity_number)*15))
   connection.commit()
   connection.close()
   return f"Order details {data}"



@app.route('/details',methods=["GET"])
def get_all_order_details():
   auth=flask.request.authorization
   if auth and auth.username=="admin" and auth.password=="admin":
      connection=sql.connect(db)
      cursor=connection.cursor()
      cursor.execute(""" SELECT * FROM USER_ORDER_DETAILS """)
      data_fetched=cursor.fetchall()
      connection.commit()
      connection.close()
      return flask.jsonify(list_to_json_converter(data_fetched,["order_id","number_of_items","email_id","cost"]))
   else:
      return flask.make_response("Could not verify your login!",401, {'WWW-Authenticate':'Basic realm="Login Required !"'})


@app.route('/details/<int:order_id>',methods=["GET"])
def get_order_details(order_id):
   connection=sql.connect(db)
   cursor=connection.cursor()
   cursor.execute(""" SELECT * FROM USER_ORDER_DETAILS where order_id= ?""" , (order_id,))
   data_fetched=cursor.fetchall()
   connection.commit()
   connection.close()
   if len(data_fetched)==0:
      return flask.make_response("We have not received your order, Please place an order via http://localhost:5000 !",400, {'WWW-Authenticate':'Basic realm="Login Required !"'})
   else:
      return flask.jsonify(list_to_json_converter(data_fetched,["order_id","number_of_items","email_id","cost"]))


def consume_message_and_trigger_email():
   consumed_messages=kafka.KafkaConsumer(TOPIC_NAME)
   for i in consumed_messages:
      value=json.loads(i.value.decode())
      email_id_extracted=value["email_id"]
      order_id_extracted=value["order_id"]
      
      first_part='say  "sent email to "'
      args=first_part+str(email_id_extracted)
      subprocess.run(args,shell=True)
      
      connection=sql.connect(db)
      cursor=connection.cursor()
      cursor.execute("""INSERT INTO EMAIL_TRACKER VALUES (?,?,?) """,(order_id_extracted,email_id_extracted,str(datetime.datetime.now())))
      connection.commit()
      connection.close()      
      

@app.route('/emails',methods=["GET"])
def get_email_transaction_details():
   auth=flask.request.authorization
   if auth and auth.username=="admin" and auth.password=="admin":
      connection=sql.connect(db)
      cursor=connection.cursor()
      cursor.execute(""" SELECT * FROM EMAIL_TRACKER """)
      data_fetched=cursor.fetchall()
      connection.commit()
      connection.close()
      return flask.jsonify(list_to_json_converter(data_fetched,["order_id","email_id","timestamp"]))
   else:
      return flask.make_response("Could not verify your login!",401, {'WWW-Authenticate':'Basic realm="Login Required !"'})
   

@app.before_first_request
def launch_consumer():
   my_thread=threading.Thread(target=consume_message_and_trigger_email)
   my_thread.start()
   

#curl -i -X POST http://localhost:5000/order -d "quantity_no_text=5"


app.run(host="0.0.0.0")   
