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

 Date: 31/12/2022 21:46:01
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
  INDEX `fk_PRODUCT_SELLER_1`(`user_id_s`) USING BTREE,
  CONSTRAINT `fk_PRODUCT_SELLER_1` FOREIGN KEY (`user_id_s`) REFERENCES `seller` (`user_id_s`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 49 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of product
-- ----------------------------
INSERT INTO `product` VALUES (1, 1, '小狗狗', 2000, '他就是一隻可愛的小狗狗', '2022-12-14 11:09:22', 1, 4, 'dog.PNG');
INSERT INTO `product` VALUES (2, 1, '螃蟹', 10000, '想吃卻吃不到', '2022-12-14 13:38:22', 1, 9, 'flower_crab.png');
INSERT INTO `product` VALUES (3, 33, '老虎', 2000000, '貴到你碰不起', '2022-12-14 14:15:57', 1, 0, 'tiger.PNG');
INSERT INTO `product` VALUES (8, 1, '小珠珠', 60, '貴妃式的生活', '12/15/22_19_44_32', 1, 43, 'pig.PNG');
INSERT INTO `product` VALUES (12, 1, '兔子', 28, '你確定你28元買的到一隻兔子', '12/15/22_19_54_04', 0, 186, 'rabbit.PNG');
INSERT INTO `product` VALUES (28, 1, '兔子娃娃', 2000, '不是活的喔', '12/15/22_20_23_17', 1, 1, 'rabbit.PNG');
INSERT INTO `product` VALUES (29, 1, '花作', 3000, '他就是一幅畫，但上面有花', '12/15/22_23_03_21', 1, 2, '51d7a659-9ee9-5737-bad4-3c385a32e4e6.png');
INSERT INTO `product` VALUES (30, 1, 'i5-13600K', 9900, '當初的夢想殞落了', '12/15/22_23_07_19', 1, 1, 'a669706e-441a-50ce-83a5-91f001dbe8f3.png');
INSERT INTO `product` VALUES (31, 1, 'i9-13900K', 19900, '大祕寶', '12/15/22_23_09_38', 1, 1, '5b33b286-0549-5807-821b-4936d8695587.png');
INSERT INTO `product` VALUES (45, 1, '柯基', 10000, '義肢狗', '12/17/22_22_54_29', 1, 5, 'e8b8cf8a-6aca-5cf3-ae1c-773938d292c4.png');
INSERT INTO `product` VALUES (46, 1, 'IPhone 14', 29990, 'It\'s a iPhone', '12/17/22_23_08_39', 1, 10, 'cab15f69-5f88-5de1-ad5b-54d5e9e0755d.png');
INSERT INTO `product` VALUES (47, 1, 'IPhone 14 pro +++', 7888, '我們賣的就是假的', '12/19/22_16_47_40', 1, 3431, 'aadd4ed4-3c4b-58b4-9f23-77d534bf6cbf.png');
INSERT INTO `product` VALUES (48, 1, 'comebuy', 60, '玩火奶茶 ( 大 )', '12/27/22_11_16_13', 1, 7, '5e0c0a0e-75ec-52b1-b07c-bcad7198856f.png');
INSERT INTO `product` VALUES (52, 39, '冰箱', 99999, '他就是一個可以冰東西的箱子', '12/31/22_17_07_38', 1, 1, 'e938f8c6-c5da-51fd-a15a-fbe1f27ab762.png');

SET FOREIGN_KEY_CHECKS = 1;
