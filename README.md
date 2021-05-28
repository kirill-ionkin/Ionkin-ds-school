# Школа Data Science от Сбербанка

Данный репозиторий является кратким, структурированным конспектом изучаемого
материала в процессе обучения
в школе Data Science от Сбербанка


## Оглавление

Материалы(презентации, juputer notebooks, etc. в папке materials)

- 0 [Организационное собрание](#Организационное-собрание)
- 1 [Основные инструменты и процесс разработки](#Основные-инструменты-и-процесс-разработки)
- 2 [Написание надёжного поддерживаемого кода на Python](#Написание-надёжного-поддерживаемого-кода-на-Python)
- 3 [Профилирование и оптимизация кода на Python](#Профилирование-и-оптимизация-кода-на-Python)
- 4 [Визуализация данных.](#Визуализация-данных)
- 5 [Математика для ML. Часть 1: Методы оптимизации](#Математика-для-ML-Часть-1:-Методы-оптимизации)
- 6 [Математика для ML. Часть 2: Вычислительная линейная алгебра](#Математика-для-ML-Часть-2:-Вычислительная-линейная-алгебра)
- 7 [Математика для ML. Часть 3: Прикладная теория вероятностей](#Математика-для-ML-Часть-3:-Прикладная-теория-вероятностей)
- 8 [Математика для ML. Часть 4: Математическая статистика]()

- [other](#other)
- [ссылка на плейлист с лекциями](https://www.youtube.com/playlist?list=PLNxGMRiN2-zX_fNnpFandY8jmCFu6mVYa)


## Организационное собрание

- [00_Organisational.pdf](./materials/0_Организационное_собрание/00_Organisational.pdf)

1. [Leetcode](https://leetcode.com/)
2. [Kaggle](https://www.kaggle.com/kirillionkin)
3. [LinkedIn](https://www.linkedin.com/in/%D0%BA%D0%B8%D1%80%D0%B8%D0%BB%D0%BB-%D0%B8%D0%BE%D0%BD%D0%BA%D0%B8%D0%BD-50a992209/)

## Основные инструменты и процесс разработки

- [01_Developers_Tools.pdf](materials/1_Основные_инструменты_и_процесс_разработки/01_Developers_Tools.pdf)

1. PyCharm([сслыка на скачивание](https://www.jetbrains.com/ru-ru/pycharm/))
    - [линтер Flake8](https://flake8.pycqa.org/en/latest/#)
    - [форматтер Black](https://black.readthedocs.io/en/stable/)
        - [настройка Black в PyCharm(видео)](https://www.youtube.com/watch?v=dxFsjgtyAHw&t=6s&ab_channel=FedericoTartarini)
    - [pre-commit](https://pre-commit.com/)
        - [настройка pre-commit hooks(видео)](https://www.youtube.com/watch?v=Wmw-VGSjSNg&ab_channel=SoftwareEngineerHaydn)

2. Git
    - [Книга Git(обязательна к прочтению)](https://git-scm.com/book/ru/v2)
    - [Онлайн практика с визуализацией работы веток](https://git-school.github.io/visualizing-git/)
    - [Практика GIT(небольшой тренажёр)](https://learngitbranching.js.org/?locale=ru_RU)
    - ["Чёрт побери, GIT!"](https://dangitgit.com/ru)
    - [README.md - markdown syntax](https://github.com/GnuriaN/format-README#%D0%9E%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


## Написание надёжного поддерживаемого кода на Python

- [02_Testing_And_Profiling.pdf](./materials/2_Написание_надёжного_поддерживаемого_кода_на_Python/02_Testing_And_Profiling.pdf)
- [02_Testing.ipynb](./materials/2_Написание_надёжного_поддерживаемого_кода_на_Python/02_Testing.ipynb)

1. PyTest([библиотека для тестирования кода](https://docs.pytest.org/en/stable/contents.html))

2. MyPy([type hints - статический анализатор кода](https://mypy.readthedocs.io/en/stable/))
    - [Лекция от JetBrains про type hints в PyCharm](https://www.youtube.com/watch?v=JqBCFfiE11g&ab_channel=JetBrainsTV)
    - [Перевод мастер-класса по MyPy от разработчика Instagram](https://medium.com/@nooovikov/mypy-c03a3174ae7d)
        - [MonkeyType - auto annotations]()


## Профилирование и оптимизация кода на Python

- [03_Profiling_and_optimizing.pdf](./materials/3_Профилирование_и_оптимизация_кода_на_Python/03_Profiling_and_optimizing.pdf)
- [3_Profiling.ipynb](./materials/3_Профилирование_и_оптимизация_кода_на_Python/3_Profiling.ipynb)
- [3_Optimisation_(solved).ipynb](./materials/3_Профилирование_и_оптимизация_кода_на_Python/3_Optimisation_(solved).ipynb)

1. Профилирование - поиск "узких" мест в коде(в Python реализован динамический анализ производительности кода).
    - встроенные средства профилирования в PyCharm:
        - [ссылка](https://www.jetbrains.com/help/pycharm/profiler.html)
        - [ссылка](https://www.jetbrains.com/help/pycharm/v8-cpu-and-memory-profiling.html)
    - Анализ времени работы
        - Явное профилирование строки / ячейки кода в Jupyter
            - `%timeit` - позволяет измерить время исполнения одной строки
            - `%timeit -n ... ...` - запуск строчки несколько раз
            - `%%timeit` - позволяет измерить время исполнения целой ячейки с кодом(запустит её несколько раз)
            - `%%time` - позволяет измерить время исполения ячейки(запустит её один раз)
        - [line profiler](https://github.com/pyutils/line_profiler)
            позволяет замерить время, приходящееся на каждую строчку кода.
            Запускается через %lprun или kernprof -lv my_file.py
            после навешивания @profile на все нужные функции.
    - Анализ количества потребляемой памяти
        - [memory_profiler](https://github.com/pythonprofilers/memory_profiler)
            аналогичен line_profiler и позволяет измерить общее и
            построчное потребление памяти программой

2. JIT - компиляция(как писать на Python циклы, за которые не стыдно)
    - [Numba](https://numba.pydata.org/)
        ![](materials/3_Профилирование_и_оптимизация_кода_на_Python/numba_screen.png)
        Numba это jit-компилятор Python, т.е. динамический компилятор,
        который по запросу транслирует функции в байт-код,
        к которому потом обращаются последующие вызовы функции.
        Прирост производительности при этом обеспечивается за счёт того,
        что интерпретатору больше не нужно выполнять тело функции построчно,
        проверять, на что указывает каждое имя в коде и т.д.
        Python — динамически типизированный интерпретируемый язык, потому далеко не весь
        его функционал можно jit-компилировать, но то подмножество, которое
        используется для решения вычислительных задачи, чаще всего компилировать можно.
        - `@numba.jit(nopython=True)`


## Визуализация данных

- [04_Visualisation.pdf](./materials/4_Визуализация_данных/04_Visualisation.pdf)
- [seaborn.ipynb](./materials/4_Визуализация_данных/seaborn.ipynb)
- [plotly.ipynb](./materials/4_Визуализация_данных/plotly.ipynb)

1. Статические визуализации
    - [Matplotlib](https://matplotlib.org/index.html)
    - [Seaborn](https://seaborn.pydata.org/#)
    - [галлерея статических графиков Python](https://www.python-graph-gallery.com/)

2. Интерактивные визуализации
    - [Plotly](https://plotly.com/python/)


## Математика для ML Часть 1: Методы оптимизации

- [05_Calculus_and_Optimisation.pdf](./materials/5_Математика_для_ML(Методы_оптимизации)/05_Calculus_and_Optimisation.pdf)
- [Методичка по матричному дифференцированию](./materials/5_Математика_для_ML(Методы_оптимизации)/Методичка%20по%20матричному%20дифференцированию.pdf)

1. Дифференциальное исчисление
2. Методы оптимизации(методы первого порядка для решения задач безусловной непрерывной оптимизации)
    - Градиентный спуск
    ![](./materials/5_Математика_для_ML(Методы_оптимизации)/1.png)
    - [Cтохастический градиентный спуск](https://paperswithcode.com/paper/on-the-almost-sure-convergence-of-stochastic)
    ![](./materials/5_Математика_для_ML(Методы_оптимизации)/2.png)
    - Momentum
    ![](./materials/5_Математика_для_ML(Методы_оптимизации)/3.png)
    - RMSProp
    ![](./materials/5_Математика_для_ML(Методы_оптимизации)/4.png)
    - Adam
    ![](./materials/5_Математика_для_ML(Методы_оптимизации)/5.png)
    - [А как подбирать длину шага?](https://github.com/amkatrutsa/optimization-fivt/blob/master/07-GD/lecture7.pdf)
    ![](./materials/5_Математика_для_ML(Методы_оптимизации)/6.png)
    - [Сравнение методов первого порядка](https://habr.com/ru/post/318970/)
    ![](./materials/5_Математика_для_ML(Методы_оптимизации)/gif.gif)

## Математика для ML Часть 2: Вычислительная линейная алгебра

- [06_Numerical_Linear_Algebra.pdf](./materials/6_Математика_для_ML(Вычислительная_линейная_алгебра)/06_Numerical_Linear_Algebra.pdf)


## Математика для ML Часть 3: Прикладная теория вероятностей

- [07_Applied_Probability_Theory.pdf](./materials/7_Математика_для_ML(Прикладная_теория_вероятностей)/07_Applied_Probability_Theory.pdf)

## other

- [to-jupyter-and-back.pdf](./materials/other/to-jupyter-and-back.pdf)
