import pika, json

params = pika.URLParameters(<YOUR_AMQP_URL>)
connection = pika.BlockingConnection(params)

chanel = connection.channel()

def publish(method, body):

    properties = pika.BasicProperties(method)
    chanel.basic_publish(
        exchange='', 
        routing_key='main', 
        body=json.dumps(body), 
        properties=properties)
