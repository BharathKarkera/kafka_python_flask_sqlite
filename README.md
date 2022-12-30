# kafka_python_flask_sqlite


First start zookeeper instance :

 4:43PM @Bharath  ~ /opt/brew/opt/kafka/bin/zookeeper-server-start /opt/brew/etc/kafka/zookeeper.properties
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

Next Starting Kafka server :

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


Run the flask app :

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



Place an order by passing email id and the number of quantity :


