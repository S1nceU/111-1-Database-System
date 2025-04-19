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

 Date: 31/12/2022 21:45:55
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for order_product
-- ----------------------------
DROP TABLE IF EXISTS `order_product`;
CREATE TABLE `order_product`  (
  `order_id` int(0) NOT NULL,
  `product_id` int(0) NOT NULL,
  `amount` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`order_id`, `product_id`) USING BTREE,
  INDEX `fk_ORDER_PRODUCT_PRODUCT_1`(`product_id`) USING BTREE,
  CONSTRAINT `fk_ORDER_PRODUCT_ORDER_1` FOREIGN KEY (`order_id`) REFERENCES `order` (`order_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_ORDER_PRODUCT_PRODUCT_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of order_product
-- ----------------------------
INSERT INTO `order_product` VALUES (1, 1, 2);
INSERT INTO `order_product` VALUES (1, 2, 88);
INSERT INTO `order_product` VALUES (2, 12, 1);
INSERT INTO `order_product` VALUES (2, 47, 1);
INSERT INTO `order_product` VALUES (2, 48, 5);
INSERT INTO `order_product` VALUES (3, 12, 4);
INSERT INTO `order_product` VALUES (4, 12, 4);
INSERT INTO `order_product` VALUES (5, 1, 5);
INSERT INTO `order_product` VALUES (7, 1, 1);
INSERT INTO `order_product` VALUES (7, 2, 4);
INSERT INTO `order_product` VALUES (9, 52, 4);
INSERT INTO `order_product` VALUES (10, 12, 5);

SET FOREIGN_KEY_CHECKS = 1;
