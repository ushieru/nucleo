-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 12-03-2020 a las 18:57:14
-- Versión del servidor: 10.1.34-MariaDB
-- Versión de PHP: 7.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `com_nucleo_medico`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `com_nucleo_medico_citas`
--

CREATE TABLE `com_nucleo_medico_citas` (
  `id` int(11) NOT NULL,
  `own` int(11) NOT NULL,
  `paciente` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `descripcion` varchar(200) NOT NULL,
  `delete` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `com_nucleo_medico_citas`
--

INSERT INTO `com_nucleo_medico_citas` (`id`, `own`, `paciente`, `fecha`, `hora`, `descripcion`, `delete`) VALUES
(1, 3, 1, '2019-11-28', '14:30:00', 'Medicina General', 0),
(2, 3, 1, '2019-11-27', '11:00:00', 'Medicina General', 0),
(3, 4, 1, '2019-12-03', '11:00:00', 'medicina general', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `com_nucleo_medico_laboratorios`
--

CREATE TABLE `com_nucleo_medico_laboratorios` (
  `id` int(11) NOT NULL,
  `own` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `telephone` varchar(15) NOT NULL,
  `isDelete` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `com_nucleo_medico_laboratorios`
--

INSERT INTO `com_nucleo_medico_laboratorios` (`id`, `own`, `name`, `email`, `address`, `telephone`, `isDelete`) VALUES
(1, 3, 'labTest 1', 'test@gmail.com', 'address #1234', '0123456789', 0),
(2, 3, 'labTest 2', 'test2@gmail.com', 'address #1234', '0123456789', 0),
(3, 3, 'labTest 3', 'test3@gmail.com', 'address #1234', '0123456789', 0),
(4, 3, 'labTest 4', 'qweqwe@gmail.com', 'address #1234', '1231231231', 0),
(5, 3, 'labTest 5', 'test5@gmail.com', 'address # 1234', '1231231321', 1),
(9, 3, 'abcLab', 'abcLab@gmail.com', 'abcLab # 4231', '1231231231', 1),
(11, 3, 'asdasd', 'asdasd', 'asdasd', '456456', 1),
(12, 3, 'labtest05', 'test5@gmail.com', 'flores2345', '3334483993', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `com_nucleo_medico_medicamentos`
--

CREATE TABLE `com_nucleo_medico_medicamentos` (
  `id` int(11) NOT NULL,
  `own` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `expiration` date NOT NULL,
  `laboratory` int(11) NOT NULL,
  `provider` int(11) NOT NULL,
  `delete` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `com_nucleo_medico_medicamentos`
--

INSERT INTO `com_nucleo_medico_medicamentos` (`id`, `own`, `name`, `expiration`, `laboratory`, `provider`, `delete`) VALUES
(1, 3, 'Paracetamol', '2022-07-01', 1, 1, 0),
(2, 3, 'Amoxicilina', '2022-11-01', 2, 3, 0),
(3, 3, 'Ambroxol', '2021-01-01', 1, 1, 0),
(4, 3, 'Betametasona', '2021-01-01', 5, 2, 0),
(5, 3, 'Aspirina', '2024-07-10', 12, 2, 0),
(6, 3, 'ampicilina', '2028-02-24', 2, 10, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `com_nucleo_medico_pacientes`
--

CREATE TABLE `com_nucleo_medico_pacientes` (
  `id` int(11) NOT NULL,
  `own` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `birthday` date NOT NULL,
  `sexo` int(1) NOT NULL,
  `email` varchar(100) NOT NULL,
  `ocupacion` varchar(100) NOT NULL,
  `escolaridad` varchar(100) NOT NULL,
  `curp` varchar(100) NOT NULL,
  `poliza` varchar(100) NOT NULL,
  `estado_civil` varchar(100) NOT NULL,
  `domicilio` varchar(100) NOT NULL,
  `colonia` varchar(100) NOT NULL,
  `estado` varchar(100) NOT NULL,
  `municipio` varchar(100) NOT NULL,
  `delegacion` varchar(100) NOT NULL,
  `celular` varchar(15) NOT NULL,
  `tel_casa` varchar(15) NOT NULL,
  `tel_oficina` varchar(15) NOT NULL,
  `delete` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `com_nucleo_medico_pacientes`
--

INSERT INTO `com_nucleo_medico_pacientes` (`id`, `own`, `name`, `birthday`, `sexo`, `email`, `ocupacion`, `escolaridad`, `curp`, `poliza`, `estado_civil`, `domicilio`, `colonia`, `estado`, `municipio`, `delegacion`, `celular`, `tel_casa`, `tel_oficina`, `delete`) VALUES
(1, 3, 'Uziel Atlai Cocolan Flores', '1997-12-29', 0, 'uzielcocolan@gmail.com', 'Estudiante', 'Superior', 'COFU971229HJCCLZ09', '159786324', 'Soltero', 'Address # 123', 'Colonia', 'Jalisco', 'Guadalajara', '', '1231231231', '15915915', '26526526', 0),
(2, 3, 'rty', '2019-11-01', 0, 'iop', 'iop', 'iop', 'iop', 'iop', 'iop', 'qwe', 'qwe', 'qwe', 'qwe', 'qwe', '123', '123', '3123', 1),
(3, 3, 'pacientedemo', '2020-02-02', 0, 'demo@gmail.com', 'demo', 'demo', 'demo', 'demo', 'demo', 'demo', 'demo', 'demo', 'demo', 'demo', '12312413412', '123123123', '123123123123', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `com_nucleo_medico_proveedores`
--

CREATE TABLE `com_nucleo_medico_proveedores` (
  `id` int(11) NOT NULL,
  `own` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `telephone` varchar(15) NOT NULL,
  `isDelete` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `com_nucleo_medico_proveedores`
--

INSERT INTO `com_nucleo_medico_proveedores` (`id`, `own`, `name`, `email`, `address`, `telephone`, `isDelete`) VALUES
(1, 3, 'provTest 1', 'email@email.com', 'address # 123', '0000000000', 1),
(2, 3, 'provTest 2', 'email@email.com', 'address # 123', '0000000000', 0),
(3, 3, 'provTest 3', 'email@email.com', 'address # 123', '0000000000', 0),
(6, 3, 'adasd', 'asdasd', 'asdasd', '789876', 1),
(9, 3, 'provtest', 'testprov@gmail.com', 'prueba 3423', '3334483993', 0),
(10, 3, 'testprov6', 'pruebaprov@gmail.com', 'test 2345', '23345678', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `com_nucleo_medico_user`
--

CREATE TABLE `com_nucleo_medico_user` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `com_nucleo_medico_user`
--

INSERT INTO `com_nucleo_medico_user` (`id`, `name`, `email`, `password`) VALUES
(3, 'Uziel Atlai Cocolan Flores', 'uzielcocolan@gmail.com', 'ffc2dfb436c72e7a9484b4120a93bc318579c61c1d86c88aed4da1b6ff5467a36cd7b0fe691f274b42a56daed902f6d09e1a6b3f8d25cf74ec05a54b6541167b'),
(4, 'Miguel', 'miguel.gonzalez.carlos97@gmail.com', 'd783573b3bd699d612611b93d1ae4db54373bd3333c2d0ec6867c31a75535a61ac4c336fb0b2d08692fc31d7af0180bfb6bd56be52d9048ff0a0f05ecf9e9035');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `com_nucleo_medico_citas`
--
ALTER TABLE `com_nucleo_medico_citas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Medico-Citas` (`own`),
  ADD KEY `Paciente-Citas` (`paciente`);

--
-- Indices de la tabla `com_nucleo_medico_laboratorios`
--
ALTER TABLE `com_nucleo_medico_laboratorios`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Medico-Laboratorio` (`own`);

--
-- Indices de la tabla `com_nucleo_medico_medicamentos`
--
ALTER TABLE `com_nucleo_medico_medicamentos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Medico-Medicamentos` (`own`),
  ADD KEY `Laboratorio-Medicamentos` (`laboratory`),
  ADD KEY `Proveedor-Medicamentos` (`provider`);

--
-- Indices de la tabla `com_nucleo_medico_pacientes`
--
ALTER TABLE `com_nucleo_medico_pacientes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Medico-Paciente` (`own`);

--
-- Indices de la tabla `com_nucleo_medico_proveedores`
--
ALTER TABLE `com_nucleo_medico_proveedores`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Medico-Proveedores` (`own`);

--
-- Indices de la tabla `com_nucleo_medico_user`
--
ALTER TABLE `com_nucleo_medico_user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `com_nucleo_medico_citas`
--
ALTER TABLE `com_nucleo_medico_citas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `com_nucleo_medico_laboratorios`
--
ALTER TABLE `com_nucleo_medico_laboratorios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `com_nucleo_medico_medicamentos`
--
ALTER TABLE `com_nucleo_medico_medicamentos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `com_nucleo_medico_pacientes`
--
ALTER TABLE `com_nucleo_medico_pacientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `com_nucleo_medico_proveedores`
--
ALTER TABLE `com_nucleo_medico_proveedores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `com_nucleo_medico_user`
--
ALTER TABLE `com_nucleo_medico_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `com_nucleo_medico_citas`
--
ALTER TABLE `com_nucleo_medico_citas`
  ADD CONSTRAINT `Medico-Citas` FOREIGN KEY (`own`) REFERENCES `com_nucleo_medico_user` (`id`),
  ADD CONSTRAINT `Paciente-Citas` FOREIGN KEY (`paciente`) REFERENCES `com_nucleo_medico_pacientes` (`id`);

--
-- Filtros para la tabla `com_nucleo_medico_laboratorios`
--
ALTER TABLE `com_nucleo_medico_laboratorios`
  ADD CONSTRAINT `Medico-Laboratorio` FOREIGN KEY (`own`) REFERENCES `com_nucleo_medico_user` (`id`);

--
-- Filtros para la tabla `com_nucleo_medico_medicamentos`
--
ALTER TABLE `com_nucleo_medico_medicamentos`
  ADD CONSTRAINT `Laboratorio-Medicamentos` FOREIGN KEY (`laboratory`) REFERENCES `com_nucleo_medico_laboratorios` (`id`),
  ADD CONSTRAINT `Medico-Medicamentos` FOREIGN KEY (`own`) REFERENCES `com_nucleo_medico_user` (`id`),
  ADD CONSTRAINT `Proveedor-Medicamentos` FOREIGN KEY (`provider`) REFERENCES `com_nucleo_medico_proveedores` (`id`);

--
-- Filtros para la tabla `com_nucleo_medico_pacientes`
--
ALTER TABLE `com_nucleo_medico_pacientes`
  ADD CONSTRAINT `Medico-Paciente` FOREIGN KEY (`own`) REFERENCES `com_nucleo_medico_user` (`id`);

--
-- Filtros para la tabla `com_nucleo_medico_proveedores`
--
ALTER TABLE `com_nucleo_medico_proveedores`
  ADD CONSTRAINT `Medico-Proveedores` FOREIGN KEY (`own`) REFERENCES `com_nucleo_medico_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
