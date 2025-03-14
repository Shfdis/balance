# В этом репозитории разрабатывался Back-end
Репозитории с:
1. [Business-панелью](https://github.com/Ariabochkina/frontend2)
2. [Формой опроса](https://github.com/Ariabochkina/frontend1)
# Balance

Серверное приложение, предоставляющее услуги автоматического изменения рецептов под предпочтения клиентов. Подойдёт под
любой бизнес, изготавливающий еду или напитки не из заготовок.

## Что мы предоставляем

### Что получит клиент?

После каждой покупки пользователь получает форму из небольшого числа вопросов. Каждый вопрос - шкала, насколько гость
предпочёл бы ослабить или усилить некоторую вкусовую характеристику. После заполнения формы рецепт изменяется под него
автоматически, и со следующим продуктом он получит адаптированный под него вкус.

### Что получает бизнес?

Форму для редактирования вышеуказанного опросника, отдельную для каждого продукта. Менеджер формы указывает коэфициенты,
насколько каждый из параметров во время приготовление влияет на заданные вкусовые характеристики.

## Как это работает?

Мы исходим из предположения, что вкусовые предпочтения клиента - унимодальная функция над пространством из отдельных
вкусовых характеристик(сладость, соленость, горечь, кислотность, температура, концентрированность вкуса и т. д.). Для
поиска максимального значения таких функций идеально подходит градиентный спуск. Но что же такое градиент для
предпочтений клиента? То насклолько он бы изменил каждую вкусовую характеристику, то есть результат собранного нами
опросника.

## Формат конфигурации рецепта

JSON-файл содержит:

Поле name, содержащее название рецепта

Поле tastes, содержащее вкусовые характеристики

Поле default_measures с полями ингридиентов и их дефолтных значений.

Поле change_coefficients с полями ингридиентов, содержащих поля вкусовых характеристик и соответствующих им коэфициентов.

## Формат опросника

JSON-файл содержит:
поле changes - словарь, содержащий поля вкусов, которым соответствуют коефициенты изменения от -0.1 до 0.1

## Функциональные требования

1. Добавление рецепта напитка пользователем
2. Создание формы опроса пользователя для заказчика
3. Изменение бизнесом коэфициентов влияния ингридиентов на вкус напитка через бизнес-панель
4. Добавление бизнесом нового рецепта
5. Принятие и обработка результатов опроса
6. Показ кастомизированного рецепта исполнителю заказа
7. Авторизация бизнеса в системе
8. Предоставление удобного API бизнесу

   
## Архитектура

### Взаимодействие компонентов:

- Бизнес редактирует общие рецепты и коэфициенты изменения при помощи business панели.
- Бизнес может добавлять новые рецепты пользователей с помощью API.
- После приобретения элемента меню некоторым пользователем, бизнес может запросить генерацию токена формы изменения рецепта, после первого её заполнения токен аннулируется и заполнение становится невозможным.
- Бизнес может получить данные о рецепте c помощью API.
  ![Architecture](architecture.jpg)
## Запросы к API бизнеса
- POST, GET /usersRecipes/<user_id>/<recipe_id> - создание и получение рецепта пользователя
- GET /usersToken - генерация формы опронсика и соответствующего ей токена(с параметрами user_id и recipe_id)
- GET /tastes/<recipe_id> - получение всех вкусовых характеристик рецепта
- POST /submit/<token> - отправка формы с последующим изменением рецепта пользователя
## Фронтенд
- на порту 3002 размещен редактор рецептов. Для входа: :3002/login
- на порту 3001 формы с опросами. Для достпа передать параметры token и recipe_id
### Демонстрация функционала
https://disk.yandex.ru/i/mr6iN2WnrF1sFg
