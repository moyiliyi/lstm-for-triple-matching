import json
import cPickle as pickle
def pre_data(path):
    sentence_list_fname = path
    sentence_list = json.load(open(sentence_list_fname,'r'))
    f=open('trainset.txt','w')
    m,tr,te=0,0,0
    train_set=[]
    test_set=[]
    train_x=[]
    train_id=[]

    test_x=[]
    test_id=[]



    for line in sentence_list:
        #print line.values()[1]#indexes
        #print line.values()[2]#times
        #print line.values()[3]#attributes
        #print line.values()[4]#values
        #print line.values()[]#results
        id          = line["sentenceId"]
        index  = line["indexes"]
        time         = line["times"]
        attribute    = line["attributes"]
        value        = line["values"]


        
        for i in range(len(time)):
            for j in range(len(attribute)):
                for k in range(len(value)):
                    tri= id
                    tri=list(tri)
                    test_id.append(tri)
                    
                    index.append(time[i])
                    index.append(attribute[j])
                    index.append(value[k])
                    temp =  list(index)
                    test_x.append(temp)
                    
                    del index[-1]
                    del index[-1]
                    del index[-1]
                    test_set=test_x,[],test_id
                    
                    
                    
                

                    
        
        #f.write(str(line.values()[7]))
        
        #print json.dumps(line)

    #print train_set[0]
    #print test_set[0]

    fout = file('test with id.pkl','wb')
    pickle.dump(test_set,fout,True)


    #f = open('readdata.txt','w')
    f.close()
    fout.close()


    '''ol = json.loads(open('assignment_training_data_word_segment.json').read())
    for line in ol:
        bar = str(line).decode('unicode-escape').encode('utf-8')
        print bar
        #f.write(bar)
        #f.write('\n')'''
    

    



