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
        
    count = 0
    for key, val in zip(topics, types):
        print count, key, val
        count += 1
    return topics

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

def bag2json(topic_list):
    for topic, msg, t in bag.read_messages(topics=topic_list):
    #    bagdata = {
    #        "topic": topic,
    #        "timestamp": str(t),
    #        "data": msg2json(msg, 0)
    #    }
        print "topic: ", topic
        #print "msg: \n", msg
        #print "time: ", str(t)
        #print "\n-----------------------------"

def select():
    l = [int(i) for i in raw_input().split()]  #error
    return l

def select_topic():
    topic_list = get_topic_and_type()

    index_list = select()
    tl = []
    for i in index_list:
        print topic_list[i]
        tl.append(topic_list[i])
    bag2json(tl)

select_topic()
bag.close()



