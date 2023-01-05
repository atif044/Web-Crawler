import threading
from queue import Queue
from spider import *
from domain import *
from general import *
from query_link_finder import *
from animation import *

print("WELCOME TO WEB SCRAPER 2.0")
#spider_shape()
user_choice =int(input("""Please enter what processor you want to execute\n1. Search by content.\n2. Search by link and domain name.\n"""))
if user_choice == 1:
    user_query = input("Enter your query: ")
    thread1 = threading.Thread(target=loading_line)
    thread1.start()
    thread1.join()
    thread2 = threading.Thread(target=execute(user_query))
    thread2.start()
   
elif user_choice == 2:
    PROJECT_NAME = input('Project Name:')
    HOMEPAGE = input('Home Page:')
    DOMAIN_NAME = get_domain_name(HOMEPAGE)
    QUEUE_FILE = PROJECT_NAME + '/queue.txt'
    CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
    NUMBER_OF_THREADS = 10
    queue = Queue()
    #FIRST_SPIDER    is speacial it will parse the main page to gaather meta data
    Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)   

    #create worker threads (will end when main exits)
    def create_workers():
        for _ in range(NUMBER_OF_THREADS):
            t = threading.Thread(target=work)
            t.daemon = True #ensuers that it exists when the main ends
            t.start()

    #do the next job in the queue
    def work():
        while True:
            url=queue.get()        
            Spider.crawl_page(threading.current_thread().name, url)
            queue.task_done()

    #each queued links is a new job
    def create_jobs():
        for link in file_to_set(QUEUE_FILE):
            queue.put(link)
        queue.join()
        crawl()


    #check if there is item then is so crawl them
    def crawl():
        queued_links=file_to_set(QUEUE_FILE)
        if len(queued_links) >0:
            print(str(len(queued_links))+ ' links in the queue')
            create_jobs()   

    create_workers()
    crawl()
    print("Execution terminated...")


else :
    print("Invalid input arguments")
    print("Execution terminated...")


