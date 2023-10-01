# Лабораторная работа #1 
Задание: Пользуясь терминалом на компьютере А перенести файл с компьютера Б на компьютер С, находящиеся в одной локальной сети.

1) __Проверяем, чтоб все устройства были подключены к одной локальной сети:__
   
   ![1](https://github.com/ArturKalinin/cloud/assets/109699946/0e13e4a2-c7bf-44b9-8a7c-88e814a9a304)

   <img width="567" alt="Снимок экрана 2023-09-28 в 13 35 11" src="https://github.com/ArturKalinin/cloud/assets/109699946/5fc323c6-0228-4e84-85d4-18b4665b0688">
   
![4](https://github.com/ArturKalinin/cloud/assets/109699946/ab09c245-51dc-424d-aea8-39d80fcd0653)

2) __Подключаемся с устройства A(имя пользователя artur) к устройству Б(имя пользователя kirill) с помощью команды `ssh [имя пользователя]@[ip-адрес]` и пароля от пользователя kirill:__
   
   <img width="571" alt="Снимок экрана 2023-09-28 в 13 56 46" src="https://github.com/ArturKalinin/cloud/assets/109699946/184ebdaa-19f2-492e-beec-4b1ca70b1e95">

3) __Осталось только перенести файл с устройства C(имя пользователя kravn) на устройство Б через терминал устройства A с помощью команды `pscp [имя пользователя]@[ip-адрес]:[путь к файлу] [путь к файлу]` и пароля от пользователя kravn:__

   <img width="569" alt="Снимок экрана 2023-09-28 в 13 58 52" src="https://github.com/ArturKalinin/cloud/assets/109699946/9f25ac97-571a-4453-b264-3fafc28658b7">

4) __Все прошло успешно, мы можем наблюдать файл там, куда мы его и передали:__

![3](https://github.com/ArturKalinin/cloud/assets/109699946/d4b97dcc-1679-4ded-9865-1fbab3fced51)

   