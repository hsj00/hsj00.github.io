---
title: "논문 읽기 02-B: 'New development of Atomic Layer Deposition: Processes, Methods and Applications', Sci. Technol. Adv. Mater., 20, (2019), 66"
layout: post
date: 2020-06-08 20:45
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

두 번째 포스팅의 TOC는 다음과 같다.

- [New development of Atomic Layer Deposition: Processes, Methods and Applications](#new-development-of-atomic-layer-deposition-processes-methods-and-applications)
  - [3. Methods for studying ALD](#3-methods-for-studying-ald)
    - [3.1 Numerical methods](#31-numerical-methods)
      - [3.1.1 Knudsen number](#311-knudsen-number)
        - [Figure.06](#figure06)
      - [3.1.2 Monte Carlo](#312-monte-carlo)
      - [3.1.3 Molecular dynamics (MD)](#313-molecular-dynamics-md)
      - [3.1.4 Computational Fluid Dynamics (CFD)](#314-computational-fluid-dynamics-cfd)
    - [3.2 Experimental methods](#32-experimental-methods)
      - [3.2.1 Chemical supply](#321-chemical-supply)
        - [Table.06](#table06)
      - [3.2.2 Reactor](#322-reactor)
        - [Table.07](#table07)
      - [3.2.3 Effluent gas handling, emissions, energy consumption](#323-effluent-gas-handling-emissions-energy-consumption)
        - [Figure.07](#figure07)
  - [4. Applications](#4-applications)
    - [4.1 Microelectronics](#41-microelectronics)
      - [4.1.1 Electronics applications](#411-electronics-applications)
      - [4.1.2 Transistors](#412-transistors)
        - [Figure.08](#figure08)
        - [Figure.09](#figure09)
      - [4.1.3 Capacitors](#413-capacitors)
        - [Figure.10](#figure10)
    - [4.2 Energy strage and conversion](#42-energy-strage-and-conversion)
        - [Figure.11](#figure11)
    - [4.3 Desalination](#43-desalination)
      - [4.3.1 Biomimetic membrane](#431-biomimetic-membrane)
        - [Figure.12](#figure12)
        - [Figure.13](#figure13)
      - [4.3.2 Graphene](#432-graphene)
        - [Figure.14](#figure14)
        - [Figure.15](#figure15)
    - [4.3 Catalyst](#43-catalyst)
        - [Figure.16](#figure16)
        - [Figure.17](#figure17)
    - [4.5 Medical](#45-medical)
  - [5. Conclusions](#5-conclusions)
  - [References](#references)

----------

# New development of Atomic Layer Deposition: Processes, Methods and Applications
    - Science and Technology of Advanced Materials, 2019, Vol. 20, NO. 1, 465-496 (Sci. Technol. Adv. Mater., 20, (2019), 66)
    - DOI: https://doi.org/10.1080/14686996.2019.1599694

----------

## 3. Methods for studying ALD
- Two main categories of ALD process research: numerical and experimental
  - pressure, temperature, purge time, concentration, etc. [^ref4]
  - determine and predict effective reaction pathways
  - atomic bond formation, species chemisorption/adsorption, chemical kinetics, film deposition
  - reactor scale: material selection/interaction, geometry effects, fluid, energy transport on a macroscopic level [^ref70], [^ref71], [^ref72], [^ref73], [^ref74], [^ref75], [^ref76], [^ref77]
  - the continuum laws
- The optimal scaling rules in maximizing the utilization of precursors in the system for a fixed growth rate and relative uniformity [^ref84]

### 3.1 Numerical methods
#### 3.1.1 Knudsen number
- The Knudsen number (K<sub>n</sub>)
  - At intermediate values of K<sub>n</sub>, kinetic models based on the Boltzmann transport equation capture the influence of both transport and collisions among the molecules; transition regime
  - Knudsen number and system complexity per volume will increase, although the computational efficiency per volume and system size will decrease
  - ratio of the mean free path(`λ`) and the characteristic length(`d`) (K<sub>n</sub>=λ/d) [^ref90]
  - λ=k<sub>B</sub>T/p√2πd<sub>g</sub><sup>2</sup>
      - p: fluid pressure
    - d<sub>g</sub>: effective diameter of the molecule
    - k<sub>b</sub>: Blotzmann constant
    - T: fluid temperature
    - d: caracteristic length
  - molecule-wall to molucule-molecule collisions
  - K<sub>n</sub> depends on the gas flows pressure, temperature, and the characteristic reactor dimensions

##### Figure.06
> Figure.06 Various methods in describing fluid flow at different levels (modified with permission from Liao and Jen [^ref91] and Coetzee and Jen [^ref11])

![fig06][fig06]

#### 3.1.2 Monte Carlo
- required exposure to conformally coat an array of holes is determined by the height to width ratio of the individual holes and is independent of their spacing in the array
- conformality of PE-ALD[^ref93]
  - `"Conformal deposition can be achieved in high aspect ratio structures with a low value of recombination probability."`
  - recombination probability (recombination limited regime)
  - reaction probability (reaction limited regime)
  - diffusion rate of particles (diffusion limited regime)
- atomistic kinetics of ALD using the Monte Carlo method derived from DFT [^ref94]
  - the essential chemistry of the ALD reactions depends on the local environment at the surface

#### 3.1.3 Molecular dynamics (MD)
- use Newton's equations of motion

- `ReaxFF (Reactive Force-Field)`: force-field technique that uses the bond order concept in medelling the interactions in chemical system [^ref105]
- `DFT (Density Functional Theory)`: computational method that derives properties of the molecule based on a determination of the electron density of the molecule [^ref102], [^ref103], [^ref104]
- `LAMMPS`: demonstrate that a single layer of molybdenum difulfide (MoS<sub>2</sub>) can effectively separate ions from water (desalination) [^ref109]
- study and predict the influence of the initial surface composition and process temperature on the roughness of the surface, the growth rate and growth mode of the film deposition [^ref110]
- surface mechanisms and energetics study of the atomic layer deposition of alumina by TMA–H2O-process [^ref111]

#### 3.1.4 Computational Fluid Dynamics (CFD)
- continuum approach (K<sub>n</sub> < 0.1)
- apply the governing equations of conservation of mass, momentum, energy, and species transport [^ref12], [^ref89], [^ref115], [^ref116], [^ref117], [^ref118]
- DFT technique plays a crucial role in the CFD modelling method
- gas velocity decided the mass flow rate and chamber pressure as the determinant factor for minimising the cycle time
- while the increasing Reynolds number can reduce the required pulse time, no major gain is obtained in the total time sequence of the ALD-cycle -> slow purging precess [^ref119]

----------

### 3.2 Experimental methods
- ALD growth rate is strongly dependent on the aspect ratio of the substrate and the reatcor design
- Spatial ALD was introduced to overcome the longer pulsing and purging time by replacing the pulse/purge chambers spatially revolving heads

#### 3.2.1 Chemical supply
##### Table.06
> Table.06 Material grown by ALD process

| Material            | Precursor                                                              | Purge  | Temperature       | Film thickness                   | Method                       | Application                                                       | Ref                             |
| ------------------- | ---------------------------------------------------------------------- | ------ | ----------------- | -------------------------------- | ---------------------------- | ----------------------------------------------------------------- | ------------------------------- |
| TiO2                | TTIP (Titanium (IV)                                                    | N2     | 90                | 103 nm/cycle                     | Low-temperature              | Cotton fabrics                                                    | [^ref132]                       |
| SrTiO3              | Ti(CpMe5) (OMe)3, O3                                                   | N2     | 370               | 0.05 nm/cycle                    |                              | Capacitor                                                         | [^ref133]                       |
| TiO2                | TDMA, H2O isopropoxide, DI                                             |        | 150               | 0.055 nm/cycle                   | Thermal                      | Catalysts membranes, dye-sensitized solar cells, batteries sensor | [^ref134]                       |
| TiO2                | SiO2, [(EtCp)Ti(NMe2)3 Et = CH2CH3]                                    | O3, O2 | 250–300           |                                  | Thermal                      | MicroelectronicsDevices                                           | [^ref135]                       |
| Ge–Sb–Se–Te (GSST)  | Sb (OC2H5)3 and [(CH3)3Si]2                                            | Ar     | 70                |                                  | Low-temperature              | PcRAM                                                             | [^ref136]                       |
| SnO x               | Tetrakis(dimethylamino)tin(IV) and H2O                                 | N2     | 80                | (0.15 ± 0.01) nm/cycle           | Spatial Atmospheric Pressure | Solar cell                                                        | [^ref137]                       |
| SnS2                | Sn(OAc)4 and H2S                                                       | N2     | 150–250           | 0.17 Å/cycle                     | Low‐temperature              | Electronicscatalysis                                              | [^ref138]                       |
| TiO2                | Titaniumtetraisopropoxide (TTIP) and H2O                               | N2     | 200               | 0.02 nm/cycle                    | Thermal                      | Nano wires                                                        | [^ref139]                       |
| Si-O-Si(CH3)3       | HMDS ((CH3)3-Si-N-Si(CH3)3) + TMCS (Cl-Si(CH3)3) and H2O               | N2     | 180               |                                  | Plasma                       | Carbon separation, capture                                        | [^ref140]                       |
| Sb2Se3, TiO2 and Pt | Titanium(IV) tetraisopropoxide (TTIP), and H2O                         | N2     | 160               |                                  |                              | Solar energy conversion                                           | [^ref141]                       |
| Al2O3 and TiO2      | TiCl4, TMA OH, O2                                                      |        | 150 and 250       |                                  | Low-Temperature              | Filtration, gas storage, and catalysis                            | [^ref142]                       |
| Al2O3               |                                                                        |        | 150, 200, and 250 |                                  |                              | Nano-electronic devices                                           | [^ref143]                       |
| Al2O3               | [Al(NMe2)2(DMP)], [Al(NEt2)2(DMP) [Al(NiPr2)2(DMP), H20                |        | 100  and 180      |                                  | Thermal and plasma ALD       | Microelectronics, organic electronics, solar cells                | [^ref168]                       |
| V2O5                | vanadium triisopropoxide (VTIP)                                        | N2     | 150 to 300        |                                  | Thermal                      | Capacitors                                                        | [^ref202]                       |
| Ru                  | Ru(DMBD)(CO)3 and O2                                                   | N2     | 290 to 320        | 0.067 nm/cycle                   | Thermal                      | Transistors, capacitors                                           | [^ref144]                       |
| RuO2                | Ru(DMBD)(CO)3 and O2                                                   | N2     | 220 to 240        | 0.065 nm/cycle                   | Thermal                      | Transistors, capacitors                                           | [^ref144]                       |
| MoS2                | Mo(NMe2)4                                                              | N2     | 60                | 1.2 Å/cycle                      | Thermal                      | Catalysis, battery                                                | [^ref145]                       |
| CuSbS2              | CuAMD, SbTDMA, H2S                                                     | N2     | 225               |                                  | Low-Temperature              | Photovoltaics                                                     | [^ref146]                       |
| TiO2                | TiCl4, H2O                                                             | N2     | 180               | 0.6 Å/cycle                      |                              | Photocatalysis                                                    | [^ref147]                       |
| TiO2                | TiCl4, H2O                                                             | N2     | 40–250            | 0.048 nm/cycle to 0.113 nm/cycle | PEALD, tALD                  | Catalysis, semiconductors                                         | [^ref148]                       |
| V2O5 and VO2        | VO[O(C3H7)]3, H2O                                                      | N2     | 135               | 0.03 nm/cycle                    | PEALD, tALD                  | Microelectronics                                                  | [^ref149]                       |
| Ag                  | Ag(fod) (PEt3), BH3(NHMe2)                                             |        | 110               | 0.3 Å/cycle                      | Thermal                      |                                                                   | [^ref150]                       |
| Bi2O3               | Bi(Ph)3 and O3                                                         | N2     | 250 and 320       | 0.23 Å/cycle                     |                              | Supercapacitors, gas sensors, solid oxide fuel cells              | [^ref151]                       |
| ZnS                 | ZnS/g-C3N4                                                             | N2     | 200               |                                  | Thermal                      | Photocatalysis                                                    | [^ref152]                       |
| Ta2O5               | Ta(N t Bu)(NEt2)3, Ta(N t Bu)(NEt2)2Cp                                 | N2     | 250–300           | 0.77 and 0.67 Å/cycle            | Thermal                      | Capacitors, solar cell                                            | [^ref153]                       |
| Cobalt              | bis(1,4-di-tert-butyl-1,3-diazadienyl) cobalt and tert-butylamine      | N2     | 170 and 200       | 0.98 Å/cycle                     | Low temperature              | Microelectronics                                                  | [^ref154]                       |
| ZnO/ZrO2            | Tetrakis(ethylmethylamino)zirconium (TEMAZ), diethylzinc (DEZ) and H2O | Ar     | 200               | 1.0 Å/cycle                      | Thermal                      | Optical and electronic devices                                    | [^ref155], [^ref156]            |
| HfO2                | HfCl4 and H2O, tetrakis (dimethylamino) hafnium and H2O                | N2     | 200–275           | −0                               | Thermal                      | Transistors (MOSFET)                                              | [^ref157], [^ref158]            |
| HfO2                | Tetrakis(dimethylamino)hafnium (TDMA-Hf, [(CH3)2N]4Hf) and H2O         | N2     | 250               |                                  | Thermal                      | Microelectronics                                                  | [^ref159]                       |
| ZrO2                | (C5H5)Zr [N(CH3)2]3) and O3                                            | Ar     | 180               | 0.8 Å/cycle                      | Thermal                      | Capacitors (DRAM)                                                 | [^ref199]                       |
| ZrO2                | CpZr[N(CH3)2]3/C7H8 and O3                                             | Ar     | 250 to 350        |                                  | Thermal                      | Microelectronics                                                  | [^ref160]                       |
| ZnO                 | (C2H5)2Zn and H2O                                                      | Ar     | 100 to 300        |                                  | Plasma, Thermal              | Microelectronics, Solar energy                                    | [^ref161], [^ref162], [^ref163] |
| MoS2                | Trimethylaluminium (TMA) and H2O                                       | N2     | 200               | 1 Å/cycle                        | Thermal                      | Field-effect transistors (FETs)                                   | [^ref164]                       |

#### 3.2.2 Reactor
- Vacuum/Viscous flow ALD reactor can be used for non-planar and high surface area substrates
- high-surface-area substrates: attractive to use dedicate reactor designs -> conventional reactors will lead to longer deposition times and lower precursor efficiency [^ref64] 
  - continuous flow process: insufficient K<sub>n</sub> flow of precursor gases -> require impractical lengths of exposure time for achieving full and uniform fillings of trenches
  - stop flow process: higher precursor concentration -> require longer diffusion time to deposit on the trench surface
- batch/compact/fluidized bed/rotary reactor: depending on the required deposited materials functionality
- ALD reactor system based on gas injection
  - (a) Cross-flow reactor system based on forced flow laterally across the wafer
  - (b) system with a single injector above the center of the wafer
  - (c) showerhead system; injected through an array of injentors covering the entire wafer surface
  - (d) vertical batch reactor; 50-150 wafers are processed simutaneously

##### Table.07
> Table.07 Main ALD reactor types classified by their most important processing-related characteristics [^ref165]

| Reactor             | Processing ability | Gas-solid contact | Agglomeration prevention                                          | Energy Provision | Vacuum quality    |
| ------------------- | ------------------ | ----------------- | ----------------------------------------------------------------- | ---------------- | ----------------- |
| Flow-type           | Medium             | Flow through      | None (static bed)                                                 | Thermal          | Medium            |
| Viscous flow        | Low                | Flow over         | None (static bed)                                                 | Thermal          | Medium            |
| Fluidized bed       | High               | Mixed flow        | Mechanical & pneumatic vibration, stirring, microjet, pulsed flow | Thermal          | Medium-atmosphere |
| Rotary              | Medium             | Mixed flow        | Rotational agitation                                              | Thermal & plasma | High-medium       |
| Pneumatic conveying | High               | Local mix (jet)   | None                                                              | Thermal          | Atmospheric       |

#### 3.2.3 Effluent gas handling, emissions, energy consumption
- precursors/nano-particle(by-products) emission -> public health risk, environmental impact
- ALD has a lower carbon footprint dueto plasma enhanced deposition and lower cumulative energy demand

##### Figure.07
> Figure.07 Life cycle greenhouse gas emission and cumulative energy demand in an ALD process compared to other processes[^ref171]. Results are modelled based on cell efficiencies of 20.4% and 25% for current and prospective cells, respectively. (SHJ-Silicon Heterojunction)

![fig07][fig07]

----------

## 4. Applications
### 4.1 Microelectronics
#### 4.1.1 Electronics applications
- potential & advantages for nanotechnology: conformality, composition and control over material thickness(atomic scale thickness control), low growth temperature [^ref5], [^ref7]
- influence of the composition of materials on devices and the effects of temperature transistors through the application of the ALD process [^ref182], [^ref183], [^ref184], [^ref185], [^ref186], [^ref187], [^ref188], [^ref189], [^ref190], [^ref191], [^ref192], [^ref193]

#### 4.1.2 Transistors
##### Figure.08
- illustration of ALD application in a transistor
- Figure 8(b): Fin field effect transistor (FinFET) trigate design enhanced by using the ALD process

> Figure.08 (a) The traditional planar MOSFET design leading to an inverted surface channel and (b) the FinFET or trigate design where a Si fin covered by the gate oxide from three sides becomes inverted from the surrounding gate oxide, thus increasing the overall inverted volume compared to the planar design for the sam gate voltage [^ref7]

![fig08][fig08]

##### Figure.09
- gas flow sequence of CVD and ALD process
  - CVD: continuous deposition rate
  - ALD: cyclical deposition rate, self-limited half cycles due to the surface chemistry

> Figure.09 Schematic showing a basic gas flow sequence for CVD and for ALD as well as expected film growth profiles vs. process time [^ref194]

![fig09][fig09]

#### 4.1.3 Capacitors
- with mainstream materials and low processing temperature achieved better leakage current density, capacitance density and voltage nolinearity [^ref197], [^ref198]

##### Figure.10
- ALD applied new 10nm-class DRAM

> Figure.10 The new 10nm-class DRAM with high performance and reliability by Samsung. The thinkness of the dielectric layers uniform to a few angstroms-DRAM chip contains hundreds of millions to billions of cells depending on data capacity. Each cell consists of two parts: a capacitor that stores data in the form of an electrical charge, and a transistor that controls access to it [^ref208]

![fig10][fig10]

----------

### 4.2 Energy strage and conversion
- catalytic surface modify by using ALD
- significantly lower costs and increase the life-span
- Fuel cell types
  - PEMFCs: polymer electrolyte membrane fuel cells
  - DMFCs: direct methanol fuel cells
  - MCFCs: molten carbonate fuel cells
  - SOFCs: solid oxide fuel cells
  - reversible fuel cell
  - PAFCs: phosphoric acid fuel cells
  - AFCs: alkaline fuel cells

##### Figure.11
> (a) TEM images of spherical alumina supported Pd catalysts with different numbers of Al<sub>2</sub>O<sub>3</sub> ALD overcoating from 0 to 20 cycles and schematic illustration of porous ALD Al<sub>2</sub>O<sub>3</sub> overcoat on Pd NP for Oxide-supported Pd catalyst and dense Al<sub>2</sub>O<sub>3</sub> film on oxide support and porous Al<sub>2</sub>O<sub>3</sub> overcoat on Pd NP formed by ALD. [^ref211]
> (b) Cross-sectional schematic of a single membrane within its silicon die before and after application of the catalyst layers using ALD [^ref210]

![fig11][fig11]

----------

### 4.3 Desalination
- focus on the latest development of biomimetic based membranes

#### 4.3.1 Biomimetic membrane
- ideal biomimetic and bioinspired membrane
  - Fabrication of the membrane through self-assembly under conditions close to the natural atmosphere such as atmospheric pressure, room temperature and aqueous evironment
  - The membranes are materials with excellent hydrodynamic, mechanical, wetting and adhesive properties usually composed of the lightest elements in the first two rows of the periodic table
  - The hierarchical organization of the membrane structure spans from molecular-nanoscale-microscale-macroscale bearing controlled configuration, mutable surface and robust interface
  - The membrane properties are highly dependent on the content and state of water in the structure, and membrane processes can be intensified by rationally manipulating the multiple selectivity mechanisms

##### Figure.12
> Figure.12 complex structural features of biological pores that can be adapted for biomimetic filtration [^ref38]

![fig12][fig12]

##### Figure.13
> Translated biomimetic design TEM showing pore geometry modifications achieved by ALD targeted to the pore mouth. ALD of polypeptide groups which modifies internal pore chemistry to produce pore active sites with dimensions and chemical functionality similar to natural biological pores. [^ref38]

![fig13][fig13]

#### 4.3.2 Graphene
- intergration of graphene in microelectronics devices requires the deposition of thin dielectric layers on top of graphene
  - Wang et al.[^ref232] created an ultrathin film based on Al<sub>2</sub>O<sub>3</sub> of ALD on graphene

##### Figure.14
> Figure.14 [^ref232]
> (a) Schematic of a graphene membrane before ALD
> (b) Optical image of an exfoliated graphene flake with 7 cycles of alumina ALD
> (c) Optical image of a pure alumina film after graphene is etched away
> (d) AFM image of a pressurized 7-cycle pure alumina ALD film with Δp=278 kPa
> (e) Deflection vs. position through the center of the film in (d) at different Δp

![fig14][fig14]

- for the ALD of high-quality dielectric layers, a seed layer is grown using highly reactive precursors and low deposition temprature or through functionalization of graphene surface with a metal or polymer buffer layer
- could lead to degradation of the electronic properties of graphene or result in a higher high-k dielectric layer [^ref233]
- has the potenial to address the issues of water desalination and climate change (Cohen-Tanugi et al.[^ref96], [^ref234], [^ref235])

##### Figure.15
> Figure.15 [^ref228]
> (a) hydrogenated graphene pore
> (b) hydroxylated graphene pore
> (c) side view of the computational system

![fig15][fig15]


### 4.3 Catalyst
- how to improve the selectivity of catalysts to convert the specific feed to specific products with little or no waste in conjunction with undesirable reactions
  - control size, shape, and morphology of supported nanoparticles to improve selectivity -> controlling metal and metal oxide active sites and improving catalytic activity, selectivity, and longevity by using ALD
  - Fischer-Tropsch process -> highest activity of metal plates having Al<sub>2</sub>O<sub>3</sub> by the washcoating method and CoO<sub>x</sub> by ALD [^ref239]

##### Figure.16
> Figure.16
> (a) classification of composite catalysts synthesized with selective ALD, (I) core-shell structure, (II) discontinuous coating structure, and (III) embedded structure [^ref238]
> (b) the effect of different catalysts on Fischer-Tropsch synthesis CH<sub>4</sub> output measured by GC [^ref239]

![fig16][fig16]

- prove that ALD overcoating could suppress the commercial catalysts deactivation which happens during steam reforming, especially by thin Al<sub>2</sub>O<sub>3</sub> layers
- thinnest ALD coating had the highest improvements which show the ability of ALD in fabricating thin film

##### Figure.17
> Figure.17 The effect of ALD oxide layers on the commercial nickel-based catalyst (left) and on commercial noble metal catalyst (right) activit on steam reforming

![fig17][fig17]

- testing tool: Integrated Atomic Layer Deposition synthersis-Catalysis (I-ALD-CAT) for catalyst synthesis and performance evaluation of a catalyst
  - combine an ALD manifold with a plug flow reactor system
  - used in synthesizing Pt active sites, Al<sub>2</sub>O<sub>3</sub> overcoats and in the activity evaluation of propylene hydrogenation under plug-flow conditions [^ref240]

### 4.5 Medical
- Organic Field-Effect Transistors (OFETs)
  - ALD using low deposition temperature for manufaturing of OFETs [^ref242]
  - application in transducing mechanical and chemical simuli in to electrical signals [^ref243]
- Plasmonics, nanoscience and nanobiotechnology
  - coating for modifying the metallic surfaces and tuning the optical and plasmonic properties -> protect the surface from oxidation and contamination to create the required biocompatible surface [^ref244]
- Delivery of a pharmacological agent at a precise rate and specific location in the body [^ref245]
  - orthopaedic implants, self-sterilizing medical devices
  - to prevent metal diffusion from medical implants [^ref246]
- Tablet formulations: design of nanoparticles, and larger-sized, single drug powder particle applications [^ref247]
- Active pharmaceutical ingredients (APIs) [^ref248]

## 5. Conclusions

ALD는 복잡한 3D 구조물에서도 균일한 박막을 형성할 수 있다는 점 때문에 반도체와 같은 분야뿐만 아니라 에너지 저장장치, 촉매, 의약부문에서도 활용되고있다. 반응기 설계뿐만 아니라 증착 공정을 설계에 수치해석적인 방법부터 실험적인 방법까지 다양한 접근을 통해 연구가 이뤄지고 있다. 레퍼런스를 보면서 직간접적으로 아는 분들의 이름이 등장해서 반가웠고, 내가 졸업한 연구실 후배가 쓴 논문도 있는걸 보면서 신기하더라.

박막 증착에 대한 기본 개념이나 내용들을 모르는게 아니니 산업에서 사용되는 방법들, 예를들면 수치해석적인 방법을 이용한 반응기 설계나 전구체 합성 같은 분야에 대한 공부도 조금씩 해나가야겠다.

레퍼런스 정리하느라 업데이트에 시간이 좀 걸렸는데 나중에 필요할 때 바로 찾아볼 수 있을테니 들인 수고가 아깝지 않을 것 같다.

다음 논문은 뭘 읽어볼까....

-----------

## References
<!-- references -->
[^ref4]: <https://doi.org/10.1116/1.4905726>{: target="_blank"}
[^ref5]: <https://doi.org/10.1016/j.tsf.2008.09.007>{: target="_blank"}
[^ref7]: <https://doi.org/10.1016/j.mattod.2014.04.026>{: target="_blank"}
[^ref11]: <unpublished>{: target="_blank"}
[^ref12]: <https://doi.org/10.1016/j.ijheatmasstransfer.2014.07.079>{: target="_blank"}
[^ref38]: <https://www.osti.gov/biblio/1314559>{: target="_blank"}
[^ref64]: <https://doi.org/10.1039/C6CC05568K>{: target="_blank"}
[^ref70]: <https://doi.org/10.1116/1.4905726>{: target="_blank"}
[^ref71]: <https://doi.org/10.1016/j.ijheatmasstransfer.2015.05.079>{: target="_blank"}
[^ref72]: <https://doi.org/10.1016/j.cherd.2014.09.019>{: target="_blank"}
[^ref73]: <https://dc.uwm.edu/etd/1187/>{: target="_blank"}
[^ref74]: <https://doi.org/10.1016/j.ijheatmasstransfer.2016.01.034>{: target="_blank"}
[^ref75]: <https://doi.org/10.1016/j.ijheatmasstransfer.2015.07.123>{: target="_blank"}
[^ref76]: <https://doi.org/10.1016/j.cherd.2014.09.019>{: target="_blank"}
[^ref77]: <https://doi.org/10.1016/j.ijheatmasstransfer.2014.07.079>{: target="_blank"}
[^ref84]: <https://doi.org/10.1016/j.ces.2014.07.002>{: target="_blank"}
[^ref89]: <https://doi.org/10.1016/j.cherd.2014.09.019>{: target="_blank"}
[^ref90]: <https://doi.org/10.1016/j.ijheatmasstransfer.2012.11.075>{: target="_blank"}
[^ref91]: <https://www.intechopen.com/books/computational-fluid-dynamics-technologies-and-applications/application-of-lattice-boltzmann-method-in-fluid-flow-and-heat-transfer>{: target="_blank"}
[^ref93]: <https://doi.org/10.1149/1.3491381>{: target="_blank"}
[^ref94]: <https://doi.org/10.1002/jcc.23491>{: target="_blank"}
[^ref96]: <http://hdl.handle.net/1721.1/98743>{: target="_blank"}
[^ref102]: <https://doi.org/10.1021/cm035009p>{: target="_blank"}
[^ref103]: <https://doi.org/10.1186/s11671-015-1008-y>{: target="_blank"}
[^ref104]: <https://doi.org/10.1063/1.4975085>{: target="_blank"}
[^ref105]: <https://doi.org/10.1016/j.nimb.2010.12.053>{: target="_blank"}
[^ref109]: <https://doi.org/10.1038/ncomms9616>{: target="_blank"}
[^ref110]: <https://doi.org/10.1080/08927020802468372>{: target="_blank"}
[^ref111]: <https://doi.org/10.1039/C5CP01912E>{: target="_blank"}
[^ref115]: <https://dc.uwm.edu/etd/1187>{: target="_blank"}
[^ref116]: <https://doi.org/10.1016/j.ijheatmasstransfer.2015.07.123>{: target="_blank"}
[^ref117]: <https://doi.org/10.1142/S0217979219400186>{: target="_blank"}
[^ref118]: <https://doi.org/10.1142/S0217979219400186>{: target="_blank"}
[^ref119]: <https://doi.org/10.1116/1.5018475>{: target="_blank"}
[^ref132]: <https://doi.org/10.1007/s10570-017-1380-0>{: target="_blank"}
[^ref133]: <https://doi.org/10.1021/acs.chemmater.5b00843>{: target="_blank"}
[^ref134]: <https://doi.org/10.1021/nn1009984>{: target="_blank"}
[^ref135]: <https://doi.org/10.1021/acs.chemmater.7b04790>{: target="_blank"}
[^ref136]: <https://doi.org/10.1039/C8TC01041B>{: target="_blank"}
[^ref137]: <https://doi.org/10.1021/acsami.7b17701>{: target="_blank"}
[^ref138]: <https://doi.org/10.1002/smll.201800547>{: target="_blank"}
[^ref139]: <https://doi.org/10.1016/j.apsusc.2018.04.115>{: target="_blank"}
[^ref140]: <https://doi.org/10.1038/s41467-018-03285-x>{: target="_blank"}
[^ref141]: <https://doi.org/10.1002/aenm.201702888>{: target="_blank"}
[^ref142]: <https://doi.org/10.1021/acsami.7b05214>{: target="_blank"}
[^ref143]: <https://doi.org/10.1039/C6RA24733D>{: target="_blank"}
[^ref144]: <https://doi.org/10.1021/acs.chemmater.6b04251>{: target="_blank"}
[^ref145]: <https://doi.org/10.1002/anie.201611838>{: target="_blank"}
[^ref146]: <https://doi.org/10.1021/acsami.6b13033>{: target="_blank"}
[^ref147]: <https://doi.org/10.1007/s00339-017-1018-y>{: target="_blank"}
[^ref148]: <https://doi.org/10.1016/j.tsf.2017.03.025>{: target="_blank"}
[^ref149]: <https://doi.org/10.1021/acsami.7b03398>{: target="_blank"}
[^ref150]: <https://doi.org/10.1021/acs.chemmater.6b04029>{: target="_blank"}
[^ref151]: <https://doi.org/10.1016/j.tsf.2016.12.021>{: target="_blank"}
[^ref152]: <https://doi.org/10.1016/j.apsusc.2017.05.012>{: target="_blank"}
[^ref153]: <https://doi.org/10.1021/acsami.6b11613>{: target="_blank"}
[^ref154]: <https://doi.org/10.1021/acs.chemmater.7b02456>{: target="_blank"}
[^ref155]: <https://doi.org/10.1039/C6CP01900E>{: target="_blank"}
[^ref156]: <https://doi.org/10.1016/j.apsusc.2018.03.099>{: target="_blank"}
[^ref157]: <https://doi.org/10.1063/1.2370425>{: target="_blank"}
[^ref158]: <https://doi.org/10.1063/1.4896501>{: target="_blank"}
[^ref159]: <https://doi.org/10.1063/1.4803486>{: target="_blank"}
[^ref160]: <https://doi.org/10.3390/ma11030386>{: target="_blank"}
[^ref161]: <https://doi.org/10.1149/MA2018-02/30/985>{: target="_blank"}
[^ref162]: <https://doi.org/10.1021/acs.chemmater.8b03165>{: target="_blank"}
[^ref163]: <https://doi.org/10.1016/j.apsusc.2018.11.064>{: target="_blank"}
[^ref164]: <https://doi.org/10.1080/14686996.2016.1167571>{: target="_blank"}
[^ref165]: <https://doi.org/10.1016/j.partic.2016.07.003>{: target="_blank"}
[^ref168]: <https://doi.org/10.1002/chem.201702939>{: target="_blank"}
[^ref171]: <https://doi.org/10.1002/pip.2540>{: target="_blank"}
[^ref182]: <https://doi.org/10.1002/pssr.201409044>{: target="_blank"}
[^ref183]: <https://doi.org/10.1116/1.4892939>{: target="_blank"}
[^ref184]: <https://doi.org/10.1002/pssa.201228303>{: target="_blank"}
[^ref185]: <https://doi.org/10.1109/LED.2013.2296604>{: target="_blank"}
[^ref186]: <https://doi.org/10.1186/s11671-017-1999-7>{: target="_blank"}
[^ref187]: <https://doi.org/10.1021/acsami.7b04637>{: target="_blank"}
[^ref188]: <https://doi.org/10.1038/srep02737>{: target="_blank"}
[^ref189]: <https://doi.org/10.1063/1.4826583>{: target="_blank"}
[^ref190]: <https://doi.org/10.1039/C4TC01727G>{: target="_blank"}
[^ref191]: <https://doi.org/10.1016/j.mee.2016.03.038>{: target="_blank"}
[^ref192]: <https://doi.org/10.1186/s11671-017-2414-0>{: target="_blank"}
[^ref193]: <https://doi.org/10.1166/jno.2017.2006>{: target="_blank"}
[^ref194]: <https://doi.org/10.3390/ma7042913>{: target="_blank"}
[^ref197]: <https://doi.org/10.1109/LED.2015.2412685>{: target="_blank"}
[^ref198]: <http://hdl.handle.net/1957/61522>{: target="_blank"}
[^ref199]: <https://doi.org/10.1016/j.jallcom.2017.06.036>{: target="_blank"}
[^ref202]: <https://doi.org/10.1039/C7TA02719B>{: target="_blank"}
[^ref208]: <https://www.samsung.com/semiconductor/newsroom/tech-trends/exploring-the-key-samsung-technologies-that-enabled-10nm-class-dram/>{: target="_blank"}
[^ref210]: <https://doi.org/10.1038/nnano.2010.13>{: target="_blank"}
[^ref211]: <https://doi.org/10.1021/cm300203s>{: target="_blank"}
[^ref228]: <https://doi.org/10.1016/j.desal.2017.07.015>{: target="_blank"}
[^ref232]: <https://doi.org/10.1021/nl3014956>{: target="_blank"}
[^ref233]: <https://doi.org/10.5772/20801>{: target="_blank"}
[^ref234]: <https://doi.org/10.1021/acs.nanolett.5b04089>{: target="_blank"}
[^ref235]: <https://doi.org/10.1021/nl3012853>{: target="_blank"}
[^ref238]: <https://doi.org/10.1116/1.5000587>{: target="_blank"}
[^ref239]: <http://bitly.kr/jFBR1zGgrn>{: target="_blank"}
[^ref240]: <https://doi.org/10.1063/1.4928614>{: target="_blank"}
[^ref242]: <https://doi.org/10.1002/app.39461>{: target="_blank"}
[^ref243]: <https://doi.org/10.1021/ar2001233>{: target="_blank"}
[^ref244]: <https://doi.org/10.1557/jmr.2011.434>{: target="_blank"}
[^ref245]: <https://doi.org/10.1007/s11837-009-0081-z>{: target="_blank"}
[^ref246]: <https://doi.org/10.1016/j.apsusc.2015.09.248>{: target="_blank"}
[^ref247]: <https://www.scitechnol.com/proceedings/nanocoating-of-drug-powders-and-minitablets-with-atomic-layer-deposition-5478.html>{: target="_blank"}
[^ref248]: <https://doi.org/10.1016/j.ijpharm.2017.04.031>{: target="_blank"}

----------

<!-- figures -->
[fig06]: https://www.tandfonline.com/na101/home/literatum/publisher/tandf/journals/content/tsta20/2019/tsta20.v020.i01/14686996.2019.1599694/20200603/images/large/tsta_a_1599694_f0006_oc.jpeg

[fig07]: https://www.tandfonline.com/na101/home/literatum/publisher/tandf/journals/content/tsta20/2019/tsta20.v020.i01/14686996.2019.1599694/20200603/images/large/tsta_a_1599694_f0007_oc.jpeg

[fig08]: https://www.tandfonline.com/na101/home/literatum/publisher/tandf/journals/content/tsta20/2019/tsta20.v020.i01/14686996.2019.1599694/20200603/images/large/tsta_a_1599694_f0008_oc.jpeg

[fig09]: https://www.tandfonline.com/na101/home/literatum/publisher/tandf/journals/content/tsta20/2019/tsta20.v020.i01/14686996.2019.1599694/20200603/images/large/tsta_a_1599694_f0009_oc.jpeg

[fig10]: https://www.tandfonline.com/na101/home/literatum/publisher/tandf/journals/content/tsta20/2019/tsta20.v020.i01/14686996.2019.1599694/20200603/images/large/tsta_a_1599694_f0010_oc.jpeg

[fig11]: https://www.tandfonline.com/na101/home/literatum/publisher/tandf/journals/content/tsta20/2019/tsta20.v020.i01/14686996.2019.1599694/20200603/images/large/tsta_a_1599694_f0011_oc.jpeg

[fig12]: https://www.tandfonline.com/na101/home/literatum/publisher/tandf/journals/content/tsta20/2019/tsta20.v020.i01/14686996.2019.1599694/20200603/images/large/tsta_a_1599694_f0012_oc.jpeg

[fig13]: https://www.tandfonline.com/na101/home/literatum/publisher/tandf/journals/content/tsta20/2019/tsta20.v020.i01/14686996.2019.1599694/20200603/images/large/tsta_a_1599694_f0013_oc.jpeg

[fig14]: https://www.tandfonline.com/na101/home/literatum/publisher/tandf/journals/content/tsta20/2019/tsta20.v020.i01/14686996.2019.1599694/20200603/images/large/tsta_a_1599694_f0014_oc.jpeg

[fig15]: https://www.tandfonline.com/na101/home/literatum/publisher/tandf/journals/content/tsta20/2019/tsta20.v020.i01/14686996.2019.1599694/20200603/images/large/tsta_a_1599694_f0015_oc.jpeg

[fig16]: https://www.tandfonline.com/na101/home/literatum/publisher/tandf/journals/content/tsta20/2019/tsta20.v020.i01/14686996.2019.1599694/20200603/images/large/tsta_a_1599694_f0016_oc.jpeg

[fig17]: https://www.tandfonline.com/na101/home/literatum/publisher/tandf/journals/content/tsta20/2019/tsta20.v020.i01/14686996.2019.1599694/20200603/images/large/tsta_a_1599694_f0017_oc.jpeg