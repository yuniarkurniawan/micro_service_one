import pika, json
from models import Products
from database import db
from main import app

try:
    params = pika.URLParameters(<YOUR_AMQP_URL>)
    connection = pika.BlockingConnection(params)

    chanel = connection.channel()
    chanel.queue_declare(queue='main')

    def callback(ch, method, properties, body):
        print('Received in main Flask')
        data = json.loads(body)
        print(data)

        if properties.content_type == 'product_created':
            
            product = Products(
                id=data['id'], 
                title=data['title'], 
                image=data['image']
            )

            db.session.add(product)
            db.session.commit()

        elif properties.content_type == 'product_updated':

            product = db.session.query(Products).get(int(data['id']))
            product.title = data['title']
            product.image = data['image']

            db.session.commit()

        elif properties.content_type == 'product_deleted':
            
            product = db.session.query(Products).get(int(data))
            db.session.delete(product)
            db.session.commit()


    chanel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)
    print('Start Consuming Main in Flask')
    chanel.start_consuming()

    chanel.close()
except Exception as e:
    print(e)
