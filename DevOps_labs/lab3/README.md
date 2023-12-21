 # ЛАБОРАТОРНАЯ РАБОТА №3
 
*Задание: сделать, чтобы после пуша в ваш репозиторий автоматически собирался докер образ и результат его сборки сохранялся куда-нибудь. (например, если результат - текстовый файлик, он должен автоматически сохраниться на локальную машину, в ваш репозиторий или на ваш сервер).*
 
 ### ВЫПОЛНЕНИЕ РАБОТЫ:
 
 1. Возьмем программу написанную на языке python(dvk.py) и сделаем так, чтобы ее вывод происходил в текстовый файл(dvk.txt).
 
 dvk.py:
 
 
![photo_2023-12-22 00 17 20](https://github.com/ArturKalinin/cloud/assets/109699946/365b5b55-0fe3-4d07-a85c-c6b731c0d180)


 
 dvk.txt:
 
 ![photo_2023-12-22 00 17 23](https://github.com/ArturKalinin/cloud/assets/109699946/4ff81ed4-8b60-4579-b226-a81f2aef4979)



 
 2. Создадим docker файл, для запуска тестов:
 
 
![photo_2023-12-22 00 17 25](https://github.com/ArturKalinin/cloud/assets/109699946/1a7e7952-d237-4088-bc8a-8ea468ad3dd7)


  
 4. Создадим секреты в виде имени и пароля пользователя, чтоб подключиться к dockerhub:
 
 ![photo_2023-12-22 00 17 27](https://github.com/ArturKalinin/cloud/assets/109699946/90946980-078a-427f-8cf0-4143213dbd3a)


 
 5. Создадим файл docker-build.yml, в котором будут задействованы наши секреты секреты, чтобы войти:
 
 
![photo_2023-12-22 00 17 29](https://github.com/ArturKalinin/cloud/assets/109699946/84cffc26-0e1d-427d-b9f6-121953292ef7)


 
 Использование никнейма:
 
 
<img width="620" alt="Снимок экрана 2023-12-22 в 00 29 43" src="https://github.com/ArturKalinin/cloud/assets/109699946/ecead270-714b-47c3-a1a9-9eb3a9406d8a">


 
 Использование пароля:
 
 <img width="618" alt="Снимок экрана 2023-12-22 в 00 29 55" src="https://github.com/ArturKalinin/cloud/assets/109699946/e1baab6d-2f93-4fae-be7d-67e6f6222f20">

 
 
 5. Смотрим прошло ли тесты:
 
 <img width="603" alt="Снимок экрана 2023-12-22 в 00 32 05" src="https://github.com/ArturKalinin/cloud/assets/109699946/e05eccb7-ee61-4e48-aee5-7c6a4ed0e96f">
<img width="433" alt="Снимок экрана 2023-12-22 в 00 32 09" src="https://github.com/ArturKalinin/cloud/assets/109699946/6af06cbe-3d84-4887-9a5c-84277a5b9757">


 
 
 6. Проверяем dockeкhub
 
 
<img width="608" alt="Снимок экрана 2023-12-22 в 00 32 14" src="https://github.com/ArturKalinin/cloud/assets/109699946/3b25d1f5-0be5-4d88-842e-ccdb5df9f179">


 
 Все работает!👍

