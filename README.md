## Flask project

### Для развертывания проекта на локальной машине необходимо выполнить следующие требования:
* Установить python 3.11.1
* Установить последнюю версию Pipenv
* Создать файл .env с переменными окружения по образцу env.md

### Настройка окружения:
* В консоли выполняем команду pipenv sync --verbose
* Выбираем интерпретатор созданного виртуального окружения в качестве основного для данного проекта (папка с виртуальным окружением будет автоматически создана либо в репозитории проекта, либо в директории Users\User\\.virtualenvs)
* В случае использования VS Code запускаем конфигурацию дебага python: Flask. В случае использования PyCharm необходимо настроить конфигурацию дебага по аналогии (конфигурацию можно найти в launch.json)