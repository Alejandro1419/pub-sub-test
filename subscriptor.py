#python subscriptor.py ruta (ejecutar en consola)
import pika
import sys
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange=''.join(sys.argv[1]), exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange=''.join(sys.argv[1]), queue=queue_name)

print(' *** Esperando mensaje por el canal '+''.join(sys.argv[1])+' Para salir presione CTRL+C ***')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()