
import pickle

# Creating a dict of info of students
dict_info = {
    'Name' : 'Chaitanya',
    'Age' : 12,
    'Gender' : 'Male',
    'School' : 'AVEMPS',
    'Freinds' : ['Adwait','Vishrut','Samartha','Neel'],
    'Class' : 7
}

# Opening a new pkl file and dumping the dict dictionary in the pkl file, in write binary mode
with open('test.pkl','wb') as pkl:
    pickle.dump(dict_info,pkl)
    
# Deleting the dict
del dict_info

# Now there is no dict named dict_info, so let's revive it and read it, in read binary mode
with open('test.pkl','rb') as open_pkl:
    dict_revive = pickle.load(open_pkl)

print(dict_revive)



    