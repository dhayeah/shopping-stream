
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
lot=[10,20,30,40]
# until ^C
while True:
    # get random values within a normal distribution of the value
	
    l=random.randint(0,3)
    types=category[l]
    status="store"
    n=random.randint(0,3)
    cost=lot[n]*price[l]
	# create CSV structure
	
    msg = f'{time()},{types},{status},{lot[n]},{cost}'
	# send to Kafka
	
    producer.send('store1', bytes(msg, encoding='utf8'))
	
    #print(f'sending data to kafka, #{count}')
    count += 1
    total_cost+=cost
    if(l==0): b1+=lot[n]
    elif(l==1):
        a1+=lot[n]
    elif (l==2):
        c1+=lot[n]
    else: 
        s1+=lot[n]
  
    print(types,status,lot[n],cost)
    if(count==51):
        print("Details:",b1,"-",a1,"-",c1,"-",s1,"-",total_cost)
        sleep(1)
        break
    sleep(0.5)
   

