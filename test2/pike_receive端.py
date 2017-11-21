import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#这个声明是防止先运行消费者.py时,没声明队列引起报错而再声明一次的，
#如果确定生产者.py中有这个队列，则不用声明（再声明一次也没什么关系）
channel.queue_declare(queue='hello',durable=True)

def callback(ch, method, properties, body):#回调函数
    print('-->',ch, method, properties)
    #time.sleep(30)
    print("[x] Received %r"% body)
    ch.basic_ack(delivery_tag=method.delivery_tag)#手动发信息给服务器确认

channel.basic_qos(prefetch_count=1)#如果服务器没处理完，就把信息发送到空闲的服务器上
channel.basic_consume(#消费消息
                    callback,#如果收到消息，就调用callback函数来处理
                    queue='hello',
                    #no_ack=True #消息处理完确认
)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()