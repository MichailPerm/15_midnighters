import requests
import pytz
from datetime import datetime

API_URL = 'https://devman.org/api/challenges/solution_attempts/'


def load_attempts():
    pages = 1
    page = 1
    while page <= pages:
        response = requests.get(API_URL, params={'page': page})
        page_data = response.json()
        pages = page_data.get('number_of_pages')
        records = page_data.get('records')
        for record in records:
            yield record
        page += 1


def is_time_in_range(timezone, timestamp):
    midnight_hour = 0
    morning_hour = 6
    user_hour = datetime.fromtimestamp(timestamp, pytz.timezone(timezone)).hour
    return midnight_hour < user_hour < morning_hour


def get_midnighters(attempts):
    midnighters = []
    for record in attempts():
        if not record:
            break
        if is_time_in_range(
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
