drop table if exists users2;
CREATE TABLE `users2` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`username` VARCHAR(255) NOT NULL COLLATE 'utf8mb4_general_ci',
	`email` VARCHAR(255) NOT NULL COLLATE 'utf8mb4_general_ci',
	`address` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`state_province` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`city` VARCHAR(255) NOT NULL COLLATE 'utf8mb4_general_ci',
	`country` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`zip_code` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	`hashed_password` VARCHAR(255) NOT NULL COLLATE 'utf8mb4_general_ci',
	`user_type` VARCHAR(255) NOT NULL COLLATE 'utf8mb4_general_ci',
	`banned` INT(11) NOT NULL,
	`profile_picture` VARCHAR(255) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	PRIMARY KEY (`id`) USING BTREE
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
;
insert into users2 values (null,'admin','admin@master.com','5th ave # 21','zacatecas','mx','gpe', '9802','$2b$12$16kNu5IW80k1Tw7xz2H3iOCsz0.oMZ7q5OSGa/OIfOae0WGFe8aI2','admin',1,null)