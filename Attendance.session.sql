-- @block
CREATE TABLE `info`(
  `no` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `img` varchar(255) DEFAULT NULL,
  `position` varchar(55) DEFAULT NULL,
  `contact` varchar(55) DEFAULT NULL,
  `resume` varchar(255) DEFAULT NULL,
  `skill1` varchar(25) DEFAULT NULL,
  `skill2` varchar(25) DEFAULT NULL,
  `skill3` varchar(25) DEFAULT NULL,
  `skill4` varchar(25) DEFAULT NULL,
  `skill5` varchar(25) DEFAULT NULL,
  `about` text ,
  `linkedin` varchar(90) DEFAULT NULL,
  `fb` varchar(55) DEFAULT NULL,
  `insta` varchar(55) DEFAULT NULL,
  `twt` varchar(55) DEFAULT NULL,
  `exp` int(11) DEFAULT NULL,
  PRIMARY KEY (no)
);

-- @block

 INSERT INTO `info` (`no`, `img`, `position`, `contact`, `resume`, `skill1`, `skill2`, `skill3`, `skill4`, `skill5`, `about`, `linkedin`, `exp`, `name`, `insta`, `twt`, `fb`) VALUES
(1, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_AlubbpWqdGsd8Fcqi4fp-E9kCFwD0eM1rdu1NeXTVe3q9R07', 'Professor ', 'mailto:malan@harvard.edu', 'https://cs.harvard.edu/malan/cv/malan.pdf', 'C++', 'GO', 'JAVA', 'PHP', 'Python', 'David J. Malan is Gordon McKay Professor of the Practice of Computer Science at Harvard University in the School of Engineering and Applied Sciences as well as a Member of the Faculty of Education in the Graduate School of Education. He teaches Computer Science 50, otherwise known as CS50, which is among Harvard University’s largest courses, one of Yale University’s largest courses, and edX’s largest MOOC, with over 5.1M registrants. He also teaches at Harvard Business School, Harvard Law School, Harvard Extension School, and Harvard Summer School. ', 'https://www.linkedin.com/in/malan/', 3, 'David J. Malan', 'https://www.instagram.com/davidjmalan/', 'https://twitter.com/davidjmalan', 'https://www.facebook.com/dmalan');

-- @block
CREATE TABLE experience(`id` int(11) NOT NULL AUTO_INCREMENT,
  `exp1name` varchar(95) DEFAULT NULL,
  `exp1place` varchar(55) DEFAULT NULL,
  `exp1time` varchar(25) DEFAULT NULL,
  `exp1info` varchar(255) DEFAULT NULL,
  `exp2name` varchar(95) DEFAULT NULL,
  `exp2place` varchar(55) DEFAULT NULL,
  `exp2time` varchar(25) DEFAULT NULL,
  `exp2info` varchar(255) DEFAULT NULL,
  `exp3name` varchar(95) DEFAULT NULL,
  `exp3place` varchar(55) DEFAULT NULL,
  `exp3time` varchar(25) DEFAULT NULL,
  `exp3info` varchar(255) DEFAULT NULL,
  `exp4name` varchar(95) DEFAULT NULL,
  `exp4place` varchar(55) DEFAULT NULL,
  `exp4time` varchar(25) DEFAULT NULL,
  `exp4info` varchar(255) DEFAULT NULL,  
  PRIMARY KEY (id),`no` int(11),
  FOREIGN KEY (no) REFERENCES info(no)
);

-- @block
INSERT INTO experience(`exp1name`, `exp1place`, `exp1time`, `exp1info`) VALUES( 'Lecturer', 'Tufts University', '2002-2005', 'Instructor for Computer Science 15: Data Structures, a second course for undergraduates. Managed staff of 10 teaching assistants');

-- @block
UPDATE  experience SET exp2name='Founder', exp2place= 'Diskaster', exp2time='2005 – 2008', exp2info='Started company that offered professional recovery of data from hard drives and memory cards as
well as forensic investigations for civil matters.' where id = 1;


-- @block
SELECT * FROM info;
SELECT * FROM experience;
