#!/usr/bin/env python
"""model.py
Defines classes corresponding to the schema.sql
"""

import web
import config

DB = web.database(
    dbn=config.DB_TYPE,
    db=config.DB_NAME,
    user=config.DB_USER,
    pw=config.DB_PASSWORD)

class Student(object):
    """Student entity"""
    def __init__(self, username):
        self.username = username

    def check_password(self, hashed_password):
        """check the password"""
        pass

    def update_password(self, hashed_password):
        """update password"""
        pass

class Course(object):
    """Course entity"""
    def __init__(self, course_no, year, semester):
        self.course_no = course_no
        self.year = year
        self.semester = semester

    def fetch_data(self):
        """get course's data"""
        pass

    def fetch_comment(self):
        """get course's comments"""
        pass

class Combo(object):
    """Combo entity"""
    def __init__(self, combo_id):
        self.combo_id = combo_id

    def fetch_data(self):
        """get combo's data"""
        pass

    def fetch_courses(self):
        """get the courses that this combo contains"""
        pass

class Remark(object):
    """Remark entity"""
    def __init__(self, username, course_no, year, semester):
        self.username = username
        self.course_no = course_no
        self.year = year
        self.semester = semester

    def edit(self):
        """edit a remark"""
        pass

    def remove(self):
        """remove a remark"""
        pass
