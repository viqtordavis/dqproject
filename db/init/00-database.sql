-- MySQL dump 10.13  Distrib 5.7.24, for osx10.9 (x86_64)
--
-- Host: localhost    Database: dataquality
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `object_repr` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `dqapp_connectiondetails`
--

DROP TABLE IF EXISTS `dqapp_connectiondetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dqapp_connectiondetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `hostname` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `port` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `databasename` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `connectstring` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `schemaname` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `connection_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dqapp_connec_connection_id_6f101182_fk_dqcheckup` (`connection_id`),
  CONSTRAINT `dqapp_connec_connection_id_6f101182_fk_dqcheckup` FOREIGN KEY (`connection_id`) REFERENCES `dqapp_connections` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;



--
-- Table structure for table `dqapp_connections`
--

DROP TABLE IF EXISTS `dqapp_connections`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dqapp_connections` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `connectionname` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `sourcedb_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `connectionname` (`connectionname`),
  KEY `dqapp_connec_sourcedb_id_30dac237_fk_dqcheckup` (`sourcedb_id`),
  CONSTRAINT `dqapp_connec_sourcedb_id_30dac237_fk_dqcheckup` FOREIGN KEY (`sourcedb_id`) REFERENCES `dqapp_sourcedb` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;



--
-- Table structure for table `dqapp_dqcheck`
--

DROP TABLE IF EXISTS `dqapp_dqcheck`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dqapp_dqcheck` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dqcheckname` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `connection_id` int(11) NOT NULL,
  `tablename` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `dqcheckname` (`dqcheckname`),
  KEY `dqapp_dqchec_connection_id_6126380e_fk_dqcheckup` (`connection_id`),
  CONSTRAINT `dqapp_dqchec_connection_id_6126380e_fk_dqcheckup` FOREIGN KEY (`connection_id`) REFERENCES `dqapp_connections` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;



--
-- Table structure for table `dqapp_dqcheckdetails`
--

DROP TABLE IF EXISTS `dqapp_dqcheckdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dqapp_dqcheckdetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tablename` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `columnname` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `optionvalues` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `dqcheck_id` int(11) NOT NULL,
  `dqrule_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dqapp_dqchec_dqrule_id_f52b6067_fk_dqcheckup` (`dqrule_id`),
  KEY `dqapp_dqchec_dqcheck_id_060edea6_fk_dqcheckup` (`dqcheck_id`),
  CONSTRAINT `dqapp_dqchec_dqcheck_id_060edea6_fk_dqcheckup` FOREIGN KEY (`dqcheck_id`) REFERENCES `dqapp_dqcheck` (`id`),
  CONSTRAINT `dqapp_dqchec_dqrule_id_f52b6067_fk_dqcheckup` FOREIGN KEY (`dqrule_id`) REFERENCES `dqapp_dqrules` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;



--
-- Table structure for table `dqapp_dqcheckrunbatch`
--

DROP TABLE IF EXISTS `dqapp_dqcheckrunbatch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dqapp_dqcheckrunbatch` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `runstatus` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `runstarttime` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `runendtime` varchar(20) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `dqcheck_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dqapp_dqchec_dqcheck_id_e458ffed_fk_dqcheckup` (`dqcheck_id`),
  CONSTRAINT `dqapp_dqchec_dqcheck_id_e458ffed_fk_dqcheckup` FOREIGN KEY (`dqcheck_id`) REFERENCES `dqapp_dqcheck` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;



--
-- Table structure for table `dqapp_dqcheckrunfact`
--

DROP TABLE IF EXISTS `dqapp_dqcheckrunfact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dqapp_dqcheckrunfact` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `measuredcount` bigint(20) NOT NULL,
  `totalcount` bigint(20) NOT NULL,
  `minvalue` decimal(11,2) NOT NULL,
  `maxvalue` decimal(11,2) NOT NULL,
  `avgvalue` decimal(11,2) NOT NULL,
  `dqcheckdetailid_id` int(11) NOT NULL,
  `runbatchid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dqapp_dqchec_dqcheckdetailid_id_215a3fb3_fk_dqcheckup` (`dqcheckdetailid_id`),
  KEY `dqapp_dqchec_runbatchid_id_1cf6c938_fk_dqcheckup` (`runbatchid_id`),
  CONSTRAINT `dqapp_dqchec_dqcheckdetailid_id_215a3fb3_fk_dqcheckup` FOREIGN KEY (`dqcheckdetailid_id`) REFERENCES `dqapp_dqcheckdetails` (`id`),
  CONSTRAINT `dqapp_dqchec_runbatchid_id_1cf6c938_fk_dqcheckup` FOREIGN KEY (`runbatchid_id`) REFERENCES `dqapp_dqcheckrunbatch` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;



--
-- Table structure for table `dqapp_dqcheckrunfactsample`
--

DROP TABLE IF EXISTS `dqapp_dqcheckrunfactsample`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dqapp_dqcheckrunfactsample` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `samplerow` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `dqcheckdetailid_id` int(11) NOT NULL,
  `runbatchid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dqapp_dqchec_dqcheckdetailid_id_230e28ce_fk_dqcheckup` (`dqcheckdetailid_id`),
  KEY `dqapp_dqchec_runbatchid_id_92a0ec18_fk_dqcheckup` (`runbatchid_id`),
  CONSTRAINT `dqapp_dqchec_dqcheckdetailid_id_230e28ce_fk_dqcheckup` FOREIGN KEY (`dqcheckdetailid_id`) REFERENCES `dqapp_dqcheckdetails` (`id`),
  CONSTRAINT `dqapp_dqchec_runbatchid_id_92a0ec18_fk_dqcheckup` FOREIGN KEY (`runbatchid_id`) REFERENCES `dqapp_dqcheckrunbatch` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;



