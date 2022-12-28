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

 Date: 28/12/2022 01:31:57
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for ticket
-- ----------------------------
DROP TABLE IF EXISTS `ticket`;
CREATE TABLE `ticket`  (
  `ticket_id` int(0) NOT NULL AUTO_INCREMENT,
  `effective_date` varchar(0) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `amount` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `discount` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `user_id_s` int(0) NOT NULL,
  PRIMARY KEY (`ticket_id`) USING BTREE,
  INDEX `fk_TICKET_SELLER_1`(`user_id_s`) USING BTREE,
  CONSTRAINT `fk_TICKET_SELLER_1` FOREIGN KEY (`user_id_s`) REFERENCES `seller` (`user_id_s`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of ticket
-- ----------------------------
INSERT INTO `ticket` VALUES (2, NULL, '67', '0.7', 1);
INSERT INTO `ticket` VALUES (3, NULL, '73', '0.7', 1);
INSERT INTO `ticket` VALUES (4, NULL, '94', '0.9', 1);
INSERT INTO `ticket` VALUES (5, NULL, '0', '0.85', 1);
INSERT INTO `ticket` VALUES (6, NULL, '5', '0.6', 1);

SET FOREIGN_KEY_CHECKS = 1;
