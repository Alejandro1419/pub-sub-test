#python publicador.py ruta mensaje (ejecutar en consola)
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange=''.join(sys.argv[1]), exchange_type='fanout')

message = ' '.join(sys.argv[2:]) or "Hola mundo"
channel.basic_publish(exchange=''.join(sys.argv[1]), routing_key='', body=message)
print(" [-] se envio: %r" % message)
connection.close()