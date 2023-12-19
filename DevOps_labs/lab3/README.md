 # ЛАБОРАТОРНАЯ РАБОТА №3
 
*Задание: сделать, чтобы после пуша в ваш репозиторий автоматически собирался докер образ и результат его сборки сохранялся куда-нибудь. (например, если результат - текстовый файлик, он должен автоматически сохраниться на локальную машину, в ваш репозиторий или на ваш сервер).*
 
 ### ВЫПОЛНЕНИЕ РАБОТЫ:
 
 1. Возьмем программу написанную на языке python(dvk.py) и сделаем так, чтобы ее вывод происходил в текстовый файл(dvk.txt).
 
 dvk.py:
 
 
 ![image](https://github.com/vitaliy1432/test/assets/112981941/d0a79a11-9a56-47f5-bdb0-3d2a9b16de99)

 
 dvk.txt:
 
 
 ![image](https://github.com/vitaliy1432/test/assets/112981941/3c40c34f-fd4b-4b95-a625-73557dcda60f)

 
 2. Создадим docker файл, для запуска тестов:
 
 
 ![image](https://github.com/vitaliy1432/test/assets/112981941/a6fba63e-c146-4748-9a6a-e103abe34d54)

  
 4. Создадим секреты в виде имени и пароля пользователя, чтоб подключиться к dockerhub:
 
 
 ![image](https://github.com/vitaliy1432/test/assets/112981941/728f4020-2eaa-42f0-aa26-e24d68c8160c)

 
 5. Создадим файл docker-build.yml, в котором будут задействованы наши секреты секреты, чтобы войти:
 
 
 ![image](https://github.com/vitaliy1432/test/assets/112981941/aee6a815-4b7a-4a43-95c0-bc5619ee6dda)

 
 Использование никнейма:
 
 
 ![image](https://github.com/vitaliy1432/test/assets/112981941/0fdb0fb9-d584-4c0e-aec6-7f41d93eeee7)
 ![image](https://github.com/vitaliy1432/test/assets/112981941/ce73ae5f-a5d8-4fad-b158-e2d72d46e17a)
 ![image](https://github.com/vitaliy1432/test/assets/112981941/547083db-8448-4450-80ba-1247592f93ac)

 
 Использование пароля:
 
 
 ![image](https://github.com/vitaliy1432/test/assets/112981941/547083db-8448-4450-80ba-1247592f93ac)

 
 5. Смотрим прошло ли тесты:
 
 
 ![image](https://github.com/vitaliy1432/test/assets/112981941/fe236069-573a-49c6-9dde-b937f39982ae)
 ![image](https://github.com/vitaliy1432/test/assets/112981941/e131a7e1-6d79-48ea-86d6-9980b7fecb9b)
 
 
 6. Проверяем dockeкhub
 
 
 ![image](https://github.com/vitaliy1432/test/assets/112981941/9e69d87c-aa21-4ab8-b73c-7a1ce8741858)

 
 Все работает!👍

