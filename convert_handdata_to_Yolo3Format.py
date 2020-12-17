from os import getcwd
from pandas import read_csv
from pandas import DataFrame
from pandas import concat

sets=['train', 'test']
classes = ["hand"]
wd = getcwd()
downSampleRate = 1
fields = ['filename','width','height','class','xmin','ymin','xmax','ymax']
def check_dataset(dataset):
    print(dataset) # this will print the a few rows of data from the beginning and end
    print('dataset.columns=', dataset.columns)
    print('last row:')
    print(dataset.values[-1])
    print('This the shape of whole data')
    print(dataset.shape)

    if( dataset.shape[0] > 5):
        print('This is to print the first 5 rows of data, plus the header')
        print(dataset.head(5))
        
        print('This is another way to print the first 5 rows of data, plus the header')
        print(dataset[0:5])
        print('Access to the first value in a particular column. For example:')
        print('the first value in a column "filename" is: ', dataset['filename'][0])
        print('the third value in a column "height" is: ', dataset['height'][2])
	
    print('{0} rows of dataset is loaded'.format(dataset.shape[0]))

def ceate_train():
    list_file = open('train.txt', 'w')
    dataset_train = read_csv('hand_data/train/train_labels.csv', header=0, index_col=None, usecols=fields)
    # for downsampling
    #dataset_train = dataset_train_o[dataset_train.index % downSampleRate == 0] 
    check_dataset(dataset_train)
	
    number_train_data = dataset_train.shape[0]
    last_filename = ''
    for i in range(number_train_data):
        filename = dataset_train['filename'][i]
        x_min = dataset_train['xmin'][i]
        y_min = dataset_train['ymin'][i]
        x_max = dataset_train['xmax'][i]
        y_max = dataset_train['ymax'][i]
        class_id = 0
        if last_filename != filename: # an different image
            if last_filename != '': list_file.write('\n')
            list_file.write('%s/hand_data/train/%s %d,%d,%d,%d,%d'%(wd,filename,x_min,y_min,x_max,y_max,class_id))
        else:
            list_file.write(' %d,%d,%d,%d,%d'%(x_min,y_min,x_max,y_max,class_id))
        last_filename = filename
    list_file.close()
    print('train.txt is created.')

def ceate_test():
    list_file = open('test.txt', 'w')
    dataset_test = read_csv('hand_data/test/test_labels.csv', header=0, index_col=None, usecols=fields)
    # for downsampling
    #dataset_test = dataset_test_o[dataset_test.index % downSampleRate == 0] 
    check_dataset(dataset_test)
	
    number_test_data = dataset_test.shape[0]
    last_filename = ''
    for i in range(number_test_data):
        filename = dataset_test['filename'][i]
        x_min = dataset_test['xmin'][i]
        y_min = dataset_test['ymin'][i]
        x_max = dataset_test['xmax'][i]
        y_max = dataset_test['ymax'][i]
        class_id = 0
        if last_filename != filename: # an different image
            if last_filename != '': list_file.write('\n')
            list_file.write('%s/hand_data/test/%s %d,%d,%d,%d,%d'%(wd,filename,x_min,y_min,x_max,y_max,class_id))
        else:
            list_file.write(' %d,%d,%d,%d,%d'%(x_min,y_min,x_max,y_max,class_id))
        last_filename = filename
    list_file.close()
    print('test.txt is created.')

ceate_train()	
ceate_test()	
