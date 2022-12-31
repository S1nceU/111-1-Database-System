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

 Date: 31/12/2022 21:45:50
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for order
-- ----------------------------
DROP TABLE IF EXISTS `order`;
CREATE TABLE `order`  (
  `order_id` int(0) NOT NULL AUTO_INCREMENT,
  `total_price` float(10, 2) NOT NULL,
  `order_time` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `status` int(0) NOT NULL,
  `user_id_c` int(0) NOT NULL,
  `ticket_id` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`order_id`) USING BTREE,
  INDEX `fk_ORDER_CUSTOMER_1`(`user_id_c`) USING BTREE,
  INDEX `fk_ORDER_TICKET_1`(`ticket_id`) USING BTREE,
  CONSTRAINT `fk_ORDER_CUSTOMER_1` FOREIGN KEY (`user_id_c`) REFERENCES `customer` (`user_id_c`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_ORDER_TICKET_1` FOREIGN KEY (`ticket_id`) REFERENCES `ticket` (`ticket_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of order
-- ----------------------------
INSERT INTO `order` VALUES (1, 200.00, '2022-12-26 22:33:04', 'NTUT', 1, 1, 2);
INSERT INTO `order` VALUES (2, 109.00, '12/27/22_12_16_43', 'NTUT', 0, 1, NULL);
INSERT INTO `order` VALUES (3, 100.00, '2022_12_27 21:58:45', 'NTUT', 0, 1, NULL);
INSERT INTO `order` VALUES (4, 78.00, '2022_12_28 23:52:18', 'NTUT', 0, 1, NULL);
INSERT INTO `order` VALUES (5, 9000.00, '2022_12_29 21:58:10', 'NTUT', 0, 1, NULL);
INSERT INTO `order` VALUES (6, 229500.00, '2022_12_31 15:59:39', 'NTUT', 0, 1, NULL);
INSERT INTO `order` VALUES (7, 36200.00, '2022_12_31 16:05:56', 'NTUT', 0, 3, NULL);
INSERT INTO `order` VALUES (9, 359996.00, '2022_12_31 17:10:17', '台北市大安區忠孝東路三段一號', 0, 5, NULL);
INSERT INTO `order` VALUES (10, 126.00, '2022_12_31 17:10:38', '台北市大安區忠孝東路三段一號', 0, 5, NULL);

SET FOREIGN_KEY_CHECKS = 1;
