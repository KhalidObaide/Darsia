from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=999999)
    username = models.CharField(max_length=999999)
    bio = models.CharField(max_length=9999999)
    email = models.CharField(max_length=999999)
    password = models.CharField(max_length=999999)
    profile_image = models.CharField(max_length=999999)
    time_created = models.CharField(max_length=999999)
    does_payed = models.CharField(max_length=999999)
    courses_took = models.CharField(max_length=999999)
    liked_courses = models.CharField(max_length=999999)
    paying_times = models.CharField(max_length=999999)
    total_times_payed = models.CharField(max_length=999999)
    total_payed_money = models.CharField(max_length=999999)
    last_pay_money = models.CharField(max_length=999999)
    first_pay_money = models.CharField(max_length=999999)
    bank_added_time = models.CharField(max_length=999999)
    bank_name  = models.CharField(max_length=999999)
    bank_number = models.CharField(max_length=999999)
    bank_cvc = models.CharField(max_length=999999)
    bank_date = models.CharField(max_length=999999)
    last_charge = models.CharField(max_length=999999)
    wallet = models.CharField(max_length=999999)

    def __str__(self):
        return self.username


class Timed_User(models.Model):
    name = models.CharField(max_length=999999)
    username = models.CharField(max_length=9999999)
    email = models.CharField(max_length=999999)
    password = models.CharField(max_length=999999)
    time_created = models.CharField(max_length=999999)
    url = models.CharField(max_length=9999999)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=999999)
    username = models.CharField(max_length=999999)
    bio = models.CharField(max_length=9999999)
    email = models.CharField(max_length=999999)
    password = models.CharField(max_length=999999)
    profile_img = models.CharField(max_length=999999)
    time_created = models.CharField(max_length=999999)
    courses_made = models.CharField(max_length=999999)
    amount_earned_total = models.CharField(max_length=999999)
    amount_earned_last = models.CharField(max_length=999999)
    amount_earned_first = models.CharField(max_length=999999)
    bank_name = models.CharField(max_length=999999)
    bank_number = models.CharField(max_length=999999)
    most_course_ben = models.CharField(max_length=999999)
    baddest_course_ben = models.CharField(max_length=999999)
    middle_course_ben = models.CharField(max_length=999999)
    last_money_took = models.CharField(max_length=999999)
    first_money_took = models.CharField(max_length=999999)
    students_got = models.CharField(max_length=999999)
    best_course_students = models.CharField(max_length=999999)
    baddest_course_students = models.CharField(max_length=999999)

    def __str__(self):
        return self.username


class Course(models.Model):
    name = models.CharField(max_length=999999)
    bio = models.CharField(max_length=999999)
    img = models.CharField(max_length=999999)
    tags = models.CharField(max_length=999999)
    price = models.CharField(max_length=999999)
    starts = models.CharField(max_length=999999)
    sub_titles = models.CharField(max_length=999999)
    videos = models.CharField(max_length=999999)
    time_created = models.CharField(max_length=999999)
    teacher = models.CharField(max_length=999999)
    students = models.CharField(max_length=999999)
    reviews = models.CharField(max_length=999999)
    permission = models.CharField(max_length=999999)
    best_raise_time = models.CharField(max_length=999999)
    baddest_raise_time = models.CharField(max_length=999999)

    def __str__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(max_length=999999)
    bio = models.CharField(max_length=9999999)
    course = models.CharField(max_length=999999)
    sub_title = models.CharField(max_length=999999)
    url = models.CharField(max_length=999999)
    video_long_time = models.CharField(max_length=999999)
    reviews = models.CharField(max_length=999999)
    status = models.CharField(max_length=999999)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.CharField(max_length=99999)
    bio = models.TextField(max_length=99999)
    time_added = models.CharField(max_length=99999)
    user_img = models.CharField(max_length=99999)
    status = models.CharField(max_length=99999)
    views = models.CharField(max_length=99999)

    def __str__(self):
        return self.user


class Bank(models.Model):
    owner = models.CharField(max_length=999999)
    bank_name = models.CharField(max_length=999999)
    bank_number = models.CharField(max_length=999999)
    bank_date = models.CharField(max_length=999999)
    bank_cvc = models.CharField(max_length=999999)
    bank_added_time = models.CharField(max_length=999999)
    bank_most_spent = models.CharField(max_length=999999)
    bank_lest_spent = models.CharField(max_length=999999)

    def __str__(self):
        return self.bank_name


class Why_darsia(models.Model):
    title = models.CharField(max_length=99999)
    bio = models.TextField(max_length=999999)
    img = models.CharField(max_length=99999)
    time_added = models.CharField(max_length=99999)
    status = models.CharField(max_length=99999)

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    email = models.CharField(max_length=999999)
    time_created = models.CharField(max_length=999999)
    status = models.CharField(max_length=999999)
    is_user = models.CharField(max_length=999999)

    def __str__(self):
        return self.email


class Url(models.Model):
    name = models.CharField(max_length=9999999)
    url = models.CharField(max_length=9999999)

    def __str__(self):
        return self.name


class Simple_Data(models.Model):
    name = models.CharField(max_length=9999999)
    data = models.CharField(max_length=9999999)

    def __str__(self):
        return self.name