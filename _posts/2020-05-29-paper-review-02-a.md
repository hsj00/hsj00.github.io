---
title: "논문 읽기 02-A: 'New development of Atomic Layer Deposition: Processes, Methods and Applications', Sci. Technol. Adv. Mater., 20, (2019), 66"
layout: post
date: 2020-05-29 20:45
tag:
    - Chemical Engineering
    - Atomic Layer Deposition
    - ALD
    - Thin Film Deposition
    - Semiconductor
    - Paper
    - Study
    - Note
headerImage: false
image:
description: 200529 `New development of Atomic Layer Deposition Processes, Methods and Applications` paper review
category: blog
author: hsj00
externalLink: true
published: true
comments: true
share: true
use_math: false
---

요즘 ALD 트렌드가 어떤지 공부도 할겸 논문 한 편 구해서 읽는다. 읽으면서 체크했던 내용들 요약하듯 짜깁기해서 정리해본다.
대충 절반으로 쪼개서 앞부분과 뒷부분으로 나눠 올릴 예정이다.

첫 번째 포스팅의 TOC는 다음과 같다.

- [New development of Atomic Layer Deposition: Processes, Methods and Applications](#new-development-of-atomic-layer-deposition-processes-methods-and-applications)
  - [Abstract](#abstract)
  - [1. Introduction](#1-introduction)
    - [1.1 Definition of ALD](#11-definition-of-ald)
    - [1.2 Backgroud](#12-backgroud)
        - [Figure.01](#figure01)
        - [Figure.02](#figure02)
    - [1.3 Thin Film Applications](#13-thin-film-applications)
    - [1.4 Comparison of ALD with other coating techniques](#14-comparison-of-ald-with-other-coating-techniques)
        - [Table.01](#table01)
        - [Table.02](#table02)
    - [1.5 Advantages and Disadvantages of ALD](#15-advantages-and-disadvantages-of-ald)
        - [Table.03](#table03)
    - [1.6 Complex 3D nanostructures](#16-complex-3d-nanostructures)
        - [Table.04](#table04)
  - [2. ALD Processes](#2-ald-processes)
        - [Table.05](#table05)
        - [Figure.05](#figure05)
  - [References](#references)

---

# New development of Atomic Layer Deposition: Processes, Methods and Applications

    - Science and Technology of Advanced Materials, 2019, Vol. 20, NO. 1, 465-496 (Sci. Technol. Adv. Mater., 20, (2019), 66)
    - DOI: https://doi.org/10.1080/14686996.2019.1599694

## Abstract

## 1. Introduction

### 1.1 Definition of ALD

-   Chemical precursors are sequentially introduced to the surface of a substrate where they chemically react directly with the surface to form sub-monolayers of film

---

### 1.2 Backgroud

-   Two of more precursors are pulsed/purged sequentially (self-limiting behaviour)

1. Exposure of the first precursor in the reactor chamber to form a layer on the substrate
2. Purge the excess first precursor and the by-products
3. Exposure of the second precursor
4. Purge or evacuation of the excess second precursor and by-products
5. The process is repeated until the required film thickness is achieved

##### Figure.01

Figure.01 Illustration of ALD for ZnO thin film deposition
![figure01][fig01]
`'Numerical modelling in the atomic layerdeposition process: A short review', unpublished.`

##### Figure.02

Figure.02 A model ALD process for depositing TiO2 on hydroxyl groups functionalized substrate using TiCl4 and H2O as precursors[^ref13]
![figure02][fig02]

---

### 1.3 Thin Film Applications

-   Semiconductors
-   Batteries
-   The solar industry
-   Membrane technololgy
-   Catalyst
-   Medicine/Medical devices
-   etc.

---

### 1.4 Comparison of ALD with other coating techniques

##### Table.01

Table.01 Different types of film deposition methods (adapted from [^ref54]), the sputtering was adapted from [^ref55] while the breath figure method was adapted from [^ref56]

| Method                           | Description and types                                                                                                                                                                                                                                                                                                                                                   | Advantages                                                                                                                                                | Applications                                                                                                                                                                                                          |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Electroplating                   | Film formation from chemicals in electrolytic solution placed onto substrate surface with a seed layer on top                                                                                                                                                                                                                                                           | Corrosion resistance, decoration, mechanical characteristics improvement, protection barriers, electrical conduction and heat resistance                  | Metal plating, corrosion resistance, decoration, mechanical characteristics improvement, friction reduction, protection barriers, improved electrical conductivity, heat resistance and radiation protection etc.     |
| Spin coating                     | Film formation from chemical reaction between liquid-phase sources (often sol-gel) applied onto surface of substrate while spinning                                                                                                                                                                                                                                     | Simplicity and ease of set up, low cost and fast operating system                                                                                         | Photoresists, insulators, organic semiconductors, synthetic metals, nanomaterials, metal and metal oxide precursors, transparent conductive oxides, optical mirrors, magnetic disk for data storage, solar cells etc. |
| Sputtering                       | A process of deposition of materials because of bombardment of targets by high energy particles ejected from a source                                                                                                                                                                                                                                                   | Deposit a wide variety of metal and metal oxide nanoparticles (NPs) and nanoclusters (NCs), insulators, alloys and composites, and even organic compounds | Silicon wafer, solar panel or optical device, catalysis                                                                                                                                                               |
| Breath figure                    | A self-assembly process that results in a honeycomb-structured films with micro-pores arranged in honeycomb shape usually formed by water microdroplets condensed on a cool surface from warm, humid air like breath                                                                                                                                                    | It is simple and applicable to a wide variety of materials with highly organized honeycomb-like porous surface                                            | Optics, photonics, surface science, biotechnology, and regenerative medicine                                                                                                                                          |
| Thermal oxidation                | Film formation by thermal oxidation of the substrate                                                                                                                                                                                                                                                                                                                    | Slow oxidation rate, good control of the oxide thickness and high values of breakdown field                                                               | Semiconductor industry, transistors, photoresistors, capacitors and field oxides, etc.                                                                                                                                |
| Physical vapour deposition (PVD) | Film formation by condensation of gasified source material, directly transported from source to substrate through the gas phase: Evaporation (thermal, E-beam), Molecular beam epitaxy (MBE), Pulsed laser deposition (PLD), Reactive PVD, Sputtering (DC, DC magnetron, RF)                                                                                            | Atomic level control of chemical composition, film thickness, and transition sharpness                                                                    | Fuel cells, batteries, microelectronics, optical and conducting surfaces, etc.                                                                                                                                        |
| Chemical vapour deposition (CVD) | Film formation by chemical reaction between mixed gaseous source materials on a substrate surface using: Atmospheric-pressure CVD (APCVD), Low-pressure CVD (LPCVD), Plasma-enhanced CVD (PECVD), Metal-organic CVD (MOCVD)                                                                                                                                             | High growth rates, good reproducibility, epitaxial films growth, good film quality, conformal step coverage                                               | Microelectronics, solar cells, fuel cells, batteries, etc.                                                                                                                                                            |
| Atomic layer deposition (ALD)    | A sub-class of CVD with film formation via sequential cycling of self-limiting chemical half-reactions on the substrate surface. Each reaction cycle accounts for the deposition of a (sub) monolayer. The reaction can be activated by thermal energy or plasma enhancement. They can be categorized as: Thermal ALD, Plasma-enhanced ALD (PEALD), Spatial ALD (S-ALD) | High quality films, conformality, uniformity, step coverage                                                                                               | Fuel cells, desalination, microelectronics, capacitors, oxides, catalysts, etc.                                                                                                                                       |

---

##### Table.02

Table.02 Comparison of thinfilmdeposition techniques which are similar to ALD [^ref57]

| **Property**          |         |         |         |               |                | **Deposition Technique** |
| --------------------- | ------- | ------- | ------- | ------------- | -------------- | ------------------------ |
| **CVD**               | **MBE** | **ALD** | **PLD** | **Evaporate** | **Sputtering** |                          |
| Deposition Rate       | Good    | Fair    | Poor    | Good          | Good           | Good                     |
| Film density          | Good    | Good    | Good    | Good          | Fair           | Good                     |
| Lack of pinholes      | Good    | Good    | Good    | Fair          | Fair           | Fair                     |
| Thickness uniformity  | Good    | Fair    | Good    | Fair          | Fair           | Good                     |
| Sharp dopant profiles | Fair    | Good    | Good    | Varies        | Good           | Poor                     |
| Step coverage         | Varies  | Poor    | Good    | Poor          | Poor           | Poor                     |
| Sharp interfaces      | Fair    | Good    | Good    | Varies        | Good           | Poor                     |
| Low substrate temp.   | Varies  | Good    | Good    | Good          | Good           | Good                     |
| Smooth interfaces     | Varies  | Good    | Good    | Varies        | Good           | Varies                   |
| No plasma damage      | Varies  | Good    | Good    | Fair          | Good           | Poor                     |

---

### 1.5 Advantages and Disadvantages of ALD

##### Table.03

Table.03 Advantages and disadvantages of ALD

| Advantages                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Disadvantages                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. High-quality films<br/>a. Control of the film thickness<br/>b. Escellent repeatablity<br/>c. High film density<br/>d. Amorphous of crystalline film<br/>e. Ultra-thin films<br/><br/>2. Conformality<br/>a. Excellent 3D conformality<br/>b. Large area thickness uniformity<br/>c. Atomically flat and smooth surface coating<br/><br/>3. Challenging Substrates<br/>a. Gentle deposition process for sensitive substrates<br/>b. Low temperature and stress<br/>c. Excellent adhesion<br/>d. Coats Teflon<br/><br/>4. Low-temperature processing<br/><br/>5. Soichiometric control<br/><br/>6. Inherent film quality associated with self-limiting<br/><br/>7. Self-assembled nature of the ALD mechanism<br/><br/>8. Multilayer | 1. The time required for the chemical reactions<br/><br/>2. The economic viability<br/><br/>3. Very high material waste rate<br/><br/>4. Very high energy waste rate<br/><br/>5. Intensive nature of the ALD process<br/><br/>6. Nano-Particle emissions |

---

### 1.6 Complex 3D nanostructures

-   A variety of materials such as semiconductors, magnetic materials, noble metals, and insulators are being fabricated using ALD to form 3D complex nanostructures
-   "The precursor flow will be hindered, and hence the reactions can be different from those reactions on a planar surface, in terms of both mechanism of nucleation and growth of the film. ... The specific challenges for the characterization of 3D nanoarchitectures were summarized in the [^ref63]."

##### Table.04

Table.04 Materials, reactants and templates used in ALD coating of nano-porous structures. Republished with permission from [^ref59]

| **Materials** |              **Reactants**              | **Temperature** | **Template**  |
| :-----------: | :-------------------------------------: | :-------------: | :-----------: |
|     TiO2      |           Ti[OCH(CH3)2]4/H2O            |      140℃       | Polycarbonate |
|     ZrO2      |             Zr[OCH(CH3)3]4              |                 |               |
|     TiO2      |                TiCl4/H2O                |      105℃       |      AAO      |
|      ZnO      |              Zn(C2H5)2/H2O              |      200℃       |      AAO      |
|      ITO      | InCp/O3 Tetrakis(dimethylamino)tin/H2O2 |      275℃       |      AAO      |
|      Ru       |              Ru(EtCp)2/O2               |      300℃       |      AAO      |
|     SiO2      |      H2N(CH2)3Si(OCH2CH3)3/H2O/O3       |      150℃       |      AAO      |
|     Fe2O3     |              Fe2(OBu)6/H2O              |    130℃-170℃    |      AAO      |
|     Fe2O3     |               Fe(Cp)2/O3                |      230℃       |      AAO      |
| Fe2O3 + Fe3O4 |               Fe(Cp)2/O2                |    350℃-500℃    |      AAO      |
|      ZnS      |              Zn(C2H5)2/H2S              |      120℃       |      AAO      |
|     Sb2O5     |             (Sb(NMe2)3)/O3              |      120℃       |      AAO      |
|     Sb2S3     |             (Sb(NMe2)3)/H2S             |      120℃       |      AAO      |
|     Nb2O3     |                 NbI5/O3                 |      320℃       |      AAO      |

-   ITO: Indum tin oxide
-   AAO: anodic aluminum oxide
-   Ru(EtCp)2: bis(ethycyclopentadienyl)ruthenium
-   Sb(NMe2)3: Tris(dimethylamido)antimony(III)

---

## 2. ALD Processes

##### Table.05

Table.05 Advantages and disadvantages of PEALD

| **Advantages**                               | **Disadvantages**                   |
| -------------------------------------------- | ----------------------------------- |
| Low deposition temperature                   | Limited conformality                |
| Higher reactivity (shorter deposition times) | More complicated reactor designs    |
| Higher film purity                           | More complicated reaction chemistry |
| Denser films                                 | Wide range of chemistry possible    |
| Higher throughput                            | Potentially poor conformality       |
| In situ plasma treatment                     | Lower throughput                    |
| Lower impurity                               | Damage to films                     |
|                                              | Additional growth parameter         |

---

##### Figure.05

Figure.05 Schematic representation of the three different types of plasma-assisted atomic layer deposition that can be distinguished: (a) direct plasma (b) remote plasma, and (c) radical enhanced
![figure05][fig05]

**`'Recently a branch of ALD, called the photo-assisted ALD or UV-enhanced ALD, has been developed. There the illumination by UV light is adapted as a part of the ALD cycle. UV exposure has been shown to enhance the surface reactions and lead to improved film properties.'`** [^ref65]

---

## References

<!-- references -->

[^ref13]: <https://doi.org/10.1016/j.jpowsour.2016.10.097>{: target="\_blank"}
[^ref54]: <https://doi.org/10.1038/micronano.2016.48>{: target="\_blank"}
[^ref55]: <https://doi.org/10.1080/14686996.2018.1542926>{: target="\_blank"}
[^ref56]: <https://doi.org/10.1080/14686996.2018.1528478>{: target="\_blank"}
[^ref57]: <https://doi.org/10.1016/j.apsusc.2016.09.040>{: target="\_blank"}
[^ref59]: <https://doi.org/10.1557/mrs.2011.264>{: target="\_blank"}
[^ref63]: <https://doi.org/10.1039/B801151F>{: target="\_blank"}
[^ref65]: <http://urn.fi/URN:ISBN:978-951-39-7099-4>{: target="\_blank"}

---

<!-- figure -->

[fig01]: https://www.tandfonline.com/na101/home/literatum/publisher/tandf/journals/content/tsta20/2019/tsta20.v020.i01/14686996.2019.1599694/20200603/images/large/tsta_a_1599694_f0001_oc.jpeg
[fig02]: https://www.tandfonline.com/na101/home/literatum/publisher/tandf/journals/content/tsta20/2019/tsta20.v020.i01/14686996.2019.1599694/20200603/images/large/tsta_a_1599694_f0002_oc.jpeg
[fig05]: https://www.tandfonline.com/na101/home/literatum/publisher/tandf/journals/content/tsta20/2019/tsta20.v020.i01/14686996.2019.1599694/20200603/images/large/tsta_a_1599694_f0005_oc.jpeg
