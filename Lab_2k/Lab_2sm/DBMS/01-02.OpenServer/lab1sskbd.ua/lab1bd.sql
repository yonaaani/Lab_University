-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Час створення: Лют 13 2023 р., 23:24
-- Версія сервера: 5.6.51
-- Версія PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База даних: `lab1bd`
--

-- --------------------------------------------------------

--
-- Структура таблиці `Client`
--

CREATE TABLE `Client` (
  `ClientID` int(11) NOT NULL,
  `Surname` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `MiddleName` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Adress` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Phone` varchar(15) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп даних таблиці `Client`
--

INSERT INTO `Client` (`ClientID`, `Surname`, `Name`, `MiddleName`, `Adress`, `Phone`) VALUES
(7, '', '', '', '', '');

-- --------------------------------------------------------

--
-- Структура таблиці `Routes`
--

CREATE TABLE `Routes` (
  `RoutesID` int(11) NOT NULL,
  `Country` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Climate` varchar(35) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Duration` int(1) NOT NULL,
  `Hotel` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп даних таблиці `Routes`
--

INSERT INTO `Routes` (`RoutesID`, `Country`, `Climate`, `Duration`, `Hotel`, `Price`) VALUES
(6, '', '', 0, '', 0);

-- --------------------------------------------------------

--
-- Структура таблиці `Vouchers`
--

CREATE TABLE `Vouchers` (
  `VouchersID` int(11) NOT NULL,
  `ClientID` int(11) NOT NULL,
  `Datejofshipment` int(40) NOT NULL,
  `Quantity` int(30) NOT NULL,
  `Discount` int(15) NOT NULL,
  `RoutesID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Індекси збережених таблиць
--

--
-- Індекси таблиці `Client`
--
ALTER TABLE `Client`
  ADD PRIMARY KEY (`ClientID`);

--
-- Індекси таблиці `Routes`
--
ALTER TABLE `Routes`
  ADD PRIMARY KEY (`RoutesID`);

--
-- Індекси таблиці `Vouchers`
--
ALTER TABLE `Vouchers`
  ADD PRIMARY KEY (`VouchersID`);

--
-- AUTO_INCREMENT для збережених таблиць
--

--
-- AUTO_INCREMENT для таблиці `Client`
--
ALTER TABLE `Client`
  MODIFY `ClientID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT для таблиці `Routes`
--
ALTER TABLE `Routes`
  MODIFY `RoutesID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT для таблиці `Vouchers`
--
ALTER TABLE `Vouchers`
  MODIFY `VouchersID` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
