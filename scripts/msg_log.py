import rosbag
import json
import yaml

bag = rosbag.Bag('../etc/bag_test.bag')

def get_bag_info():
    info_dict = yaml.load(rosbag.Bag('../etc/bag_test.bag', 'r')._get_yaml_info())
    print json.dumps(info_dict, indent=4)

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

msg_list = []
for topic, msg, t in bag.read_messages():
    bagdata = {
        "topic": topic,
        "data": msg2json(msg, 0),
        "timestamp": str(t)
    }
    print "topic: ", topic
    #print "msg: \n", msg
    #print "time: ", str(t)
    #print "\n-----------------------------"

    msg_list.append(bagdata)
bag.close()