--
-- Table structure for table `dqapp_dqrules`
--

DROP TABLE IF EXISTS `dqapp_dqrules`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dqapp_dqrules` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dqrulename` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `dqruledesc` longtext COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `dqrulename` (`dqrulename`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dqapp_dqrules`
--

LOCK TABLES `dqapp_dqrules` WRITE;
/*!40000 ALTER TABLE `dqapp_dqrules` DISABLE KEYS */;
INSERT INTO `dqapp_dqrules` VALUES (1,'Null_Check','Check Null Values in Data'),(2,'Valid_Values','Check if the data contains values other than given valid values'),(3,'Invalid_Values','Check if the given invalid values exists in data'),(4,'Pattern_Check','Check if the data follows given string pattern');
/*!40000 ALTER TABLE `dqapp_dqrules` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dqapp_dqrulesql`
--

DROP TABLE IF EXISTS `dqapp_dqrulesql`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dqapp_dqrulesql` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sqlstmt` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `dqrule_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dqapp_dqrule_dqrule_id_05579978_fk_dqcheckup` (`dqrule_id`),
  CONSTRAINT `dqapp_dqrule_dqrule_id_05579978_fk_dqcheckup` FOREIGN KEY (`dqrule_id`) REFERENCES `dqapp_dqrules` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dqapp_dqrulesql`
--

LOCK TABLES `dqapp_dqrulesql` WRITE;
/*!40000 ALTER TABLE `dqapp_dqrulesql` DISABLE KEYS */;
/*!40000 ALTER TABLE `dqapp_dqrulesql` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dqapp_sourcedb`
--

DROP TABLE IF EXISTS `dqapp_sourcedb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dqapp_sourcedb` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dbname` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dqapp_sourcedb`
--

LOCK TABLES `dqapp_sourcedb` WRITE;
/*!40000 ALTER TABLE `dqapp_sourcedb` DISABLE KEYS */;
INSERT INTO `dqapp_sourcedb` VALUES (1,'mysql'),(2,'oracle'),(3,'hive'),(4,'sqlserver');
/*!40000 ALTER TABLE `dqapp_sourcedb` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-07 17:57:20
