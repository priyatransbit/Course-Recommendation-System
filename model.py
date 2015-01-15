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
    PRIORITY = ['admin', 'student']

    def __init__(self, username, hashed_password, nickname, priority):
        self.username = username
        self.hashed_password = hashed_password
        self.nickname = nickname
        assert(priority in self.PRIORITY), "invalid priority"
        self.priority = priority

    def register(self):
        """register as a new user"""
        DB.insert(config.TB_STUDENT,
                  username=self.username,
                  password=self.hashed_password,
                  nickname=self.nickname,
                  priority=self.priority)

    def check_password(self, hashed_password):
        """check the password"""
        pass

    def update_password(self, hashed_password):
        """update password"""
        pass

class Course(object):
    """Course entity"""
    CATEGORY = ['CORE_TECH',
                'ELEC_TECH',
                'CORE_POL',
                'CORE_MAN',
                'FOUN_MAN',
                'CORE_HEAL',
                'ELEC_PHM']
    SEMESTER = ['fall', 'spring']

    def __init__(self, course_no, year, semester, name, professor, category, description):
        self.course_no = course_no
        self.year = year
        assert(semester in self.SEMESTER), "invalid semester"
        self.semester = semester
        self.name = name
        self.professor = professor
        assert(category in self.CATEGORY), "invalid category"
        self.category = category
        self.description = description

    def register(self):
        """register a course"""
        DB.insert(config.TB_COURSE,
                  course_no=self.course_no,
                  year=self.year,
                  semester=self.semester,
                  name=self.name,
                  professor=self.professor,
                  category=self.category,
                  description=self.description)


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
    def __init__(self, username, course_no, year, semester, content):
        self.username = username
        self.course_no = course_no
        self.year = year
        assert(semester in Course.SEMESTER), "invalid semester"
        self.semester = semester
        self.content = content

    def post(self):
        """post a comment"""
        DB.insert(config.TB_REMARK,
                  username=self.username,
                  course_no=self.course_no,
                  year=self.year,
                  semester=self.semester,
                  content=self.content)

    def edit(self):
        """edit a remark"""
        pass

    def remove(self):
        """remove a remark"""
        pass
