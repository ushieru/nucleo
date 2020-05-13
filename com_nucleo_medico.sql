-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 13-05-2020 a las 17:10:28
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `nucleo`
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
  `status` int(11) NOT NULL DEFAULT 0 COMMENT '0 = Por atender;\r\n1 = Atendido;\r\n2 = Cancelada;'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `com_nucleo_medico_empleados`
--

CREATE TABLE `com_nucleo_medico_empleados` (
  `id` int(11) NOT NULL,
  `id_own` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `telefono` varchar(12) NOT NULL,
  `password` varchar(300) NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT 0,
  `change_password` tinyint(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `com_nucleo_medico_highlights`
--

CREATE TABLE `com_nucleo_medico_highlights` (
  `id` int(11) NOT NULL,
  `id_paciente` int(11) NOT NULL,
  `highlight` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
  `isDelete` int(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
-- Disparadores `com_nucleo_medico_medicamentos`
--
DELIMITER $$
CREATE TRIGGER `init_stock_AI` AFTER INSERT ON `com_nucleo_medico_medicamentos` FOR EACH ROW INSERT INTO `com_nucleo_medico_medicamentos_stock`(`id`, `cantidad`) VALUES (NEW.id, 0)
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `com_nucleo_medico_medicamentos_movements`
--

CREATE TABLE `com_nucleo_medico_medicamentos_movements` (
  `id` int(11) NOT NULL,
  `id_medicamento` int(11) NOT NULL,
  `id_empleado` int(11) NOT NULL,
  `io` tinyint(1) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `com_nucleo_medico_medicamentos_stock`
--

CREATE TABLE `com_nucleo_medico_medicamentos_stock` (
  `id` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
  `celular` varchar(15) NOT NULL,
  `tel_casa` varchar(15) NOT NULL,
  `tel_oficina` varchar(15) NOT NULL,
  `delete` int(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `com_nucleo_medico_recetas`
--

CREATE TABLE `com_nucleo_medico_recetas` (
  `id` int(11) NOT NULL,
  `id_own` int(11) NOT NULL,
  `id_paciente` int(11) NOT NULL,
  `prescripcion` text NOT NULL,
  `fecha` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `com_nucleo_medico_user`
--

CREATE TABLE `com_nucleo_medico_user` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
-- Indices de la tabla `com_nucleo_medico_empleados`
--
ALTER TABLE `com_nucleo_medico_empleados`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_own` (`id_own`);

--
-- Indices de la tabla `com_nucleo_medico_highlights`
--
ALTER TABLE `com_nucleo_medico_highlights`
  ADD PRIMARY KEY (`id`);

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
-- Indices de la tabla `com_nucleo_medico_medicamentos_movements`
--
ALTER TABLE `com_nucleo_medico_medicamentos_movements`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `com_nucleo_medico_medicamentos_stock`
--
ALTER TABLE `com_nucleo_medico_medicamentos_stock`
  ADD PRIMARY KEY (`id`);

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
-- Indices de la tabla `com_nucleo_medico_recetas`
--
ALTER TABLE `com_nucleo_medico_recetas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_own` (`id_own`),
  ADD KEY `id_paciente` (`id_paciente`);

--
-- Indices de la tabla `com_nucleo_medico_user`
--
ALTER TABLE `com_nucleo_medico_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `com_nucleo_medico_citas`
--
ALTER TABLE `com_nucleo_medico_citas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `com_nucleo_medico_empleados`
--
ALTER TABLE `com_nucleo_medico_empleados`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `com_nucleo_medico_highlights`
--
ALTER TABLE `com_nucleo_medico_highlights`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `com_nucleo_medico_laboratorios`
--
ALTER TABLE `com_nucleo_medico_laboratorios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `com_nucleo_medico_medicamentos`
--
ALTER TABLE `com_nucleo_medico_medicamentos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `com_nucleo_medico_medicamentos_movements`
--
ALTER TABLE `com_nucleo_medico_medicamentos_movements`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `com_nucleo_medico_pacientes`
--
ALTER TABLE `com_nucleo_medico_pacientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `com_nucleo_medico_proveedores`
--
ALTER TABLE `com_nucleo_medico_proveedores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `com_nucleo_medico_recetas`
--
ALTER TABLE `com_nucleo_medico_recetas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `com_nucleo_medico_user`
--
ALTER TABLE `com_nucleo_medico_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

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
-- Filtros para la tabla `com_nucleo_medico_empleados`
--
ALTER TABLE `com_nucleo_medico_empleados`
  ADD CONSTRAINT `com_nucleo_medico_empleados_ibfk_1` FOREIGN KEY (`id_own`) REFERENCES `com_nucleo_medico_user` (`id`);

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
-- Filtros para la tabla `com_nucleo_medico_medicamentos_stock`
--
ALTER TABLE `com_nucleo_medico_medicamentos_stock`
  ADD CONSTRAINT `com_nucleo_medico_medicamentos_stock_ibfk_1` FOREIGN KEY (`id`) REFERENCES `com_nucleo_medico_medicamentos` (`id`);

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

--
-- Filtros para la tabla `com_nucleo_medico_recetas`
--
ALTER TABLE `com_nucleo_medico_recetas`
  ADD CONSTRAINT `com_nucleo_medico_recetas_ibfk_1` FOREIGN KEY (`id_own`) REFERENCES `com_nucleo_medico_user` (`id`),
  ADD CONSTRAINT `com_nucleo_medico_recetas_ibfk_2` FOREIGN KEY (`id_paciente`) REFERENCES `com_nucleo_medico_pacientes` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
