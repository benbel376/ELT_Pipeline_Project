DROP TABLE IF EXISTS `elt`;
CREATE TABLE IF NOT EXISTS `source` 
(
    `track_id` INT NOT NULL,
    `types` TEXT NOT NULL,
    `traveled_d` FLOAT NOT NULL,
    `avg_speed` FLOAT NOT NULL,
    `trajectory` LONGTEXT NOT NULL
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;