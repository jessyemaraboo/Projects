#Immigration rate in Flanders in the last 5 years

This project aims to identify and analyse the immigration rate in the last 5 years in the flanders region in order to improve or expand systems to better receive and integrate these people.

#### Metrics
- Did the immigration rate in flanders increased or decresed in the past 5 years?
- What are the provinces with the most and the least immigrants?
- What is the commom gender of those people?
- What is the average age?
- What is the average civil status?

#### Data collection
##### stabel
dataset1 (population_2021) accessed on: 20.October.2026 = https://statbel.fgov.be/en/open-data/population-place-residence-nationality-marital-status-age-and-sex-10

dataset2 (population_2022) accessed on: 20.October.2026 = https://statbel.fgov.be/en/open-data/population-place-residence-nationality-marital-status-age-and-sex-12

dataset3 (population_2023) accessed on: 20.October.2026 = https://statbel.fgov.be/en/open-data/population-place-residence-nationality-marital-status-age-and-sex-13

dataset4 (population_2024) accessed on: 20.October.2026 = https://statbel.fgov.be/en/open-data/population-place-residence-nationality-marital-status-age-and-sex-15

dataset5 (population_2025) accessed on: 20.October.2026 = https://statbel.fgov.be/en/open-data/population-place-residence-nationality-marital-status-age-and-sex-16

#### Analysis methodology
Self exploratory data analysis using historical data of population comprising the years from 2021 to 2025 to evaluate immigration rates in Flanders region.

#### Tools
- SQL
- Python [pandas]
- PowerBI

#### Analysis results

#### Limitations



#### Queries: 2021
#Exploratory analysis for the population_2021
SELECT * FROM population_2021

#COUNT of foreigners in Flanders
-- Foreigners  => 83026
SELECT `TX_NATLTY_NL` AS Nationality, COUNT (`CD_NATLTY`) AS Total
FROM population_2021
GROUP BY `TX_NATLTY_NL`
ORDER BY Total

#Provinces with the most non-belgian people
-- Prov. Antwerpen => 21407
-- Prov. Vlaams-Brabant => 18137
-- Prov. Oost-Vlaanderen => 15120
SELECT
`TX_PROV_DESCR_NL`AS Provinces,
 COUNT(`CD_NATLTY`) AS Total
FROM population_2021
WHERE `TX_NATLTY_NL` = 'niet-Belgen'
GROUP BY `TX_PROV_DESCR_NL`
ORDER BY Total DESC

--LIMIT 3

#Average age of the foreigners #45.22
SELECT
ROUND(AVG(CD_AGE),2) AS Average_Age
FROM population_2021
WHERE `TX_NATLTY_NL` = 'niet-Belgen'

#Usual Gender of the foreigners
--Fem => 42169
--Masc => 40857
SELECT `CD_SEX` as Gender, COUNT(`CD_NATLTY`) AS Total
FROM population_2021
WHERE `TX_NATLTY_NL` = 'niet-Belgen'
GROUP BY `CD_SEX`
ORDER BY Total DESC

#Usual civil status
--Ongehuwd (Single) => 35137
-- Gehuwd (Married) => 28749
-- Gescheiden (Divorced) => 12741
-- Weduwstaat (Widow) => 6399
SELECT `TX_CIV_STS_NL` as Gender, COUNT(`CD_NATLTY`) AS Total
FROM population_2021
WHERE `TX_NATLTY_NL` = 'niet-Belgen'
GROUP BY `TX_CIV_STS_NL`
ORDER BY Total DESC

#Cities with the most foreigners
-- Antwerpen 635
-- Gent 566
-- Genk 525
  #with the least
-- Herstappe 3
-- Horebekke 22
-- Lo-Reninge 46
SELECT `TX_DESCR_NL` as Cities, COUNT(`CD_NATLTY`) AS Total
FROM population_2021
WHERE `TX_NATLTY_NL` = 'niet-Belgen'
GROUP BY `TX_DESCR_NL`
ORDER BY Total ASC
LIMIT 3

#min and max age
-- min  => 0
-- max => 100
SELECT MIN(`CD_AGE`) Min_Age, MAX(`CD_AGE`) Max_Age
FROM population_2021
WHERE `TX_NATLTY_NL` = 'niet-Belgen'

#### Queries: 2022
SELECT * FROM population_2022

#COUNT of foreigners in Flanders
-- Foreigners  => 84490
SELECT `TX_NATLTY_NL` AS Nationality, COUNT (`CD_NATLTY`) AS Total
FROM population_2022
GROUP BY `TX_NATLTY_NL`
ORDER BY Total

#Provinces with the most non-belgian people
-- Prov. Antwerpen => 21698
-- Prov. Vlaams-Brabant => 18460
-- Prov. Oost-Vlaanderen => 15469
SELECT
`TX_PROV_DESCR_NL`AS Provinces,
 COUNT(`CD_NATLTY`) AS Total
