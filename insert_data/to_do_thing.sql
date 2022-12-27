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

 Date: 28/12/2022 01:32:01
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for to_do_thing
-- ----------------------------
DROP TABLE IF EXISTS `to_do_thing`;
CREATE TABLE `to_do_thing`  (
  `event_id` int(0) NOT NULL AUTO_INCREMENT,
  `event_content` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `event_state` int(0) NOT NULL,
  PRIMARY KEY (`event_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of to_do_thing
-- ----------------------------
INSERT INTO `to_do_thing` VALUES (1, '忘記帳號密碼', 1);
INSERT INTO `to_do_thing` VALUES (2, '網頁跑版', 1);
INSERT INTO `to_do_thing` VALUES (3, '我們不得不面對一個非常尷尬的事實，那就是，每個人都不得不面對這些問題。 在面對這種問題時，一般來說，帶著這些問題，我們來審視一下我是一隻魚。蕭伯納曾經說過，自我控制是最強者的本能。', 1);
INSERT INTO `to_do_thing` VALUES (4, '使用者 userHI 性騷擾我', 0);

SET FOREIGN_KEY_CHECKS = 1;
