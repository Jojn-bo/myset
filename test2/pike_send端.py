import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()#声明一个管道

#声明queue
channel.queue_declare(queue='hello',durable=True)#durable服务器down了，可以持久化消息队列

# n RabbitMQ a message can never be sent directly to the queue, it away
channel.basic_publish(exchange='',
                      routing_key='hello',#queue名字
                      body='Hello World!',
                      properties=pika.BasicProperties(delivery_mode=2)#让队列中的消息持久化
                      )

print("[x] Sent 'Hello World!'")
connection.close()#关闭队列