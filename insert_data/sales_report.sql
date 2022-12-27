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

 Date: 28/12/2022 01:31:46
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for sales_report
-- ----------------------------
DROP TABLE IF EXISTS `sales_report`;
CREATE TABLE `sales_report`  (
  `report_id` int(0) NOT NULL AUTO_INCREMENT,
  `sales_results` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `sales_score` int(0) NOT NULL,
  `user_id_s` int(0) NOT NULL,
  PRIMARY KEY (`report_id`) USING BTREE,
  INDEX `fk_SALES_REPORT_SELLER_1`(`user_id_s`) USING BTREE,
  CONSTRAINT `fk_SALES_REPORT_SELLER_1` FOREIGN KEY (`user_id_s`) REFERENCES `seller` (`user_id_s`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sales_report
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
