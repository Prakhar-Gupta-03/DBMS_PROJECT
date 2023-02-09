USE test;
CREATE TABLE Admin(
    Admin_ID INT NOT NULL AUTO_INCREMENT,
    Admin_Password VARCHAR(20) NOT NULL,
    PRIMARY KEY (Admin_ID)
)
INSERT INTO Admin (Admin_Password) VALUE ('opDAD6hbh');
SELECT *FROM admin;