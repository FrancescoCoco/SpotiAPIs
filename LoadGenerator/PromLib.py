import time
from datetime import datetime

from prometheus_api_client import PrometheusConnect


# Activate connection to prometheus server
import MongoLib


def activate_connection():
    prom = PrometheusConnect(url="http://localhost:9090/", disable_ssl=True)
    return prom


# get all metrics
def get_all_metrics(prom: PrometheusConnect):
    print(prom.all_metrics())


# get response time of find all artists:
def get_resp_time_findallartist(prom: PrometheusConnect, nartists, cpu, memory):
    time.sleep(1)
    metrics = prom.custom_query(query="response_time_findAllArtist")
    for metric in metrics:
        response_time = metric['value'][1]
        my_metric_mongo = {'response_time': response_time,'number_artists': nartists, 'cpu': cpu, 'memory': memory}
        print(my_metric_mongo)
        return my_metric_mongo
