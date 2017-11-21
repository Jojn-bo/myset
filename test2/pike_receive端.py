import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#这个声明是防止先运行消费者.py时,没声明队列引起报错而再声明一次的，
#如果确定生产者.py中有这个队列，则不用声明（再声明一次也没什么关系）
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print('-->',ch, method, properties)
    print("[x] Received %r"% body)

channel.basic_consume(#消费消息
                    callback,#如果收到消息，就调用callback函数来处理
                    queue='hello',
                    no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()