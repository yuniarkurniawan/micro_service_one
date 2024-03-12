import pika, json

params = pika.URLParameters('amqps://edoubgdl:JCEWuKDUzNJ6h0iR_ilmuRLuz4JpQRwH@armadillo.rmq.cloudamqp.com/edoubgdl')
connection = pika.BlockingConnection(params)

chanel = connection.channel()

def publish(method, body):

    properties = pika.BasicProperties(method)
    chanel.basic_publish(
        exchange='', 
        routing_key='admin', 
        body=json.dumps(body), 
        properties=properties)