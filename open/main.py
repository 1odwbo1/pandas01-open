import os
folder_name = os.path.dirname(__file__)
file_name = os.path.join(folder_name,'test.txt')
with open(file_name,'w',encoding='UTF8') as f:
    f.write('orderDate,itemNo,userID,province\n')
    f.write('2018-04-08,1155380002,187455802,河北省\n')
    f.writelines(
        ['2018-04-08,1155380002,187455802,河北省\n'
         '2018-06-08,1155380002,187455802,浙江省\n'
         '2018-04-08,1155380002,187455802,福建省\n'] )
read_file = os.path.join(folder_name,'test.txt')
with open(read_file,'r',encoding='UTF8') as f:
     j = 1
     for line in f.readlines():
         print('第%d' % j + '行数据是：'+ line)
         j+=1