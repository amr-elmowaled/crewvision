import asyncio
from vision_objects import Scene

# Note: there will definity be a lot of other functions or classes, but these here for now are inteded to serve as the blueprint for the contract between CV team and App team

class VisionEngine:

    def __init__(self, config_path="vision/config.json", buffer_limit=500):
        """
        buffer_limit: the maximum amount of Scenes the engine should store in the scenes queue before it starts discarding old scenes
        config_path: the path to config.json file, which stores the data about cameras, their IPs, which stream to use, and its zone specific x,y,width,height in the frame

        note: its very unlikely that the vision engine will outrun the app, but buffer limit is added anyway as a 'just in case' guardrail.
        note: the config.json file is inteded to be setup only once during installation
        """


        pass

    async def create_stream(self):
        """
        streaming scenes
        note: a thread fetching new scenes to the scenes queue will be running here
        note: the function is defined as asynchronous to block the coroutine until a new scene is ready in the queue if none exists
        """
        
        while True:

            # note: a producer-consumer problem comes here, the producer runs in another thread
            scene = await asyncio.to_thread(self.scenes_queue.get) # fetch the next scene or wait until the producer add a new scene if the scenes queue is empty

            yield scene # yield a scene ! -- hamada helal documentation :)

    def pause_streaming(self):
        """stops adding new scene to the scenes queue, stopping both inference and camera capture"""
        pass

    def resume_streaming(self):
        """resume adding new scenes to the scenes queue"""
        pass

    def get_buffer_capacity(self):
        """returns buffer remaining empty capacity"""
        

        return self.buffer_limit - self.scenes_queue.qsize()