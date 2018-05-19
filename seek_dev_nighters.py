import requests

def load_attempts():
    pages = 1
    for page in range(pages):
        # FIXME подключить загрузку данных из API
        yield {
            'username': 'bob',
            'timestamp': 0,
            'timezone': 'Europe/Moscow',
        }

def get_midnighters():
    pass

if __name__ == '__main__':
  pass
