import requests

# URL вашего REST API
api_url = 'https://example.com/api/posts'

# Данные нового поста
new_post = {
    'title': 'Новый пост',
    'description': 'Это описание нового поста.'
}

# 1. Создание нового поста
response = requests.post(api_url, json=new_post)

if response.status_code == 201:  # Успешное создание
    print('Пост успешно создан.')

    # 2. Проверка наличия поста по описанию
    get_response = requests.get(api_url)
    
    if get_response.status_code == 200:
        posts = get_response.json()
        # Проверка наличия поста
        if any(post['description'] == new_post['description'] for post in posts):
            print('Пост найден на сервере.')
        else:
            print('Пост не найден на сервере.')
    else:
        print('Ошибка при получении списка постов:', get_response.status_code)
else:
    print('Ошибка при создании поста:', response.status_code)