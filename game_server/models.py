# coding: utf-8
from django.db import models
from django.utils.six import python_2_unicode_compatible

@python_2_unicode_compatible
class Player(models.Model):
    # verbose_name为在django后台显示的字段名称
    playerid = models.CharField(max_length=10, unique=True, verbose_name='玩家ID')
    playername = models.CharField(max_length=10, unique=True, verbose_name='玩家姓名')
    level = models.PositiveIntegerField(verbose_name='玩家等级')
    experience = models.PositiveIntegerField(verbose_name='玩家经验')
    # auto_now_add=True为只记录首次创建时间
    regtime = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')

    def __str__(self):
        return self.playerid

@python_2_unicode_compatible
class Player_gold_log(models.Model):
    # 因为一个玩家对应多条金币变化记录，所以用ForeignKey，而不是用OneToOneField
    playerid = models.ForeignKey(Player, verbose_name='玩家ID')
    serverid = models.CharField(max_length=10, verbose_name='服务器ID')
    gold_change = models.IntegerField(verbose_name='金币变化数量')
    gold = models.PositiveIntegerField(verbose_name='金币剩余数量')
    gold_change_time = models.DateTimeField(verbose_name='金币变化时间')

