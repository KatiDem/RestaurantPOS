from django.db import models
import datetime


class Table(models.Model):
    name = models.CharField('Table name', max_length=30, unique=True)
    is_available = models.BooleanField('Status', default=False, help_text='If the table is free-True, busy-False')

    class Meta:
        verbose_name = 'Стол'
        verbose_name_plural = 'Столы'
        ordering = ['is_available']

    def __str__(self):
        return self.name_table


class MenuItem(models.Model):

    APPETIZERS = 'AP'
    COLD_PLATTER = 'CP'
    HOT_APPETIZERS = 'HA'
    STARTERS = 'ST'
    SOUPS = 'SO'
    SALADS = 'SA'
    MAIN_DISHES = 'MD'
    MEAT = 'ME'
    STEAK = 'SE'
    POULTRY_DISHES = 'PD'
    FISH_AND_SEAFOODS = 'FS'
    SIDES = 'SI'
    SNACKS = 'SN'
    SAUCES = 'SU'
    DESSERTS = 'DE'
    BEVERAGES = 'BE'
    SOFT_DRINKS = 'SD'
    HOT_DRINKS = 'HD'
    WINE_LIST = 'WL'
    CATEGORY_CHOISES = [
        (APPETIZERS, 'закуски'),
        (COLD_PLATTER, 'холодные закуски'),
        (HOT_APPETIZERS, 'горячие закуски'),
        (STARTERS, 'первые блюда'),
        (SOUPS, 'супы'),
        (SALADS, 'салаты'),
        (MAIN_DISHES, 'основные блюда'),
        (MEAT, 'блюда из мяса'),
        (STEAK, 'стейки'),
        (POULTRY_DISHES, 'блюда из птицы'),
        (FISH_AND_SEAFOODS, 'морепродукты'),
        (SIDES, 'гарниры'),
        (SNACKS, 'закуски'),
        (SAUCES, 'соусы'),
        (DESSERTS, 'десерты'),
        (BEVERAGES, 'напитки'),
        (SOFT_DRINKS, 'прохладительные напитки'),
        (HOT_DRINKS, 'горячие напитки'),
        (WINE_LIST, 'винная карта'),
    ]

    name = models.CharField('Название блюда',max_length=100)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    description = models.TextField('Описание', max_length=1000)
    category = models.CharField('Категории', max_length=2, choices=CATEGORY_CHOISES)
    #calories = models.IntegerField('Колличество калорий', default=0, null=True, blank=True)
    #serving_weight = models.PositiveIntegerField('Вес порции', default=0)
    #business_lunch = models.BooleanField('Бизнес ланч', default=False)
    #image = models.ImageField('Фото блюда', null=True, blank=True)
    #comment = models.CharField('Комментарий', max_length=150, null=True, blank=True)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='MenuItem', verbose_name='Пункт меню')
    quantity = models.PositiveSmallIntegerField('Колличество')
    total_price = models.DecimalField('Общая стоимость', max_digits=5, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.total_price = self.get_price()
        super(OrderItem, self).save(*args, **kwargs)

    def get_price(self):
        return self.menu_item.price * self.quantity

    def __str__(self):
        return "%sx %s" % (self.quantity, self.menu_item)


class Order(models.Model):
    number = models.CharField('Номер заказа', max_length=100,  null=True, blank=True, unique=True)
    # waiter = models.ForeignKey('Waiter', on_delete=models.CASCADE, verbose_name='Waiter')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name='Стол')
    number_of_guests = models.PositiveSmallIntegerField('Количество гостей', default=1)
    items = models.ManyToManyField(OrderItem)
    cost = models.DecimalField('Сумма за весь заказ', max_digits=5, decimal_places=2, null=True, blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа', null=True, blank=True)
    dish_is_ready = models.BooleanField('Отметка о готовности заказа на кухне', default=False)
    time_dish_is_ready = models.CharField('Время приготовления заказа', max_length=10, null=True, blank=True)
    comment = models.CharField('Комментарий', max_length=250, null=True, blank=True)
    cancelled = models.BooleanField('Заказ отменен', default=False)
    paid = models.BooleanField('Заказ оплачен', default=False)

    def save(self, *args, **kwargs):
        order = Order()
        self.cost = 0
        if self.dish_is_ready:
            self.time_dish_is_ready = datetime.datetime.today().strftime("%H:%M:%S")
        if not self.id:
            super(Order, self).save(*args, **kwargs)
        self.number = f'{str(self.id)}-{datetime.datetime.today().strftime("%d.%m.%Y")}'
        self.cost = self.get_total()
        return super(Order, self).save(*args, **kwargs)

    def get_total(self):
        return sum([order_item.get_price() for order_item in self.items.all()])

    def __str__(self):
        return str(self.number)




