# Generated by Django 2.1.5 on 2019-06-04 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='퀴즈 푼 날짜')),
                ('myAnswer', models.CharField(max_length=1, verbose_name='회원 답')),
            ],
            options={
                'verbose_name': '회원퀴즈',
                'verbose_name_plural': '회원퀴즈',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='퀴즈내용')),
                ('answer', models.CharField(max_length=1, verbose_name='답')),
            ],
            options={
                'verbose_name': '퀴즈',
                'verbose_name_plural': '퀴즈',
            },
        ),
        migrations.CreateModel(
            name='QuizSub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='퀴즈주제')),
                ('photo', models.ImageField(null=True, upload_to='quiz/quizSub_img/', verbose_name='사진')),
            ],
            options={
                'verbose_name': '퀴즈주제',
                'verbose_name_plural': '퀴즈주제',
            },
        ),
    ]