FROM population_2022
WHERE `TX_NATLTY_NL` = 'niet-Belgen'
GROUP BY `TX_PROV_DESCR_NL`
ORDER BY Total DESC

--LIMIT 3

#Average age of the foreigners #45.39
SELECT
ROUND(AVG(CD_AGE),2) AS Average_Age
FROM population_2022
WHERE `TX_NATLTY_NL` = 'niet-Belgen'

#Usual Gender of the foreigners
--Fem => 43026
--Masc => 41464
SELECT `CD_SEX` as Gender, COUNT(`CD_NATLTY`) AS Total
FROM population_2022
WHERE `TX_NATLTY_NL` = 'niet-Belgen'
GROUP BY `CD_SEX`
ORDER BY Total DESC

#Usual civil status
--Ongehuwd (Single) => 35819
-- Gehuwd (Married) => 29129
-- Gescheiden (Divorced) => 13079
-- Weduwstaat (Widow) => 6463
SELECT `TX_CIV_STS_NL` as Gender, COUNT(`CD_NATLTY`) AS Total
FROM population_2022
WHERE `TX_NATLTY_NL` = 'niet-Belgen'
GROUP BY `TX_CIV_STS_NL`
ORDER BY Total DESC

#Cities with the most foreigners
-- Antwerpen 633
-- Gent 565
-- Genk 533
  #with the least
-- Herstappe 9
-- Horebekke 22
-- Lo-Reninge 54
SELECT `TX_DESCR_NL` as Cities, COUNT(`CD_NATLTY`) AS Total
FROM population_2022
WHERE `TX_NATLTY_NL` = 'niet-Belgen'
GROUP BY `TX_DESCR_NL`
ORDER BY Total DESC
LIMIT 3

#min and max age
-- min  => 0
-- max => 100
SELECT MIN(`CD_AGE`) Min_Age, MAX(`CD_AGE`) Max_Age
FROM population_2022
WHERE `TX_NATLTY_NL` = 'niet-Belgen'

#### Queries: 2023
SELECT * FROM population_2023

#COUNT of foreigners in Flanders
-- Foreigners  => 87612
SELECT `TX_NATLTY_NL` AS Nationality, COUNT (`CD_NATLTY`) AS Total
FROM population_2023
GROUP BY `TX_NATLTY_NL`
ORDER BY Total

#Provinces with the most non-belgian people
-- Prov. Antwerpen => 22294
-- Prov. Vlaams-Brabant => 19188
-- Prov. Oost-Vlaanderen => 16239
SELECT
`TX_PROV_DESCR_NL`AS Provinces,
 COUNT(`CD_NATLTY`) AS Total
FROM population_2023
WHERE `TX_NATLTY_NL` = 'niet-Belgen'
GROUP BY `TX_PROV_DESCR_NL`
ORDER BY Total DESC

--LIMIT 3

#Average age of the foreigners #45.84
SELECT
ROUND(AVG(CD_AGE),2) AS Average_Age
FROM population_2023
WHERE `TX_NATLTY_NL` = 'niet-Belgen'

#Usual Gender of the foreigners
--Fem => 45032
--Masc => 42580
SELECT `CD_SEX` as Gender, COUNT(`CD_NATLTY`) AS Total
FROM population_2023
WHERE `TX_NATLTY_NL` = 'niet-Belgen'
GROUP BY `CD_SEX`
ORDER BY Total DESC

#Usual civil status
--Ongehuwd (Single) => 38380
-- Gehuwd (Married) => 29481
-- Gescheiden (Divorced) => 13220
-- Weduwstaat (Widow) => 6531
SELECT `TX_CIV_STS_NL` as Gender, COUNT(`CD_NATLTY`) AS Total
FROM population_2023
WHERE `TX_NATLTY_NL` = 'niet-Belgen'
GROUP BY `TX_CIV_STS_NL`
ORDER BY Total DESC

#Cities with the most foreigners
-- Antwerpen 630
-- Gent 567
-- Genk 529
  #with the least
-- Herstappe 9
-- Horebekke 34
-- Lo-Reninge 70
SELECT `TX_DESCR_NL` as Cities, COUNT(`CD_NATLTY`) AS Total
FROM population_2023
WHERE `TX_NATLTY_NL` = 'niet-Belgen'
GROUP BY `TX_DESCR_NL`
ORDER BY Total DESC
LIMIT 3

#min and max age
-- min  => 0
-- max => 100
SELECT MIN(`CD_AGE`) Min_Age, MAX(`CD_AGE`) Max_Age
FROM population_2023
WHERE `TX_NATLTY_NL` = 'niet-Belgen'

#### Queries: 2024
SELECT * FROM population_2024

#COUNT of foreigners in Flanders
-- Foreigners  => 88876
SELECT `TX_NATLTY_NL` AS Nationality, COUNT (`CD_NATLTY`) AS Total
FROM population_2024
GROUP BY `TX_NATLTY_NL`
ORDER BY Total

