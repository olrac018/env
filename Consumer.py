import json
from kafka import KafkaConsumer


class Person(object):
    def __init__(self, fname, mname, lname):
        self.fname = fname
        self.mname = mname
        self.lname = lname




consumer = KafkaConsumer('foobar', bootstrap_servers='192.168.8.101:9092')

for msg in consumer:

    loaded = json.loads(msg.value)


    employee = Person(**loaded)

    print (employee)

    print employee.fname
    print employee.mname
    print employee.lname
