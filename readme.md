# Подготовка к работе
Установка и активация окружения

``` python3 -m venv .venv_my_proj ```
``` source .venv_my_proj/bin/activate ```

Связь с репозиторием на Github

``` git config user.name "d1alekt1k" ```
``` git config user.email "nanikov8@gmail.com" ```
``` git remote add origin https://github.com/d1alekt1k8/rep_iis_lab1.git ```
``` git branch -M main ```
``` git push -u origin main ```

Установка необходимых библиотек

``` pip install matplotlib ```
``` pip install pandas ```
``` pip install seaborn ```
``` pip install numpy ```
``` pip install pickle4 ```

# Описание проекта
Проект посвящён решению задачи классификации цен на мобильные телефоны

Исходные данные: https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification?resource=download

# Запуск
Для запуска проекта необходимо выполнить следующие команды:

``` git clone https://github.com/d1alekt1k8/rep_iis_lab1.git ```

Открыть папку через функцию "Open Folder" в разделе File

Создать виртуальное окружение:
``` python3 -m venv .venv_lr1 ```

Активировать виртуальное окружение:
``` source .venv_lr1/bin/activate ```

Установка зависимостей:
``` pip install -r requirments.txt ```

Установить исходные данные и загрузить в папку ` ./data `

# Исследование данных
Находится в ``` ./eda/eda.ipynb ```

В ходе исследования были проведены действия:

- Признаки, описывающие наличие или отсутствие параметра, переведы в категориальный тип. Например:
``` df['blue'] = df['blue'].astype('category') ```
- Числовые признаки, содержащие небольшой диапазон чисел, получили меньший по объёму тип данных. Например:
``` df['fc'] = df['fc'].astype('int8') ```

- Удалены данные со значением ширины экрана меньше 3 см.
``` df = df.query('sc_w >= 3') ```

- Удалены данные со значением разрешения по высоте меньше 20 пикселей.
``` df = df.query('px_height >= 20') ```

В ходе анализа были выявлены следующие закономерности:

- Среди числовых признаков только у ёмкости аккумулятора наблюдается линейная зависимость с ценой: чем выше ёмкость, тем выше цена. (см график ```./eda/graph1.png```)

- Наличие Wi-Fi уменьшает время возможного разговора по телефону, то есть увеличивает разряд батареи. (см график ```./eda/graph2.png```)
