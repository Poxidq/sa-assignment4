import threading
import queue

class Pipeline:
    def __init__(self, stages):
        self.stages = stages
        self.queues = [queue.Queue() for _ in range(len(stages) + 1)]
        self.threads = []

    def start(self):
        for i, stage in enumerate(self.stages):
            thread = threading.Thread(target=stage, args=(self.queues[i], self.queues[i + 1]))
            self.threads.append(thread)
            thread.start()

    def stop(self):
        for q in self.queues:
            q.put(None)

        for thread in self.threads:
            thread.join()
