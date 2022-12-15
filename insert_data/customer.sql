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

 Date: 16/12/2022 00:30:29
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for customer
-- ----------------------------
DROP TABLE IF EXISTS `customer`;
CREATE TABLE `customer`  (
  `user_id_c` int(0) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `account` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `phone` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `id_number` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `user_status` bit(1) NULL DEFAULT NULL,
  PRIMARY KEY (`user_id_c`) USING BTREE,
  UNIQUE INDEX `123`(`account`) USING BTREE,
  UNIQUE INDEX `321`(`email`) USING BTREE,
  UNIQUE INDEX `2`(`id_number`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of customer
-- ----------------------------
INSERT INTO `customer` VALUES (1, 'Jason', '109590123', 'password', 'ex@e456456', 'NTUT', '0987654321', 'L19516789', b'0');
INSERT INTO `customer` VALUES (2, 'JasonLin', '109590001', 'password', 'ex@ex.com', 'NTUT', '0912378945', 'L123412345', b'0');
INSERT INTO `customer` VALUES (3, 'GKY', '109590021', 'password', 'ex@GKY.com', 'NTUT', '0987654321', 'L789675743', b'0');

SET FOREIGN_KEY_CHECKS = 1;
