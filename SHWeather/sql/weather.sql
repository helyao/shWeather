/*
Navicat MySQL Data Transfer

Source Server         : iLocalHost
Source Server Version : 50628
Source Host           : localhost:3306
Source Database       : weather

Target Server Type    : MYSQL
Target Server Version : 50628
File Encoding         : 65001

Date: 2017-07-02 17:55:50
*/

CREATE DATABASE IF NOT EXISTS weather DEFAULT CHARSET utf8;

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for sh_weather
-- ----------------------------
DROP TABLE IF EXISTS `sh_weather`;
CREATE TABLE `sh_weather` (
  `time` varchar(20) DEFAULT NULL,
  `wea_from` varchar(20) DEFAULT NULL,
  `wea_to` varchar(20) DEFAULT NULL,
  `tem_from` int(11) DEFAULT NULL,
  `tem_to` int(11) DEFAULT NULL,
  `win_from` varchar(30) DEFAULT NULL,
  `win_to` varchar(30) DEFAULT NULL,
  `time_stamp` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sh_weather
-- ----------------------------
