import threading
import pymysql
import time


from validate_email import validate_email

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='check_email',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
myCursor =connection.cursor()

db_lock = threading.Lock()

class myThread(threading.Thread):
    def __init__(self, name, file_path):
        threading.Thread.__init__(self)
        self.name = name
        self.file_path = file_path
    def run(self):
        time.start = time.time()
        file = open(self.file_path, 'r')
        print('San sang chay ' + self.name)
        while True:
            s = file.readline()
            s1 = s.strip("\n")
            if s1 == None or s1 == '' or s1 == '\n':
                break
            is_valid = validate_email(s1, verify=True)
            if is_valid == True:
                query ="INSERT INTO exit_email(email) VALUES('" + s1 + "');"
                print("Query: " + query)
                db_lock.acquire()
                myCursor.execute(query)
                connection.commit()
                db_lock.release()
            else:
                query = "INSERT INTO non_exit_email(email) VALUES('" + s1 + "');"
                print("Query: " + query)
                db_lock.acquire()
                myCursor.execute(query)
                connection.commit()
                db_lock.release()
        time.end = time.time()
        print(time.end - time.start)

if __name__ == "__main__":
    thread1 = myThread('Thread 1', 'test1.txt')
    # thread2 = myThread('Thread 2', 'test2.txt')
    # thread3 = myThread('Thread 3', 'test3.txt')
    # thread4 = myThread('Thread 4', 'test4.txt')
    # thread5 = myThread('Thread 5', 'test5.txt')
    # thread6 = myThread('Thread 6', 'test6.txt')
    # thread7 = myThread('Thread 7', 'test7.txt')
    # thread8 = myThread('Thread 8', 'test8.txt')
    # thread9 = myThread('Thread 9', 'test9.txt')
    # thread10 = myThread('Thread 10', 'test10.txt')
    # thread11 = myThread('Thread 11', 'test11.txt')
    # thread12 = myThread('Thread 12', 'test12.txt')
    # thread13 = myThread('Thread 13', 'test13.txt')
    # thread14 = myThread('Thread 14', 'test14.txt')
    # thread15 = myThread('Thread 15', 'test15.txt')
    # thread16 = myThread('Thread 16', 'test16.txt')
    # thread17 = myThread('Thread 17', 'test17.txt')
    # thread18 = myThread('Thread 18', 'test18.txt')
    # thread19 = myThread('Thread 19', 'test19.txt')
    # thread20 = myThread('Thread 20', 'test20.txt')
    thread1.start()
    # thread2.start()
    # thread3.start()
    # thread4.start()
    # thread5.start()
    # thread6.start()
    # thread7.start()
    # thread8.start()
    # thread9.start()
    # thread10.start()
    # thread11.start()
    # thread12.start()
    # thread13.start()
    # thread14.start()
    # thread15.start()
    # thread16.start()
    # thread17.start()
    # thread18.start()
    # thread19.start()
    # thread20.start()






