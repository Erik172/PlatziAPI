# Codigo para Extraer y Transformar los datos restornados por el web scraper
from scrapinghub import ScrapinghubClient
from scrapinghub import client
import models
import os

client = ScrapinghubClient(os.getenv('SCRAPINGHUB_KEY'))
idProyect = os.getenv('SCRAPINGHUB_PROJECT')
project = client.get_project(idProyect)

def initSpiderPlatzi():
    project.jobs.run('platzi')

def dataSpiderPlatziFilterCourses(job):
    job = client.get_job(f'{idProyect}/2/{job}')

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
    job = client.get_job(f'{idProyect}/1/{job}')
    
    for item in job.items.iter():
        total = models.totalPosts()
        if models.searchPostTitle(item['name']) == True:
            print(f"El post {item['name']} ya existe")
        else:
            print(f"agregando el post {item['name']}")
            item['_id'] = total
            models.addPost(item)

    return 201
    