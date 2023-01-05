import os 
##each website we crawl is a seperate project

#creating a new project directory to save content
def create_project_directory(directory):
    if not os.path.exists(directory):
        print("creating project directory..." + '('+directory+')')
        os.makedirs(directory)
        
#self made directory remove functionality
def delete_project_directory(directory):
    if os.path.exists(directory):
        print("deleting project directory..." +'('+directory+')')
        os.removedirs(directory)
    else:
        print('('+directory+')'+" does not exist...")
        
#create queue and crawled files 
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.exists(project_name):
        create_project_directory(project_name)
    if not os.path.isfile(queue):
        write_file(queue,base_url)
        print('queue file created')
    if not os.path.isfile(crawled):
        write_file(crawled,'')  
        print('crawl file created')
    print('all file created sucessfully')

#writing data in files
def write_file(file_name , data):
    with open(file_name, 'w') as fil:
        fil.write(data)
    print('write successful')

#add data to existing file
def append_to_file(file_name,data):
    with open(file_name,'a') as fil:
        fil.write(data+'\n') 

#delete existing data from file
def trunc_file_content(file_name):
    with open(file_name,'w'):
        pass
    
#use set because it only allows unique element

#read a file and convert each line to set items
def file_to_set(file_name):    
    result=set()
    with open(file_name,'rt')as fil:
        for line in fil:
            result.add(line.replace('\n','')) #replace a specific character with what you want
    return result

#iterate through set, each item will be new line in the file
def set_to_file(links,file_name):
    trunc_file_content(file_name)
    for link in sorted(links): #sorts the links by alphabetic order
         append_to_file(file_name,link)

#parsing through html files