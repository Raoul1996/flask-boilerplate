# ************************************************************
# Sequel Pro SQL dump
# Version 
#
# https://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 106.13.140.135 (MySQL 5.5.5-10.1.38-MariaDB-0+deb9u1)
# Database: neuq_robot
# Generation Time: 2019-05-04 06:33:03 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
SET NAMES utf8mb4;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table robot_data
# ------------------------------------------------------------

DROP TABLE IF EXISTS `robot_data`;

CREATE TABLE `robot_data` (
  `create_time` datetime NOT NULL,
  `update_time` datetime DEFAULT NULL,
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `robot_id` varchar(255) NOT NULL,
  `position_x` varchar(255) DEFAULT NULL,
  `position_y` varchar(255) DEFAULT NULL,
  `position_z` varchar(255) DEFAULT NULL,
  `velocity_x` varchar(255) DEFAULT NULL,
  `velocity_y` varchar(255) DEFAULT NULL,
  `velocity_z` varchar(255) DEFAULT NULL,
  `direction_x` varchar(255) DEFAULT NULL,
  `direction_y` varchar(255) DEFAULT NULL,
  `direction_z` varchar(255) DEFAULT NULL,
  `battery` int(11) DEFAULT NULL,
  `temperature` int(11) DEFAULT NULL,
  `ip` varchar(16) DEFAULT NULL,
  `data` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table robot_email
# ------------------------------------------------------------

DROP TABLE IF EXISTS `robot_email`;

CREATE TABLE `robot_email` (
  `create_time` datetime NOT NULL,
  `update_time` datetime DEFAULT NULL,
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table robot_robot
# ------------------------------------------------------------

DROP TABLE IF EXISTS `robot_robot`;

CREATE TABLE `robot_robot` (
  `create_time` datetime NOT NULL,
  `update_time` datetime DEFAULT NULL,
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `description` text,
  `name` varchar(100) DEFAULT NULL,
  `owner_id` bigint(20) NOT NULL,
  `type` varchar(4) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table robot_user
# ------------------------------------------------------------

DROP TABLE IF EXISTS `robot_user`;

CREATE TABLE `robot_user` (
  `create_time` datetime NOT NULL,
  `update_time` datetime DEFAULT NULL,
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `college` smallint(6) NOT NULL,
  `admin` tinyint(1) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



# Dump of table test
# ------------------------------------------------------------

DROP TABLE IF EXISTS `test`;

CREATE TABLE `test` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
