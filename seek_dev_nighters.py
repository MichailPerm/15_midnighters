import requests
import pytz
from datetime import datetime, time

API_URL = 'https://devman.org/api/challenges/solution_attempts/'


def load_attempts():
    pages = 2
    for page in range(1, pages):
        response = requests.get(API_URL, params={'page': page})
        page_data = response.json()
        pages = int(page_data.get('number_of_pages'))
        records = page_data.get('records')
        for record in records:
            if record.get('timestamp'):
                yield record


def get_time(timezone, timestamp):
    user_time = datetime.fromtimestamp(timestamp, pytz.timezone(timezone)).time()
    if time(0, 0, 0) < user_time < time(6, 0, 0):
        return user_time
    return None


def get_midnighters():
    midnighters = []
    for record in load_attempts():
        if not record:
            break
        if get_time(record.get('timezone'), record.get('timestamp')):
            midnighters.append(record.get('username'))

    return midnighters


def print_midnighters(midnighters):
    for midnighter in midnighters:
        print(midnighter)


if __name__ == '__main__':
    midnighters = get_midnighters()
    print_midnighters(midnighters)
