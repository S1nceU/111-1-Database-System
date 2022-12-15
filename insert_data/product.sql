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

 Date: 16/12/2022 00:30:43
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
  `publish_date` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `status` int(0) NOT NULL,
  `total_amount` int(0) NOT NULL,
  `product_img` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`product_id`) USING BTREE,
  UNIQUE INDEX `name_same`(`product_name`) USING BTREE,
  INDEX `fk_PRODUCT_SELLER_1`(`user_id_s`) USING BTREE,
  CONSTRAINT `fk_PRODUCT_SELLER_1` FOREIGN KEY (`user_id_s`) REFERENCES `seller` (`user_id_s`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of product
-- ----------------------------
INSERT INTO `product` VALUES (1, 1, 'computer', 2000, '他就是一台電腦', '2022-12-14 11:09:22', 1, 1, NULL);
INSERT INTO `product` VALUES (2, 1, 'cat', 10000, '可愛貓貓', '2022-12-14 13:38:22', 1, 1, NULL);
INSERT INTO `product` VALUES (3, 33, 'body', 2000000, '硬化的腎臟', '2022-12-14 14:15:57', 1, 2, NULL);
INSERT INTO `product` VALUES (8, 1, 'milktea', 60, '桂花凍貴妃歐雷', '12/15/22_19_44_32', 1, 50, '12/15/22_19_44_32.png');
INSERT INTO `product` VALUES (12, 1, 'chips', 28, '樂事洋芋片', '12/15/22_19_54_04', 1, 200, '12/15/22_19_54_04.png');
INSERT INTO `product` VALUES (28, 1, 'dog', 2000, '可愛的小狗狗', '12/15/22_20_23_17', 1, 20, '12/15/22_20_23_17.png');
INSERT INTO `product` VALUES (29, 1, 'milk bottle', 3000, '喬伊小姐的大奶罐', '12/15/22_23_03_21', 1, 2, '51d7a659-9ee9-5737-bad4-3c385a32e4e6.png');
INSERT INTO `product` VALUES (30, 1, 'i5-13600K', 9900, '小哥哥艾里最愛你了', '12/15/22_23_07_19', 1, 1, 'a669706e-441a-50ce-83a5-91f001dbe8f3.png');
INSERT INTO `product` VALUES (31, 1, 'i9-13900K', 19900, '這也是蕭詠之未來會有的東西', '12/15/22_23_09_38', 1, 1, '5b33b286-0549-5807-821b-4936d8695587.png');

SET FOREIGN_KEY_CHECKS = 1;
