import requests
import os

TRAVIS_TEST_RESULT = os.environ.get("TRAVIS_TEST_RESULT")
TRAVIS_REPO_SLUG = os.environ.get("TRAVIS_REPO_SLUG")
TRAVIS_BRANCH = os.environ.get("TRAVIS_BRANCH")
TRAVIS_JOB_WEB_URL = os.environ.get("TRAVIS_JOB_WEB_URL")
TRAVIS_COMMIT_MESSAGE = os.environ.get("TRAVIS_COMMIT_MESSAGE")
TELEGRAM_TOKEN = "808619876:GHrtj9zs-KvKhhtWyu1YoxjtIikUYMGVjD8g"
CHAT_ID = "272560060"

if TRAVIS_TEST_RESULT != 0:
    build_status = "Успешно"
else:
    build_status = "Неуспешно"

TEXT = f"Прогон завершился: {build_status} \n Репозиторий: {TRAVIS_REPO_SLUG} \n Ветка: {TRAVIS_BRANCH} \n Commit сообщение: {TRAVIS_COMMIT_MESSAGE} \n Веб-лог: {TRAVIS_JOB_WEB_URL}"


def send_message():
    URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    body = {'chat_id': CHAT_ID, 'text': TEXT}
    response = requests.post(url=URL, json=body)
    return response


def send_file():
    URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendDocument"
    body = {'chat_id': CHAT_ID}
    file = {"document": open("test_log.log")}
    response = requests.post(url=URL, data=body, files=file)
    return response


send_message()
send_file()
