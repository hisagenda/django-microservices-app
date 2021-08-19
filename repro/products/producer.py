import pika, json

params = pika.URLParameters('amqps://wjjtapdy:FuSZHkfACX5bsSwi8NXk5WvNfeSQSyYL@elk.rmq2.cloudamqp.com/wjjtapdy')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)