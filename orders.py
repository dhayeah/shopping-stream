
# imports
from kafka import KafkaProducer # pip install kafka-python
import numpy as np              # pip install numpy
from sys import argv, exit
from time import time, sleep
import random

# set up the producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
types=""
n=0
status=""
count = 1
cost=0
l=0
category=["books","appliances","crafts","sports"]
price=[200,1500,300,900]
total_cost=0
b1=0
a1=0
c1=0
s1=0
# until ^C
while True:
    # get random values within a normal distribution of the value
	
    l=random.randint(0,3)
    types=category[l]
    status="release"
    n=random.randint(1,10)
    cost=n*price[l]
	# create CSV structure
	
    msg = f'{time()},{types},{status},{n},{cost}'
	# send to Kafka
	
    producer.send('release1', bytes(msg, encoding='utf8'))
	
    #print(f'sending data to kafka, #{count}')
    count += 1
    total_cost+=cost
    if(l==0): b1+=n
    elif(l==1):
        a1+=n
    elif (l==2):
        c1+=n
    else: 
        s1+=n
  
    print(types,status,n,cost)
    if(count==101):
        sleep(1)
        break
    sleep(0.5)
print("Details:",b1,"-",a1,"-",c1,"-",s1,"-",total_cost)
