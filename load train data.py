import json
import cPickle as pickle

sentence_list_fname = 'assignment_training_data_word_segment.json'
sentence_list = json.load(open(sentence_list_fname,'r'))
f=open('trainset.txt','w')
m,tr,te=0,0,0
train_set=[]
test_set=[]
train_x=[]
train_y=[]

test_x=[]
test_y=[]



for line in sentence_list:
    #print line.values()[7]#indexes
    #f.write(str(line.values()[3]))
    #print line.values()[3]#times
    #print line.values()[6]#attributes
    #print line.values()[4]#values
    #print line.values()[2]#results
  
    
    for i in range(len(line.values()[3])):
        for j in range(len(line.values()[6])):
            for k in range(len(line.values()[4])):
                tri= line.values()[3][i],line.values()[6][j],line.values()[4][k]
                tri=list(tri)
                if tri in line.values()[2]:
                    if m%2==0:
                        train_y.append(1)
                    else:
                        test_y.append(1)
                else:
                    if m%2==0:
                        train_y.append(0)
                    else:
                        test_y.append(0)
                
                line.values()[7].append(line.values()[3][i])
                line.values()[7].append(line.values()[6][j])
                line.values()[7].append(line.values()[4][k])
                temp =  list(line.values()[7])
                if m%2==0:
                    train_x.append(temp)
                else:
                    test_x.append(temp)
                del line.values()[7][-1]
                del line.values()[7][-1]
                del line.values()[7][-1]
                if m%2==0:
                    train_set=train_x,train_y
                    tr=tr+1
                else:
                    test_set=test_x,test_y
                    te=te+1

                
                
            

                
    
    #f.write(str(line.values()[7]))
    
    #print json.dumps(line)
    m=m+1
    '''if m == 500:
        break'''
#print train_set[0]
#print test_set[0]

fout = file('info.pkl','wb')
pickle.dump(train_set,fout,True)
pickle.dump(test_set,fout,True)
print m,tr,te
#f = open('readdata.txt','w')
f.close()
fout.close()


'''ol = json.loads(open('assignment_training_data_word_segment.json').read())
for line in ol:
    bar = str(line).decode('unicode-escape').encode('utf-8')
    print bar
    #f.write(bar)
    #f.write('\n')'''
    

    