#Provinces with the most non-belgian people
-- Prov. Antwerpen => 22577
-- Prov. Vlaams-Brabant => 19470
-- Prov. Oost-Vlaanderen => 16499
SELECT
`TX_PROV_DESCR_NL`AS Provinces,
 COUNT(`CD_NATLTY`) AS Total
FROM population_2024
WHERE `TX_NATLTY_NL` = 'niet-Belgen'
GROUP BY `TX_PROV_DESCR_NL`
ORDER BY Total DESC

--LIMIT 3

#Average age of the foreigners #46.10
SELECT
ROUND(AVG(CD_AGE),2) AS Average_Age
FROM population_2024
WHERE `TX_NATLTY_NL` = 'niet-Belgen'

#Usual Gender of the foreigners
--Fem => 45681
--Masc => 43195
SELECT `CD_SEX` as Gender, COUNT(`CD_NATLTY`) AS Total
FROM population_2024
WHERE `TX_NATLTY_NL` = 'niet-Belgen'
GROUP BY `CD_SEX`
ORDER BY Total DESC

#Usual civil status
--Ongehuwd (Single) => 38961
-- Gehuwd (Married) => 29850
-- Gescheiden (Divorced) => 13406
-- Weduwstaat (Widow) => 6659
SELECT `TX_CIV_STS_NL` as Gender, COUNT(`CD_NATLTY`) AS Total
FROM population_2024
WHERE `TX_NATLTY_NL` = 'niet-Belgen'
GROUP BY `TX_CIV_STS_NL`
ORDER BY Total DESC

#Cities with the most foreigners
-- Antwerpen 632
-- Gent 565
-- Genk 530
  #with the least
-- Herstappe 9
-- Horebekke 25
-- Lo-Reninge 62
SELECT `TX_DESCR_NL` as Cities, COUNT(`CD_NATLTY`) AS Total
FROM population_2024
WHERE `TX_NATLTY_NL` = 'niet-Belgen'
GROUP BY `TX_DESCR_NL`
ORDER BY Total ASC
LIMIT 3

#min and max age
-- min  => 0
-- max => 100
SELECT MIN(`CD_AGE`) Min_Age, MAX(`CD_AGE`) Max_Age
FROM population_2024
WHERE `TX_NATLTY_NL` = 'niet-Belgen'

#### Queries: 2025
SELECT * FROM population_2025

#COUNT of foreigners in Flanders
-- Foreigners  => 86697
SELECT `TX_NATLTY_NL` AS Nationality, COUNT (`CD_NATLTY`) AS Total
FROM population_2025
GROUP BY `TX_NATLTY_NL`
ORDER BY Total
LIMIT 1

#Provinces with the most non-belgian people
-- Prov. Antwerpen => 22178
-- Prov. Vlaams-Brabant => 19325
-- Prov. Oost-Vlaanderen => 15873
SELECT
`TX_PROV_DESCR_NL`AS Provinces,
 COUNT(`CD_NATLTY`) AS Total
FROM population_2025
WHERE `TX_NATLTY_NL` = 'niet-Belgen'
GROUP BY `TX_PROV_DESCR_NL`
ORDER BY Total DESC

--LIMIT 3

#Average age of the foreigners #46.60
SELECT
ROUND(AVG(CD_AGE),2) AS Average_Age
FROM population_2025
WHERE `TX_NATLTY_NL` = 'niet-Belgen'

#Usual Gender of the foreigners
--Fem => 44600
--Masc => 42097
SELECT `CD_SEX` as Gender, COUNT(`CD_NATLTY`) AS Total
FROM population_2025
WHERE `TX_NATLTY_NL` = 'niet-Belgen'
GROUP BY `CD_SEX`
ORDER BY Total DESC

#Usual civil status
--Ongehuwd (Single) => 37813
-- Gehuwd (Married) => 28863
-- Gescheiden (Divorced) => 13395
-- Weduwstaat (Widow) => 6626
SELECT `TX_CIV_STS_NL` as Gender, COUNT(`CD_NATLTY`) AS Total
FROM population_2025
WHERE `TX_NATLTY_NL` = 'niet-Belgen'
GROUP BY `TX_CIV_STS_NL`
ORDER BY Total DESC

#Cities with the most foreigners
-- Antwerpen 632
-- Gent 573
-- Genk 530
  #with the least
-- Herstappe 9
-- Horebekke 19
-- Lo-Reninge 68
SELECT `TX_DESCR_NL` as Cities, COUNT(`CD_NATLTY`) AS Total
FROM population_2025
WHERE `TX_NATLTY_NL` = 'niet-Belgen'
GROUP BY `TX_DESCR_NL`
ORDER BY Total DESC
LIMIT 3

#min and max age
-- min  => 0
-- max => 100
SELECT MIN(`CD_AGE`) Min_Age, MAX(`CD_AGE`) Max_Age
FROM population_2025
WHERE `TX_NATLTY_NL` = 'niet-Belgen'