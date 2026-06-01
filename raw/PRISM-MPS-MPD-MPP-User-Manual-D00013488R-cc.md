## **PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

This document supports software version 5.4 **D00013488R**

**March 2026**

**2**

## **Copyrights and Trademark Notices**

Telestream® is a registered trademark of Telestream 2 LLC. All third-party trademarks are the property of their respective owners. Copyright © 2026 Telestream 2 LLC. All rights reserved.

Telestream products are covered by U.S. and foreign patents, issued and pending. Information in this publication supersedes that in all previously published material. Specifications and price change privileges reserved.

**Blender:** Images from Big Buck Bunny used without modification under the Creative Commons Attribution 3.0 license. (c) copyright 2008, Blender Foundation (http://peach.blender.org/about).

**Dolby:** Dolby and the double-D symbol are registered trademarks of Dolby Laboratories.

**Fraunhofer IIS and Thomson Multimedia** . MPEG Layer-3 audio coding technology licensed from Fraunhofer IIS and Thomson Multimedia.

**intoPIX and Fraunhofer** . Notice under 35 U.S.C. §287(a): This product or service includes JPEG XS compliant features that are covered by patents in the United States and in other jurisdictions owned by intoPIX SA (“intoPIX”) and/or FraunhoferGesellschaft zur Föerderung der angewandten Forschung E.V. (“Fraunhofer”) and listed at https://www.jpegxspool.com. Additional patents may be pending in United States and elsewhere.

## **Warranty**

Telestream on behalf of itself and its Affiliates (“Telestream”) warrants that this product will be free from defects in materials and workmanship for a period of one (1) year from the date of shipment. If any such product proves defective during this warranty period, Telestream, at its option, either will repair the defective product without charge for parts and labor, or will provide a replacement in exchange for the defective product. Parts, modules and replacement products used by Telestream for warranty work may be new or reconditioned to like new performance. All replaced parts, modules and products become the property of Telestream.

In order to obtain service under this warranty, Customer must notify Telestream of the defect before the expiration of the warranty period and make suitable arrangements for the performance of service. Customer shall be responsible for packaging and shipping the defective product to the service center designated by Telestream, with shipping charges prepaid. Telestream shall pay for the return of the product to Customer if the shipment is to a location within the country in which the Telestream service center is located. Customer shall be responsible for paying all shipping charges, duties, taxes, and any other charges for products returned to any other locations.

This warranty shall not apply to any defect, failure or damage caused by improper use or improper or inadequate maintenance and care. Telestream shall not be obligated to furnish service under this warranty a) to repair damage resulting from attempts by

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**3**

personnel other than Telestream representatives to install, repair or service the product; b) to repair damage resulting from improper use or connection to incompatible equipment; c) to repair any damage or malfunction caused by the use of non- Telestream supplies; or d) to service a product that has been modified or integrated with other products when the effect of such modification or integration increases the time or difficulty of servicing the product.

THIS WARRANTY IS GIVEN BY TELESTREAM WITH RESPECT TO THE PRODUCT IN LIEU OF ANY OTHER WARRANTIES, EXPRESS OR IMPLIED. TELESTREAM AND ITS VENDORS DISCLAIM ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. TELESTREAM’S RESPONSIBILITY TO REPAIR OR REPLACE DEFECTIVE PRODUCTS IS THE SOLE AND EXCLUSIVE REMEDY PROVIDED TO THE CUSTOMER FOR BREACH OF THIS WARRANTY. TELESTREAM AND ITS VENDORS WILL NOT BE LIABLE FOR ANY INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES IRRESPECTIVE OF WHETHER TELESTREAM OR THE VENDOR HAS ADVANCE NOTICE OF THE POSSIBILITY OF SUCH DAMAGES.

[W2 – 15AUG04]

## **Telestream Software License Agreement**

THE PROGRAM, OR PROGRAMS, ENCODED OR INCORPORATED WITHIN EQUIPMENT OR ACCOMPANYING THIS AGREEMENT, IS FURNISHED SUBJECT TO THE TERMS AND CONDITIONS OF THIS AGREEMENT. RETENTION OF THE PROGRAM FOR MORE THAN THIRTY DAYS OR USE OF THE PROGRAM IN ANY MANNER WILL BE CONSIDERED ACCEPTANCE OF THE AGREEMENT TERMS. IF THESE TERMS ARE NOT ACCEPTABLE, THE UNUSED PROGRAM AND ANY ACCOMPANYING DOCUMENTATION SHOULD BE RETURNED PROMPTLY TO TELESTREAM FOR A FULL REFUND OF THE LICENSE FEE PAID. (FOR INFORMATION REGARDING THE RETURN OF PROGRAMS ENCODED OR INCORPORATED WITHIN EQUIPMENT, CONTACT THE NEAREST TELESTREAM SALES OFFICE.)

## **Definitions**

“Telestream” means Telestream 2 LLC, a Delaware limited liability company, and its Affiliates, or the local Telestream legal entity that is supplying the equipment. “Program” means the Telestream software product (executable program and/or data) enclosed with this Agreement or included within the equipment with which this Agreement is packed. “Customer” means the person or organization in whose name the Program was ordered.

## **License**

Customer may:

**1.** Use the Program on a single machine at any one time; and

**2.** Copy the Program for archival or backup purposes, provided that no more than one (1) such copy is permitted to exist at any one time. Each copy of the Program

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**4**

made by Customer must include a reproduction of any copyright notice or restrictive rights legend appearing in or on the copy of the Program as received from Telestream.

Customer may not:

**1.** Use the Program on more than one machine at any one time;

**2.** Transfer the Program to any person or organization outside of Customer or the corporation of which Customer is a part without the prior written consent of Telestream, except in connection with the transfer of the equipment within which the programs are encoded or incorporated;

**3.** Export or re-export, directly or indirectly, the program, any associated documentation, or the direct product thereof, to any country to which such export or re-export is restricted by law or regulation of the United States or any foreign government having jurisdiction without the prior authorization, if required, of the Office of Export Administration, Department of Commerce, Washington, D.C. and the corresponding agency of such foreign government;

**4.** Modify the Program, create derivative works, or merge the Program with another program;

**5.** Reverse compile or disassemble the Program for any purpose, beyond the extent that such activity is expressly permitted by applicable open source licenses or applicable law notwithstanding this limitation; or

**6.** Copy the documentation accompanying the Program.

For Programs designed to reside on a single-machine and support one or more additional machines, either locally or remotely, without permitting the Program to be transferred to an additional machine for local execution, the additional machines shall be considered within the definition of “single machine.” For programs permitting the Program to be transferred to an additional machine for local execution, a separate license shall be required for each such machine with which the Program may be used. Title to the Program and all copies thereof, but not the media on which the Program or copies may reside, shall be and remain with Telestream or others for whom Telestream has obtained a respective licensing right. Customer shall pay when due all property taxes that may now or hereafter be imposed, levied or assessed with respect to the possession or use of the Program or this license and shall file all reports required in connection with such taxes. If the Program or any related documentation is acquired by or for an agency of the U.S. Government, the Program and documentation shall be considered “commercial computer software” or “commercial computer software documentation” respectively, as those terms are used in 48 CFR §12.212, 48 CFR §227.7202, or 48 CFR §252.227-7014, and are licensed with only those rights as are granted to all other licensees as set forth in this Agreement.

THE PROGRAM MAY NOT BE USED, COPIED, MODIFIED, MERGED, OR TRANSFERRED TO ANOTHER EXCEPT AS EXPRESSLY PERMITTED BY THESE TERMS AND CONDITIONS. UPON TRANSFER OF ANY COPY, MODIFICATION, OR MERGED PORTION OF THE PROGRAM, THE LICENSE GRANTED HEREIN IS AUTOMATICALLY TERMINATED WITH RESPECT TO THE PARTY THAT TRANSFERS THE PROGRAM.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**5**

## **Term**

The license granted herein is effective upon acceptance by Customer, and shall remain in effect until terminated as provided herein. The license may be terminated by Customer at any time upon written notice to Telestream. The license may be terminated by Telestream or any third party from whom Telestream may have obtained a respective licensing right if Customer fails to comply with any term or condition and such failure is not remedied within thirty (30) days after notice hereof from Telestream or such third party. Upon termination by either party, Customer shall return to Telestream or destroy, the Program and all associated documentation, together with all copies in any form.

## **Limited Warranty**

The Program is provided “as is” without warranty of any kind, either express or implied. Telestream does not warrant that the functions contained in the Program will meet Customer's requirements or that the operation of the Program will be uninterrupted or error-free.

TELESTREAM AND ITS VENDORS DISCLAIM ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. LIMITATION OF LIABILITY, IN NO EVENT SHALL TELESTREAM OR OTHERS FROM WHOM TELESTREAM HAS OBTAINED A LICENSING RIGHT BE LIABLE FOR ANY INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING OUT OF OR CONNECTED WITH CUSTOMER'S POSSESSION OR USE OF THE PROGRAM, EVEN IF TELESTREAM OR SUCH OTHERS HAS ADVANCE NOTICE OF THE POSSIBILITY OF SUCH DAMAGES.

## **Third-party Disclaimer**

Except as expressly agreed otherwise, third parties from whom Telestream may have obtained a licensing right do not warrant the program, do not assume any liability with respect to its use, and do not undertake to furnish any support or information relating thereto.

## **General**

This Agreement contains the entire agreement between the parties with respect to the use, reproduction, and transfer of the Program. Neither this Agreement nor the license granted herein is assignable or transferable by Customer without the prior written consent of Telestream. This Agreement and the license granted herein shall be governed by the laws of the state of California. All questions regarding this Agreement or the license granted herein should be directed to the nearest Telestream Sales Office.

## **Third-party Software License**

The PRISM MPS, MPD, and MPP products use open source software from the Linux FFmpeg project (FFmpeg), which is licensed under LGPL v2.1. The FFmpeg source code

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**6**

has been modified for use on the PRISM, so a copy of the modified source code will be made available upon request in accordance with the LGPL v2.1 license. Visit www.telestream.net/telestreamsupport/video/support.htm to find contacts in your area.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Important Compliance and Safety Information 7**

## **Important Compliance and Safety Information**

## **United States of America Compliance Notices**

## **Class A Interference Statement**

This equipment has been tested and found to comply with the limits for a Class A digital device, pursuant to Part 15, Subpart B of the FCC Rules. These limits are designed to provide reasonable protection against harmful interference in a commercial installation. This equipment generates, uses, and can radiate radio frequency energy and, if not installed and used in accordance with the instructions, may cause harmful interference to radio communications. However, there is no guarantee that interference will not occur in a particular installation. Operation of this equipment in a residential area is likely to cause harmful interference in which the user will be required to correct the interference at the user’s expense.

## **FCC Caution**

This device complies with Part 15 of the FCC Rules. Operation is subject to the following two conditions:

**1.** This device may not cause harmful interference, and

**2.** This device must accept any interference received, including interference that may cause undesired operation.

## **Safety**

UL 61010-1: 2012 R7.19: Safety Requirements for Electrical Equipment for Measurement, Control, and Laboratory Use - Part 1: General Requirements.

## **Environmental**

Perchlorate Materials: this product contains one or more type CR lithium batteries. According to the state of California, CR lithium batteries are classified as perchlorate materials and require special handling.

See _www.dtsc.ca.gov/hazardouswaste/perchlorate_ for additional information.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **8 Important Compliance and Safety Information**

## **Canada Compliance Notices**

## **Department of Communications Radio Interference Regulations**

This digital apparatus does not exceed the Class A limits for radio-noise emissions from a digital apparatus as set out in the Radio Interference Regulations of the Canadian Department of Communications. This Class A digital apparatus complies with Canadian ICES-003.

## **Règlement sur le brouillage radioélectrique du Quadstere des Communications**

Cet appareil numérique respecte les limites de bruits radioélectriques visant les appareils numériques de classe A prescrites dans le Règlement sur le brouillage radioélectrique du Quadstere des Communications du Canada. Cet appareil numérique de la Classe A est conforme à la norme NMB-003 du Canada.

## **Safety**

CAN/CSA-C22.2 NO. 61010-1-12 + GI1 + GI2 (R2017) + A1: Safety Requirements for Electrical Equipment for Measurement, Control, and Laboratory Use - Part 1: General Requirements.

## **Sécurité**

CAN/CSA-C22.2 NO. 61010-1-12 + GI1 + GI2 (R2017) + A1: Exigences de sécurité pour l'électricité Matériel de mesure, de contrôle et d'utilisation en laboratoire - Partie 1: Généralités Exigences.

## **European Union, European Free Trade Association (EFTA), and United Kingdom Compliance Notices**

This equipment may be operated in the countries that comprise the member countries of the European Union and the European Free Trade Association. These countries, listed in the following paragraph, are referred to as The European Community throughout this document:

AUSTRIA, BELGIUM, BULGARIA, CYPRUS, CROATIA, CZECHIA, DENMARK, ESTONIA, FINLAND, FRANCE, GERMANY, GREECE, HUNGARY, IRELAND, ITALY, LATVIA, LITHUANIA, LUXEMBOURG, MALTA, NETHERLANDS, POLAND, PORTUGAL, ROMANIA, SLOVAKIA, SLOVENIA, SPAIN, SWEDEN, UNITED KINGDOM, ICELAND, LICHTENSTEIN, NORWAY, SWITZERLAND

## **Declaration of Conformity**

Marking by the “CE” symbol indicates compliance with the Essential Requirements of the EMC Directive of the European Union 2014/30/EU

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Important Compliance and Safety Information 9**

This equipment meets the following conformance standards:

## **Safety**

EN 61010-1: 2010 + A1: Safety Requirements for Electrical Equipment for Measurement, Control, and Laboratory Use - Part 1: General Requirements Low Voltage Directive 2014/35/EU

## **Emissions**

EN 55032: 2015 + A11: 2020, CISPR 32: 2015, EN 61000-3-2: 2014, EN 61000-3-3: 2013

## **Immunity**

EN 55035: 2017, EN 61000-4-2: 2009,

EN 61000-4-3: 2006 + A1: 2008 + A2: 2010, EN 61000-4-4: 2012, EN 61000-4-5: 2014 + A1: 2017, EN 61000-4-6: 2014, EN 61000-4-8: 2010, EN 61000-4-11: 2020

Environments: E2

## **Warnings**

- Warning! This is a Class A product. In a domestic environment, this product may cause radio interference, in which case, the user may be required to take appropriate measures.

- Achtung! Dies ist ein Gerät der Funkstörgrenzwertklasse A. In Wohnbereichen konnen bei Betrieb dieses Gerätes Rundfunkstörungen auftreten, in welchen Fallen der Benutzer für entsprechende Gegenmalßnahmen verantwortlich ist.

- Attention! Ceci est un produit de Classe A. Dans un environnement domestique, ce produit risque de créer des interférences radioélectriques, il appartiendra alors a l’utilisateur a prendre des mesures spécifiques appropriées.

Notes:

**1.** For Compliance with the EMC standards listed here, high-quality shielded interface cables should be used.

**2.** Emissions which exceed the levels required by this standard may occur when this equipment is connected to a test object.

## **Environmental Compliance**

This section provides information about the environmental impact of the product.

## _Product End-of-Life Handling_

Observe the following guidelines when recycling an instrument or component:

## _Equipment Recycling_

Production of this equipment required the extraction and use of natural resources. The equipment may contain substances that could be harmful to the environment or

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **10 Important Compliance and Safety Information**

human health if improperly handled at the product's end of life. To avoid release of such substances into the environment and to reduce the use of natural resources, we encourage you to recycle this product in an appropriate system that will ensure that most of the materials are reused or recycled appropriately.

This symbol on the product or its packaging indicates that this product complies with the applicable European Union requirements according to Directives 2012/19/EU and 2006/66/EC on waste electrical and electronic - equipment (WEEE) and batteries.

It also indicates that this product must not be disposed of with your other household waste. Instead, it is your responsibility to dispose of your waste equipment by handing it over to a designated collection point for the recycling of waste electrical and electronic equipment. The separate collection and recycling of your waste equipment at the time of disposal will help conserve natural resources and ensure that it is recycled in a manner that protects human health and the environment. For more information about where you can drop off your waste for recycling, please contact your local authority, or where you purchased your product.

## _Battery Recycling_

This product may contain a rechargeable battery, which must be recycled or disposed of properly. Please properly dispose of or recycle the battery according to local government regulations.

## _Transporting Batteries or Products with Batteries in them_

The capacity of the lithium-ion secondary battery shipped with this product is under 100 Wh. The lithium content of the installed primary battery is under 1 g. Each battery meets the applicable requirements of UN Manual of Tests and Criteria Part Ill Section 38.3. Battery quantity is under the limit for shipment according to Section II of the relevant Packing Instructions from the IATA Dangerous Goods Regulations. Consult your air carrier for applicability and determination of any special lithium battery transportation requirements.

## _Restriction of Hazardous Substances_

This product is classified as an industrial monitoring and control instrument, and is required to comply with the substance restrictions of the RoHS 3 Directives 2011/65/EU and EU 2015/863.

## **Korea Compliance Statement**

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Important Compliance and Safety Information 11**

## **Taiwan Compliance Statement**

This is a Class A product based on the standard of the Bureau of Standards, Metrology and Inspection (BSMI) CNS 13438, Class A. In a domestic environment this product may cause radio interference, in which case the user may be required to take adequate measures.

## **Japan Compliance Statement**

This is a Class A product based on the standard of the VCCI Council (VCCI 32: 2016). If this equipment is used in a domestic environment, radio interference may occur, in which case the user may be required to take corrective actions.

## **Important Safety Information**

This manual contains information and warnings that must be followed by the user for safe operation and to keep the product in a safe condition. To safely perform service on this product, see the Service Safety Summary that follows the General Safety Summary.

## **General Safety Summary**

Use the product only as specified. Review the following safety precautions to avoid injury and prevent damage to this product or any products connected to it. Carefully read all instructions. Retain these instructions for future reference.

## **Comply with Local and National Safety Codes**

For correct and safe operation of the product, it is essential that you follow generally accepted safety procedures in addition to the safety precautions specified in this manual.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **12 Important Compliance and Safety Information**

## **Product is Designed to be Used by Trained Personnel Only**

Only qualified personnel who are aware of the hazards involved should remove the cover for repair, maintenance, or adjustment. Before use, always check the product with a known source to be sure it is operating correctly.

While using this product, you may need to access other parts of a larger system. Read the safety sections of the other component manuals for warnings and cautions related to operating the system.

When incorporating this equipment into a system, the safety of that system is the responsibility of the assembler of the system.

## **To Avoid Fire or Personal Injury**

_Use proper power cord:_ Use only the power cord specified for this product and certified for the country of use. Do not use the provided power cord for other products.

_Ground the product:_ This product is grounded through the grounding conductor of the power cord. To avoid electric shock, the grounding conductor must be connected to earth ground. Before making connections to the input or output terminals of the product, ensure that the product is properly grounded. Do not disable the power cord grounding connection.

_Power disconnect:_ The power cord disconnects the product from the power source. See instructions for the location. Do not position the equipment so that it is difficult to operate the power cord; it must remain accessible to the user at all times to allow for quick disconnection if needed.

_Observe all terminal ratings:_ To avoid fire or shock hazard, observe all rating and markings on the product. Consult the product manual for further ratings information before making connections to the product. Do not apply a potential to any terminal, including the common terminal, that exceeds the maximum rating of that terminal.

_Do not operate without covers:_ Do not operate this product with covers or panels removed, or with the case open. Hazardous voltage exposure is possible.

_Avoid exposed circuitry:_ Do not touch exposed connections and components when power is present.

_Do not operate with suspected failures:_ If you suspect that there is damage to this product, have it inspected by qualified service personnel.

_Disable the product if it is damaged._ Do not use the product if it is damaged or operates incorrectly. If in doubt about safety of the product, turn it off and disconnect the power cord. Clearly mark the product to prevent its further operation.

Before use, inspect voltage probes, test leads, and accessories for mechanical damage and replace when damaged. Do not use probes or test leads if they are damaged, if there is exposed metal, or if a wear indicator shows.

Examine the exterior of the product before you use it. Look for cracks or missing pieces.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Important Compliance and Safety Information 13**

## **Use Only Specified Replacement Parts**

Do not operate in wet/damp conditions: Be aware that condensation may occur if a unit is moved from a cold to a warm environment.

Do not operate in an explosive atmosphere.

Keep product surfaces clean and dry: Remove the input signals before you clean the product.

Provide proper ventilation: Refer to the manual's installation instructions for details about installing the product so it has proper ventilation.

Slots and openings are provided for ventilation and should never be covered or otherwise obstructed. Do not push objects into any of the openings.

Provide a safe working environment: Always place the product in a location convenient for viewing the display and indicators.

Be sure your work area meets applicable ergonomic standards. Consult with an ergonomics professional to avoid stress injuries.

Use only the Telestream rack-mount hardware specified for this product.

## **Service Safety Summary**

The Service Safety Summary section contains additional information required to safely perform service on the product. Only qualified personnel should perform service procedures. Read this Service Safety Summary and the General Safety Summary before performing any service procedures.

_To avoid electric shock:_ Do not touch exposed connections.

_Do not service alone:_ Do not perform internal service or adjustments of this product unless another person capable of rendering first aid and resuscitation is present.

_Disconnect power:_ To avoid electric shock, switch off the product power and disconnect the power cord from the mains power before removing any covers or panels, or opening the case for servicing.

_Use care when servicing with power on:_ Dangerous voltages or currents may exist in this product. Disconnect power, remove battery (if applicable), and disconnect test leads before removing protective panels, soldering, or replacing components.

_Verify safety after repair:_ Always recheck ground continuity and mains dielectric strength after performing a repair.

## **Terms in the Manual**

These terms may appear in this manual:

_**WARNING:** Warning statements identify conditions or practices that could result in injury or loss of life._ ~~CO~~

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **14 Important Compliance and Safety Information**

**CAUTION: Caution statements identify conditions or practices that could result in damage to this product or other property.**

## **Terms on the Product**

These terms may appear on the product:

_DANGER_ indicates an injury hazard immediately accessible as you read the marking.

WARNING indicates an injury hazard not immediately accessible as you read the marking.

_CAUTION_ indicates a hazard to property including the product.

## **Symbols on the Product**

When this symbol is marked on the product, be sure to consult the manual to find out the nature of the potential hazards and any actions which have to be taken to avoid them. (This symbol might also be used to refer the user to ratings in the manual.)

The following symbol(s) might appear on the product:

## **General Safety Product Specific Statements**

Use the product only as specified. Review the following safety precautions to avoid injury and prevent damage to this product or any products connected to it.

Carefully read all instructions. Retain these instructions for future reference.

Comply with local and national safety codes.

For correct and safe operation of the product, it is essential that you follow generally accepted safety procedures in addition to the safety precautions specified in this manual. The product is designed to be used by trained personnel only.

Only qualified personnel who are aware of the hazards involved should remove the cover for repair, maintenance, or adjustment.

Before use, always check the product with a known source to be sure it is operating correctly.

This product is not intended for detection of hazardous voltages.

Use personal protective equipment to prevent shock and arc blast injury where hazardous live conductors are exposed.

When incorporating this equipment into a system, the safety of that system is the responsibility of the assembler of the system.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Preface 15**

## **Preface**

This manual contains information to help you use the PRISM SDI/IP Waveform Monitor:

- How to operate the instrument using the front panel, external mouse, keyboard, display, or remote connection.

- How to use the various applications for monitoring SDI or IP video signals.

- How to configure the instrument for network and remote access.

- How to set up error logging and alarms.

## **Where to Find More Information**

The full User Manual, Release Notes, and other information about your product are available for download at www.telestream.net/video/resources.htm. The Product documentation table lists all the documentation for the PRISM SDI / IP Waveform Monitor.

## Product documentation

| Product documentation  |                 |                 |                                          |
| ---------------------- | --------------- | --------------- | ---------------------------------------- |
| **Document**           | **Manual type** | **Part number** | **Description**                          |
| MPS, MPD, and MPP User | User            | D00013488x      | Provides detailed operating information. |
| Manual                 |                 |                 |                                          |
| Release Notes          | Release Notes   | D00010030x      | Describes the new features,              |
|                        |                 |                 | improvements, and limitations of the     |
|                        |                 |                 | instrument firmware.                     |
| Read-this-first        | User            | P00010449x      | Lists all relevant documents.            |
| MPS Installation and   | User            | P00010445x      | Describes the set up of a PRISM MPS      |
| Safety Instructions    |                 |                 | instrument, and provides basic safety    |
|                        |                 |                 | and operating information.               |
| MPD Installation and   | User            | P00010446x      | Describes how to install and set up a    |
| Safety Instructions    |                 |                 | PRISM MPD instrument, and provides       |
|                        |                 |                 | basic safety and operating information.  |
| MPP Installation and   | User            | P00010588x      | Describes how to install and set up a    |
| Safety Instructions    |                 |                 | PRISM MPP instrument, and provides       |
|                        |                 |                 | basic safety and operating information.  |

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **16 Preface**

## Product documentation

| Product documentation  |                 |                 |                                          |
| ---------------------- | --------------- | --------------- | ---------------------------------------- |
| **Document**           | **Manual type** | **Part number** | **Description**                          |
| MPS Rack Accessory     | User            | P00010448x      | Describes how to connect rack            |
| Installation Manual    |                 |                 | equipment to a PRISM MPS instrument      |
|                        |                 |                 | and install it in a rack. Provides basic |
|                        |                 |                 | safety and operating information.        |
| MPS Portable Accessory | User            | P00010447x      | Describes how to connect portable        |
| Installation Manual    |                 |                 | accessory equipment to a PRISM MPS       |
|                        |                 |                 | instrument. Provides basic safety and    |
|                        |                 |                 | operating information.                   |

## **Conventions Used in this Manual**

The PRISM SDI / IP Waveform Monitor is also referred to as the “PRISM monitor” throughout this manual.

## **Telestream Contact Information**

To obtain product information, technical support, or provide comments on this guide, contact us using our website, email, or phone number listed.

| **Resource**     | **Contact Information**                              |
| ---------------- | ---------------------------------------------------- |
| Telestream Video | Website:http://www.telestream.net/telestream-support |
| Support          | Email: videosupport@telestream.net                   |
|                  | US and Canada Toll-free: 1-844-219-5329              |
|                  | Outside of US and Canada: 1-503-967-9833             |
| Telestream       | Website:www.telestream.net                           |
|                  | Sales and Marketing Email: info@telestream.net       |
|                  | Address:                                             |
|                  | Telestream                                           |
|                  | 848 Gold Flat Road, Suite 1                          |
|                  | Nevada City, CA 95959                                |
|                  | USA                                                  |

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Preface 17**

| **Resource**         | **Contact Information**                                  |
| -------------------- | -------------------------------------------------------- |
| International        | Website:www.telestream.net                               |
| Distributor Support  | See the Telestream website for your regional authorized  |
|                      | Telestream distributor.                                  |
| Telestream Technical | Email: techwriter@telestream.net                         |
| Writers              | If you have comments or suggestions about improving      |
|                      | this document, or other Telestream documents—or if       |
|                      | you've discovered an error or omission, please email us. |

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **18 Contents**

## **Contents**

**Important Compliance and Safety Information ............................................ 7 Preface ............................................................................................................ 15 Contents ......................................................................................................... 18 Getting Started .............................................................................................. 20** Product Description ...................................................................................................................... 20 Accessories ....................................................................................................................................... 27 Power-on and Power-off Procedures ..................................................................................... 28 SFP Module Installation ............................................................................................................... 30 Network Installation ...................................................................................................................... 31 Managing Network Ports ............................................................................................................ 33 MPS Connectors ............................................................................................................................. 34 MPD Connectors ............................................................................................................................ 39 MPP Connectors ............................................................................................................................. 44 Secure Web Interface .................................................................................................................... 48 Display Elements ............................................................................................................................ 50 **Methods of Operation ................................................................................... 59** Touchscreen ..................................................................................................................................... 59 Select and Organize Applications ............................................................................................ 61 On-Screen Tools ............................................................................................................................. 66 Keyboard and Mouse Operation .............................................................................................. 67 Configure Extended Display ...................................................................................................... 68 Remote Control Operation ......................................................................................................... 71 Camera Tally and UMD ................................................................................................................ 79 **Configure the Instrument ............................................................................. 84** Configure and Select Virtual Inputs ........................................................................................ 84 Configure Instrument for HDR/WCG Monitoring ............................................................ 138 Using NMOS .................................................................................................................................. 142 Adjust Audio Settings ................................................................................................................ 148 Configure Instrument Outputs .............................................................................................. 151 Configure to Decode Timecode ............................................................................................ 155 Configure Reference Settings ................................................................................................. 156 Configure and Recall Instrument Presets ........................................................................... 159 Configure Syslog ......................................................................................................................... 169 SNMP Functionality .................................................................................................................... 170 Configure Alarms ........................................................................................................................ 172 Adjust Display .............................................................................................................................. 183 Configure Time and Date ......................................................................................................... 190 Upgrade Instrument Firmware .............................................................................................. 192 Upgrade Software License ....................................................................................................... 196

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Contents 19**

Troubleshooting .......................................................................................................................... 196 **Functions ..................................................................................................... 198** Headphone or Speaker Volume, Balance, Device, and Source Adjustment .......... 198 Capture ........................................................................................................................................... 201 **Application Information ............................................................................ 206** Application Options ................................................................................................................... 206 Waveform Application .............................................................................................................. 212 Vector Application ...................................................................................................................... 225 Lightning Application ............................................................................................................... 234 Diamond Application ................................................................................................................ 242 CIE Application ............................................................................................................................. 248 Stop Display Application .......................................................................................................... 253 CAM Application ......................................................................................................................... 263 Picture Application ..................................................................................................................... 273 Video Session Application ....................................................................................................... 291 Audio Application ....................................................................................................................... 298 Dolby Status Application ......................................................................................................... 319 AES Channel Status Application ............................................................................................ 325 Event Log Application ............................................................................................................... 326 IP Status Application .................................................................................................................. 333 IP Session Application ............................................................................................................... 337 IP Graphs Application ................................................................................................................ 352 PIT Histogram Application ....................................................................................................... 358 PTP Graphs Application ............................................................................................................ 361 Stream Timing Application ...................................................................................................... 363 ANC (Ancillary Data) Session Application .......................................................................... 369 Datalist Application .................................................................................................................... 371 Timing Application ..................................................................................................................... 374 Eye Application ............................................................................................................................ 377 Jitter Application ......................................................................................................................... 379 External Reference Application ............................................................................................. 381 Audio-Video Delay Application ............................................................................................. 386 IP Display and Generator Applications ............................................................................... 389 SDI Generator Application ....................................................................................................... 403 **PTP Operational Overview ........................................................................ 406** PTP Introduction ......................................................................................................................... 406 Five Basic PTP Timing Messages ............................................................................................ 407 Profiles and Domains ................................................................................................................. 408 One-Step and Two-Step Operation ...................................................................................... 409 Multicast, Unicast, and Mixed Communication Modes ................................................ 409 BMCA Operation ......................................................................................................................... 411 Compensating for Causes of Asymmetric Delay ............................................................. 412 **NMOS Specifications .................................................................................. 414** NMOS Discovery Version 1.3 ................................................................................................... 414

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **20 Getting Started** Product Description

## **Getting Started**

This chapter helps you set up and begin to use the PRISM SDI / IP Waveform Monitor.

## **Topics**

- **Product description** describes the instrument and key features.

- **Controls and Connectors** shows how to verify that you have received all of the parts of the instrument, lists standard and optional accessories, and lists options for the instrument.

- **Network Installation** shows how to set up the instrument on an Ethernet network.

## **Product Description**

The PRISM SDI / IP Waveform Monitor provides flexible options and field-installable upgrades to monitor a variety of SDI and IP statistics as well as video and audio content. The comprehensive feature set, along with an intuitive and simplified graphical presentation of IP statistics, including video quality and diagnostic information, allows engineers to ensure the delivery of superior Quality of Service (QoS) levels in an increasingly complex broadcast environment involving compressed or uncompressed video transmission through SDI/IP signal paths. PRISM is an ideal solution for monitoring SDI/IP hybrid environments including master control rooms, production studios, OB vans, and signal contribution or distribution centers.

## **PRISM Model Form Factors**

The PRISM SDI/IP Waveform Monitor is available in three form factors:

**MPS:** The PRISM MPS is 3RU half-rack width with an integrated 9-inch HD display and touch panel.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Getting Started 21** Product Description

**MPP:** The PRISM MPP is 1RU full-rack width. An external display or remote access is required for operation.

**MPD:** The PRISM MPD is 3RU full-rack width with two integrated 9-inch HD display and touch panels.

## **Supported Formats**

Supported SDI Formats

| Supported SDI Formats | Supported SDI Formats |               |       |          |                      |                 |
| --------------------- | --------------------- | ------------- | ----- | -------- | -------------------- | --------------- |
|                       |                       | **Sample**    |       |          |                      |                 |
| **Link**              | **Format**            | **Structure** |       | **Bits** | **Frame/Field Rate** | **Option**      |
| SD-SDI                | 525i                  | 4:2:2         | YCbCr | 10b      | 59.94i               | Base instrument |
|                       | 625i                  | 4:2:2         | YCbCr | 10b      | 50i                  | Base instrument |
| HD-SDI                | 1280x720              | 4:2:2         | YCbCr | 10b      | 23.98/24/25/29.97/   | Base instrument |
|                       |                       |               |       |          | 30/50/59.94/60p      |                 |
|                       | 1920x1080             | 4:2:2         | YCbCr | 10b      | 50/59.94/60i,        | Base instrument |
|                       |                       |               |       |          | 23.98/24/25/29.97/   |                 |
|                       |                       |               |       |          | 30p, and psF         |                 |
|                       | 2048x1080             | 4:2:2         | YCbCr | 10b      | 23.98/24/25/29.97/   | Base instrument |
|                       |                       |               |       |          | 30p, and psF         |                 |

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **22 Getting Started** Product Description

## Supported SDI Formats

|                             |            | **Sample**    |       |          |                      |                 |
| --------------------------- | ---------- | ------------- | ----- | -------- | -------------------- | --------------- |
| **Link**                    | **Format** | **Structure** |       | **Bits** | **Frame/Field Rate** | **Option**      |
| 3G-SDI Level A              | 1920x1080  | 4:2:2         | YCbCr | 10b      | 50/59.94/60p         | Base instrument |
|                             | 1920x1080  | 4:4:4         | RGB   | 10/12b   | 23.98/24/25/29.97/   | MPSDP-PROD      |
|                             |            |               |       |          | 30p                  |                 |
|                             | 2048x1080  | 4:2:2         | YCbCr | 10b      | 47.95/48/50/59.94/   | Base instrument |
|                             |            |               |       |          | 60p                  |                 |
|                             | 2048x1080  | 4:4:4         | RGB   | 10/12b   | 23.98/24/25/29.97/   | MPSDP-PROD      |
|                             |            |               |       |          | 30p                  |                 |
| 3G-SDI Level B              | 1920x1080  | 4:2:2         | YCbCr | 10b      | 50/59.94/60p         | Base instrument |
|                             | 1920x1080  | 4:4:4         | RGB   | 10/12b   | 23.98/24/25/29.97/   | MPSDP-PROD      |
|                             |            |               |       |          | 30p                  |                 |
|                             | 2048x1080  | 4:2:2         | YCbCr | 10b      | 47.95/48/50/59.94/   | Base instrument |
|                             |            |               |       |          | 60p                  |                 |
|                             | 2048x1080  | 4:4:4         | RGB   | 12b      | 23.98/24/25/29.97/   | MPSDP-PROD      |
|                             |            |               |       |          | 30p                  |                 |
| Quad Link HD-SDI            | 3840x2160  | 4:2:2         | YCbCr | 10b      | 23.98/24/25/29.97/   | MPSDP-FMT-4K    |
| Square Division             |            |               |       |          | 30p, and psF         |                 |
|                             | 4096x2160  | 4:2:2         | YCbCr | 10b      | 23.98/24/25/29.97/   | MPSDP-FMT-4K    |
|                             |            |               |       |          | 30p                  |                 |
| Quad Link 3G-SDI            | 3840x2160  | 4:2:2         | YCbCr | 10b      | 50/59.94/60p         | MPSDP-FMT-4K    |
| Level A, Square<br>Division | 3840x2160  | 4:4:4         | RGB   | 10/12b   | 23.98/24/25/29.97/   | MPSDP-FMT-4K    |
|                             |            |               |       |          | 30p                  | and MPSDP-      |
|                             |            |               |       |          |                      | PROD            |
|                             | 4096x2160  | 4:2:2         | YCbCr | 10b      | 47.95/48/50/59.94/   | MPSDP-FMT-4K    |
|                             |            |               |       |          | 60p                  |                 |
|                             | 4096x2160  | 4:4:4         | RGB   | 10/12b   | 23.98/24/25/29.97/   | MPSDP-FMT-4K    |
|                             |            |               |       |          | 30p                  | and MPSDP-      |
|                             |            |               |       |          |                      | PROD            |

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Getting Started 23** Product Description

## Supported SDI Formats

|                                   |            | **Sample**    |       |          |                           |                            |
| --------------------------------- | ---------- | ------------- | ----- | -------- | ------------------------- | -------------------------- |
| **Link**                          | **Format** | **Structure** |       | **Bits** | **Frame/Field Rate**      | **Option**                 |
| Quad Link 3G-SDI                  | 3840x2160  | 4:2:2         | YCbCr | 10b      | 50/59.94/60p              | MPSDP-FMT-4K               |
| Level B, Square<br>Division       | 3840x2160  | 4:4:4         | RGB   | 10/12b   | 23.98/24/25/29.97/        | MPSDP-FMT-4K               |
|                                   |            |               |       |          | 30p                       | and MPSDP-                 |
|                                   |            |               |       |          |                           | PROD                       |
|                                   | 4096x2160  | 4:2:2         | YCbCr | 10b      | 47.95/48/50/59.94/        | MPSDP-FMT-4K               |
|                                   |            |               |       |          | 60p                       |                            |
|                                   | 4096x2160  | 4:4:4         | RGB   | 10/12b   | 23.98/24/25/29.97/        | MPSDP-FMT-4K               |
|                                   |            |               |       |          | 30p                       | and MPSDP-                 |
|                                   |            |               |       |          |                           | PROD                       |
| Quad Link 3G-SDI                  | 3840x2160  | 4:2:2         | YCbCr | 10b      | 50/59.94/60p              | MPSDP-FMT-4K               |
| Level A, Two<br>Sample Interleave | 3840x2160  | 4:4:4         | RGB   | 10/12b   | 23.98/24/25/29.97/<br>30p | MPSDP-FMT-4K<br>and MPSDP- |
|                                   |            |               |       |          |                           | PROD                       |
|                                   | 4096x2160  | 4:2:2         | YCbCr | 10b      | 47.95/48/50/59.94/        | MPSDP-FMT-4K               |
|                                   |            |               |       |          | 60p                       |                            |
|                                   | 4096x2160  | 4:4:4         | RGB   | 10/12b   | 23.98/24/25/29.97/        | MPSDP-FMT-4K               |
|                                   |            |               |       |          | 30p                       | and MPSDP-                 |
|                                   |            |               |       |          |                           | PROD                       |
| Quad Link 3G-SDI                  | 3840x2160  | 4:2:2         | YCbCr | 10b      | 50/59.94/60p              | MPSDP-FMT-4K               |
| Level B, Two<br>Sample Interleave | 3840x2160  | 4:4:4         | RGB   | 10/12b   | 23.98/24/25/29.97/<br>30p | MPSDP-FMT-4K<br>and MPSDP- |
|                                   |            |               |       |          |                           | PROD                       |
|                                   | 4096x2160  | 4:2:2         | YCbCr | 10b      | 47.95/48/50/59.94/        | MPSDP-FMT-4K               |
|                                   |            |               |       |          | 60p                       |                            |
|                                   | 4096x2160  | 4:4:4         | RGB   | 10/12b   | 23.98/24/25/29.97/        | MPSDP-FMT-4K               |
|                                   |            |               |       |          | 30p                       | and MPSDP-                 |
|                                   |            |               |       |          |                           | PROD                       |
| 6G-SDI                            | 3840x2160  | 4:2:2         | YCbCr | 10b      | 23.98/24/25/29.97/        | MPSDP-FMT-4K               |
|                                   |            |               |       |          | 30p                       |                            |
|                                   | 4096x2160  | 4:2:2         | YCbCr | 10b      | 23.98/24/25/29.97/        | MPSDP-FMT-4K               |
|                                   |            |               |       |          | 30p                       |                            |

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **24 Getting Started** Product Description

## Supported SDI Formats

|                                              |                                              |            |               | **Sample**    | **Sample** |                               |          |                      |                 |              |
| -------------------------------------------- | -------------------------------------------- | ---------- | ------------- | ------------- | ---------- | ----------------------------- | -------- | -------------------- | --------------- | ------------ |
| **Link**                                     |                                              | **Format** |               | **Structure** |            |                               | **Bits** | **Frame/Field Rate** |                 | **Option**   |
| 12G-SDI                                      |                                              | 3840x2160  |               | 4:2:2         | YCbCr      |                               | 10b      | 50/59.94/60p         |                 | MPSDP-FMT-4K |
|                                              |                                              | 3840x2160  |               | 4:4:4         | RGB        |                               | 10/12b   | 23.98/24/25/29.97/   |                 | MPSDP-FMT-4K |
|                                              |                                              |            |               |               |            |                               |          | 30p                  |                 | and MPSDP-   |
|                                              |                                              |            |               |               |            |                               |          |                      |                 | PROD         |
|                                              |                                              | 4096x2160  |               | 4:2:2         | YCbCr      |                               | 10b      | 47.95/48/50/59.94/   |                 | MPSDP-FMT-4K |
|                                              |                                              |            |               |               |            |                               |          | 60p                  |                 |              |
|                                              |                                              | 4096x2160  |               | 4:4:4         | RGB        |                               | 10/12b   | 23.98/24/25/29.97/   |                 | MPSDP-FMT-4K |
|                                              |                                              |            |               |               |            |                               |          | 30p                  |                 | and MPSDP-   |
|                                              |                                              |            |               |               |            |                               |          |                      |                 | PROD         |
| Quad Link 12G-SDI                            | Quad Link 12G-SDI                            | 7680x4320  |               | 4:2:2         | YCbCr      |                               | 10b      | 50/59.94/60p         |                 | MPSDP-FMT-8K |
| Supported Video Formats in ST 2022-6 Streams | Supported Video Formats in ST 2022-6 Streams |            |               |               |            |                               |          |                      |                 |              |
|                                              |                                              |            | **Sample**    | **Sample**    |            |                               |          |                      |                 |              |
| **Link**                                     | **Format**                                   |            | **Structure** |               | **Bits**   | **Frame/Field Rate**          |          |                      | **Option**      |              |
| SD-SDI                                       | 525i                                         |            | 4:2:2         | YCbCr         | 10b        | 59.94i                        |          |                      | Base instrument |              |
|                                              | 625i                                         |            | 4:2:2         | YCbCr         | 10b        | 50i                           |          |                      | Base instrument |              |
| HD-SDI                                       | 1280x720                                     |            | 4:2:2         | YCbCr         | 10b        | 23.98/24/25/29.97/30/50/      |          |                      | Base instrument |              |
|                                              |                                              |            |               |               |            | 59.94/60p                     |          |                      |                 |              |
|                                              | 1920x1080                                    |            | 4:2:2         | YCbCr         | 10b        | 50/59.94/60i                  |          |                      | Base instrument |              |
|                                              |                                              |            |               |               |            | 23.98/24/25/29.97/30p and psF |          |                      |                 |              |
| 3G-SDI                                       | 1920x1080                                    |            | 4:2:2         | YCbCr         | 10b        | 50/59.94/60p                  |          |                      | Base instrument |              |
| Level A                                      |                                              |            |               |               |            |                               |          |                      |                 |              |
| 3G-SDI                                       | 1920x1080                                    |            | 4:2:2         | YCbCr         | 10b        | 50/59.94/60p                  |          |                      | Base instrument |              |
| Level B                                      |                                              |            |               |               |            |                               |          |                      |                 |              |

Supported Video Formats in ST 2022-6 Streams

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Getting Started 25** Product Description

Supported Video Formats in ST 2110-20 Streams

|            |            | **Sample**    | **Sample** |          |                          |                   |
| ---------- | ---------- | ------------- | ---------- | -------- | ------------------------ | ----------------- |
| **Link**   | **Format** | **Structure** |            | **Bits** | **Frame/Field Rate**     | **Option**        |
| ST 2110-20 | 525i       | 4:2:2         | YCbCr      | 10b      | 59.94i                   | Base instrument   |
|            | 625i       | 4:2:2         | YCbCr      | 10b      | 50i                      | Base instrument   |
|            | 1280x720   | 4:2:2         | YCbCr      | 10b      | 23.98/24/25/29.97/30/50/ | Base instrument   |
|            |            |               |            |          | 59.94/60p                |                   |
|            | 1920x1080  | 4:2:2         | YCbCr      | 10b      | 50/59.94/60i             | Base instrument   |
|            | 1920x1080  | 4:2:2         | YCbCr      | 10b      | 23.98/24/25/29.97/30/50/ | Base instrument   |
|            |            |               |            |          | 59.94/60p                |                   |
|            | 1920x1080  | 4:4:4         | RGB        | 12b      | 23.98/24/25/29.97/30/50/ | MPSDP-PROD        |
|            |            |               |            |          | 59.94/60p                |                   |
|            | 2048x1080  | 4:2:2         | YCbCr      | 10b      | 23.98/24/25/29.97/30/50/ | Base instrument   |
|            |            |               |            |          | 59.94/60p                |                   |
|            | 2048x1080  | 4:4:4         | RGB        | 12b      | 23.98/24/25/29.97/30/50/ | MPSDP-PROD        |
|            |            |               |            |          | 59.94/60p                |                   |
|            | 3840x2160  | 4:2:2         | YCbCr      | 10b      | 23.98/24/25/29.97/30/50p | MPSDP-FMT-4K      |
|            | 3840x2160  | 4:2:2         | YCbCr      | 10b      | 59.94/60p                | MPSDP-FMT-4K and  |
|            |            |               |            |          |                          | MPSDP-25GE        |
|            | 3840x2160  | 4:4:4         | RGB        | 12b      | 23.98/24/25/29.97/30p    | MPSDP-FMT-4K, and |
|            |            |               |            |          |                          | MPSDP-PROD        |
|            | 4096x2160  | 4:2:2         | YCbCr      | 10b      | 23.98/24/25/29.97/30/50p | MPSDP-FMT-4K      |
|            | 4096x2160  | 4:2:2         | YCbCr      | 10b      | 59.94/60p                | MPSDP-FMT-4K and  |
|            |            |               |            |          |                          | MPSDP-25GE        |
|            | 4096x2160  | 4:4:4         | RGB        | 12b      | 23.98/24/25/29.97/30p    | MPSDP-FMT-4K,     |
|            |            |               |            |          |                          | MPSDP-PROD, and   |
|            |            |               |            |          |                          | MPSDP-25GE        |

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **26 Getting Started** Product Description

Supported Video Formats for ST 2110-22

|            |            | **Sample**    |          |                            |            |
| ---------- | ---------- | ------------- | -------- | -------------------------- | ---------- |
| **Link**   | **Format** | **Structure** | **Bits** | **Frame/Field Rate**       | **Option** |
| ST 2110-22 | 1280x720   | 4:2:2 YCbCr   | 10b      | 23.98/24/25/29.97/30p/     | JPXS       |
|            |            |               |          | 50/59.94/60p               |            |
|            | 1920x1080  | 4:2:2 YCbCr   | 10b      | 23.98/24/25/29.97/30p,     | JPXS       |
|            |            |               |          | 50/59.94/60i, 50/59.94/60p |            |
|            | 2048x1080  | 4:2:2 YCbCr   | 10b      | 23.98/24/25/29.97/30/50/   | JPXS       |
|            |            |               |          | 59.94/60p                  |            |
|            | 3840x2160  | 4:2:2 YCbCr   | 10b      | 23.98/24/25/29.97/30/      | JPXS and   |
|            |            |               |          | 50p/59.94/60p              | FMT-4K     |
|            | 4096x2160  | 4:2:2 YCbCr   | 10b      | 23.98/24/25/29.97/30/      | JPXS and   |
|            |            |               |          | 50p/59.94/60p              | FMT-4K     |

## ST 2110-30 and -31 Streams

| **Conformance Level** | **Description**                                                            |
| --------------------- | -------------------------------------------------------------------------- |
| Conformance level A   | Reception of 48-kHz streams with one to eight channels at packet times of  |
|                       | 1 ms                                                                       |
| Conformance level B   | Reception of 48 kHz streams with one to eight channels at packet times of  |
|                       | 1 ms or 1 to 8 channels at packet times of 125 µs                          |
| Conformance level C   | Reception of 48 kHz streams with one to 16 channels at packet times of 125 |
|                       | µs                                                                         |

**Note:** PRISM instruments with the 25GE module have up to four ST 2110-30 streams of reception with up to 16 audio channels total.

## **Software Licenses**

- MPSDP-25GE adds a node-locked license for 25GE support.

- MPSDP-IP-MEAS adds a node-locked license for IP Measurement feature sets; this includes IP/PTP Graph, IP/PTP Session, PIT Histogram, Timing, Stream Timing, and Stream capture applications.

- MPSDP-FMT-4K adds a node-locked license for 4K formats and enables 6G/12G-SDI.

- MPSDP-FMT-8K adds a node-locked license for 8K formats and enables 12G-SDI; MPSDP-FMT-4K is also required for 8K format support.

- MPSDP-AUD adds a node-locked license for enhanced audio feature sets; this includes Phase, Session, Correlation, Loudness, and Dolby E status display.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Getting Started 27** Accessories

- MPSDP-DLBY adds a node-locked license for Dolby E, D, and D+ decoding. Also provides ED2 metadata in the Dolby Status application.

- MPSDP-ENG-QC adds a node-locked license for baseband engineering and quality control feature sets; this includes Datalist, CC decoding, ANC Session, and EBU R103 Gamut monitoring.

- MPSDP-PROD adds a node-locked license for production feature sets; this includes Stop, False Color, Light meter, HDR/WCG Conversion, Luma Qualified CIE, HDR Measurements, and 3D LUTs. It also adds support for deep color formats for both receiver and generator.

- MPSDP-GEN adds a node-locked license for SDI/IP signal generator; this includes IP/SDI Generator application.

- MPSDP-EXTNDSP adds a node-locked license for enabling extended desktop (MPD models include this license as standard).

- MPSDP-SRND adds a node-locked license for surround sound display.

- MPSDP-MULTI adds a node-locked license for SDI/IP (ST 2110-20 or ST 2110-22) multichannel input and Camera Alignment Monitoring.

- MPSDP-JPXS adds a node-locked license for decoding and generating ST 2110-22 JPEG XS streams. Generating JPEG XS streams also requires Option MPSDP-GEN.

## **Accessories**

There are several options for the MPS, MPD, and MPP instruments to make them more useful and flexible.

## **Rack Mounting**

The following rack-mounting equipment is available for the MPS, MPD, and MPP models:

- **MPS Rack:** The MPS Rack Accessory Kit (product MPS-RACK) allows you to install one MPS or two MPS units side-by-side in an equipment rack. A bracket is provided to fill the space next to a single MPS in a rack, and equipment to attach the MPS securely to a rack is included. The same kit also contains brackets to connect two MPS side-by-side and equipment to attach the MPS securely to a rack. The kit includes instructions for installation of either setup.

- **MPD Rack:** The equipment to install the MPD in a rack is provided with the MPD. Installation and safety instructions are included.

- **MPP Rack:** The equipment to install the MPP in a rack is provided with the MPP. Installation and safety instructions are included.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **28 Getting Started**

Power-on and Power-off Procedures

## **Portability**

The MPS Portable Accessory Kit (product MPS-PTBL) provides equipment for the portability and protection of one MPS. Included is a carry handle, a protective cover for a monitor, a bracket to attach a battery mount plate, a protective bottom plate, a mount to connect the unit to a tripod, and instructions to attach the equipment.

## **Power-on and Power-off Procedures**

This section describes how to apply power to the MPS, MPD, and MPP units and how to power-on and power-off the instruments.

## **International Power Cords**

The instrument was shipped with one of the following power cord options. Power cords for use in North America are UL-listed and CSA-certified. Cords for use outside North America are approved by at least one authority acceptable in the country to which the product is shipped.

- PWR-CORD-NA-S15 – North America power cord

- PWR-CORD-EURO – Universal EUR power cord

- PWR-CORD-CHN – China power cord

- PWR-CORD-IN – India power cord

- PWR-CORD-UK – United Kingdom power cord

- PWR-CORD-BRZ – Brazil power cord

- PWR-CORD-AUS– Australia power cord

- PWR-CORD-CHE – Switzerland power cord

- PWR-CORD-JPN – Japan power cord

● PWR-CORD-NONE – No power cord or AC adapter

## **CAUTION: To reduce risk of fire and shock, use the certified power cord provided** ~~CO~~ **with the product.**

## **Power Cord Installation**

This instrument is powered by an AC power source. Connect the power cord to the power connector on the rear panel of the instrument.

The power connector is keyed to be directional, with the flat portion of the power cord housing facing the left of the instrument (as viewed from the rear). When fully inserted, the power cord housing latches onto the instrument power connector.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Getting Started 29** Power-on and Power-off Procedures |

**CAUTION: To minimize the risk of damage to the instrument, we strongly recommend connecting the power cord to the instrument before connecting the power cord to the AC power source.**

## **Power Cord Removal**

The power cord housing latches on the instrument power connector when fully inserted. To remove the power cord, grasp the plug body and press the latch, shown, and firmly pull the cord out of the instrument.

- **CAUTION: To prevent damage to the power cord or to the instrument power connector, do not attempt to disconnect the power cord by pulling on the cable. You must press the latch on the plug body to disengage the locking mechanism and pull the plug at the same time.**

**CAUTION: To minimize the risk of damage to the instrument, we strongly recommend disconnecting the power cord from the AC power source before disconnecting the power cord from the instrument.**

## **Power-on Procedure**

**1.** Connect power to the instrument (see _Power Cord Installation_ ). If the PRISM monitor was previously powered off by a power interruption or by disconnecting the power cord from the rear of the instrument, the instrument powers on when power is reconnected.

**2.** (MPP only) For the first power-up, connect a monitor, keyboard, and mouse to establish a network address for the product (see _Network Installation_ ).

**3.** Press the power button on the front panel to turn the instrument on. In normal operation, the MPS-MPD power button light is turned on during the power-on sequence and then turns off.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **30 Getting Started** SFP Module Installation

In normal operation, the MPP power button blinks during the power-on sequence and then turns on.

**==> picture [14 x 4] intentionally omitted <==**

**----- Start of picture text -----**<br>
Power<br>**----- End of picture text -----**<br>

**==> picture [31 x 4] intentionally omitted <==**

**----- Start of picture text -----**<br>
-off Procedure<br>**----- End of picture text -----**<br>

**4.** Press the power button on the instrument front panel to turn the instrument off. Alternatively, in the instrument:

- **A.** Select the **Settings** icon ( ) and then select **Utilities** .

- **B.** Select **Power** and then select **Power Down Now** .

**CAUTION: To prevent data loss, we strongly recommend you shut down the instrument before disconnecting the power cord.**

**5.** To completely remove power from the instrument, disconnect the power cord from the AC power source and then disconnect the power cord from the instrument (see _Power Cord Removal_ ).

## **SFP Module Installation**

The following optional SFP modules are available for MPS-200 and -300, MPD-200 and - 300, and MPP-200 and -300 models:

- MP-SFP 10GESR is a 10G Ethernet short-range SFP+ transceiver (850 nm);

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Getting Started 31** Network Installation |

- MP-SFP 10GELR is a 10G Ethernet long-range SFP+ transceiver (1310 nm);

- MP-SFP 25GESR is a 25G Ethernet short-range SFP28 transceiver (850 nm); and

- MP-SFP 25GELR is a 25G Ethernet long-range SFP28 transceiver (1310 nm).

**Note:** ST 2022-7 requires two 10GE or 25GE SFP modules to be installed. For proper ST 2022-7 operation, both modules must support the same 10GE or 25GE data rate.

## **Install SFP Module**

To install an SFP module, insert the SFP module into the SFP connector. The module latches into place when fully inserted.

**Note:** There are different types of SFP modules for 10GE and 25GE signals. If the SFP module does not match the unit signal setting (for example, a 25GE SFP module is installed and the unit is set for a 10GE signal), the Link Status (in Network, under Settings) returns “SFP Error.”

To remove the SFP module, pull down on the latch and pull the module out of the SFP connector.

**Note:** Different types of SFP modules may have different latching mechanisms. The 10/25GE connectors are marked on the back of the MPS (see _MPS Connectors_ ), MPD (see _MPD Connectors_ ), and MPP (see _MPP Connectors_ ).

## **SFP Module Transportation**

AN **CAUTION:module from the instrument, store and transport the SFP module in an anti-To prevent static damage to the SFP module, if you remove the SFP static bag or container. CAUTION: To prevent possible damage to the PRISM monitor and SFP modules,** ~~LC~~ **remove the SFP modules before transporting the PRISM monitor.**

## **Network Installation**

See the installation and safety instructions manual that shipped with the instrument for basic installation instructions. After the instrument is physically installed, you might want to connect it directly to a PC or to a network. This section explains how.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **32 Getting Started** Network Installation

## **Connect Directly to a PC**

**1.** Connect the instrument directly to a PC with an Ethernet cable or an Ethernet switch.

**2.** Set up the instrument as shown.

**3.** Choose Manual IP mode to set the IP address manually. Be sure to set an address that is compatible with the setting of the PC.

**Note:** The default IP address of the PRISM monitor is 192.168.1.2.

## **Connect to a Network**

To allow network access to the instrument, you must set the IP address. Network addresses can be assigned automatically (DHCP) or manually. If your network does not use DHCP, you must manually enter the address for the instrument. To get a fixed address, talk to your LAN administrator. The default IP address of the PRISM monitor is 192.168.1.2.

**CAUTION: Remote connectivity can be lost when the control port and either video port are on the same subnet. It is possible to lose remote connectivity while working locally and not know the connectivity was lost. For details about this problem and how to avoid it, see** _**Prevent Remote Connectivity Loss**_ **.**

To connect the instrument to a network and access it with a remote PC:

**1.** (MPP only) Connect a monitor, keyboard, and mouse to the instrument.

**2.** On the PRISM monitor, select the **Settings** icon ( ).

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Getting Started 33** Managing Network Ports

**3.** Select **Network** .

**4.** Select the **CONTROL IP PORT** tab.

**5.** Depending on your local network requirements, select **DHCP** or **Manual** as the method for selecting an IP address.

**CAUTION: If you select Manual, remote access can be lost if the addresses are not known and correct. Local access is required to select DHCP to reconnect remote access.**

**6.** If you cannot use DHCP and you selected Manual, use the Manual submenu to set the IP address, subnet mask, gateway address, DNS address, and DNS Search Domain parameters you obtained from your LAN administrator. (Be sure to use compatible addresses between the PC and the instrument.)

**7.** In the **IP Address** box, type or select the IP input address.

**CAUTION: IGMP communications can fail when the Video IP Ports are configured for the same IP Address.**

**8.** Select the **Close** icon ( ).

## **Managing Network Ports**

Network ports are virtual connections on networked devices such as the MPS, MPD, and MPP products, which allow data to be sent or received. These products require a number of network ports to be open for proper operation.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **34 Getting Started** MPS Connectors

## Required Network Ports

| **Port Type ** | **Port**    | **Function** |
| -------------- | ----------- | ------------ |
| TCP            | 22          | SSH          |
| TCP            | 80          | HTTP         |
| TCP            | 5900        | VNC server   |
| TCP            | 6080        |              |
| TCP            | 8080        | Web server   |
| TCP            | 8999        |              |
| TCP            | 9000        |              |
| UDP            | 161-162     | SNMP         |
| UDP            | 5004-5005   | RTSP         |
| UDP            | 30000-60000 | Web RTC      |

Consult with your network administrator to ensure that these ports are available.

## **MPS Connectors**

This section explains the differences between the connectors of the MPS models.

## **MPS-100 Rear Connectors**

The example shows the rear panel with labeled connectors of an MPS-100.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Getting Started 35** MPS Connectors

Labeled PRISM MPS-100 Rear-Panel Connectors

| **Connector Label,**<br>**Symbol, or End** | **Description**                                                                                                                                                                                                                         |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AC In                                      | Connector is for an AC power source.                                                                                                                                                                                                    |
| DC In                                      | Connector is for a standard XLR DC power source.<br>Pin 1: negative voltage<br>Pin 2: not in use<br>Pin 3: not in use<br>Pin 4: positive voltage<br>**Note:**A battery that can provide 12 amps of continuous<br>operation is required. |
|                                            | Ethernet port is a standard RJ-45 connector for 10/100/<br>1000Base-T Ethernet cable.                                                                                                                                                   |
|                                            | Two USB 3.0 ports are for connecting a mouse and keyboard,<br>importing or exporting instrument presets, upgrading the<br>instrument firmware, or saving screen captures.                                                               |
| ()<br>4‘)                                  | Audio output (1/8-inch—3.5 mm—line out) port is for<br>headphones to listen to the selected audio channel pair.1                                                                                                                        |
| SDI1 Input                                 | SDI1 can operate in these modes:<br>**•**Input only supporting SD, HD, 3G, 6G, or 12G signals<br>**•**Quad link 4K and 8K input when used with SDI inputs 1-4                                                                           |
| SDI2 Input                                 | SDI2 can operate in these modes:<br>**•**Input only supporting SD, HD, 3G, 6G, or 12G signals<br>**•**Quad link 4K and 8K input when used with SDI inputs 1-4                                                                           |
| SDI3 I/O                                   | SDI3 can operate in these modes:<br>**•**Input supporting SD, HD, 3G, 6G, or 12G signals<br>**•**Output loop-through of SDI1 input<br>**•**Quad link 4K and 8K input when used with SDI inputs 1-4                                      |
| SDI4 I/O                                   | SDI4 can operate in these modes:<br>**•**Input supporting SD, HD, 3G, 6G, or 12G signals<br>**•**Output loop-through of SDI2 input<br>**•**Quad link 4K or 8K input when used with SDI inputs 1-4                                       |
| DP                                         | Display Port output is for an external monitor. The output video<br>format is 1920×1080.2                                                                                                                                               |
| GPIO                                       | GPIO is a 15-pin, micro D-sub connector, see the*GPIO Remote*<br>\_Connector Pin Assignments and Preset Functions_table.                                                                                                                |

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **36 Getting Started** MPS Connectors

Labeled PRISM MPS-100 Rear-Panel Connectors

| **Connector Label,**<br>**Symbol, or End** | **Description**                                                                                                                                                                     |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| REF IN                                     | REF IN is used for analog reference signals black burst and<br>trilevel sync for locking.                                                                                           |
| REF OUT                                    | REF OUT is a pass-through of the REF IN.                                                                                                                                            |
| AUX OUT                                    | AUX OUT is for SDI output of the selected SDI input; or it is an SDI<br>generator output (GEN license is required):<br>**•**For quad link inputs (4K or 8K), the AUX OUT is link 1. |

1. Audio output is an 1/8-inch (3.5 mm) diameter port for a headset. It has connections for left and right audio channels. Headset plugs that are an 1/8 inch and have an additional contact for a microphone might not work because the headphone ports are not set for the spacing requirements of a third connection on the plug.

2. When connecting to an external monitor, a monitor with a 1920×1080-capable display works best with the instrument.

GPIO Remote Connector Pin Assignments and Preset Functions

| **Characteristic** |               | **Pin Function**     |
| ------------------ | ------------- | -------------------- |
| Connector Pin      | Connector Pin | 1 GND (In)           |
| Assignments        |               | 2 Do not connect     |
| 1                  | 8             | 3 Do not connect     |
| oes                |               | 4 Do not connect     |
|                    |               | 5 Do not connect     |
| 9                  | 15            |                      |
|                    |               | 6 GND (In)           |
|                    |               | 7 Do not connect     |
|                    |               | 8 Do not connect     |
|                    |               | 9 Do not connect     |
|                    |               | 10 Preset A1 recall1 |
|                    |               | 11 Preset A2 recall1 |
|                    |               | 12 Preset A3 recall1 |
|                    |               | 13 Preset A4 recall1 |
|                    |               | 14 Preset A5 recall1 |
|                    |               | 15 Preset A6 recall1 |

1. Active low inputs, internally pulled up to 5 V. A 5 V tolerant open drain or open collector driver, are recommended.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Getting Started 37** MPS Connectors

## **Recall a Preset through GPIO**

Ground and release the pin related to the preset (for example, pin 10 for preset A1) to a ground (pin 1 or 6). The GPIO must be turned on:

**1.** Select the **Settings** icon ( ), select **Utilities** and then select **GPIO** .

**2.** Set **Preset Recall** to **On** .

Or through API:

At the API command line, to turn the GPIO recall on, send:

GPIO_PRESET_RECALL_ENABLE_ON

To turn the GPIO recall off, send:

GPIO_PRESET_RECALL_ENABLE_OFF

## **MPS-200/300 Rear Connectors**

This example shows the rear panel with labeled connectors of an MPS-300.

Labeled PRISM MPS200/300 Rear-Panel Connectors

| **Connector Label,** |                                      |
| -------------------- | ------------------------------------ |
| **Symbol, or End**   | **Description**                      |
| AC In                | Connector is for an AC power source. |

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **38 Getting Started** | MPS Connectors

Labeled PRISM MPS200/300 Rear-Panel Connectors

| **Connector Label,** |                                                                                                                 |
| -------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Symbol, or End**   | **Description**                                                                                                 |
| DC In                | Connector is for a standard XLR DC power source.                                                                |
|                      | Pin 1: negative voltage                                                                                         |
|                      | Pin 2: not in use                                                                                               |
|                      | Pin 3: not in use                                                                                               |
|                      | Pin 4: positive voltage                                                                                         |
|                      | **Note:**A battery that can provide 12 amps of continuous                                                       |
|                      | operation is required.                                                                                          |
| aa                   | Ethernet port is a standard RJ-45 connector for 10/100/<br>1000Base-T Ethernet cable.                           |
|                      | Two USB 3.0 ports are for connecting a mouse and keyboard,                                                      |
|                      | importing or exporting instrument presets, upgrading the                                                        |
|                      | instrument firmware, or saving screen and stream captures.                                                      |
| ()<br>‘>             | Audio output (1/8-inch—3.5mm—line out) port is for<br>headphones to listen to the selected audio channel pair.1 |
| SDI1                 | SDI1 can operate in these modes:                                                                                |
| (EYE in MPS-300      | **•**Input only supporting SD, HD, 3G, 6G, or 12G signals.                                                      |
| only)                | **•**Quad link 4K and 8K input when used with SDI inputs 1-4                                                    |
|                      | **•**MPS-300 only: Eye diagram up to 12G for physical layer                                                     |
|                      | measurements, including automated measurements of SDI                                                           |
|                      | eye pattern parameters.                                                                                         |
| SDI2                 | SDI2 can operate in these modes:                                                                                |
|                      | **•**Input only supporting SD, HD, 3G, 6G, or 12G signals                                                       |
|                      | **•**Quad link 4K and 8K input links when used with SDI inputs 1-4                                              |
| SDI3                 | SDI3 can operate in these modes:                                                                                |
|                      | **•**Input supporting SD, HD, 3G, 6G, or 12G signals                                                            |
|                      | **•**Output loop-through of SDI1 input                                                                          |
|                      | **•**Quad link 4K and 8K input when used with SDI inputs 1-4                                                    |
| SDI4                 | SDI4 can operate in these modes:                                                                                |
|                      | **•**Input only supporting SD, HD, 3G, 6G, or 12G signals                                                       |
|                      | **•**Output loop-through of SDI2 input                                                                          |
|                      | **•**Quad link 4K and 8K input when used with SDI inputs 1-4                                                    |

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Getting Started 39** MPD Connectors

## Labeled PRISM MPS200/300 Rear-Panel Connectors

## **Connector Label, Symbol, or End Description**

| **Connector Label,**<br>**Symbol, or End** | **Connector Label,**<br>**Description**                             |
| ------------------------------------------ | ------------------------------------------------------------------- |
| 10/25GE                                    | SFP module slots can be configured for IP or SDI applications.      |
| SDI I/O                                    | **•**10/25GE: Two SFP28 ports are for 10/25GE IP applications. See  |
|                                            | MP-SFP products for available modules.                              |
|                                            | **•**SDI I/O (for future functionality): Two optional SFP ports can |
|                                            | provide up to four SDI signal loop-through outputs up to 12G.       |
| DP                                         | Display Port output is for an external monitor. The output video    |
|                                            | format is 1920×1080.2                                               |
| GPIO                                       | GPIO is a 15-pin, micro D-sub connector, see the*GPIO Remote*       |
|                                            | \_Connector Pin Assignments and Preset Functions_table.             |
| REF IN                                     | REF IN is used for analog reference signals black burst and         |
|                                            | trilevel sync for locking.                                          |
| REF OUT                                    | **Note:**This is a dual-purpose output that can be controlled in    |
|                                            | the UI to set to REF OUT or PPS.                                    |
|                                            | **•**REF OUT is a pass-through of the REF IN.                       |
|                                            | **•**PPS connector outputs a 1 PPS (pulse per second) signal when   |
|                                            | the instrument is locked to a PTP reference. 3.3v drive. TTL        |
|                                            | compatible.                                                         |
| AUX OUT                                    | AUX OUT is for SDI output of the selected SDI, ST 2022, or          |
|                                            | ST 2110 input; or it is an SDI generator output (GEN license is     |
|                                            | required):                                                          |
|                                            | **•**For quad link inputs (4K or 8K) the AUX OUT is link 1.         |
|                                            | **•**ST 2110-20/22/30/31 inputs are supported.                      |

1. Audio output is a 1/8-inch (3.5 mm) diameter port for a headset. It has connections for left and right audio channels. Headset plugs that are 1/8 inch and have an additional contact for a microphone might not work because the headphone ports are not set for the spacing requirements of a third connection on the plug.

2. When connecting to an external monitor, a monitor with a 1920×1080-capable display works best with the instrument.

## **MPD Connectors**

This section explains the differences between the connectors of the MPD models.

## **MPD-100 Rear Connectors**

The example shows the rear panel of an MPD-100. The table provides details of each connector.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **40 Getting Started** MPD Connectors

**==> picture [58 x 5] intentionally omitted <==**

**----- Start of picture text -----**<br>
MPD-100 Rear Panel Detail<br>**----- End of picture text -----**<br>

Labeled PRISM MPD-100 Rear-Panel Connectors

| **Connector Label,** |                                                               |
| -------------------- | ------------------------------------------------------------- |
| **Symbol, or End**   | **Description**                                               |
| AC In                | Connector for an AC power source.                             |
|                      | Ethernet port is a standard RJ-45 connector for 10/100/       |
|                      | 1000Base-T Ethernet cable.                                    |
|                      | Two USB 3.0 ports are for connecting a mouse and keyboard,    |
|                      | importing or exporting instrument presets, upgrading the      |
|                      | instrument firmware, or saving screen captures.               |
| SDI1                 | SDI1 can operate in these modes:                              |
|                      | **•**Input only supporting SD, HD, 3G, 6G, or 12G signals.    |
|                      | **•**Quad link 4K and 8K input when used with SDI inputs 1-4. |
| SDI2                 | SDI2 can operate in these modes:                              |
|                      | **•**Input only supporting SD, HD, 3G, 6G, or 12G signals.    |
|                      | **•**Quad link 4K and 8K input when used with SDI inputs 1-4. |

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Getting Started 41** MPD Connectors

Labeled PRISM MPD-100 Rear-Panel Connectors

| **Connector Label,** |                                                                      |
| -------------------- | -------------------------------------------------------------------- |
| **Symbol, or End**   | **Description**                                                      |
| SDI3                 | SDI3 I/O can operate in these modes:                                 |
|                      | **•**Input supporting SD, HD, 3G, 6G, or 12G signals.                |
|                      | **•**Output loop-through of SDI 1 input.                             |
|                      | **•**Quad link 4K and 8K input when used with SDI inputs 1-4.        |
| SDI4                 | SDI4 I/O can operate in these modes:                                 |
|                      | **•**Input only supporting SD, HD, 3G, 6G, or 12G signals.           |
|                      | **•**Output loop-through of SDI 2 input.                             |
|                      | **•**Quad link 4K and 8K input when used with SDI inputs 1-4.        |
| GPIO                 | GPIO is a 15-pin, micro D-sub connector, see the*GPIO Remote*        |
|                      | \_Connector Pin Assignments and Preset Functions_table.              |
| REF IN               | REF IN is used for analog reference signals black burst and          |
|                      | trilevel sync for locking.                                           |
| REF OUT              | REF OUT is a pass-through of the REF IN.                             |
| AUX OUT              | AUX OUT provides an SDI output of the selected input. It also        |
|                      | includes the audio associated with the input.                        |
|                      | If Multi Input is enabled (MULTI license is required), the output is |
|                      | same as the Primary Channel.                                         |
|                      | For quad link inputs, (4K or 8K), the AUX OUT is link 1.             |
|                      | **Note:**MPD 100 does not support IP Inputs.                         |

## **MPD-Front Connectors**

The example shows the front panel of an MPD-100, -200, or -300. The table provides details of each connector.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **42 Getting Started** MPD Connectors

Labeled PRISM MPD-100/-200/300 Front-Panel Connectors

## **Connector Symbol Description**

2 USB 3.0 ports are for connecting a mouse and keyboard, importing or exporting instrument presets, upgrading the instrument firmware, or saving screen and stream captures.

Audio output (1/8-inch—3.5 mm—line out) port is for headphones to listen to the selected audio channel pair.[1]

1. Audio output is a 1/8-inch (3.5 mm) diameter port for a headset. It has connections for left and right audio channels. Headset plugs that are 1/8 inch and have an additional contact for a microphone might not work because the headphone ports are not set for the spacing requirements of a third connection on the plug.

## **MPD-200/300 Rear Connectors**

The following example shows the rear panel of an MPD-300. The table provides details of each connector.

MPD-200/300 Rear Panel Detail

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Getting Started 43** MPD Connectors |

Labeled PRISM MPD-200/300 Rear-Panel Connectors

| **Connector Label**                                                                             |                                                                      |
| ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **or Symbol**                                                                                   | **Description**                                                      |
| AC In                                                                                           | Connector for an AC power source.                                    |
| Ethernet port is a standard RJ-45 connector for 10/100/<br>1000Base-T Ethernet cable.<br>~~ee~~ |                                                                      |
|                                                                                                 | Two USB 3.0 ports are for connecting a mouse and keyboard,           |
|                                                                                                 | importing or exporting instrument presets, upgrading the             |
|                                                                                                 | instrument firmware, or saving screen and stream captures.           |
| SDI1                                                                                            | SDI 1 can operate in these modes:                                    |
| (EYE in                                                                                         | **•**Input only supporting SD, HD, 3G, 6G, or 12G signals.           |
| MPD-300 only)                                                                                   | **•**Quad link 4K and 8K input when used with SDI inputs 1-4.        |
|                                                                                                 | **•**MPD-300 only: Eye diagram up to 12G for physical layer          |
|                                                                                                 | measurements, including automated measurements of SDI                |
|                                                                                                 | eye pattern parameters.                                              |
| SDI2                                                                                            | SDI2 can operate in these modes:                                     |
|                                                                                                 | **•**Input only supporting SD, HD, 3G, 6G, or 12G signals.           |
|                                                                                                 | **•**Quad link 4K and 8K input when used with SDI inputs 1-4.        |
| SDI3                                                                                            | SDI3 I/O can operate in these modes:                                 |
|                                                                                                 | **•**Input supporting SD, HD, 3G, 6G, or 12G signals.                |
|                                                                                                 | **•**Output loop-through of SDI 1 input.                             |
|                                                                                                 | **•**Quad link 4K and 8K input when used with SDI inputs 1-4.        |
| SDI4                                                                                            | SDI4 I/O can operate in these modes:                                 |
|                                                                                                 | **•**Input only supporting SD, HD, 3G, 6G, or 12G signals.           |
|                                                                                                 | **•**Output loop-through of SDI 2 input.                             |
|                                                                                                 | **•**Quad link 4K and 8K input when used with SDI inputs 1-4.        |
| 10/25GE                                                                                         | SFP module slots can be configured for IP or SDI applications.       |
| SDI I/O                                                                                         | **•**10/25GE: Two SFP28 ports are for 10/25GE IP applications. See   |
|                                                                                                 | MP-SFP products for available modules.                               |
|                                                                                                 | **•**SDI I/O (for future functionality): Two optional SFP ports can. |
|                                                                                                 | provide up to four SDI signal loop-through outputs up to 12G.        |
| GPIO                                                                                            | GPIO is a 15-pin, micro D-sub connector, see the*GPIO Remote*        |
|                                                                                                 | \_Connector Pin Assignments and Preset Functions_table.              |
| REF IN                                                                                          | Used for analog reference signals black burst and trilevel sync      |
|                                                                                                 | for locking.                                                         |

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **44 Getting Started** MPP Connectors

Labeled PRISM MPD-200/300 Rear-Panel Connectors

| **Connector Label** |                                                                   |
| ------------------- | ----------------------------------------------------------------- |
| **or Symbol**       | **Description**                                                   |
| REF OUT             | **Note:**This is a dual-purpose output that can be controlled in  |
|                     | the UI to set to REF OUT or PPS.                                  |
|                     | **•**REF OUT is a pass-through of the REF IN.                     |
|                     | **•**PPS connector outputs a 1 PPS (pulse per second) signal when |
|                     | the instrument is locked to a PTP reference. 3.3v drive. TTL      |
|                     | compatible.                                                       |
| AUX OUT             | AUX OUT is for SDI output of the selected SDI, ST 2022, or        |
|                     | ST 2110 input; or it is an SDI generator output (GEN license is   |
|                     | required):                                                        |
|                     | **•**For quad link inputs (4K or 8K) the AUX OUT is link 1.       |
|                     | **•**ST 2110-20/22/30/31 inputs are supported.                    |

## **MPP Connectors**

This section explains the differences between the connectors of the MPP models.

## **MPP Front Connectors**

The following example shows the front panel of all MPP models. The table provides details of each connector.

| **Connector** | **Description**                                                                   |
| ------------- | --------------------------------------------------------------------------------- |
| USB Ports     | Two USB 3.0 ports are for connecting a mouse and keyboard, importing or           |
|               | exporting instrument presets, upgrading the instrument firmware, or saving screen |
|               | and stream captures.                                                              |
| Headphone     | Audio output (1/4-inch—6.35 mm) port is for headphones to listen to the selected  |
| Output        | audio channel pair.                                                               |

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Getting Started 45** MPP Connectors

## **MPP-100 Rear Connectors**

The following example shows the rear panel of an MPP-100. The table provides details of each connector.

Labeled PRISM MPP-100 Rear-Panel Connectors

| **Connector**      |                                                                                     |
| ------------------ | ----------------------------------------------------------------------------------- |
| **Label, Symbol,** |                                                                                     |
| **or End**         | **Description**                                                                     |
| AC Input           | Connector for an AC power source.                                                   |
| GPIO               | GPIO is a 15-pin, micro D-sub connector, see the*GPIO Remote Connector Pin*         |
|                    | \_Assignments and Preset Functions_table.                                           |
| SDI1-4             | Four HD-BNC SDI connector pairs (eight total), including a dedicated SDI input and  |
|                    | a dedicated SDI output for each pair. The output SDI signal is an active loop-      |
|                    | through of the corresponding input and is always on.                                |
|                    | The SDI inputs support SD, HD, 3G, and 12G.                                         |
|                    | SDI inputs 1-4 can be used together for monitoring Quad Link 4K and 8K inputs.      |
| AUX OUT            | SDI output of the selected SDI input.                                               |
| REF                | The REF input connector can be used to lock to analog black burst and trilevel sync |
|                    | signals.                                                                            |
|                    | The REF output connector can be a loop-through of the input analog sync signal or   |
|                    | the Pulse Per Second (PPS) signal when the instrument is locked to a PTP reference  |
|                    | (3.3V TTL).                                                                         |
|                    | The Ethernet port is a standard RJ-45 connector for 10/100/1000Base-T Ethernet      |
|                    | cable.                                                                              |

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **46 Getting Started** MPP Connectors

Labeled PRISM MPP-100 Rear-Panel Connectors

**Connector Label, Symbol, or End Description** Two USB 3.0 ports are for connecting a mouse and keyboard, importing or exporting instrument presets, upgrading the instrument firmware, or saving screen and stream captures. DP1-DP2 Two DisplayPort outputs for external monitors. The output video format is 1920×1080[1] . DP1 is the primary monitor, and DP2 is the secondary monitor when using the Extended Display feature. **Note:** We recommend plugging in the external monitors before turning on the instrument so the monitors are properly identified and configured. **Note:** We recommend using external DP monitors to avoid using DP adapters such as HDMI-to-DP. Not all DP adapters work with the MPP product. **Note:** (MPP only) If you hear five beeps when powering up the MPP, this indicates that an external display is not connected to the instrument.

1. When connecting to an external monitor, a monitor with a 1920×1080-capable display works best with the instrument.

## **MPP-200/300 Rear Connectors**

The following example shows the rear panel of an MPP-300. The MPP-200 is identical to the MPP-300 in appearance, but the MPP-200 does not have the Eye function the MPP300 has. The table provides details of each connector.

Labeled PRISM MPP-200/300 Rear-Panel Connectors

**Connector Label, Symbol, or End Description** AC Input Connector for an AC power source.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Getting Started 47** MPP Connectors

Labeled PRISM MPP-200/300 Rear-Panel Connectors

| **Connector**      |                                                                                      |
| ------------------ | ------------------------------------------------------------------------------------ |
| **Label, Symbol,** |                                                                                      |
| **or End**         | **Description**                                                                      |
| ANALOG AUDIO       | The DB25 connector connects up to eight audio channels of stereo or surround         |
| OUT 1-8            | sound speakers to the instrument. Embedded SDI audio or ST 2110-30 streams can       |
|                    | be directed to the Analog Audio out connector. See*ANALOG AUDIO OUT and LINE*        |
|                    | \_OUT (MPP-200/300 only)\_for details about using this connector. Each channel       |
|                    | provides a Professional level, balanced signal at +4dBu for a -20dBFS digital PCM    |
|                    | source. The DB25 connector uses the standard TASCAM pinout for analog audio.         |
|                    | G: ground (green), -: cold (blue), +: hot (red)                                      |
|                    | 1<br>3<br>5<br>7                                                                     |
|                    | 13<br>G-+<br>GS ac<br>Cas<br>g<br>Cir:<br>1                                          |
|                    | OKO<br>GOK GOS OFOKS G/                                                              |
|                    | £0.OOO ONOVO_ONO//O_O\E’<br>25<br>G-+<br>G-+<br>G-+<br>q-+ 4                         |
|                    | 2<br>4<br>6<br>8                                                                     |
| Line Out           | A 3.5 mm port is used to connect an external device such as an audio mixer or set    |
|                    | of stereo speakers. Audio in surround formats is downmixed to stereo or the Left     |
|                    | and Right channels on this port.                                                     |
| —                  | Line Out provides a Semi-Pro/Consumer level signal at -10dBV for a -10.7dBFS         |
|                    | digital PCM source.                                                                  |
| GPIO               | One five-pin, micro D-sub connector. For details, see the*GPIO Remote Connector Pin* |
|                    | \_Assignments and Preset Functions_table.                                            |
| SDI1-4             | Four HD-BNC SDI connector pairs (eight total), include a dedicated SDI input and a   |
|                    | dedicated SDI output. The output SDI signal is an active loop-through of the         |
|                    | corresponding input and is always on.                                                |
|                    | The SDI inputs support SD, HD, 3G, and 12G signals.                                  |
|                    | SDI inputs 1-4 can be used together to monitor Quad Link 4K and 8K inputs.           |
|                    | SDI1 can be used for SD, HD, and 12G Eye functionality on MPP-300 instruments.       |
| AUX OUT            | SDI output of the selected SDI, ST 2022, or ST 2110 input.                           |
| REF                | The REF input connector can be used to lock to analog black burst and trilevel sync  |
|                    | signals.                                                                             |
|                    | The REF output connector can be a loop-through of the input analog sync signal or    |
|                    | the PPS (pulse per second) signal when the instrument is locked to a PTP reference   |
|                    | (3.3V TTL).                                                                          |
| 10/25GE            | Two SFP28 ports are for 10/25GE IP applications. See MP-SFP products for available   |
|                    | modules.                                                                             |

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **48 Getting Started** Secure Web Interface

Labeled PRISM MPP-200/300 Rear-Panel Connectors

## **Connector Label, Symbol, or End Description**

Ethernet port is a standard RJ-45 connector for 10/100/1000Base-T Ethernet cable.

Two USB 3.0 ports are for connecting a mouse and keyboard, importing or exporting instrument presets, upgrading the instrument firmware, or saving screen and stream captures.

DP1-DP2 Two DisplayPort outputs for external monitors. The output video format is 1920×1080[1] . DP1 is the primary monitor and DP2 is the secondary monitor when using the Extended Display feature.

**Note:** We recommend plugging in the external monitors before turning on the instrument so the monitors are properly identified and configured.

**Note:** We recommend using external DP monitors to avoid the use of DP adapters such as HDMI-to-DP. Not all DP adapters will work with the MPP product.

1. When connecting to an external monitor, a monitor with a 1920×1080-capable display works best with the instrument.

## **Secure Web Interface**

The PRISM web server can use HTTPS instead of HTTP to provide a secure web interface. This might be required by your organization cybersecurity requirements, such as EBU R 143. The factory configuration for the web interface is to use HTTP but you can install your organization certificate files and use HTTPS.

Most browsers show the site status and protocols. For example, with plain HTTP, the Chrome browser indicates the PRISM web interface is “Not secure”:

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Getting Started 49** Secure Web Interface

## **Configure Web Server**

## **Install an SSL Certificate**

To install new SSL certificate files and switch to HTTPS:

**1.** In the PRISM web interface, select **HTTP / HTTPS Configuration** .

**2.** In the **Password** box, type your password, and then click **Login** . The default password is PRISM, but your organization should choose their own unique password. See _Find or Change Hostname, Password, and IP Address_ .

Two or three files are needed to complete the installation. Your IT organization should provide the files for your domain. Use the web interface to select these files from a location on a local computer.

**SSL Certificate (.crt)** : Click **Browse** and choose the certificate file. This file should contain the PEM format certificate chain for the server, any intermediate certificates, and the CA certificate. The certificate chain can be of any length, although most will contain two or three certificates. The first certificate in the file should be the server certificate that corresponds to the SSL Certificate Key file. The SSL Certificate file should have a filename extension of .crt.

**SSL Certificate Key** (key): Click **Browse** and choose the private key file. The private key should correspond to the first certificate in the SSL Certificate file. This file should use the PEM format and have a filename extension of .key.

**SSL Password File (optional)** : Click **Browse** and choose the password file. This file is optional and is needed only if the key file uses passphrases. The password file should have a filename extension of .txt.

**3.** Click **Install Certificate** to upload the files to PRISM.

**4.** If the certificate files are installed successfully, select **HTTPS (Port 443)** from the **Web Server Protocol** list, and then click **Restart Web Server** . After the web server restarts, the web page shows as secure.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **50 Getting Started** Display Elements

**Note:** If you change the configuration from HTTPS back to HTTP, you might need to force a hard refresh of your browser, including any open NoVNC or WebRTC sessions.

At any time, click **View Certificate Information** to see the status of the currently installed certificates, including the expiry date. This button is disabled if no certificates have been installed yet.

## **Delete an SSL Certificate**

To delete a certificate:

**1.** In the PRISM web interface, select **HTTP / HTTPS Configuration** .

**2.** From the **Web Server Protocol** list, select **HTTP** .

**3.** Click **Delete Certificate** . This button is disabled if no certificates have been installed yet.

## **Display Elements**

The following figures show the key elements of the MPS, MPD, and MPP displays. Descriptions of the elements are provided in the tables.

## **MPS Display**

The MPS default display has four tiles. The MPS can support eight tiles if a second display is added and the Extended Display Mode option (MPSDP-EXTNDSP) is purchased and enabled.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Getting Started 51** Display Elements

PRISM MPS Display Elements

**==> picture [383 x 135] intentionally omitted <==**

**----- Start of picture text -----**<br>
|||
|---|---|
|Item name|Description|
|Applications Tabs|Some applications have selectable tabs (highlighted readouts)|
|Bar|you can use to display additional information.|
|Application Tiles|Location of the application tile. The application tiles can be|
|1-4|quarter-screen, half-screen, or full-screen.|
|Application Name|The name of the displayed application.|
|Power Button|Press the button to turn the instrument on or off. To completely|
|remove power from the instrument, remove the power cord.|

**----- End of picture text -----**<br>

**==> picture [295 x 49] intentionally omitted <==**

**----- Start of picture text -----**<br>
|||||||
|---|---|---|---|---|---|
|CAUTION:|To prevent data loss, we strongly recommend you|
|shut down the instrument before disconnecting the power|
|cord. Press the power button or select|Settings|,|Utilities|,|
|Power|, and then|Power|Down|Now|.|

**----- End of picture text -----**<br>

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **52 Getting Started** Display Elements

## PRISM MPS Display Elements

**Item name Description** Status Bar The left side of the status bar has icons with links to various instrument settings including Volume ( ), Presets ( ), Settings ( be ), Input type ( ), and the Tile application menu ( ). Select the **Home** icon ( ) to exit any displayed menus. The right side of the status bar lists instrument status, such as the selected input, type of input signal, selected signal reference, video/reference signal status, audio channel status, the real-time clock or PTP clock (to switch between the clocks, see _Configure Time and Date_ ), and a link to the Activity menu ( ).

**Note:** When you select an instrument setting, the associated menu replaces the status bar.

## **MPD Display**

PRISM MPD Display Elements

**Item name Description** Application Location of the application tile. The application tiles can be quarterTiles 1-8 screen, half-screen, or full-screen.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Getting Started 53** Display Elements

## PRISM MPD Display Elements

**Item name Description** Power Button Press the button to turn the instrument on or off. To completely remove power from the instrument, remove the power cord.

**CAUTION: To prevent data loss, we strongly recommend you first shut down the instrument before disconnecting the power cord. Press the power button or select** Settings **,** Utilities **,** Power **, and then** Power Down Now **.**

Status Bar The left side of the status bar has icons with links to various instrument settings including Volume ( ), Presets ( ), global Settings ( ), Input type ( ), and the Tile application menu ( ). Ee rs Select the **Home** icon ( ) to exit any displayed menus. The right side of the status bar lists instrument status such as the selected input, type of input signal, selected signal reference, video/ reference signal status, audio channel status, the real-time clock or PTP clock (to change the status bar clock, see _Change Status Bar Clock_ ), and a link to the Activity menu ( ).

**Note:** When you select an instrument setting, the menu appears and the status bar moves to the right. If you select another instrument setting on the status bar, the selected menu replaces the status bar.

Application Some applications have selectable tabs (highlighted readouts) you Tabs can use to view additional information. Application The name of the displayed application. Name

## **MPP Display**

The MPP has no built-in display, so one or two external displays can be connected. The instrument can also be operated without external displays using remote access features such as VNC and WebRTC, but a monitor must be connected to determine the IP address when the instrument is first turned on.

The MPP display can show up to four tiles if one external display is connected, and up to eight tiles if a second display is connected. The Extended Display Mode option (MPSDP-EXTNDSP) is required for 8 tile operation.

Refer to the MPP Rear Connectors section for important information about connecting external displays.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **54 Getting Started** Display Elements

## **Activity Center**

The Activity center tracks messages and devices in the PRISM. For example, you can view messages that allow you to eject devices mounted to the instrument. These steps explain how to eject a USB drive from the instrument using the Activity center.

A number above the Activity icon indicates the number of messages waiting in and devices connected to the instrument.

**1.** Select the Activity icon to view the DASHBOARD messages, which includes devices connected to the instrument. The instrument can use USBs formatted to exFAT or FAT32.

**Note:** After you insert a USB drive, you unmount via the Activity icon before removing it from the instrument.

**2.** Select the Eject icon ( B ) to unmount the USB drive from the instrument.

**Note:** If there is no USB drive in the instrument, the Eject USB Drive text and eject icon do not appear.

**3.** Select the Activity icon ( ) again to close the window.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Getting Started 55** Display Elements

## **Monitor Alarms**

The Activity DASHBOARD, in the status bar, provides a user-configurable alarm notification system. This allows the user to be notified only of the alarms of interest.

To configure which alarms you receive notifications for, select **Settings** menu, and then **Alarms** .

The Activity icon is color coded:

- A gray icon means no alarms have been activated.

- A yellow icon means at least one alarm was active, but it has cleared.

- A red icon means at least one alarm is currently active.

**Note:** Active alarms take precedence over cleared alarms. If there are cleared alarms and active alarms, the icon is red.

## **Use Activity DASHBOARD**

To _open_ the closed Activity DASHBOARD, select the **Activity** icon ( ).

To _close_ the open Activity DASHBOARD, select the **Activity** icon ( ).

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **56 Getting Started** Display Elements

The alarm group buttons and the alarm titles are color-coded.

- The Group buttons (ANC Session, Audio, etc.) color coding:
  - A gray button means no alarms in the group are turned on in the DASHBOARD.

  - A green button means at least one alarm in the group is turned on but no alarms are active.

  - A yellow button means at least one alarm in the group has been activated but it has cleared.

  - A red button means at least one alarm in the group has been activated and it is still active.

**Note:** A red (active) alarm takes precedence over yellow (cleared). If the group has both active and cleared alarms, the button is red.

- The alarm titles (under the group buttons) are color coded as follows:
  - A white title means the alarm is _not_ turned on in the DASHBOARD.

  - A green title means the alarm is turned on in the DASHBOARD and the alarm is not active.

  - A yellow title means the alarm was activated but it has cleared.

  - A red title means the alarm was activated and it is still active.

## **Turn Alarms On or Off in DASHBOARD**

**Note:** Turning alarms off means they are not tracked in the DASHBOARD or through the Activity icon. No color change or alarm occurs. The alarms are still logged in the Event Log application and sent to the Syslog server if turned on.

**1.** In the status bar, select the **Settings** icon ( ) and then select **Alarms** .

**2.** To turn on an alarm select the checkbox beside its name.

- To turn on a group of alarms in the DASHBOARD, select the checkbox of the alarm group.

- To turn an alarm group off, clear the checkbox.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Getting Started 57** Display Elements

- To turn on an alarm, select the title of a group of alarms to see the individual alarms, and then select the checkbox of the alarm.

- To turn an alarm off, clear the checkbox.

- An alarm with N/A under Threshold has no thresholds to set. To set the thresholds, select the alarm line, and then select the up or down arrow.

## **Acknowledge Alarm Notifications**

You can acknowledge all alarms on the dashboard or all alarms in the selected alarm group. When you acknowledge an alarm, the color changes to green.

- To acknowledge all alarms on the DASHBOARD, select **Acknowledge All Alarms** at the top of the DASHBOARD. The alarms and group buttons are green unless an

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **58 Getting Started** | Display Elements

alarm is still asserted; in that case, the alarm and the related group button remain red.

- To acknowledge all alarms in the selected alarm group, select **Acknowledge Group Alarms** at the top of the DASHBOARD. The alarms in the selected group and the group button are green unless an alarm is still asserted; in that case, the alarm and the related group button remain red.

## **Use Alarm Groups**

You can sort alarm groups for easier checking and clearing. You can also sort them by group in the Event Log.

## **Choose Alarm Group**

Select the group button from the options under the DASHBOARD header (such as ANC Session). The alarm group is circled in white, and the alarms in that group appear under the group buttons.

## **See Alarms in Event Log Application**

Select **View in tile 1** at the top of the DASHBOARD. The Event Log appears in tile 1, and the errors are filtered by the group selected in the Dashboard Alarm Group.

## **Filter Event Log Alarms by Group**

Select an alarm group and select **View in tile 1** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Methods of Operation 59** Touchscreen

## **Methods of Operation**

This chapter describes the primary methods of operating the instrument.

## **Topics**

■ Touchscreen

- Select and Organize Applications

- On-Screen Tools

■ Keyboard and Mouse Operation

■ Configure Extended Display

- Remote Control Operation

- Camera Tally and UMD

## **Touchscreen**

This section explains how to set up a second touchscreen display and how to use touchscreens with the applications. The following figure shows the PRISM display in four-tile mode with the All Applications menu open.

**Note:** Your available applications depend on the PRISM model and the installed options.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **60 Methods of Operation** Touchscreen

## **Supported Touchscreen Gestures**

To control the instrument, use these touchscreen gestures:

- Touch or tap the screen to select display elements.

- Double-tap an application to change the display between a quarter-screen and a full-screen display or between a half-screen tile and a full-screen display of the selected application. Double-tap a full-screen display to return to the quarter- or half-screen tile.

- Swipe up, down, left, or right to move through menus and preset listings, and to view additional application information.

- Pinch in to zoom in or pinch out to zoom out (if the application supports it).

**Note:** The terms “tap,” “swipe,” and “pinch” apply to the touchscreen on the instrument. If you are using a mouse and keyboard you must “click,” “scroll,” and use the scroll wheel on the mouse.

## **Touchscreen Feedback**

On touchscreen-enabled monitors, you can activate an on-screen marker to see where you touched a monitor.

To turn on the Touch Indicator:

**1.** Select the **Settings** icon (

- .

**2.** Select **Utilities** and then select **Touch Settings** .

**3.** Select the touch indicator size from the options: **Dot** , **Small** , **Med** , or **Large**

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Methods of Operation 61** Select and Organize Applications

To turn off the Touch Indicator:

**1.** Select the **Settings** icon (

- .

**2.** Select **Utilities** and then select **Touch Settings** .

**3.** Select **Off** .

## **Select and Organize Applications**

You can include up eight to application icons on the Applications toolbar, in any order. To open a different application in a tile:

**1.** On the status bar, select the **Tiles** icon ( ) to open the application bar.

**2.** Select a tile to replace with a different application.

**3.** Select an application from the application bar.

**4.** If an application is not on the application bar, select the **All Applications** menu icon ( ) to the right of the application bar.

**5.** Select the new application from the **All Applications** menu.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **62 Methods of Operation** Select and Organize Applications

**Note:** The applications available in the All Applications menu depend on what options were ordered.

## **Change Applications in Application Bar**

**1.** In the **All Applications** menu, select **Edit** from the menu header.

- Select an application marked with a number to remove it from the application bar.

**Note:** Removed applications leave that space open in the application bar only while the menu is in edit mode. If there is a space in the application list when the changes are saved, the applications are consolidated on the left and any spaces are moved to the right.

- Select **Clear All** to remove all the applications from the application bar.

- Select an application that is not marked with a number to add it to an empty space in the application bar.

**Note:** The applications are added to the Applications menu from the left. If the number 1 and 2 spaces are empty, the next selected application is added to the number 1 space.

**2.** Select **Save** . If you select the **Close** icon ( xX) ) before saving, a message appears asking if you want to save the changes. Select **Ok** to save the changes or **Cancel** to close the All Applications menu and return the application bar to the layout before you selected Edit.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Methods of Operation 63** Select and Organize Applications

**3.** Select the **Close** icon ( ).

## **Access Application Settings Menu**

**1.** Select the tile with the application.

**2.** Select the **Tiles** icon ( ) on the left of the application bar.

**3.** Select the **Tile** icon ( 2 | ). The application Settings menu appears.

## **Change Design of Interface (Two Options)**

On the Tiles menu and the All Applications menu, you can view application icons in color or gray scale. For easier visibility, you can modify the highlight color for the selected application and the selected tile.

## **Turn Color of Application Icons On or Off**

You can enable or disable color for applications in the All Applications menu and the applications bar.

**1.** Select the **Tiles** icon ( ) and then select the **All Applications** menu icon ( ).

**2.** In the All Applications menu header, select the **Colored Icons** button to turn the icon colors on or off.

## **Change Selected Application Border Color**

**1.** Select the **Tiles** icon ( ) and then select the **All Applications** menu icon ( ).

**2.** In the All Applications menu header, select **Border Color** to open the color options menu.

**3.** Select **Blue** , **White** , or **Yellow** . The border of any selected tile is highlighted in the chosen color.

## **Manage Tile Display**

Based on your requirements, you can display each application quarter-screen, halfscreen, or full-screen. The default for the PRISM instrument is to display four quarterscreen tiles. These configurations show how to expand the applications to half- or fullscreen tiles and reduce them back to a quarter of the screen.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **64 Methods of Operation** Select and Organize Applications

## **Half-Screen Tiles**

There are several half-screen configurations. To enlarge the tile vertically, select the **Tiles** icon ( ssTis ) and then select the **Half-Screen** icon ( reLt) ). To return to quarter-screen, select the **Reduce** icon ( ryLt ).

## **Full-Screen Tile**

One tile has expanded to use the entire PRISM monitor. To change to and from fullscreen mode:

- double-tap an application to change it between full-screen and quarter- or halfscreen mode; or

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Methods of Operation 65** Select and Organize Applications

- select the **Tiles** icon ( ) to open the application bar, and then select the **Reduce**
  - icon ( ) or the **Full Screen** icon ( ) to change views.

## **Quarter-Screen Tiles**

You can size tiles to a quarter-screen to view up to four tiles at the same time. To change between quarter-screen mode and larger displays, do one of the following:

- Expand Tile to Entire Monitor (Full-screen Mode):
  - Double-click or double-tap an application to change between quarter-screen tile and full-screen mode.

  - Select the **Tiles** icon ( ; ) to open the application bar, and then select the **Reduce** icon ( ) or the **Full-Screen** icon ( ) to change modes.

- Extend Tile Vertically (Half-screen Mode):
  - In the application bar, select the **Half-Screen** icon ( Lt ) to expand the tile vertically.

  - Select the **Reduce** icon ( Lt) ) to change the tile to a quarter-screen.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **66 Methods of Operation** On-Screen Tools

## **On-Screen Tools**

Some settings for the Waveform, Vector, Lightning, and Stop Display applications are available outside the settings menu through on-screen tools. Applications with onscreen tools enabled have buttons on the top and bottom of the display that allow you to adjust the application settings. When first selecting one of the displays, a highlighted ring appears around each available on-screen tool such as Gain, Format, Sweep, Cursors and Position. For instructions on how to use each on-screen tool, see these application sections:

- _Waveform Application On-screen Tools_

- _Vector Application On-screen Tools_

- _Stop Display Application On-screen Tools_

- Lightning Application On-screen Tools

- _CAM Application On-screen Tools_

- _External Reference Application On-screen Tools_

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Methods of Operation 67** Keyboard and Mouse Operation

## **Keyboard and Mouse Operation**

You can use a USB keyboard and mouse to operate the instrument. The mouse must have a scrolling wheel to access all of the menu selections. Select applications to perform actions as you would on the touch panel.

Connect the keyboard and mouse:

- Use the USB ports on the rear panel of the instrument (MPS) or front or rear panel (MPD or MPP).

- Connect an external monitor to any of the available display outputs, including Display Port.

**Home Icon:** The Esc key on the keyboard is mapped to function as the Home icon, which closes any displayed menus.

**Volume Control:** If your keyboard has volume control keys, you can use them to control the volume of the audio output on the instrument.

**Input and Preset Selection:** Keyboard controls for selecting SDI inputs and instrument presets lists the keyboard controls to quickly select between the SDI inputs and to select from instrument presets 1 through 6.

Keyboard Controls for Selecting SDI Inputs and Instrument Presets

| **Action** | **Keyboard**<br>**Control** | **Result**                                                                                                            |
| ---------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Input      | ALT+i                       | Prepare the instrument for an input selection.                                                                        |
| Preset     | ALT+p                       | Prepare the instrument for a preset selection from preset<br>Group A. Repeat 2 to 5 times to select preset Group B-F. |
| Select 1   | 1                           | Select Input 1 or select Preset 1 from the selected preset<br>group.                                                  |

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **68 Methods of Operation** Configure Extended Display

Keyboard Controls for Selecting SDI Inputs and Instrument Presets

| **Action** | **Keyboard**<br>**Control** | **Result**                                                           |
| ---------- | --------------------------- | -------------------------------------------------------------------- |
| Select 2   | 2                           | Select Input 2 or select Preset 2 from the selected preset<br>group. |
| Select 3   | 3                           | Select Input 3 or select Preset 3 from the selected preset<br>group. |
| Select 4   | 4                           | Select Input 4 or select Preset 4 from the selected preset<br>group. |
| Select 5   | 5                           | Select Input 5 or select Preset 5 from the selected preset<br>group. |
| Select 6   | 6                           | Select Input 6 or select Preset 6 from the selected preset<br>group. |

To select an SDI input or instrument preset:

**1.** On the keyboard, use one of two options:

- Press **ALT** and **i** at the same time to make an input selection change.

- Press **ALT** and at the same time press **p** one time to recall a preset from Preset Group A. Press the letter **p** 2-5 times to select a preset from another Preset Group (B-F). For example, press ALT and at the same time and press p three times to make a selection from Preset Group C.

**2.** Press a number from 1 to 6 to select the input or to select a preset from the selected Preset Group (A-F).

## **Configure Extended Display**

This section explains how to set up a second (extended) display for an MPS, MPD and MPP.

## **Configure MPP Primary Display**

The MPP product does not include a display, so an external display must be connected unless you plan to use remote access exclusively. Connect a DisplayPort monitor to the DP1 connector to establish a primary display.

## **Configure MPS or MPP Extended Display**

When a second display is connected to an MPS or MPP instrument, you can extend the main display to the second display. Extending the display increases the number of application tiles in the workspace. Using the extended display function requires

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Methods of Operation 69** Configure Extended Display

software option MPSDP-EXTNDSP; without the option, the main display is duplicated onto the extended display.

**1.** Connect the MPS/MPP to an external monitor that will serve as the extended display and power on both products. For MPS the monitor will plug into the DP port. For MPP, the monitor will plug into the DP2 port.

**2.** In the primary MPS/MPP display, select the **Settings** icon ( ) and then select **Display** .

**3.** Select **EXTENDED DISPLAY** .

**Note:** BRIGHTNESS controls are available on MPS and MPD products, depending on the display installed. See _Configure Brightness_ .

## **4.** Set **Extended Display Mode** to **Enabled** .

(For MPP, the “Extended Display Mode” selection will state “Use DP1 for Primary, DP2 for Extended.”)

If the second display is touch-enabled, identify the locations of the displays.

**1.** At Identify Touchscreens, select **Start** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **70 Methods of Operation** Configure Extended Display

**2.** Follow the on-screen instructions. When instructed to touch the Primary and Extended displays, make sure to touch on the touchscreens. Do not use a mouse. The touchscreens will not be properly identified if you use a mouse or if you configure remotely, such as with VNC.

**Note:** The process to identify the touchscreens can be performed again at any time. When the process completes successfully, it is not necessary to perform it again unless you change the touchscreen configuration, for example, if you change the USB port connections on the back of the instrument.

If needed, select a status bar for the extended display; in the Pinned Status Bar menu, select an option:

- **Off** : No status bar is in the extended display.

- **Input:** The Input status bar (the same status bar that appears when you select Input on the main display) appears in the status display.

- **Preset:** The Preset status bar (the same status bar that appears when you select Preset on the main display) appears in the status display.

**Note:** When you select Input or Preset to pin to the extended display, the Input or Preset option on the status bar is unavailable.

For information about configuring a generic display as the extended display, refer to the API Help for the **display_list** and **requested_display_mappings** .

## **Configure MPD Extended Display**

An MPD comes with two internal displays, so the software option MPSDP-EXTNDSP and the extended display are enabled by default. But there are advantages to turning the extended display off, like changing the aspect ratio of tiles 1-4 in a VNC application to make them larger and more readable.

**1.** Select the **Settings** icon ( ) and then select **Display** .

**2.** Select **EXTENDED DISPLAY** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Methods of Operation 71** Remote Control Operation

If needed, select a status bar for the extended display:

## **1.** Set **Extended Display Mode** to **Enabled** .

**2.** On the **Pinned Status Bar** menu, select an option:

- **Off:** No status bar is in the extended display.

- **Input:** The Input status bar (the same status bar that appears when you select Input on the main display) appears in the status display.

- **Preset** : The Preset status bar (the same status bar that appears when you select Preset on the main display) appears in the status display.

**Note:** When you select Input or Preset to pin to the extended display, the Input or Preset option on the status bar is unavailable.

## **Remote Control Operation**

You can control PRISM through WebRTC, VNC, API commands, or NMOS. The following section explains how to avoid connection loss, how to find the IP address, and how to find and change the hostname and password for PRISM.

## **Prevent Remote Connectivity Loss**

**Note:** Before setting a PRISM instrument for remote use, do not set the PRISM Control IP Port address to the subnet of any of the Video IP Ports (or the Video IP Ports subnet to the Control IP Port address), or all remote connectivity (WebRTC, VNC, API) will be lost. If connectivity is lost this way, you need local access to the PRISM to correct it.

For details about changing port addresses, see _Connect to a Network_ .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **72 Methods of Operation** | Remote Control Operation

When the Control IP address is set to the subnet of a Video IP Port, any request comes in on the Control port, but the response is returned through Video IP Port 1, so the response is not sent back to the sender, even though the PRISM Control port received the request. The sender is not connected to a network reachable by the Video IP Port 1.

This is an example of port settings that will cause a loss of connectivity:

- Control IP Port: 172.19.133.12 / 24 (255.255.255.0)

- Video IP Port 1: 172. _19_ .227.177 / 16 (255.255.0.0)

The Control IP Port address 172.19.133.12 is within the Video IP Port 172.19.xxx.xxx address.

Perform the following steps to change the subnet mask / prefix number without losing remote connectivity:

**1.** Disable the port.

- **A.** Select the **Settings** icon ( ) and then select **Network** .

- **B.** Select the **VIDEO IP PORT** tab.

- **C.** Change the **Data Rate** to the unselected option (if you are using a 10Gb rate, select 25Gb; if you are using 25Gb, select 10Gb).

**2.** In the **Subnet Mask / Preset** box, select the up or down arrows to set the number to **/30** .

**Note:** The /30 is close to a link local address. It is unlikely to accidentally forward traffic to that interface; the Video IP Ports can remain active without interfering with Control Port traffic.

**3.** On the **VIDEO IP PORT** tab, reset the **Data Rate** back to the original rate.

If you made this change locally, check whether remote connectivity is still available by signing in to the PRISM web page.

## **Find or Change Hostname, Password, and IP Address**

This section explains how to find the hostname, password, and IP address of a PRISM, as well as how and where to change the hostname and password.

## **Find Hostname**

On the status bar, the current hostname is under the Telestream logo.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Methods of Operation 73** Remote Control Operation

## **Change the Hostname**

**1.** On the PRISM monitor to connect to, select the **Settings** icon ( ) **.**

**2.** Select **Network** and then select the **REMOTE ACCESS** tab.

**3.** In the **Hostname** box, type a new hostname with the remote keyboard or the onscreen keyboard.

**4.** Select **Save** .

## **Find and Change Password**

**Note:** PRISM products are shipped with the same default password. It is strongly recommended to change the password as soon as possible after it is received.

**1.** On the PRISM monitor to connect to, select the **Settings** icon ( ) **.**

**2.** Select **Network** and then select the **REMOTE ACCESS** tab.

**3.** In the **Password** box, type a new password.

**4.** Select **Save** .

## **Find IP Address**

**1.** On the PRISM monitor to connect to, select the **Settings** icon ( ) **.**

**2.** Select **Network** and then select the **STATUS** tab. The IP address of the instrument is in the Control IP Port section.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **74 Methods of Operation** Remote Control Operation

## **Remote Control Through WebRTC**

When the PRISM monitor is connected to an Ethernet network, you can use a computer connected to the network to remotely control the instrument and listen to the audio through a web browser. Setting a remote connection has a point where is it possible to lose a connection that can only be corrected by direct, in-person access to the PRISM. To understand and prevent this problem, see _Prevent Remote Connectivity Loss_ .

To access eight tiles remotely on an MPS, it must be connected to a second display or a display emulator, and the Extended Display mode must be enabled.

To access eight tiles remotely on an MPP, it must be connected to two external displays, two display emulators, or no displays, and the Extended Display mode must be enabled.

## **Connect with WebRTC**

**1.** In a web browser, type the hostname or IP address of the PRISM. See _Find or Change Hostname, Password, and IP Address_ . When the PRISM is connected, the PRISM HOME page appears.

**2.** Select **Remote-WebRTC** . A sign-in page appears.

**3.** In the **Password** box, type the password for that instrument.

**4.** If it is needed, in the **User Name** box, type the user name for the WebRTC chat tool.

**5.** Select **WebRTC Connect** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Methods of Operation 75** Remote Control Operation

**Note:** If you cannot log in to WebRTC via Google Chrome, press **Ctrl+Shift+R** to refresh the browser cache, and then log in to WebRTC.

## **Adjust WebRTC Settings**

Select the **WebRTC** menu button at the top left of the tiles. The WebRTC menu appears at the top of the tiles.

## **WebRTC Access**

Displays the hostname of the instrument.

## **Bitrate**

The slider control changes the bandwidth and fidelity of the images. If the data available (for example on a slow network) does not allow a smooth view, or freezes the image, of the PRISM information, adjust the Bitrate control. Start with Bitrate at 2 MB or less. Any change to the Bitrate control changes the bitrate of all the users on the instrument.

## **Chat**

Select to open a chat message window with other people using the PRISM through WebRTC. If you entered a user name when you logged in, it is shown in the chat window. If you did not enter a user name, a hexadecimal ID is shown.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **76 Methods of Operation** Remote Control Operation

## **Start Recording**

Select to start and stop a recording of the screen and audio as it is presented on the PRISM. When recording is stopped, an automatically named .webm file is downloaded to the local computer in the Downloads folder.

## **Volume**

Select to turn the audio on and off. The WebRTC volume level is controlled with the computer volume controls.

## **Remote Control Through VNC Operation**

When the PRISM monitor is connected to an Ethernet network, you can use a computer connected to the same network to remotely control the instrument in a web browser or in a VNC client such as VNC Viewer. Setting a remote connection has a point where is it possible to lose a connection that can only be corrected by direct, in-person access to the PRISM. To understand and prevent this problem, see _Prevent Remote Connectivity Loss_ .

To access eight tiles remotely on an MPS, it must be connected to a second display or a display emulator, and the Extended Display mode must be enabled.

To access eight tiles remotely on an MPP, it must be connected to two external displays, two display emulators, or no displays, and the Extended Display mode must be enabled.

## **Connect with VNC Client**

When using VNC for extended periods of time, we recommend using a VNC client:

**1.** On an Internet-connected computer, open a VNC client.

**2.** Enter the hostname or IP address from the instrument in the VNC Server search bar. See _Find or Change Hostname, Password, and IP Address_ . The VNC client connects to the instrument in a separate window.

## **Connect with Web Browser**

**1.** Enter the hostname or IP address from the instrument in a web browser. See _Find or Change Hostname, Password, and IP Address_ . The PRISM HOME page appears.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Methods of Operation 77** Remote Control Operation

**2.** Select **Remote-noVNC** . The noVNC page appears.

**3.** Select **Connect** . The sign-in page appears.

**4.** Enter the password for that instrument in the **Password** box and select **Send Credentials** .

To adjust the scale of the PRISM tiles if the tiles do not all fit on the display:

**1.** In the PRISM web interface, select the control tab on the left side of the tiles to open the noVNC settings.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **78 Methods of Operation** Remote Control Operation

**2.** Select the **Settings** icon.

**3.** In the **Scaling Mode** menu, select **Local Scaling** . The tiles resize to fit the web browser window.

**4.** Select the **Settings** icon again to close the Settings menu.

## **Remote Control Through API Commands**

The PRISM monitor has a command set for controlling the instrument using REST-style API commands. You can use GET and POST commands to configure the virtual inputs and to select the active input. Setting a remote connection has a point where is it possible to lose a connection that can only be corrected by direct, in-person access to the PRISM. To understand and prevent this problem, see _Prevent Remote Connectivity Loss_ .

**1.** Enter the hostname or IP address in a web browser. See _Find or Change Hostname, Password, and IP Address_ . The PRISM HOME page appears.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Methods of Operation 79** Camera Tally and UMD

**2.** Select **API Help Page** . A PRISM API Documentation web page similar to the sample appears.

## **Remote Control Through NMOS**

See _Using NMOS_ for details about NMOS remote control of the instrument.

## **Camera Tally and UMD**

Camera Tally and Under Monitor Display (UMD) allows use of the TLS version 5.0 protocol over Ethernet using UDP transport to send information to the IP address of PRISM using port 5446. This protocol provides red, amber, or green indication per tile of the state of the channel and can be used to provide an ASCII character label that will appear in the tile. A fourth Tally function provides a red dot in the upper right corner of the tile.

**1.** Select the **Settings** icon ( ) and then select **Display** .

**2.** Select **Tally UMD** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **80 Methods of Operation** Camera Tally and UMD

**Note:** BRIGHTNESS controls are available on MPS and MPD products, depending on the display installed. See _Configure Brightness_ .

**3.** Set **TALLY** to **Enabled** to enable the received TSL protocol to provide information for each of the tile displays and allow the indication of red, amber, or green to be shown for the appropriate tile.

To disable this Tally display, set **TALLY** to **Disabled** . Note: Disabling Tally resets the tally configurations.

**4.** Set **UMD** to **Enabled** to allow an on-screen label to be overlaid on a tile when the appropriate protocol message is sent.

To disable this UMD label on-screen, set **UMD** to **Disabled** .

**5.** From the **Position** list, select the position of the UMD label: **Top** or **Bottom** of the tile.

**6.** From the **Background Color** list, select the background color of the UMD label: **Black** , **Red** , **Green** , or **Blue** .

**7.** From the **Background Transparency** list, select the background transparency level for the UMD label: **Solid** , **25%** transparency, **50%** transparency, **75%** transparency, or **Clear** .

**8.** From the **Picture / Trace Size** list, select one of the following:

- **Normal** – The UMD label is overlaid on top of the tile.

- **Shrunk** – The Picture or Trace is scaled so the UMD label does not obscure any part of the tile display.

- **Auto** – The tile content is shrunk only if the UMD label is enabled and present.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Methods of Operation 81** Camera Tally and UMD

The following image shows Tally and UMD information being sent to multiple tiles. This configuration has UMD positioned at the top of the tile with a solid black background and a normal overlay of the label within the tile.

To display Tally/UMD information on a tile, version 5.0 UMD messages must be sent with the following fields:

**Note:** The TSL UMD/Tally protocol specifies little-endian (LSB/MSB) byte order. All examples provided are in little-endian format.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **82 Methods of Operation** Camera Tally and UMD

- **INDEX Field:** The INDEX field (16 bits) in the (DMSG) section controls tile selection, subtile selection, and fourth tally. The template is as follows:

- **CONTROL** (16 bits) within the (DMSG) section manages the main tally lights for each tile:
  - **Bits 0-1:** Control the red tally light. These bits are also used to control the fourth tally light when it is enabled (as indicated by the INDEX field).

  - **Bits 2-3:** Control the amber tally light.

  - **Bits 4-5:** Control the green tally light.

- **(Display Data):** This section controls the UMD text displayed on each tile.
  - **LENGTH:** (16 bits) Indicates the byte count of the text field (maximum 20 characters). Set to 0 to turn off UMD for that tile.

  - **TEXT:** Contains the actual UMD text to be displayed. Note that 0x00 should be interpreted as a space character (0x20).

**Important note:** The TSL UMD/Tally protocol uses little-endian byte order. This means that the least significant byte (LSB) of the INDEX value is transmitted first, followed by the most significant byte (MSB).

For additional information, see Tally Protocol 5.0:

https://tslproducts.com/wp-content/uploads/TSL-UMD-protocol.pdf

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Methods of Operation 83** Camera Tally and UMD |

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **84 Configure the Instrument** | Configure and Select Virtual Inputs

## **Configure the Instrument**

This chapter describes how to configure these instrument settings:

- Virtual inputs: _Configure and Select Virtual Inputs_

- HDR monitoring: _Configure Instrument for HDR/WCG Monitoring_

- PTP reference settings: _Configure Reference Settings_

- Presets: _Configure and Recall Instrument Presets_

- Internal time and date: _Configure Time and Date_

- Firmware upgrade: _Upgrade Instrument Firmware_

- Installed software and hardware versions: _Verify Firmware Upgrade_

Most of the instrument settings are controlled using the Settings menu. To access the ~~ee~~ global settings menu, select the **Settings** icon ( ) in the status bar.

**Note:** Some settings require you to enter values. You can use a USB keyboard to enter these values instead of using the touchscreen keypad on the instrument.

## **Configure and Select Virtual Inputs**

To configure multiple virtual inputs, select **Settings** and then select **Inputs** for options:

- _Configure SDI Inputs_

- _Configure IP Inputs_ (this includes ST 2022-6 and ST 2110-20/22/30/31/40 and RTP streams)

- _Select Input_

- _Rename Virtual Input_

The input selection options are in the middle of the status bar. The first line is the userdefined name, and the second line is the format.

**CAUTION: IGMP communications fail if the Video IP Ports are configured for the same IP address.** ~~a~~

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 85** Configure and Select Virtual Inputs

## **Configure SDI Inputs**

**Note:** SDI Quad link for 4K or 8K is available only when the MPSDP-FMT-4K or MPSDPFMT-8K software option is present. If it is not present, you can configure only a singlelink input. SDI single link for SD, HD, and 3G is always available.

## **Configure SDI Input**

**1.** Select the **Settings** icon ( ).

**2.** Select **Inputs** .

**3.** Select an input and then select **SDI** .

**Note:** You can give the virtual inputs any meaningful name.

**4.** Select one of the following options:

- select **Single** for the Input Configuration and select one of the four physical SDI inputs to monitor; or

- select **Quad Link** for the Input Configuration and confirm that Quad Link cables are connected to the back of the instrument:
  - ♦ Quad Link A is connected to SDI-IN 1.

  - ♦ Quad Link B is connected to SDI-IN 2.

  - ♦ Quad Link C is connected to SDI-IN 3.

  - ♦ Quad Link D is connected to SDI-IN 4.

**Note:** To use Quad Link Inputs, you must connect all four SDI inputs to a cable on the back of the PRISM.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **86 Configure the Instrument** Configure and Select Virtual Inputs

**5.** If you selected Quad Link in the previous step, select a UHD/4K Mode: **Auto** , **Sq Div** (Square Division), or **2 SI** (Two Sample Interleave). SDI 1-4 (Link A-D) is selected by default.

**Note:** The Quad Link and UHD/4K Mode buttons are available when the MPSDP-FMT4K software option is present.

In AUTO mode, the instrument defaults to Two Sample Interleave mode if the Video Payload Identifier (VPID) complies with ST 425.3 or ST 425.5. The instrument defaults to Square Division mode if the VPID complies with ST 292.1, ST 372, ST 425.1, or a quad-HD signal is present and VPID is missing. VPID in the signal is required for this option to operate properly.

The 8K format trace applications—Waveform, Stop, Vector, Diamond, and Lightning

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 87** Configure and Select Virtual Inputs

Displays, enabled by MPSDP-FMT-8K—are rendered based on the resized 8K signal and are suitable for operational applications such as setting camera exposure for live programming. However, this approach might not be suitable for some engineering applications. This approach impacts only 8K formats and not SD/HD/3G/4K formats in operations or engineering. 8K formats can use up to four trace applications.

## **Select SDI Video Settings**

These settings are the same for Single and Quad Link input configurations. The Gamma and Color Gamut settings define the characteristics of the video signal.

**Note:** Auto is the preferred setting for video options. At this setting, PRISM determines the settings from the signal or any metadata (if present).

## **1.** Under **SDI** , select **Video** .

**==> picture [3 x 5] intentionally omitted <==**

**----- Start of picture text -----**<br>
)<br>**----- End of picture text -----**<br>

**2.** In the **Format** list, select one of the following:

- **Auto:** The system selects the setting based on the information in the incoming signal.

- **525i**

- **625i**

- **720p**

- **1080i**

- **1080PsF**

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **88 Configure the Instrument** Configure and Select Virtual Inputs

- **1080p**

- **2048x1080p**

- **3840x2160p**

- **4096x2160p**

- **7680x4320p**

**3.** If a 3-gigabit transport is being used, select **In 3G-SDI** and choose one of the following:

- **Auto:** The system selects the setting based on the information in the incoming signal.

- **Level A**

- **Level B**

**4.** From the **Gamma Curve** list, select one of the following; the selection characterizes the video signal on each virtual input.

- **Auto:** The system selects the setting based on ST 352 VPID. If 352 VPID is not present, SDR Narrow is selected.

- **SDR Narrow:** The reference OETF (Optical to Electrical Transfer Function) is defined in ITU-R BT.709 with gamma of 0.45 and the reference EOTF is defined in ITU-R BT.1886 with gamma of 2.4.

The Narrow scaling places the extremes of the nonlinear color value from zero to unity at code words 40 hex (64 dec) and 3AC hex (940 dec) in a 10-bit representation for 0% to 100% graticule scale. This range is typical for standarddynamic range.

- **SDR Full:** The reference OETF is defined in ITU-R BT.709 with gamma of 0.45 and the reference EOTF (Electrical to Optical Transfer Function) is defined in ITU-R BT.1886 with gamma of 2.4.

The full scaling places the extremes of the nonlinear color value from zero to unity at code words 0d and 1023d in 10-bit representation and 0d and 4095d in 12-bit representation for 0% black and 100% white, respectively.

- **PQ Narrow:** The reference OETF with a high luminance range capability of 0 to 10,000 cd/m[2] standardized in ST 2084. The EOTF is the inverse of OETF.

The narrow scaling places the extremes of the nonlinear color value from zero to unity at code words 40 hex (64 dec) and 3AC hex (940 dec) in a 10-bit representation for 0% to 100% graticule scale. This range is typical for standarddynamic range.

- **PQ Full:** The reference OETF with a high luminance range capability of 0 to 10,000 cd/m[2] standardized in ST 2084. The EOTF is the inverse of OETF.

The full scaling places the extremes of the nonlinear color value from zero to unity at code words 0d and 1023d in 10-bit representation and 0d and 4095d in 12-bit representation for 0% black and 100% white, respectively.

- **HLG:** The reference OETF is standardized in ARIB B67 and the reference EOTF is standardized in ITU BT.2100 at the nominal display peak luminance of 1000 nits.

- **S-Log2:** The reference OETF is defined as Sony S-Log2.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 89** Configure and Select Virtual Inputs |

- **S-Log3:** The reference OETF is defined as Sony S-Log3.

- **S-Log3 (Live HDR):** The reference OETF and OOTF (Optical to Optical Transfer Function) are defined as Sony S-Log3 (Live HDR).

- **Log C:** The reference OETF is defined as ARRI Log C.

**5.** From the **Structure** list, select one of the following:

- Auto: The system selects the setting based on ST 352 VPID. If VPID is not present, YCbCr 4:2:2 10bit is selected.

- YCbCr 4:2:2 10bit

- YCbCr 4:2:2 12bit

- YCbCr 4:4:4 10bit

- RGB 4:4:4 10bit

- RGB 4:4:4 12bit

**6.** From the **Color Gamut** list, select one of the following; the selection determines the color space of the video signal selection.

- **Auto:** The system selects the setting based on ST 352 VPID. If ST 352 VPID is not present, Rec. 709 is selected.

- **Rec. 709:** Standard for HD

- **Rec. 2020:** Standard for 4K

**Note:** Rec. 709 gamut is selected automatically when the SD format is detected / selected in the video signal.

**7.** From the **Favorite 3D LUTs** list, select a 3D LUT.

Telestream provides a standard set of Lookup Tables (LUTs) for Convert to Rec. 709. You can add your own LUTs via the web page of the instrument. For details, see _Using 3D Lookup Tables_ . From the available LUTs installed in the PRISM, you can select the Favorites to appear in the selection list in addition to Convert to Rec. 709.

> To save a 3D LUT as a favorite, select the Information icon ( ® ) and select the star beside a LUT. To save a 3D LUT as a favorite, select the star beside the LUT.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **90 Configure the Instrument** Configure and Select Virtual Inputs

## **Select SDI Audio Settings**

The Audio settings define how the audio is embedded in the SDI input signal. These settings are the same for Single and Quad Link input configurations, except the Quad Link, which is intended for 8K, can have 32 channels—instead of 16—in Program Configuration.

**1.** Under **SDI** , select **AUDIO** .

**2.** To enable 32-channel mode (UHD, 4K, and 8K only), set **32 Channel Mode** to **On** .

**Note:** In 12G 32-channel mode, the first 16 channels come from virtual link 1, and the next 16 channels come from virtual link 2. This conforms with standards ST 2082-10 for 12G-SDI and ST 2082-12 for Quad 12G-SDI.

**3.** Configure one type of audio: See _Configure PCM_ , _Configure DOLBY_ , or _Configure DOLBY ED2_ (use of Dolby or Dolby ED2 requires the MPSDP-DLBY license).

## **Configure PCM**

**1.** Under **AUDIO** , select **PCM** .

**2.** Select **Program Configuration** .

**3.** Set **Program Configuration** to **On** .

**4.** Select **Edit** . The Edit button is replaced by the Default, Clear, and Undo buttons.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 91** Configure and Select Virtual Inputs

**Note:** 8k (Quad 12G-SDI Link) and 4K (Single 12G-SDI Link) can have 32 channels instead of 16.

**5.** Select the type of program (such as mono or stereo) and select the audio channel to assign to it. Repeat until all audio in the current input signal has programs assigned to channels.

- **M** is mono and requires one channel.

- **ST** is stereo and requires two channels.

- **5.1** is surround sound and requires six channels. To change the channel order in the audio bars, see _5.1 Channel Order_ .

- **7.1** is surround sound and requires eight channels.

- **5.1.4** is immersive audio and requires 10 channels: six for the audio main bed, or level–marked in cyan, and four for the audio upper bed, marked in orange.

**Note:** 5.1.4 provides bar labels for the audio channels, but is not available for downmix capability or for loudness display.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **92 Configure the Instrument** Configure and Select Virtual Inputs

- **7.1.4** is immersive audio and requires 12 channels: eight for the audio main bed, or level–marked in cyan, and four for the audio upper bed, marked in orange.

**Note:** 7.1.4 provides bar labels for the audio channels but is not available for downmix capability or for loudness display.

- **Unassigned** removes an assignment from a channel. Select **Unassigned** and select any block in an assignment, for example, the middle of a 7.1 assignment, the entire assignment is removed and is not displayed on the Audio application.

- **Default** resets the channels to eight stereo pairs.

- **Clear** removes all assignments, including the default.

**6.** Select **Save** and close the menu.

**Note:** You must save the program configuration to update the programs in the audio bars and loudness meter.

## **Configure DOLBY**

**Note:** Dolby selection works with Dolby D, D Plus, or E signals.

**1.** Under **AUDIO** , select **DOLBY** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 93** Configure and Select Virtual Inputs

**2.** From the **Dolby Audio Ch Pair** list, select the audio channel pair that contains Dolby audio.

**3.** If needed, identify Dolby Audio Channels, or go to Step D:

- **A.** Open the Audio application.

- **B.** Return to the **Inputs** menu and select **PCM** in Audio.

- **C.** In the Audio application, in the audio levels, find and note the audio channels marked with DOLBY D or DOLBY E.
  - **a.** In the **Inputs** menu, select **DOLBY** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **94 Configure the Instrument** Configure and Select Virtual Inputs

- **b.** From the **Dolby Audio Ch Pair** list, select the channel pair that is marked as DOLBY in the Audio application. The audio bar layout is configured automatically based on the metadata in the Dolby stream.

- **D.** Select **Save** and close the menu.

## **Configure DOLBY ED2**

**1.** Under **AUDIO** , select **DOLBY ED2** .

**2.** In the **Dolby ED2 Audio Ch Pairs** menu, select the consecutive channel pairs that contain Dolby ED2 audio.

**3.** If needed, identify Dolby ED2 Audio Channels, or go to Step D:

- **A.** In the **Inputs** menu, select **PCM** (instead of DOLBY ED2).

- **B.** Open the Audio application.

- **C.** In the Audio application, in the audio levels, find and note the audio channels marked with “DOLBY ED2.”

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 95** Configure and Select Virtual Inputs

- **a.** In the **Inputs** menu, select **DOLBY ED2** (instead of PCM).

- **b.** From the **Dolby ED2 Audio Ch Pairs** list, select the channel pairs that are marked as DOLBY ED2 in the Audio application. Dolby ED2 metadata in the selected channels is decoded.

**Note:** When you select Dolby ED2 in the Inputs menu, the Audio application stops presenting data. This is expected; only Dolby ED2 metadata is supported.

## **D.** Select **Save** and close the menu.

**Note:** The audio programs that you configure in the Program Configuration menu are used to select a program for measurement by the Loudness application, to display audio bars in the Audio application, and to monitor with headphones. When all the channels are unassigned, all channels are treated as stereo pairs. The audio programs in the Dolby stream are set up automatically based on the Dolby metadata.

## **Rename Virtual Input**

**1.** Select the **Settings** icon ( ).

**2.** Select **Inputs** .

**3.** Select an input and then select the **Name** field. The text editing display appears.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **96 Configure the Instrument** Configure and Select Virtual Inputs

**4.** Use the editing controls to enter a new name for the input. Some notes on using the text editor:

- Enter a name with up to 16 characters.

- Select the **Clear** icon ( ) next to the input box to remove the existing name.

- Tap the **Shift** key to access capital letters.

- Tap **Backspace** to delete characters.

- Tap the **123-abc** key to change between accessing letters, and numbers and symbols.

**5.** Select **Enter** and then select **Save** .

## **Configure IP Inputs**

This section describes the settings for IP inputs.

## **Configure Data Rate**

**1.** Select the **Settings** icon ( ).

**2.** Select **Network** .

**3.** Select the **VIDEO IP PORT** tab.

**4.** Select a **Data Rate** : **10Gb** or **25Gb** . The Data Rate applies to both ports; both ports must be 10 Gb or 25 Gb.

**Note:** If you cannot select the 25Gb button, the MP2-25GE license has not been installed.

**5.** If you are using a 25GE connection with RS-FEC, set **FEC** to **RS-FEC** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 97** Configure and Select Virtual Inputs

**Note:** If the 25-GE signal from the switch does not match the PRISM in FEC setting, the IP Status Port displays a red X and 0.0 bps. This response is similar to a disconnected fiber cable.

PRISM does not support RS-FEC auto-negotiation; you might have to manually configure your switch to enable or disable RS-FEC.

- If the instrument can read the multisource agreement (MSA) data from the installed SFP module, the data rate of the SFP module and the optical wavelength is displayed in the SFP Module line.

- If the SFP module speed does not match the Data Rate setting, instead of the data rate and frequency, the message “SFP not compatible with selected Data Rate” appears.
  - If the SFP module does not have readable MSA data, instead of the data rate and frequency, the message “Unknown” appears.

**Note:** If MSA data is missing, the SFP Module line displays no compatibility warning regardless of what type of SFP module is installed or the Data Rate setting. The instrument and the SFP module work if the SFP module matches the Data Rate setting.

- If no SFP module is installed, instead of data rate and frequency, the message “Disconnected” is displayed.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **98 Configure the Instrument** Configure and Select Virtual Inputs

Possible Status in the VIDEO IP PORT, SFP Module Line

| **Type of SFP installed** | **Data Rate setting**     | **Data Rate setting**     |
| ------------------------- | ------------------------- | ------------------------- |
|                           | **10 Gb setting**         | **25 Gb setting**         |
| SFP 25-Gb module          | SFP not compatible…       | (Data rate) / (frequency) |
| SFP 10-Gb module          | (Data rate) / (frequency) | SFP not compatible…       |
| Unreadable MSA data       | Unknown                   | Unknown                   |
| No SFP installed          | Disconnected              | Disconnected              |

**1.** Select **RS-FEC** if Forward Error Correction (FEC) is needed. RS-FEC is specified by IEEE 802.3 Clause 91.

**Note:** FEC is available only when the Data Rate is set to 25Gb. If you turn on FEC, it is turned on for both ports.

- The IP Status display shows the Data Rate setting, FEC setting, and signal status.

**Note:** If the Data Rate or FEC are incorrect, a red X appears on the left of the traffic bar, as when the fiber is disconnected.

- The Data Rate setting (10 or 25 Gb) is on the right of the network traffic bar.

- The FEC setting is below the data rate.

- The signal status is on the left of the network traffic bar.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 99** Configure and Select Virtual Inputs

Possible Status of the Ports in IP Status

| **Type of SFP installed** | **Data rate setting** | **Data rate setting** |
| ------------------------- | --------------------- | --------------------- |
|                           | **10 Gb**             | **25Gb**              |
| SFP 25-Gb module          | SFP Mismatch          | OK                    |
| SFP 10-Gb module          | OK                    | SFP Mismatch          |
| Unreadable MSA data       | Unknown               | Unknown               |
| No SFP installed          | Disconnected          | Disconnected          |

**1.** If the IP Status Port displays “SFP Mismatch,” repeat Steps 1 through 4 to confirm that the Data Rate is set correctly, and check whether the installed SFP module has the expected data rate.

## **Configure ST 2022-6**

This section is relevant to the 200 and 300 versions of the MPS, MPD, and MPP.

**Note:** If you are not using ST 2022-6, go to _Configure ST 2110_ .

**1.** Select the **Settings** icon ( ).

**2.** Select **Inputs** .

**3.** Select an input from the list.

**4.** Select **IP** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **100 Configure the Instrument** Configure and Select Virtual Inputs

**5.** Select **ST2022-6** .

**6.** Select **ST2022-7 Seamless Switching** to enable or disable it.

**Note:** There is a difference between “port” and “path.” The port is the physical SFP port that is used to input the 10/25GE signal. Path 1 and Path 2 are the signal paths to be used for seamless switching. This differentiation is being made because it is possible for both Path 1 and Path 2 to use a single port.

With ST 2022-7 seamless switching, a reconstructed output stream is created from the two input streams. The reconstructed stream is used downstream for various display tiles like Picture. The buffer size to absorb the packet reception time difference between Path1 and Path2 is 10 ms. The output stream reconstruction does not work properly for streams on Path1 and Path2 with skew greater than 10 ms. This error makes tiles show the wrong images and information.

**7.** Enter the Source and Destination information for Path 1 and Path 2, if applicable.

**Note:** Path 2 is available if ST 2022-7 Seamless Switching is enabled. You might have to scroll down to see Path 2.

- To have the instrument ignore a parameter, select **Unmasked** next to the parameter to change the state to Masked.

- To edit a parameter value, select inside the parameter box to open the editing display. An on-screen keypad appears.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 101** Configure and Select Virtual Inputs

**8.** When you are done editing, select **Enter** .

**9.** Scroll down to enter the Source and Destination information for Path 2.

## **Select ST 2022-6 Video Settings**

The Gamma and Color Gamut settings are the same for ST 2022-6 and ST 2110 video stream configurations, but the ST 2110 menu has a different layout. The settings define the characteristics of the video signal.

**1.** Under **ST2022-6** , select **Video** .

**2.** From the **Gamma Curve** list, select one of the following; the selection characterizes the video signal on each virtual input

- **Auto:** The system selects the setting based on ST 352 VPID. If 352 VPID is not present, SDR Narrow is selected.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **102 Configure the Instrument** Configure and Select Virtual Inputs

- **SDR Narrow:** The reference OETF (Optical to Electrical Transfer Function) is defined in ITU-R BT.709 with gamma of 0.45 and the reference EOTF (Electrical to Optical Transfer Function) is defined in ITU-R BT.1886 with gamma of 2.4.

The Narrow scaling places the extremes of the nonlinear color value from zero to unity at code words 40 hex (64 dec) and 3AC hex (940 dec) in a 10-bit representation for 0% Black to 100% White. This range is typical for standarddynamic range.

- **SDR Full:** The reference OETF is defined in ITU-R BT.709 with gamma of 0.45 and the reference EOTF is defined in ITU-R BT.1886 with gamma of 2.4.

The full scaling places the extremes of the nonlinear color value from zero to unity at code words 0d and 1023d in 10-bit representation and 0d and 4095d in 12-bit representation for 0% black and 100% white, respectively.

- **PQ Narrow:** The reference OETF with a high luminance range capability of 0 to 10,000 cd/m[2] standardized in ST 2084. The EOTF is the inverse of OETF.

The narrow Scaling places the extremes of the nonlinear color value from zero to unity at code words 40 hex (64 dec) and 3AC hex (940 dec) in a 10-bit representation for 0% Black to 100% White. This range is typical for standarddynamic range.

- **PQ Full:** The reference OETF with a high luminance range capability of 0 to 10,000 cd/m[2] standardized in ST 2084. The EOTF is the inverse of OETF.

The Full scaling places the extremes of the nonlinear color value from zero to unity at code words 0d and 1023d in 10-bit representation and 0d and 4095d in 12-bit representation for 0% black and 100% white, respectively.

- **HLG:** The reference OETF is standardized in ARIB B67 and the reference EOTF is standardized in ITU BT.2100 at the nominal display peak luminance of 1000 nits.

- **S-Log2:** The reference OETF is defined as Sony S-Log2.

- **S-Log3:** The reference OETF is defined as Sony S-Log3.

- **S-Log3 (Live HDR):** The reference OOTF is defined as Sony S-Log3.

- **Log C:** The reference OETF is defined as ARRI Log C.

**3.** From the **Color Gamut** list, select one of the following; the selection is the color space of the video signal.

- **Auto:** The system selects the setting based on ST 352 VPID. If 352 VPID is not present, Rec. 709 is selected.

- **Rec. 709:** Standard for HD.

- **Rec. 2020:** Standard for 4K.

**Note:** Rec. 709 gamut is selected automatically when the SD format is detected or selected in the video signal.

**4.** From the **Favorite 3D LUTs** list, select a 3D LUT.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 103** Configure and Select Virtual Inputs |

> To save a 3D LUT as a favorite, select the Information icon ( ® ) and select the star beside a LUT. 3D LUTs marked as favorites will be selectable in the Settings Input menu.

## **Select ST 2022-6 Audio Settings**

**1.** Under **ST2022-6** , select **AUDIO** .

**2.** Configure one type of audio: See _Configure PCM_ , _Configure DOLBY_ **,** or _Configure DOLBY ED2_ (use of Dolby requires the MPSDP-DLBY license).

## **Configure PCM**

- **A.** Under **AUDIO** , select **PCM** .

## **B.** Select **Program Configuration** .

## **C.** Set **Program Configuration** to **On** .

- **D.** Select **Edit** . The Edit button is replaced by the Default, Clear, and Undo buttons.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **104 Configure the Instrument** Configure and Select Virtual Inputs

- **E.** Select the type of program (mono, stereo, etc.) and select the audio channel to assign to it. Repeat until all the audio in the current input signal have programs assigned to channels.
  - ♦ **M** is mono, one channel.

  - ♦ **ST** is stereo, two channels.

  - ♦ **5.1** is surround sound, six channels.

To change the channel order in the audio bars, see _5.1 Channel Order_ .

- ♦ **7.1** is surround sound, eight channels.

- ♦ **5.1.4** is immersive audio and requires 10 channels: six for the audio main bed, or level–marked in cyan, and four for the audio upper bed, marked in orange.

**Note:** 5.1.4 provides bar labels for the audio channels but is not available for downmix capability or for loudness display.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 105** Configure and Select Virtual Inputs

- ♦ **7.1.4** is immersive audio and requires 12 channels: eight for the audio main bed, or level–marked in cyan, and four for the audio upper bed, marked in orange.

**Note:** 7.1.4 provides bar labels for the audio channels but is not available for downmix capability or for loudness display.

- ♦ **Unassigned** removes an assignment from a channel. Select **Unassigned** and click any block in an assignment, for example the middle of a 7.1 assignment, and the entire assignment is removed and is not displayed on the Audio application.

- ♦ **Default** resets the channels to eight stereo pairs.

- ♦ **Clear** removes all assignments, including the default.

- **F.** Select **Save** and close the menu.

**Note:** You must save the program configuration to update the programs in the audio bars and loudness meter.

## **Configure DOLBY**

**Note:** Dolby selection works with Dolby D, D Plus, or E signals.

- **A.** Under **AUDIO** , select **DOLBY** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **106 Configure the Instrument** Configure and Select Virtual Inputs

- **B.** From the **Dolby Audio Ch Pair** list, select the audio channel pair that contains Dolby audio.

- **C.** If needed, identify Dolby Audio Channels, or go to Step D:
  - **a.** Open the Audio application.

  - **b.** Return to the **Inputs** menu and select **PCM** .

  - **c.** In the Audio application, in the audio levels, find and note the audio channels marked with DOLBY D or DOLBY E.

  - **d.** In the **Inputs** menu, select **DOLBY** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 107** Configure and Select Virtual Inputs

- **e.** From the **Dolby Audio Ch Pair** list, select the channel pair that is marked as DOLBY in the Audio application. The audio bar layout is configured automatically based on the metadata in the Dolby stream.

- **D.** Select **Save** and close the menu.

**Note:** Audio programs configured in the Program Configuration menu are used to select a program for measurement by the Loudness application, to display audio bars in the Audio application, and to monitor with headphones. When all the channels are unassigned, all the channels are treated as stereo pairs. The audio programs in the Dolby E stream are automatically set up based on the Dolby D/D Plus/E metadata.

## **Configure DOLBY ED2**

## **A.** Under **AUDIO** , select **DOLBY ED2** .

- **B.** From the **Dolby ED2 Audio Ch Pairs** list, select the consecutive channel pairs that contain Dolby ED2 audio.

- **C.** If needed, identify Dolby ED2 Audio Channels, or go to Step D:
  - **a.** In the **Inputs** menu, select **PCM** (instead of DOLBY ED2).

  - **b.** Open the Audio application.

  - **c.** In the Audio application, in the audio levels, find and note the audio channels marked with “DOLBY ED2.”

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **108 Configure the Instrument** Configure and Select Virtual Inputs

- **d.** In the **Inputs** menu, select **DOLBY ED2** (instead of PCM).

- **e.** From the **Dolby ED2 Audio Ch Pairs** list, select the channel pairs that are marked as DOLBY ED2 in the Audio application. Dolby ED2 metadata in the selected channels is decoded.

**Note:** When you select Dolby ED2 in the Inputs menu, the Audio application stops presenting data. This is expected; only Dolby ED2 metadata is supported.

- **D.** Select **Save** and close the menu.

## **Configure ST 2110**

This section is relevant to the 200 and 300 versions of the MPS, MPD, and MPP.

**Note:** If you are not using ST 2110, go to _Configure ST 2022-6_ .

For remote configuration via NMOS, go to _Configure Inputs with NMOS_ .

**1.** Select the **Settings** icon ( ).

**2.** Select **Inputs** and then select an input from the list.

**3.** Select **IP** and then select **ST 2110** .

**4.** Set **Seamless Switching** to **Enabled** or **Disabled** as needed.

**Note:** For Seamless Switching, the two Path 1 and Path 2 streams should be identical. If the streams are not identical, error messages are shown in the status bar. There is a difference between “port” and “path.” The port is the physical SFP port that is used to input the 10GE signal. Path 1 and Path 2 are the signal paths to be used for seamless switching.

With Seamless Switching, a reconstructed output stream is created from the two input

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 109** Configure and Select Virtual Inputs

streams. The reconstructed stream is used downstream for various display tiles like Picture. The buffer size to absorb the packet reception time difference between Path1 and Path2 is 10 ms. The output stream reconstruction does not work properly for streams on Path1 and Path 2 with skew greater than 10 ms. This error makes Picture tiles show the wrong image.

## **Configure Video (ST 2110-20/22) Stream**

**Note:** Incoming 10-bit ST 2110-20 data is supported in the range 4-1019. Incoming data below the minimum is reduced to 4 and data above the maximum is reduced to 1019.

Decoding ST 2110-22 requires the MPSDP-JPXS license.

**1.** Under **ST2110** , select the **Video** tab.

**2.** Set **Enable Video** to **Enabled** .

**3.** In the Video Transport section, select the video transport protocol: **ST2110-20** or **ST2110-22** .

**4.** For each video stream, enter the information in **SFP Port** , **Source Addr.** , **Source Port** , **Destination Addr.** , and **Destination Port** .

- If any fields are inaccessible (gray), set **Masked-Unmasked** to **Unmasked** .

**5.** Set **Ignore RTP Sequence Errors** to **On** if needed. This setting causes the instrument to ignore errors caused by out-of-order RTP packets; no events are generated. This is useful if incoming RTP packets are deliberately out of sequence.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **110 Configure the Instrument** Configure and Select Virtual Inputs

**6.** In the **RTP Payload Type box** , type a number between 96 and 127.

**7.** In the **Packet Read Schedule (PRS)** section, select **Gapped** , **Narrow Linear** , or **Wide Linear** to correctly measure the CMAX and VRX buffer measurements in the IP graphs.

**Note:** You can use the PIT Histogram to determine whether the signal is a gapped, narrow-linear, or wide-linear stream.

**8.** The **TR Offset** defines the timing reference offset of the sender for network delays. Select **Auto** to provide an offset based on the current video standard.

**9.** Select **Gamma Curve** and choose one of the following settings; the selection characterizes the video signal on each virtual input.

- **Auto:** The system selects the setting based on ST 352 VPID. If 352 VPID is not present, SDR Narrow is selected.

- **SDR Narrow:** The reference OETF (Optical to Electrical Transfer Function) is defined in ITU-R BT.709 with gamma of 0.45 and the reference EOTF (Electrical to Optical Transfer Function) is defined in ITU-R BT.1886 with gamma of 2.4.

The Narrow scaling places the extremes of the nonlinear color value from zero to unity at code words 40 hex (64 dec) and 3AC hex (940 dec) in a 10-bit representation for 0% Black to 100% White. This range is typical for standarddynamic range.

- **SDR Full:** The reference OETF is defined in ITU-R BT.709 with gamma of 0.45 and the reference EOTF is defined in ITU-R BT.1886 with gamma of 2.4.

The full scaling places the extremes of the nonlinear color value from zero to unity at code words 0d and 1023d in 10-bit representation and 0d and 4095d in 12-bit representation for 0% black and 100% white, respectively.

- **PQ Narrow:** The reference OETF with a high luminance range capability of 0 to 10,000 cd/m[2] standardized in ST 2084. The EOTF is the inverse of OETF.

The narrow Scaling places the extremes of the nonlinear color value from zero to unity at code words 40 hex (64 dec) and 3AC hex (940 dec) in a 10-bit representation for 0% Black to 100% White. This range is typical for standarddynamic range.

- **PQ Full:** The reference OETF with a high luminance range capability of 0 to 10,000 cd/m[2] standardized in ST 2084. The EOTF is the inverse of OETF.

The Full scaling places the extremes of the nonlinear color value from zero to unity at code words 0d and 1023d in 10-bit representation and 0d and 4095d in 12-bit representation for 0% black and 100% white, respectively.

- **HLG:** The reference OETF is standardized in ARIB B67 and the reference EOTF is standardized in ITU BT.2100 at the nominal display peak luminance of 1000 nits.

- **S-Log2:** The reference OETF is defined as Sony S-Log2.

- **S-Log3:** The reference OETF is defined as Sony S-Log3.

- **S-Log3 (Live HDR):** The reference OOTF is defined as Sony S-Log3.

- **Log C:** The reference OETF is defined as ARRI Log C.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 111** Configure and Select Virtual Inputs

**10.** In the **Color Gamut** list, select one of the following; the selection is the color space of the video signal.

- **Auto:** The system selects the setting based on ST 352 VPID. If 352 VPID is not present, Rec. 709 is selected.

- **Rec. 709:** Standard for HD.

- **Rec. 2020:** Standard for 4K.

**Note:** NMOS/SDP files coerce these parameters from Auto mode.

Rec. 709 gamut is selected automatically when the SD format is detected or selected in the video signal.

When the color gamut is not in Auto mode, the status bar indicates the format in yellow.

**11.** From the **Favorite 3D LUTs** list, select a 3D LUT.

To save a 3D LUT as a favorite, select the Information icon ( ) and select the star beside a LUT. 3D LUTs marked as favorites will be selectable in the Settings Input menu.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **112 Configure the Instrument** | Configure and Select Virtual Inputs

**12.** If needed, set **Format Detection** to **Manual** .

**Note:** Manual Format Detection is required for ST 2110 Fast Switching and MULTI Input when IP sources are used. See _Configure ST 2110 Fast Switching_ .

**13.** In the **Resolution** box, set the resolution.

**14.** In the **Frame Rate** box, set the frame rate.

**15.** If the **Structure** list is not grayed out, select it to change to **RGB 4:4:4 12bit** as needed.

**Note:** Only some resolutions and frame rates allow the Structure to be RGB 4:4:4 12bit.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 113** Configure and Select Virtual Inputs

**16.** Select **Save** .

## **Configure Audio (ST 2110-30 / 31) Stream**

**Note:** To decode an Audio (ST 2110-30 /31) stream, Video (ST 2110-20) must be available and licensed.

An audio stream can only be assigned once to a virtual input's audio stream configuration, for example, Stream 1, Stream 2, etc.

**1.** Under **ST2110** , select the **Audio** tab.

**2.** Select anywhere in the **Stream** row to configure (1-8). You can configure up to 16 audio channels for each ST 2110-30/31 stream. A total of 16 audio channels can be monitored across all streams.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **114 Configure the Instrument** Configure and Select Virtual Inputs

**3.** Set **Enable Audio Stream** to **Enabled** . This subscribes the audio stream from the media switch.

**4.** Set **Map Stream** to **Enabled.** This makes the audio stream appear in the Audio applications.

**5.** In the **Audio Transport** section, select the audio transport protocol: **ST2110-30** or **ST2110-31** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 115** Configure and Select Virtual Inputs

**Note:** Both ST 2110-30 and ST 2110-31 can carry PCM or Dolby D, D Plus, or Dolby E. However, if ST 2110-30 will carry Dolby content, the data must be transmitted in pairs and set to start on odd channels such as 1-2 or 3-4.

Only a single stream can be set for ST 2110-31; one to four streams can be ST 2110-30, up to a total of eight audio streams, with up to 16 audio channels total.

An identical stream should not be configured and enabled within the audio input configuration; only one of the identical streams will be decoded at a time.

**6.** In the **SFP Port list** , select a number.

**Note:** The SFP (physical) Port configuration is common for Video, Audio, and Data.

## **7.** In the **Destination Addr.** box, enter the address.

**Note:** If the IP stream is uniquely specified, Source Addr., Source Port, and Destination Port are optional.

**8.** In the **RTP Payload Type** box, type a number between 96 and 127.

**Note:** The RTP Payload Type is displayed in the IP Status application.

**9.** In the **Num of Channels** box, type the number of channels in the audio stream. The number must be an even number between 2 and 16 (such as 2, 4, 6, etc.). Up to 16 audio channels, across all audio streams, are supported.

**10.** In the **Packet Timing** section, select an option as needed; Auto is recommended.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **116 Configure the Instrument** Configure and Select Virtual Inputs

**Note:** If an audio program uses multiple streams, all streams must have the same packet timing.

The Bit Depth is already set to 24.

## **11.** Select **Save Stream** .

**Note:** In some cases, when an audio stream is added to the instrument, the audio bars might include the message “STREAM CONFIG ERR.” If this occurs, check the IP session available in IP MEAS and select the Audio tab for information about the number of channels detected and packet timing. Make sure these values are configured correctly for the virtual input in order to decode the audio stream.

**12.** Repeat Steps 1 through 11 for each stream to configure. You can configure up to eight audio streams as required, maintaining a total of 16 audio channels.

**13.** Under **Audio** , configure one type of audio: See _Configure PCM_ , _Configure DOLBY_ , or _Configure DOLBY ED2_ (use of Dolby requires the MPSDP-DLBY license).

## **Configure PCM**

- **A.** Under **AUDIO** , select **PCM** .

- **B.** Select **Program Configuration** .

- **C.** Set **Program Configuration** to **On** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 117** Configure and Select Virtual Inputs

- **D.** Select **Edit** . The Edit button is replaced by the Default, Clear, and Undo buttons.

- **E.** Select the type of program (mono, stereo, etc.) and select the audio channel to assign it. Repeat until all the audio in the current input signal have programs assigned to channels.
  - ♦ **M** is mono, one channel.

  - ♦ **ST** is stereo, two channels.

  - ♦ **5.1** is surround sound, six channels.

To change the channel order in the audio bars, see _5.1 Channel Order_ .

- ♦ **7.1** is surround sound, eight channels.

- ♦ **5.1.4** is immersive audio and requires 10 channels: six for the audio main bed, or level–marked in cyan, and four for the audio upper bed, marked in orange.

**Note:** 5.1.4 provides bar labels for the audio channels, but is not available for downmix capability or for loudness display.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **118 Configure the Instrument** Configure and Select Virtual Inputs

- ♦ **7.1.4** is immersive audio and requires 12 channels: eight for the audio main bed, or level–marked in cyan, and four for the audio upper bed, marked in orange.

**Note:** 7.1.4 provides bar labels for the audio channels but is not available for downmix capability or for loudness display.

- ♦ **Unassigned** removes an assignment from a channel. Select **Unassigned** and click any block in an assignment, for example the middle of a 7.1 assignment, the entire assignment is removed and is not displayed on the Audio application.

- ♦ **Default** resets the channels to eight stereo pairs.

- ♦ **Clear** removes all assignments, including the default.

- **F.** Select **Save** and close the menu.

**Note:** You must save the program configuration to update the programs in the audio bars and loudness meter.

- **G.** If you need to continue configuring the instrument, see _Configure Data (ST 211040/43) Stream_ .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 119** Configure and Select Virtual Inputs

## **Configure DOLBY**

**Note:** Dolby selection works with Dolby D, D Plus, or E signals.

To use Dolby in ST 2110, you must configure the Audio Transport, in the audio stream, as ST 2110-31.

## **A.** Under **AUDIO** , select **DOLBY** .

- **B.** In the **Dolby Audio Channel Pair** menu, select the audio channel pair that contains Dolby audio.

- **C.** If needed, identify Dolby Audio Channels, or go to Step D:
  - **a.** Open the Audio application.

  - **b.** Return to the **Inputs** menu and select **PCM** .

  - **c.** In the Audio application, in the audio levels, find and note the audio channels marked with DOLBY D or DOLBY E.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **120 Configure the Instrument** Configure and Select Virtual Inputs

- **d.** In the **Inputs** menu, select **DOLBY** .

- **e.** From the **Dolby Audio Ch Pair** list, select the channel pair that is marked as DOLBY in the Audio application. The audio bar layout is configured automatically based on the metadata in the Dolby stream.

- **D.** Select **Save** and close the menu.

**Note:** Audio programs configured in the Program Configuration menu are used to select a program for measurement by the Loudness application, to display audio bars in the Audio application, and to monitor with headphones. When all the channels are unassigned, all the channels are treated as stereo pairs. The audio programs in the Dolby E stream are automatically set up based on the Dolby E metadata.

The number of audio streams and channels determines the content and order of audio channels embedded in the AUX OUT.

If the number of audio channels present does not complete a group (four channels), the remaining channels in the group will be labeled “Z BIT.”

If the audio bars are flashing in the audio display, or sounds are garbled or the wrong pitch, the audio input configuration might not be set up correctly. Check the IP address, port, and payload type from the IP session display and make sure to select the correct number of audio channels. A guideline for the number of audio channels (assuming 24-bit, 48kHz audio) is approximately 1 to 1.5 Mbps per channel. See the IP Status BITRATE column.

To receive only audio, disable the video stream.

An audio stream can only be assigned once to a virtual input's audio stream configuration, for example, Data 1, Data 2, etc.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 121** Configure and Select Virtual Inputs

- **E.** If you need to continue configuring the instrument, see _Configure Data (ST 211040/43) Stream_ .

## **Configure DOLBY ED2**

**A.** Under **AUDIO** , select **DOLBY ED2** .

- **B.** From the **Dolby ED2 Audio Ch Pairs** list, select the consecutive channel pairs that contain Dolby ED2 audio.

- **C.** If needed, identify Dolby ED2 Audio Channels, or go to Step D:
  - **a.** In the **Inputs** menu, select **PCM** (instead of DOLBY ED2).

  - **b.** Open the Audio application.

  - **c.** In the Audio application, in the audio levels, find and note the audio channels marked with “DOLBY ED2.”

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **122 Configure the Instrument** Configure and Select Virtual Inputs

- **d.** In the **Inputs** menu, select **DOLBY ED2** (instead of PCM).

- **e.** From the **Dolby ED2 Audio Ch Pairs** list, select the channel pairs that are marked as DOLBY in the Audio application. Dolby ED2 metadata in the selected channels is decoded.

**Note:** When you select Dolby ED2 in the Inputs menu, the Audio application stops presenting data. This is expected; only Dolby ED2 metadata is supported.

- **D.** Select **Save** and close the menu.

- **E.** If you need to continue configuring the instrument, go to the next section.

## **Configure Data (ST 2110-40/43) Stream**

**1.** Select the **Data** tab.

**2.** Select anywhere in the Stream row to configure (1-4).

**3.** Set **Enable Data** to **Enabled** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 123** Configure and Select Virtual Inputs

**4.** Select the **Data Transport** type: **ST2110-40** or **ST2110-43** .

**Note:** ST 2110-43 is the TTML Subtitles transport.

**5.** For each data stream, enter the information in the **SFP Port** , **Source Addr.** , **Source Port** , **Destination Addr** ., and **Destination Port** boxes.

**6.** In the **RTP Payload Type** box, type a number between 96 and 127.

**Note:** The RTP Payload Type number must be unique for each IP stream. The RTP Payload Type is displayed in the IP Status application.

Keep Alive packets are required to keep TTML decoding synchronized with the rest of the ST 2110 stream.

**7.** Select **Save** and close the menu.

## **Configure RTP**

Monitoring general-purpose RTP streams allows you to see physical and IP layer measurements, but none of the video, audio, and data payload is decoded and displayed.

To monitor general-purpose RTP streams:

**1.** Select the **Settings** icon ( ).

**2.** Select **Inputs** and select the input from the list.

**3.** Select **IP** and then select **RTP** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **124 Configure the Instrument** Configure and Select Virtual Inputs

**4.** In the **SFP Port** box, specify the port being monitored.

**5.** Enter the **Source** and **Destination** information.

**6.** In the **RTP Payload Type** box, type a number between 0 and 127.

**7.** Select the **Video Format** and corresponding **Frame Rate** .

**8.** Select **Save** and close the menu.

## **Select Input**

PRISM provides the following input modes:

- **Single Input mode:** Select any single input to monitor from an IP or SDI signal.

- **Multi-input mode:** Select multiple SDI or IP (ST 2110-20 or ST 2110-22) inputs to simultaneously monitor up to four virtual inputs. Option MPSDP-MULTI is required.

## **Single Input Mode**

To select a single configured input from an IP or SDI signal:

**Note:** If the MPSDP-MULTI option is not installed, multiple inputs is not available, “Multi:” is not in the Inputs menu, and only single input mode is available.

**1.** Make sure **Single Input** mode is enabled:

- **A.** Select the **Settings** icon ( ) and then select **Input** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 125** Configure and Select Virtual Inputs

## **B.** Set **Multi Mode** to **Off** .

**2.** Select the **Input** icon ( ) from the status bar at the bottom of the PRISM monitor.

**3.** Select a configured input from the list in the Input bar.

**4.** Select the **Home** icon ( ) to close the Input selection controls.

## **Multiple Inputs Mode**

Multi-input mode can simultaneously monitor up to four SDI or IP (ST 2110-20 or ST 2110-22) inputs. When using multi-input mode, there is a primary channel and up to three secondary channels.

## **Primary Channel**

The primary channel is the main input of the four possible inputs. It can be reassigned at any time. The current primary channel is marked in the Multi Input menu and the status bar with a cyan dot.

Alarms, Audio Output, and SDI Aux are supported only for the primary channel.

## **Secondary Channels**

The secondary channels are any selected channel that is not the primary. These are marked in the Multi Input menu and status bar with white dots. These inputs cannot be displayed in primary-only applications but are displayed in all other applications unless otherwise noted. If a secondary channel is assigned to a tile with a primary-only application (or a secondary channel is assigned a primary-only application), the tile displays a message that it cannot display the application on a secondary channel.

## **Selecting Multiple inputs**

**1.** Select the **Input** icon ( ) from the status bar at the bottom of the PRISM monitor.

**2.** Select the multi-input button on the Input bar.

**Note:** If “Multi:” is not on the Input bar and the Multi button is not active, the MPSDPMULTI option might not be installed.

## **3.** Set **Multi Input** to **ON** .

## **4.** Set **Edit Mode** to **ON** .

When Edit mode is OFF:

- No individual input menus appear when you select an input button.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **126 Configure the Instrument** Configure and Select Virtual Inputs

- Selecting an input applies the selected input without confirmation.

- Selecting an input changes that input to the primary channel.

- The options in the multi-input menu are not available (the inputs in the tiles and the selected channels cannot be changed).

**5.** Assign inputs to one of four channels:

**Note:** If you do not select any channels, the first virtual input (the left channel on the Input menu) is set as the primary and is displayed on all tiles.

- **A.** Select an input from the Input bar.

- **B.** In the menu, select **Add Channel** .

In the following example, SDI-In 1 is the primary channel (cyan dot) with number indicated virtual channel and SDI-In 2 is unselected.

The input appears in the list of channels with a white dot and virtual input number.

**Note:** If there are already four inputs selected, an error message appears. Follow the instructions in the message to remove a channel.

- **C.** Repeat Steps A and B until all the needed channels are selected.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 127** Configure and Select Virtual Inputs

## **Change Primary Channel**

One of the inputs must be the primary channel. The primary channel is initially set to the active input from single input mode.

To reassign the primary channel:

**1.** Select one of the secondary channels marked with a white dot (the potential primary channel must be selected as a monitored channel).

**2.** Select **Make Primary** .

The selected secondary input becomes primary and the primary becomes a secondary; the white dot turns cyan and the cyan dot turns white. In the multiinput menu, the titles in the tiles change color and any tiles set to Follow Primary change to the selected input.

Follow Primary means a tile input configuration follows the primary input, no matter what input is selected as the primary. If a secondary input is changed to primary, all tiles set to Follow Primary change to the new primary input.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **128 Configure the Instrument** Configure and Select Virtual Inputs

**Note:** The primary input becomes a secondary input. If a tile that is now using a secondary input has a primary-only application, a message appears notifying you that the application cannot work with a secondary channel.

## **Configure Input Tiles**

To set the Multi Input tiles to display specific inputs:

**1.** In the tile map, select a Tile 1-4, or 1-8 if there is an extended display (eight tiles also requires the option MPSDP-EXTNDSP).

**2.** Click each tile that you want to use for the selected input, and then select the channel for that input to be applied to each tile.

**3.** Select the input to display from the list of selected inputs at the bottom of the Multi menu or select Follow Primary.

The labels in the tiles show the name of the selected input (such as SDI-In 1), it also shows if they are following the primary (the tile label shows “Follow Primary”). If the selected input is the primary channel, the tile information is in cyan.

## **Reset Tile Map**

To reset the Multi Input tile map back to default:

**1.** In the **Multi** menu, select **Reset** . Reset sets all the tiles in the tile map to Follow Primary, it sets channel 1 (the input at the far left of the input menu) as the primary, and it removes all selected inputs from the channels list (no other inputs are selected for monitoring). It leaves the previously selected applications in the tiles, but they are all set to monitor the primary input.

**2.** Select the multi-input menu button.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 129** Configure and Select Virtual Inputs

## **Operation with ST 2110**

Inputs may be configured for ST 2110 either manually or with NMOS (see _Configure ST 2110_ and _Configure Inputs with NMOS_ ).

**Note:** ST 2110 audio and data are only supported on the primary input. Any ST 211030/31 or ST 2110-40/43 streams configured for secondary inputs will not be joined.

For ST 2110-20 or ST 2110-22 streams, the input must be configured for manual format detection.

- For NMOS operation, the format detection is set using the SDP file.

- If the format of the stream is unknown, switch to single input mode and set format detection to Auto. Use the format reported in the status bar to then set the manual format detection for each input.

- When finished, set **Multi Input** to **On** .

The two SFP IP ports support up to 25Gb of IP traffic, depending on the data rate of your network. When monitoring multiple ST 2110 inputs, you must configure inputs so that a stream won’t overflow the port. You may use up to 95% of the available link bandwidth.

From the input settings:

- You may use ST 2022-7 Seamless Switching if desired, although it may limit the number of simultaneous virtual inputs you can use, due to twice the bandwidth required.

- If Seamless Switching is disabled, select which SFP port will be used for each input, 1 or 2.

**Note:** Video/Audio/Data for an input must all use the same SFP port.

The IP Status application displays the virtual input channel each stream is mapped to.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **130 Configure the Instrument** Configure and Select Virtual Inputs

## **Adjust Source Label**

The input information (label) in the tile contains the name of the input it is set to monitor (like SDI-In 2), if the tile is following the primary, the signal transport, and the frame rate of the input.

To open the Source Label controls, select the **Settings** icon ( ), and then select **Display** .

- To move the Source Labels, open the **Source Label Position** menu and select the location for the label from the options. You can also select and drag the label to one of four locations (bottom-left or right, top-left or right).

- To set the Source Label timeout, open the **Source Label Timeout** menu, and select when and how the label should appear.

- To show hidden labels or brighten dimmed, select the **Home** icon (

- ).

The trace applications will function but might have reduced trace quality if the primary input is missing or if any secondary input frame rates are incompatible with the primary input (for example, an input of 1080i/59 is incompatible with an input of 1080i/50).

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 131** Configure and Select Virtual Inputs

## **Multi-Input Applications**

There are some limitations when using applications with multiple inputs. Because multiple inputs work only with SDI inputs, the IP input applications are not applicable. Several applications work only with the chosen primary channel.

Primary-only applications:

- Video Session

- Audio

- Dolby Status

- AES Channel Status

- IP Session

- IP Graphs

- PIT Histogram

- Stream Timing

- ANC Session

- Datalist

- Timing

- AV Delay

**Note:** These primary-only applications are marked with a cyan dot when Multi Input mode is on. The applications are marked in the application bar and the All Applications menu.

IP applications that are not tied to IP Inputs are functional in Multi Input mode:

- IP Status

- IP Session (Layer 1/2 and PTP tabs)

- PTP Graphs

**Note:** These Picture application functions are available only to the primary channel: Convert to Rec. 709, Source ID Overlay, Closed Caption, HDR Measurements, and Lightmeter.

## **Configure ST 2110 Fast Switching**

This procedure sets up the instrument for ST 2110 fast switching between inputs. This mode enables a make-before-break setting for ST 2110 signals. The system subscribes to the second video stream, switches at the marker bit, and then unsubscribes from the first stream.

Twice the bandwidth is required to handle two IP streams during input transitions. If there is insufficient bandwidth for the make-before-break operation, the system will

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **132 Configure the Instrument** Configure and Select Virtual Inputs

drop packets during the transition. In this situation, you might want to disable this feature. This condition will likely occur for 4K/50p signals on a 10G network or if there are other signals on the link that would reduce the bandwidth to be insufficient for make-before-break operation.

The benefits of fast switching are as follows:

- Switching ST 2110 inputs is much faster.

- Switching between inputs displays complete frames on the picture application.

- It reduces switching errors in the Event Log and IP Graphs.

- SDI Aux out switches between the two sources with no CRC errors.

- SDI Aux out seamlessly switches between the two sources.

The following are the prerequisites for ST 2110 fast switching:

- Signals to fast switch must be the same exact resolution, frame rate, and structure or fast switching is not possible.

- Set the virtual inputs being fast switched to the Resolution and Frame Rate of the signals, or for NMOS applications the format specified in the SDP file.

**Note:** If the Resolution and Frame Rate of the input does not match the signal, the Picture could produce false images to the point of being unusable.

2110 Fast Switching is not supported in Multi Input mode.

- ST 2110-20 video inputs must be locked to PTP and well-timed.
  - PRISM tolerates a maximum skew between the streams up to 500 microseconds, with the skew taking into account jitter and delay.

  - If the AUX OUTPUT Loop-through is enabled, the aux output jitter specification must be met for each stream.

- For best switching time performance:
  - Streams should have the same Packing Mode: Block or General.

  - Streams should have the same Packet Read Schedule (PRS): Gapped or Linear.

  - Streams should be ST 2110-21-compliant.

When a PRISM receives a new stream that does not meet the prerequisites, fast switching might not be possible.

## **Configure ST 2110 Fast Switching Through NMOS**

Activate the video receiver with an SDP file containing the appropriate format information. The format information for video is defined in the _a=fmtp_ line.

## **Required Media Type Parameters**

Include the payload-format-specific Media Type parameters in the _a=fmtp_ clause of the SDP for all streams conforming to this standard. This sample is a part of an SDP file.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 133** Configure and Select Virtual Inputs

v=0

o=- 123456 2 IN IP4 0.0.0.0

s=Sample video SDP file (SMPTE ST 2110-20 with SMPTE ST 2022-7) i=1080p@50 Hz video streams

t=0 0

a=group:DUP first second

a=recvonlym=video 20000 RTP/AVP 96

i=First video stream description c=IN IP4 239.20.10.113/8 a=rtpmap:96 raw/90000 a=mid:first _a=fmtp_ :96 sampling=YCbCr-4:2:2; width=3840; height=2160; exactframerate=60000/1001; depth=10; TCS=SDR; LJ \_ colorimetry=BT2020; PM=2110GPM; TP=2110TPN; SSN=ST2110-20:2017;

a=ts-refclk:localmac=98-03-9B-A0-88-83

a=mediaclk:direct=0

m=video 20000 RTP/AVP 96

i=Second video stream description c=IN IP4 239.20.20.113/8 a=rtpmap:96 raw/90000 a=mid:second _a=fmtp_ :96 sampling=YCbCr-4:2:2; width=3840; height=2160; exactframerate=60000/1001; depth=10; TCS=SDR; a LJ colorimetry=BT2020; PM=2110GPM; TP=2110TPN; SSN=ST2110-20:2017; [te ~~a~~ a=ts-refclk:localmac=98-03-9B-A0-88-82 a=mediaclk:direct=0

- **sampling:** indicates the structure of video signal. Possible values are YCbCr-4:2:2 and RGB-4:4:4.

- **depth:** indicates the number of bits per sample. Possible values are 10 or 12.

- **width:** the number of pixels per row. Permitted values are integers between 1 and 32767 inclusive. PRISM supports 720, 1280, 1920, and 3840.

- **height:** the number of full-bandwidth sample rows per frame. Permitted values are integers between 1 and 32767 inclusive. PRISM supports 486, 576, 720, 1080, and 2160.

- **exactframerate:** the frame rate in frames per second. Integer frame rates are written as a single decimal number (for example 25). Non-integer frame rates are written as a ratio of two integer decimal numbers separated by a forward-slash (for example 30000/1001) using the numerically smallest numerator value possible. PRISM supports 24000/1001, 24, 25, 30000/1001, 30, 50, 60000/1001 and 60.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **134 Configure the Instrument** Configure and Select Virtual Inputs

- **colorimetry:** the system colorimetry used by the image samples. Supported values are BT709, BT2020, and UNSPECIFIED. UNSPECIFIED means the PRISM uses whatever value was manually set (see the Color Gamut menu).

## **Media Type Parameters with Default Values**

Senders can include the format-specific Media Type parameters in the _a=fmtp_ clause of the SDP for all streams using this standard.

- **interlace:** If this parameter name is present, it means the video is interlaced, or the video is Progressive segmented Frame (PsF). If this parameter name is not present, the progressive video format is used.

- **segmented:** If this parameter name is present, and the interlace parameter name is also present, then the video is a Progressive segmented Frame (PsF). Using this parameter without the interlace parameter is not possible.

- **TCS:** Transfer Characteristic System; this parameter specifies the transfer characteristic system of the image samples (in the Gamma Curve menu in the settings for an input). The supported values are SDR, PQ, HLG, and UNSPECIFIED. If the TCS value is unspecified, receivers use the value SDR. UNSPECIFIED means the PRISM uses whatever value was manually set (see the Gamma Curve menu).

These attributes determine the PRISM settings. These all correspond to one of the format menus:

- The TCS attribute sets the Gamma Curve.

**Note:** For SDR and HLG, these are always narrow for ST 2110.

- The colorimetry attribute sets the Color Gamut.

- The width and height attributes set the Resolution.

- The exactframerate attribute—and the presence or absence of the interlace and segmented attributes—set the Frame Rate.

## **Configure ST 2110 Fast Switching Through UI**

**1.** Select the **Settings** icon ( ) and then select **Inputs** .

**2.** Set **ST 2110 Fast Switching** to **On** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 135** Configure and Select Virtual Inputs

**3.** Set up the first IP input. See _Configure ST 2110_ for details.

**4.** In the **Inputs** menu, set **Format Detection** to **Manual** .

**Note:** Setting Format Detection to Auto is not effective for fast switch; the setting must be made manually.

**5.** Set the **Resolution** , **Frame Rate** , and **Structure** (if the option is available) to the same settings as the signal. See _Configure ST 2110 Fast Switching_ for the requirements to set up inputs for fast switching.

**Note:** If the Resolution and Frame Rate (and any Structure) of the input does not match the actual signal, the Picture could produce false images to the point of being unusable.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **136 Configure the Instrument** Configure and Select Virtual Inputs

- **A.** Find the resolution and frame rate of the incoming signal; set **Format Detection** to **Auto** and select **Save** .

- **B.** Open the Video Session application. The resolution, frame rate, and structure are listed near the top of the tile.

- **C.** In the **Inputs** menu, set **Format Detection** to **Manual** .

- **D.** Set the **Resolution** and **Frame Rate** , and **Structure** if needed, to the measurements from the Video Session application and select **Save** .

When the selected virtual input has been manually set, the details are listed in the status bar in yellow.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 137** Configure and Select Virtual Inputs

**6.** Set up the second input the same as the first.

**7.** Switch between the configured IP inputs.

**Note:** If you are switching to a third input, you might need to allow for the first stream to leave, or link saturation might occur.

## **Configure SDI Vu**

When SDI Vu is enabled, it is available in the Video Session display as an additional tab. This display provides Video Format, Y/C CRC checks, Video Frequency Offset, Audio Content, and ANC Parity monitoring. On the SDI Vu tab, you can monitor and log error events for all four physical SDI inputs (SDI 1–4) simultaneously, regardless of whether they are selected as active inputs. You can monitor the inputs in single or multi-input mode.

To enable SDI Vu:

**1.** Select the **Settings** icon ( ) and then select **Inputs** .

**2.** Set **SDI Vu to On** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **138 Configure the Instrument** Configure Instrument for HDR/WCG Monitoring

## **Configure Instrument for HDR/WCG Monitoring**

PRISM provides HDR/WCG monitoring features that aid in the setup and balance of cameras in HDR/WCG during content creation. Before using these features, configure the virtual input (see _Configure and Select Virtual Inputs_ ). Use the Gamma and Color Gamut menus to adjust the PRISM monitor settings to reflect the input signal properties if they are not automatically selected.

These applications and features are used to configure the instrument for HDR/WCG monitoring.

## **Transfer Function/Color Space Conversion**

**Note:** This tool is available only with Option MPSDP-PROD.

If it is enabled, the Transfer function/color space conversion function uses the Favorite 3D LUT, such as Convert to Rec. 709 or user-installed LUTs. The Picture, Waveform, Vector, Lightning, Diamond, and Stop applications apply the Favorite LUT configured by the user. The SDI Aux Out can also apply the Favorite LUT for a given input to the output signal. For details, see _Using 3D Lookup Tables_ .

Select the **Convert to Rec. 709** feature to convert the Gamma / Gamut settings for the signal to the BT. 709 Gamma / Gamut signal. This feature allows you to match the skin tone and the color in BT. 709 Gamma / Gamut displays. The conversion between input video and linear light is processed in Scene light.

**Note:** Convert to Rec. 709 mode is not supported for SD signals.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 139** Configure Instrument for HDR/WCG Monitoring

## **Using 3D Lookup Tables**

**Note:** This tool is available only with Option MPSDP-PROD.

PRISM 3D Lookup Table (LUT) support enables content producers to view content before and after 3D LUT processing without an external 3D LUT converter box. The content can be viewed with trace applications such as Waveform and Vector or on an external picture monitor connected to the SDI Aux Output.

A lookup table is a method to convert the original image to a different image based on the artistic look required for the content, for instance converting a daylight shot to a nighttime scene. The conversion process is based on a mathematical matrix that converts the image data to a new look. In PRISM, this process is based on 3D 33x33x33 matrices in .cube format. These LUTs provide color space and gamma conversion from one format to another, such as from HLG to SDR.

The favorite 3D LUT is selected on an input-by-input basis. Each virtual input can have a different favorite 3D LUT.

You can select the Telestream preinstalled “Convert to Rec. 709” LUTs or install custom Type 1 33x33x33 .cube format LUTS.

To manage 3D LUTs, in the PRISM web interface, select **Manage 3D LUTs** . The Manage 3D LUTs screen lists the 3D LUTs that have been uploaded.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **140 Configure the Instrument** Configure Instrument for HDR/WCG Monitoring

To filter the list, type some or all of a LUT name in the **Search LUTs** box.

To sort the list, click the column heading you want to sort by. In the following example, the list will be sorted by group.

Favorite 3D LUTs are available for selection in the input configuration menu. A LUT can be made a “favorite” by tagging it with a star in the PRISM web interface via the **Manage 3D LUTs** option or via **Settings > Utilities > Manage 3D LUTs** . For quick favorites while editing an input, you can also select the “i” symbol and back arrow. Once a LUT has been configured as a favorite, it is available in the input list for processing.

To save a 3D LUT as a favorite, select the star beside the LUT. Blue Star LUTs are factoryinstalled LUTS and cannot be deleted, although they can be downloaded. They are selected based on Input gamma and gamut for the “Convert to Rec. 709” function.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 141** Configure Instrument for HDR/WCG Monitoring

## **Uploading LUTs**

While multiple LUTs can be loaded to the instrument, a set of Favorite 3D LUTs can be accessed from the dropdown list in the input configuration. You can upload 3D LUT (.cube) files from your computer to PRISM. Uploaded files must be 33x33x33 and .cube format that conforms to the Adobe Cube standard. These LUTs can be obtained from NBCU or BBC, or created from editing and color-correction applications (such as Resolve, Adobe Premiere Pro, Final Cut, and LUTCalc). The LUT dimensions are 33 x 33 x 33 and are RGB in and out. The coefficients are floating point values from 0.0 to 1.0.

You can download NBCU LUTs from GitHub:

https://github.com/digitaltvguy/NBCUniversal-UHD-HDR-SDR-Single-MasterProduction-Workflow-Recommendation-LUTs

To upload a new 3D LUT:

**1.** Click the **Upload** icon ( ).

**2.** (Optional) From the **Input Gamma** list, select the input gamma: **Any** , **SDR Narrow SDR Full** , **PQ Narrow** , **PQ Full** , **HLG** , **S-Log2** , **S-LOG3** , **S-Log3** , **S-Log3 (Live HDR)** , or **Log C** .

**3.** (Optional) From the **Output Gamma** list, select the output gamma: **Any** , **SDR Narrow** , **SDR Full** , **PQ Narrow** , **PQ Full** , **HLG** , **S-Log2** , **S-LOG3** , **S-Log3** , **S-Log3 (Live HDR)** , or **Log C** . This ensures that the appropriate graticules are displayed.

**4.** (Optional) From the **Input Gamut** list, select the input gamut: **Any** , **Rec. 709** , or **Rec. 2020** . We recommend filling in the optional information about LUT specifics so users have additional information about how the LUT should be used.

**5.** (Optional) From the **Output Gamut** list, select the output gamut: **Any** , **Rec. 709** , or **Rec. 2020** . This ensures that the correct color space conversion coefficients and VPID values are used and that appropriate application graticules are displayed.

**6.** (Optional) To save the LUT as a favorite select the star icon. 3D LUTs marked as favorites will be selectable in the Settings Input menu.

**7.** (Optional) In the **Optional LUT Name** box, type a name for the LUT. This does not change the file name.

**8.** (Optional) To add the LUT to a group, type the group name in the **Group** box.

**9.** (Optional) Type a description in the **Description** box. If you leave this box blank, the description will be populated automatically from the TITLE field in the LUT file.

**10.** Click **Browse** . Navigate to the 3D LUT file and select it.

**11.** Click **Upload** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **142 Configure the Instrument** Using NMOS

## **Downloading LUTs**

To download a LUT:

**1.** Click the **Download** icon ( ).

**2.** Save the file locally.

## **Editing LUTs**

To edit a previously installed LUT:

**1.** Click the **Edit** icon ( ).

**2.** Edit the LUT metadata as necessary and click the **Save** icon ( ).

## **Deleting LUTs**

To delete a LUT, click the Delete icon ( ). **Note:** The LUT is deleted immediately; there is no confirmation dialog box.

## **Using NMOS**

NMOS (Networked Media Open Specifications) allows system integrators to build an IP system with PRISM being managed by system management software. The software discovers, registers, and configures inputs for monitoring. The NMOS implementation is

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 143** Using NMOS

compatible with IS-04 discovery and registration, and IS-05 device connection management.

You can choose DNS or Static (manual) IP addresses when configuring the NMOS Registration Server. Static IP addressing ensures consistent connectivity, improved network security for implementation of access control lists, firewall rules, and establishing Quality of Service (QoS) rules.

## **Enable NMOS Discovery & Registration**

To enable NMOS on the instrument:

**1.** Select the **Settings** icon ( ).

**2.** Select **Network** .

**3.** Select **NMOS** .

**4.** Set **Enable NMOS Discovery & Registration** to **Enabled** .

**5.** Set **NMOS Discovery Version** to **Version 1.2** or **Version 1.3** , according to the system management software.

**6.** Select the **NMOS Registration Method: DNS** or **Static** .

**7.** If you chose DNS in Step 6:

- **A.** Set the **NMOS Registration Method** to **DNS** .

- **B.** Set the desired static **NMOS Registry Address** and **Port** .

- **C.** Set **NMOS DNS** to **Auto** , **Multicast** , or **Unicast** as needed.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **144 Configure the Instrument** | Using NMOS

**Note:** PRISM checks for DNS registry announcements to find an NMOS registry. If there are multiple registries, PRISM attempts to register with the NMOS registry that has the highest priority (0 is highest). If NMOS DNS is set to Auto, all Multicast and Unicast registry announcements are considered. Selecting Multicast or Unicast shows only that type of registry announcement.

**8.** If you chose Static in Step 6:

## **A.** Set the **NMOS Registration Method** to **Static** .

**B.** Set the desired static **NMOS Registry Address** and **Port** .

You can view the Static NMOS Registry status on the IP Session NMOS tab. If PRISM is successfully registered, the LED will be green.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 145** Using NMOS

**Note:** The Advertised Port is the physical port on the back of the instrument. The Control selection is for the RJ-45 10/100/1000Mbps Ethernet port.

If you change the control port IP address or the label of the instrument and you use NMOS for configuration, we recommend rebooting the instrument to update the NMOS registration server.

## **Reset NMOS**

To clear the NMOS configurations on the instrument, select **Reset** and then select **Ok** . A loading icon appears as the configuration is loaded.

**Note:** Using RESET deletes the internal NMOS presets folder, removes any previous history of connections, and sets the NMOS configuration back to default values.

## **Configure Inputs with NMOS**

Enabling NMOS creates and registers up to six different devices. Each of these devices correlates to a PRISM virtual input.

The PRISM input associated with the device can be found in the device “label” and “instance-id” tag.

Each device contains the following NMOS receivers:

- 1 video receiver

- 8 audio receivers

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **146 Configure the Instrument** Using NMOS

- 4 ancillary data receivers

Each receiver indicates the PRISM input and stream number it configures in the “label”, “description”, and “grouphint”.

Performing an NMOS activation on a receiver configures the stream(s) for the corresponding virtual input and media type. For instance, activating the above receiver will configure the Path 1 and 2 for Audio Stream 1 on the third input.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 147** Using NMOS

**Note:** NMOS activations will automatically set the corresponding input to IP, ST 2110, and rename to “NMOS Input <device number>”.

An NMOS activation will configure an input regardless of whether it is selected. An activation _will not_ set the current/primary input.

To switch the current/primary input, use the _**activeInput**_ PRISM API command.

## **Support for Existing Drivers**

For custom NMOS drivers that expect PRISM to advertise a set number of devices and receivers, you can use the following PRISM APIs:

- **nmos_single_device_mode:** When this mode is enabled, PRISM only advertises a single NMOS device containing video, audio, and data receivers. Any receiver activations will configure the specified target input. When disabled, PRISM advertises six devices: one for each virtual input.

- **nmos_target_input:** Sets the target input for NMOS activations in single device mode. In this mode, any NMOS receiver activations will configure the specified input.

- **nmos_audio_receivers_count:** Sets the number of audio receivers each device advertises.

- **nmos_anc_receivers_count:** Sets the number of ancillary data receivers each device advertises.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **148 Configure the Instrument** Adjust Audio Settings

## **Configure IP Generator with NMOS**

When NMOS is enabled alongside the IP generator, a device is created and registered. This device corresponds to the current generator mode that is enabled.

The device contains two senders that, when activated, configure:

- the destination IP

- the destination port

- the enable for the stream.

For more information about NMOS and the IP generator, see _IP Display NMOS Operation_ and _Test Signal NMOS Operation_ .

## **Adjust Audio Settings**

The Audio settings menu has several tools that relate to aspects of the Audio application, the audio signal, and aural output. Details of several of these can be found in other parts of the document where they are specifically relevant.

**1.** Select the **Settings** icon ( ).

**2.** Select **Audio** .

**3.** See the following sections for details about configuring these features:

- Loudness Settings: See _Loudness Display_ .

- Bar Ballistics: See _Ballistics_ .

- 5.1 Channel Order: See _5.1 Channel Order_ .

- Set Downmix Mode: See _Downmix Controls_ .

**4.** In the **Dolby DRC Mode** section, select **Off** , **Line** , or **RF** . Line and RF are modes of Dynamic Range Control (DRC)—compression—factors that are applied when decoding Dolby content for monitoring or output.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 149** Adjust Audio Settings

**5.** Select the **Downmix Dynamic Rng.: Line** or **RF** . These DRC compression factors are applied when downmixing to the various Dolby D listening modes.

## **Peak Program Level (dBFS)**

This level is marked by the red arrow in the Audio application. Audio above this mark is shown in red. This audio is above the peak level.

To change the Peak Program Level (dBFS) number:

**1.** In the **Audio** settings menu, select the **Peak Program Level (dBFS)** box.

**2.** Enter the number on the keypad or select the up or down arrows.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **150 Configure the Instrument** Adjust Audio Settings

## **Test Level (dBFS)**

The Test level, which is also called the reference or line-up level, is the yellow arrow in the Audio application. Audio above this mark is shown in yellow. This audio is between the test and peak levels.

To change the Test level (dBFS) number:

**1.** In the **Audio Settings** menu, select the **Test Level (dBFS)** box.

**2.** Enter the number on the keypad or select the up or down arrows.

**Note:** You cannot set the Test level above the Peak Program level. If the peak is set to -5, then the test cannot be -4. If the test is set to -4 (through the arrows or the keypad), the peak is set automatically to -4.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 151** Configure Instrument Outputs

## **Configure Instrument Outputs**

You can set the AUX OUT connector to Loop-through or Generator, and turn on the SDI loop-through. The AUX OUT connector always contains an SDI signal.

## **AUX OUTPUT**

**1.** Select the **Settings** icon ( ) and select **Outputs** .

**2.** Set the **AUX OUTPUT** to one of the following:

- **Loop-through:** The Loop-through option sends the active SDI or IP signal to the AUX OUT connector. If the active signal is IP, it is converted to an SDI signal at the AUX OUT connector. The AUX OUT audio and video timing relationship (delay) is maintained if the IP signal is ST 2110. The MPP product also has dedicated loopthrough connectors for each of the four SDI inputs. These dedicated loopthrough connectors are always enabled.

**Note:** AUX OUT loop-through of IP inputs is available for ST 2022-6 and ST 2110-20/ 22/30/31 (see _Configure Audio (ST 2110-30 / 31) Stream_ for audio configuration details) including embedded audio streams.

- **Generator:** The Generator option sends the output of the SDI generator to the AUX OUT connector. See SDI Generator Application for instructions on configuring the SDI Generator signal.

## ○ **3D LUT Mode:**

- ♦ To apply the user-selected LUT to the Aux output, select **On** . The VPID follows the aux output format of the LUT. 3D LUTs cannot be applied to AUX SDI Output in SD formats.

- ♦ To enable APP LINK mode, select **APP LINK** . APP LINK mode enables you to easily view and control the state of the AUX LUT from a tile application. In the following example, an application LUT has been turned on in the Waveform application, and the AUX LUT has been turned off.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **152 Configure the Instrument** Configure Instrument Outputs

If you toggle the AUX LUT button so that it is in the same state as the application LUT button, the buttons’ state is linked and a lock icon appears. If you change the state of the LUT button, the state of the AUX LUT button changes, too. This toggles the AUX LUT enable.

If you toggle the AUX LUT button so that it is in a different state than the application LUT button, the link between the buttons is disabled, and changing the state of one button does not affect the state of the other.

**Note:** For 2110-20 streams, if the format is 525i, the active video is cropped to 480 lines. If the format is 625i, the active video is cropped to 576 lines.

## **AUX OUTPUT AUDIO CHANNELS**

For ST 2110 inputs, you can configure the Aux Out signal to follow the input audio streams or map to the headphone pair.

**1.** Select the **Settings** icon ( ) and select **Outputs** .

**2.** Set the **AUX OUTPUT AUDIO CHANNELS:**

- **Fixed Channels** to have Aux Out follow the input audio streams.

- **Selected headphone pair on Ch-1 and Ch-2** to have Aux Out pair 1/2 map directly to headphone pair 1/2.

**3.** In the status bar, select **Volume** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 153** Configure Instrument Outputs

**4.** Select the pair from the list. All other audio pairs on the Aux Out are muted.

**Note:** In the case of multichannel audio, the Aux Out audio does not support remapping of downmixed audio. Pair 1/2 is output instead.

If the audio is decoded Dolby content, the volume pair selection is the raw pairs, with the exception that undecoded Dolby is not sent to the aux output to prevent speaker damage.

## **SDI LOOP-THROUGH (MPS/MPD only)**

When **SDI LOOP-THROUGH** is set to **On** , SDI 1 is looped out to SDI 3 and SDI 2 is looped out to SDI 4.

## **SDI LOOP-THROUGH (MPP only)**

The MPP product has dedicated loop-through connectors for each of the four SDI inputs. These dedicated loop-through connectors are always enabled, so there is no menu selection for SDI loop-through on MPP.

## **ANALOG AUDIO OUT and LINE OUT (MPP-200/300 only)**

The Analog Audio connector on MPP-200/300 provides up to eight channels of analog audio on a standard TASCAM style DB25 connector. Breakout cables for DB25 to eight channel XLR (for example) are readily available from audio equipment vendors.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **154 Configure the Instrument** Configure Instrument Outputs

The Line Out connector can provide discrete channels or downmix to an external 2- channel device such as a speaker. See section _MPP-200/300 Rear Connectors_ for pin out and signal level details.

Select **Discrete Channels** to route the active audio program to the Analog Audio connector as shown in the table below. All shaded channels are mute. The Left and Right channels are routed to the Line Out connector.

Up to eight discrete audio channels are supported. If an audio program has more than eight channels, only the first eight channels are supported.

Select **Downmix** to route a downmix signal to the channel 1 and 2 on the Analog Audio connector as shown in the mapping table below. All shaded channels are mute.

Downmix will also be present on the Line Out connector.

Downmix of 5.1.4 and 7.1.4 are not supported.

See _Downmix Controls_ for instructions about setting up a downmix signal.

Analog Audio Output Mapping

|             | **Channel** | **Channel** |       |       |       |       |       |       |
| ----------- | ----------- | ----------- | ----- | ----- | ----- | ----- | ----- | ----- |
| **Format**  | **1**       | **2**       | **3** | **4** | **5** | **6** | **7** | **8** |
| Mono        | M           | mute        | mute  | mute  | mute  | mute  | mute  | mute  |
| Stereo      | L           | R           | mute  | mute  | mute  | mute  | mute  | mute  |
| 5.1 / 5.1.4 | L           | R           | C     | Lfe   | Ls    | Rs    | mute  | mute  |
| 7.1 / 7.1.4 | L           | R           | C     | Lfe   | Ls    | Rs    | Lbs   | Rbs   |
| Downmix     | L           | R           | mute  | mute  | mute  | mute  | mute  | mute  |

See section _MPP-200/300 Rear Connectors_ for pin out and signal level details of the Analog Audio signals.

**Note:** Only the Mute control affects the channels on the Analog Audio and Line Out connectors. Volume and Balance do not affect the Analog Audio and Line Out channels.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 155** Configure to Decode Timecode

## **Configure to Decode Timecode**

Timecode decodes and displays ST 12-1:2014 Ancillary Timecode on the status bar. ANC LTC (linear time code), ANC VITC (vertical interval time code), and Date Readout are supported.

**1.** Select the **Settings** icon ( ).

**2.** Select **Anc Data** .

## **Select Timecode Format**

In the **Timecode Format** section, select **LTC** or **VITC** as needed.

**Note:** Changing the timecode format changes the timecode at the bottom of the Status frame, all alarms and events, and in the timecode overlay.

## **Turn on Timecode Overlay**

In the **Timecode Overlay** section, select one of the following:

- **Off:** No timecode overlay is displayed.

- **Display 1:** Adds a timecode overlay to _only_ the first monitor or screen.

Move the timecode: select it and drag it to any place in the first monitor or screen.

- **Display 2:** Adds a timecode overlay to _only_ the second monitor or screen. Move the timecode: select it and drag it to any place in the second monitor or screen.

- **Both:** Adds a timecode overlay to both monitors or screens (one on each).

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **156 Configure the Instrument** Configure Reference Settings

Move each timecode independently: select one and drag it to any place it the respective monitor or screen.

**Note:** Both Timecode Overlays match the Timecode Format (LTC or VITC) in the Anc Data menu and the timecode in the Status frame.

## **Configure Reference Settings**

The reference configuration of PRISM is in the middle of the status bar. The third line is the reference type. The fourth line displays the Video versus Reference lock indication, which shows whether the signal is N/A, Mismatched, Drifting, or Locked.

The Timing application supports SDI timing against Analog external reference, analog external reference timing against PTP, SDI timing against PTP, and IP timing against PTP.

## **Configure External Reference**

**1.** Select the **Settings** icon ( ).

**2.** Select **Reference** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 157** Configure Reference Settings

**3.** Select a reference option:

- **Internal:** The timing is based on an internal clock.

- **Analog:** Refers to a Black Burst or Tri-Level Sync (TLS) external reference. An analog external reference is connected to the REF BNC input on the back panel.

- **PTP:** Refers to Precision Timing Protocol (PTP) external reference. PTP external reference must come through the 10/25GE SFP Port 1 input on the back panel.

**Note:** When you select a reference, the reference changes in the status bar and in the Timing application.

## **Configure Analog Reference Settings**

**1.** Select the **Settings** icon ( ).

**2.** Select **Reference** and then select the **Analog Ref Setting** tab.

**3.** Select a reference I/O option:

- **Loop-Through Input to Output:** The REF input is looped out the REF output BNC.

- **Terminate Input:** The REF input is terminated at the REF input BNC. There is no signal at REF output BNC.

- **Terminate Input, PPS Output:** The REF input is terminated at the BNC. The REF output BNC will have the PPS signal when the PTP is locked.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **158 Configure the Instrument** Configure Reference Settings

## **Configure PTP Reference Settings**

**1.** Select the **Settings** icon ( ).

**2.** Select **Reference** and then select the **PTP Settings** tab.

**3.** Select **Enable PTP Logging to the Event Log** to enable or disable it.

**4.** Select the profile to configure: **ST2059** , **AES67** , or **General** . The default communication mode for each profile is Multicast.

- If you select the ST2059 profile and the communication mode, it is a mixture of Multicast and Unicast, select **Mixed SMPTE w/o negotiation** .

**Note:** On the SMPTE profile mixed mode, the PTP Announce and Sync messages are sent as Multicast. However, the Delay request and Delay Response messages are sent as Unicast. Therefore, it is important to ensure correct configuration of IP addresses and layer three communication to ensure that the Delay Request and Response are transmitted and received correctly.

**5.** Select the **Domain (0-127)** box.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 159** Configure and Recall Instrument Presets

**6.** Use the editing controls to enter a new domain number. When using the editor:

- Select the **Clear** icon ( ) to remove the existing domain number.

- Tap **Backspace** to delete characters.

**7.** When you are done editing the domain number, press **Enter** .

**8.** Repeat Steps 4 through 7 for each PTP profile.

## **Configure and Recall Instrument Presets**

Instrument setups can become complex as you tailor them to monitor various parameters. To save set up time and ensure consistency, you can save and quickly access instrument setups in the instrument using the **Presets** icon ( ) on the instrument display.

The instrument can store up to 36 separate instrument presets. The presets are divided into six groups, A through F, with each group containing six preset storage locations. The default preset names are A1-A6, B1-B6, C1-C6, D1-D6, E1-E6, and F1-F6.

All instrument settings except those set in the Utilities and Network Settings submenus of the Configuration menu are saved in a Preset. Settings that are not saved are those such as the clock setting, IP configuration, and network address. This is an overview of the settings saved in a Preset. Some settings are option- or model-dependent:

- Application assigned to each tile

- Application icon order in the application selector list

- Application specific settings

- Input selection and configuration (including single- and multi-input mode)

- PTP reference settings

- SDI Generator, IP Display, and IP Generator settings

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **160 Configure the Instrument** Configure and Recall Instrument Presets

## **Turn on Edit Mode**

When Edit mode is on, selecting a preset button displays a menu to allow changes to that preset button (Rename and Save as) you can also recall the existing settings (Recall). You can assign any preset button with any configuration of applications, outputs, and inputs.

When edit mode is off, selecting a preset button recalls only the preset settings assigned to that button, with no confirmation.

To turn on Edit Mode:

**1.** Select the **Settings** icon ( ).

**2.** Select **Presets** .

**3.** Set **Edit Mode** to **On** .

## **Save Presets**

To save a preset with a user-defined name and settings, or to reassign a named preset with new name and settings:

**1.** Set up the instrument the way you want it configured. This includes selecting the application display for each tile and configuring inputs and the PTP reference settings.

**2.** _Turn on Edit Mode_ .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 161** Configure and Recall Instrument Presets

**3.** Select the **Presets** icon ( ) to open the Preset selection menu at the bottom of the PRISM display.

**4.** Locate the Preset button you want to save with the current instrument configuration. There are six presets in each of six groups. Use the arrow buttons ( and C ) or swipe left or right to move to the preset group (A–F).

**Note:** When a preset has no content, **<** empty **>** is displayed on the preset button.

**5.** When you have found the preset to assign the settings (this includes choosing an assigned preset and overwriting the existing settings), select the preset button. A menu appears.

**6.** Select **Save As** to save the existing settings to the highlighted preset button and name it. An on-screen keyboard appears.

**7.** If the preset button name is <empty> or you want to change the name, use the keyboard. If you do not want to change the name, select **Save** . A confirmation window appears.

**8.** Select **OK** to save the preset. The preset name changes from <empty> or a name to the entered name. The number is the preset position in the preset group.

**9.** Select the **Home** icon ( ) to close the Preset selection menu.

## **Rename PRISM Presets**

To rename a preset without changing any settings.

**1.** _Turn on Edit Mode_ .

**2.** Select the preset to rename.

**3.** Select **Rename** and type a new name. If Rename does not appear, Edit mode is not on.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **162 Configure the Instrument** Configure and Recall Instrument Presets

**4.** Select **Save** .

## **Rename Group of Presets**

**1.** Select the **Settings** icon ( ).

**2.** Select **Presets** .

**3.** Select **Rename** .

**4.** Select the **Preset** group, at the top of the submenu, to select the group with the preset to rename (this includes naming an <empty> preset).

**5.** Select the name box of the preset to name or rename. An on-screen keyboard appears.

**Note:** You can also rename a preset group by selecting a group name box.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 163** Configure and Recall Instrument Presets

**6.** Use the on-screen keyboard to enter a new name for the preset. When renaming a preset:

- Enter a name with up to 16 characters.

- Select the **Clear** icon ( ) to remove the existing name.

- Tap the **Shift** key to access capital letters.

- Tap **Backspace** to delete characters by backspacing over them.

- Tap the **123-abc** key to change between the letter keyboard and the numberssymbols keyboard.

**7.** When the preset name is correct, select **Enter** .

**Note:** If Edit Mode is on, you can rename a preset through the Preset selections menu. Select the preset to rename and then select **Rename** and rename the preset just as in the Presets Rename submenu.

## **Download and Upload PRISM Presets**

To download the presets of an entire PRISM (clone the presets) and upload them to another PRISM, there are two options: _Download Presets to USB Drive_ or _Download File of Presets Locally_ .

## **Download Presets to USB Drive**

**1.** Insert a USB drive into PRISM with the presets.

**2.** Select the **Settings** icon ( ).

**3.** Select **Presets** .

**4.** Select **Save and Copy USB Presets** and then select **SAVE TO USB** .

**5.** Select the USB drive and select **Save** . A copy of the presets is downloaded to the USB drive.

**6.** Select the **Activity** icon ( ) and then select the **Eject** icon ( ) to unmount the bal Q

USB drive from the instrument.

**7.** Remove the USB drive with the presets from PRISM.

For details about uploading the presets to another PRISM, see _Upload Presets from USB Drive_ .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **164 Configure the Instrument** Configure and Recall Instrument Presets

## **Upload Presets from USB Drive**

## **CAUTION: Uploading presets overwrites all existing presets in PRISM.**

**1.** Insert a USB drive with PRISM presets into PRISM to upload the presets.

**2.** Select the **Settings** icon ( ).

**3.** Select **Presets** .

**4.** Select **Save and Copy USB Presets** and then select **COPY FROM USB** .

**5.** Select the USB memory drive and select **Copy** . The downloaded presets are uploaded to PRISM.

**6.** Select the **Activity** icon ( | ) and then select the **Eject** icon ( Q ) to unmount the USB drive from the instrument.

**7.** Remove the USB drive with the presets from PRISM.

**8.** Select the **Close** icon ( ).

**9.** Repeat Steps 1 through 8 for any other PRISMs to copy the presets.

## **Download File of Presets Locally**

**1.** Use a web browser to access the PRISM HOME page for PRISM with the presets.

**2.** Select **Preset Download and Upload** . (Some home pages have different options than the example.)

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 165** Configure and Recall Instrument Presets

**3.** Select **Download from PRISM** and then select **Download** . A copy of the presets is downloaded to the local computer with the name of the PRISM and a timestamp, or you can rename the presets file.

**4.** To upload the presets to another PRISM, go to _Upload Presets through PRISM Homepage_ .

**==> picture [3 x 1] intentionally omitted <==**

**----- Start of picture text -----**<br>
.<br>**----- End of picture text -----**<br>

## **Upload Presets through PRISM Homepage**

## **CAUTION: Uploading presets overwrites all existing presets in the PRISM uploading the presets.**

**1.** With the presets file downloaded locally, go to the PRISM HOME page to upload the presets.

**2.** Select **Preset Download and Upload** .

**3.** Select **Upload to PRISM** and then select **Browse** . A file explorer window appears.

**4.** Find the saved preset (.prst) file, select it, and select **Open** . The file explorer window closes and the preset file is listed on the PRISM HOME page.

**5.** Select **Upload** . The downloaded presets are uploaded to the PRISM.

**6.** Repeat Steps 1 through 5 for any other PRISMs to receive the same presets.

**7.** Select your browser’s **Back** button to return to the PRISM HOME page.

## **Recall User-Defined Presets**

**1.** Select the **Presets** icon ( ).

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **166 Configure the Instrument** Configure and Recall Instrument Presets

**2.** Find the preset to recall. Use the arrow buttons ( and ) or swipe left or right to move to the preset group (A–F).

**Note:** When a preset has no content, **<** empty **>** is displayed on the preset button.

**3.** Select the preset button to recall. The selected preset button is highlighted and the instrument settings change to those assigned to the selected preset.

**4.** Select the **Home** icon ( ) to close the Preset selection menu.

**Note:** If the Edit Mode is on, select the preset to recall and then select **Recall** from the menu.

## **Use Preset Menu Options**

This menu has several alternatives to using the Settings menu:

**1.** Select the **Preset** menu button.

- Turn the **Preset Edit Mode** on or off; set the option to **On** or **Off** as needed. For details about the Preset Edit Mode, see _Turn on Edit Mode_ .

- Turn **Recall Saved Inputs** on or off; set the option to **On** or **Off** as needed. For details about the Recall Saved Inputs option, see _Recall Presets without Inputs_ .

- Rename the preset group:

- **i.** Select **Rename Preset Group** . To change individual preset names, see _Rename PRISM Presets_ . An on-screen keyboard appears.

- **ii.** Rename the current group name with the on-screen keyboard or a physical keyboard.

- **iii.** Select **Save** to save the new name.

**2.** Select the **Preset** menu button to close the menu.

## **Recall Presets without Inputs**

Presets contain all PRISM settings including input configuration. Turning off the Recall Saved Inputs setting allows the presets to be recalled without recalling any of the input settings (video, audio, data). In this mode, only the application and other settings are recalled.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 167** Configure and Recall Instrument Presets

**Note:** When the Recalled Saved Inputs setting is off, the preset still has all of the input settings, but they are not applied.

**1.** Select the **Settings** icon ( ).

**2.** Select **Presets** .

**3.** Set **Recall Saved Inputs** to **Off**

## **Recall Factory Presets**

**1.** Select the **Settings** icon ( ).

**2.** Select **Presets** .

**3.** Select **Preset Settings** .

**4.** In the confirmation box that appears, select **OK** to confirm the selection and to reset the instrument settings to the factory defaults. The following table lists some of the settings that are reset.

**Note:** Custom presets are still available after recalling the factory preset.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **168 Configure the Instrument** Configure and Recall Instrument Presets

Instrument Settings Reset by Recall Factory Preset

| **Item**                                                                    | **Setting**              |
| --------------------------------------------------------------------------- | ------------------------ |
| Tile 1 application                                                          | Waveform                 |
| Tile 2 application                                                          | Video Session            |
| Tile 3 application                                                          | Picture                  |
| Tile 4 application                                                          | Audio                    |
| SDI-In 1 input configuration<br>Input name<br>Input type<br>Input connector | SDI-In 1<br>SDI<br>SDI 1 |
| SDI-In 2 input configuration<br>Input name<br>Input type<br>Input connector | SDI-In 2<br>SDI<br>SDI 2 |
| SDI-In 3 input configuration<br>Input name<br>Input type<br>Input connector | SDI-In 3<br>SDI<br>SDI 3 |
| SDI-In 4 input configuration<br>Input name<br>Input type<br>Input connector | SDI-In 4<br>SDI<br>SDI 4 |
| SDI-In 5 input configuration<br>Input name<br>Input type<br>Input connector | SDI-In 5<br>SDI<br>SDI 1 |
| SDI-In 6 input configuration<br>Input name<br>Input type<br>Input connector | SDI-In 6<br>SDI<br>SDI 2 |

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 169** Configure Syslog

Instrument Settings Reset by Recall Factory Preset

| **Item**                                                                                                                        | **Setting**                            |
| ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| PTP reference configuration<br>PTP Logging to the Event Log<br>Selected Profile<br>ST 2059 domain<br>ST 2059 communication mode | Enabled<br>ST 2059<br>127<br>Multicast |
| SDI Generator configuration<br>Enable SDI Generator                                                                             | Disabled                               |
| IP Generator configuration<br>Enable IP ST 2110 Generator<br>Reference                                                          | Disabled<br>Internal                   |

## **Configure Syslog**

**Note:** PRISM supports Syslog protocol (RFC 5424) for alarms and events.

**1.** Select the **Settings** icon ( ).

**2.** Select **Network** and then select **REMOTE ACCESS** .

**3.** In the **Syslog Server Address** box, type the IP address of the computer running the syslog server software.

**4.** In the **Syslog Server Port** box, type the number configured in the syslog server software.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **170 Configure the Instrument** SNMP Functionality

**Note:** If you have questions about configuring your syslog server software, contact your system administrator.

**5.** Select **Save** . The syslog server software collects events and alarms, and displays the details.

## **SNMP Functionality**

This section explains how to configure and use SNMP and traps (alarms).

## **SNMP Web UI Settings**

To configure SNMP through a web browser:

**1.** Go to the PRISM homepage (enter the PRISM IP address in a web browser).

**2.** Select **SNMP** and set **Enable SNMP Traps** to **Enable** .

**3.** Fill in the **Trap Destination** and **Trap Community String** fields.

**4.** Select **Download** to download the SNMP MIB.

## **SNMP Traps**

PRISM supports SNMP only for alarms (traps). PRISM supports a single trap prefix (prismTrap), which can be seen in the Video signal lost sample. The SNMP configuration is created through the RESTful API.

- The alarm is identified in the SNMP trap payload.

- The PRISM SNMP MIB is provided in the file prism_mon.mib file, which can be downloaded from the PRISM web page.

- SNMP trap destination address is set with RESTful API using post operation, through Postman or a similar application.

- The alarms generated in the PRISM are sent to the destination trap receiver as a single SNMP trap.

- Users must have a trap receiver running on the destination machine and the IP address of the PRISM (snmpAgent) need to be configured with the destination IP address.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 171** SNMP Functionality

## **Enable Restful API SNMP Controls**

**Note:** To open the PRISM help page, go to http://IpAddress/api/help (replace “IpAddress” with your PRISM IP address).

To set SNMP_TRAP_ENABLE_ON, you need an API development application, such as Postman.

**1.** In a PRISM, open an API development application, such as Postman.

- GET and POST are allowed commands.

- In these examples, replace “aaa.aaa.aaa.aaa” with the IP address of the PRISM the sending the traps and “bbb.bbb.bbb.bbb: with the IP address of the computer receiving the traps.

**2.** Set the SNMP_TRAP_ENABLE_ON:

- **A.** Enter the IP address of the unit:

aaa.aaa.aaa.aaa/api/snmp_trap_enable

- **B.** In the body of the JSON command, enter:

{ "ints":[ "SNMP_TRAP_ENABLE_ON" ] }

- **C.** Execute as a POST operation.

**3.** Set the trap destination address:

- **A.** Enter the following command:

aaa.aaa.aaa.aaa/api/snmp_trap_destination_address

- **B.** In the body of the JSON command, enter:

{ "string":"bbb.bbb.bbb.bbb" }

## **C.** Execute as a POST operation.

**4.** Set the SNMP community string:

- **A.** Enter the address of the unit:

aaa.aaa.aaa.aaa/api/snmp_trap_community

## **B.** In the body of the JSON command, enter:

{ "string" : "new_trap_community" }

- **C.** Execute as a POST operation.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **172 Configure the Instrument** Configure Alarms

## **Check Traps**

**1.** Download the prism_mon.mib from the PRISM web page.

- **A.** Open the PRISM instrument home page.

- **B.** Enter the PRISM IP address in a browser.

- **C.** Select **SNMP** in the PRISM menu.

- **D.** Select **Download** .

**2.** Install any SNMP manager on the machine where you want to check the traps.

- **A.** From the SNMP manager, configure the SNMP agent (PRISM) IP address.

- **B.** Load the prism.mib file.

- **C.** Open the trap receiver window.

- **D.** Confirm that the traps are received on the trap receiver window of the MIB browser application on the destination machine (on port 162).

## **Configure Alarms**

Alarms are always operational and logged (with a few exceptions). They are also optionally sent to a syslog server or SNMP client. For each alarm group or individual alarm, you can also enable presentation on the Activity Dashboard.

Many alarms also have user-definable thresholds to set specific limits for the alarm.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 173** Configure Alarms

## **Select Group Alarms**

Select the **Settings** icon ( ) and then select **Alarms** .

- To turn on the group of alarms, select the checkbox under Dashboard for the group.

- To reset the thresholds for a group of alarms, select the **Reset** icon ( ) under Threshold for the group.

## **Select Specific Alarm**

**1.** Select the **Settings** icon ( ), select **Alarms** , and then select the alarm group that contains the specific alarm.

**2.** Select the checkbox of the alarm to monitor.

## **Change Alarm Threshold**

**Note:** If the alarm shows information in the Threshold column (not N/A), you can change the setting.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **174 Configure the Instrument** Configure Alarms

**1.** Select the alarm title.

**2.** Select the arrows to change the threshold settings.

Depending on the alarm, there might be up to four thresholds.

## **All Alarms**

This section lists the available alarms by group; individual alarm titles are in bold. There are descriptions of each alarm and what parts of alarms can be set, if any.

There are two types of events in the Event Log:

- Type 1: The first occurrence of an error immediately triggers a Persistent (Set) alarm.

- Type 2: An event that is not followed by another event in 1 second is recorded as a Momentary Alarm. An event with multiple occurrences that continue for more than 1 second is recorded as a Persistent (Set) alarm.

Type 1 measurements:

- SDI Active Field Length Error

- SDI Total Field Length Error

- SDI Line Length Error

- SDI EAV Placement Error

- SDI SAV Placement Error

- SDI Line Number Error

- SDI Y-channel CRC Error

- SDI C-channel CRC Error

- SDI Y-channel ANC Checksum Error

- SDI C-channel ANC Checksum Error

- SDI EDH Active Picture CRC Error

- SDI EDH Full-field CRC Error

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 175** Configure Alarms

- Ethernet CRC Error

Type 2 measurement:

- Any other events not listed above

## **ANC Session**

- **Duplicate SCTE104 Message:** A copy of an SCTE104 packet has been received as seen on the ANC Session application.

- **SCTE104 Message:** An SCTE104 packet has been received as seen on the ANC Session application.

## **Audio**

- **Audio Over Error:** Audio signal is at or above the specified Max audio level for a time longer than the Duration setting. Duration and the Max decibels of the audio can be set.

- **Audio Pair Out of Phase:** Currently selected channels displayed in Lissajous have the channel correlation at or below the specified percentage for a time longer than the duration setting. Duration and the Min percentage of the audio pair phase can be set. See _Audio Pair Out of Phase Alarm Description_ .

- **Audio Sample Peak:** Max dBFS can be set.

- **Audio Signal Lost:** No Audio is present in the currently active signal.

- **Audio Silence Error:** Duration in seconds and Min dB can be set.

- **Audio True Peak:** Max dBTP can be set.

- **Loudness Dialogue Meas:** Max dialnorm can be set.

- **Loudness Infinite:** Max and Min LKFS/LUFS can be set.

- **Loudness Momentary:** Max LKFS/LUFS can be set.

- **Loudness Range:** Min LU can be set.

- **Loudness Short:** Max LKFS/LUFS can be set.

- **Loudness Speech:** Min % can be set.

## **CC (Closed Captions) / Subtitles**

- **ARIB Closed Captions Lost:** No valid ARIB closed caption packets in the ancillary data space were found. Duration of the loss can be set.

- **CEA708 Closed Captions Lost:** No valid CEA708 closed caption packets in the ancillary data space were found. Duration of the loss can be set.

- **OP-47 Multipacket Teletext Lost:** No valid Operational Practice 47 multidata packets were found in the ancillary data space of the signal. Duration of the loss can be set.

- **OP-47 SDP Teletext Lost:** No valid Operational Practice 47 SDP data packets were found in the ancillary data space of the signal. Duration of the loss can be set.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **176 Configure the Instrument** Configure Alarms

- **S334-1 CEA 608 Closed Captions Lost:** No valid ST 334-1 CEA 608 closed caption packets were found in the ancillary data space. Duration of the loss can be set.

- **S334-2 CEA 608 Closed Captions Lost:** No valid ST 334-2 CEA 608 closed caption packets were found in the ancillary data space. Duration of the loss can be set.

- **SMPTE 2031 Teletext Lost:** No valid ST 2031 ANC data packets were found in the ancillary data space. Duration of the loss can be set.

- **TTML Closed Captions Lost:** No valid TTML data was found in the ST 2110-43 stream for the time specified in the Duration setting.

## **Gamut**

- Input signal contains colors that violate the set limits for YRGB gamut thresholds. Set limits: YRGB minimum and maximum, Picture Area percent, and Frame Duration. See _Gamut Alarm_ .

## **HDR**

**Note:** These errors relate to the information displayed in the Measurement Overlay. See _Measurement Overlay: Details_ .

To turn on the HDR alarms, in **Settings** ( ), in **Alarms** , set **Enable HDR Alarms** to **On**

Disabling the HDR alarms allows the PRISM to run with fewer CPU cycles for quieter operation.

- **Area HDR Percent:** Area of the video image that is in the HDR Zone (above HDR Zone Threshold Nits). This is the value reported by the “% HDR Area” in the Picture Measurements overlay. To set the HDR Zone Threshold, go to the **Measurement Thresholds** in **Picture** settings.

- **Area Percent Nits:** Percent of the area of the active video that is above the specified threshold (in nits) for more than the specified duration. To set the Area (%), go to the **Measurement Thresholds** in **Picture** settings.

- **Brightest Percent Nits:** Brightest percent of the active video that is above the specified threshold (in nits) for more than the specified duration. To set the Brightest Area (%), go to the **Measurement Thresholds** in **Picture** settings.

- **Contrast Ratio:** Contrast ratio of the video is above or below the specified thresholds for more than the specified duration.

- **Darkest Percent Nits:** Darkest percent of the active video is above the specified threshold (in nits) for more than the specified duration. To set the Darkest Area (%), go to the **Measurement Thresholds** in **Picture** settings.

- **Dynamic Range:** Dynamic range of the video is above or below the specified thresholds for more than the specified duration.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 177** Configure Alarms

## **IP**

- **Audio Stream Configuration Error:** Detected Audio Channel count and/or Packet Timing do not match the Stream Configuration. See IP Session Audio for the Stream.

- **Combined RTP Sequence Error:** RTP sequence error occurred in the combined output of a media stream protected using RTP packet reordering or ST 2022.7 seamless switching.

- **Data Rate Invalid or Unstable:** Detected data rate of a video input is unstable or nonstandard.

- **Ethernet BER Excessive:** Excessive bit-error rate has been detected on Ethernet interface.

- **Ethernet Buffer Overflow:** Overflow was detected on IP Video Ports.

- **Ethernet CRC Error:** CRC error was detected in an Ethernet frame.

- **Ethernet Interface Saturated:** Ethernet interface is saturated.

- **HBRMT Header Invalid:** Error occurred in the HBRMT header.

- **HBRMT Sequence Error:** Packets are dropped, out of order, or duplicated; or a sequence number in a flow does not change.

- **HBRMT Timestamp Error:** HBRMT timestamp is corrupt or is not updating at the correct frequency for the specified media type.

- **L4 Protocol Checksum Error:** Checksum error was detected in an IP or UDP packet.

- **Network Connection Lost:** Fiber connection to SFP port has been removed or FEC mode is in the wrong state.

- **RTP Header Invalid:** Error occurred in the RTP header.

- **RTP Marker Frequency Error:** RTP marker bit is not designated at the correct frequency for the specified media type.

- **RTP Sequence Error:** Sequence errors can be caused by dropped, out of order, or duplicated packets. They can also be triggered when the sequence number within a flow does not change.

- **RTP Timestamp Error:** RTP timestamp is corrupt or is not updating at the correct frequency for the specified media type.

- **S2022.7 Path Missing:** One of the data paths in a ST 2022-7 seamless switching configuration is missing.

## **SDI Vu**

- **ANC Parity:** An ANC channel has had a parity error.

- **AV Samples:** The number of audio samples per five frames of video doesn’t match the expected number of audio samples.

- **Audio Content (Silence, Mute):** The audio level of an audio channel has been below the silence threshold for a duration greater than the duration for silence, set in seconds, or a mute has been present for greater than the number of audio

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **178 Configure the Instrument** Configure Alarms

samples. **Note:** An audio channel with undecoded Dolby content may be detected as being mute.

- **Audio Parity - AES:** An audio error has occurred in AES audio.

- **Audio Parity - Emb:** An audio error has occurred in embedded audio.

- **CRC C channel:** An error has occurred on the CRC C channel.

- **CRC Y channel:** An error has occurred on the CRC Y channel.

- **Video Frequency:** The variance in carrier frequency is higher than the threshold.

## **Timing**

- **External Reference Lost:** External reference signal is not detected.

- **Link Timing Error:** Timing difference between any two links exceeds 400 nanoseconds, according to ST 425-6 2014.

- **PTP Unlocked:** PTP is unlocked or missing.

- **Timing Drift:** Input signal is not frequency locked to the reference signal. Drift rate is more than 10us of timing change on a 20-second window, larger drift rates are detected faster.

- **Video and Reference Mismatch:** Detected format of the external reference signal is not compatible with the input signal format.

- **Video-RTP Offset PATH 1 and PATH 2:** The value of Video-RTP Offset exceeds the threshold. This measurement is the difference between the IP VIdeo-RTP timestamp and the PTP reference time.

## **Video Session**

- **Format Unsupported:** Detected video format is not supported.

- **Inter-link Format Mismatch:** Four links of a quad-link signal are not the same format.

- **SD Video Detected:** Detected video format is standard definition, for example 525 or 625.

- **SDI Active Field Length Error:** Input signal is not frequency locked to the reference signal.

- **SDI C-channel ANC Checksum Error:** Displays the status of the C channel ancillary embedded checksum value that was calculated for the video signal. Using a known test signal, the checksum status can be used to verify integrity through a system. An error means that the C Channel embedded checksum value does not match the calculated checksum value, which indicates that a transmission error has occurred.

- **SDI C-channel CRC Error:** Displays the status of the C channel embedded CRC (Cyclical Redundancy Check) that was calculated for the video signal. Using a known test signal, the CRC status can be used to verify integrity through a system. An error means that the C Channel embedded CRC value does not match the calculated CRC value, which indicates that a transmission error has occurred.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 179** Configure Alarms

- **SDI EAV Placement Error:** SDI End-of-Active Video placement error has occurred.

- **SDI EDH Active Picture CRC Error:** RP165 AP CRC value embedded in the data stream differs from the calculated CRC, or that it has been marked as invalid in the EDH packet, indicating there are EDH errors in the active picture.

- **SDI EDH Full-Field CRC Error:** RP165 FF CRC embedded value differs from the calculated CRC value (or that it has been marked as invalid in the EDH packet), indicating that there are EDH errors in the full field.

- **SDI Line Length Error:** Incorrect encoded transport line number was detected.

- **SDI Line Number Error:** Incorrect encoded transport line number was detected.

- **SDI SAV Placement Error:** SDI Start-of-Active Video placement error has occurred.

- **SDI Total Field Length Error:** The total field length of SDI video is incorrect.

- **SDI Y-channel ANC Checksum Error:** Displays the status of the Y channel ancillary embedded checksum value that was calculated for the video signal. Using a known test signal, the checksum status can be used to verify integrity through a system. An error means that the Y Channel embedded checksum value does not match the calculated checksum value, which indicates that a transmission error has occurred.

- **SDI Y-channel CRC Error:** Displays the status of the Y channel embedded CRC (Cyclical Redundancy Check) that was calculated for the video signal. Using a known test signal, the CRC status can be used to verify integrity through a system. An error means that the Y Channel embedded CRC value does not match the calculated CRC value, which indicates that a transmission error has occurred.

- **SMPTE 352M Payload ID Missing:** A mandatory ST 352M video payload identifier packet is missing.

- **Video Format Changed:** TRS count performed by the instrument does not agree with the line number embedded in the 292M line.

- **Video Format Mismatch:** Detected format of the video-input signal does not match the Input Format setting (which is set to a specific line rate, rather than being set to Auto) in the SDI Input submenu of the Configure menu or the setting specified in the ST 352 payload (if present).

- **Video Signal Lost:** Video input signal has not been detected at the selected input.

- **SDI C-channel ANC Checksum Error:** Displays the status of the C channel ancillary embedded checksum value that was calculated for the video signal. Using a known test signal, the checksum status can be used to verify integrity through a system. An error means that the C Channel embedded checksum value does not match the calculated checksum value, which indicates that a transmission error has occurred.

- **SDI C-channel CRC Error:** Displays the status of the C channel embedded CRC (Cyclical Redundancy Check) that was calculated for the video signal. Using a known test signal, the CRC status can be used to verify integrity through a system. An error means that the C Channel embedded CRC value does not match the calculated CRC value, which indicates that a transmission error has occurred.

- **SDI EAV Placement Error:** SDI End-of-Active Video placement error has occurred.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **180 Configure the Instrument** Configure Alarms

- **SDI EDH Active Picture CRC Error:** RP165 AP CRC value embedded in the data stream differs from the calculated CRC, or that it has been marked as invalid in the EDH packet, indicating there are EDH errors in the active picture.

- **SDI EDH Full-Field CRC Error:** RP165 FF CRC embedded value differs from the calculated CRC value (or that it has been marked as invalid in the EDH packet), indicating that there are EDH errors in the full field.

- **SDI Line Length Error:** Incorrect encoded transport line number was detected.

- **SDI Line Number Error:** Incorrect encoded transport line number was detected.

- **SDI SAV Placement Error:** SDI Start-of-Active Video placement error has occurred.

- **SDI Total Field Length Error:** The total field length of SDI video is incorrect.

- **SDI Y-channel ANC Checksum Error:** Displays the status of the Y channel ancillary embedded checksum value that was calculated for the video signal. Using a known test signal, the checksum status can be used to verify integrity through a system. An error means that the Y Channel embedded checksum value does not match the calculated checksum value, which indicates that a transmission error has occurred.

- **SDI Y-channel CRC Error:** Displays the status of the Y channel embedded CRC (Cyclical Redundancy Check) that was calculated for the video signal. Using a known test signal, the CRC status can be used to verify integrity through a system. An error means that the Y Channel embedded CRC value does not match the calculated CRC value, which indicates that a transmission error has occurred.

- **SMPTE 352M Payload ID Missing:** A mandatory ST 352M video payload identifier packet is missing.

- **Video Format Changed:** TRS count performed by the instrument does not agree with the line number embedded in the 292M line.

- **Video Format Mismatch:** Detected format of the video-input signal does not match the Input Format setting (which is set to a specific line rate, rather than being set to Auto) in the SDI Input submenu of the Configure menu or the setting specified in the ST 352 payload (if present).

- **Video Signal Lost:** Video input signal has not been detected at the selected input.

## **Alarm Descriptions**

This section provides more details about certain alarms.

## **Audio Pair Out of Phase Alarm Description**

The Audio Pair Out of Phase alarm warns if the audio signals in a pair are out of phase, according to the set duration and percentage of phase.

The example alarm is set for 1 second duration of -30%.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 181** Configure Alarms

The percentage describes the location on the correlation meter (below the Lissajous image) in the Audio application. The alarm does not occur when the phase marker (green diamond) is above -30% (in the example setting) for more than a second.

**Note:** The midpoint of the correlation meter is 0. Far left is -1 or -100%, which is out of phase. Far right is +1 or +100%, which is in phase.

## **Gamut Alarm**

The gamut alarm indicates when the input signal contains colors that violate the currently set limits for YRGB gamut thresholds, which are specified by the Settings/ Alarms/Gamut. These measurements conform to the EBU R103 V3 standard.

- **Enable Gamut Alarm:** Set to **Off** to disable gamut measurements and minimize CPU loading for quieter operation.

- **Gamut Preset:** Select **EBU R103** to reset the gamut measurements to the EBU R103 V3 defaults. The Gamut Preset resets only the YRGB thresholds, not the Picture Area or Frame Duration.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **182 Configure the Instrument** Configure Alarms

Thresholds can be displayed in 10-bit or 12-bit representation.

- **YRGB:** Select the line to set Min and Max.

- **Picture Area:** Select anywhere in the line to open the control to set a percentage.

- **Frame Duration:** Select anywhere in the line to open the control to set the number of frames.

Gamut alarms are reported in the Event Log application in the format:

**Gamut Violation:** Max YRGB, Min yrgb, Area xx.x%

- Max YRGB: violation for Y, R, G, or B components, violations are marked by an uppercase component letter. Underscores are used when no violations are found.

- Min yrgb: violation for Y, R, G, or B components, violations are marked by a lowercase component letter. Underscores are used when no violations are found.

- Area: the percent of the active picture that is in violation for one component. This is only the component with the most violation, not all components together.

**Limits:** Max xxxd, Min xxxd, >x% Area, >X Frames

These limits were in effect when the alarm was asserted.

In this example:

- Max has violations in the G and B components. Min has violations in the y, r, g, and b components. The component with the most violation covers 0.9% of the active picture.

- Gamut Maximum is set to 984d, the Minimum Threshold is set to 20d, the Picture Area is set to 1 percent, and the Frames Duration is set to 1.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 183** Adjust Display

**Note:** When Gamut is disabled, no Gamut alarms are generated or logged.

Gamut measurements are not supported for psF, 3G Level-B, SQD, or 8K input signals.

## **Viewing Alarms**

In addition to viewing alarms in the Event Log application, you can view the current status of all enabled alarms on the PRISM web page.

**1.** In a web browser, enter the hostname or IP address of the PRISM. See _Find or Change Hostname, Password, and IP Address_ .

When the PRISM is connected, the PRISM HOME page is displayed.

**2.** Select **Alarm Status** . The Alarm Status screen is displayed.

The status of all enabled alarms is displayed here. You can use the controls at the top of the page to poll alarm updates or refresh them manually.

To download the alarm history, press **Download Event Log** . A comma-separated values (csv) file is written to the download folder specified by the web browser.

## **Adjust Display**

The Display has settings for screen labels when multi-input is used, settings for trace and graticule intensity, and settings for brightness. It also has controls for extended display, which are explained in _Configure Extended Display_ .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **184 Configure the Instrument** Adjust Display

## **Configure Source Label**

When you use multi-input, you can define where and how the on-screen labels appear:

**1.** Select the **Settings** icon ( ).

**2.** Select **Display** .

**3.** Select **MULTI INPUT** . The Multi Input menu appears.

**Note:** You can set these options when multi-input is on or off.

## **Source Label Position**

The on-screen, multi-input label is visible when Multi Input is on. To change the location of the label:

- on the Multi Input page, select the **Source Label Position** menu and choose the location of the display; or

- in a tile, select a label and drag it to one of the four corners of the tile. The other labels in the other tiles will change to match.

## **Source Label Timeout**

You can configure whether labels are displayed as well as how long they are displayed. To change the action of the labels, select the **Source Label Timeout** menu and select from the options. These settings affect all tile labels.

## **Configure Safe Area Graticules**

When you use safe-area graticules, you can define where and how the Picture application on-screen graticules appear.

**1.** Select the **Settings** icon ( ).

**2.** Select **Display** .

**3.** Select **SAFE AREA GRATICULES** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 185** Adjust Display

**4.** In the **Safe Area Standard** section, select a standard: **ST 2046** , **RP 218** , **ITU** , or **ARIB TR-B.4** . The safe areas must be turned on in a Picture tile to appear. For details about turning on the selected safe areas, see _Select Safe Area Graticules_ .

**5.** To set custom safe areas:

- **A.** Select anywhere in **Custom 1** or **Custom 2** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **186 Configure the Instrument** Adjust Display

- **B.** Update the **Width** and **Height** settings as needed.
  - ♦ In the **Width** and **Height** boxes, type a percent number up to the hundredths place; or

  - ♦ Select the up or down arrows to set the numbers. The arrows change the number by hundredths. Hold the arrow to change the number faster.

**Note:** The percent number is the percent of the image (active height or width) that the custom frame will surround.

The SAFE ACTION frame turns on a solid line in the Picture tile.

The SAFE TITLE frame turns on a dashed line in the Picture tile.

**Note:** Because the safe area is defined by percent of the image, the image format does not affect the marked area. For example, 90% of the height of the image is 90% for 1280 x 720 or 4096x2160.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 187** Adjust Display

- **C.** If you need to move the frame off-center, select in the **Horizontal Offset** or **Vertical Offset** box and enter the percent of the frame to move the safe area.
  - ♦ Select the **±** symbol in the on-screen keypad to switch between positive and negative numbers.

  - ♦ To move the frame horizontally, positive numbers move the frame to the right, negative numbers move the frame to the left.

  - ♦ To move the frame vertically, positive numbers move the frame down, negative numbers move the frame up.

If the Offset takes a graticule frame outside the Picture tile, the border (solid or dashed) is visible at the edge of the tile (whatever side the frame is off) while the rest of the frame is smaller, as if the entire frame is visible.

- **D.** Select **Save Custom** . The Custom Safe Areas (Action and Title) are updated in the selected Picture tile when they are turned on in the Picture settings menu.

For details about turning on Custom Safe Areas, see _Select Safe Area Graticules_ .

## **Configure Graticule Colors**

**1.** Select the **Settings** icon ( ).

**2.** Select **Display** and then select **SAFE AREA GRATICULES** .

**3.** In the **Graticule Colors** section, select the colors from the following lists:

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **188 Configure the Instrument** Adjust Display

- **Safe Area Action 1 and Title 1:** This color is for both the Custom 1 Safe Area Action (solid line) and Custom 1 Safe Area Title (dashed line).

- **Safe Area Action 2 and Title 2:** This color is for both the Custom 2 Safe Area Action (solid line) and Custom 2 Safe Area Title (dashed line).

- **Picture Center Graticule:** This color is for the Picture Center Graticule.

- **AFD Graticule:** This color is for the AFD frame.

## **Configure Trace and Graticule Intensity**

To adjust the brightness of an application graticule and trace:

**1.** Select the **Settings** icon ( ).

**2.** Select **Display** .

**3.** Select **TRACE AND GRATICULE INTENSITY** .

**4.** Use the **Plus** icon ( Pe ) to increase intensity or the **Minus** icon ( ‘a ) to decrease intensity of the trace or graticules.

**Note:** You can also adjust the intensity by selecting anywhere in the control or by selecting and dragging the selector circle left or right.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 189** Adjust Display

## **Enable Picture Low Latency Mode**

If you enable Picture Low Latency Mode, you can quickly toggle between inputs, for SDI and IP. Picture Low Latency Mode minimizes the PRISM signal path latency, allowing users to more quickly see signal changes on the local Picture display, such as input changes. Low-latency mode improves the picture display response at the expense of additional picture judder. When low-latency mode is disabled (the default), the moving content of pictures transition smoothly, but the picture response time is longer.

To enable Picture Low Latency Mode:

**1.** Select the **Settings** icon ( ).

**2.** Select **Display** .

**3.** Set **Picture Low Latency Mode** to **On** .

**Note:** Picture Low Latency mode may introduce motion artifacts.

## **Configure Brightness**

**Note:** BRIGHTNESS controls are available on MPS and MPD products, depending on the display installed.

To adjust brightness:

**1.** Select the **Settings** icon ( ).

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **190 Configure the Instrument** Configure Time and Date

**2.** Select **Display** .

## **3.** Select **BRIGHTNESS** .

**4.** Move the slider, or use the **Plus** icon ( ) to increase brightness level or the **Minus** icon ( 4] ) to decrease it.

**5.** Select **Default** to configure the brightness to the default level, 40% (203 Nits).

The MPD model has two brightness sliders, and the MPS model has one.

## **Configure Time and Date**

This section explains how to set the internal time and date used by the instrument to record events. It also explains how to change the clock available on the status bar between PTP time and RTC.

**Note:** If you change the time and date settings, you must reboot the instrument to implement the changes.

**1.** Select the **Settings** icon ( ) and then select **Utilities.**

**2.** Select **Time and Date** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 191** Configure Time and Date

## **Update Time Zone**

**1.** Open the **Time and Date** menu (see _Configure Time and Date_ ) and select **TIME SETTINGS** .

**2.** From the **Time Zone** list, select the time zone offset for your location. The selection names include the time offset from UTC and major cities in those time zones.

**3.** Select **Save** to update the clock. A reboot is not required to change the time zone.

## **Change Status Bar Clock**

**Note:** The RTC or PTP clock in the status bar is set automatically to local time.

**1.** Open the **Time and Date** menu (see _Configure Time and Date_ ), select **TIME SETTINGS** .

**2.** In **Clock** on the status bar, select **Auto** , **RTC** , or **PTP** .

**Note:** The Auto setting searches for a PTP signal; if one is not available, it selects RTC.

**3.** Select **Save** . A reboot is not required to change the status bar clock.

## **Update RTC Clock**

**1.** Open the **Time and Date** menu (see _Configure Time and Date_ ), select **RTC CLOCK** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **192 Configure the Instrument** | Upgrade Instrument Firmware

**2.** Adjust the time and date using the up and down arrows as needed. The time setting uses a 24-hour clock, so no AM/PM setting is required.

**3.** Select **Save** .

**4.** In the message box that appears, select **OK** to confirm that you want to reboot the instrument to implement the time and date changes.

## **Upgrade Instrument Firmware**

Telestream releases updates to product firmware to add new features or to fix reported problems. Check the Telestream website regularly for new firmware releases and security updates.

**CAUTION: After upgrading to 5.x, the unit should not be downgraded to an earlier version. Please contact Telestream technical support for assistance. If power to the instrument is lost before the instrument begins erasing the internal flash, you can restart the firmware upgrade after the instrument reboots.**

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 193** Upgrade Instrument Firmware |

## **Before Upgrading**

You do not need to perform a firmware upgrade if the latest version of firmware is already installed on the instrument. To determine whether the firmware must be upgraded:

**1.** Power on the instrument.

**2.** Verify that the current software version is installed on the instrument:

- **A.** Select the **Settings** icon ( ) and select **Utilities** .

- **B.** Select **Version** . In the Software section, note the version number installed on the instrument.

**3.** Verify the latest version of firmware at the Telestream website:

- **A.** Use a web browser and go to the Telestream website software page:
  - www.telestream.net/video/resources.htm#Software

- **B.** Select the product and model title that best matches the instrument (such as PRISM) and in the list, find the software-upgrade package for the instrument.

- **C.** Note the latest version number of the software-upgrade package(s).

**4.** If the latest firmware version on the website is newer than the version on the instrument, upgrade the firmware.

**5.** Select the Firmware Release version for the instrument to download the update.

- **CAUTION: After the instrument starts the upgrade process, DO NOT remove power from the instrument. If you do, the instrument flash may get corrupted and you must send the instrument to a Telestream factory service center to restore it.**

**6.** Go to _Upgrade Firmware_ .

**Note:** The upgrade normally takes about 5 minutes to complete.

For details of what changed in the release, download the Release Notes for the version.

## **Upgrade Firmware**

You can upgrade the firmware remotely or via a USB drive.

## **Upgrade Firmware Remotely**

**1.** Enter the hostname or IP address from the instrument in a web browser. See _Find or Change Hostname, Password, and IP Address_ . The PRISM HOME page appears.

**2.** Select **Capture / Firmware / Diagnostics** . The Capture / Firmware / Diagnostics page appears.

**3.** In the Firmware Upload section, select **Browse** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **194 Configure the Instrument** Upgrade Instrument Firmware

**4.** Navigate to the local directory that contains the .ubin file you want to upload. Select the file and select **Open** .

**5.** Select **Upload** . The file is uploaded from your local computer to PRISM. After the firmware is up loaded, the MD5sum is displayed and can be compared with the one in the download package.

**6.** Select the **upgrade via the UI** link to launch VNC and finish installing the firmware.

**7.** On the PRISM monitor, select the **Settings** icon ( ) and select **Utilities** .

**8.** Select **Firmware Upgrade** . The display lists all of the files on the system with a .ubin file extension.

**9.** Select the file in the list, and then select **Install** to start the upgrade. When the upgrade begins, a message box appears stating that the firmware installation is in progress.

**Note:** If a USB device is inserted, the name of the USB device is listed along with the available .ubIn files.

The upgrade normally takes about 5 minutes to complete.

**Note:** Do not interrupt the instrument during the installation process.

## **Upgrade Firmware via USB Drive**

**1.** On an Internet-enabled computer, prepare a formatted (in exFAT or FAT32), nonbootable USB drive. It needs at least 2 GB of available space.

**2.** Unzip the PRISM file and copy the upgrade file with a .ubin file extension from the upgrade package onto the USB drive.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 195** Upgrade Instrument Firmware |

**Note:** The upgrade package includes an MD5 checksum and a PDF file, read the PDF file before performing the upgrade. The file contains important information about the firmware release.

**3.** Remove the USB drive from the computer and insert the USB drive into a USB port on the PRISM monitor.

**4.** On the PRISM monitor, select the **Settings** icon ( ) and select **Utilities** .

**5.** Select **Firmware Upgrade** . After the USB drive has been scanned, the display lists all of the files on the USB drive with a .ubin file extension.

**6.** Select the file in the list, and then select **Install** to start the upgrade. When the upgrade begins, a message box appears stating that the firmware installation is in progress.

**CAUTION: Removing the USB drive or powering off the instrument before the upgrade is complete can cause upgrade failure. To prevent upgrade failure, wait until the Installation Complete message box appears before performing these actions.**

The upgrade normally takes about 5 minutes to complete.

**Note:** It is important to not interrupt the instrument during the installation process.

**7.** When the install is complete, PRISM reboots automatically.

**8.** Select the **Activity** icon ( ) to view the devices mounted to the instrument.

**9.** Select the **Eject** icon ( B ) to unmount the USB drive from the instrument.

**10.** Remove the USB drive from the PRISM monitor.

**11.** Shut off the instrument:

- **A.** Select the **Settings** icon( ) and select **Utilities** .

- **B.** Select **Power** and select **Power Down Now** .

**12.** Disconnect the instrument from AC power.

**13.** Reconnect the instrument to AC power.

**14.** Press the power button on the instrument front panel to turn the instrument on.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **196 Configure the Instrument** Upgrade Software License

## **Verify Firmware Upgrade**

**1.** Select the **Settings** icon ( ).

**2.** Select **Utilities** and then select **Version** .

**3.** Verify that the displayed firmware version number matches the version of the firmware upgrade package you installed.

## **Upgrade Software License**

A software license upgrade allows you to add optional software features to the instrument. Go to www.telestream.net for the latest list of features that can be licensed

## **Install Software License Upgrade**

To activate the licenses, the instrument must be accessible by another computer on the local network. The instrument does not need to access the Internet.

To activate the licenses:

**1.** Connect the PRISM instrument to a local network and turn on power.

**2.** After the instrument has powered on, find the IP address:

- **A.** Select the **Settings** icon ( ) and then select **Network** .

- **B.** Select the **STATUS** tab and note the IP Address.

**3.** In a web browser, enter the IP address.

**4.** Select **License Portal** and follow the instructions on the page.

For further assistance, contact our technical support team: - www.telestream.net/telestream support/video/support.htm

## **Verify Software License Upgrade**

**1.** Select the **Settings** icon ( ).

**2.** Select **Utilities** and then select **Options.**

**3.** Verify that the displayed options match the options you installed.

## **Troubleshooting**

If the instrument needs service, you might be asked to provide the diagnostics file to Telestream to aid in understanding any problems with the instrument. This section describes how to download a zip file containing a service report of instrument diagnostics. The file can be downloaded remotely to your computer or to a USB drive on the PRISM.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Configure the Instrument 197** Troubleshooting

## **Download a Diagnostics File Remotely**

**1.** Enter the hostname or IP address from the instrument in a web browser. See _Find or Change Hostname, Password, and IP Address_ . The PRISM HOME page appears.

**2.** Select **Capture / Firmware / Diagnostics** . The Capture / Firmware / Diagnostics page appears.

**3.** In the Diagnostics File Download section, select **Save and Download** .

**4.** The Diagnostics File will be downloaded to the standard download directory determined by the computer and browser you are using. Do not navigate away from the web page while the diagnostic file is being downloaded.

## **Download a Diagnostics File to a USB Drive**

**1.** Select the **Settings** icon ( ).

**2.** Select **Utilities** and then select **Diagnostics** .

**3.** Insert a USB drive into one of the USB ports on the PRISM monitor.

**4.** Select **Save Diagnostics** to save the diagnostics report to the USB drive.

**5.** Select the **Activity** icon ( ) and then select the **Eject** icon ( B ) to unmount the USB drive from the instrument.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **198 Functions** Headphone or Speaker Volume, Balance, Device, and Source Adjustment

## **Functions**

This chapter describes additional functions available on the PRISM monitor.

- Headphone and speaker volume, balance, source adjustment, and downmix

- Stream Capture

## **Headphone or Speaker Volume, Balance, Device, and Source Adjustment**

Headphones can be connected to MPS, MPD, and MPP products:

- MPS headphone output on rear panel connector or front of bracket panel accessory for rack installation

- MPD headphone output on rear panel connector or front panel headphone port

- MPP headphone output on front panel

To access the volume, balance, and source controls for the headphone, select the **Volume** icon ( ). The available options are:

**1.** Select the audio device to use.

**2.** Select the source from the list of available channel pairs.

**3.** Use the control or arrow buttons to turn the volume up or down.

**4.** Use the control or arrow buttons to adjust the audio balance left or right.

**5.** Select the mute button to mute the audio.

**6.** Select the downmix button to listen to a downmixed group of channels. If the downmix button is not visible the Program Configuration might not be set in the **Settings > Inputs** menu. See the following Downmix Controls section.

**==> picture [364 x 99] intentionally omitted <==**

**----- Start of picture text -----**<br>
Audio<br>Mute Balance Volume<br>Device<br>Audio<br>Downmix<br>Sources<br>**----- End of picture text -----**<br>

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Functions 199**

Headphone or Speaker Volume, Balance, Device, and Source Adjustment

## **Downmix Controls**

Downmix combines channels to monitor them grouped as stereo or mono. There are several options to hear combined channels.

**Note:** The Dolby program configuration is based on metadata; no user input is needed. Downmix buttons are added to the Volume controls if they are applicable. See _Configure DOLBY_ .

## **Enable Downmix Button**

**1.** If the Input is PCM (not Dolby) select the **Settings** icon ( ).

**2.** Select **Inputs** .

**3.** Select the input with the channels to downmix.

- If the input is SDI, select **AUDIO** .

- If the input is ST 2022-6, select **AUDIO** .

- If the input is ST 2110, select **Audio (2110-30/31).**

**4.** If the Audio is PCM, select **PCM** and then select **Program Configuration** .

**5.** Check the Program Configuration is on and configured for multichannel audio (5.1 or higher).

**6.** Select **Save** .

**7.** Select the **Volume** icon ( ). The downmix button is visible.

## **Set Downmix Mode**

**Note:** This procedure is for PCM audio input.

With the downmix parameters set, select one of the Downmix Mode options in the Settings Audio menu:

**1.** Select the **Settings** icon ( ).

**2.** Select **Audio** .

**3.** Select from the Downmix Mode options.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **200 Functions**

Headphone or Speaker Volume, Balance, Device, and Source Adjustment

- **Lt Rt** (left-total and right-total, a stereo Pro Logic mix): Reduces the stream to two channels. The center channel is reduced 3dB, the surround channels are added together to create a single signal and reduced 6dB, and the LFE is muted. The surround signal is added 180 degrees out of phase to the left-and-center signal, making up the left-total channel. The surround signal is added _in_ phase (0 degrees) to the right-and-center signal, making up the right-total channel.

- **Lo Ro** (left-only and right-only, a stereo only downmix): Reduces the stream to two channels. The center channel is reduced 3dB, both surround channels are reduced 3dB, and LFE is muted. The center channel is added to the left-and-left-surround signal to make the left-only channel. The center channel is added to the right-andright-surround signal to make the right-only channel.

- **Mono** : Reduces the stream to one channel. The center channel is reduced 3dB, the surround channels are each reduced 3dB, and the LFE is muted. All six channels are combined.

If the audio program is configured for 5.1 or above, a button in the Volume controls, in the status bar, is marked as Downmix.

## **Audio Controls**

**==> picture [425 x 117] intentionally omitted <==**

**----- Start of picture text -----**<br>
Audio<br>Mute Balance Volume<br>Device<br>Audio<br>Downmix<br>Sources<br>= LL<br>**----- End of picture text -----**<br>

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Functions 201** Capture |

Audio control features and descriptions

| **Option**       | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mute             | Mute or unmute audio                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Balance          | Left and right balance control of selected audio pair                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Volume           | Volume control of selected audio pair                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Audio<br>device  | Output audio device to control. This can be headphones using the audio<br>ports or USB inputs. The name of the audio device in the list depends on<br>what port is used and the device itself:<br>**•**Headphones: Headphones plugged into the front or rear panel audio<br>ports<br>**•**If a USB audio device supports device descriptors, the vendor supplied<br>device name appears in the list.<br>**•**Unknown: Unidentified audio device plugged into the front or rear<br>panel USB ports |
| Downmix          | Audio channel group to monitor channels mixed down to stereo or<br>mono (visible when only Program Configuration is on and set)                                                                                                                                                                                                                                                                                                                                                                   |
| Audio<br>sources | Audio channels available to monitor                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

- **WARNING: To avoid damaging your hearing, always turn the volume down to the minimum before you put on headphones and then turn the volume up slowly.**

## **Capture**

The Capture feature has two modes: Screenshot and Stream.

- Screenshot capture takes an image of the entire screen and saves it internally or to a USB drive.

- Stream capture creates a PCAP file capturing up to 2 GB of data internally or on a USB drive for further analysis. Both modes are useful for comparing sources or capturing transient events.

The requirements to use the Capture feature are as follows:

- MPSDP-IP-MEAS option installed; and

- USB 3.0 drive connected to the rear panel of the PRISM monitor. Alternatively, for
  - remote download to a client PC, select the **Settings** icon ( ), and then select **Capture** and **Internal Storage** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **202 Functions** Capture

**Note:** For the fastest capture rate with the Stream Capture, we recommend using a USB 3.0 drive, plugged into one of the USB 3.0 ports on the rear panel of the instrument. Using a USB 2.0 drive or USB 2.0 ports can cause the stream capture to take longer.

Maximum stream capture PCAP files are approximately 2 GB in size.

## **Capture Screenshot**

## **1.** From the **Settings** menu, select **Capture** .

**Note:** If the Capture configuration menu does not appear under the Settings menu, option MPSDP-IP-MEAS is not installed, but screen captures are still functional.

**2.** Select **Screenshot** under SELECT CAPTURE TYPE.

**3.** In the SELECT CAPTURE DESTINATION section, select one of the following:

- **Internal Storage** – to save internally for remote download; or

- **USB Drive** – to save the file to a USB drive.

**4.** On the application bar, select the **Capture** icon ( ).

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Functions 203** Capture

- A screenshot is saved to the capture destination that you selected.

**5.** To download an internally saved screenshot:

- **A.** Enter the hostname or IP address from the instrument in a web browser. See _Find or Change Hostname, Password, and IP Address_ . The PRISM HOME page appears.

- **B.** Select **Capture / Firmware / Diagnostics** . The Capture / Firmware / Diagnostics page appears.

- **C.** Select **Screenshot** to begin downloading the file.

- **D.** The capture file will be downloaded to the standard download directory determined by the computer and browser you are using.I

**Note:** You can also use the API command http://aaa.aaa.aaa.aaa/api/ downloadScreenshot to download the capture file.

## **Perform Stream Capture**

**1.** Select the **Settings** icon ( ) and then select **Capture** . If the Capture configuration menu does not appear under the Settings menu, option MPSDP-IPMEAS is not installed and stream captures are disabled.

**2.** Select **Screenshot and Stream** under SELECT CAPTURE TYPE.

**3.** Select the **Port to Capture** menu and select from inputs (10/25GE SFP) 1 or 2. When capturing on a port configured for 25-Gb data rate, the maximum total bit rate on the port must be less than 15 Gbps. Data packets captured in the PCAP file might be dropped if the total bit rate exceeds this limit.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **204 Functions** Capture

## **4.** In the **Stream Size (MB)** box, set the size of the capture.

**Note:** The minimum stream size is 1MB and the maximum size is 2000 MB.

**5.** Select the **Close** icon ( ).

**6.** In the SELECT CAPTURE DESTINATION section, select one of the following:

- **Internal Storage** – to save internally for remote download; or

- **USB Drive** – to save the file to a USB drive. Verify there is a USB drive connected to the PRISM monitor.

**7.** On the application bar, select the **Capture** icon ( ) to start the process. When the capture type is Screenshot and Stream, a percentage is displayed under the Capture icon.

**Note:** During capture, the Aux Out signal is turned off, and Pictures and Traces are blanked.

**Note:** Select the Capture icon again to stop the stream capture early. The Capture icon is the only element you can interact with on the PRISM monitor while the capture and save are taking place.

A screenshot and pcap file are saved to the selected destination, either Internal or USB storage. The name of the file and the path to the file on the USB drive are displayed after the save is complete.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Functions 205** Capture |

**8.** Select **OK** to close the menu.

**9.** To download an internally saved screenshot or stream:

- **A.** Enter the hostname or IP address from the instrument in a web browser. See _Find or Change Hostname, Password, and IP Address_ . The PRISM HOME page appears.

- **B.** Select **Capture / Firmware / Diagnostics** . The Capture / Firmware / Diagnostics page appears.

**C.** Select **Screenshot** or **Stream** to begin downloading the file.

**D.** In the dialog box that appears, navigate to a local directory and save the file.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **206 Application Information** Application Options

## **Application Information**

This chapter describes the monitoring and measurement applications available on the PRISM monitor. Each of these applications can be viewed in quarter-screen, half-screen, or full-screen mode; double-tap in the application to change between modes.

To view the All Applications menu, select the **Tiles** icon ( ) and then select the **All Applications** menu icon ( ).

**Note:** Some displays require a specific option to be installed. For example, the IP Graph display is not accessible unless you have Option MPSDP-IP-MEAS.

## **Application Options**

This section describes the application groups.

## **Base Instrument Applications**

Unless otherwise noted, these applications are available on every PRISM monitor:

**Note:** The SD; HD 720p, 1080p, and 1080i; and 3G Level A formats can display up to eight trace applications at a time. All other formats can display up to four trace applications at a time. The trace applications are Waveform, Vector, Stop, Diamond, Lightning, and CIE.

## **Application Icon Description**

_Waveform Application_ : View the voltage versus time display of the video signal.

_Vector Application_ : Call up the Vector, which plots color difference signals for viewing hue and amplitude, but not luminance.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 207** Application Options

| **Application Icon** | **Description**                                                   |
| -------------------- | ----------------------------------------------------------------- |
|                      | _Lightning Application_: View luma and chroma amplitudes and      |
|                      | verify component timing using a color-bar signal.                 |
|                      | _Diamond Application_: Detect invalid colors.                     |
|                      | _Picture Application_: View the picture decoded from the          |
|                      | incoming video signal.                                            |
|                      | _Video Session Application_: View information about the format    |
|                      | of the signal and metrics for SDI Format, VPID ST 352, Bit Level, |
|                      | and CRC Status.                                                   |
|                      | _Audio Application_: View audio bar levels for the monitored      |
|                      | signal with Test Level and Peak Program indicators. (Lissajous    |
|                      | display and Channel Correlation meter for monitoring two-         |
|                      | channel audio phase and Audio session require Option              |
|                      | MPSDP-AUD.)                                                       |
|                      | _Event Log Application_:View a log of detected errors.            |
|                      | _IP Status Application_:See an overview of the monitored IP       |
|                      | stream and see the status of each program in the stream. This     |
|                      | application is available only in the 200 and 300 versions of the  |
|                      | MPS, MPD, and MPP.                                                |
|                      | _Timing Application_:View timing offsets between the incoming     |
|                      | SDI video signals and Black Burst / Tri-Level Sync external       |
|                      | reference signals.                                                |
|                      | _Eye Application_:View an eye pattern diagram of the SDI input    |
|                      | only. This application is available only in the 200 and 300       |
|                      | versions of the MPS, MPD, and MPP.                                |

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **208 Application Information** Application Options

**Application Icon Description** _Jitter Application_ : View the wave shape of the jitter and additional time-domain information. This application is available only in the 300 version of MPS, MPD, and MPP.

_External Reference Application_ : Check the analog reference signal is the correct type, amplitude, and acceptable signal integrity.

_IP Display Application_ : Use the Display application to send the tiled PRISM display as an ST 2110 stream for multiviewer applications. This application is available only in the 200 and 300 versions of MPS, MPD, and MPP.

## **Option MPSDP-PROD**

This supports SDI and ST 2110 Deep Color formats, see tables _Supported SDI Formats_ and _Supported Video Formats in ST 2110-20 Streams_ . It also supports this feature and these additional applications, which are available when option MP2-PROD is installed, unless otherwise noted:

**Convert to Rec. 709** : This feature adds a setting to allow the trace displays to convert camera logs to Rec. 709.

## **Application Icons Description**

_Stop Display Application_ : Monitor video signals with a variety of transfer functions in a consistent manner. This is also required for the Stop display type in the Cam application.

_CIE Application_ : Check the chromaticity of the video against various color gamut limits.

**Application Icons Description** _CAM Application_ : Check the color levels and balances between up to four camera inputs.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 209** Application Options

## **Option MPSDP-MULTI**

This option enables you to monitor up to four SDI, ST 2110-20 or ST 2110-22 JPEG XS (available when option MP2-JPXS is installed) inputs. Without this option, you can monitor only one input at a time.

## **Option MPSDP-JPXS**

This option enables you to monitor ST 2110-22 JPEG XS inputs and adds a tab to the Video Session application if the current input is JPEG XS.

## **Option MPSDP-AUD**

These additional applications are available when Option MPSDP-AUD is installed:

**Application Icons Description** _Audio Application_ : Adds Lissajous, Session, Correlation, and Loudness capabilities to the existing Audio application.

_Dolby Status Application_ : View metadata content in the selected Dolby audio stream. _AES Channel Status Application_ : View AES data related to the SDI input audio channels.

## **Option MPSDP-DLBY**

This option enables full decoding of Dolby E, D, and D Plus signals. It also enables decoding of ED2 metadata.

## **Option MPSDP-ENG-QC**

Unless otherwise noted, these additional applications are available when option MPSDP-ENG-QC is installed:

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **210 Application Information** Application Options

## **Application Icons**

## **Description**

_Picture Application_ : Decode and display closed captions or subtitles in CEA 608, CEA 708, OP47/ST2031, and ARIB B24 to the existing Picture application.

_Datalist Application_ : View the digital data in SDI frames to perform in-depth monitoring and analysis of incoming SDI data.

_ANC (Ancillary Data) Session Application_ : Monitor all ancillary data present in a signal.

_Audio-Video Delay Application_ : Measure the audio-to-video synchronization (lip sync) when using a Flash Pop test sequence that can be generated from the Telestream Sync Pulse Generator.

## **Option MPSDP-IP-MEAS**

These additional applications and feature are available when option MPSDP-IP-MEAS is installed, unless otherwise noted. These applications are available only in the 200 and 300 versions of the MPS, MPD, and MPP.

**IP Stream Capture** : This feature allows the capture IP streams to a PCAP file. The maximum capture size is 2 GB, which allows for the capture of 10 seconds of HD video.

**Application Icons Description** Oo _IP Session Application_ : View performance parameters of the IP Oo stream, including Layer 2, video, and PTP parameters. IP Session _IP Graphs Application_ : View trend graphs of various performance parameters of the IP stream including total bit rate, session bit rate, PIT, RTP sequence errors, video CRC errors, IP Graphs and TS-DF (Time Stamped Delay Factor). | _PIT Histogram Application_ : View a histogram of the PIT (Packet Interval Time) to monitor network delay variation statistics. ellisil

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 211** Application Options

_PTP Graphs Application_ : View trend graphs of various performance parameters of the PTP signal include leader-tofollower and follower-to-leader delays and variances.

_Stream Timing Application_ : View the timing of the ST 2110 video, audio, and data as it was received relative to the embedded RTP time stamps.

_Timing Application_ (for IP signals): Adds features to the standard Timing application, including viewing timing offsets between the incoming ST 2022-6 and ST 2110-20 video signals and PTP signals.

## **Option MPSDP-GEN**

Unless otherwise noted, these additional applications are available when option MPSDP-GEN is installed:

## **Application Icons Description**

_IP Generator Application_ : Use the Generator function to send an ST 2110 test stream for checking a receiver device and signal path. Alternately, use the Display function to send the tiled PRISM display as an ST 2110 stream for multiviewer applications. This application is available only on the 200 and 300 versions of MPS, MPD, and MPP.

_SDI Generator Application_ : Provides an SDI test signal to check the receiver device and signal path.

## **Option MPSDP-EXTNDSP**

This option enables using eight separate tiles; a second monitor is required. Without this option, you can use only four tiles and a second monitor duplicates the four tiles on the first monitor.

## **View Installed Options**

To view options installed on the instrument, click the **Settings** icon ( ), click **Utilities** , and then click **Options** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **212 Application Information** Waveform Application

## **Status Indicators**

Many application displays include status icons, which provide a quick method for viewing signal status.

T signal parameter has not been in an error condition.

! The signal parameter was in an error condition but the error has cleared.

The signal parameter is in an error condition.

The signal parameter is not being monitored for an error condition.

## **Waveform Application**

The Waveform display is a signal-level-versus-time display of the video signal.

## **Configure the Waveform Application**

**1.** Select the **Tiles** icon ( ).

**2.** Select the tile with the Waveform application.

**3.** Select the **Tile** icon ( ).

**Note:** To move the settings left or right, select the **Move** icon ( ) in the Settings menu header.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 213** Waveform Application

**4.** To view a picture thumbnail within the Waveform tile, set **Picture Display** to **On** . In multi-input mode, you can monitor up to four inputs. For more information about multi-input mode, see _Multiple Inputs Mode_ . To view the full waveform display without the thumbnail, set **Picture Display** to **Off.**

**5.** In the **Trace Appearance** section, select one of the following to change the colors of the parade traces:

- **Monochrome:** Display all traces in a conventional green.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **214 Application Information** Waveform Application

- **Color:** Display the components of the traces in the colors described in the Display Mode. For example, the components in RGB mode are shown in red, green, and blue.

**Note:** The Color setting works only when Display Style is set to Parade. The Overlay mode displays the traces in green.

**6.** In the **Display Style** section, select the way signal components are displayed in the active tile:

- **Parade:** All components are shown beside each other. This setting allows the traces to appear in the described colors.

- **Overlay:** All components are drawn at the same location so they appear on top of each other. This trace is displayed in green.

**7.** From the **Sweep** list, select the waveforms to view between the lines or fields. The options depend on the active display style.

- When the Parade display style is active, you can select **1 line** or **1 field** .

- When Overlay display style is active, you can select **1 line** , **2 line** , **1 field** , or **2 field** .

**8.** In the **Display Mode** list, select the display mode (available only while displaying SDI inputs):

- **Y** : Displays the input as White (Y) for the Luma component. This display is the YRGB mode with the Red (R), Green (G), and Blue (B) components turned off.

- **RGB** : Displays the input as R, G, and B components.

- **YPbPr** : Displays the input as Y for the Luma component, and color difference Cyan (Pb) and Magenta (Pr) components.

- **YRGB** : Displays the input as Y, R, G, and B components.

**9.** Waveform filters are useful for isolating a specific characteristic of the input. For example, you can enable a Low Pass filter for quick camera exposure setting. In the **Filter** section, select a waveform filter:

- **Flat** : Display the full available bandwidth.

- **Low Pass** : Display only the low frequency part of the signal.

**10.** From the **Graticule** list, select a vertical scale value.

In the Waveform display application, select the **Graticule** menu to choose the graticule that fits your need. The trace represents the video data in the vertical axis.

- The mV, %, and Code Value are fixed graticules. They are compatible with the traditional waveform scales.

- The Reflectance and Stop graticules vary depending on the Gamma selection in the Input Settings menu. These are the Scene light graticules that are used for scene setting and camera exposure adjustment.

- The Nits graticule varies depending on the Gamma selection in Input Settings menu. This is the Display light graticule and is used for mastering the content for a targeted HDR system.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 215** Waveform Application

**11.** Set **3D LUT: Convert to Rec. 709** to **On** to allow trace displays to convert the Gamma and Color Gamut settings for the signal to SDR Narrow and BT. 709 or use a custom Favorite LUT.

**Note:** To automatically convert settings to BT.709, set **3D LUT: Convert to Rec. 709** to **On** ; if it is not on, you must manually change the graticule selection. (See _Configure Instrument for HDR/WCG Monitoring_ .) Convert to Rec. 709 mode is not supported for SD signals.

**12.** Set **Line Select** to **On** to select 1 Line or **Off** to select All Lines. When Line Select is set to On (Line Select: Line 1), the display shows only results for the selected line in the picture. You can use on-screen tools to select the line; see _Line Select Function_ . Alternatively, you can select the line directly on the Picture.

**13.** To remove the trace of vertical and horizontal blanking data, set **Show Active Area Only** to **On** . When Show Active is enabled, for a one-line waveform sweep the

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **216 Application Information** Waveform Application

width of the waveform trace and alignment matches the width and offset of the Picture application.

**14.** In the **Gain** section, select **x1** , **x2** , **x5** , or **x10** .

**15.** In the **Magnification** section, select **Best** , **x1** , **x10** , **x20** , **x25** , or **x50** .

## **Waveform Application On-screen Tools**

Using the on-screen tools, you can change the gain, horizontal position, vertical position, gamma LUT, cursors, display mode, display format, and selected line without opening the Waveform Settings menu. Select the button for the setting you want to adjust. All the available tools are located on the top and bottom of the display and are highlighted for a few seconds when the application is first opened or if you select in the tile heading.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 217** Waveform Application

## **Gain**

To increase or decrease the magnification of the trace display:

**1.** Select **Gain** .

**2.** Select one of the preset magnifications for fixed gain.

**3.** Select **Gain** (the number varies); select **VAR: Off** to change it to **VAR: On** . Variable gain allows flexibility in changing the gain factor between 0.5x to 20.0x.

The limits of the variable gain change depend on the gain factor you select.

- 1.0x has a range of 0.25x to 4.00x gain.

- 2.0x has a range of 0.50x to 8.00x gain.

- 5.0x has a range of 1.25x to 20.00x gain.

- 10.0x has a range of 2.50x to 40.00x gain.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **218 Application Information** Waveform Application

To adjust the gain:

- On a touchscreen, pinch to change the scale of the trace for large increments.

- For single increments, select the **Plus** (+) button or **Minus** (-) button to adjust the gain.

- Use the scroll wheel on a mouse to adjust the variable gain.

- Select the **Reset** icon ( ) to remove variable gain adjustments.

## **Horizontal and Vertical Position**

Adjust the position of the trace display.

**1.** Select the **H Pos** button to allow incremental adjustment of the horizontal trace.

- Select and drag to move the trace on the touchscreen. This method can be performed without using the button.

- Use a mouse scroll wheel to move the trace.

- For incremental adjustments, select the **Plus** (+) button or **Minus** (-) button to adjust the horizontal position.

- Select the **Reset** icon ( ) to reset the horizontal position adjustment to default.

**2.** Select the **V Pos** button to adjust the vertical trace.

- Select and drag to move the trace on the touchscreen. This method can be performed without using the button.

- Use a mouse scroll wheel to move the trace.

- For incremental adjustments, select the **Plus** (+) button or **Minus** (-) button to adjust the vertical position.

- Select the **Reset** icon ( ) to reset the vertical position adjustment to default.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 219** Waveform Application

## **Gamma LUT**

Turn the Gamma LUT on or off:

**1.** Select the **LUT** button (other elements in the button are variable depending on the options selected) in the top middle of display.

**2.** Select the lower **LUT:** button to turn on/off the 3D LUT for this tile. If a custom LUT is selected, the name is indicated if it is enabled.

To change the gamma curve and color gamut (displayed in the LUT button):

**1.** Select the **Settings** icon ( ).

**2.** Select **Inputs** and select the input being used.

**3.** Select **SDI** and **VIDEO** .

**4.** From the **Gamma Curve** list, select one of the following; the selection characterizes the video signal on each virtual input.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **220 Application Information** Waveform Application

- **Auto:** The system selects the setting based on ST 352 VPID. If 352 VPID is not present, SDR Narrow is selected.

- **SDR Narrow:** The reference OETF (Optical to Electrical Transfer Function) is defined in ITU-R BT.709 with gamma of 0.45 and the reference EOTF is defined in ITU-R BT.1886 with gamma of 2.4.

The Narrow scaling places the extremes of the nonlinear color value from zero to unity at code words 40 hex (64 dec) and 3AC hex (940 dec) in a 10-bit representation for 0% Black to 100% White. This range is typical for standard-dynamic range.

- **SDR Full:** The reference OETF is defined in ITU-R BT.709 with gamma of 0.45 and the reference EOTF (Electrical to Optical Transfer Function) is defined in ITU-R BT.1886 with gamma of 2.4.

The full scaling places the extremes of the nonlinear color value from zero to unity at code words 0d and 1023d in 10-bit representation and 0d and 4095d in 12-bit representation for 0% black and 100% white, respectively.

- **PQ Narrow:** The reference OETF with a high luminance range capability of 0 to 10,000 cd/m[2] standardized in ST 2084. The EOTF is the inverse of OETF.

The narrow scaling places the extremes of the nonlinear color value from zero to unity at code words 40 hex (64 dec) and 3AC hex (940 dec) in a 10-bit representation for 0% Black to 100% White. This range is typical for standard-dynamic range.

- **PQ Full:** The reference OETF with a high luminance range capability of 0 to 10,000 cd/m[2] standardized in ST 2084. The EOTF is the inverse of OETF.

The full scaling places the extremes of the nonlinear color value from zero to unity at code words 0d and 1023d in 10-bit representation and 0d and 4095d in 12-bit representation for 0% black and 100% white, respectively.

- **HLG:** The reference OETF is standardized in ARIB B67 and the reference EOTF is standardized in ITU BT.2100 at the nominal display peak luminance of 1000 nits.

- **S-Log2:** The reference OETF is defined as Sony S-Log2.

- **S-Log3:** The reference OETF is defined as Sony S-Log3.

- **S-Log3 (Live HDR):** The reference OETF and OOTF (Optical to Optical Transfer Function) are defined as Sony S-Log3 (Live HDR).

- **Log C:** The reference OETF is defined as ARRI Log C.

**5.** From the **Structure** list, select one of the following **:**

- Auto: The system selects the setting based on ST 352 VPID. If VPID is not present, YCbCr 4:2:2 10bit is selected.

- YCbCr 4:2:2 10bit

- YCbCr 4:2:2 12bit

- YCbCr 4:4:4 10bit

- RGB 4:4:4 10bit

- RGB 4:4:4 12bit

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 221** Waveform Application

**6.** From the **Color Gamut** list, select one of the following; the selection determines the color space of the video signal selection.

- **Auto:** The system selects the setting based on ST 352 VPID. If ST 352 VPID is not present, Rec. 709 is selected.

- **Rec. 709:** Standard for HD

- **Rec. 2020:** Standard for 4K

**7.** From the **Favorite 3D LUTs** list, select a 3D LUT.

> To save a 3D LUT as a favorite, select the Information icon ( Lt ) and select the star beside a LUT.

**8.** Select **Save** .

## **Cursor Measurement**

To make precise measurements with time and voltage cursors:

**1.** Select the **Cursors** button in the top right of the tile to show the time and voltage cursor options.

**2.** Select the **T: Off** button to display two cursors. Select **T: On** to hide the two cursors. To select the type of cursor to display, select the **T Units** button, and then select the cursor type.

- To display time cursors, select the **time** button.

- To display pixel cursors, select the **pixel** button.

Select and hold anywhere on the cursors to move them and mark exact times or pixels in the trace. The cursors are highlighted in yellow when moved. The time stamp or number of pixels of each cursor and the delta are displayed on the right side of the application. With the use of Show Active Area Only and a picture tile above or below the waveform trace, you can correlate a specific region in the image to a part of the waveform trace using the cursors in the waveform for guidance.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **222 Application Information** Waveform Application

**Note:** The cursor tab provides an easy way to adjust each cursor.

Pixel cursors are available only if show active area mode is on and the sweep is only 1 line overlay or 1 line single component parade.

**3.** Select the **V: Off** button to display two voltage cursors. Select **V: On** to hide the two cursors.

**4.** Select the **V Units** button to change the voltage units between percentage (%), millivolts (mV), or code value (CV). The selected option (%, mV, or CV) is added to the button title.

**5.** Select and hold anywhere on the V1 or V2 cursor to move the cursor and mark exact times in the trace. The cursors are highlighted in yellow when moved. The voltage measurement at each cursor and the delta are displayed on the right side of the application.

**6.** Select the **Cursors** button to hide the T and V buttons.

**Note:** The time, pixel, and voltage cursor positions are retained if the trace is moved horizontally or vertically, or if the gain is adjusted.

## **Display Mode**

To change how the waveforms are displayed:

**1.** Select the button in the bottom left corner of the application to expand the available display options (the button label varies depending on the last option selected).

**2.** Select a waveform display option:

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 223** Waveform Application

- Select **YPbPr** to display any combination of the Y, Pb, and Pr components.

- Select **RGB** to display any combination of the R, G, and B components.

- Select **YRGB** to display any combination of the Y, R, G, and B components.

**3.** Select the components to monitor:

- To remove a component, select the letter of the component from the waveform list. For example, to remove the green component from the waveform, select G in RGB.

- To make a removed component visible, select the letter of the component.

## **Display Format**

To change the Display Style, Sweep, and Magnification of the waveform:

**1.** Select the button in the bottom right corner of the application to expand the available display format options (the button label varies depending on the last option selected).

**2.** Select **Mag** and then select the magnification: **Best** , **1.0x** , **10.0x** , **20.0x** , or **25.0x** .

**3.** Select the **Display Style** option to switch between **Parade** and **Overlay** .

**4.** Select the **Sweep** options as needed. The options depend on which Display Style is active.

- When the Parade display style is active, you can select **1 line** or **1 field** .

- When Overlay display style is active, you can select **1 line** , **2 line** , **1 field** , or **2 field** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **224 Application Information** Waveform Application

## **Line Select Function**

You can select a single picture line to monitor in the display. By default, All Lines is selected and all lines are monitored.

**Note:** If you enable Line Select, the same line is selected in any trace display.

To turn on Line Select and choose the line to monitor:

**1.** Select the **Lines** button at the bottom of the tile.

**2.** Select **1 Line** .

- To scroll through lines, select the **Plus** (+) button or **Minus** (-) button.

- To enter a specific line to monitor:
  - ♦ select **Line Sel.** and enter the line on the keypad; or

  - ♦ in the Picture application, use the line-select cursor (for active lines).

Depending on the resolution in the signal, the Line Select provides different information.

- If a signal is SD, HD, 3G:
  - ♦ the Line number is the selected line, including vertical blanking,

  - ♦ if the signal is interlaced format, the Fields readout is below the Line number,

  - ♦ the Pic Line number is next to Line; the Pic Line is the active line number, or numbers, selected.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 225** Vector Application

- If a signal is UHD, 4K:
  - ♦ the Line number is the selected raster line,

  - ♦ the SDI Line is the selected line including vertical blanking,

  - ♦ the link number appears below the SDI Line.

**Note:** In link, the letters (A, B, C, or D) refers to the physical links. The numbers (1, 2, 3, or 4) refer to the virtual links. For example, A3/62 indicates it is physical link 1 and virtual link 3 (in a two-sample interleave, 12G transport).

## **Vector Application**

The Vector application provides an X-Y plot of color difference signals, allowing the operator to match skin tones and color of ITU-R BT 709 or 2020 color space. With Option MPSDP-PROD, transfer function/color space conversion allows for an ITU-R BT 709 color space to verify wide color-gamut compatibility.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **226 Application Information** Vector Application

## **Configure the Vector Application**

**1.** Select the **Tiles** icon ( ).

**2.** Select the tile with the Vector application.

**3.** Select the **Tile** icon ( ).

**Note:** To move the settings left or right, select the **Move** icon ( ) in the Settings menu header.

**4.** In the **Bar Targets** section, select **75%** or **100%** scaling.

**5.** Select **IQ Axis** to turn the IQ Axis on or off.

**Note:** This is only for inputs configured for Rec. 709 Color Gamuts.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 227** Vector Application

**6.** Select **SDI Compass Rose** to turn the compass in the Vector tile on or off.

**7.** In the **Gain** section, select the trace vector magnifications: **1.0x** , **2.0x** , **5.0x** , or **10.0x** .

**8.** If you set **3D LUT: Convert to Rec. 709** to **On** , the trace displays to convert the Gamma and Color Gamut settings for the signal to SDR Narrow and BT. 709 (requires Option MPSDP-PROD).

**9.** Select the lower **LUT:** button to turn on/off the 3D LUT for this tile. If a custom LUT is selected, the name is indicated if it is enabled.

**Note:** To automatically convert settings to BT.709, set **3D LUT: Convert to Rec. 709** to **On** ; if it is not on, you must manually change the graticule selection. (See _Configure Instrument for HDR/WCG Monitoring_ .) Convert to Rec. 709 mode is not supported for SD signals.

**10.** In the **Line Select** section, choose the picture lines to monitor in the display: **All Lines** or **1 Line** . If you select 1 Line, then the display shows only results for the selected line in the picture. You can use on-screen tools to select the line; see _Line Select Function_ . Alternatively, you can select the line directly on the Picture.

## **Vector Application On-screen Tools**

You can change the gain, horizontal position, vertical position, gamma LUT, selected line, and bar targets without opening the Vector settings menu through on-screen tools. Select the button for the setting you want to adjust. The available tools are on the top and bottom of the display. They are highlighted for a few seconds when the application is first opened or if you select anywhere in the middle of the application tile.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **228 Application Information** Vector Application

## **Gain**

To increase or decrease the magnification of the trace display:

**1.** Select **Gain** (the number varies) in the trace tile to open the magnification menu.

**2.** Select one of the preset magnifications for fixed gain.

- On a touchscreen, you can pinch to change the scale of the trace for large increments.

**3.** Select **VAR:** (On or Off) to turn the variable gain on or off.

- Variable gain (VAR: On) allows you to change the gain factor (Var Gain) in 0.01 increments.

**4.** Select the **Plus** (+) button or **Minus** (-) button under Var Gain as needed to make detailed adjustments to the variable gain.

The limits of the variable gain depend on the gain factor you select.

- 1.0x has a range of 0.25x to 4.00x gain.

- 2.0x has a range of 0.50x to 8.00x gain.

- 5.0x has a range of 1.25x to 20.00x gain.

- 10.0x has a range of 2.50x to 40.00x gain.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 229** Vector Application

Select the **Reset** icon ( Reset ) to remove variable gain adjustments and reset the gain to 1.00 and 1.0x.

## **Horizontal and Vertical Position**

To adjust the position of the trace display:

**1.** Select **H Pos** to allow adjustment of the horizontal trace.

- Select-and-drag to move the trace on the touchscreen. This method can be performed without using the button.

- Use a mouse scroll wheel to move the trace.

- For small changes, select the **Plus** (+) button or **Minus** (-) button to adjust the horizontal position.

- Select the **Reset** icon ( ) to reset the horizontal position adjustment to default.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **230 Application Information** Vector Application

**2.** Select **V Pos** to allow adjustment of the vertical trace.

- Select-and-drag to move the trace on the touchscreen. This method can be performed without using the button.

- Use a mouse scroll wheel to move the trace.

- For incremental adjustments, select the **Plus** (+) button or **Minus** (-) button to adjust the vertical position.

- Select the **Reset** icon ( ) to reset the vertical position adjustment to default.

## **Gamma LUT**

Turn the Gamma LUT on or off:

**1.** Select the **LUT** button (other elements in the button depend on the options selected) in the top middle of display.

**2.** Select the lower **LUT:** button to turn on/off the 3D LUT for this tile. If a custom LUT is selected, the name is indicated if it is enabled.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 231** Vector Application

To change the gamma curve and color gamut (displayed in the LUT button):

**1.** Select the **Settings** icon ( ).

**2.** Select **Inputs** and select the input being used.

**3.** Select **SDI** and **VIDEO** .

**4.** Select the **Gamma Curve** menu and select the option. The selection characterizes the video signal on each virtual input.

- **Auto:** The system selects the setting based on ST 352 VPID. If 352 VPID is not present, SDR Narrow is selected.

- **SDR Narrow:** The reference OETF (Optical to Electrical Transfer Function) is defined in ITU-R BT.709 with gamma of 0.45 and the reference EOTF is defined in ITU-R BT.1886 with gamma of 2.4.

The Narrow scaling places the extremes of the nonlinear color value from zero to unity at code words 40 hex (64 dec) and 3AC hex (940 dec) in a 10bit representation for 0% Black to 100% White. This range is typical for standard-dynamic range.

- **SDR Full:** The reference OETF is defined in ITU-R BT.709 with gamma of 0.45 and the reference EOTF (Electrical to Optical Transfer Function) is defined in ITU-R BT.1886 with gamma of 2.4.

The full scaling places the extremes of the nonlinear color value from zero to unity at code words 0d and 1023d in 10bit representation and 0d and 4095d in 12-bit representation for 0% black and 100% white, respectively.

- **PQ Narrow:** The reference OETF with a high luminance range capability of 0 to 10,000 cd/m[2] standardized in ST 2084. The EOTF is the inverse of OETF.

The narrow scaling places the extremes of the nonlinear color value from zero to unity at code words 40 hex (64 dec) and 3AC hex (940 dec) in a 10bit representation for 0% Black to 100% White. This range is typical for standard-dynamic range.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **232 Application Information** Vector Application

- **PQ Full:** The reference OETF with a high luminance range capability of 0 to 10,000 cd/m[2] standardized in ST 2084. The EOTF is the inverse of OETF.

The full scaling places the extremes of the nonlinear color value from zero to unity at code words 0d and 1023d in 10-bit representation and 0d and 4095d in 12-bit representation for 0% black and 100% white, respectively.

- **HLG:** The reference OETF is standardized in ARIB B67 and the reference EOTF is standardized in ITU BT.2100 at the nominal display peak luminance of 1000 nits.

- **S-Log2:** The reference OETF is defined as Sony S-Log2.

- **S-Log3:** The reference OETF is defined as Sony S-Log3.

- **S-Log3 (Live HDR):** The reference OETF and OOTF (Optical to Optical Transfer Function) is defined as Sony S-Log3 (Live HDR).

- **Log C:** The reference OETF is defined as ARRI Log C.

**5.** Choose the **Structure** option from the menu:

- **Auto:** The system selects the correct setting based on ST 352 VPID. If 352 VPID is not present, YCbCr 4:2:2 10bit is selected.

- YCbCr 4:2:2 10bit

- YCbCr 4:2:2 12bit

- YCbCr 4:4:4 10bit

- RGB 4:4:4 10bit

- RGB 4:4:4 12bit

**6.** Choose the **Color Gamut** option from the menu. This selects the color space of the video signal selection.

- **Auto:** The system selects the setting based on ST 352 VPID. If ST 352 VPID is not present, Rec. 709 is selected.

- **Rec. 709:** Standard for HD

- **Rec. 2020:** Standard for 4K

**Note:** Rec. 709 gamut is selected automatically when the SD format is detected / selected in the video signal.

**7.** From the **Favorite 3D LUTs** list, select a 3D LUT.

> To save a 3D LUT as a favorite, select the Information icon ( 0 ) and select the star beside a LUT.

**8.** Select **Save** . The LUT button updates to match your selections.

## **Bar Targets**

To change the scaling of the Vector display:

**1.** Select the **Bars** button in the bottom right corner of the application to expand the available options.

**2.** Select **75%** or **100%** scaling.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 233** Vector Application

## **Line Select Function**

By default, all picture lines are monitored in the display. You can select a single picture line to monitor.

**Note:** If you enable line select, the same line is selected in any trace display.

To turn on Line Select and choose the line to monitor:

**1.** Select the **Lines** button at the bottom of the tile.

**2.** Select **1 Line** .

- To scroll through lines, select the **Plus** (+) button or **Minus** (-) button.

- To enter a specific line to monitor:
  - ♦ select **Line Sel.** and enter the line on the keypad; or

  - ♦ in the Picture application, use the line-select cursor (for active lines).

Depending on the resolution in the signal, the Line Select provides different information.

- If a signal is SD, HD, 3G:
  - ♦ The Line number is the selected line, including vertical blanking,

  - ♦ If the signal is interlaced format, the Fields readout is below the Line number,

  - ♦ The Pic Line number is next to Line; the Pic Line is the active line number, or numbers, selected.

- If a signal is UHD, 4K:
  - ♦ The Line number is the selected raster line,

  - ♦ The SDI Line is the selected line including vertical blanking,

  - ♦ The link number appears below the SDI Line.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **234 Application Information** Lightning Application

**Note:** In link, the letters (A-D) refer to the physical links. The numbers (1-4) refer to the virtual links. For example, A3/62 indicates it is physical link 1 and virtual link 3 (in a two-sample interleave, 12G transport).

## **Lightning Application**

The Lightning application shows luma and chroma amplitudes and helps verify component timing using a color-bar signal. Using a test signal in component format, this display helps make precise, accurate measurements of interchannel amplitude and timing.

## **Configure the Lightning Application**

**1.** Select the **Tiles** icon ( ).

**2.** Select the tile with the Lightning application.

**3.** Select the **Tile** icon ( ).

**Note:** To move the settings left or right, select the **Move** icon ( ) in the Settings menu header.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 235** Lightning Application

**4.** In the **Bar Targets** section, select **75%** or **100%** scaling.

**5.** In the **V Gain** section, select the vertical gain: **1.0x** , **2.0x** , **5.0x** , or **10.0x** magnification.

**6.** In the **H Gain** section, select the horizontal gain: **1.0x** , **2.0x** , **5.0x** , or **10.0x** magnification.

**7.** Set **3D LUT: Convert to Rec. 709** to **On** to allow trace displays to convert the Gamma and Color Gamut settings for the signal to SDR Narrow and BT. 709 (requires Option MP2-PROD).

**Note:** To automatically convert settings to BT.709, set **3D LUT: Convert to Rec. 709** to **On** ; if it is not on, you must manually change the graticule selection. (See _Configure Instrument for HDR/WCG Monitoring_ .) Convert to Rec. 709 mode is not supported for SD signals.

**8.** Set **Line Select** to **On** to select 1 Line or **Off** to select All Lines. When Line Select is set to On (Line Select: Line 1), the display shows only results for the selected line in the picture. You can use on-screen tools to select the line; see _Line Select Function_ . Alternatively, you can select the line directly on the Picture.

## **Lightning Application On-screen Tools**

You can change the horizontal gain, vertical gain, horizontal position, vertical position, gamma LUT, selected line, and bar targets without using on-screen tools to open the Lightning Settings menu. Select the button for the setting you want to adjust. The available tools are on the top and bottom of the display. They are highlighted for a few seconds when the application is first opened or if you select anywhere in the middle of the application tile.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **236 Application Information** Lightning Application

## **Horizontal and Vertical Gain**

To increase or decrease the magnification of the horizontal and vertical trace displays:

**1.** Select the button at the top-left to open the available options menu.

**2.** Using the **H Gain** and **V Gain** options, select one of the preset magnifications for fixed horizontal and vertical gain.

**3.** From the **Variable Gain** list, select one of the following:

- **VAR: H:** To change the horizontal gain in increments.

- **VAR: V:** To change the vertical gain. Variable gain allows you flexibility in changing the gain factor between 0.5x to 20.0x.

- **Off:** To shut off both gain options.

The limits of the variable gain depend on the gain factor you select.

- ♦ 1.0x has a range of 0.25x to 2.00x gain.

- ♦ 2.0x has a range of 0.50x to 4.00x gain.

- ♦ 5.0x has a range of 1.25x to 10.00x gain.

- ♦ 10.0x has a range of 2.50x to 20.00x gain.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 237** Lightning Application

To adjust the gain:

- With a touchscreen, pinch to change the scale of the trace for large incremental changes.

- For incremental adjustments, select the **Plus** (+) button or **Minus** (-) button.

- Use the scroll wheel on a mouse to adjust the variable gain.

- Select the **Reset** icon ( ) to remove variable gain adjustments.

## **Horizontal and Vertical Position**

To adjust the position of the trace display:

**1.** Select the **H Pos** button to allow adjustment of the horizontal trace.

- Select-and-drag to move the trace on the touchscreen. This method can be performed without using the button.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **238 Application Information** | Lightning Application

- Use a mouse scroll wheel to move the trace.

- For incremental adjustments, select the + (plus) or - (minus) button.

- Select the **Reset** icon ( ) to change the horizontal position adjustment to default.

**2.** Select the **V Pos** button to allow adjustment of the vertical trace.

- Select-and-drag to move the trace on the touchscreen. This method can be performed without using the button.

- Use a mouse scroll wheel to move the trace.

- For incremental adjustments, use the + (plus) or - (minus) button.

- Select the **Reset** icon ( ) to reset the vertical position adjustment to default.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 239** Lightning Application |

## **Gamma LUT**

Turn the Gamma LUT on or off:

**1.** Select the **LUT** button (other elements in the button depend on the options selected) in the top middle of the tile.

**2.** Select the lower **LUT:** button to turn on/off the 3D LUT for this tile. If a custom LUT is selected, the name is indicated if it is enabled.

To change the gamma curve and color gamut (displayed in the LUT button):

**1.** Select the **Settings** icon ( ).

**2.** Select **Inputs** and select the input being used.

**3.** Select **SDI** and then select **VIDEO** .

**4.** Select the **Gamma Curve** menu and choose the setting. The selection characterizes the video signal on each virtual input.

- **Auto:** The system selects the setting based on ST 352 VPID. If 352 VPID is not present, SDR Narrow is selected.

- **SDR Narrow:** The reference OETF (Optical to Electrical Transfer Function) is defined in ITU-R BT.709 with gamma of 0.45 and the reference EOTF (Electrical to Optical Transfer Function) is defined in ITU-R BT.1886 with gamma of 2.4.

The Narrow scaling places the extremes of the nonlinear color value from zero to unity at code words 40 hex (64 dec) and 3AC hex (940 dec) in a 10-bit representation for 0% Black to 100% White. This range is typical for standard-dynamic range.

- **SDR Full:** The reference OETF is defined in ITU-R BT.709 with gamma of 0.45 and the reference EOTF is defined in ITU-R BT.1886 with gamma of 2.4.

The full scaling places the extremes of the nonlinear color value from zero to unity at code words 0d and 1023d in 10-bit representation and 0d and 4095d in 12-bit representation for 0% black and 100% white, respectively.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **240 Application Information** Lightning Application

- **PQ Narrow:** The reference OETF with a high luminance range capability of 0 to 10,000 cd/m[2] standardized in ST 2084. The EOTF is the inverse of OETF.

The narrow Scaling places the extremes of the nonlinear color value from zero to unity at code words 40 hex (64 dec) and 3AC hex (940 dec) in a 10-bit representation for 0% Black to 100% White. This range is typical for standard-dynamic range.

- **PQ Full:** The reference OETF with a high luminance range capability of 0 to 10,000 cd/m[2] standardized in ST 2084. The EOTF is the inverse of OETF.

The Full scaling places the extremes of the nonlinear color value from zero to unity at code words 0d and 1023d in 10-bit representation and 0d and 4095d in 12-bit representation for 0% black and 100% white, respectively.

- **HLG:** The reference OETF is standardized in ARIB B67 and the reference EOTF is standardized in ITU BT.2100 at the nominal display peak luminance of 1000 nits.

- **S-Log2:** The reference OETF is defined as Sony S-Log2.

- **S-Log3:** The reference OETF is defined as Sony S-Log3.

- **S-Log3 (Live HDR):** The reference OOTF is defined as Sony S-Log3.

- **Log C:** The reference OETF is defined as ARRI Log C.

**5.** Select **Color Gamut** settings in the menu. The selection is the color space of the video signal.

- **Auto:** The system selects the setting based on ST 352 VPID. If 352 VPID is not present, Rec. 709 is selected.

- **Rec. 709:** Standard for HD.

- **Rec. 2020:** Standard for 4K.

**6.** From the **Favorite 3D LUTs** list, select a 3D LUT.

To save a 3D LUT as a favorite, select the Information icon ( ) and select the star beside a LUT.

**7.** Select **Save** .

## **Bar Targets**

To change the scaling of the Lightning Display:

**1.** Select **Bars** in the bottom-right corner of the application to expand the available options.

**2.** Select **75%** or **100%** scaling.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 241** Lightning Application |

## **Line Select Function**

By default, all picture lines are monitored in a display. You can select a single picture line to monitor.

**Note:** If you enable line select, the same line is selected in any trace display.

To turn on Line Select (and choose the line to monitor):

**1.** Select the **Lines** button at the bottom of the tile.

**2.** Select **1 Line** .

- To scroll through lines, use the **Plus** (+) button or **Minus** (-) button.

- To enter a specific line to monitor:
  - ♦ select **Line Sel.** and enter the line on the keypad; or

  - ♦ in the **Picture** application, use the line-select cursor (for active lines).

Depending on the resolution in the signal, the Line Select provides different information.

- If a signal is SD, HD, or 3G:
  - ♦ The Line number is the selected line, including vertical blanking.

  - ♦ If the signal is interlaced format, the Fields readout is below the Line number.

  - ♦ The Pic Line number is next to Line; the Pic Line is the active line number, or numbers, selected.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **242 Application Information** Diamond Application

- If a signal is UHD or 4K:
  - ♦ The Line number is the selected raster line.

  - ♦ The SDI Line is the selected line including vertical blanking.

  - ♦ The link number appears below the SDI Line.

**Note:** In link, the letters (A-D) refer to the physical links. The numbers (1-4) refer to the virtual links. For example, A3/62 indicates it is physical link 1 and virtual link 3 (in a two-sample interleave, 12G transport).

## **Diamond Application**

The Diamond application provides a tool for white and black balancing at camera setup and for color gamut adjustment at color editing and QC. For additional information about the Diamond application, see _Check Gamut_ .

## **Configure the Diamond Application**

**1.** Select the **Tiles** icon ( ).

**2.** Select the tile with the Diamond application.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 243** Diamond Application

**3.** Select the **Tile** icon ( ).

**Note:** To move the settings left or right, select the **Move** icon ( ) in the Settings menu header.

**4.** In the **Display Mode** section, select one of the following options:

- **Diamond:** The normal Diamond display shows Gamut violations of the SDI input if translated to RGB color space.

- **Split Diamond:** The split Diamond display offsets the two halves of the Diamond to better see negative RGB Gamut errors.

**5.** Set **3D LUT: Convert to Rec. 709** to **On** to allow the trace displays to convert the Gamma and Color Gamut settings for the signal to SDR Narrow and BT. 709 (requires Option MPSDP-PROD).

**Note:** To automatically convert settings to BT.709, set **3D LUT: Convert to Rec. 709** to **On** ; if it is not on, you must manually change the graticule selection. (See _Configure Instrument for HDR/WCG Monitoring_ .) Convert to Rec. 709 mode is not supported for SD signals.

**6.** Set **Line Select** to **On** to select 1 Line or **Off** to select All Lines. When Line Select is set to On (Line Select: Line 1), the display shows only results for the selected line in the picture. You can use on-screen tools to select the line; see _Line Select Function_ . Alternatively, you can select the line directly on the Picture.

## **Check Gamut**

The diamond display effectively shows how the R, G, and B signals relate. The Diamond display is a good tool for detecting gamut errors.

To form the diamond display, the instrument converts the Y, Pb, and Pr components recovered from the serial signal to R, G, and B. To predictably display all three components, they must lie between peak white, 700 mV, and black, 0 V.

For a signal to be in gamut, all signal vectors must lie within the G-B and G-R diamonds. Conversely, if a signal vector extends outside the diamond, it is out of gamut. The

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **244 Application Information** Diamond Application

direction of an excursion out of gamut indicates which signal is excessive. Errors in green amplitude affect both diamonds equally, while blue amplitude errors affect only the top diamond and red errors affect only the bottom diamond.

Compare the signal to the display to determine out-of-gamut components. Be aware of these details:

- The intensity of a vector indicates its duration.

- A momentary out-of-gamut condition appears as a faint trace. Long duration violations show as a bright trace.

When evaluating out-of-gamut components, consider:

- Example A:

R - Ok G > 700 mV

B - Ok

- Example B:

R - Ok G - Ok B > 700 mV

- Example C:

R - Ok G - Ok, 350 mV B < 0 mV

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 245** Diamond Application

**Note:** Bending of the transitions indicates timing delays. When a color bar signal is applied, the vertical axis becomes an indicator of delay errors. Monochrome signals appear as vertical lines. Nonlinear component processing, such as from a gamma corrector that alters white balance, can cause deviations along the vertical axis.

## **Diamond Application On-screen Tools**

You can use on-screen tools to change the gamma LUT and selected line without opening the Diamond Settings menu. Select the button for the setting you want to adjust. The available tools are on the top and bottom of the display. They are highlighted for a few seconds when the application is first opened or if you select anywhere in the middle of the application tile.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **246 Application Information** Diamond Application

## **Gamma LUT**

To turn the Gamma LUT on or off:

**1.** Select the **LUT** button (other elements in the button depend on the options selected) in the top middle of the tile.

**2.** Select the lower **LUT:** button to turn on/off the 3D LUT for this tile. If a custom LUT is selected, the name is indicated if it is enabled.

To change the gamma curve and color gamut (displayed in the LUT button):

**1.** Select the **Settings** icon ( ).

**2.** Select **Inputs** and select the input being used.

**3.** Select **SDI** and **VIDEO** .

**4.** From the **Gamma Curve** list, select one of the following; the selection characterizes the video signal on each virtual input.

- **Auto:** The system selects the setting based on ST 352 VPID. If 352 VPID is not present, SDR Narrow is selected.

- **SDR Narrow:** The reference OETF (Optical to Electrical Transfer Function) is defined in ITU-R BT.709 with gamma of 0.45 and the reference EOTF is defined in ITU-R BT.1886 with gamma of 2.4.

The Narrow scaling places the extremes of the nonlinear color value from zero to unity at code words 40 hex (64 dec) and 3AC hex (940 dec) in a 10-bit representation for 0% Black to 100% White. This range is typical for standard-dynamic range.

- **SDR Full:** The reference OETF is defined in ITU-R BT.709 with gamma of 0.45 and the reference EOTF (Electrical to Optical Transfer Function) is defined in ITU-R BT.1886 with gamma of 2.4.

The full scaling places the extremes of the nonlinear color value from zero to unity at code words 0d and 1023d in 10-bit representation and 0d and 4095d in 12-bit representation for 0% black and 100% white, respectively.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 247** Diamond Application

- **PQ Narrow:** The reference OETF with a high luminance range capability of 0 to 10,000 cd/m[2] standardized in ST 2084. The EOTF is the inverse of OETF.

The narrow scaling places the extremes of the nonlinear color value from zero to unity at code words 40 hex (64 dec) and 3AC hex (940 dec) in a 10-bit representation for 0% Black to 100% White. This range is typical for standard-dynamic range.

- **PQ Full:** The reference OETF with a high luminance range capability of 0 to 10,000 cd/m[2] standardized in ST 2084. The EOTF is the inverse of OETF.

The full scaling places the extremes of the nonlinear color value from zero to unity at code words 0d and 1023d in 10-bit representation and 0d and 4095d in 12-bit representation for 0% black and 100% white, respectively.

- **HLG:** The reference OETF is standardized in ARIB B67 and the reference EOTF is standardized in ITU BT.2100 at the nominal display peak luminance of 1000 nits.

- **S-Log2:** The reference OETF is defined as Sony S-Log2.

- **S-Log3:** The reference OETF is defined as Sony S-Log3.

- **S-Log3 (Live HDR):** The reference OETF and OOTF (Optical to Optical Transfer Function) are defined as Sony S-Log3 (Live HDR).

- **Log C:** The reference OETF is defined as ARRI Log C.

**5.** From the **Structure** list, select one of the following:

- Auto: The system selects the setting based on ST 352 VPID. If VPID is not present, YCbCr 4:2:2 10bit is selected.

- YCbCr 4:2:2 10bit

- YCbCr 4:2:2 12bit

- YCbCr 4:4:4 10bit

- RGB 4:4:4 10bit

- RGB 4:4:4 12bit

**6.** From the **Color Gamut** list, select one of the following; the selection determines the color space of the video signal selection.

- **Auto:** The system selects the setting based on ST 352 VPID. If ST 352 VPID is not present, Rec. 709 is selected.

- **Rec. 709:** Standard for HD

- **Rec. 2020:** Standard for 4K

**7.** From the **Favorite 3D LUTs** list, select a 3D LUT.

To save a 3D LUT as a favorite, select the Information icon ( ) and select the star beside a LUT.

**8.** Select **Save** . The LUT button updates to match your selections.

## **Line Select Function**

You can select a single picture line to monitor in the display. By default, All Lines is selected and all lines are monitored.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **248 Application Information** CIE Application

**Note:** If you enable line select, the same line is selected in any trace display.

To turn on Line Select (and choose the line to monitor):

**1.** Select the **Lines** button at the bottom of the tile.

**2.** Select **1 Line** .

- To scroll through lines, select the **Plus** (+) button or **Minus** (–) button.

- To enter a specific line to monitor:
  - ♦ select **Line Sel.** and enter the line on the keypad; or

  - ♦ in the Picture application, use the line-select cursor (for active lines).

Depending on the resolution in the signal, the Line Select provides different information.

- If a signal is SD, HD, or 3G:
  - ♦ the _Line_ number is the selected line, including vertical blanking;

  - ♦ if the signal is interlaced format, the _Fields_ readout is below the Line number;

  - ♦ the _Pic Line_ number is next to Line; the Pic Line is the active line number, or numbers, selected.

- If a signal is UHD or 4K:
  - ♦ the Line number is the selected raster line,

  - ♦ the SDI Line is the selected line including vertical blanking,

  - ♦ the link number appears below the SDI Line.

**Note:** In link, the letters (A-D) refer to the physical links. The numbers (1-4) refer to the virtual links. For example, A3/62 indicates it is physical link 1 and virtual link 3 (in a two-sample interleave, 12G transport).

## **CIE Application**

The CIE application shows video data as it is plotted in a 1931 or 1976 CIE diagram. CIE diagrams are used to check the chromaticity of the video signal and determine

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 249** CIE Application

compliance to the standard color Gamut limits shown on the CIE diagram. In addition to the BT.2020, P3, and Rec. 709 limits shown, the D65 white point is also indicated.

## **Configure the CIE Application**

**1.** Select the **Tiles** icon ( ).

**2.** Select the tile with the CIE application.

**3.** Select the **Tile** icon ( ).

**Note:** To move the settings left or right, select the **Move** icon ( = ) in the Settings menu header.

**4.** In the **Color Space** section, select **CIE 1931** or **CIE 1976** .

**5.** In the **Trace Appearance** section, select how video data is plotted on the CIE display:

- **Monochrome:** The plotted video data is gray.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **250 Application Information** CIE Application

- **Color:** The plotted video data is colored with the corresponding CIE diagram colors.

**6.** Set **Line Select** to **On** to select 1 Line or **Off** to select All Lines. When Line Select is set to On (Line Select: Line 1), the display shows only results for the selected line in the picture. You can use on-screen tools to select the line; see _Line Select Function_ . Alternatively, you can select the line directly on the Picture.

## **CIE Application Line Select Function**

You can select a single picture line to monitor in the display. By default, All Lines is selected and all lines are monitored.

**Note:** If you enable line select, the same line is selected in any trace display.

To turn on Line Select (and choose the line to monitor):

**1.** Select the **Lines** button at the bottom of the tile.

**2.** Select **1 Line** .

- To scroll through lines, use the **Plus** (+) button or **Minus** (-) button.

- To enter a specific line to monitor:
  - ♦ select **Line Sel.** and enter the line on the keypad; or

  - ♦ in the Picture application, use the line-select cursor (for active lines).

Depending on the resolution in the signal, the Line Select provides different information.

- If a signal is SD, HD, 3G:
  - ♦ the Line number is the selected line, including vertical blanking;

  - ♦ if the signal is interlaced format, the Fields readout is below the Line number;

  - ♦ the Pic Line number is next to Line; the Pic Line is the active line number, or numbers, selected.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 251** CIE Application

- If a signal is UHD, 4K:
  - ♦ the Line number is the selected raster line,

  - ♦ the SDI Line is the selected line including vertical blanking,

  - ♦ the link number appears below the SDI Line.

In link, the letters (A-D) refer to the physical links. The numbers (1-4) refer to the virtual links. For example, A3/62 indicates it is physical link 1 and virtual link 3 (in a two-sample interleave, 12G transport).

## **Luma Qualified CIE**

Luma Qualified CIE Settings allow you to configure luma limits to constrain the trace within the CIE display. This can be useful for editors and colorists to help isolate the image within a specific luma range so that the operator can easily adjust the trace to keep within specific limits.

**Luma Qualified CIE On** constrains the CIE display within the specified user-defined limits. When Off is selected, the full luma range is shown within the CIE display.

**Input Gamma** shows the current gamma that is being used. This can be configured within the Virtual Input settings for the currently selected input.

The **Threshold Units** luma range can be selected in %, Nits or CV (Code Value) from the list.

You can adjust the **Lower Threshold** by using the up/down arrows or pressing on the value to bring up a keypad to enter the values directly. You can also use the left slider to adjust the value. The number is shown in the dialog box along with conversion for the other available values.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **252 Application Information** CIE Application

You can adjust the **Upper Threshold** by using the up/down arrows or pressing on the value to bring up a keypad to enter the values directly. You can also use the right slider to adjust the value. The number is shown in the dialog box along with conversion for the other available values.

The CIE Display in the upper left of the display shows whether the LQ CIE is Off or On and the selected luma range being used.

Here is the CIE display with the LQ CIE turned off. The full luma range of the signal is shown within the CIE display.

To aid in isolating a specific color range within the highlights or shadows, you can select a specific upper and lower luma threshold. In this case, the upper luma range has been set between a code value of 909 and a lower threshold of 608. When the LQ CIE is turned on, the trace is constrained within the specified luma range. In this case, the trace is constrained into the yellow color range, allow the operator to adjust the image more easily for this specific color range.

This LQ CIE display can be used in conjunction with the False Color Picture displays for Gamut or Luminance.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 253** Stop Display Application

## **Stop Display Application**

The Stop Display provides a tool to monitor video signals, with a variety of transfer functions, in a consistent manner. It helps the director of photography, cinematographer, and lighting engineer.

**Note:** Stop Display is enabled with Option MPSDP-PROD and is affected by the Gamma and Color Gamut settings. For additional information regarding these settings, see _Configure and Select Virtual Inputs_ .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **254 Application Information** Stop Display Application

- **Configure the Stop Display Application 1.** Select the **Tiles** icon ( 8 ).

  **2.** Select the tile with the Stop Display application.

  **3.** Select the **Tile** icon ( a ).

**Note:** To move the settings left or right, select the **Move** icon ( ) in the Settings menu header.

**4.** In the **Trace Appearance** section, select one of the following to change the colors of the parade traces:

- **Monochrome:** Display all traces in a conventional green.

- **Color:** Display the components of the traces in the colors described in the Display Mode. For example, the components in RGB mode are shown in red, green, and blue.

**Note:** The Color setting works only when Display Style is set to Parade. The Overlay mode displays the traces in green.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 255** Stop Display Application

**5.** In the **Display Style** section, select the way signal components are displayed in the active tile:

- **Parade:** All components are shown beside each other. This setting allows the traces to appear in the described colors.

- **Overlay:** All components are drawn at the same location so they appear on top of each other. This trace is displayed in green.

**6.** From the **Sweep** list, select the waveforms to view between the lines or fields or make timing measurements on them. The options depend on the active display style.

- When the Parade display style is active, you can select **1 line** or **1 field** .

- When Overlay display style is active, you can select **1 line** , **2 line** , **1 field** , or **2 field** .

**7.** In the **Display Mode** list, select the display mode (available only while displaying SDI inputs):

- **Y:** Displays the input as White (Y) for the Luma component. This display is the YRGB mode with the Red (R), Green (G), and Blue (B) components turned off.

- **RGB:** Displays the input as R, G, and B components.

- **YPbPr:** Displays the input as Y for the Luma component, and color difference Cyan (Pb) and Magenta (Pr) components.

- **YRGB:** Displays the input as Y, R, G, and B components.

**Note:** The inputs are shown only in their colors if Trace Appearance is set to Color.

**8.** To remove the trace of vertical and horizontal blanking data, set **Show Active Area Only** to **On** . When Show Active is enabled for a one-line waveform sweep, the width of the waveform trace and alignment matches the width of the Picture application.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **256 Application Information** Stop Display Application

**9.** Set **3D LUT: Convert to Rec. 709** to **On** to allow trace displays to convert the Gamma and Color Gamut settings for the signal to SDR Narrow and BT. 709 or use a custom Favorite LUT.

**10.** Set **Line Select** to **On** to select 1 Line or **Off** to select All Lines. When Line Select is set to On (Line Select: Line 1), the display shows only results for the selected line in the picture. You can use on-screen tools to select the line; see _Line Select Function_ . Alternatively, you can select the line directly on the Picture.

**11.** The Low Pass Enable setting is useful for isolating a specific characteristic of the input. Set **Low Pass Enable** as follows:

- **On:** Display only the low frequency of the signal.

- **Off:** Display the full available bandwidth.

**12.** In the **Reference** section, select one of the following:

- **Scene Light:** Shows a stop graticule in the vertical axis and is fixed regardless of the selected Gamma. It is used for scene setting and camera exposure adjustment.

- **Display Light:** Shows a Nits graticule in the vertical axis and is fixed regardless of Gamma selected. It is used for mastering the content for a targeted HDR system.

This turns on the “Best” option in Gain.

The example is of the Display Light setting.

[

**13.** In the **Gain** section, select the trace vector magnifications: **1.0x** , **2.0x** , **5.0x** , or **10.0x** . Best is available when you select Display Light in Reference. Display Light maximizes the trace height with 1,000 nits of brightness.

**14.** In the **Magnification** section, select **Best** , **1.0x** , **10.0x** , **20.0x** , or **25.0x** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 257** Stop Display Application

## **Stop Display Application On-screen Tools**

You can use the on-screen tools to change the gain, display mode, and sweep without opening the Stop Display menu. Select the button for the setting to adjust. The available tools are on the top and bottom of the display. They are highlighted for a few seconds when the application is first opened or if you select anywhere in the middle of the application tile.

## **Gain**

To increase or decrease the magnification of the trace display:

**1.** Select **Gain** .

**2.** Select a preset fixed-gain value: **1.0x** , **2.0x** , **5.0x** , or **10.0x** .

**3.** Select the **Reset** icon ( ) to reset the gain to 1.0x.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **258 Application Information** Stop Display Application

## **Horizontal and Vertical Position**

To adjust the position of the trace display:

**1.** Select **H Pos** to allow adjustment of the horizontal trace.

- Select-and-drag to move the trace on the touchscreen. This method can be performed without using the button.

- Use a mouse scroll wheel to move the trace.

- For incremental adjustments, select the **Plus** (+) button or **Minus** (-) button to adjust the horizontal position.

- Select the **Reset** icon ( ) to reset the horizontal position adjustment to default.

**2.** Select **V Pos** to allow adjustment of the vertical trace.

- Select-and-drag to move the trace on the touchscreen. This method can be performed without using the button.

- Use a mouse scroll wheel to move the trace.

- For incremental adjustments, select the plus + (plus) or - (minus) to adjust the vertical position.

- Select the **Reset** icon ( ) to reset the vertical position adjustment to default.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 259** Stop Display Application |

## **Gamma LUT**

Turn the Gamma LUT on or off:

**1.** Select the **LUT** button (other elements in the button are variable depending on the options selected) in the upper middle of display.

**2.** Select the lower **LUT:** button to set the Gamma LUT on or off.

To change the gamma curve and color gamut (displayed in the LUT button):

**1.** Select the **Settings** icon ( ).

**2.** Select **Inputs** and select the input being used.

**3.** Select **SDI** and **VIDEO** .

**4.** From the **Gamma Curve** list, select one of the following; the selection characterizes the video signal on each virtual input.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **260 Application Information** Stop Display Application

- **Auto:** The system selects the setting based on ST 352 VPID. If 352 VPID is not present, SDR Narrow is selected.

- **SDR Narrow:** The reference OETF (Optical to Electrical Transfer Function) is defined in ITU-R BT.709 with gamma of 0.45 and the reference EOTF is defined in ITU-R BT.1886 with gamma of 2.4.

The Narrow scaling places the extremes of the nonlinear color value from zero to unity at code words 40 hex (64 dec) and 3AC hex (940 dec) in a 10-bit representation for 0% Black to 100% White. This range is typical for standard-dynamic range.

- **SDR Full:** The reference OETF is defined in ITU-R BT.709 with gamma of 0.45 and the reference EOTF (Electrical to Optical Transfer Function) is defined in ITU-R BT.1886 with gamma of 2.4.

The full scaling places the extremes of the nonlinear color value from zero to unity at code words 0d and 1023d in 10-bit representation and 0d and 4095d in 12-bit representation for 0% black and 100% white, respectively.

- **PQ Narrow:** The reference OETF with a high luminance range capability of 0 to 10,000 cd/m[2] standardized in ST 2084. The EOTF is the inverse of OETF.

The narrow scaling places the extremes of the nonlinear color value from zero to unity at code words 40 hex (64 dec) and 3AC hex (940 dec) in a 10-bit representation for 0% Black to 100% White. This range is typical for standard-dynamic range.

- **PQ Full:** The reference OETF with a high luminance range capability of 0 to 10,000 cd/m[2] standardized in ST 2084. The EOTF is the inverse of OETF.

The full scaling places the extremes of the nonlinear color value from zero to unity at code words 0d and 1023d in 10-bit representation and 0d and 4095d in 12-bit representation for 0% black and 100% white, respectively.

- **HLG:** The reference OETF is standardized in ARIB B67 and the reference EOTF is standardized in ITU BT.2100 at the nominal display peak luminance of 1000 nits.

- **S-Log2:** The reference OETF is defined as Sony S-Log2.

- **S-Log3:** The reference OETF is defined as Sony S-Log3.

- **S-Log3 (Live HDR):** The reference OETF and OOTF (Optical to Optical Transfer Function) are defined as Sony S-Log3 (Live HDR).

- **Log C:** The reference OETF is defined as ARRI Log C.

**5.** From the **Structure** list, select one of the following:

- Auto: The system selects the setting based on ST 352 VPID. If VPID is not present, YCbCr 4:2:2 10bit is selected.

- YCbCr 4:2:2 10bit

- YCbCr 4:2:2 12bit

- YCbCr 4:4:4 10bit

- RGB 4:4:4 10bit

- RGB 4:4:4 12bit

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 261** Stop Display Application

**6.** From the **Color Gamut** list, select one of the following; the selection determines the color space of the video signal selection.

- **Auto:** The system selects the setting based on ST 352 VPID. If ST 352 VPID is not present, Rec. 709 is selected.

- **Rec. 709:** Standard for HD

- **Rec. 2020:** Standard for 4K

**7.** From the **Favorite 3D LUTs** list, select a 3D LUT.

> To save a 3D LUT as a favorite, select the Information icon ( 0 ) and select the star beside a LUT.

**8.** Select **Save** .

## **Display Mode**

To change the displayed signal components:

**1.** Select the button in the bottom-left corner of the application to expand the available display options.

**2.** Select the components to view:

- In the list of components, select the letter of the color to remove it. For example, select R to remove the red trace.

- Select the letter of a removed component to make it visible.

## **Display Format**

To change the Display Style, Sweep, and Magnification of the Stop Display:

**1.** Select the button in the bottom right corner of the application to expand the available display format options.

**2.** Select **Mag** and then select the magnification: **Best** , **1.0x** , **10.0x** , **20.0x** , or **25.0x** .

**3.** Select the **Display Style** option to switch between **Parade** and **Overlay** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **262 Application Information** Stop Display Application

**4.** Select **Parade** or **Overlay** to switch between the Display Style options. The options depend on which Display Style is active.

- When Parade display style is active, select **1 line** or **1 field** .

- When Overlay display style is active, select **1 line** , **2 line** , **1 field** , or **2 field** .

## **Line Select Function**

Line Select allows you to select a single picture line to monitor in the display. By default All Lines is selected and all lines are monitored.

**Note:** The same line is selected in any trace display if line select is enabled.

To turn on Line Select (and choose the line to monitor):

**1.** Select **Lines** at the bottom of the tile.

**2.** Select **1 Line** .

- To scroll through lines, select the **Plus** (+) button or **Minus** (-) button.

- To enter a specific line to monitor:
  - ♦ select **Line Sel.** and enter the line on the keypad; or

  - ♦ in the Picture application, use the line-select cursor (for active lines).

Depending on the signal resolution, the Line Select provides different information.

- If a signal is SD, HD, or 3G:
  - ♦ the Line number is the selected line, including vertical blanking;

  - ♦ if the signal is interlaced format, the Fields readout is below the Line number; and

  - ♦ the Pic Line number is next to Line; the Pic Line is the active line number, or numbers, selected.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 263** CAM Application

- If a signal is UHD or 4K:
  - ♦ the Line number is the selected raster line;

  - ♦ the SDI Line is the selected line including vertical blanking; and

  - ♦ the link number appears below the SDI Line.

In link, the letters (A-D) refer to the physical links. The numbers (1-4) refer to the virtual links. For example, A3/62 indicates it is physical link 1 and virtual link 3 (in a two-sample interleave, 12G transport).

## **CAM Application**

The CAM application displays the output of up to four cameras to check color levels and balance when MULTI input is selected.

## **Source Label Overlay**

The source label overlay is format information that includes the picture format, frame rate, structure, and gamma curve for that channel. It appears at the bottom of the CAM application tile, over the camera thumbnails if they are displayed.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **264 Application Information** CAM Application

The format information overlay can be set to turn off after 5 seconds, dim after 5 seconds, or never turn off. The format information does not appear if the instrument is not in multi-input mode.

To change the format information overlay:

**1.** Select the **Settings** icon ( ) and then select **Display** .

**2.** Select **MULTI INPUT** and select the **Source Label Timeout** option.

## **Configure the CAM Application**

**1.** Select the **Tiles** icon ( as ).

**2.** Select the tile with the CAM application.

**3.** Select the **Tile** icon ( ).

**Note:** To move the settings left or right, select the **Move** icon ( — ) in the Settings menu header.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 265** CAM Application

**4.** Set **Display Type** to **Waveform** or **Stop** . The Waveform setting makes the CAM application act like the Waveform application; see _Waveform Application_ . The Stop setting makes the CAM application act like the Stop Display application; see _Stop Display Application_ . To use the Stop setting in the Display Type, the MPSDP-PROD license is required.

**5.** Set **Thumbnail** to **On** to show a small picture of each input at the bottom of each input channel.

**6.** From the **Sweep** list, select the sweep rate: **1 Line** or **1 Field** .

**7.** From the **Display Mode** list, select one of the following:

- **Y:** Displays the input as White (Y) for the Luma component. This display is the YRGB mode with the Red (R), Green (G), and Blue (B) components turned off.

- **RGB:** Displays the input as R, G, and B components.

- **YRGB:** Displays the input as Y, R, G, and B components.

**8.** Waveform filters are useful for isolating a specific characteristic of the input. For example, you can enable a Low Pass filter for quick camera exposure setting. In the **Filter** section, select a waveform filter:

- **Flat:** Display the full available bandwidth.

- **Low Pass:** Display only the low frequency part of the signal.

**9.** From the **Graticule** list, select a vertical scale value. The options depend on whether the Display Type is set to Waveform or Stop.

- In multi-input, the primary input is used for graticule selection. When inputs have different gammas, select the input of interest as the primary input to get the correct graticule.

The Code Value vertical unit is a hexadecimal value. The Stop, Reflectance, and Nits scale are drawn differently, depending on the gamma setting in the input menu.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **266 Application Information** CAM Application

- Waveform Options:
  - The % value is a fixed graticule. It is compatible with the traditional waveform scales.

  - The Stop graticule is the Scene light graticules for scene setting and camera exposure adjustment.

  - The Nits graticule is the Display light graticule for mastering the content for a targeted HDR system.

- Stop Options:
  - The Log Nits graticule is the Display light graticule for mastering the content for a targeted HDR system using Stop application processing.

  - The Log Stops graticule is the Scene light graticules are for scene setting and camera exposure adjustment using Stop application processing.

**10.** Set **Line Select** to **On** to monitor one raster line in the display or **Off** to monitor all lines. When Line Select is set to On (Line Select: Line 1), the display shows only results for the selected line in the picture. You can use on-screen tools to select the line; see _Line Select Function_ . Alternatively, you can select the line directly on the Picture.

**11.** In the **Gain** section, select the vertical gain of the trace display: to **x1** , **x2** , **x5** , or **x10** times.

## **Choose Inputs for CAM Application**

The channel images shown in the CAM application are determined by the Select channels in the Multi Input menu. The channels are chosen from those listed in the Input menu. Up to four channels can be shown in the CAM application at one time.

The instrument can show up to four trace applications (Waveform, Vector, Lightning, Diamond, CIE, or Stop Display) at the same time. Each input channel in the CAM application acts as one of those trace applications. That is, if three tiles are showing trace applications, the CAM application can show only one input. If the CAM application shows four inputs (inputs coming into the instrument), no other tiles can show trace applications.

To automatically give the CAM application access to the four trace applications, change the CAM application tile to full screen. Up to four channels are immediately available in the CAM application.

To select channels to see in the CAM application:

**1.** Select the **Input** icon ( ) on the status bar.

**2.** Select the **Multi Input** button on the Input bar.

**Note:** If “Multi:” is not in the Input menu and the Multi button is not active, the MPSDP-MULTI option might not be installed.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 267** CAM Application

**3.** Set **Multi Input** to **ON** .

**4.** Set **Edit Mode** to **ON** .

**==> picture [2 x 5] intentionally omitted <==**

**----- Start of picture text -----**<br>
[<br>**----- End of picture text -----**<br>

**5.** To set the inputs in Select channels:

- Add a channel to the **Select channel** list; select the channel in the **Input** menu and select **Add Channel** . The CAM application shows the channel in the tile immediately.

**Note:** Select **Make Primary** to enable the graticules for the needed gamma.

The example shows three channels in the Select channel list from the Input menu, so the CAM application shows those three channels in the order they are in the Input menu, not the order they are chosen for the Select channel list.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **268 Application Information** CAM Application

- Remove a channel from the Select channel list; select the channel in the **Input** menu and select **Remove Ch** . The CAM application removes the channel from the tile immediately.

**6.** Select the channel in the **Input** menu again to close it.

**7.** Select the **Multi Input** button to close the menu.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 269** CAM Application

## **CAM Application On-screen Tools**

You can change the gain, horizontal position, vertical position, thumbnail (on or off), display mode, line select, and sweep rate—without opening the CAM Settings menu— through on-screen tools. Select the button for the setting you want to adjust. All the available tools are located on the top and bottom of the display and are highlighted for a few seconds when the application is first opened or if you select in the tile heading.

## **Gain**

To increase or decrease the vertical gain of the trace display.

**1.** Select **Gain** .

**2.** Select the gain amount: **1.0x** , **2.0x** , **5.0x** , or **10.0x** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **270 Application Information** CAM Application

## **Thumbnail**

To turn on the thumbnail under the CAM signal image, select **Thumbnail** and then select **Thumbnail : Off** .

Select **Thumbnail : On** to turn the thumbnail off.

## **Vertical Position**

Select **V Pos** to adjust the vertical trace. Select the button to turn the lock off and on.

- Select-and-drag to move the trace on the touchscreen. This method can be used if the setting is locked or not. The V Pos button must be unlocked (no lock-symbol) for the select-and-drag to work.

- For incremental adjustments, select the **Plus** (+) button or **Minus** (-) button to adjust the vertical position.

- Select the **Reset** button ( Reset ) to move the signal image back to 0.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 271** CAM Application

## **Display Mode**

To change how the waveforms are displayed:

**1.** Select the button in the bottom left corner of the application to expand the available display options (the button label varies depending on the last option selected).

**2.** Select the components to monitor:

- In the waveform list of components, select the letter of the component to remove it. For example, select G to remove the green component from the waveform.

- Select the letter of a removed component to make it visible.

## **Line Select Function**

You can select a single raster line to monitor in the display. By default, all lines are monitored. If you enable Line Select, the same line is selected in any trace display.

To turn on Line Select (and choose the line to monitor):

**1.** Select **Lines** at the bottom of the tile.

**2.** Select **1 Line** .

- To scroll through lines, select the **Plus** (+) button or **Minus** (-) button.

- To enter a specific line to monitor: select **Line Sel.** and enter the line on the keypad.

To turn Line Select off and monitor all lines, select **Lines** at the bottom of the tile and select **All Lines** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **272 Application Information** CAM Application

## **Sweep**

To change the sweep, select the button in the bottom right corner of the application and select **1 Line** or **1 Field** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 273** Picture Application

## **Picture Application**

The Picture display lets you see the picture generated by the video signal.

(Copyright 2008, Blender Foundation / www.bigbuckbunny.org)

**Note:** Tiles displaying the Picture application in multi-input mode and viewing secondary inputs do not show content from all 4K contribution links.

In full-screen mode, there is no cropping. Pictures are decimated horizontally or vertically to obtain the correct aspect ratio. This decimation might cause some artifacts.

## **Configure the Picture Application**

**1.** Select the **Tiles** icon ( ).

**2.** Select the tile with the Picture application.

**3.** Select the **Tile** icon ( ).

**Note:** To move the settings left or right, select the **Move** icon ( - ) in the Settings menu header.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **274 Application Information** Picture Application

**4.** Set **3D LUT: Convert to Rec. 709** to **On** to allow the trace displays to convert camera logs to Rec. 709 (requires Option MPSDP-PROD) or use a custom Favorite LUT.

**Note:** In multi-input mode, Convert to Rec. 709 works only with the primary channel. Convert to Rec. 709 mode is not supported for SD signals.

**5.** Set **Format Overlay** to **On** to display the format information on top of the picture. Select and drag the format information window to set the location.

**6.** Source ID Overlay provides an overlay of the video source on the Picture application. The source data carries ANC data conforming to ST 291M. The default DID is 0x53 and, SDID is 0x49. Set them as required. The source ID is limited to 15 ASCII characters. To enable the Source ID Overlay, set the **Source ID Overlay** to **On** . Select and drag the overlay to the correct location on the application.

**Note:** In multi-input mode, Source ID Overlay works only with the primary channel.

**7.** You can select the picture line to monitor in the available trace displays, including Waveform, Stop, Vector, Diamond, Lightning, and CIE. Set **Line Select** to **Off** to select All Lines or **On** to select 1 Line. If you select 1 Line, a horizontal line appears on the picture. To choose a line to monitor, select and drag the line. The selected line number is noted on the line.

**8.** For information about configuring closed caption/subtitle formats and services, see _Closed Caption/Subtitle Details_ .

**9.** In the **SD Aspect Ratio** section, select one of the following SD (standard definition) aspect ratios:

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 275** Picture Application

- **AUTO:** The AFD data will set the aspect ratio.

- **16x9**

Selecting an option that has non-SD input has no effect.

**10.** For information about configuring safe area graticules, including AFD and AFD data, see _Graticules: Details_ .

**11.** You can adjust the visibility of the available picture measurements. For details, see _Measurement Overlay: Details_ .

**12.** For information about configuring the threshold for HDR picture measurements, see _Measurement Thresholds: Details_ .

**13.** The Lightmeter displays the light level (in nits or stops) at the point marked by the Lightmeter cursor in the Picture display. For more information about this feature, see _Lightmeters: Details_ .

**14.** The Input Gamma section indicates the input Gamma set in the Settings menu for the selected input.

**15.** Select **False Color** option to turn on false color. The false-color displays apply a color palette to the picture to highlight attributes associated with images. See _False Color: Details_ for more information about this feature.

## **Closed Caption/Subtitle Details**

**Note:** In multi-input mode, Closed Caption/Subtitles works only with the primary channel.

The Closed Caption/Subtitles conform to ST 334:2015.

To configure closed captions/subtitles:

**1.** In the **Picture Settings** menu, select **Closed Caption** .

**2.** To turn on the CC Information Overlay, set **CC Information Overlay** to **On** . The CC Information Overlay provides closed caption/subtitle format and service information. To move the overlay, select the overlay and drag it to the new location within the tile.

**3.** In the **Captions/Subtitles Transport** section, select a format to decode and open the service options:

- **OFF:** Turns off the closed caption decoding. The overlay remains in the Picture tile if it is on.

- **Auto:** Detects and selects the closed captions/subtitles format in the signal and presents the service options. Select the appropriate input.

- **CEA608:** A standard format of closed captions/subtitles data used in the U.S., Canada, and Mexico for analog TV transmissions. If a service has no activity for 10 seconds, it is considered missing.
  - ♦ In the **CEA608 Channel** section, select the appropriate input (1 through 4).

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **276 Application Information** Picture Application

- **CEA708:** A standard format of closed captions/subtitles data in the U.S. and Canada for digital TV transmissions. If a service has no activity for 10 seconds, it is considered missing.
  - ♦ In the **CEA708 Service** section, select the appropriate input (1 through 6).

- **WST:** Also called Teletext, WST is a standard format for closed captions/subtitles in many parts of the world. Support includes OP-47 and 2031.
  - ♦ In the **Teletext Page** box, set the page number for your region. Select the up or down arrow, or select the number and use the pop-up keypad.

  - ♦ PRISM supports the complete primary character set for general Latin-based languages, plus secondary character sets for additional symbols, accents, and characters specific to:
    - English

    - Portuguese

    - Spanish

    - French

    - German

    - Italian

- **ARIB:** This is a standard B24 of decoding.
  - ♦ In the **ARIB Type** section, select the appropriate format: **HD** , **SD** , or **Mobile** .

- **TTML2:** An XML-based format for the interchange of captions and subtitles over ST 2110-43 transports. If TTML transport is selected or if detected using the AUTO setting, then additional information is presented.
  - ♦ In the **Selected TTML2 Language Track** box, you can select a language track between 1 and 10 even if the language track is not currently available. The selected language track is saved in presets, which is one reason why you might want to select a language track that isn’t currently available.

  - ♦ The **Detected Languages** section displays the track number and detected language for available TTML tracks. The supported character sets are Latin, Cyrillic (1/2/3), Hebrew, Arabic, and Greek. The supported national option sets are English, German, Italian, French, Portuguese, and Spanish.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 277** Picture Application

**Note:** Each Picture tile can select a closed caption format and a service.

## **Graticules: Details**

**Note:** Graticules conform to industry standard ST 2016-1.

This section explains how to turn safe area graticules on and off, including AFD.

To configure graticules:

**1.** In the **Picture Settings** menu, select **Graticules** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **278 Application Information** Picture Application

The AFD graticule frame is based on input AFD data. These are not adjustable.

**2.** In the **Graticules** menu, select from the options as needed:

- To show the center crosshairs, set **Picture Center Graticule** to **On** . The crosshairs appear in the middle of the selected Picture tile whether there is AFD data or not.

- To show the AFD frame, set **AFD Graticules** to **On** . The dashed line is the received AFD data aspect ratio. If AFD data is not present, the graticule will not be displayed.

- To show the AFD on-screen information, set **AFD Overlay** to **On** . The AFD data description appears in the selected Picture tile even if there is no AFD data.

**Note:** The Bar1 and Bar2 data complies with ST 2016-1-2009.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 279** Picture Application

**3.** For information about changing the colors of the AFD graticule and the Picture Center Graticule, see _Configure Graticule Colors_ .

**4.** The safe areas for each Picture tile are independent of other Picture tiles. You can change a Picture tile to display any, all, or none of the Safe Area Action or Title options while nothing changes in any other Picture tiles.

- Select a ratio for the Safe Area Standards (SMPTE, ITU, and ARIB TR-B.4) to turn on the graticules in a Picture tile. To change the Safe Area Standard that is used, see _Configure Safe Area Graticules_ .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **280 Application Information** Picture Application

- The Safe Area _Action_ 1-2 menus turn on a solid line defining a safe area.

- The Safe Area _Title_ 1-2 menus turn on a dashed line defining a safe area.

**5.** Select a safe area ratio option: **4x3** , **14x9** , or **16x9** . The standard safe area in a Picture tile depends on the selected ratio.

**Note:** These ratios do not affect AFD graticules.

**6.** You can define custom safe areas. Select the **Custom 1** and **Custom 2** options to see the custom-defined space in a Picture tile. These safe areas are set independently and, if selected, override the standard safe area selection. The

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 281** Picture Application

specifics of each custom graticule are listed under the Custom 1, Custom 2 names. For details about setting the Custom Safe Areas, see _Set Custom Safe Areas_ .

There are two custom options in each menu.

## **Picture Measurements**

**Note:** In multi-input mode, Picture Measurements works only with the primary channel.

To turn on the overlay containing a selectable set of picture measurements (including HDR measurements):

**1.** Select the **Picture** application.

**2.** In the **Applications** menu, select the **Tile** icon ( ).

**3.** If needed, select the measurement overlay and drag it to set the location.

## **Measurement Overlay: Details**

**1.** In the **Picture Settings** menu, select **Measurements Overlay** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **282 Application Information** Picture Application

**2.** Set **Measurements Overlay** to **On** . The Measurements Overlay appears in the Picture application. You can select the overlay window and drag it to any location in the Picture tile.

**3.** To make the picture measurements visible in the overlay, select the checkboxes beside the desired measurements. Clear the checkboxes to remove the measurements from the overlay.

For many parameters, a threshold setting is required. For details about setting measurement thresholds, see _Measurement Overlay: Details_ .

You can set the following measurements; settable thresholds are indicated by _x_ :

- Total percent HDR area the nits threshold for this measurement

- _X_ percent area, in nits

- Brightest _x_ percent Area, in nits

- Darkest _x_ percent Area, in nits

- Contrast Ratio (Brightest:Darkest)

- Dynamic Range (stops = Log2(Brightest _x_ percent / Darkest _x_ percent)).

## **Measurement Thresholds: Details**

To set the thresholds for picture measurements that require them:

## **1.** Select **Measurement Thresholds** in the **Picture Settings** menu.

**Note:** These settings also affect the HDR alarm settings, see _HDR_ in the alarms table.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 283** Picture Application

**2.** Specify the following thresholds as needed:

- **HDR Zone Threshold (Nits):** Any picture value higher than this threshold, in nits, is considered to be in the HDR zone.

- **Area (%):** Defines the brightest percentage of the picture used to determine the bright threshold in nits.

- **Brightest Area (%):** Defines the brightest percentage of the picture used to determine the HDR threshold in nits.

- **Darkest Area (%):** Defines the darkest percentage of the picture used to determine the dark threshold in nits.

## **Lightmeters: Details**

**Note:** In multi-input mode, Lightmeters work only with the primary channel.

Lightmeters measure the light level, in nits or stops, at the point marked by the Lightmeter cursor in the Picture application. Proper operation requires selecting the appropriate Gamma Curve in the input settings. (See _Gamma Curve_ .)

**Note:** The readout is the average luminance of a 5x5 pixel area in a 1920x1080 picture, a 10x10 pixel area in a 3840x2160 picture, and a 20x20 pixel area in a 7680x4320 picture.

## **Turn on Lightmeter Cursors**

**1.** Select the **Picture** application and then, in the **Applications** menu, select the **Tile** icon ( [J ).

**2.** Select **Lightmeter** .

**3.** Set the **Lightmeter Overlay** to **On** .

**4.** Select the number of needed Lightmeter cursors (up to 5).

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **284 Application Information** Picture Application

**Note:** The Lightmeters all use the same method for measurements. The colors of the Lightmeter cursors are just for identification.

The Lightmeters are visible in the Picture application.

## **Adjust Lightmeter Cursors**

- To move the Lightmeter cursors, select any part of the crosshairs or the measurement numbers and drag the target to the new location. The measurement updates automatically.

- To remove a selected Lightmeter cursor from the Picture, clear the checkbox of the color in the Picture Settings menu.

- To remove all the Lightmeters cursors from the Picture, clear the checkboxes of all the Lightmeter colors or set the Lightmeter Overlay to Off.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 285** Picture Application

## **False Color: Details**

**1.** Select the **Picture** application and then select the **Tile** icon ( [J ) in the **Applications** menu.

**2.** From the **False Color** list, select a false color palette. The false color turns on and shows the selected option:

- **Gamut:** Check gamut compliance to Rec. 2020, Rec. 709, and P3 gamut limits. There are three modes for determining the amount of color excursions outside the gamut of interest and deciding whether to remap the colors or ignore them. Select one of the following:
  - ♦ **Single Color:** Use for a quick check of gamut compliance to Rec. 709 and P3 gamut limits. Every pixel that is outside the gamut of interest, such as Rec. 709, is colored using fully saturated red.

  - ♦ **Banded Color:** This measurement is applicable only for signals that use the Rec. 2020 color gamut. Banded color indicates pixels that exceed the Rec. 709 or P3 gamut limits as contained in the Rec. 2020 color gamut.

In this trilevel “Banded” false color mode, yellow (low) regions represent pixels whose colors fall between 0% and 33% of the excursion zone between the Rec. 709 and Rec. 2020 gamut triangles. The orange (medium) areas represent excursions between 33% and 66% of the excursion zone. The red (high) areas represent the final third of the excursion zone. This false color representation makes it easy to focus on specific areas of interest. For example, the yellow and orange areas could be ignored, and color mapping efforts could focus only in the areas of the picture represented by the red pixels.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **286 Application Information** Picture Application

- ♦ **Original Color:** This mode Indicates the color(s) that exceed the Rec. 709 and P3 gamut limits for signals using the Rec. 2020 color gamut. This mode indicates colors that need correction. The colors indicated are out of gamut.

Select **Outside 709** or **Outside P3** to choose the Gamut of interest for Gamut False Color indication.

- **% Area:** A fixed false-color palette is applied to regions of the picture with Brightest, Area, and Darkest. You can disable any or all of these false colors by clearing the checkbox next to the color in the % Area menu.

- **Luminance:** Create a user-defined false color palette based on luminance values.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 287** Picture Application

**Note:** In multi-input mode, Luminance False Color works with both the primary and secondary channels.

The Luminance False Color display replaces pixels that fall within a specified range of nits or stops values to a color that you specify. You can configure up to nine ranges. For example, you can use the Luminance False Color display to tag pixels that are within a specified HDR range.

(Copyright 2008, Blender Foundation / www.bigbuckbunny.org)

## **Luminance Details**

The false color ranges are defined in nits or stops, depending on the gamma curve set up in the input (select the **Settings** icon ( ) and then select **Input** ). If a camera-based gamma curve is set, such as S-Log2, the false color ranges are in stops. If a displaybased gamma curve is set, such as SDR Narrow, the false color ranges are in nits.

## **Turn on Meter Overlay**

In the **Luminance** menu, set **Meter Overlay** to **On** to enable the Meter Overlay in the Picture tile. The overlay shows the false color definitions in nits or stops made in the Luminance False Color table at the bottom of the menu. You can move the overlay to the right, bottom, left, or top of the image by dragging the meter with a mouse or by touch.

PRISM provides two false color defaults that take into account the input gamma curve.

- Select **BT.2408** default to set False Color according to that standard.

- Select **Sub Super** for convenient False Color default for Sub Black or Super White. This is useful for:
  - highlighting pixels below 0 Nits (Orchid by default).

  - HDR production.

Sub Super sets up bands that are above and below the black level (Sub) and outside the upper limit (Super).

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **288 Application Information** Picture Application

You can use the Enable selector to show or hide any band.

**Note:** Sub Super works best in CV mode, which supports setting the bands to regions in which Nits is undefined. If the Code Value is for a band in which the Nits units are undefined, a 0 is displayed in the Nits column. If you change the units between Nits and CV, it might affect the range of the Sub and will be limited to 0 Nits. You might have to recall the preset in Code Value to restore the Sub region.

If changes are made to the false color ranges in the Luminance False Color table, an indication that the default settings have changed is shown.

## **Customize False Colors**

The Luminance False Color table allows you to customize the minimum and maximum range of up to nine false color bands. Band limits are specified in either Nits/Stops or Code Value (CV), based on the selected units.

The band range is displayed in Percent or Nits/Code Value by selecting the readout in the table header.

To enable specific bands, select the checkbox in the **Enable** column of the table. You can change the Nits or Stops range even if the checkbox is not set.

To display specific colors, select the checkbox in the **Enable** column of the table. You can change the Nits or Stops range even if the checkbox is not set.

To adjust the band range, select anywhere in the row. You can adjust the Minimum and Maximum value in the range using the up and down arrow buttons, or select in the number field and a numeric entry keypad appears. Enter the value and select **Enter** to close. The false colors in the Picture and the Meter Overlay are updated as adjustments are made.

If the range for one color overlaps the range for another color, the color that is higher in the table overlaps the colors lower in the table.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 289** Picture Application

You can turn False Color on and off in the tile:

**1.** Select the **Picture** tile, which brings up a False Color setting.

**2.** Select the **False Color** option to change between on and off.

The false color shown is the most recent false color display selected in the Picture Settings menu.

## **Extended Full-Screen Display**

In an extended display, you can enlarge the Picture application even more than full screen. The picture expands to cover the status bar.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **290 Application Information** Picture Application

**Note:** This option is available only with the Picture application in an extended display or the right-side display in MPD models.

There are two ways to change between full-screen and extended full-screen mode.

- Double-tap: Each double-tap in the Picture application changes the display to the next size: from quarter-screen mode (or half-screen if it was set) to full-screen, to maximum-screen mode (the status menu is covered), and back to quarter- or halfscreen mode.

- Select the icons:
  - **A.** In the Picture application, in the extended display, select the **Tiles** icon ( = ) to open the application bar and select the full-screen icon ( helwy ). The Picture application changes to full-screen mode.

  - **B.** Select the **Extended Full-Screen** icon ( t™ ). The Picture application changes to extended full-screen mode.

  - **C.** Select the **Reduce** icon ( Ral(Ces) ) to return to half- or quarter-screen mode.

The following figure shows the extended display (right side) in full-screen mode.

The following figure shows the extended display in extended full-screen mode.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 291** Video Session Application

## **Picture Application On-screen Tools**

You can turn the gamma LUT and False Color on or off without opening the Picture Settings menu, through an on-screen tool. Select the button for the setting you want to adjust.

## **Gamma LUT**

Turn the Gamma LUT on or off, select the **LUT** button. If a custom LUT is selected, the name is indicated if it is enabled.

## **False Color**

To turn False Color on or off, select the **False Color** button. For more information about False Color, see _False Color: Details_ .

## **Video Session Application**

**Note:** In multi-input mode, Video Session works only with the primary channel.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **292 Application Information** Video Session Application

Use this application to view various performance parameters of the SDI video signal or the decoded IP stream. Select any of the tab titles to view the associated information: **SDI Format, VPID 352, Bit Level** , **CRC Status** , **JPEG XS** , or SDI Vu.

The ST 2110-22 JPEG XS tab shows the decoded JPEG XS metadata from an ST 2110-22 stream. See _2110-22 JPEG XS Tab_ for further information.

## **Video Session Elements**

The following elements are at the top of the Video Session application:

- **INPUT:** Shows the selected input source on the top line and shows the detected format, sample structure, and transport of the input signal on the second line.

- **Display tabs:** Each tab has a status indicator to provide a quick view of the status of the parameters in each tab.
  - **SDI FORMAT:** This page shows the status of various SDI signal parameters on the input signal. See _SDI Format Elements_ .

  - **VPID 352:** This page shows the status of the ST 352M VPID on the input signal. For 3G-SDI signals, VPID is required on the primary link (Link A). See _VPID 352 Tab_ .

  - **BIT LEVEL:** This page shows if there are any stuck bits in the input signal. See _BIT LEVEL Tab_ .

  - **CRC STATUS:** This page shows the status of CRC and Checksum errors in the video signal. See _CRC STATUS Tab_ .

  - **SDI Vu:** This page shows error events for all four physical SDI inputs (SDI 1–4) simultaneously, regardless of whether they are selected as active inputs. See _SDI Vu Tab_ .

  - **2110-22 JPEG XS:** This page shows the decoded JPEG XS metadata from an ST 2110-22 stream. See _2110-22 JPEG XS Tab_ .

- **Run Time:** The instrument maintains a running monitoring session for the Video Session application. The Run Time readout displays the amount of time that has elapsed during the current monitoring session. The time is displayed as

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 293** Video Session Application

DD, HH:MM:SS. DD is number of days, HH is number of hours, MM is number of minutes, and SS is number of seconds.

- **Reset icon:** Select the **Reset** icon (
  - ) to restart the monitoring session.

- **Run** / **Stop icons:** When the monitoring session is running (collecting error data), select the **Stop** icon ( C) ) to stop the session. When the monitoring session is stopped (no error data collection and no display updates), select the **Play** icon ( oC ) to restart the session.

## **SDI Format Elements**

Select the **SDI FORMAT** tab to view the status of various SDI signal parameters on the input signal:

- **SAV Place Err:** Indicates if a Start-of-Active-Video Placement error has occurred.

- **EAV Place Err:** Indicates if an End-of-Active-Video Placement error has occurred.

- **Field Length Err:** Indicates if a Field Length error has occurred.

- **Line Length Err:** Indicates if a Line Length error has occurred.

- **Line Number Err:** Indicates if a Line Number error has occurred.

- **Ancillary Data:** Indicates if Ancillary Data is present in the video signal. The displayed values are either Present or None for SD signals, or Y and C Present and None for HD and 3-Gbps signals.

- **Statistics:** This section of the display shows the status and statistical values for certain errors. For information about the errors in this section, view the help file in the instrument: When the Video Session is active in a tile, select the HELP button.

- **Status:** Shows the status of the associated error as OK, Invalid, Missing, or Error.

## **VPID 352 Tab**

Select the VPID 352 tab to view the VPID values of the ST 352M payload. For ST 2110-40 inputs, VPID is sent over the lowest-numbered ST 2110-40 stream. For ST 2110-40, if the payload contains VPID ANC information that is verified as present in the ANC Session, then the VPID will be decoded in this display.

For 3G-SDI signals, VPID is required on the primary link (Link A).

**Note:** If input parameters such as Gamma Curve, Color Gamut, or Structure are set to Auto, VPID 352 (if present) is used to set them.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **294 Application Information** Video Session Application

**Note:** Full- and half-screen modes show the Binary values (shown in the example, under BIT LEVEL), which are hidden in 1/4-screen mode to present a more compact view.

The VPID 352 tab consists of two panes:

- **Left pane:** Shows the presence of an ST 352M payload. The number of data streams determine the number of links, with the VPID values shown in hexadecimal. To view the decoded VPID information in the right pane, select a link.

- **Right pane:** Contains the decoded VPID of the selected link. The VPID contains 4 bytes of data, and these show the transport standard, picture, frame rate, sampling structure, and bit depth information. Depending on the standard, different information might be present, such as Aspect Ratio, Transfer Characteristic, Colorimetry, H Pixel, and Channel Assignment.

## **BIT LEVEL Tab**

Select the **BIT LEVEL** tab to see if there are any stuck bits in the input signal.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 295** Video Session Application

- **Y Stuck Bits:** Displays which of the luminance video bits are stuck. If the readout is “---”, then none of the bits are stuck.

**Note:** For 8-bit video, because the unused bits are always low, “-----LL” is displayed when no other bits are stuck.

- **C Stuck Bits:** Displays which Chrominance video bits are stuck. If the readout is “---”, then none of the bits are stuck.

## **CRC STATUS Tab**

Select the **CRC STATUS** tab to view the status of CRC and Checksum errors in the video signal.

**Note:** The instrument uses the RP 165 standard for error checking. For HD and 3 Gb/s signals, the CRCs change on every video line.

- **Y Chan CRC Error:** Displays the status of the Y channel embedded CRC (Cyclical Redundancy Check) that was calculated for the video signal. Using a known test signal, the CRC status can be used to verify integrity through a system. An error means that the Y Channel embedded CRC value does not match the calculated CRC value, which indicates that a transmission error has occurred.

- **C Chan CRC Error:** Displays the status of the C channel embedded CRC (Cyclical Redundancy Check) that was calculated for the video signal. Using a known test signal, the CRC status can be used to verify integrity through a system. An error

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **296 Application Information** Video Session Application

means the C Channel embedded CRC value does not match the calculated CRC value, which indicates that a transmission error has occurred.

- **Y Anc Checksum Error:** Displays the status of the Y channel ancillary embedded checksum value that was calculated for the video signal. Using a known test signal, the checksum status can be used to verify integrity through a system. An error means the Y Channel embedded checksum value does not match the calculated checksum value, which indicates that a transmission error has occurred.

- **C Anc Checksum Error:** Displays the status of the C channel ancillary embedded checksum value that was calculated for the video signal. Using a known test signal, the checksum status can be used to verify integrity through a system. An error means the C Channel embedded checksum value does not match the calculated checksum value; this indicates a transmission error has occurred.

- The CRC Status display is also divided into four columns:
  - **Status:** Shows the status of the associated error:

  - **OK:** No error is currently detected.

  - **Invalid:** The data for the item is currently invalid.

  - **Missing:** The data for the item is currently missing.

  - **Error:** The associated error is currently in an error state.

- **Err Fields:** The number of fields, since the last reset, that contained at least one error.

- **Err Secs:** The number of seconds, since the last reset, that contained at least one error.

- **% Err Fields:** Shows a calculated number of the percentage of all fields since the last reset that contained at least one error.

## **SDI Vu Tab**

When SDI Vu is enabled, it is available in the Video Session display. For details about enabling SDI Vu, see _Configure SDI Vu_ . Select the **SDI Vu** tab to view error events for the four physical SDI inputs.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 297** Video Session Application

The following indicators are displayed on the SDI Vu tab:

- Video Format

- Y Chan CRC

- C Chan CRC

- Video Freq Offset

- Audio Content

- Audio Parity AES

- Audio Parity Emb

- AV Samples

- ANC Parity

Color-coded icons indicate the status of each measurement:

- **Green:** The SDI input is assigned to a monitoring channel and no errors are detected on the virtual input.

- **Red:** Error detected or at least one error reported in the virtual input, possible signal missing.

- **Dash (-):** No error detected, no valid data in audio content, or no measurement due to no signal.

For details about configuring SDI Vu alarms, see _SDI Vu_ in the alarms table.

## **2110-22 JPEG XS Tab**

Select the **2110-22 JPEG XS** tab to view the decoded JPEG XS metadata of the ST 211022 stream. The metadata includes common video attributes such as resolution, frame rate, sample structure, range, timecode, and colorspace.

**Note:** Decoding ST 2110-22 requires the MPSDP-JPXS license.

The tab also displays metadata specific to JPEG XS:

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **298 Application Information** Audio Application

- **Payload Bitrate** describes the total bitrate of the undecoded ST 2110-22 stream.

- **Decoded Bitrate** reports the bitrate of the uncompressed video data after it has been decoded.

- **Compression Ratio** is the ratio between the decoded bitrate and the payload bitrate.

- **Profile** specifies the JPEG XS profile used for encoding.

- **Level Signaling** indicates the level of the JPEG XS codec. This is often used to define the maximum resolution and frame rate.

- **Sublevel Signaling** provides more information about constraints within the specified level. This is often used for specifying the nominal bits per pixel for the encoded image.

## **Audio Application**

**Note:** In multi-input mode, Audio works only with the primary channel.

The Audio application provides a level-meter display with multiple ballistic settings, and optional Audio Session and Lissajous with Channel Correlation displays. Audio Session shows instantaneous measurements of the level meters and the Lissajous and Channel Correlation displays show audio phase information. You can perform Dolby E decoding on a specified SDI input channel pair.Scroll left and right to see additional audio channels.

**Note:** The Lissajous, Channel Correlation meter, and Audio Session displays require software option MPSDP–AUD. Dolby E decoding requires option MPSDP-DLBY. The 32channel audio support requires option MPSDP-FMT-8K.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 299** Audio Application

## **Configure Audio**

This section describes the parts of the Audio tile and the information available, such as level meters and the Lissajous display. It also explains the measurements in those displays.

Level meters are the vertical bar graphs. The height of the bar indicates the amplitude of the audio program in the corresponding input channel. The meter levels are color coded based on their relationship to the Test level and Peak Program level indicators:

- The meter bars are displayed below the Test level in a green color.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **300 Application Information** Audio Application

- Between the Test level and the Peak Program level, the meter bars are displayed in yellow.

- Above the Peak Program level, the meter bars are displayed in red.

For details about changing the Test level, see _Test Level (dBFS)_ .

For details about changing the Peak Program level, see _Peak Program Level (dBFS)_ .

To configure the Audio settings:

**1.** Select the **Tiles** icon ( ).

**2.** Select the tile with the Audio application.

**3.** Select the **Tile** icon ( ).

**Note:** To move the settings left or right, select the **Move** icon ( ) in the Settings menu header.

**4.** 5.1 Channel Order changes the order in which the right and center channels in any 5.1 surround program are displayed in the level meters. To configure the order:

- **A.** Select the **Settings** icon ( ).

- **B.** Select **Audio** .

- **C.** In the **5.1 Channel Order** section, select **LCR** or **LRC** . The level meter reorders to left-center-right or left-right-center.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 301** Audio Application

**Note:** This setting affects all 5.1 surround programs. If you select a second 5.1 surround program, both programs are set to LCR or LRC.

**5.** Ballistics displays the selected ballistics for the level-meter dynamic response above the level meter, on the left. To change the ballistics:

- **A.** Select the **Settings** icon ( ) and then select **Audio** .

- **B.** From the **Bar Ballistics** list, select **True Peak** , **PPM Type1** , or **PPM Type2** .

## **Test Level and Peak Program Level Indicators**

The arrows or diamonds next to the level bars indicate the Test level (in yellow) and Peak level (in red) limits for the display. Test level is also known as Reference level or Line-up level.

## **Level Meter Scale and Units**

By default, the units are in dB relative to full scale (dBFS). The 0 dB mark is digital Full scale.

## **Lissajous Display**

The phase of a selected pair of audio channels is plotted on a soundstage plot. Soundstage plots the two channels at 45-degree angles, with the mono combination appearing on the vertical axis, much like a left-right image in a studio.

To select the audio channel pair to plot on the Lissajous display, select the **Volume** icon ( ) on the status bar and choose from the list of available channel pairs.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **302 Application Information** Audio Application

## **Channel Correlation Meter**

The Channel Correlation Meter displays the channel correlation under the Lissajous display.

- For identical or highly correlated signals, the indicator is white and moves to the far right (+1).

- For highly correlated signals, the indicator is green and moves to the right (towards +1).

- For uncorrelated signals, the indicator is yellow and tends to stay in the middle (around 0).

- For anti-correlated signals (one goes up when the other goes down), the indicator is red and moves to the left (towards -1).

## **Level Meter Bar Messages**

This instrument displays information within the level meter bars. These are messages that can appear and are shown in order of priority:

- **UNLOCKED:** The instrument is not locked to an incoming signal on the indicated input channel. Data cannot be decoded and all data and other errors are ignored. This means that if an input is selected, nothing recognizable is present on the input, or if embedded audio is selected, the VIDEO input is unrecognizable.

- **PARITY:** The incoming subframe does not have even parity as specified by the digital audio standards. The data sample is unreliable and is ignored. The level meters and Lissajous display treat the sample as a zero sample.

- **CRC ERR:** The CRC code in the channel status packet is incorrect. Sometimes the CRC code is set to zero, indicating that the signal is missing; when this is the case, this message is not displayed.

- **MUTE:** The number of consecutive all-zero samples equals or exceeds 10.

- **SILENCE:** The signal is below -70 dB for 5 seconds or more.

- **V BIT:** Indicates that the Validity bit is set high for one or more data samples. In the AES/EBU standard, a set validity bit indicates that the sample is not suitable for conversion to audio. By default, the level meter bars and Lissajous

- **NOT PRESENT:** Indicates that an audio bar is not present in the current audio input. For example, if a Dolby Digital input has a coding mode indicating a reduced number of channels.

- **DOLBY D, DOLBY D+, DOLBY E, DOLBY ED2:** Indicates that the specified type of Dolby encoded audio is present on the channel or channels.

- **CLIP:** Indicates the audio level was at the digital code for the maximum amplitude for ten consecutive samples.

- **OVER:** Indicates when the audio amplitude (level) exceeds the silence level threshold for the specified duration. The default is -2 dB for 1 second. To change the alarm settings, see _Configure Alarms_ .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 303** Audio Application

**Note:** The 32-channel audio is supported with a MPSDP-FMT-8K license. In 8K video with Quad 12G-SDI connection, the first 16 channels (of 32 channels) come from the link A1 and the next 16 channels come from the link B1. To view the 32-channel audio bars, you must select the two Audio applications in two tiles.

## **Lissajous Display**

The Lissajous display is a visual of a user-specified pairing of channel inputs with a channel correlation meter.

To turn on the Lissajous display, in **Aux Display** , select **Lissajous** .

The Lissajous display appears to the right of the Audio bars.

## **Loudness Display**

The Loudness display is a visual of the audio loudness measurements. You can view audio loudness values associated with audio loudness measurements. This instrument maintains a running audio loudness session.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **304 Application Information** Audio Application

**Note:** The Loudness measurement is available for mono, stereo, 5.1, and 7.1 multichannel audio programs.

To turn on the Loudness display, in **Aux Display** , select **Loudness** .

The Loudness display appears to the right of the audio bars.

**Note:** The Audio tile appearance can vary based on the selection of other auxiliary audio displays, including Audio Session or Lissajous Display.

## **Configure the Loudness Display**

**1.** Select the **Settings** icon ( ) on the status bar.

**2.** Select **Audio** .

**3.** Select **Loudness Settings** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 305** Audio Application

**4.** Load a standard:

- Select **EBU R128:2014** or **ATSC A/85:2013** for a predefined loudness metering configuration. This setting also changes the full-scale units between LUFS and LKFS according to the standard.

- Or customize the Loudness Display configuration according to the metering measurement goal or audio content type (dialogue, music, or movie). The Configuration Parameters for Loudness Display table lists the available configuration parameters.

Configuration Parameters for Loudness Display

| **Parameter**                | **Available**<br>**Configurations**                                              | **Notes**                                                                                                                           |
| ---------------------------- | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| LOUDNESS<br>METERING<br>MODE | BS.1770-1 with DI1,<br>BS.1770-2 with DI,<br>Leq(A) with DI,<br>BS.1770-2 w/o DI | Mode implies a weighting function (A-<br>weighting or K-weighting) and gating<br>technique(s) when performing loudness<br>metering. |
| Speech<br>Threshold (%)      | 0 to 100%                                                                        | Threshold above which the Speech Gating is<br>turned on in the DI-enabled metering<br>modes.                                        |
| Loudness<br>Ballistics       | Short Average,<br>Long Average,<br>EBU R128 M                                    | Sets the response of the Loudness meter bar.                                                                                        |
| TARGET<br>LOUDNESS           | 0 to -31LKFS with 0<br>to 10LU tolerance                                         | Sets the intended target loudness (to be<br>highlighted in the Loudness display with<br>appropriate color code).                    |
| LOUDNESS<br>THRESHOLDS       | Loud is 0 to -30 and<br>Quiet 0 to -60 Full<br>Scale Loudness                    | Sets the limits to trigger in-bar status for<br>quiet and loud level.                                                               |

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **306 Application Information** Audio Application

Configuration Parameters for Loudness Display (Continued)

| **Parameter**                                   | **Available**<br>**Configurations** | **Notes**                                                                                                                                                                                                                                                                         |
| ----------------------------------------------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Short-Term<br>Gating Window                     | EBU R128 (3s),<br>Legacy (10s)      | Duration of the sliding windows for short-<br>term loudness measurement.                                                                                                                                                                                                          |
| Full-Scale Units                                | LKFS or LUFS                        | Region specific selection; has no effect on<br>measurement.                                                                                                                                                                                                                       |
| TRUE PEAK<br>DC Block<br>and<br>Emphasis Filter | Enable or Disable                   | DC Block simulates the effect of downstream<br>devices that remove DC.<br>The Emphasis Filter compensates for<br>dispersion effects from Nyquist filters in the<br>broadcast chain that make it difficult to<br>measure and control the peak levels of<br>high‐frequency signals. |

1 Dialogue Intelligence enabled

**Note:** The dialogue intelligence algorithm in PRISM introduces a latency of 2.048 s in the effective measurement of the short-term and infinite Loudness. Other Loudness measurement parameters are not affected by the latency.

The Loudness measurements are updated every 500 ms in the user interface.

Maximum short-term Loudness level can be considered as an alternative to using Loudness range for short audio clips.

## **Change Channels the Loudness Meter Measures**

Select the correct program labels at the bottom of the level bars (green letters mean it is selected). The Loudness meter measures the levels based on the selected audio program.

**Note:** Changing the selected Audio program that the Loudness meter measures changes the headphones or speaker pair, and changing the headphones or speaker pair changes the selected Audio program the Loudness meter measures. Changing the Audio program also resets the Loudness measurement.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 307** Audio Application

**Note:** The low-frequency effects channel (Lfe1) in 5.1 and 7.1 is not used in the loudness calculations.

## **Loudness Meter Labels**

- The labels at the bottom of the audio bars (marked as 1) in this example means it is program 2 and there is a left and a right channel.

- The label at the bottom of the Loudness bar (marked as 2) means it is measuring program 2.

- The green letters in the status bar (marked as 3) mark the channels the Loudness display is measuring and where they are in the channel series.

## **Loudness Meter Controls**

- To start and stop the loudness meter, select the **Play** ( ) or **Stop** ( ) button.

- To reset the measurement run time, select the **Reset** button ( ).

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **308 Application Information** Audio Application

- You can use the controls to independently stop, start, and reset the Audio Session and Loudness measurements.

## **Surround Display**

To turn on the Surround display:

**1.** In **Aux Display** , select **Surround** .

**2.** Turn on the Loudness Meter to monitor the loudness level, if needed; set the **Loudness Meter** to **On** .

**3.** Set Loudness Metering to the preferred type.

- **A.** Select the **Settings** icon ( ).

- **B.** Select **Audio** and then select **Loudness Settings** .

- **C.** In the **LOUDNESS METERING MODE** section, select an option:
  - ♦ **BS.1770-1 plus Dialogue Intelligence**

  - ♦ **BS.1770-2 plus Dialogue Intelligence**

  - ♦ **BS.1770-2**

  - ♦ **Leq(A) plus Dialogue Intelligence**

**Note:** A-weighting—Leq(A)—biases the response toward that of human hearing.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 309** Audio Application

**4.** Set the surround settings:

- **A.** In the Audio tile settings, select **Surround Sound Settings** .

- **B.** In the **Analyzer Layer** section, select the level(s) to view:
  - ♦ **Main Bed:** the lower level of audio;

  - ♦ **Upper Bed:** the top level of audio; or

  - ♦ **Both:** Main Bed Upper Bed together.

- **C.** In the **Phantom Source Indicator** section, select **Main Bed** or **Upper Bed** .

- **D.** If needed, set the **Dominance Indicator** to **On** .

- **E.** If needed, set the **Immersive Dominance Indicator** to **On** .

## **Surround Display Elements**

You can monitor the relative loudness of the individual elements rendered in a surround-sound listening environment. Check the surround sound display for performance parameters and indicators.

## 5.1 Surround Sample

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **310 Application Information** Audio Application

**Note:** The Audio Surround Sound display is provided under license from RTW GmbH & Co. KG.

Phantom Sound Indicator (PSI) bars are on each side of the surround sound display. The bars indicate the location of potential phantom sound sources formed by adjacent channels. The white tick marks on these moving bar indicators show the phantom source locations. The bar length indicates the correlation between the adjacent channels. A short-to-medium length green bar indicates positive correlation between the channels, forming a localized phantom sound source located at the white tick mark. The bar grows to full length and changes color to yellow as the correlation moves to zero, indicating a wide, non-localized sound image. The bar changes color to red for adjacent channels with significant negative correlation. For negative correlations, the ends of the PSI for the L and R channels continue to grow at a 45-degree angle while the other PSIs remain at full length.

- **L-R PSI:** Left-to-right phantom sound indicator bar.

- **L-Ls PSI:** Left-to-left surround phantom sound indicator bar.

- **Dominance indicator:** Shows the position of the subjectively perceived acoustic focal point.

- **L-C / C-R PSI:** Left-to-center and center-to-right phantom sound indicator bar.

- **Phantom source grid:** A measurement of 50 is the center of the left-to-center or center-to-right scales.

- **R-Rs PSI:** Right-to-right surround phantom sound indicator bar.

- **Center volume indicator:** This displays the sound volume of the center channel as a vertical yellow bar between the L and R channels, and connects the ends of the L, C, and R audio level indicators with straight lines.

- **Total volume indicator:** This is the cyan polygon formed by connecting the level indicator end points, showing the total sound volume of the L, R, Ls, and Rs channels. Each connecting line bends away from the center if the two signals have a positive correlation, bends toward the center if the signals have a negative correlation, and do not bend if the signals are uncorrelated.

- **Loudness grid:** This is the ruled scale, radiating from the center, on which the level indicators register their audio level and balance. The scale has tick marks at 10 dB intervals. An additional tick mark indicates the –18 dB level. The –18 dB and –20 dB levels are typically used for aligning audio levels.

- **Ls-Rs PSI:** Left surround-to-right surround phantom sound indicator bar.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 311** Audio Application

## 7.1.4 Surround (Main Bed) Sample

Phantom Sound Indicator (PSI) bars are on each side of the surround sound display. The bars indicate the location of potential phantom sound sources formed by adjacent channels. The white tick marks on these moving bar indicators show the phantom source locations. The bar length indicates the correlation between the adjacent channels. A short-to-medium length green bar indicates positive correlation between the channels, forming a localized phantom sound source located at the white tick mark. The bar grows to full length and changes color to yellow as the correlation moves to zero, indicating a wide, non-localized sound image. The bar changes color to red for adjacent channels with significant negative correlation. For negative correlations, the ends of the PSI for the L and R channels continue to grow at a 45-degree angle while the other PSIs remain at full length.

- **L-R PSI:** Left-to-right phantom sound indicator bar.

- **Dominance indicator (main bed):** Shows the position of the subjectively perceived acoustic focal point. The white crosshair is specifically for the main bed data.

- **L-Ls PSI:** Left-to-left surround phantom sound indicator bar.

- **L-Lbs PSI:** Left-to-left back surround phantom sound indicator bar.

- **Ls-Lbs PSI:** Left surround-to-left back surround phantom sound indicator bar.

- **Level indicator (main bed):** Shows the position of the subjectively perceived acoustic focal point for the main bed of audio data.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **312 Application Information** Audio Application

- **Rbs-Lbs PSI:** Right back surround-to-left back surround phantom sound indicator bar

- **L-C / C-R PSI:** Left-to-center and center-to-right phantom sound indicator bar.

- **Phantom source grid:** A measurement of 50 is the center of the left-to-center or center-to-right scales.

- **R-Rs PSI:** Right-to-right surround phantom sound indicator bar.

- **R-Rbs PSI:** Left-to-left back surround phantom sound indicator bar.

- **Center volume indicator:** This displays the sound volume of the center channel as a vertical yellow bar between the L and R channels, and connects the ends of the L, C, and R audio level indicators with straight lines.

- **Rs-Rbs PSI:** Left surround-to-left back surround phantom sound indicator bar.

- **Total volume indicator:** This is the cyan polygon formed by connecting the level indicator end points, showing the total sound volume of the L, R, Ls, and Rs channels. Each connecting line bends away from the center if the two signals have a positive correlation, bends toward the center if the signals have a negative correlation, and do not bend if the signals are uncorrelated.

- **Loudness grid:** This is the ruled scale, radiating from the center, on which the level indicators register their audio level and balance. The scale has tick marks at 10 dB intervals. An additional tick mark indicates the –18 dB level. The –18 dB and –20 dB levels are typically used for aligning audio levels.

## 7.1.4 Surround (Upper Bed) Sample

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 313** Audio Application

**Note:** If in the Analyzer Layer, the Upper Bed layer (or Both) is selected, but there is no upper bed data, as in non-immersive surround programs like 5.1 or 7.1, the upper bed surround display will be empty (no orange display) because there is no upper bed audio data.

Phantom Sound Indicator (PSI) bars are on each side of the surround sound display. The bars indicate the location of potential phantom sound sources formed by adjacent channels. The white tick marks on these moving bar indicators show the phantom source locations. The bar length indicates the correlation between the adjacent channels. A short-to-medium length green bar indicates positive correlation between the channels, forming a localized phantom sound source located at the white tick mark. The bar grows to full length and changes color to yellow as the correlation moves to zero, indicating a wide, non-localized sound image. The bar changes color to red for adjacent channels with significant negative correlation. For negative correlations, the ends of the PSI for the L and R channels continue to grow at a 45-degree angle while the other PSIs remain at full length.

- **Ltf-Rtf PSI:** Left top front-to-right top front phantom sound indicator bar

- **Dominance indicator (upper bed):** Shows the position of the subjectively perceived acoustic focal point. The orange crosshair is specifically for the main bed data.

- **Level indicator (upper bed):** Shows the position of the subjectively perceived acoustic focal point for the upper bed of audio data.

- **Ltf-Ltr PSI:** Left top front-to-Left top rear surround phantom sound indicator bar

- **Ltr-Ltr PSI:** Left top rear-to-Right top rear surround phantom sound indicator bar

- **Phantom source grid:** A measurement of 50 is the center of the left-to-center or center-to-right scales.

- **Rtf-Rtr PSI:** Right top front-to-Right top rear surround phantom sound indicator bar

- **Center volume indicator:** This displays the sound volume of the center channel as a vertical yellow bar between the L and R channels, and connects the ends of the L, C, and R audio level indicators with straight lines.

- **Total volume indicator (upper bed):** This is the orange polygon formed by connecting the level indicator end points, showing the total sound volume of the L, R, Ls, and Rs channels. Each connecting line bends away from the center if the two signals have a positive correlation, bends toward the center if the signals have a negative correlation, and do not bend if the signals are uncorrelated.

- **Loudness grid:** This is the ruled scale, radiating from the center, on which the level indicators register their audio level and balance. The scale has tick marks at 10 dB intervals. An additional tick mark indicates the –18 dB level. The –18 dB and –20 dB levels are typically used for aligning audio levels.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **314 Application Information** Audio Application

## 7.1.4 Surround (Both Beds) Sample

**Note:** In the Analyzer Layer, the Both layer is selected, but there is no upper bed data, as in non-immersive surround programs like 5.1 or 7.1, the upper bed surround display will be empty (no orange display) because there is no upper bed audio data.

- **Immersive Dominance Indicator:** Shows the position of the subjectively perceived acoustic focal point of all data. The dot is only visible when both beds are shown.

- **Main bed data:** For details of the display, see _7.1.4 Surround (Main Bed) Sample_ .

- **Upper bed data:** For details of the display, see _7.1.4 Surround (Upper Bed) Sample_ .

## **Surround Display Usage Notes**

The displays shown here are examples of how the surround sound waveform appears for some typical signal types.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 315** Audio Application

**Example 1:** Shows uncorrelated signals with the same level in the L, C, R, Ls, and Rs channels.

**Note:** PSI are yellow, showing uncorrelated audio between the channels.

**Example 2:** Shows a sine wave test tone with the same level in the L, C, R, Ls, and Rs channels. All signals are in phase, creating white marks for the phantom source indicators mean that each channel has the same amplitude and frequency.

**Example 3:** This is the same as example 2, with the exception that Channel L is out of phase.

**Note:** The PSIs are in red for L-R, L-Ls, and L-C.

**Example 4:** Shows the surround sound program with strong center-channel presence, typically from high dialogue audio levels compared to other channels.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **316 Application Information** Audio Application

**Example 5:** Shows a surround sound program with weak center-channel presence, likely with a lower dialogue level compared to other channels.

**Example 6:** Shows a monaural signal in channels Ls and Rs, creating a phantom source in the center, as in a 5.1 surround sound system. Typically, a mix could contain a copy of the L and R channel at a lower level in the Ls-Rs to create a pseudo surround mix. The white marks mean a monaural channel for Ls and Rs. The other channels are uncorrelated.

## **Loudness Meter**

The Loudness Meter is part of the Audio application, and it is configured in the Audio Settings menu. The Audio Loudness Meter allows you to view audio loudness values associated with audio loudness measurements. This instrument maintains a running audio loudness session.

To turn on the audio loudness values, set **Loudness Meter** to **On** .

The Loudness Meter appears to the right of the audio bars.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 317** Audio Application

**Note:** Loudness measurements are not supported for more than eight channels, so the Loudness Meter does not function with 5.1.4 or 7.1.4 programs.

PRISM supports Audio Loudness Alarms. Changing the active audio program will reset the Infinite Loudness measurements. So, you must stop the Loudness measurements in the audio application if you want to listen to the audio output or measure the loudness of a different audio program.

## **Audio Session**

Audio Session consists of several performance parameters for an overview of the audio input signal.

To turn on the audio signal overview, set **Audio Session** to **On** .

The Audio Session appears below the audio bars.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **318 Application Information** Audio Application

## **Downmix Solo**

To isolate and identify an unexpected noise in a stream, you can select one channel of a downmixed 5.1 or 7.1 stream and listen to it separately.

To use Downmix Solo:

**1.** In the Audio Settings, set **Downmix Solo** to **On** .

**2.** Select the **Volume** ( ) icon in the status bar.

**3.** In the volume controls, select the **downmix** button.

**4.** Select the **Home** icon ( ) to close the volume controls.

**5.** Select a channel to isolate in the Audio application:

- To change the solo channel, select another channel in the downmixed stream.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 319** Dolby Status Application

- To return to the entire downmixed stream (without turning Downmix Solo off), select the highlighted channel again.

## **Dolby Status Application**

**Note:** In multi-input mode, Dolby Status works only with the primary channel.

Dolby Status supports all Dolby metadata for the currently monitored input. The application tile indicates whether Dolby audio is available in the monitored input.

**Note:** The Dolby Status application requires software options MPSDP-AUD or MPSDPDLBY.

If the instrument has Dolby monitoring capabilities, it can decode and monitor audio signals that are based on Dolby digital surround sound formats. These formats are Dolby D (AC-3)/D Plus (E-AC-3) compression (designed for distribution) and Dolby E compression (designed for production).

To refresh the Dolby Status data, select the **Refresh** icon ( &) ) at the top of the Dolby Status tile.

If information on the Dolby Status page should have updated but did not, for example the Program Desc Text has not updated, click the **Refresh** icon to update the data.

This sample shows Dolby D data.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **320 Application Information** Dolby Status Application

This sample shows Dolby E data with the external reference measurement.

This sample shows Dolby ED2 data with a Presentation option (in the top right corner) selected.

**Note:** Presentation titles are user-selected. You can change them to refer to the related information as needed.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 321** Dolby Status Application

This sample shows Dolby Timing.

## **Configure the Dolby Status Application**

**1.** Select the **Tiles** icon ( ).

**2.** Select the tile with the Dolby Status application.

**3.** Select the **Tile** icon ( ).

**Note:** To move the settings left or right, select the **Move** icon ( - ) in the Settings menu header.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **322 Application Information** | Dolby Status Application

**4.** You can select the source of the Dolby E metadata from the incoming Dolby E audio if the instrument is decoding Dolby E audio or from VANC metadata if the Dolby E is decoded externally. In the **Metadata Source** section, select one of the following:

- **Auto:** Selects the Dolby E audio by default as the metadata source, if it is available. If Dolby E audio is not available, it uses VANC audio.

- **AES:** Selects the Dolby E audio as the metadata source. The Dolby Status application is blank if Dolby E is not being decoded.

- **VANC:** Selects VANC as the metadata source. The SDID must be properly selected.

**5.** The **DID** section indicates the data identifier of the requested packet; it is set to 0x45 (69 decimal) and is not changeable.

**6.** In the **SDID** box, specify the Secondary Data Identifier of the requested packet. An SDID value of 01h is used when there is only one audio program associated with a video signal and there is no intended association between VANC packets with an SDID value of 01h and a specific audio channel pair.

Association Between the First Audio Channel Pair of an Audio Program and the SDID Values

| **Audio Channel Pair** | **SDID** |
| ---------------------- | -------- |
| No association         | 01h      |
| Channel pair 1/2       | 02h      |
| Channel pair 3/4       | 03h      |
| Channel pair 5/6       | 04h      |
| Channel pair 7/8       | 05h      |
| Channel pair 9/10      | 06h      |

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 323** Dolby Status Application

Association Between the First Audio Channel Pair of an Audio Program and the SDID Values (Continued)

| **Audio Channel Pair** | **SDID** |
| ---------------------- | -------- |
| Channel pair 11/12     | 07h      |
| Channel pair 13/14     | 08h      |
| Channel pair 15/16     | 09h      |

When multiple audio programs are carried by or associated with a single video signal, the SDID value is used to identify the VANC data packets carrying the audio metadata for each audio program.

The audio channels making up an audio program are assigned to consecutively numbered or consecutively arranged audio channel pairs. The VANC packets carrying the audio metadata for a specific audio program are identified by setting the SDID values of these packets to the value associated with the lowest numbered audio channel pair of the group of audio channel pairs carrying the complete audio program.

For example, if there is a six-channel program carried in the first three audio channel pairs and a stereo program carried by the fourth audio channel pair, then the VANC packets carrying the metadata for the six-channel program would have their SDID value set to 02h because the program starts in audio channel pair 1/2. The VANC packets carrying the metadata for the stereo program would have their SDID value set to 05h because the stereo program starts in audio channel pair 7/8.

**7.** From the **Dolby Program** list, select the Dolby program number to monitor. The Program number on the top right of the Dolby Status application border is the same as the Dolby Program number in the Dolby Status Settings. Select the arrow and select the number of the program to monitor.

## **Dolby D/D Plus/E Status Elements**

This section describes some elements that appear in the Dolby Status application for Dolby D, D Plus, or E. For a complete list of the elements that might appear, see the Dolby Metadata Guide at the _Dolby website_ .

- **Program Desc Text** is a 32-character ASCII text field that the program author uses to describe the audio program; for example, the name of the program (Movie Channel Promo), the program source (Football Main Feed), or the program language (Danish).

- **Dolby Format** indicates the Dolby Format. This indicator is also tied to the Dolby Format Error/Alarm: if the Alarm is asserted, the Dolby Format is displayed in red.

- **Channel Mode** (or Audio Coding Mode) indicates the active channels within the encoded bit stream, representing it in a ratio, X/Y, where X is the number of front channels (Left, Center, Right) and Y is the number of rear (Surround) channels. If the LFE Channel is present, an L is added at the end of the channel mode.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **324 Application Information** Dolby Status Application

- **Program Config** determines how the audio channels are grouped in a Dolby E bitstream. Up to eight channels can be grouped together in individual programs, where each program contains its own metadata.

- **Metadata Source** indicates the input from which the Dolby Content is sourced.

- For Dolby E, **Dolby Data Rate** indicates the data rate that would be used to encode a Dolby Digital bitstream.

- **Bitstream Mode** describes the audio service in the Dolby Digital bitstream. A complete audio program can consist of a main audio service (a complete mix of all the program audio), an associated audio service comprising a complete mix, or a main service combined with an associated service. For more information about possible values, see the instrument online help; when the Dolby Status display is active in a tile, select the HELP button.

- **Dolby E Frame Rate** displays the frame rate of the Dolby E audio. If Dolby Frame Rate is not the same as the video Frame Rate, the rate value is displayed in red.

- **Dolby E Frame Loc** displays the location (line number and sample number) of the ST 337 preamble.

- **Dolby ExtRef Guardband** displays the location (line number and sample number) of the corresponding black-burst reference that aligns with the ST 337 preamble.

- **Dialogue Level** represents the long-term, A-weighted average level of dialog within a presentation, Leq(A).

## **Dolby ED2 Status Elements**

This section describes some elements that appear in the Dolby Status application for Dolby ED2. For a complete list of the elements that might appear, see the Dolby Metadata Guide ot the _Dolby website_ .

- The **Dolby E(Pair 1) 1-2 and Dolby E(Pair 1) 3-4** tabs in the Dolby Status tile have most of the same elements as the Dolby D, D Plus, and E data. For more details, see _Dolby D/D Plus/E Status Elements_ .

- The **Dolby ED2** tab in the Dolby Status Tile has the following elements:
  - Evolution pair 1(1-2) and Evolution pair 2(3-4): Describes the status of the channel pairs (in parentheses) of the ED2 transport.

  - Type: This is the audio object type, such as Bed or Dynamic.

  - Index: This is the object number starting after the Audio Bed.

  - Position X, Position Y, Position Z: This positional metadata describes the audio objects in the bitstream.

- The **Dolby Timing** tab in the Dolby Status Tile has these elements:
  - Dolby E Frame Loc (pair 1) and Dolby E Frame Loc (pair 2): Displays the line, field, and sample numbers of the of the corresponding video of the Dolby ED2 preamble.

  - Ext Ref Guardband (pair 1) and Ext Ref Guardband (pair 2): Displays the line, field, and sample number of the corresponding black-burst reference that aligns with

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 325** AES Channel Status Application

the Dolby E preamble location. Make sure the Dolby E preamble location stays in field 1 of the reference signal. If it stays in field2 of the reference, the Dolby E stream might corrupt at signal switching.

Before checking this measurement, make sure that Analog or PTP is selected (in Setting and then the Reference menu) and the incoming signal is locked to a reference signal on the status bar.

## **AES Channel Status Application**

**Note:** In multi-input mode, AES Channel Status works only with the primary channel.

The AES Channel Status application provides detailed data for each audio channel in the monitored signal, up to 16 channels total. It is available only for SDI.

The data is presented by channel in transport order, regardless of how the Audio application maps or configures the channels.

**Note:** Only Professional mode (in Channel Use) is available.

If the two Block CRC lines ( _should be_ and _computed_ ) do not match, the Block CRC ( _computed_ ) line turns red as a warning that the numbers are mismatched and a CRC error has happened.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **326 Application Information** Event Log Application

## **Event Log Application**

The Event Log application provides a view of detected errors. The display buffer for the application shows 1,000 log entries.

**Note:** To see the available columns (Notes and Date), set the application to fullscreen.

## **Event Log Elements**

- **Reset icon** : Select the reset icon ( ) to hide all log items, so only new log items are displayed. Select **Undo Reset** in the settings menu to show the log items that were hidden by pressing Reset.

- **Track icon:** The Track icon ( ) and the text “Tracking” to the left mean the Event Log is tracking new events. The newest events appear at the bottom of the Event Log.

Scroll in the Event Log list or select -and-hold the control and move to a previous event. Tracking new events is automatically paused.

- **Pause icon** : The **Pause** icon ( ) and the text “Paused” means the Event Log is not tracking new events. Select the Pause icon to return to tracking new events.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 327** Event Log Application

The Error Log has the following columns:

- **Group:** Lists the group the event is related to and shows the current state of the log entries:
  - Red-rising edge ( ) items are detected errors.

  - ○ Green-falling edge ( S%

  - Green-falling edge ( ) items are errors that have cleared.

  - Red and green-rising and falling edge ( fi ) items indicate a momentary error that was in error condition but is now in normal condition. The PTP or TC field is blank when the selected time source is not available.

The following alarms do not have a momentary event status:

      - ♦ SDI Active Field Length Error

      - ♦ SDI Total Field Length Error

      - ♦ SDI Line Length Error

      - ♦ SDI EAV Placement Error

      - ♦ SDI SAV Placement Error

      - ♦ SDI Line Number Error

      - ♦ SDI Y-channel CRC Error

      - ♦ SDI C-channel CRC Error

      - ♦ SDI Y-channel ANC Checksum Error

      - ♦ SDI C-channel ANC Checksum Error

      - ♦ SDI EDH Active Picture CRC Error

      - ♦ SDI EDH Full-field CRC Error

      - ♦ Ethernet CRC Error

- White items are informational and identify a change in instrument state.

- **Event:** Lists the title of the error.

- **PTP (UTC)** or **TC (LTC):** Shows the time, in the mode chosen by the user, the error occurred.

- **Date:** Shows the date, according to the internal clock, that the error occurred in the form YYYY-MM-DD.

- **Time:** Shows the time, according to the internal clock, that the error occurred in the form HH:MM:SS.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **328 Application Information** Event Log Application

## **Configure the Event Log Application**

**1.** Select the **Tiles** icon ( ).

**2.** Select the tile with the Event Log application.

**3.** Select the **Tile** icon ( ).

**Note:** To move the settings left or right, select the **Move** icon ( ) in the Settings menu header.

**4.** In the **Timestamp Selection** section, select one of the following:

- **Timecode:** To set TC (LTC) or TC (VITC) for error tracking in the Event Log. To configure TC (LTC) or TC (VITC):

- **i.** Select the **Settings** icon ( ), then select **Anc Data** .

- **ii.** In **Timecode Format** select **LTC** or **VITC** .

- **PTP:** To set PTP (UTC) for error tracking in the Event Log.

To cancel the last reset of the logged events, select **Undo Reset** .

## **Filter Events**

This section explains how to sort logged events in the Event Log.

## **Filter by Group**

- To open the group filter, select the **Group** heading.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 329** Event Log Application

**Note:** If there is any other filter applied (Event, Date, Time—marked by a full filter icon ( hd ) next to a heading), it limits what any other filter shows. For example, if no events are selected in the Event filter, then no errors appear even if all the groups are selected.

- To move the menu, select-and-hold anywhere in the menu and drag it.

- To select all checkboxes (see all errors), or clear all (hide all errors), select the **All Groups** checkbox. The Event Log immediately adds or removes errors from the list.
  - If all groups are selected (no filter), the Group filter icon is empty.

  - If any group is not selected (a filter is applied), the Group filter icon is full **.**

- To select or remove the check from any single checkbox, select anywhere in the title line.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **330 Application Information** Event Log Application

## **Filter by Event**

- To open the event filter, select the **Event** heading.

**Note:** If there is any other filter applied (Group, Date, Time—marked by a filled filter icon— hd —next to a tile), it limits what any other filter shows. For example, if no groups are selected in the Group filter, then no errors appear even if all the events are selected.

- To move the menu, select-and-hold anywhere in the menu and drag it.

- To select all checkboxes (see all errors), or remove all checks (hide all errors), select the **All Events** checkbox. The Event Log immediately adds or removes errors from the list.
  - If all groups are selected (no filter), the filter icon is empty.

  - If any group is not selected (a filter is applied), the filter icon is full.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 331** Event Log Application

- To select or remove the check from any single checkbox, select anywhere in the line of the title.

- To scroll through the list of events, select the arrows at the top and bottom of the menu.

## **Filter by Date or Time**

- To open the Date and Time filter, select the **Date** or **Time** heading. Both open the same menu.

**Note:** If there is any other filter applied (Group, Event—marked by a filled filter icon— hd —next to a tile), it limits what any other filter shows. For example, if no groups are selected in the Group filter, then no errors appear even if all the events are selected.

- To move the menu, select-and-hold anywhere in the menu and drag it.

- To enter a filter date:
  - Select in the **Date From** box and either type a date (yyyy-mm-dd) or select the date using the on-screen Adjust Date tool.

  - If needed, select a date in the **Date To** box.

**Note:** Other filters (duration, time) are not required.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **332 Application Information** Event Log Application

- To enter a filter time:
  - Select in the **Time From** box and either type a time (hh-mm-ss) or select the time using the on-screen Adjust Time tool, and select **Enter** .

  - If needed, select a time in the **Time To** box.

**Note:** Other filters (duration, date) are not required.

- To enter a duration filter, select in the **Duration** box and type the number of hours or use the on-screen keypad, and select **Enter** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 333** IP Status Application

## **Note:** Other filters (date, time) are not required.

- If no date, duration, or time filter is entered (no filter), the filter icon is open.

- If a date, duration, or time filter is entered (a filter is applied), the filter icon is filled.

## **IP Status Application**

The IP Status application provides an overview of the monitored IP stream and shows the status of each program in the stream. After the input signals have been subscribed to using the input settings menu, the traffic on the SFP ports can be viewed using the IP Status application. The application is available only in the 200 and 300 versions of MPS, MPD, and MPP.

Use this application if there are possible IP signal integrity issues. If a flow has a red X, PRISM has detected issues. The next application to use is the IP Session. Depending on

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **334 Application Information** IP Status Application

the network switch deployed, the traffic might not appear in the IP Status application immediately.

## **Configure the IP Status Application**

**1.** Select the **Tiles** icon ( ).

**2.** Select the tile with the IP Status application.

**3.** Select the **Tile** icon ( ).

**Note:** To move the settings left or right, select the **Move** icon ( = ) in the Settings menu header.

**4.** To monitor both Port 1 and Port 2, select **Both** .

If you select both ports, two traffic bars show the amount of traffic on each port, and there is a traffic table with a Port column.

- The active monitored streams are always displayed at the top of the list.

- The columns are sortable.

- The selected input is now highlighted in the ID column.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 335** IP Status Application

- When the row has a yellow gradient, it indicates a signal that was present and is now gone. Select the reset button at the right side of the banner (at the top) to clear the signals that are no longer there.

## **Status Indicators**

In the left column of an IP Status tile, the following indicators describe the signal parameter:

The signal parameter has not been in an error condition.

The signal parameter was in an error condition but the error has cleared.

The signal parameter is in an error condition.

The signal parameter is not being monitored for an error condition.

The following backgrounds indicate the flow status:

- A green background means the flow is present and selected.

- A black background means the flow is present but not selected.

- A yellow background means the flow was present but is not present now.

## **Elements of IP Status Display**

- **Port 1** and **Port 2:** Status of Port 1 and Port 2.

- **Total:** Shows the total bit rate of the video in the IP stream.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **336 Application Information** IP Status Application

- **IP stream bandwidth bar:** The blue bar outline at the top of the display represents the total bandwidth of the 10GE or 25GE stream, depending on the type of SFP that is present. The blue bars inside the outline show the relative bandwidth size of items in the IP stream compared to the total available bandwidth of the stream. Numbers inside the blue bars correspond to the ID numbers listed in the display.

- **Run Time:** The instrument maintains a running IP Status Session. The Run Time readout displays the amount of time that has elapsed during the current IP Status Session. The time is displayed as “DD, HH:MM:SS”, where DD is number of days, HH is number of hours, MM is number of minutes, and SS is number of seconds.

- **Reset icon:** Select the Reset icon ( B) ) to reset the status session. After a reset, items appear in the list in the order they are detected.

The IP Status application is divided into these columns:

- **ID:** Shows the ID number of each item in the IP stream. The ID numbers correspond to the numbers in the blue bar at the top of the display.

- **PORT:** Shows the Port number being monitored.

- **STRM:** Shows the stream number for a given media type for that row. For example, STRM 1 is the first audio stream in the input settings.

- **CH:** When in multi-input mode, the Virtual Channel will be indicated.

- **PROTOCOL:** Shows the protocol being used by each item in the IP stream.

- **BITRATE:** Shows the bit rate of each item in the IP stream.

- **PAYLD:** Shows the RTP Payload Type number of each IP stream.

- **DEST IP:** Shows the destination IP address and port number of the monitored stream in the format <destination IP address>:<port number>.

- **SOURCE IP:** Shows the source IP address and port number of the monitored stream in the form <source IP address>:<port number>.

- **DEST MAC:** Shows the destination MAC address of the monitored stream.

- **SOURCE MAC:** Shows the source MAC address of the monitored stream.

- **PTP DOM:** Shows the PTP domain of the monitored stream.

- **SEQ ERR:** Shows the number of sequence errors in the monitored stream.
  - IN-Error count means “IN”-coming stream errors.

  - CORR-Error count means after “CORR”-ection process of packet reordering or ST 2022-7. Zero means no errors occurred since reset. Steady count mean errors are not occurring. Increasing count means new errors are occurring.

- **RTP CLK:** Shows the RTP clock of the monitored stream.

- **RTP MARK:** Shows the RTP marker frequency of the monitored stream.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 337** IP Session Application

## **IP Session Application**

The IP Session application displays the status of various IP stream parameters. Select any of the tab titles to view the associated information: Layer 1/2, Video, Audio, Data, PTP, or NMOS. The application is available only in the 200 and 300 versions of MPS, MPD, and MPP.

**Note:** Option MPSDP-IP-MEAS must be installed to use the IP Session application. The display shows only Path 1 unless you enable ST 2022-7 Seamless Switching (see _Configure ST 2022-6_ ). There is a difference between “Port” and “Path.” The Port is the physical SFP port that is used to input the IP signal. Path 1 and Path 2 are the signal paths to be used for seamless switching. This differentiation is being made because it is possible for both Path 1 and Path 2 to use a single Port.

## **Configure the IP Session Application**

**1.** Select the **Tiles** icon ( ).

**2.** Select the tile with the IP Session application.

**3.** Select the **Tile** icon ( ).

**Note:** To move the settings left or right, select the **Move** icon ( - ) in the Settings menu header.

**4.** In the **Audio** list, select the audio stream for the selected input to monitor. The selected audio stream is noted in the Audio tab.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **338 Application Information** IP Session Application

## **IP Session Header Elements**

The elements at the top of the IP Session application are shared between several tabs. Select a tab to view the associated display. Each tab has a status indicator to provide a quick view of the status of the parameters in each tab.

- Select **Layer 1/2** to view the status of various signal parameters in the physical and link layers.

- Select **Video** to view the status of the video in the stream.

- The **AUDIO** tab label indicates which stream is being monitored. For example, AUDIO-1 indicates stream 1 as configured in the Settings – Input menu. In the application menu, select the Audio stream to monitor.

- The **Data** tab label indicates which stream is being monitored. For example, Data-1 indicates stream 1 as configured in the Settings – Input menu. In the application menu, select the Data stream to monitor.

- Select **PTP** to view PTP parameters.

- Select **NMOS** to view information on the registration server and the last Session Description Protocol (SDP) files received.

The instrument maintains a running monitoring session for the IP Session application. The Run Time readout displays the amount of time that has elapsed during the current monitoring session. The time is displayed as “DD, HH:MM:SS”, where DD is number of days, HH is number of hours, MM is number of minutes, and SS is number of seconds.

Select the **Reset** icon ( ) to reset the monitoring session.

When the monitoring session is running (collecting error data), select the **Stop** icon ( C) ) to stop the session. When the session is stopped (no error data collection and no display updates), select the **Play** icon ( ) to start the session.

## **LAYER 1/2 Tab**

**Note:** In multi-input mode, LAYER 1/2 works with both primary and secondary channels.

To view the status of these signal parameters, select the **LAYER 1/2** tab.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 339** IP Session Application

## ● **Layer 1:**

- **10GbE Link or 25GbE Link:** Shows the status of the link connection.
  - ♦ **Disconnected:** No SFP module present.

  - ♦ **No Signal:** No input signal detected.

  - ♦ **OK:** Locked to input signal.

- SFP Loss of Signal (LOS):
  - ♦ **Disconnected:** No SFP module present.

  - ♦ **OK:** Locked to input signal.

**Note:** The functionality of this signal depends on the brand of SFP installed. The signal is intended as a preliminary indication that the received signal strength is below a range specified by the SFP vendor. Such an indication typically points to noninstalled cables, broken cables, or a disabled, failing or powered-off transmitter at the far end of the cable.

## ● **Layer 2:**

- **Lock:** Shows the lock status of the link:
  - ♦ **OK:** The 10/25G Ethernet Phy Rx port is successfully locked to the inbound Ethernet signal.

  - ♦ **ERROR:** The 10/25G Ethernet Phy Rx port lost lock to the incoming Ethernet signal during the last second. This indicates there is likely a physical layer problem with the link.

- CRC Error columns:
  - ♦ **STATUS:** There have been no overflow errors in the Ethernet MAC during the last second.

  - ♦ **ERR SECS:** This is an interval of a second during which any error has occurred, regardless of whether that error was a single-bit error, or a complete loss of communication for that entire second.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **340 Application Information** IP Session Application

## ● **Layer 2 Metrics:**

- **Rx Bytes:** A count of the number of bytes received

- **Rx BER High:** The Sync Header BER is greater than 10-4

- **Rx CRC Errors:** A count of the number of CRC errors detected

- **Rx Frames Ok:** A count of the number of Ethernet frames received without error

- **Rx Frames Errored:** A count of the number of Ethernet frames received with errors detected

- **Rx Undersize Packets:** A count of the number of Ethernet frames received that are less than 64 bytes long

- **Rx Oversize Packets:** A count of the number of Ethernet frames received that are greater than 1522 bytes long

- **Tx Bytes:** A count of the number of bytes transmitted

- **Tx Frames Ok:** A count of the number of Ethernet frames transmitted without error

- **Tx Frames Errored:** A count of the number of Ethernet frames transmitted with errors detected

## **VIDEO Tab**

To view the status of the video in the stream, select the **VIDEO** tab.

## ● **L3 IP:**

- **Source Addr:** Lists the source addresses for the L3 IP layer.

- **Destination Addr:** Lists the destination addresses for the L3 IP layer.

- **L4 UDP:**

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 341** IP Session Application

- **Source Port:** Lists the source ports for the L4 UDP layer.

- **Destination Port:** Lists the destination ports for the L4 UDP layer.

- **L5 RTP:** Lists these parameters of the L5 RTP (Real Time Protocol) layer. RTP Datagrams are defined in IETF RFC 3550.
  - **Version:** Identifies the version of RTP and should be a value of 2.

  - **Padding:** Indicates whether padding bytes are present. Possible values are:
    - ♦ **false:** Indicates no extra padding bytes are at the end of the RTP packet.

    - ♦ **true:** Indicates that padding octets have been added to the RTP packet that are not part of the payload.

  - **Extension:** Indicates whether an extension is present. Possible values are:
    - ♦ **false:** Indicates no extension is present.

    - ♦ **true:** Indicates an extension is present.

  - **CSRC:** Identifies the contributing source IDs. This value should be set to zero.

  - **Marker:** This value should be set to 1 to indicate the last Media Datagram of the video frame. The value is set to 0 for all other Media Datagrams and should be 0 for most packets.

**Note:** For ST 2022-6 signals, the status indicator turns red if the Marker Bit Frequency does not match the frame rate indicated in the HBRMT header. For ST 2110 signals, the status indicator turns red if the Marker Bit Frequency does not match the measured field rate of the detected format.

- **Payload type:** Identifies the type of RTP payload:
  - ♦ **98:** Indicates an ST 2022.6 High Bit Rate Media Transport.

  - ♦ **99:** Indicates an ST 2022.5 High Bit Rate Media Forward Error Correction (FEC) payload.

  - ♦ **33:** Indicates an ST 2022.2 Constant Bit Rate MPEG-2 Transport Stream Adaptive Sample Picture Encapsulation (ASPEN) payload.

**Note:** The payload type for ST 2110 streams should be between 96 and 127. The payload type is set by the user.

- **Sequence number:** RTP sequence counter that changes by one for each RTP Media Datagram sent.

**Note:** The status indicator turns red if the received RTP sequence numbers do not change by 1 on every packet.

- **Time Stamp:** Reflects the sampling instant of the first octet in the RTP datagram. This value can be used to determine packet sequence errors and jitter calculations to be made.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **342 Application Information** IP Session Application

**Note:** For ST 2022-6 signals, the status indicator turns red if the Time Stamp field does not change at the rate of 27 MHz on every packet. For ST 2110 signals, the status indicator turns red if the Time Stamp field does not change at the start of every field or frame at the rate of 90 kHz on every packet.

- **SSRC:** Identifies the Synchronization Source ID and is set in compliance with RFC3550. This identifier is chosen randomly and should be unique so no two SSRC have the same value with an RTP session.

- **Interface Sampling Frequency Error:** This error indicates that the incoming video is arriving at a frequency outside of the supported range to maintain stable video lock. The signal on the SDI Out video connector might be affected. Possible interface sampling frequency declaration in stream header is incorrect for the stream type being carried.

**Note:** The status indicator turns red if the received frame rate is not stable enough during conversion to SDI. Marker Bit Frequency Errors can also trigger this indicator.

- **HBRMT:** Lists these parameters of the High Bit Rate Media Payload Header:

**Note:** The HBRMT parameters apply only to ST 2022-6 streams.

- **Video Source Format:** Identifies whether source formatting is present:
  - ♦ **Not Present:** Indicates no Source Format information is present.

  - ♦ **Present:** Indicates source formatting is present.

- **Video Source ID:** Identifies the video source:
  - ♦ **Primary (0x0):** Indicates a primary stream.

  - ♦ **Protect (0x1):** Indicates a protected stream.

  - ♦ **Reserved (n):** When _n_ is a number other than 0 or 1, indicates that a reserved value is being used.

- **Frame Count:** The Video Frame counter changes in value for the next RTP sequence and rolls over after 255.

**Note:** The status indicator turns red if the frame count field does not change by 1 at the start of every frame.

- **Reference for time stamp:** Identifies the time stamp reference:
  - ♦ **Unlocked (0x0):** Indicates the time stamp is not locked to any particular source.

  - ♦ **Reserved (0x1):** Indicates an illegal value.

  - ♦ **UTC (0x2):** Indicates the time stamp is locked to a UTC time source.

  - ♦ **Private (0x3):** Indicates the time stamp is locked to a private time source.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 343** IP Session Application

- **Video Payload Scrambling:** Identifies the payload scrambling status:
  - ♦ **Unscrambled (0x0):** Indicates the payload is not scrambled.

  - ♦ **Reserved (n):** When _n_ is a number other than 0, it indicates a reserved value is being used.

- **FEC usage:** Identifies the FEC usage status:
  - ♦ **No FEC (0x0):** Indicates no forward-error correction is being used.

  - ♦ **Column (0x1):** Indicates column FEC is being used.

  - ♦ **Col/Row (0x2):** Indicates column and row FEC are being used.

  - ♦ **Reserved (n):** When _n_ is a number greater than 2, indicates a reserved value is being used.

- **Clock Frequency:** Identifies the video word clock frequency of the payload video. Possible values are:
  - ♦ **0000:** No time stamp

  - ♦ **0001:** 27 MHz

  - ♦ **0010:** 148.5 MHz

  - ♦ **0011:** 148.5 /1.001 MHz

  - ♦ **0100:** 297 MHz

  - ♦ **0101:** 297/1.001 MHz

  - ♦ **0110-1111:** Reserved

- **Reserved:** This value should be set to 0.

- Video Source Format fields: These Video Source Format field values are displayed:
  - ♦ **MAP:** Identifies which SMPTE mapping scheme is used. Possible values are: Direct (0x0), LevelB (0x1), 2xHD (0x2), or Reserved (n).

  - ♦ **FRAME:** Identifies the raster size. Possible values are: Unspecified (0x0), 720x480i (0x10), 720x576i (0x11), 1920x1080i (0x20), 1920x1080p (0x21), 1920x1080sf (0x22), 2048x1080p (0x23), 2048x1080sf (0x24), or 1280x720p (0x30).

  - ♦ **F rate:** Identifies the frame rate. Possible values are: Unknown/Unspecified frame rate 2.970 GHz signal (0x00), Unknown/Unspecified frame rate 2.970/ 1.001 GHz signal (0x01), Unknown/Unspecified frame rate 1.485 GHz signal (0x02), Unknown/Unspecified frame rate 1.485/1.001 GHz signal (0x03), Unknown/Unspecified frame rate 0.270 GHz signal (0x04), Reserved (0x040x0f), 60 (0x10), 60/1.001 (0x11), 50 (0x12), Reserved (0x13), 48 (0x14), 48/ 1.001 (0x15), 30 (0x16), 30/1.001 (0x17), 25 (0x18), Reserved (0x19), 24 (0x1A), 24/1.001 (0x1B), Reserved (0x1C-0xFF).

  - ♦ **Sample:** Identifies the pixel sampling/quantization scheme. Possible values are: Unspecified (0x0), 4:2:2/10 bit (0x1), 4:4:4/10 bit (0x2), 4:4:4:4/10 bit (0x3), 4:2:2/12 bit (0x5), 4:4:4/12 bit (0x6), 4:4:4:4/12 bit (0x7), or 4:2:2:4/12 bit (0x8).

  - ♦ **Fmt** - **Reserve:** This bit is reserved for future use and is set to 0.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **344 Application Information** IP Session Application

- **Video TimeStamp:** Shows the value of a free-running counter that is synchronous with the interface word clock of the encapsulated video. This time stamp is fixed at the transmitter to the first information in the datagram.

- **Header Extension:** Indicates the number of 4-octet header extension words that come after the HBRMT payload.

## **Audio Tab**

The AUDIO tab label indicates which stream is being monitored. For example, AUDIO-1 indicates stream 1 as configured in the Settings – Input menu. Select the Audio stream to monitor in the application menu.

## **Configure the Audio Stream**

**1.** Select the **Tile** icon ( ) in the application bar.

**2.** Select the **Audio** tab and select the stream number to monitor. The selected audio stream is noted on the AUDIO tab.

## **AUDIO Tab Elements**

- **L3 IP:**
  - **Source Addr:** Lists the source addresses for the L3 IP layer.

  - **Destination Addr:** Lists the destination addresses for the L3 IP layer.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 345** IP Session Application

- **L4 UDP:**
  - **Source Port:** Lists the source ports for the L4 UDP layer.

  - **Destination Port:** Lists the destination ports for the L4 UDP layer.

- **L5 RTP:** Lists these parameters of the L5 RTP (Real Time Protocol) layer. RTP Datagrams are defined in IETF RFC 3550.
  - **Version:** Identifies the version of RTP and should be a value of 2.

  - **Padding:** Indicates whether padding bytes are present. Possible values are:
    - ♦ **false:** Indicates no extra padding bytes are at the end of the RTP packet.

    - ♦ **true:** Indicates that padding octets have been added to the RTP packet that are not part of the payload.

  - **Extension:** Indicates whether an extension is present. Possible values are:
    - ♦ **false:** Indicates no extension is present.

    - ♦ **true:** Indicates an extension is present.

  - **CSRC:** Identifies the contributing source IDs. This value should be set to 0.

  - **Marker:** This value should be set to 1 to indicate the last media datagram of the video frame. The value is set to 0 for all other media datagrams and should be 0 for most packets.

  - **Payload type:** Identifies the type of RTP payload.

  - **Sequence number:** RTP sequence counter changes by one for each RTP media datagram sent.

**Note:** The status indicator turns red if the received RTP sequence numbers do not change by 1 on every packet.

- **Time Stamp:** Reflects the sampling instant of the first octet in the RTP datagram. This value can be used to determine packet sequence errors and jitter calculations to be made.

**Note:** The status indicator turns red if the Time Stamp field does not change at 48kHz rate on every group of audio samples.

- **SSRC:** Identifies the synchronization source ID and is set in compliance with RFC3550. This identifier is chosen randomly and should be unique so no two SSRC have the same value with an RTP session.

## **Data Tab**

The DATA tab indicates which stream is being monitored. For example, DATA-1 indicates stream 1 as configured in the Settings – Input menu. Select the Data stream to monitor in the application menu.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **346 Application Information** IP Session Application

## ● **L3 IP:**

- **Source Addr:** Lists the source addresses for the L3 IP layer.

- **Destination Addr:** Lists the destination addresses for the L3 IP layer.

- **L4 UDP:**
  - **Source Port:** Lists the source ports for the L4 UDP layer.

  - **Destination Port:** Lists the destination ports for the L4 UDP layer.

- **L5 RTP:** Lists the parameters of the L5 RTP (Real Time Protocol) layer. RTP datagrams are defined in IETF RFC 3550.
  - **Version:** Identifies the version of RTP and should be a value of 2.

  - **Padding:** Indicates whether padding bytes are present. Possible values are:
    - ♦ **false:** Indicates no extra padding bytes are at the end of the RTP packet.

    - ♦ **true:** Indicates that padding octets have been added to the RTP packet that are not part of the payload.

  - **Extension:** Indicates whether an extension is present. Possible values are:
    - ♦ **false:** Indicates no extension is present.

    - ♦ **true:** Indicates an extension is present.

  - **CSRC:** Identifies the contributing source IDs. This value should be set to zero.

  - **Marker:** This value should be set to 1 to indicate the last media datagram of the video frame. The value is set to 0 for all other media datagrams and should be 0 for most packets.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 347** IP Session Application

**Note:** For ST 2022-6 signals, the status indicator turns red if the Marker Bit Frequency does not match the frame rate indicated in the HBRMT header. For ST 2110 signals, the status indicator turns red if the Marker Bit Frequency does not match the measured field rate of the detected format.

- **Payload type:** Identifies the type of RTP payload.

- **Sequence Number:** RTP sequence counter changes in increments of one for each RTP media datagram sent.

- **Time Stamp:** Reflects the sampling instant of the first octet in the RTP datagram. This value can be used to determine packet sequence errors and jitter calculations to be made.

**Note:** For ST 2022-6 signals, the status indicator turns red if the Time Stamp field does not change at the rate of 27 MHz on every packet. For ST 2110 signals, the status indicator turns red if the Time Stamp field does not change at the start of every field or frame at the rate of 90 kHz on every packet.

- **SSRC:** Identifies the synchronization source ID and is set in compliance with RFC3550. This identifier is chosen randomly and should be unique so no two SSRC have the same value with an RTP session.

## **PTP Tab**

**Note:** PTP is supported in multi-input mode.

Select the **PTP** tab to view the status of the PTP elements in the stream. PTP is currently supported only on 10/25 GE SFP Port 1. For instructions on locking to PTP see _Configure Reference Settings_ .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **348 Application Information** IP Session Application

- **Lock Status:** Indicates whether the instrument PTP follower is locked to the leader PTP signal for the selected domain. These values might appear:
  - **No Leader present:** Indicates that the leader PTP clock has not been detected on the selected domain.

  - **Locked:** Indicates that the leader PTP clock is detected and there is less than 1000 ns of phase lag between the leader clock and the instrument.

  - **Unlocked:** Indicates that the leader PTP clock is detected and there is greater than 1000 ns of phase lag between the leader clock and the instrument.

- **PTP time:** Shows the time derived from the PTP Leader as UTC (Coordinated Universal Time).

- **Leader** / **Follower Phase Lag:** Shows the detected offset between the leader and follower clocks.

- **Offset from Leader:** The Offset from Leader is the phase error of the phase-locked loop, which controls the follower clock. The phase lag is a reasonable estimate of how well the PTP follower is locked to the leader; however, the phase lag does not indicate whether there is any asymmetry in the network.

- **Grandmaster ID:** Shows the MAC Address of PTP Leader with the bytes ff:fe inserted in the middle. This ID is also used in the BMCA as a tiebreaker if all of the parameters match down through priority 2.

- **Steps Removed:** Shows the number of communication paths traversed between the local clock and the Grandmaster clock.

- **Domain:** Shows the domain being used. Domains allow multiple PTP services to coexist simultaneously on one physical Ethernet connection.

- **Profile:** Shows the profile being used: General, AES67, or ST2059. This is the userselected profile set on the Settings, Reference configuration menu page and is not detected on the input.

- **Delay Message Interval:** For Multicast communication mode, the only delay message interval allowed is “Follow Leader.” In this mode, the follower sets the delay request rate according to the information sent by the leader in the delay response message.

**Note:** The PRISM monitor currently supports Multicast communication mode and SMPTE mixed mode without negotiation.

- **Grandmaster BMCA Values:** Lists these values for the Grandmaster BMCA (Best Master Clock Algorithm) in order of precedence:
  - **Priority 1:** This parameter defines which clocks are allowed to be considered as leaders. To be considered as a leader, the value should be set to 128 or less. Priority 1 is the first criteria in the BMCA, so if Priority 1 is set to a lower value than other devices on the system, then it is chosen even if the clock quality is poor. Typically, all the leaders in a domain should have the same value for the Priority 1 parameter.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 349** IP Session Application

- **Clock Class:** This value characterizes the TAI (International Atomic Time) traceability. The clock class value varies to indicate the type of reference in use by the Grandmaster clock. For example, when locked to GPS the PTP grandmaster reports a class 6. However, if in holdover mode after locking to GPS, then it reports a class of 7.

- **Clock Accuracy:** This value characterizes the clock accuracy for the purpose of determining the best leader clock.

- **Clock Variance:** This value is reported by the PTP leader to indicate the variance of the clock over a one second interval. A lower number indicates a more stable clock and is preferred by the BMCA.

- **Priority 2:** This parameter is used to break the tie between leaders that have the same clock quality. Several values can be used to define a hierarchy of devices. Most profiles use 128 as a default, so a value of 127 or lower would indicate a preferred leader.

- **Clock Source:** The clock source field is not used by the BMCA. The field is set to indicate the type of reference in use by the Grandmaster clock.

- **Communication Mode:** There are three basic message modes for PTP: Multicast, Unicast, and mixed Multicast and Unicast. For full Multicast or Unicast modes, all of the PTP messages are sent in the selected mode type.

**Note:** The PRISM monitor currently supports Multicast communication mode and SMPTE mixed mode without negotiation. In later firmware releases, other communication modes will be supported.

For some profiles, such as some telecom profiles and the ST2059 profile, a mixture of Multicast and Unicast are allowed. On the SMPTE profile unique mixed mode, the Announce and Sync messages are sent as multicast. However, the Delay Request and Delay Response messages are sent as Unicast. Therefore, it is important to ensure correct configuration of IP addresses and layer three communication to ensure that the Delay Request and Response are transmitted and received correctly.

Some points to understand about communication modes:

- Whatever mode is chosen, the leader and follower must match or be compatible.

- Multicast and Mixed modes might need IGMP joins and leaves Full Unicast must have the leader address in all follower AMTs.

- Unicast without negotiation does not allow leader to regulate load.

- Two leaders can be used on different domains to serve followers on different communication modes.

- **Delay Mechanism:** Shows the delay mechanism mode being used:

**Note:** The PRISM monitor currently supports only the End-to-End delay mechanism.

- **End-to-End:** In this mode, the sync, follow-up, delay-request, and delayresponse messages go through the network all the way between the leader and

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **350 Application Information** IP Session Application

follower. End-to-End mode is useful in PTP networks where some or all devices are not PTP aware.

- **Peer-to-Peer:** In this mode, the Pdelay-request and Pdelay-response messages are local to each link in the network. Each device determines the local link and device delays. The sync message from the leader then collects the corrections as it propagates from the leader to follower. Peer-to-Peer mode is useful in PTP networks where the routing configuration changes. For Peer-to-Peer mode to work well, all of the devices need to be PTP aware.

## ● **Message rates:**

- **Announce:** Displays the rate of the Announce messages received from the leader. Typical values are 1 to 4 messages a second, but a wide range is allowed by some profiles. If the value is lower than expected, it might indicate a problem in the network or the leader.

- **Sync:** Displays the rate of the Sync messages received from the leader. Typical values are 1 to 16 messages a second, but some profiles allow much higher rates. If the value is lower than expected, it might indicate a problem in the network or the leader.

- **Delay Request:** Displays the rate of the Delay Request messages sent by the follower. In multicast mode, the Delay Request rate is required to be set in response to a field in the Delay Response message from the leader. Typically the leader sets this field such that the Delay Request message rate is equal to the Sync message rate.

**Note:** For SMPTE mixed mode, PRISM sets the delay Request rate equal to the Sync message rate received from the leader.

- **Delay Response:** Displays the rate of the Delay Response messages received from the leader. Each Delay Request should have a matching Delay Response, so if the value is lower than expected then it might indicate a problem in the network or the leader

## **NMOS Tab**

Select the NMOS tab to view the registration server information, server list and the last SDP file received.

To enable and configure NMOS see _Using NMOS_ .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 351** IP Session Application

- **Registration Server:** The Host Name row shows the DNS host name when DNS is selected as the NMOS registration method, or “Static IP Address” when Static is selected. The IP Address Status LED is green when PRISM is successfully registered with the server.

- **Registration Server List:** Select the Registration Server List tab to view the Host Name, IP Address, and Priority of the servers registered to this instrument using NMOS.

**Note:** Select **Return** to go back to the main IP Session NMOS menu.

- **Last SDP Files Received:** Select the Last SDP File Received tab to view video, audio, and data SDP files for each NMOS dev. These files contain information used to configure input signals from the registration servers.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **352 Application Information** IP Graphs Application

**Note:** Select **Return** to go back to the main IP Session NMOS menu.

## **IP Graphs Application**

**Note:** IP Graphs are supported in multi-input mode for a primary IP input.

Use the IP Graphs application to view various graphs that show aspects of the IP stream. As you scroll through the various graphs, the top of the selected graph moves to the top of the display area to help view the complete graph. The displayed graph is included in a saved preset. The application is available only in the 200 and 300 versions of MPS, MPD, and MPP.

**Note:** Option MPSDP-IP-MEAS must be installed to use the IP Graphs application.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 353** IP Graphs Application

If ST 2022-7 monitoring is configured, the IP Graphs application includes Path 1 and Path 2. The graph data can be switched between viewing only Path 1, only Path 2, or both by selecting the Path button in the top right of the screen.

**Note:** The Path button works only with ST 2022-7 seamless switching enabled in input configuration.

If ST 2110 monitoring is configured, you can select Video, Audio, and data. For Audio and Data, you can select one stream at a time from the four available streams in the Tile Settings menu.

If ST 2022-6 monitoring is configured, the IP Graphs include:

- **Video CRC Error graph:** The Video CRC Error graph shows any present CRC errors in the currently decoded signal and can be compared to other time graphs such as RTP Sequence Errors.

- **TS-DF graph:** The TS-DF graph shows the Time Stamped Delay Factor, as defined in EBU Tech 3337, which is a method for measuring network jitter in RTP streams.

## **Configure the IP Graphs Application**

**1.** Select the **Tiles** icon ( ).

**2.** Select the tile with the IP Graphs application.

**3.** Select the **Tile** icon ( ).

**Note:** To move the settings left or right, select the **Move** icon ( - ) in the Settings menu header.

**4.** From the **Trend Interval** list, select the interval: **1 minute** , **5 minute** , **10 minute** , **30 minute** , **1 hour** , **3 hour** , **6 hour** , **12 hour** , or **1 day** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **354 Application Information** IP Graphs Application

**5.** From the **Audio** list, select a stream to monitor. The monitored stream is noted in the IP Graphs heading, next to the Stream type button.

**6.** From the **Data** list, select a stream to monitor. The monitored stream is noted in the IP Graphs heading, next to the Stream type button.

## **IP Graphs Application Elements**

The elements at the top of the IP Graphs application are shared between all graphs.

**Note:** Only Path 1 displays unless you enable ST 2022-7 Seamless Switching, (see _Configure ST 2022-6_ ).

- **PATH 1** and **PATH 2:** Describes the two information paths.

- **Port:** Shows the physical port used on the instrument.

- **Src:** Lists the source address of the IP stream.

- **Dest:** Lists the destination address of the IP stream.

- **Protocol:** Lists the protocol being used by the monitored stream.

- **PRS:** Shows the Packet Read Schedule (PRS) defined in the input video settings.

- **Clear icon:** Select the **Clear** icon ( ) to reset the monitoring session.

- **Stream type:** Select this button to change to Video ( ), Audio ( ), or Data ( ) EI 2

- stream IP graphs.

- **Data stream:** Shows the Data stream being monitored. For example, Data 1 indicates stream 1 as configured in the Settings – Input menu. Select the Data stream to monitor in the application menu.

- **Path:** Select the Path button to change to Path 1, Path 2, or both Path 1 and 2.

- **Res:** Lists the resolution of the graph display at the bottom right of the graph.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 355** IP Graphs Application

## **Total Bit Rate Graph**

The Total Bit Rate graph shows the total bit rate currently on the 10/25 GE input. The maximum available bandwidth depends on 10/25 GE input: 10.3Gbps and 25.8Gbps. These readouts appear:

- **Max:** Shows the maximum bandwidth used during the time window.

- **Mean:** Shows the mean bandwidth used during the time window.

- **Min:** Shows the minimum bandwidth used during the time window.

- **Free Min:** Shows the minimum available bandwidth that is not in use.

- **Free Max:** Shows the maximum available bandwidth that is not in use.

## **Session Bit Rate Graph**

The Session Bit Rate graph shows the data rate of the currently selected input stream.

## **PIT Graph**

The PIT (Packet Interval Time) graph shows the difference in arrival time between sequential packets of the active stream. This is one indication of the packet jitter and dropped packet rate. The colored bars represent the range from minimum to maximum for all of the packets within that time interval.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **356 Application Information** IP Graphs Application

## **RTP Sequence Error Graph**

The RTP Sequence Error section shows the RTP sequence information and indicates whether a packet is received out of order.

In the Reconstructed Path Errors section, 0 means no sequence errors have been detected, and any number (not 0) means sequence error or errors were detected after RTP packet reordering on each path and ST 2022-7 seamless reconstruction process.

## **Path1–Path2 Differential Graph**

Path Differential represents the time difference between the Path 1 and Path 2 streams in an ST 2022-7 system. As the path differential gets larger, it becomes more difficult for equipment receiving the data to properly process both paths, depending on the size of the input buffer in the equipment.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 357** IP Graphs Application

The ST 2022-7 specification defines Path Differential as an absolute value, but the Path1-Path2 Differential graph shows the signed value of Path 1 minus Path 2. A positive value means that Path 2 is lagging behind Path 1.

**Note:** The measurement range of Path1-Path2 differential measurement is 1 second.

The Path1-Path2 differential measurement is not supported for ST 2110-30.

## **CMAX and VRX Buffer Graph**

ST 2110-21 specifies a timing model for ST 2110-10 video RTP streams with these parametric models:

**Note:** The CMAX and VRX trend graphs are not available for streams 525i 59.94 and 650i 50. The graphs are also not available on SFP 2.

Make sure the input signal and PRISM are locked to PTP for these measurements.

- A network compatibility model to regulate the burst characteristics of senders, which promotes the compatibility with the switches. The CMAX section provides a trend graph for this type of modeling.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **358 Application Information** PIT Histogram Application

- A virtual receiver buffer model to ensure there is no buffer overflow or underflow in the receiver that could cause the packet loss and picture quality degradation. The VRX Buffer section provides a trend graph for this type of modeling.

Both trend graphs help engineers properly setup the packet delivery timing in the RTP packet sender.

## **PIT Histogram Application**

**Note:** PIT Histogram is supported in multi-input mode for primary IP inputs.

Use the PIT (Packet Interval Time) Histogram application to monitor the network delay variation statistics. The application is available only in the 200 and 300 versions of MPS, MPD, and MPP.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 359** PIT Histogram Application

-

**Note:** If ST 2110 monitoring is configured, you can select Video, Audio, or Data (one stream at a time, selectable in Tile Settings).

## **Configure the PIT Histogram Application**

To open the PIT Histogram Settings menu:

**1.** Select the **Tiles** icon ( ).

**2.** Select the tile with the PIT Histogram application.

**3.** Select the **Tile** icon ( ).

**Note:** To move the settings left or right, select the **Move** icon ( - ) in the Settings menu header.

**4.** Select a **Y-Axis** scaling option: **Linear** or **Log** .

**5.** From the **Audio** list, select the audio stream to monitor. The selected audio stream is noted in the PIT Histogram heading next to the monitored path.

## **PIT Histogram Elements**

- **Port 1** and **Port 2:** Shows the physical ports on the instrument.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **360 Application Information** PIT Histogram Application

- **Src** / **Dest:** Lists the source and destination addresses of the IP stream.

- **Protocol:** Lists the protocol being used by the monitored stream.

- **Path:** Select the button, in the top-right corner of the tile, to switch between Path 1 only (green), Path 2 only (blue), or both Path 1 and Path 2 data (cyan where Path 1 and 2 are overlapped).

**Note:** The Path button works only with ST 2022-7 seamless switching enabled in input configuration.

- **Stream type:** Select to switch between the video, audio, or data stream IP graphs.

**Note:** The Stream Type button is available only with ST 2110 streams.

Packet Interval information:

- **Max:** Shows the maximum packet interval time.

- **Mean:** Shows the mean packet interval time.

- **Min:** Shows the minimum packet interval time.

- **Std Dev:** Shows the standard deviation of the packet interval time.

Use the pinch and pinch-out gestures on the graph to zoom in and out. After using the zoom-in gesture, the text Zoomed” is displayed on the bottom of the graph.

**Note:** When using a keyboard and mouse, click-and-drag to zoom in.

Select the **Reset** button ( Reset ) to set the graph back to autoscale mode.

**Note:** The Reset button is only displayed after zooming in.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 361** PTP Graphs Application

## **PTP Graphs Application**

Use the PTP Graphs application to monitor the message timing between leader and follower in a PTP network. The application is available only in the 200 and 300 versions of MPS, MPD, and MPP.

For more information on PTP operations and settings, see _Configure Reference Settings_ and _PTP Introduction_ .

**Note:** Option MPSDP-IP-MEAS must be installed to use the PTP Graphs application.

**==> picture [3 x 1] intentionally omitted <==**

**----- Start of picture text -----**<br> -<br>**----- End of picture text -----**<br>

## **Configure the PTP Graphs Application**

To open the PTP Graphs Settings menu:

**1.** Select the **Tiles** icon ( ).

**2.** Select the tile with the PTP Graphs application.

**3.** Select the **Tile** icon ( ).

**Note:** To move the settings left or right, select the **Move** icon ( - ) in the Settings menu header.

**4.** From the **PTP Trend Interval** menu, select the interval. The PTP Trend Interval defines the extent of the horizontal axis on the graph.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **362 Application Information** PTP Graphs Application

## **PTP Graph Elements**

The PTP graphs are useful in observing the effects of traffic on the PTP messages and the operation of transparent and boundary clocks. Non-PTP aware switches might have significant PTP delay variations, while transparent and boundary clocks have much less variation and total delay.

- **PTP Lock:** Shows the status of the PTP lock.
  - **Grandmaster ID:** Displays the reference source, based on the Domain.

  - **Domain:** Can be changed in **Settings** ( ), **Reference.**

  - **Profile:** Shows the profile that has been selected in the reference settings menu. This is not detected from the incoming PTP messages.

  - **PTP Time:** Time of day derived from the PTP signals.

  - **Res** (Resolution): Shows the time increment for each bar on the display. Longer graph settings collect data into larger bins to be displayed. This range and resulting resolution are selected in the setting menu for PTP graphs.

- **Trace Types:** There are four displays available. For each one, the Max., Min., and Mean (average) are shown on the left, while the traces versus time is shown on the right. The traces indicate the Max, and Min envelope, and the Mean (average) for each time bin. The time scale can be adjusted in the settings menu. The data is logged for 1 day so you can go back and look at long-term trends.

Use the control to move the displays up or down.

- **Leader-Follower Delay:** This graph indicates the difference in the time stamps for the PTP Sync messages; these go from the leader to the follower. This display indicates effects of the downstream network delay and adjustments made to the follower clock. After the follower is locked and the timing is stable, the perturbations on this graph are largely due to network variations. Traffic often causes some messages to be delayed so the maximum delay increases.

As the PTP is locking, the follower clock adjusts, so the trace might have large swings or jumps. As the system locks, the leader-to-follower and follower-toleader delays should converge on the same value. This value represents the

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 363** Stream Timing Application

average network delay between the leader and follower for the traffic in both directions.

If the network delay is too unstable, then the PTP might never lock. This appears as large variations on this trace.

- **Leader-to-Follower Variation:** The leader-to-follower variation graph is derived from the same data as the leader-to-follower delay. The absolute value of the changes in delay are filtered according to RFC1889 and displayed. This display then shows a measure of the variation of the network delay. A low value indicates a PTP follower is likely to quickly lock, a large value indicates it could be difficult for a PTP follower to lock.

- **Follower-Leader Delay:** This graph indicates the difference in the time stamps for the PTP Delay Request messages that go from the follower to the leader. This display indicates effects of the upstream network delay and adjustments made to the follower clock. After the follower is locked and the timing is stable, the perturbations on this graph are largely due to network variations. Traffic often causes some messages to be delayed so the maximum delay increases.

As the PTP is locking, the follower clock adjusts, so the trace might have large swings or jumps. As the system locks, the leader-to-follower and follower-to leader-delays should converge on the same value. This value represents the average network delay between the leader and follower for the traffic in both directions.

If the network delay is too unstable, then the PTP might never lock. This appears as large variations on this trace.

- **Leader** - **Follower Variation:** The leader-to-follower variation is derived from the same data as the leader-to-follower delay. The absolute value of the changes in delay are filtered according to RFC1889 and displayed. This display then shows a measure of the variation of the network delay. A low value indicates a PTP follower is likely to quickly lock. A large value indicates it could be difficult for a PTP follower to lock.

- **Offset from Leader:** The graph shows the error in the follower clock phase as measured by the PTP time stamps. This value is used to adjust the follower clock to drive the error toward zero.

The Offset from Leader is the phase error of the phase-locked loop, which controls the follower clock. The offset from leader is a reasonable estimate of how well the PTP follower is locked to the leader; however, the offset from leader does not indicate if there is any asymmetry in the network.

## **Stream Timing Application**

**Note:** Stream Timing is supported in multi-input when the primary input is IP.

The Stream Timing application shows the timing of the video, audio, and data as it was received relative to the embedded RTP time stamps. It also shows the relative delay

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **364 Application Information** Stream Timing Application

between Audio/Video and the Data/Video, which is the amount of delay needed to realign the two essence types. The application is available only in the 200 and 300 versions of MPS, MPD, and MPP.

**Note:** The Stream Timing application requires Option MPSDP-IP-MEAS.

## **Configure the Stream Timing Application**

**1.** Select the **Tiles** icon ( ).

**2.** Select the tile with the Stream Timing application.

**3.** Select the **Tile** icon ( ).

**Note:** To move the settings left or right, select the **Move** icon ( - ) in the Settings menu header.

.

**4.** From the **Timing Trend Interval** list, and select the interval.

- To undo the last clear or reset of the monitoring session, select **Undo Reset** .

**5.** From the **Audio** list, choose the audio stream to monitor. The selected stream is noted in the AUDIO tab label.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 365** Stream Timing Application

## **Stream Timing Elements**

The elements at the top of the Stream Timing application are shared between all graphs:

**Note:** Only Path 1 displays, unless you enable ST 2022-7 Seamless Switching. (See _Configure ST 2022-6_ .)

- **Clear:** Select the **Clear** icon ( ) to reset the monitoring session.

- **Path:** Select the Path button to switch between Path 1, Path 2, or both Path 1 and Path 2.

- **Stream type tabs:** Select these tabs to switch between the stream offset graphs:
  - VIDEO

  - AUDIO

**Note:** The number in the AUDIO tab is the selected stream.

- DATA

- **Res:** Lists the resolution of the graph display.

## **Video Offset Tab**

The Video Offset tab has options to see the timing and data between the video stream and PTP or RTP offset.

## **Vid-PTP**

The Vid-PTP graph shows the relative delay between video stream and PTP. This value indicates the amount of delay that must be applied to realign the video and PTP according to the time stamps. This is a time-based graph of the Timing Display application.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **366 Application Information** Stream Timing Application

## **Vid-RTP Offset**

The Vid-RTP Offset graph shows timing of the video stream as it was received relative to the embedded RTP time stamps.

## **Audio Offset**

Select the Audio Offset tab to view the timing and data between the audio stream and video stream or RTP offset.

## **Aud-Vid Offset**

The Aud-Vid Offset graph shows the relative delay between audio and video streams. This value indicates the amount of delay that must be applied to realign the signals according to the time stamps.

**Note:** The selected stream is indicated in the Audio tab as <1-8>.

The audio measurements are logged to a single graph. If you change the audio stream being monitored, we recommend resetting the graph to only see the measurements relative to the current stream.

To change the monitored stream:

**1.** Select the **Tile** icon ( ) and select the Audio menu.

**2.** Select the stream to monitor.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 367** Stream Timing Application

## **Aud-RTP Offset**

The Aud-RTP Offset graph shows timing of the audio stream as it was received relative to the embedded RTP time stamps.

## **Video-RTP Offset PATH 1 and PATH 2**

Indicates when the deviation of the RTP timestamp to the PTP reference is greater than the configured threshold. The default value is +/-1ms and can be set up to a value of 20ms.

## **Data Offset**

Select the Data Offset tab to view the timing and data between the data stream and video stream or RTP offset.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **368 Application Information** Stream Timing Application

## **Data-Vid Offset**

The Data-Vid Offset graph shows the relative delay between data and video streams. This value indicates the amount of delay that must be applied to realign the signals according to the time stamps.

**Note:** The selected stream is indicated in the Data tab as <1-4>.

The data measurements are logged to a single graph. If you change the data stream being monitored, we recommend resetting the graph to only see the measurements relative to the current stream.

To change the monitored stream:

**1.** Select the **Tile** icon ( ) and select **Data** .

**2.** Select the stream to monitor.

## **Data-RTP Offset**

The Data-RTP Offset graph shows timing of the data stream as it was received relative to the embedded RTP time stamps.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 369** ANC (Ancillary Data) Session Application

## **ANC (Ancillary Data) Session Application**

**Note:** In multi-input mode, ANC Session works only with the primary channel.

The ANC Session application allows you to examine all the ancillary data present in a signal. The instrument continually monitors the signal and tells you when changes in the presence of data occur.

Select the **Clear** icon ( ) to reset the monitoring session for both the WATCH LIST and the SCTE104 pages.

**Note:** PRISM monitors the first four links of the eight logical SDI links in Quad Link 3G LB and Quad Link 12G.

## **WATCH LIST Tab**

Select the **Watch List** tab to view a list of detected ANC data. The Watch List tab also reports the last detected time, so infrequent ANC data, such as SCTE-104, can be monitored in the Occurrence column. The Line/Sample information, in conjunction with Datalist display, helps you diagnose the ANC data at the bit level.

- **STRM:** The ST 2110-40 or -43 stream number.

- **DID:** Data identifier of the packet, permissible values range from 1 to 0xFF (255) inclusive.

- **SDID:** Secondary data identifier of the packet, permissible values range from 0 through 0xFF (255) inclusive.

- **LINK:** This is the virtual link or stream the ANC data is present on.

- **LOCATION(S):** This is the transport line number the ANC data is present on.

- **OCCURRENCE:** Shows the last time a packet occurred.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **370 Application Information**

ANC (Ancillary Data) Session Application

- **NOTE:** Shows the basic information about the ANC data, such as time code or summary of SCTE104.

**Note:** A green checkmark in the WATCH LIST Name column means data is being continuously received. A yellow exclamation mark means data has been received but it has stopped.

## **SCTE104 Tab**

Select the **SCTE104** tab to view Multiple Operations Messages, and the RTC / TC (Real Time Clock/Time Code) section displays the reception time of ANC packets that have SCTE104 data. You can review the last 10 messages to check whether the message sequence is correct.

Select the **Run** button ( ) to start the data stream.

Select the **Pause** button ( ) to pause the data stream.

**Note:** When the **Run** button ( ) is visible, data monitoring-collecting is paused. When the **Pause** button ( ) is visible, data collecting-monitoring is running.

Multiple Operation Codes and Titles

| **Op Code** | **Op Title**                          |
| ----------- | ------------------------------------- |
| 0x0101      | splice_request_data()                 |
| 0x0102      | splice_null_request_data()            |
| 0x0104      | time_signal_request_data()            |
| 0x0109      | insert_DTMF_descriptor_request_data() |

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 371** Datalist Application

Multiple Operation Codes and Titles

| **Op Code** | **Op Title**                                  |
| ----------- | --------------------------------------------- |
| 0x010A      | insert_avail_descriptor_request_data()        |
| 0x010B      | insert_segmentation_descriptor_request_data() |
| 0x010C      | proprietary_command_request_data()            |

**Note:** The RTC (real-time clock) and TC (time code) numbers on the SCTE104 page match the RTC and TC in the PRISM status menu.

The number in the left column of the SCTE104 page is the number of operations received. Select the **Plus** icon ( ) or **Minus** icon ( Kd ) to scroll through the list of up to the last 10 received messages.

Received messages that are marked as duplicates (ST 2010 header of 0x09) display “Duplicate” instead of Multiple or Single Operation. “Duplicate” is also marked in the Event Log.

## **Datalist Application**

**Note:** In multi-input mode, Datalist works only with the primary channel.

You can view digital data in SDI frames for select HD, 3G Level A, and single-link 12G formats to perform in-depth monitoring and analysis of incoming SDI data.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **372 Application Information** Datalist Application

## Supported Datalist Formats

|                |            | **Sample**    |       |          |                      |           |            |
| -------------- | ---------- | ------------- | ----- | -------- | -------------------- | --------- | ---------- |
| **Link**       | **Format** | **Structure** |       | **Bits** | **Frame/Field Rate** | **Audio** | **Option** |
| HD-SDI         | 1920x1080  | 4:2:2         | YCbCr | 10b      | 50/59.94/60i,        | 16ch      | Standard   |
|                |            |               |       |          | 23.98/24/25/29.97/   |           |            |
|                |            |               |       |          | 30p, and psF         |           |            |
| 3G-SDI Level A | 1920x1080  | 4:2:2         | YCbCr | 10b      | 50/59.94/60p         | 16ch      | Standard   |
| 12G-SDI        | 3840x2160  | 4:2:2         | YCbCr | 10b      | 50/59.94/60p         | 16ch      | FMT-4K     |

**Note:** 4K Quad Link signals can be monitored by looking at the individual links as separate inputs.

Datalist requires software option MPSDP-ENG-QC.

The Datalist display shows the digital data from the selected SDI input. It is updated approximately once per second, and updating can be controlled by selecting the **Run/ Pause** button in the application banner.

While the application is running or paused, you can scroll through the SDI data using a touchscreen or mouse. Scroll vertically by touch-swipe or use the mouse scroll wheel. Scroll horizontally by touch-swipe or click-and-drag with the mouse. Alternately, the described navigation controls can be used.

Note that the navigations controls are available only in Half-Screen and Full-Screen modes. The **Half-Screen** icon ( LF ) expands the tile vertically. If the tile expands, it covers the tile above or below, depending on whether you are expanding the top or bottom tile. The **Reduce** icon ( Lt ) turns the tile to quarter-screen size. Similarly the **Full Screen** icon ( ) expands the tile vertically and horizontally. The **Reduce** icon ( ) te) 17) returns the tile back to the previous mode.

The color map for the various types of data is as follows:

Within the application, you can select the **Question Mark** icon ( ) to view the color map.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 373** Datalist Application

The following table describes each item.

| **Item** | **Description**                                                                                                                                                                                                                                                      |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1        | SDI frame data: The SDI frame data is color coded for easier identification.<br>Select the**?**icon in the application banner for help in decoding the SDI data<br>types.                                                                                            |
| 2        | Selected SDI sample: The SDI sample that is selected by the Line and Sample<br>controls at the bottom of the application.                                                                                                                                            |
| 3        | Line and sample numbers.                                                                                                                                                                                                                                             |
| 4        | Line and sample data types.                                                                                                                                                                                                                                          |
| 5        | Line and sample selection: Use these controls to go to a specific sample and<br>line. The number can be entered directly by selecting the current number;<br>this displays a keyboard. Enter the line or sample number and select**Enter**to<br>go to that location. |
| 6        | SDI frame shortcuts: Use these controls to go to the next EAV, SAV, and ANC<br>location after the selected SDI sample. For example, to go to the next SAV<br>location, select the**SAV**button and then select the**Fast Forward**button.                            |
| 7        | **Run/Pause control:**Select this button to run and pause the SDI frame<br>updates. Pausing allows you to examine a single SDI frame in more detail.                                                                                                                 |

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **374 Application Information** Timing Application

## **Timing Application**

**Note:** In multi-input mode, Timing works only with the primary channel.

The Timing application uses a reference to evaluate the timing of the input of singlelink SDI, quad-link SDI, or IP formats (ST 2022-6 or ST 2110-20). The timing of the input is compared to the expected frame time according to the reference alignment.

SDI versus Black Burst is available in standard. SDI versus PTP, IP versus PTP, Black Burst versus PTP requires Option MPSDP-IP-MEAS.

For analog references (Black Burst or Tri-Level sync), the relative position of the horizontal and vertical sync pulses are compared to the input signal. In the case of PTP, the current time is obtained and compared to the SMPTE Epoch. When an input is configured for ST 2022-7-style redundant streams, circles for Path 1 (green) and Path 2 (blue) appear; otherwise, only a single path appears. When the input signal is fully aligned with the reference, both circles are in the center of the display indicated by the + symbol. The ability to compare IP-format signals is available only in the 200 and 300 versions of MPS, MPD, and MPP.

**Note:** PTP must be locked to use the Timing application with PTP references.

## **Configure the Timing Application**

**1.** Select the **Tiles** icon ( ).

**2.** Select the tile with the Timing application.

**3.** Select the **Tile** icon ( ).

**Note:** To move the settings left or right, select the **Move** icon ( - ) in the Settings menu header.

**4.** Select a following measurement mode:

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 375** Timing Application

- **Video to Reference:** The input video signal (SDI or IP) is compared relative to the reference input (analog or PTP).

- **Analog to PTP:** Used in a hybrid system to compare the analog reference to the PTP reference to ensure synchronization.

## **Compare Analog Reference with PTP**

**1.** If you haven’t already done so, choose the **Setting References** . See _Configure External Reference_ .

**2.** In the **Timing Settings** menu, select **Analog to PTP** .

The Timing application compares the Analog to PTP.

## **Timing Elements**

The Timing elements are as follows:

- **Path 1** and **Path 2:** Displays the IP video format if an IP input signal is selected.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **376 Application Information** Timing Application

**Note:** You can switch between Path 1, Path 2, or both Path 1-2 using the Path button at the top right of the application display.

- **Leader ID** and **Domain:** Displays the reference Source and Domain.

- **PTP Time:** Time of day derived from the PTP signals.

- **Protocol:** Displays the input protocol.

- **Ref Lock:** A (check in green) indicates the PRISM is locked to the reference.
  - A (x in red) indicates the PRISM is not locked to the reference.

- **Reference Indicator:** A crosshair indicator centered in the display represents the reference signal.

- **Circle:** The circle represents the timing of the input signal. A signal that is early is above or to the left of the crosshair. A signal that is late is below or to the right.

- **Offset:** The difference in timing between the input and reference. A positive number, or “delayed” value, means the input occurs after the reference. A negative number, or “advanced” value, means the input occurs before the reference.
  - **Time:** The total difference in frame timing between the input and reference

  - **Pixels:** The timing difference between the reference and input signal, expressed as in pixels, instead of time units, after the vertical offset has been removed. This has a range of ± ½ line for the input format.

  - **Vertical:** The timing difference between the reference and input signal, expressed as the number of lines of delay for the input video format. This has a range of ± 1/2 field for progressive signals and ± 1/2 frame for interlace signals.

  - **Horizontal:** The timing difference between the reference and input signal, expressed as the line time, which remains from the total delay after the vertical offset has been removed. This has a range of ± 1/2 a line for the input format.

Additional offset displays are available for Quad Link SDI signals.

- **Link Offsets:** Time delays of Links B, C, and D relative to Link A. These time delays are also shown graphically under the timing display window.

- **Max Link Offset:** Maximum time delay between any two links.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 377** Eye Application

## **Timing Offsets for IP Signals**

Because ST 2022-6 streams are complete SDI signals encapsulated in IP, the timing measurement treats these IP signals as if they were SDI. So the timing system detects the start of the IP frame, then extrapolates to the 0 h point of the encapsulated SDI. Then using PTP as the reference, the ideal alignment point for that frame rate is calculated based on the PTP epoch. Finally, the offset between the ST 2022-6 signal and the ideal alignment is displayed. The display shows both absolute time and the time parsed into lines or horizontal delay as time and pixels.

For ST 2110-20 streams, the Timing application displays the time of the first packet of the frame. Since ST 2110 does not include blanking, the first packet is nominally coincident with the first active line in the SDI raster. This means it is normal for the ST 2110 streams to be delayed by the lines in the vertical blanking of a given format. This value varies by format: HD (21 lines), 3G (42 lines), 4K/UHD (84 lines). According to ST 2110-21, both gapped and linear flows should have the start of frame delayed by the equivalent of vertical blanking.

## **Use Cases for Measuring Timing**

One use case for the Timing application is to measure the delay in a gateway and network. If a properly timed SDI signal is applied to a gateway, then the timing measurement on the resulting IP flow displays the combined latency in the gateway and the network.

Each ST 2110 stream also carries time stamps. The Stream Timing application allows for the analysis of these time stamps.

## **Eye Application**

**Note:** In multi-input mode, Eye works only with the primary channel.

The Eye application presents an eye pattern diagram of the SDI signal to verify electrical characteristics of the SDI transport layer. Use this application to make automated eye measurements on SD, HD, and 4K SDI signals. This application is available only in the 300 version of MPS, MPD, and MPP. The software option MPSDP-FMT-4K enables 12GSDI support. This application is valid only on SDI 1.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **378 Application Information** Eye Application

When the application is in full-screen mode, a data display is visible. To move the information, select the text and drag it.

## **Configure the Eye Application**

**1.** Select the **Tiles** icon ( ).

**2.** Select the tile with the Eye application.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 379** Jitter Application

**3.** Select the **Tile** icon ( ).

**Note:** To move the settings left or right, select the **Move** icon ( ) in the Settings menu header.

**4.** From the **Jitter High Pass Filter** list, select the high pass filter: **Timing** , **Align** , **10 Hz** , **100 Hz** , **1 kHz** , **10 kHz** , or **100 kHz** .

**Note:** For multipiece displays, the filter setting applies to both pieces.

**5.** From the **Sweep Mode** list, select **3 Eye** , **10 Eye** , **1 Field** , or **2 Field** .

**6.** Set **Jitter Meter** to **Show** to turn on the jitter meter above the eye pattern.

**Note:** Eye measurements (eye amplitude, eye risetime, eye falltime, eye rise-fall, eye rise overshoot, eye fall overshoot, and P-P jitter) are displayed when the Eye application is in full-screen mode. The display can be moved by selecting and dragging it.

## **Jitter Application**

**Note:** In multi-input mode, Jitter works only with the primary channel.

The Jitter Display application shows the wave shape of the jitter and allows you to view additional time-domain information, such as whether there are jitter components that are synchronous or nearly synchronous to the video line or frame.

This application is available in the 300 version of MPS, MPD, and MPP. The software option MPSDP-FMT-4K enables 12G-SDI support. This application is valid only on SDI 1.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **380 Application Information** Jitter Application

When the application is in full-screen mode, a data display is visible. The information can be moved anywhere in the tile. Select the text and drag it to a new location.

To configure the Jitter Display settings:

**1.** Select the **Tiles** icon ( ).

**2.** Select the tile with the Jitter application.

**3.** Select the **Tile** icon ( ).

**Note:** To move the settings left or right, select the **Move** icon ( =| ) in the Settings menu header.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 381** External Reference Application

**4.** From the **Jitter High-Pass Filter** list, select the high pass filter: **Timing** , **Align** , **10 Hz** , **100 Hz** , **1 kHz** , **10 kHz** , or **100 kHz** . Depending on the format, Timing typically uses the 10 Hz filter and Align uses the 1 kHz or 100 kHz filter.

- From the **Sweep Mode** list, select **1 Line** , **2 Line** , **1 Field** , or **2 Field** .

- Set **Jitter Meter** to **Show** to turn on the jitter meter at the top of the tile.

**Note:** Eye measurements (eye amplitude, eye risetime, eye falltime, eye rise-fall, eye rise overshoot, eye fall overshoot, and P-P jitter) are displayed when the Jitter Display application is in full-screen mode.

## **External Reference Application**

The External Reference application shows the analog reference signal is the correct type, amplitude, and acceptable signal integrity.

## **Configure the External Reference Application**

**1.** Select the **Tiles** icon ( ).

**2.** Select the tile with the External Ref application.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **382 Application Information** External Reference Application

**3.** Select the **Tile** icon ( ).

**Note:** To move the settings left or right, select the **Move** icon ( =] ) in the Settings menu header.

**4.** In the **Sweep** list, select the waveforms to view between the lines or fields or make timing measurements on them.

**5.** In the **Gain** section, select **1.0x** , **2.0x** , or **5.0x** .

**6.** In the **Magnification** section, select **Best** or **1.0x** .

## **External Reference Application On-screen Tools**

You can change the gain, horizontal and vertical positions, sweep line, and magnification—without opening the External Reference Settings menu—through onscreen tools. Select the button for the setting you want to adjust. All the available tools are located on the top and bottom of the display and are highlighted for a few seconds when the application is first opened or if you select anywhere in the middle of the application tile.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 383** External Reference Application

## **Gain**

You can increase or decrease the magnification of the trace display.

**1.** Select **Gain** to open the magnification menu.

**2.** Select one of the preset magnifications for fixed gain: 1.0x, 2.0x, 5.0x.

## **Horizontal and Vertical Position**

**Note:** External Reference is AC coupled. If signals other than: NTSC Black Burst with setup, PAL Black Burst, or Tri-Level Sync is applied, the V Pos needs to be manually changed to move the blanking to the zero mV/IRE.

You can adjust the horizontal and vertical positions of the trace independently of each other.

- To adjust the horizontal position:
  - Touch-and-drag to move the trace on the touchscreen.

  - Click-and-drag to move the trace on a non-touch screen. The H Pos must be unlocked for this function (no lock on the H Pos button).

  - **i.** If there is a lock in the H Pos button, select **H Pos** to remove the lock.

  - **ii.** Click-and-drag to move the trace.

  - Select the **Plus** (+) button or **Minus** (-) button for incremental changes.

  - **i.** Select **H Pos** .

  - **ii.** Select the **Plus** (+) button or **Minus** (-) button to change the position.

  - Select the **Reset** icon ( ) to move the horizontal position to the default.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **384 Application Information** External Reference Application

- To adjust the vertical position:
  - Touch-and-drag to move the trace on the touchscreen.

  - Click-and-drag to move the trace on a non-touch screen. The V Pos must be unlocked for this function (no lock on the V Pos button).

  - **i.** If there is a lock in the V Pos button, select **V Pos** to remove the lock. **ii.** Click-and-drag to move the trace.

  - Select the **Plus** (+) button or **Minus** (-) button for incremental changes.

  - **i.** Select **V Pos** .

  - **ii.** Select the **Plus** (+) button or **Minus** (-) button to change the position.

  - Select the **Reset** icon ( ) to reset the vertical position adjustment to default.

## **Display Format**

To change the Sweep of the waveform:

**1.** Select **Sweep:** in the bottom right corner of the application to expand the available display format options (the button label varies depending on the last option selected) and select the Sweep option, and in some cases the magnification, as needed.

**2.** Select the Sweep option as needed: 1 line, 2 line, 1 field, or 2 field.

**3.** Select the **Mag** option to set the magnification to Best or 1.0x. The Best magnification option works only with sweep types 2 Line and 2 Field.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 385** External Reference Application

**4.** The information at the bottom of the tile notes if the instrument is set to LoopThrough Input to Output or to Terminate Input. To change this setting, select **Settings** , select **Reference** , select the **ANALOG SETTINGS** tab, and choose the input or output setting. See _Select a reference I/O option:_ .

External Reference Display supports the following input formats:

- Black Burst:
  - PAL – 625i

  - NTSC – 525i

- Tri-Level Sync:
  - 720p – 50, 59.94, 60

  - 1080i – 50,59, 60

  - 1080psF – 23.98

  - 1080p – 23.98, 24,25, 29.97, 30, 50, 59.94, 60

**Note:** Source Input and External Reference should have a matching frame rate.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **386 Application Information** Audio-Video Delay Application

## **Audio-Video Delay Application**

The Audio-Video Delay display shows any difference between the video signal and the timing of the audio. The measurement uses the video signal as the 0 line in the display and if the audio signal is in advance or delayed of it. The thresholds for the audio occurring before or after the video can be set. If the audio signal is outside of either limit (later than the delay threshold or before the advance threshold), the display shows a yellow bar.

**Note:** The application requires the MPSDP-ENG-QC license.

The application can monitor up to 16 channels.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 387** Audio-Video Delay Application

**Note:** This application requires a test-signal source with an AV timing mode enabled from a Telestream device such as the TG8000, SPG8000A, or SPG9000.

## **Configure the Audio-Video Delay Application**

**1.** Select the **Tiles** icon ( ).

**2.** Select the tile with the Audio-Video Delay application.

**3.** Select the **Tile** icon ( ).

**Note:** To move the settings left or right, select the **Move** icon ( ) in the Settings menu header.

**4.** The Advance Threshold number is the time the audio test signal can arrive before the visual test signal arrives (to the left of the 0 line) and not register as an error; that is, the channel is green in the display. To change the Advance Threshold number, in the **Advance Threshold** box, type the number or select the up or down arrows.

**Note:** The number in the menu is shown as positive, but in the display it is marked as negative, such as -22, and is only to the left of the 0 line.

**5.** The Delay Threshold number is the time the audio test signal can arrive _after_ the visual test signal arrives (to the _right_ of the 0 line) and not register as an error; that is, the channel is green in the display. To change the Delay Threshold number, in the **Delay Threshold** box, type the number or select the up or down arrows.

**6.** The User Offset allows moving the 0 line in advance or delay of the visual test signal arrival. Set **Apply Offset** to **On** to turn on the offset. The offset setting is on the top right of the tile.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **388 Application Information** Audio-Video Delay Application

**7.** To change the Apply Offset number, in the **User Offset** box, type the number or select the up or down arrows.

- A positive number in the field moves the 0 line to the left of the incoming signal, so the signal arrives in advance. The Time and Frames measurements are positive.

- A negative number in the field moves the 0 line to the right of the incoming signal, so the signal arrives delayed. The Time and Frames measurements are negative.

The following example shows an offset of 10 ms Advanced, making the correctly timed visual test signal appear to arrive 10 ms delayed.

The following example shows an offset of 33 ms Delayed, making the correctly timed visual test signal appear to arrive 33 ms early.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 389** IP Display and Generator Applications

## **IP Display and Generator Applications**

The IP Display and IP Generator applications use the 10G/25G IP ports to transmit ST 2110 streams, so they are both included in the same application if the IP Generator option has been purchased. Otherwise, only the standard IP Display application is present.

You can use the IP Display application to send the tiled PRISM display as an ST 2110 stream for multiviewer applications.

If you have an IP Generator license, you can check the receiver device and signal path via the IP Generator application, which provides ST 2110 -20/-30 with ST 2022-7 test signals. The application is available only in the 200 and 300 versions of MPS, MPD, and MPP.

## **Note:** The IP Generator application requires Option MPSDP-GEN.

.

## **Configure the IP Display Application**

**1.** Select the **Tiles** icon ( ).

**2.** Select the tile with the IP Display application.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **390 Application Information** IP Display and Generator Applications

**3.** Select the **Tile** icon ( ).

**Note:** To move the settings left or right, select the **Move** icon ( ) in the Settings menu header.

**4.** In the **IP Generator Mode** section, select **Display** .

**5.** Select **IP ST 2110 Display** to enable or disable the IP ST 2110 Display.

**6.** In the **Reference** section, select the IP Generator reference: **Internal** or **PTP** .

**7.** The **Resolution** section indicates the resolution.

**8.** From the **Frame Rate** list, select the frame rate (only the frame rates available for the selected resolution appear):

- **59.94i:** available for resolution 525i.

- **50i:** available for resolution 625i.

- **23.98p** , **24p** , **25p, 29.97p** , **30p, 50p** , **50i** , **59.94p** , **59.94i** , **60p** , and **60i:** available for resolution 1920x1080.

- **23.98p** , **24p** , **25p** , **29.97p** , **30p** , **50p** , **59.94p** , **and 60p:** available for all other resolutions.

**Note:** The resolution 4096x2160 is limited to a maximum frame rate of 50p if the Video IP Port Data Rate is set to 10Gb.

**9.** From the **Structure** list, select **YCbCr 4:2:2 10bit** or **RGB 4:4:4 12bit** (for supported Resolution and Frame rates, and for matching receiver, see _Supported Video Formats in ST 2110-20 Streams_ ).

**10.** In the **RTP Payload Type** box, set the generated IP stream to an RTP Payload Type number between 96 and 127.

**Note:** Each generated IP stream must have a unique RTP Payload Type number.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 391** IP Display and Generator Applications

**11.** Select **DISPLAY 1** and **DISPLAY 2** to enable or disable them as needed. Display 2 is the extended display if you enable that option in the **Settings > Display** menu. Otherwise, it is a mirror of Display 1.

**12.** For enabled ports, enter addresses into the **Destination Addr.** and **Destination Port** boxes. When enabled and the fields are filled in, each port is configured automatically.

**Note:** The Source IP Address, Source Port, Source MAC Address, and Destination MAC Address are configured automatically based on the Destination Address and Destination Port.

**13.** Select **Save** .

## **IP Display NMOS Operation**

When the IP Display generator is enabled, an NMOS device is created and registered.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information**

**392**

IP Display and Generator Applications

The device contains a video sender for each display. Each sender advertises the current generator settings via the IS-04 and IS-05 APIs. Performing an activation on a sender will configure the destination address and port for that display.

**Note:** The Display senders only support single leg (path 1) operation.

## **Configure IP Display SDP Files**

SDP files are created when the IP Display function is enabled. To see the SDP files:

**1.** In the PRISM web interface, select **IP Display & Generator SDP Files** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 393** IP Display and Generator Applications

**2.** In the **IP Display SDP File(s)** section, select **Display1 SDP File** or **Display2 SDP File** to view the contents of the file

**3.** In the **IP Test Signal SDP Files** section, select the file to use in test signal mode: **Video SDP File** or **Audio SDP File** .

**4.** To copy SDP file contents to the Clipboard, select **Copy to Clipboard** .

**5.** To Export SDP file contents, select **Export to File** and save the file locally.

**6.** To close an SDP file, select **Close** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **394 Application Information** IP Display and Generator Applications

## **IP Display Elements**

Display tabs provide information about the Stream 1 and Stream 2 status for both displays.

## **View the TRANSPORT Status**

Select the **TRANSPORT** tab to view the status of the IP streams.

## **View Video Stream Settings**

Select the **VIDEO** tab to view the settings of the video streams.

## **Configure the IP Generator Application**

**1.** Select the **Tiles** icon ( ).

**2.** Select the tile with the IP Generator application.

**3.** Select the **Tile** icon ( ).

**Note:** To move the settings left or right, select the **Move** icon ( — ) in the Settings menu header.

**4.** In the **IP Generator Mode** section, select **Test Signal** .

**5.** Select **IP ST 2110 Generator** to enable or disable the IP ST 2110 Generator.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 395** IP Display and Generator Applications

**6.** In the **Reference** section, select the IP Generator reference: **Internal** or **PTP** .

## **Configure the Video Test Signal**

**1.** In the **TEST SIGNAL** section, select **Video** .

**2.** Select **Enable Video** to enable or disable the test signal video.

**3.** In the Video Transport section, select the video transport protocol: **ST2110-20** or **ST2110-22** .

**4.** From the **Resolution** list, select **525i** , **625i** , **1280x720** , **1920x1080** , **2048x1080** , **3840x2160** , or **4096x2160** .

**5.** From the **Frame Rate** list, select the frame rate (only the frame rates available for the selected resolution appear):

- **59.94i:** available for resolution 525i.

- **50i:** available for resolution 625i.

- **23.98p** , **24p** , **25p, 29.97p** , **30p, 50p** , **50i** , **59.94p** , **59.94i** , **60p** , and **60i:** available for resolution 1920x1080.

- **23.98p** , **24p** , **25p** , **29.97p** , **30p** , **50p** , **59.94p** , **and 60p:** available for all other resolutions.

**Note:** The resolution 4096x2160 is limited to a maximum frame rate of 50p if the Video IP Port Data Rate is set to 10Gb.

**6.** From the **Structure** list, select **YCbCr 4:2:2 10bit** or **RGB 4:4:4 12bit** (for supported Resolution and Frame rates, and for matching receiver, see _Supported Video Formats in ST 2110-20 Streams_ ).

**7.** From the **Pattern** list, select **Black** or **100% Color Bars** .

**8.** Select **Motion** to enable or disable horizontal motion of the color bars.

**Note:** The Motion option is unavailable when Pattern is set to Black.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **396 Application Information** IP Display and Generator Applications

**9.** In the **Packing Mode** section, select one of the following:

- **Block:** Block Packing Mode is based on 180-byte blocks and supports many formats.

- **General:** General Packing Mode follows the open packing standards of RFC 4175.

**10.** In the **RTP Payload Type** box, set the generated IP stream to an RTP Payload Type number between 96 and 127.

**Note:** Each generated IP stream must have a unique RTP Payload Type number.

**11.** In the **Packet Read Schedule (PRS)** section, select one of the following:

- **Gapped:** Gapped PRS reads packets at an equally spaced sequence throughout the active field or frame interval and accounts for vertical blanking (gaps).

- **Narrow (Linear):** Narrow (linear) PRS reads the packets at an equally spaced sequence throughout a video frame.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 397** IP Display and Generator Applications

**12.** If ST2110-22 (JPEG XS) was selected as the video transport:

- **A.** In the **Compression Ratio** section, select one of the following: **5:1** , **10:1** , or **20:1** .

- **B.** In the **Quality** section, select one of the following:
  - ♦ **PSNR:** The JPEG XS encoder is configured to optimize the image quality based on the Peak Signal to Noise Ratio (PSNR) calculation.

  - ♦ **Visual:** The JPEG XS encoder is configured for an optimal real-life subjective quality assessment. This option can provide a better viewing experience, but it sometimes produces lower PSNR results.

**13.** Select **VIDEO PORT SFP 1** and **VIDEO PORT SFP 2** to enable or disable them as needed.

**14.** For enabled ports, enter addresses into the **Destination Addr.** and **Destination Port** boxes. When enabled and the fields are filled in, each port is configured automatically.

**Note:** The Source IP Address, Source Port, Source MAC Address, and Destination MAC Address are configured automatically based on the Destination Address and Destination Port.

## **Configure the Audio Test Signal**

**1.** In the **TEST SIGNAL** section, select **Audio** .

**2.** Select **Enable Audio** to enable or disable it.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **398 Application Information** IP Display and Generator Applications

**3.** In the **Channels** section, select **2** or **8** channels.

**4.** In the **Frequency** section, select **1-kHz** or **Multiple** .

**5.** In the **Amplitude** section, select one of the following options:

- **Mute:** always available

- - **20 dBFS:** available when Frequency is set to 1 kHz

- - **18 dBFS:** available when Frequency is set to 1 kHz

- **Multiple:** available when Frequency is set to Multiple

**6.** The Sample Depth (all Channels) section lists the sample depth of all channels. The following table shows the audio test signal values in each channel when both Frequency and Amplitude, in the Settings menu, are set to Multiple.

Multiple Settings with Amplitude and Frequency Levels Per Channel

| **Channel** | **Amplitude (dBFS)** | **Frequency (Hz)** |
| ----------- | -------------------- | ------------------ |
| 1           | -18                  | 240                |
| 2           | -22                  | 480                |
| 3           | -20                  | 360                |
| 4           | -28                  | 120                |
| 5           | -24                  | 600                |

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 399** IP Display and Generator Applications

Multiple Settings with Amplitude and Frequency Levels Per Channel (Continued)

| **Channel** | **Amplitude (dBFS)** | **Frequency (Hz)** |
| ----------- | -------------------- | ------------------ |
| 6           | -26                  | 1200               |
| 7           | -30                  | 1800               |
| 8           | -32                  | 2400               |

**7.** In the **Packet Time** section, select **125 µs** or **1 ms** .

**8.** In the **RTP Payload Type** box, type an RTP Payload Type number for the generated IP stream.

**Note:** Each generated IP stream must have a unique RTP Payload Type number.

**9.** Select **AUDIO PORT SFP 1** and **AUDIO PORT SFP 2** to enable or disable them as needed.

**10.** For enabled ports, enter addresses into the **Destination Addr** . and **Destination Port** fields. When enabled and the fields are filled in, each port is configured automatically.

**Note:** The Source IP Address, Source Port, Source MAC Address, and Destination MAC Address are configured automatically based on the Destination Address and Destination Port.

**11.** Select **Save** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **400 Application Information** IP Display and Generator Applications

## **Test Signal NMOS Operation**

When the IP Test Signal generator is enabled, an NMOS device is created and registered.

The device contains one video sender and one audio sender. Each sender advertises the current generator settings via the IS-04 and IS-05 APIs. Performing an activation on a sender will configure the destination address and port for that display.

## **Configure IP Generator SDP Files**

SDP files are created when the IP Display function is enabled. To see the SDP files:

**1.** In the PRISM web interface, select **IP Display & Generator SDP Files** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 401** IP Display and Generator Applications

**2.** In the **IP Display SDP File(s)** section, select **Display1 SDP File** or **Display2 SDP File** to view the contents of the file

**3.** In the **IP Test Signal SDP Files** section,.select the file to use in test signal mode: **Video SDP File** or **Audio SDP File** .

**4.** To copy SDP file contents to the Clipboard, select **Copy to Clipboard** .

**5.** To Export SDP file contents, select **Export to File** and save the file locally.

**6.** To close an SDP file, select **Close** .

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **402 Application Information** IP Display and Generator Applications

## **IP Generator Elements**

Display tabs provide information regarding the generated IP streams. Select a tab to view the associated display.

## **View TRANSPORT Status**

Select the **TRANSPORT** tab to view the status of the generated IP streams.

## **VIDEO Tab**

Select the **VIDEO** tab to view the settings of the generated video stream.

## **View AUDIO Stream Settings**

Select the **AUDIO** tab to view the settings of the generated audio stream.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 403** SDI Generator Application

## **SDI Generator Application**

The SDI Generator application provides SDI video signals that can be used to check the receiver device and the signal path.

**Note:** The SDI Generator application requires Option MPSDP-GEN.

## **Configure the SDI Generator Application**

**1.** Select the **Tiles** icon ( ).

**2.** Select the tile with the SDI Generator application.

**3.** Select the **Tile** icon ( ).

**Note:** To move the settings left or right, select the **Move** icon ( - ) in the Settings menu header.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **404 Application Information** SDI Generator Application

**4.** Set **Enable SDI Generator** to **Enabled** or **Disabled** .

**5.** The Reference section indicates that the SDI Generator uses an internal reference.

**6.** From the **Format** list, select the format: **SD** , **HD 720** , **HD1080** , **3G Level A** , **3G Level B** , **6G UHD** , or **12G UHD** .

**7.** In the **Frame Rate** list, select the frame rate (only the frame rates available for the selected format appear):

- **525i 59.94:** for format SD only

- **625i 50:** for format SD only

- **720p 50:** for format HD 720 only

- **720p 59.94:** for format HD 720 only

- **720p 60:** for format HD 720 only

- **1080i 50:** for format HD 1080 only

- **1080p 50:** for format 3G LevelA or 3G LevelB only

- **1080i 59.94:** for format HD 1080 only

- **1080p 59.94:** for format 3G LevelA or 3G LevelB only

- **1080i 60:** for format HD 1080 only

- **1080p 60:** for format 3G LevelA or 3G LevelB only

- **3840p 23.98:** for format 6G UHD only

- **3840p 24:** for format 6G UHD only

- **3840p 25:** for format 6G UHD only

- **3840p 29.97:** for format 6G UHD only

- **3840p 30:** for format 6G UHD only

- **3840p 50:** for format 12G UHD only

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**Application Information 405** SDI Generator Application

- **3840p 59.94:** for format 12G UHD only

- **3840p 60:** for format 12G UHD only

**8.** The Pattern section lists the only pattern, 100% Color Bars.

**9.** Select **Motion** to enable or disable horizontal motion of the color bars.

## **SDI Generator Elements**

Select the **VIDEO** tab to view the settings of the generated SDI stream.

**Note:** SDI audio and data generation is not yet available.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **406 PTP Operational Overview** PTP Introduction

## **PTP Operational Overview**

This chapter provides an overview of PTP network operation. Not all of the functionality described is available in the PRISM monitor.

## **PTP Introduction**

This describes how a PTP leader is chosen, with some description of the priorities. It also explains some of the relationship between the potential devices.

## **PTP Leader Selection**

In a PTP network, all the leaders on the network are evaluated by the Best Master Clock Algorithm (BMCA). The BMCA runs on all devices, and chooses a leader based on several parameters. Some of the parameters relate to clock quality; conversely the Priority 1 and Priority 2 parameters are set by the user to influence the choice of a leader:

**Note:** The PRISM monitor has no role in setting the priority parameters or in providing information to the BMCA.

- Priority 1: This parameter defines which clocks are allowed to be considered as leaders. To be considered as a leader, the value should be set to 128 or less. Priority 1 is the first criteria in the BMCA, so if Priority 1 is set to a lower value than other devices on the system, then it is chosen even if the clock quality is poor. Typically, all the leaders in a domain should have the same value for the Priority 1 parameter.

- Priority 2: This parameter is used to break the tie between leaders that have the same clock quality. Several values can be used to define a hierarchy of devices. Most profiles use 128 as a default, so a value of 127 or lower would indicate a preferred leader.

- The final tiebreaker in the BMCA is the clock ID. This is usually the MAC address, so it provides a unique value by which the BMCA can choose.

## **Network Topology**

In a typical IEEE1588 PTP network, many devices can be either leaders or followers. If the current leader stops working, all the devices that are capable of being a leader broadcast their clock quality and a new leader is selected.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**PTP Operational Overview 407** Five Basic PTP Timing Messages

For video networks it might make sense to depart from the telecom-style PTP topology and dedicate devices to be only leaders or followers. This is the approach supported by the PRISM monitor, which allows for a more traditional primary and backup leader structure controlling a range of follower devices. The BMCA is still used to select the active leader and the network still takes the place of the ECO in the legacy Black-burst/ Tri-level network. The PRISM monitor is a follower-only device.

## **Five Basic PTP Timing Messages**

This section describes the five basic timing messages in a PTP system. Other messages are present in some instances. For example, grant requests and responses appear in unicast systems, and Type Length Value (TLV) management messages appear in ST 2059 profile systems.

## **Announce Message**

The Announce message is sent by the leader to advertise its capability. This message contains the clock quality and priority settings needed for the BMCA to evaluate which device is the best leader.

## **Sync Message**

The Sync message is sent by the leader and is used to measure the propagation delay from the leader to the follower. The sync message might contain the timestamp indicating when it was sent, or that time might be in the Follow-up message. The receiver must timestamp the sync message upon receipt. These two timestamps are usually called t1 and t2 and provide the first delay measurement.

## **Follow-up Message**

The Follow-up message is sent only in cases where the PTP network hardware is not capable of inserting the timestamp or corrections into the Sync message. (See _One-Step and Two-Step Operation_ .)

## **Delay Request Message**

The Delay request is sent by the follower. The time it is sent is noted by the follower but is not included in the message. This time is usually called t3. When the delay request is received by the leader, the leader timestamps the receive time. This timestamp is usually called t4.

## **Delay Response Message**

The Delay response is sent from the leader to the follower. The response contains the t4 timestamp from when the leader received the delay request. After the follower receives

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **408 PTP Operational Overview** Profiles and Domains

the delay response, it has the second pair of timestamps needed to calculate the second delay measurement of the follower to leader delay.

## **Message Timing**

The example shows the relationships between the five PTP timing messages.

## **Profiles and Domains**

Multiple domains and profiles can coexist on the same network.

## **Profiles**

The IEEE1588 standard defines multiple parameters, such as the rates for Sync and Announce messages, and optional functions such as grandmaster clusters. Specific industries wanting to use PTP are encouraged to define their own “profile,” which allows the PTP standard to be tuned for specific applications. The profile defines the default and range of each parameter, and defines which options are required, allowed, or prohibited.

In the PRISM monitor, the user should select the PTP profile (General, ST 2059, or AES67). The user can then modify the profile parameters and save as part of an

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**PTP Operational Overview 409** One-Step and Two-Step Operation

instrument preset. The allowed range of the parameters is restricted to that which is allowed for the selected profile type.

## **Domains**

The IEEE1588 standard defines “domains,” which allow multiple PTP services to coexist simultaneously on one physical Ethernet connection. For example, on a given network one leader and several followers can be using domain 0 while a second leader and other followers are using domain 1. These two PTP services are independent. One use for this is to have leaders on different domains provide PTP on different profiles. For example, domain 0 might be an AES67 profile, domain 1 could be a leader using the AVB (802.1AS) profile, and domain 127 could be a leader on the ST 2059 profile.

## **One-Step and Two-Step Operation**

Some PTP messages have a timestamp associated with them. This timestamp indicates the time of the local clock when the message was sent or received. In some cases, the hardware is capable of embedding the timestamp in the message as it is sent. This is known as “one-step” mode because the message and its associated time are sent together.

In other cases, the hardware is not capable of inserting the time into the message, so instead it is sent in a second Follow-up message. This is called “two-step” mode because there are two messages.

Be aware that in End-to-End mode, only the Sync message is affected by the one-step and two-step setting because it is the only message that needs the transmit time stamp inserted. In a similar fashion, Peer-to-Peer mode has some messages that might require follow-up support.

The IEEE1588 standard specifies that all followers are required to operate with either one-step or two-step message types. One type of device that often requires two-step operation is a Transparent Clock, because it has to calculate the residence time of a message and insert that time into the message or the follow-up message.

## **Multicast, Unicast, and Mixed Communication Modes**

There are three basic message modes for PTP: Multicast, Unicast, and mixed Multicast and Unicast. For full Multicast or Unicast modes, all of the PTP messages are sent in the selected mode type.

For some profiles, such as some telecom profiles and the ST2059 profile, a mixture of Multicast and Unicast are allowed. On the SMPTE profile unique mixed mode, the Announce and Sync messages are sent as multicast. However, the Delay Request and Delay Response messages are sent as Unicast.Therefore, it is important to ensure

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **410 PTP Operational Overview**

Multicast, Unicast, and Mixed Communication Modes

correct configuration of IP addresses and layer three communication to ensure that the Delay Request and Response are transmitted and received correctly.

Some points to understand about communication modes:

- Whatever mode is chosen, the leader and follower must match or be compatible.

- Multicast and Mixed mode might need IGMP joins and leaves.

- Full Unicast must have the leader address in all follower AMTs.

- Unicast without negotiation does not allow leader to regulate load.

- Two leaders can be used on different domains to serve followers on different communication modes.

All of the leader and follower devices on a given domain must use compatible communication modes. For most profiles, this means the leader and follower communication modes need to match exactly. On the SMPTE profile, the Multicast and Mixed modes are compatible, so a leader in any of these modes should work with a follower in any of those modes.

## **Multicast System Messages**

Multicast messages are broadcast and so they can be received without knowing the address of the sender. This allows a follower to hook up to the network, receive the announce messages and discover the identity of the leader. Multicast in some networks requires the devices to use IGMP to join and leave the multicast group.

In Multicast PTP systems, the leader sets the rate of the announce and sync messages. The leader also sends the maximum allowed delay request rate in the delay response message. Ideally, the follower uses that value to set the delay request rate although some followers set this rate independently. The delay request rate is typically the same as the sync rate, but might be higher or lower.

## **Unicast System Messages**

Unicast messages require the address of the leader be entered into the Acceptable Master Table (AMT) in each follower. If there are multiple leaders, the IP address for each leader must be entered in the AMTs of all the followers.

In Unicast PTP systems, the follower must have the address of the leader in its acceptable leader table because the follower initiates the communication with the leader. The follower sends several grant requests to the leader requesting specific rates for each message type. If the leader accepts the grant requests, it sends grant acknowledges. If the leader denies the grant, the follower might send a new grant request at a lower rate. This process might continue for several iterations until the leader and follower agree on a rate. The leader and follower then start exchanging the PTP messages. If the leader cannot support any of the rates requested by the follower, then the follower cannot lock to the leader.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**PTP Operational Overview 411** BMCA Operation

## **Mixed Mode System Messages**

In Mixed Mode systems, some messages are Multicast and some are Unicast. For the ST 2059 profile, the Announce and Sync messages are sent as Multicast. This allows devices to discover the active leader. The Delay Request messages are configured as Unicast, in some case with negotiation, and in other cases without negotiation.

## **SMPTE Profile System Messages**

For SMPTE profile systems, a given domain must use one type of message for all Announce, Sync, and Follow-up messages. Therefore, all leaders and followers on that domain must be configured for either Multicast or they all must be configured for Unicast.

For SMPTE mixed mode, the Announce, Sync, and Follow up messages are configured as Multicast, whereas the delay requests can be Multicast, Unicast, or Unicast without negotiation. To use this combination with an SPG8000A or SPG9000 reference clock generator, set the leader and follower to any of the modes: Multicast, Mixed, or Mixed without negotiation. The leaders support all of the follower modes simultaneously.

## **BMCA Operation**

The Best Master Clock Algorithm (BMCA) is used to choose the active leader on the domain. This is partially explained in the introduction to this document. The BMCA operation varies somewhat as function of communication mode.

## **Multicast Mode**

In Multicast mode, the active leader sends announce messages which all other leaders and followers can receive. So all devices can evaluate the BMCA and decide on the best leader. If any device detects that its BMCA rating is better than the current leader, it sends an announcement and takes over as the active leader.

## **Unicast Mode**

In Unicast mode, followers only get Announce messages if they establish a grant from the leader. Therefore, each follower must set up a grant with every device in its AMT. Since the leaders do not set up grants from other leaders, they do not have the information to evaluate the BMCA and know if they are the active leader. It is up to the followers to evaluate the BMCA based on the Announce message they get from each leader in their AMT. Each follower then decides which leader is the best and then set up grants for the other message types. If followers on a given network have a different list of leaders in their AMT, then they might choose a different leader.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **412 PTP Operational Overview** Compensating for Causes of Asymmetric Delay

## **Mixed Mode**

In a ST 2059 mixed environment, the announce message is Multicast. Therefore, the BMCA can follow the Multicast conventions.

## **Compensating for Causes of Asymmetric Delay**

Several factors can cause the PTP message delay to be different for the messages sent from the leader to follower as opposed to the messages the other direction from the follower to leader. Unless corrected, this propagation delay asymmetry causes an offset in the clock phase equal to ½ the difference in the two path delays. There are several main causes of asymmetric delay:

- Rate mismatch in the ports on a switch

- Traffic mismatch on the two paths

- Message type mismatch

- Cable delay variation

This section contains suggestions on how to design the system to minimize the delay asymmetry. Alternatively, some followers provide a way to manually enter a correction value to cancel the delay error.

## **Rate Mismatch**

Rate mismatch in a switch causes a delay asymmetry because the switch performs a “store and forward” action on messages. This means the entire message must be stored in the buffer before it starts to be “forwarded” or sent out. For example, for a 100 Mb input and 1 Gb output, the switch must wait for the entire message to clock in at the slow rate before it can start outputting the message at the high rate. Conversely for a 1 Gbps input and 100 Mbps output, the entire packet is quickly read in at the faster rate, so then the output can start sooner but at a lower rate.

While the total time is the same for both directions, the delay on the fast-in, slow-out direction is shorter on the packets, which contain the PTP time stamps. This effect is significant on a 100-Mb to 1-Gb rate mismatch, but much less significant on a 1-G to 10G switch since the message time at 1 Gbps is quite short. If the switch supports Transparent Clock (TC) mode, then this rate mismatch delay effect is corrected by the TC delay correction.

## **Traffic Mismatch**

Another cause of asymmetric delay is traffic mismatch on the two paths. If there is a high percentage of traffic utilization on the leader to follower path, then most of the PTP messages might be delayed significantly. If the traffic on the other direction is significantly different, then the messages on the path might not suffer the same delay.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

**PTP Operational Overview 413** Compensating for Causes of Asymmetric Delay

This effect can be quite large depending on the traffic, the quality of the switch, and the number of switches in the network. To reduce this effect, a user should avoid large loading on the PTP network, use high-quality switches that avoid this delay variance, or use PTP Transparent mode switches that insert residence time information to allow the follower to correct for this delay.

Setting the Diff Serve QoS on the switch and configuring the PTP messages with an appropriate DSCP can also mitigate the effects of traffic delay.

## **Message Type Mismatch**

Another cause of delay asymmetry is message-type mismatch. For example, if the sync message is Multicast and the delay request is Unicast, then some switches might process the messages differently and cause a differential delay. Because the SMPTE profile allows a mixed mode operation, switches should be evaluated to ensure they do not have this effect. If transparent mode switches are used, then this effect should be corrected by the follower.

## **Cable Delay Variation**

The actual propagation delay through Category 5 cable can be significantly different in one direction versus the other direction. This can be due to the twist rate on the pairs, routing inside the sheath, material differences, etc. The PTP system is incapable of removing this effect, so the best way to prevent this is to use high-quality cable with a minimum variation in the physical propagation delay.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**

> **414 NMOS Specifications** NMOS Discovery Version 1.3

## **NMOS Specifications**

This chapter summarizes key NMOS specifications. Some of the specifications might not be available in the PRISM monitor.

## **NMOS Discovery Version 1.3**

The changes in NMOS Discovery version 1.3 are summarized here.

- Added additional network data for nodes as required by IS-06.

- Deprecated mDNS announcements for nodes in registered mode.

- Replaced DNS-SD service type for registration API.

- Permit deprecated node API connection management is not implemented.

- Added explicit requirements for 501 responses when features are not implemented.

- Added support for future device and transport types.

- Permitted a sender's “manifest_href” to be null when the transport type does not require a transport file.

- Added 409 response code for registries with conflicting resources.

- Added support for signaling authorization requirements.

- Indicated the potential for source/flow attributes and caps will be defined externally in the future.

- Revised the discovery process to ignore mDNS records when unicast records are available.

**PRISM MPS, MPD, and MPP SDI / IP Waveform Monitor User Manual**
