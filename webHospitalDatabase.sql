USE [master]
GO
/****** Object:  Database [Web Hospital Project Lab]    Script Date: 29.04.2024 15:45:27 ******/
CREATE DATABASE [Web Hospital Project Lab]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'Web Hospital Project Lab', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.SQLEXPRESS\MSSQL\DATA\Web Hospital Project Lab.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'Web Hospital Project Lab_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.SQLEXPRESS\MSSQL\DATA\Web Hospital Project Lab_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [Web Hospital Project Lab] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Web Hospital Project Lab].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [Web Hospital Project Lab] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [Web Hospital Project Lab] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [Web Hospital Project Lab] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [Web Hospital Project Lab] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [Web Hospital Project Lab] SET ARITHABORT OFF 
GO
ALTER DATABASE [Web Hospital Project Lab] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [Web Hospital Project Lab] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [Web Hospital Project Lab] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [Web Hospital Project Lab] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [Web Hospital Project Lab] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [Web Hospital Project Lab] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [Web Hospital Project Lab] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [Web Hospital Project Lab] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [Web Hospital Project Lab] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [Web Hospital Project Lab] SET  DISABLE_BROKER 
GO
ALTER DATABASE [Web Hospital Project Lab] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [Web Hospital Project Lab] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [Web Hospital Project Lab] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [Web Hospital Project Lab] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [Web Hospital Project Lab] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [Web Hospital Project Lab] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [Web Hospital Project Lab] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [Web Hospital Project Lab] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [Web Hospital Project Lab] SET  MULTI_USER 
GO
ALTER DATABASE [Web Hospital Project Lab] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [Web Hospital Project Lab] SET DB_CHAINING OFF 
GO
ALTER DATABASE [Web Hospital Project Lab] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [Web Hospital Project Lab] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [Web Hospital Project Lab] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [Web Hospital Project Lab] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [Web Hospital Project Lab] SET QUERY_STORE = ON
GO
ALTER DATABASE [Web Hospital Project Lab] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [Web Hospital Project Lab]
GO
/****** Object:  Table [dbo].[Doktorlar]    Script Date: 29.04.2024 15:45:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Doktorlar](
	[DoktorID] [smallint] IDENTITY(1,1) NOT NULL,
	[Ad] [varchar](30) NULL,
	[Soyad] [varchar](30) NULL,
	[UzmanlikAlani] [varchar](50) NULL,
	[CalistigiHastane] [varchar](50) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Hastalar]    Script Date: 29.04.2024 15:45:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Hastalar](
	[HastaID] [smallint] IDENTITY(1,1) NOT NULL,
	[Ad] [varchar](30) NULL,
	[Soyad] [varchar](30) NULL,
	[DogumTarihi] [date] NULL,
	[Cinsiyet] [bit] NULL,
	[TelefonNo] [varchar](15) NULL,
	[Adres] [varchar](200) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Randevular]    Script Date: 29.04.2024 15:45:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Randevular](
	[RandevuID] [smallint] IDENTITY(1,1) NOT NULL,
	[RandevuTarihi] [date] NULL,
	[RandevuSaati] [time](7) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Raporlar]    Script Date: 29.04.2024 15:45:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Raporlar](
	[RaporID] [smallint] IDENTITY(1,1) NOT NULL,
	[RaporTarihi] [date] NULL,
	[RaporIcerigi] [varchar](500) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Yonetici]    Script Date: 29.04.2024 15:45:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Yonetici](
	[YoneticiID] [smallint] IDENTITY(1,1) NOT NULL,
	[AdSoyad] [varchar](60) NULL
) ON [PRIMARY]
GO
USE [master]
GO
ALTER DATABASE [Web Hospital Project Lab] SET  READ_WRITE 
GO
