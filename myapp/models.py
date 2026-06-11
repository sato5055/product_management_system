from django.db import models

# Create your models here.
class Account_User(models.Model):
    class Meta:
        db_table = "account_user"

    user_id = models.CharField(verbose_name="会員ID", max_length=128, primary_key = True)
    password = models.CharField(verbose_name="パスワード", max_length=256)
    name = models.CharField(verbose_name="名前", max_length=128)
    address = models.CharField(verbose_name="住所", max_length=256)
    
class Shopping_Category(models.Model):
    class Meta:
        db_table = "shopping_category"
    
    category_id = models.IntegerField(verbose_name="カテゴリID", primary_key = True)
    name = models.CharField(verbose_name="カテゴリ名", max_length=256)


class Shopping_Item(models.Model):
    class Meta:
        db_table = "shopping_item"

    item_id = models.IntegerField(verbose_name="商品ID", primary_key = True)
    name = models.CharField(verbose_name="商品名", max_length=128)
    manufacturer = models.CharField(verbose_name="メーカー名", max_length=32)
    color = models.CharField(verbose_name="商品の色", max_length=16)
    price = models.IntegerField(verbose_name="価格")
    stock = models.IntegerField(verbose_name="在庫数")
    recommended = models.BooleanField(verbose_name="オススメ", default = False, max_length=1)
    category_id = models.IntegerField(verbose_name="カテゴリID")


class Shopping_Itemsincart(models.Model):
    class Meta:
        db_table = "Shopping_Itemsincart"

    #id = models.IntegerField(verbose_name="ID", primary_key = True)
    amount = models.IntegerField(verbose_name="数量")
    booked_date = models.DateTimeField(verbose_name="登録日", auto_now_add=True)

    item = models.ForeignKey(Shopping_Item, verbose_name="商品ID", on_delete=models.CASCADE)
    user = models.ForeignKey(Account_User, verbose_name="会員ID", max_length=128, on_delete=models.CASCADE)

class Shopping_Purchase(models.Model):
    class Meta:
        db_table = "Shopping_Purchase"

    purchase_id = models.IntegerField(verbose_name="注文ID", primary_key = True)
    destination = models.CharField(verbose_name="配送先", max_length=256)
    booked_date = models.DateTimeField(verbose_name="注文日", auto_now_add=True)
    cancel = models.BooleanField(verbose_name="キャンセル", max_length=1, default=False)
    user = models.ForeignKey(Account_User, verbose_name="注文者", max_length=128, on_delete=models.CASCADE)


class Shopping_Purchasedetail(models.Model):
    class Meta:
        db_table = "Shopping_Purchasedetail"

    purchase_detail_id = models.IntegerField(verbose_name="注文詳細ID", primary_key = True)
    amount = models.IntegerField(verbose_name="注文数")
    item = models.ForeignKey(Shopping_Item, verbose_name="商品ID", on_delete=models.CASCADE)
    purchase = models.ForeignKey(Shopping_Purchase, verbose_name="注文ID", on_delete=models.CASCADE)

class Administrator_Admin(models.Model):
    class Meta:
        db_table = "Administrator_Admin"

    admin_id = models.CharField(verbose_name = "管理者ID", primary_key=True, max_length=128)
    password = models.CharField(verbose_name = "パスワード", max_length=256)
