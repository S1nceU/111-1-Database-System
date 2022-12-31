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

 Date: 31/12/2022 21:46:11
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for seller
-- ----------------------------
DROP TABLE IF EXISTS `seller`;
CREATE TABLE `seller`  (
  `user_id_s` int(0) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `account` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `phone` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `id_number` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `user_status` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`user_id_s`) USING BTREE,
  UNIQUE INDEX `1`(`account`) USING BTREE,
  UNIQUE INDEX `2`(`email`) USING BTREE,
  UNIQUE INDEX `3`(`id_number`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 34 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of seller
-- ----------------------------
INSERT INTO `seller` VALUES (1, 'Jason', '109590009', 'password', 'ex@ex', 'NTUT', '0987654321', 'L123456789', 1);
INSERT INTO `seller` VALUES (30, 'Acute Angle Gan', 'userHI', 'password', 'email@email', 'NTUT', '0987654321', 'L76895409', 1);
INSERT INTO `seller` VALUES (31, 'ponywen', '109590027', 'password', 'ponywen@gmail.com', 'GS', '09896745231', 'B785849030', 1);
INSERT INTO `seller` VALUES (32, 'Sophia', '11038025', 'password', 'Sophia@gmail.com', 'GS', '0935800017', 'B785849456', 1);
INSERT INTO `seller` VALUES (33, 'Roy', 'royis87', 'password', 'Roy@gmail.com', 'NT', '0945695175', 'F156765345', 1);
INSERT INTO `seller` VALUES (39, 'Seller', 'seller', 'sellerpassword', 'seller@seller.com', '台北市大安區忠孝東路三段一號', '0227712171', 'A123789456', 0);

SET FOREIGN_KEY_CHECKS = 1;
