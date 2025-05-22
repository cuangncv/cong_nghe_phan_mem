-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th5 22, 2025 lúc 07:34 PM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `congnghe_phanmem`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `pt`
--

CREATE TABLE `pt` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `sex` varchar(255) NOT NULL,
  `birth` date NOT NULL,
  `phone` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `note` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `pt`
--

INSERT INTO `pt` (`id`, `name`, `sex`, `birth`, `phone`, `email`, `address`, `note`) VALUES
(3, 'Lê Nam', 'Nam', '1998-12-13', '0912876531', 'llnln@gmail.com', 'Hoàng Quốc Việt - Cầu Giấy - Hà Nội', 'PT đang kiếm người yêu'),
(5, 'Lê Minh', 'Nữ', '1999-03-17', '0879435923', 'lm@gmail.com', 'Nguyễn Trãi - Hà Đông - Hà Nội', ''),
(10, 'Nguyễn Q', 'Nam', '2024-04-01', '0987765432', 'quang@gmail.com', '', ''),
(21, 'Nguyễn Hoàng', 'Nam', '2025-05-21', '0987653567', 'qqq@gmail.com', '', ''),
(22, 'Nguyễn QQ', 'Nữ', '2025-05-21', '098751', 'quanggg@gmail.com', '', '');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `pt`
--
ALTER TABLE `pt`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `pt`
--
ALTER TABLE `pt`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
