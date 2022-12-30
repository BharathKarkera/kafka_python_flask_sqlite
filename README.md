# kafka_python_flask_sqlite


**First start zookeeper instance :**

 4:43PM @Bharath  ~ `/opt/brew/opt/kafka/bin/zookeeper-server-start /opt/brew/etc/kafka/zookeeper.properties`
[2022-12-28 16:43:38,055] INFO Reading configuration from: /opt/brew/etc/kafka/zookeeper.properties (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2022-12-28 16:43:38,066] INFO clientPortAddress is 0.0.0.0:2181 (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2022-12-28 16:43:38,066] INFO secureClientPort is not set (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2022-12-28 16:43:38,066] INFO observerMasterPort is not set (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2022-12-28 16:43:38,066] INFO metricsProvider.className is org.apache.zookeeper.metrics.impl.DefaultMetricsProvider (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
[2022-12-28 16:43:38,070] INFO autopurge.snapRetainCount set to 3 (org.apache.zookeeper.server.DatadirCleanupManager)
[2022-12-28 16:43:38,070] INFO autopurge.purgeInterval set to 0 (org.apache.zookeeper.server.DatadirCleanupManager)
.
.
.

**Next Starting Kafka server :**

 4:45PM @Bharath  ~ /opt/brew/opt/kafka/bin/kafka-server-start /opt/brew/etc/kafka/server.properties
[2022-12-28 16:45:45,003] INFO Registered kafka:type=kafka.Log4jController MBean (kafka.utils.Log4jControllerRegistration$)
[2022-12-28 16:45:45,268] INFO Setting -D jdk.tls.rejectClientInitiatedRenegotiation=true to disable client-initiated TLS renegotiation (org.apache.zookeeper.common.X509Util)
[2022-12-28 16:45:45,346] INFO Registered signal handlers for TERM, INT, HUP (org.apache.kafka.common.utils.LoggingSignalHandler)
[2022-12-28 16:45:45,348] INFO starting (kafka.server.KafkaServer)
[2022-12-28 16:45:45,349] INFO Connecting to zookeeper on localhost:2181 (kafka.server.KafkaServer)
[2022-12-28 16:45:45,362] INFO [ZooKeeperClient Kafka server] Initializing a new session to localhost:2181. (kafka.zookeeper.ZooKeeperClient)
[2022-12-28 16:45:45,368] INFO Client environment:zookeeper.version=3.6.3--6401e4ad2087061bc6b9f80dec2d69f2e3c8660a, built on 04/08/2021 16:35 GMT (org.apache.zookeeper.ZooKeeper)
[2022-12-28 16:45:45,368] INFO Client environment:host.name=192.168.1.70 (org.apache.zookeeper.ZooKeeper)
.
.
.


**Run the flask app :**

 2:46PM @Bharath  ~ python3 app.py
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://17.233.54.29:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 488-492-345



**Place an order by passing email id and the number of quantity :**


 3:11PM @Bharath  ~ curl --data "quantity_no_text=10&email_id=naga@gmail.com" http://localhost:5000/order
Order details {'order_id': 'fe843f95-73a3-4537-af29-b179c8fa5ec4', 'number_of_items': 10, 'email_id': 'naga@gmail.com', 'cost': 150}
3:11PM @Bharath  ~ 
 3:11PM @Bharath  ~ 
 3:11PM @Bharath  ~ curl -i --data "quantity_no_text=15&email_id=bharath@gmail.com" http://localhost:5000/order
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 135
Server: Werkzeug/2.0.2 Python/3.9.7
Date: Fri, 30 Dec 2022 21:11:45 GMT

Order details {'order_id': '6645d7e5-c1a0-4a33-bfbe-13c70f365555', 'number_of_items': 15, 'email_id': 'bharath@gmail.com', 'cost': 225}
3:11PM @Bharath  ~ 
 3:11PM @Bharath  ~ 
 3:11PM @Bharath  ~ curl -i --data "quantity_no_text=8&email_id=suman@gmail.com" http://localhost:5000/order
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 132
Server: Werkzeug/2.0.2 Python/3.9.7
Date: Fri, 30 Dec 2022 21:12:00 GMT

Order details {'order_id': 'b0180660-7953-463c-a0c3-9d85918cd2f2', 'number_of_items': 8, 'email_id': 'suman@gmail.com', 'cost': 120}

 3:13PM @Bharath  ~ curl -i -X POST  --data "quantity_no_text=2&email_id=shrini@gmail.com" http://localhost:5000/order
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 132
Server: Werkzeug/2.0.2 Python/3.9.7
Date: Fri, 30 Dec 2022 21:14:15 GMT

Order details {'order_id': '024661dd-53b1-4ca9-a59d-7d93cb1063e0', 'number_of_items': 2, 'email_id': 'shrini@gmail.com', 'cost': 30}



**Get the order details :**

 3:19PM @Bharath  ~ curl -i http://localhost:5000/details/b0b996d0-e24e-4598-bcbc-7ba6d402277c
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 148
Server: Werkzeug/2.0.2 Python/3.9.7
Date: Fri, 30 Dec 2022 21:19:41 GMT

[
  {
    "cost": 30, 
    "email_id": "shrini@gmail.com", 
    "number_of_items": 2, 
    "order_id": "b0b996d0-e24e-4598-bcbc-7ba6d402277c"
  }
]
 3:19PM @Bharath  ~ 
 
 
 
 **Get all order details (After Authenticating):**
 
  3:32PM @Bharath  ~ curl -i -u admin:admin http://localhost:5000/details                                 
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 148
Server: Werkzeug/2.0.2 Python/3.9.7
Date: Fri, 30 Dec 2022 21:32:46 GMT

[
  {
    "cost": 150, 
    "email_id": "naga@gmail.com", 
    "number_of_items": 10, 
    "order_id": "2d7c166d-7494-45d1-b4e5-83595a7151e7"
  }
]
 3:32PM @Bharath  ~ 
