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

 Date: 28/12/2022 01:31:00
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for cart_product
-- ----------------------------
DROP TABLE IF EXISTS `cart_product`;
CREATE TABLE `cart_product`  (
  `product_id` int(0) NOT NULL,
  `user_id_c` int(0) NOT NULL,
  `amount` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`product_id`, `user_id_c`) USING BTREE,
  INDEX `fk_CART_PRODUCT_CUSTOMER_1`(`user_id_c`) USING BTREE,
  CONSTRAINT `fk_CART_PRODUCT_CUSTOMER_1` FOREIGN KEY (`user_id_c`) REFERENCES `customer` (`user_id_c`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_CART_PRODUCT_PRODUCT_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cart_product
-- ----------------------------
INSERT INTO `cart_product` VALUES (1, 1, 1);
INSERT INTO `cart_product` VALUES (1, 3, 1);

SET FOREIGN_KEY_CHECKS = 1;
