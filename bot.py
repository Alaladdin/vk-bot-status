import os
from dotenv import load_dotenv
import vk_api
import time


def main():
    print('[MAIN] started')

    # dotenv
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    # vk
    vk_session = vk_api.VkApi(os.getenv('LOGIN'), os.getenv('PASSWORD'))
    vk_session.auth()
    vk = vk_session.get_api()

    status_list = ['new status']

    def change_status(text):
        vk.status.set(text=text)
        print(f'Status changed to: \'{text}\'')

    while True:
        for i in range(len(status_list)):
            iteration_time = 1 * 60 * 60 * 24  # 1 day
            change_status(status_list[i])
            time.sleep(iteration_time)


if __name__ == '__main__':
    main()
