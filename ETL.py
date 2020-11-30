# Codigo para Extraer y Transformar los datos restornados por el web scraper
from scrapinghub import ScrapinghubClient
import models
import time
import json
import os

# API KEY de ScrapingHub
apiKey = os.environ["API_SCRAPY"]
client = ScrapinghubClient(apiKey)

project = client.get_project(484255)

def initSpiderPlatzi():
    project.jobs.run('platzi')

def dataSpiderPlatziFilterCourses(job):
    job = client.get_job(f'484255/2/{job}')

    for item in job.items.iter():
        total = models.totalCourses()
        if item.get('course'):
            if models.searchCourseName(item['course']) == True:
                print(f'Ya Exite {item["course"]}')
            else:
                print(f"Agregando {item['course']}")
                item['_id'] = total
                models.addCourse(item)
    return 201

def initSpiderBlog():
    project.jobs.run('blog')

def dataSpiderBlog(job: int):
    job = client.get_job(f'484255/1/{job}')
    
    for item in job.items.iter():
        total = models.totalPosts()
        if models.searchPostTitle(item['name']) == True:
            print(f"El post {item['name']} ya existe")
        else:
            print(f"agregando el post {item['name']}")
            item['_id'] = total
            models.addPost(item)

    return 201

def automaticSpiderBlog():
    with open('config/jobBlog.json') as f:
        job = json.load(f)
        initSpiderBlog()
        print("En 20 minutos empieza el filtrado de datos")
        time.sleep(1200)
        dataSpiderBlog(int(job['job']))
        job['job'] += 1
        f.write(job)
        f.close()

def automaticSpiderPlatzi():
    with open('config/jobPlatzi.json') as f:
        job = json.load(f)
        initSpiderPlatzi()
        print("En 20 minutos empieza se empieza a los filtrar datos")
        time.sleep(1200)
        dataSpiderPlatziFilterCourses(int(job['job']))
        job['job'] += 1
        f.write(job)
        f.close()