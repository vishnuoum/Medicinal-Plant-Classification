-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 11, 2023 at 05:07 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `plant`
--

-- --------------------------------------------------------

--
-- Table structure for table `plant`
--

CREATE TABLE `plant` (
  `id` int(255) NOT NULL COMMENT 'Plant ID',
  `name` varchar(80) NOT NULL COMMENT 'Plant Name',
  `pic` text NOT NULL COMMENT 'Plant image',
  `scientific` text NOT NULL COMMENT 'Plant Scientific Name',
  `description` text NOT NULL COMMENT 'Description on plant'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `plant`
--

INSERT INTO `plant` (`id`, `name`, `pic`, `scientific`, `description`) VALUES
(1, 'Tulsi', 'http://cdn.shopify.com/s/files/1/0047/9730/0847/products/nurserylive-seeds-krishna-tulsi-tulsi-black-0-5-kg-seeds.png?v=1634226026', 'Ocimum tenuiflorum', 'Ocimum sanctum L. (also known as Ocimum tenuiflorum, Tulsi) has been used for thousands of years in Ayurveda for its diverse healing properties. Tulsi, the Queen of herbs, the legendary ‘Incomparable one’ of India, is one of the holiest and most cherished of the many healing and healthy giving herbs of the orient. The sacred basil, Tulsi, is renowned for its religious and spiritual sanctity, as well as for its important role in the traditional Ayurvedic and Unani system of holistic health and herbal medicine of the East. It is mentioned by Charaka in the Charaka Samhita; an Ayurvedic text. Tulsi is considered to be an adaptogen, balancing different processes in the body, and helpful for adapting to stress. Marked by its strong aroma and astringent taste, it is regarded in Ayurveda as a kind of ‘elixir of life’ and believed to promote longevity. Tulsi extracts are used in Ayurvedic remedies for common colds, headaches, stomach disorders, inflammation, heart disease, various forms of poisoning and malaria. Traditionally, O. sanctum L. is taken in many forms, as herbal tea, dried power or fresh leaf. For centuries, the dried leaves of Tulsi have been mixed with stored grains to repel insects.');

-- --------------------------------------------------------

--
-- Table structure for table `purposes`
--

CREATE TABLE `purposes` (
  `id` int(255) NOT NULL COMMENT 'Purpose ID',
  `plantId` int(255) NOT NULL COMMENT 'Plant ID Reference',
  `part` varchar(100) NOT NULL COMMENT 'Part of Plant',
  `description` text NOT NULL COMMENT 'Purpose'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `purposes`
--

INSERT INTO `purposes` (`id`, `plantId`, `part`, `description`) VALUES
(1, 1, 'Leaf', 'Tulsi leaves has been shown to counter metabolic stress through normalization of blood glucose, blood pressure and lipid levels, and psychological stress through positive effects on memory and cognitive function and through its anxiolytic and anti-depressant properties.');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(255) NOT NULL COMMENT 'User ID',
  `name` varchar(50) NOT NULL COMMENT 'Username',
  `phone` varchar(20) NOT NULL COMMENT 'Phone no.',
  `password` text NOT NULL COMMENT 'User password'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `phone`, `password`) VALUES
(1, 'Vishnu', '1234567890', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),
(2, 'VM', '123', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),
(3, 'VM', '1234', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),
(4, '1', '1', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `plant`
--
ALTER TABLE `plant`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `purposes`
--
ALTER TABLE `purposes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `plant`
--
ALTER TABLE `plant`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT COMMENT 'Plant ID', AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `purposes`
--
ALTER TABLE `purposes`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT COMMENT 'Purpose ID', AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT COMMENT 'User ID', AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
