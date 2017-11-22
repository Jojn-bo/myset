import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channal = connection.channel()

channal.exchange_declare(exchange='logs',exchange_type= 'fanout')

result = channal.queue_declare(exclusive = True)#exclusive:排他，唯一的,不指定queue名字，rabbit会随机
queue_name = result.method.queue

channal.queue_bind(exchange='logs',queue=queue_name)

print('[*] Waiting for logs. To exit press CTRL+C')

