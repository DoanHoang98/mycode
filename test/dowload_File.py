import os
import queue
import threading
import urllib.request

########################################################################
class Downloader(threading.Thread):
    """Threaded File Downloader"""

    # ----------------------------------------------------------------------
    def __init__(self, Queue, name):
        threading.Thread.__init__(self)
        self.Queue = Queue
        self.name = name

    # ----------------------------------------------------------------------
    def run(self):
        print("Start queue " + self.name + "\n")
        while True:
            # gets the url from the queue
            url = self.Queue.get()
            print("fetch url " + url + " at queue " + self.name + "\n")
            # download the file
            self.download_file(url)

            # send a signal to the queue that the job is done
            self.Queue.task_done()
            print("Done task at queue " + self.name)

    # ----------------------------------------------------------------------
    def download_file(self, url):
        """"""
        handle = urllib.request.urlopen(url)
        fname = os.path.basename(url)
        with open(fname, "wb") as f:
            while True:
                chunk = handle.read(1024)
                if not chunk: break
                f.write(chunk)

# ----------------------------------------------------------------------
def main(urls):
    """
    Run the program
    """
    Queue = queue.Queue()

    # create a thread pool and give them a queue
    for i in range(5):
        t = Downloader(Queue, i)
        t.setDaemon(True)
        t.start()

    # give the queue some data
    for url in urls:
        Queue.put(url)

    # wait for the queue to finish
    Queue.join()

if __name__ == "__main__":
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
main(urls)