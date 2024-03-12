import pika, json, os, django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Products

try:
    params = pika.URLParameters(<YOUR_AMQP_URL>)
    connection = pika.BlockingConnection(params)

    chanel = connection.channel()
    chanel.queue_declare(queue='admin')

    def callback(ch, method, properties, body):
        print('Receipt in admin')
        data = json.loads(body)
        print(data)

        product = Products.objects.get(id=data)
        product.likes = product.likes + 1
        product.save()
        print('Product increase....!')

    chanel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)
    print('Start Consuming in Django')
    chanel.start_consuming()
    chanel.close()

except Exception as e:
    print(e)
