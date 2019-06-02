# Generated by Django 2.1.5 on 2019-06-02 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='작성일시')),
                ('hits', models.IntegerField(default=0, verbose_name='조회수')),
            ],
            options={
                'verbose_name': '게시판',
                'verbose_name_plural': '관리자 게시판',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='분류')),
            ],
            options={
                'verbose_name': '분류',
                'verbose_name_plural': '게시판 분류',
            },
        ),
        migrations.CreateModel(
            name='DonationOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='기부단체명')),
                ('desc', models.TextField(verbose_name='단체설명')),
                ('photo', models.ImageField(upload_to='staff/donation/', verbose_name='사진')),
                ('url', models.URLField(max_length=250, verbose_name='홈페이지 주소')),
                ('is_donate', models.BooleanField(default=False, verbose_name='이달 기부단체')),
            ],
            options={
                'verbose_name': '기부단체',
                'verbose_name_plural': '기부단체',
            },
        ),
        migrations.CreateModel(
            name='QnA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='제목')),
                ('question', models.TextField(verbose_name='질문')),
                ('answer', models.TextField(null=True, verbose_name='답변')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='작성일시')),
            ],
            options={
                'verbose_name': '질문',
                'verbose_name_plural': '질문 게시판',
                'ordering': ['-date'],
            },
        ),
    ]
