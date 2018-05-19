import requests
import pytz
from datetime import datetime

API_URL = 'https://devman.org/api/challenges/solution_attempts/'


def get_pages_quantity():
    response = requests.get(API_URL)
    page_data = response.json()
    return page_data.get('number_of_pages')


def load_attempts():
    pages = get_pages_quantity()
    for page in range(1, pages):
        response = requests.get(API_URL, params={'page': page})
        page_data = response.json()
        records = page_data.get('records')
        for record in records:
            yield record


def check_if_time_in_range(timezone, timestamp):
    user_hour = datetime.fromtimestamp(timestamp, pytz.timezone(timezone)).hour
    if 0 < user_hour < 6:
        return True


def get_midnighters(attempts):
    midnighters = []
    for record in attempts():
        if not record:
            break
        if check_if_time_in_range(
                record.get('timezone'),
                record.get('timestamp')
        ):
            midnighters.append(record.get('username'))
    midnighters = sorted(list(set(midnighters)))
    return midnighters


def print_midnighters(midnighters):
    for midnighter in midnighters:
        print(midnighter)


if __name__ == '__main__':
    midnighters = get_midnighters(load_attempts)
    print_midnighters(midnighters)
