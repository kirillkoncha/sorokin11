import os
import sys
import config
from vk_api import VkApi
import markovify
vk_session = VkApi(token=TOKEN)
vk = vk_session.get_api()
model_json = open('mark_model.json').read()
model = markovify.Text.from_json(model_json)
import schedule, time
import threading

def post():
    vk.wall.post(message=model.make_short_sentence(580), owner_id='-194924812')

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

schedule.every(12).hours.do(run_threaded, post)

while 1:
    schedule.run_pending()
    time.sleep(1)
