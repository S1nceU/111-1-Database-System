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

 Date: 15/12/2022 12:25:51
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for product
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product`  (
  `product_id` int(0) NOT NULL AUTO_INCREMENT,
  `user_id_s` int(0) NOT NULL,
  `product_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `price` int(0) NOT NULL,
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `publish_date` datetime(0) NOT NULL,
  `status` bit(1) NOT NULL,
  `total_amount` int(0) NOT NULL,
  `product_img` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`product_id`) USING BTREE,
  INDEX `fk_PRODUCT_SELLER_1`(`user_id_s`) USING BTREE,
  CONSTRAINT `fk_PRODUCT_SELLER_1` FOREIGN KEY (`user_id_s`) REFERENCES `seller` (`user_id_s`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of product
-- ----------------------------
INSERT INTO `product` VALUES (1, 1, 'computer', 2000, '他就是一台電腦', '2022-12-14 11:09:22', b'1', 1, NULL);
INSERT INTO `product` VALUES (2, 1, 'cat', 10000, '可愛貓貓', '2022-12-14 13:38:22', b'1', 1, NULL);
INSERT INTO `product` VALUES (3, 33, 'body', 2000000, '硬化的腎臟', '2022-12-14 14:15:57', b'1', 2, NULL);

SET FOREIGN_KEY_CHECKS = 1;
