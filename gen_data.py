#!/usr/bin/env python
"""gen_data.py
generate fake data
"""

from model import Student, Course, Remark

if __name__ == "__main__":
    STUDENTS = [
        Student('ZZY', 'xxx', 'zzy', 'student'),
        Student('GCY', 'yyy', 'gcy', 'student')
    ]

    COURSES = [
        Course('EN.600.424', '2015', 'spring', 'Network Security', 'S. Nielson', 'CORE_TECH', 'This course focuses on communication security in computer systems and networks. The course is intended to provide students with an introduction to the field of network security. The course covers network security services such as authentication and access control, integrity and confidentiality of data, firewalls and related technologies, Web security and privacy. Course work involves implementing various security techniques. A course project is required. [Systems] EN.600.120 (or equivalent) recommended.'),
        Course('EN.650.445', '2015', 'spring', 'Practical Cryptographic Systems', 'M. Green', 'CORE_TECH', 'This semester long course will teach skill of how cryptographic systems work and fail - as part of a complete hardware and software system. The skills will be taught by examples I.e., by studyng and identifying flows in widely deployed crypto systems. We will place a particular emphasis on the failure of "security by obscurity" and the feasibility of reverse-engineering undocumented crypto systems. Co-listed with EN.600.454.')
    ]

    REMARKS = [
        Remark('ZZY', 'EN.600.424', '2015', 'spring', 'Nice course!'),
        Remark('GCY', 'EN.650.445', '2015', 'spring', 'This is easy!')
    ]

    # for student in STUDENTS:
    #     student.register()

    # for course in COURSES:
    #     course.register()

    for remark in REMARKS:
        remark.post()
