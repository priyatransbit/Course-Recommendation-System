  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  nickname VARCHAR(255) NOT NULL,
  priority ENUM('admin', 'student') NOT NULL,
  registration_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  is_online BIT(1) NOT NULL DEFAULT FALSE,
  PRIMARY KEY (username)
);

CREATE TABLE IF NOT EXISTS course (
  course_no VARCHAR(255) NOT NULL,
  year  YEAR(4) NOT NULL,
  semester ENUM('fall', 'spring') NOT NULL,
  name  VARCHAR(255) NOT NULL,
  professor VARCHAR(255) NOT NULL,
  category ENUM('CORE_TECH', 'ELEC_TECH', 'CORE_POL', 'CORE_MAN', 'FOUN_MAN','CORE_HEAL', 'ELEC_PHM'),
  description TEXT NOT NULL,
  PRIMARY KEY (course_no, year, semester)
);

CREATE TABLE IF NOT EXISTS combo (
  combo_id INT NOT NULL AUTO_INCREMENT,
  year YEAR(4) NOT NULL,
  semester ENUM('fall', 'spring') NOT NULL,
  description TEXT NOT NULL,
  PRIMARY KEY (combo_id)
);

CREATE TABLE IF NOT EXISTS remark (
  remark_id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  course_no VARCHAR(255) NOT NULL,
  year  YEAR(4) NOT NULL,
  semester ENUM('fall', 'spring') NOT NULL,
  time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  content TEXT NOT NULL,
  thumbup INT NOT NULL DEFAULT 0,
  PRIMARY KEY (remark_id, username, course_no, year, semester),
  FOREIGN KEY (username) REFERENCES student(username) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (course_no, year, semester) REFERENCES course(course_no, year, semester) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS combo_contain (
  combo_id INT NOT NULL AUTO_INCREMENT,
  course_no VARCHAR(255) NOT NULL,
  year  YEAR(4) NOT NULL,
  semester ENUM('fall', 'spring') NOT NULL,
  PRIMARY KEY (combo_id, course_no, year, semester),
  FOREIGN KEY (combo_id) REFERENCES combo(combo_id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (course_no, year, semester) REFERENCES course(course_no, year, semester) ON DELETE CASCADE ON UPDATE CASCADE
);
