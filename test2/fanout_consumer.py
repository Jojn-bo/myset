import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channal = connection.channel()

channal.exchange_declare(exchange='logs',exchange_type= 'fanout')

result = channal.queue_declare(exclusive = True)#exclusive:排他，唯一的,不指定queue名字，rabbit会随机分配一个名字，exclusive=True会在使用此queue的消费者断开后，自动将queue删除
queue_name = result.method.queue
print('random queuename',queue_name)

channal.queue_bind(exchange='logs',queue=queue_name)

print('[*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print('[x] %r'%body)

channal.basic_consume(callback, queue=queue_name, no_ack=True)

channal.start_consuming()