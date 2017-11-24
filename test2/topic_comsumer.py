import pika,sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channal = connection.channel()

channal.exchange_declare(exchange='topic_logs',exchange_type='topic')

result = channal.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write('Usage:%s [binding_key]...\n'% sys.argv[0])
    sys.exit(1)

for binding_keys in binding_keys:
    channal.queue_bind(exchange='topic_logs',queue=queue_name,routing_key=binding_keys)

print('[*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print('[x] %r:%r'% (method.routing_key, body))

channal.basic_consume(callback,queue=queue_name,no_ack=True)

channal.start_consuming()