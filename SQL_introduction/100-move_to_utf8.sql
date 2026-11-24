-- Converts hbtn_0c_0, first_table and its name field to utf8mb4 / utf8mb4_unicode_ci.
-- Convert the database
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Switch to the database
USE hbtn_0c_0;
-- Convert the table and its text fields (including name)
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
