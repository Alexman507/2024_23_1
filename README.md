## Настройка проекта
После клонирования введите следующие команды (на винде, для другой системы команды отличаются) в консоли в папке проекта:

`python -m venv venv`

`venv/scripts/activate`

`pip install -r requirements.txt`

Не забудьте активировать миграции, чтобы связи с БД работали:

`python manage.py migrate`

Для загрузки настроенных групп и разрешений:

`python manage.py loaddata data/groups.json`

Также можно подгрузить пользователей:

`python manage.py loaddata data/users.json`


## Задание 1 (+)

Создайте группу для роли модератора и опишите необходимые доступы:

- может отменять публикацию продукта,
- может менять описание любого продукта,
- может менять категорию любого продукта.

Группу создавайте в админке. Права доступа для продуктов опишите в модели продукта и назначьте группе через админку. Не забудьте сохранить группы фикстурой или создать команду для создания групп для отправки наставнику на проверку.
`python -Xutf8 manage.py dumpdata auth.permission --indent 2 --output data/groups.json`, 

то же самое сделал с группами, потом вручную переложил в groups.json

Примечание

Недостающее поле признака публикации необходимо добавить таким образом, чтобы можно было определять статус продукта. Можно использовать `BooleanField` со значением `False` по умолчанию или `CharField` с указанием вариантов значений (`choises`). При этом по умолчанию должен быть вариант, который не предполагает публикации продукта.

Подсказка

Проверяйте права, которые назначены пользователю в контроллерах или шаблонах. Данные об авторизованном пользователе хранятся в объекте `request.user`. Получить права пользователя в контроллере можно с помощью метода `has_perm()`. При необходимости проверки прав доступа в шаблонах для отображения, например, кнопок в зависимости от роли пользователя необходимо использовать `{{ perms }}`. Документацию по использованию можно найти [здесь.](https://docs.djangoproject.com/en/5.0/topics/auth/default/#permissions)

## Задание 2 (+)

Реализуйте решение, которое проверит, что редактирование продукта доступно только его владельцу.

Внедрите в шаблоны проверку на владельца объекта и отображайте кнопки редактирования только пользователям, которые являются владельцами (если пользователь не наделен другими правами).

### Дополнительное задание (+-)

Выделите отдельную роль для пользователя — контент-менеджера, который может управлять публикациями в блоге. Также не забудьте реализовать проверки на то, что обычный пользователь или модератор из другого отдела не сможет ничего изменить в разделе блога.









