CREATE TABLE `duty_bot`(
  `id`           bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `nick_name`    varchar(30) NOT NULL DEFAULT '',
  `token`        varchar(38) NOT NULL COMMENT 'now bot token only contain 38 characters',
  `owner`        varchar(75) NOT NULL COMMENT 'staff email',
  `name`         varchar(30) NOT NULL,
  `description`  varchar(1024) DEFAULT '',
  `platform`     varchar(30) NOT NULL,
  `create_time`  DATETIME DEFAULT CURRENT_TIMESTAMP,
  `modify_time`  DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `status`       tinyint NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `uniq_nick_name` (nick_name),
  KEY `idx_platform`(`platform`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `duty_question_category`(
  `id`           bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name`         varchar(30) NOT NULL DEFAULT '',
  `type`         tinyint NOT NULL DEFAULT 0 COMMENT '0 means need create a group',
  `owner_id`     bigint(20) NOT NULL,
  `platform`     varchar(30) NOT NULL DEFAULT '',
  `wiki`         varchar(1024) DEFAULT '',
  `create_time`  DATETIME DEFAULT CURRENT_TIMESTAMP,
  `modify_time`  DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `status`       tinyint NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniq_name` (`name`),
  INDEX `idx_platform` (platform),
  KEY `idx_create_time` (`create_time`)
) ENGINE=InnoDB DEFAULT  CHARSET=utf8mb4;


CREATE TABLE `duty_staff`(
  `id`           bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name`         varchar(30) NOT NULL,
  `role`         varchar(30) NOT NULL DEFAULT '',
  `email`        varchar(75) NOT NULL,
  `create_time`  DATETIME DEFAULT CURRENT_TIMESTAMP,
  `modify_time`  DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `status`       tinyint NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniq_email` (`email`),
  INDEX `idx_create_time` (`create_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `duty_questions`(
  `id`           bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `title`        varchar(100) NOT NULL,
  `description`         varchar(1024) DEFAULT '',
  `create_time`  DATETIME DEFAULT CURRENT_TIMESTAMP,
  `modify_time`  DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `status`       tinyint NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uniq_title` (`title`),
  INDEX `idx_create_time` (`create_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `duty_category_ques_ref`(
  `id`           bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `category_id`  bigint(20) NOT NULL,
  `question_id`  bigint(20) NOT NULL,
  `create_time`  DATETIME DEFAULT CURRENT_TIMESTAMP,
  `modify_time`  DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `idx_category_id` (`category_id`),
  INDEX `idx_question_id` (`question_id`),
  INDEX `idx_create_time` (`create_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
CREATE TABLE `duty_answers`(
  `id`           bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `question_id`  bigint(20) NOT NULL,
  `content`      varchar(1024) DEFAULT '',
  `owner_id`     bigint(20) NOT NULL,
  `create_time`  DATETIME DEFAULT CURRENT_TIMESTAMP,
  `modify_time`  DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `status`       tinyint NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`),
  INDEX `idx_question_id` (`question_id`),
  INDEX `idx_create_time` (`create_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
