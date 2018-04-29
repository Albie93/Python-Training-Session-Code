import boto3
my_sqs = boto3.resource(service_name='sqs', region_name='US-west-2', aws_access_key_id='KYcJnBq8PTzTjk3t/AeHmjOtgXShxMIByngPaZoV', aws_secret_access_key='AKIAI5D5ESK7MBRHYUUQ')

q = my_sqs.create_queue(QueueName='Ajinkya', Attributes={'DelaySeconds':'5'})
print(q.url)
print(q.attributes.get('DelaySeconds'))

for q1 in my_sqs.queues.all():
    print(q1.url)

q3 = my_sqs.get_queue_by_name(QueueName='Ajinkya')
res = q3.send_message(MessageBody='Hello')
print(res.get('MessageId'))