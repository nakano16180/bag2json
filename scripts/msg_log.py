import rosbag
import json
import yaml

bag = rosbag.Bag('../etc/bag_test.bag')

def get_bag_info():
    info_dict = yaml.load(rosbag.Bag('../etc/bag_test.bag', 'r')._get_yaml_info())
    print json.dumps(info_dict, indent=4)

def get_topic_and_type():
    topics = bag.get_type_and_topic_info()[1].keys()
    types = []
    for i in range(0,len(bag.get_type_and_topic_info()[1].values())):
        types.append(bag.get_type_and_topic_info()[1].values()[i][0])
        
    for key, val in zip(topics, types):
        print key, val

def msg2json(msg, indent):
    try:
        dic = {}
        for m in type(msg).__slots__:
            #print indent*"    ", m
            dic[m] = msg2json(msg.__getattribute__(m), int(indent+1))
        return dic            
    except:
        #print indent*"    ", msg
        return msg

#for topic, msg, t in bag.read_messages():
#    bagdata = {
#        "topic": topic,
#        "timestamp": str(t),
#        "data": msg2json(msg, 0)
#    }
    #print "topic: ", topic
    #print "msg: \n", msg
    #print "time: ", str(t)
    #print "\n-----------------------------"

get_topic_and_type()
bag.close()



