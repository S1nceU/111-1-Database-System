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

 Date: 15/12/2022 12:25:25
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for category
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category`  (
  `product_id` int(0) NOT NULL,
  `label_id` int(0) NOT NULL,
  PRIMARY KEY (`product_id`, `label_id`) USING BTREE,
  INDEX `fk_CATEGORY_LABEL_1`(`label_id`) USING BTREE,
  CONSTRAINT `fk_CATEGORY_LABEL_1` FOREIGN KEY (`label_id`) REFERENCES `label` (`label_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_CATEGORY_PRODUCT_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of category
-- ----------------------------
INSERT INTO `category` VALUES (3, 1);

SET FOREIGN_KEY_CHECKS = 1;
