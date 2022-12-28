/*
 Navicat Premium Data Transfer

 Source Server         : WSS
 Source Server Type    : MySQL
 Source Server Version : 80030
 Source Host           : localhost:3306
 Source Schema         : world

 Target Server Type    : MySQL
 Target Server Version : 80030
 File Encoding         : 65001

 Date: 28/12/2022 01:31:24
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for label
-- ----------------------------
DROP TABLE IF EXISTS `label`;
CREATE TABLE `label`  (
  `label_id` int(0) NOT NULL AUTO_INCREMENT,
  `label` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`label_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of label
-- ----------------------------
INSERT INTO `label` VALUES (1, 'organ');
INSERT INTO `label` VALUES (2, '3C');
INSERT INTO `label` VALUES (3, 'doll');
INSERT INTO `label` VALUES (4, '周邊');
INSERT INTO `label` VALUES (5, 'NB');
INSERT INTO `label` VALUES (6, '數位');
INSERT INTO `label` VALUES (7, '家電');
INSERT INTO `label` VALUES (8, '日用');
INSERT INTO `label` VALUES (9, '食用');
INSERT INTO `label` VALUES (10, '生活');
INSERT INTO `label` VALUES (11, '活動戶外');
INSERT INTO `label` VALUES (12, '美妝');
INSERT INTO `label` VALUES (13, '品牌評鑑');
INSERT INTO `label` VALUES (14, '書店');

SET FOREIGN_KEY_CHECKS = 1;
