---
title: 'Video Test and Monitoring Equipment'
source: 'https://www.telestream.net/video/prism-tech-spec.htm'
author:
published:
created: 2026-05-25
description: 'Highly scalable cloud based video encoding / transcoding service. Encode in any format, deliver to any device.'
tags:
  - 'clippings'
---

## The PRISM Family

| Model   | Form Factor    | Depth | Interface                      | SDI Inputs Capability (4 x 12G SDI)\* | IP Inputs Capability (2 x 10G/25G)\* | Eye Measurement capability (12G SDI)\* | Format Support (SD,HD,3G,4K,8K)\* | Power Input |
| ------- | -------------- | ----- | ------------------------------ | ------------------------------------- | ------------------------------------ | -------------------------------------- | --------------------------------- | ----------- |
| MPS-100 | 3RU, Half-rack | 5”    | 1920 x 1080 9” Touchscreen x 1 | Standard                              | X                                    | X                                      | Standard                          | AC/DC       |
| MPS-200 | 3RU, Half-rack | 5”    | 1920 x 1080 9” Touchscreen x 1 | Standard                              | Standard                             | X                                      | Standard                          | AC/DC       |
| MPS-300 | 3RU, Half-rack | 5”    | 1920 x 1080 9” Touchscreen x 1 | Standard                              | Standard                             | Standard                               | Standard                          | AC/DC       |
| MPD-100 | 3RU, Full-rack | 5”    | 1920 x 1080 9” Touchscreen x 2 | Standard                              | X                                    | X                                      | Standard                          | AC          |
| MPD-200 | 3RU, Full-rack | 5”    | 1920 x 1080 9” Touchscreen x 2 | Standard                              | Standard                             | X                                      | Standard                          | AC          |
| MPD-300 | 3RU, Full-rack | 5"    | 1920 x 1080 9" Touchscreen x 2 | Standard                              | Standard                             | Standard                               | Standard                          | AC          |
| MPP-100 | 1RU, Full-rack | 11”   | External Monitor               | Standard                              | X                                    | X                                      | Standard                          | AC          |
| MPP-200 | 1RU, Full-rack | 11”   | External Monitor               | Standard                              | Standard                             | X                                      | Standard                          | AC          |
| MPP-300 | 1RU, Full-rack | 11”   | External Monitor               | Standard                              | Standard                             | Standard                               | Standard                          | AC          |

## Video Format Support

## Supported SDI video formats

<table><thead><tr><th>Link</th><th>Format</th><th>Sample Structure</th><th>Bits</th><th>Frame/field rate</th><th>Audio</th><th>Option</th></tr></thead><tbody><tr><td rowspan="2">SD-SDI</td><td>525i</td><td>4:2:2 YCbCr</td><td>10b</td><td>59.94i</td><td>16ch</td><td>Standard</td></tr><tr><td>625i</td><td>4:2:2 YCbCr</td><td>10b</td><td>50i</td><td>16ch</td><td>Standard</td></tr></tbody><tbody><tr><td rowspan="4">HD-SDI</td><td>1280x720</td><td>4:2:2 YCbCr</td><td>10b</td><td>23.98/24/25/29.97/30/50/59.94/60p</td><td>16ch</td><td>Standard</td></tr><tr><td>1920x1080</td><td>4:2:2 YCbCr</td><td>10b</td><td>50/59.94/60i, 23.98/24/25/29.97/30p, and psF</td><td>16ch</td><td>Standard</td></tr><tr><td>2048x1080</td><td>4:2:2 YCbCr</td><td>10b</td><td>29.97/30p, and psF</td><td>8ch</td><td>Standard</td></tr><tr><td>2048x1080</td><td>4:2:2 YCbCr</td><td>10b</td><td>23.98/24/25p, and psF</td><td>16ch</td><td>Standard</td></tr></tbody><tbody><tr><td rowspan="4">3G SDI Level A</td><td>1920x1080</td><td>4:2:2 YCbCr</td><td>10b</td><td>50/59.94/60p</td><td>16ch</td><td>Standard</td></tr><tr><td>2048x1080</td><td>4:2:2 YCbCr</td><td>10b</td><td>47.95/48/50/59.94/60p</td><td>16ch</td><td>Standard</td></tr><tr><td>1920x1080</td><td>4:4:4 RGB</td><td>10/12b</td><td>23.98/24/25/29.97/30p</td><td>16ch</td><td>PROD*</td></tr><tr><td>2048x1080</td><td>4:4:4 RGB</td><td>10/12b</td><td>23.98/24/25/29.97/30p</td><td>16ch</td><td>PROD*</td></tr></tbody><tbody><tr><td rowspan="6">3G SDI Level B</td><td>1920x1080</td><td>4:2:2 YCbCr</td><td>10b</td><td>50/59.94/60p</td><td>16ch</td><td>Standard</td></tr><tr><td>2048x1080</td><td>4:2:2 YCbCr</td><td>10b</td><td>59.94/60p</td><td>8ch</td><td>Standard</td></tr><tr><td>2048x1080</td><td>4:2:2 YCbCr</td><td>10b</td><td>47.95/48/50p</td><td>16ch</td><td>Standard</td></tr><tr><td>1920x1080</td><td>4:4:4 RGB</td><td>10/12b</td><td>23.98/24/25/29.97/30p</td><td>16ch</td><td>PROD*</td></tr><tr><td>2048x1080</td><td>4:4:4 RGB</td><td>10/12b</td><td>29.97/30p</td><td>8ch</td><td>PROD*</td></tr><tr><td>2048x1080</td><td>4:4:4 RGB</td><td>10/12b</td><td>23.98/24/25p</td><td>16ch</td><td>PROD*</td></tr></tbody><tbody><tr><td rowspan="3">Quad Link HD-SDI Square Division</td><td>3840x2160</td><td>4:2:2 YCbCr</td><td>10b</td><td>23.98/24/25/29.97/30p, and psF</td><td>16ch from Link A</td><td>FMT-4K*</td></tr><tr><td>4096x2160</td><td>4:2:2 YCbCr</td><td>10b</td><td>23.98/24/25p, and psF</td><td>16ch from Link A</td><td>FMT-4K*</td></tr><tr><td>4096x2160</td><td>4:2:2 YCbCr</td><td>10b</td><td>29.97/30p, and psF</td><td>8ch from Link A</td><td>FMT-4K*</td></tr></tbody><tbody><tr><td rowspan="4">Quad Link 3G-SDI Level A, Square Division</td><td>3840x2160</td><td>4:2:2 YCbCr</td><td>10b</td><td>50/59.94/60p</td><td>16ch from Link A</td><td>FMT-4K*</td></tr><tr><td>4096x2160</td><td>4:2:2 YCbCr</td><td>10b</td><td>47.95/48/50/59.94/60p</td><td>8ch from Link A</td><td>FMT-4K*</td></tr><tr><td>3840x2160</td><td>4:4:4 RGB</td><td>10/12b</td><td>23.98/24/25/29.97/30p</td><td>16ch from Link A</td><td>FMT-4K* and PROD*</td></tr><tr><td>4096x2160</td><td>4:4:4 RGB</td><td>10/12b</td><td>23.98/24/25/29.97/30p</td><td>16ch from Link A</td><td>FMT-4K* and PROD*</td></tr></tbody><tbody><tr><td rowspan="4">Quad Link 3G-SDI Level B, Square Division</td><td>3840x2160</td><td>4:2:2 YCbCr</td><td>10b</td><td>50/59.94/60p</td><td>16ch from Link A</td><td>FMT-4K*</td></tr><tr><td>4096x2160</td><td>4:2:2 YCbCr</td><td>10b</td><td>47.95/48/50/59.94/60p</td><td>8ch from Link A</td><td>FMT-4K*</td></tr><tr><td>3840x2160</td><td>4:4:4 RGB</td><td>10/12b</td><td>23.98/24/25/29.97/30p</td><td>16ch from Link A</td><td>FMT-4K* and PROD*</td></tr><tr><td>4096x2160</td><td>4:4:4 RGB</td><td>10/12b</td><td>23.98/24/25/29.97/30p</td><td>16ch from Link A</td><td>FMT-4K* and PROD*</td></tr></tbody><tbody><tr><td rowspan="4">Quad Link 3G-SDI Level A, Two Sample Interleave</td><td>3840x2160</td><td>4:2:2 YCbCr</td><td>10b</td><td>50/59.94/60p</td><td>16ch from Link A</td><td>FMT-4K*</td></tr><tr><td>4096x2160</td><td>4:2:2 YCbCr</td><td>10b</td><td>47.95/48/50/59.94/60p</td><td>8ch from Link A</td><td>FMT-4K*</td></tr><tr><td>3840x2160</td><td>4:4:4 RGB</td><td>10/12b</td><td>23.98/24/25/29.97/30p</td><td>16ch from Link A</td><td>FMT-4K* and PROD*</td></tr><tr><td>4096x2160</td><td>4:4:4 RGB</td><td>10/12b</td><td>23.98/24/25/29.97/30p</td><td>16ch from Link A</td><td>FMT-4K* and PROD*</td></tr></tbody><tbody><tr><td rowspan="4">Quad Link 3G-SDI Level B, Two Sample Interleave</td><td>3840x2160</td><td>4:2:2 YCbCr</td><td>10b</td><td>50/59.94/60p</td><td>16ch from Link A</td><td>FMT-4K*</td></tr><tr><td>4096x2160</td><td>4:2:2 YCbCr</td><td>10b</td><td>47.95/48/50/59.94/60p</td><td>8ch from Link A</td><td>FMT-4K*</td></tr><tr><td>3840x2160</td><td>4:4:4 RGB</td><td>10/12b</td><td>23.98/24/25/29.97/30p</td><td>16ch from Link A</td><td>FMT-4K* and PROD*</td></tr><tr><td>4096x2160</td><td>4:4:4 RGB</td><td>10/12b</td><td>23.98/24/25/29.97/30p</td><td>16ch from Link A</td><td>FMT-4K* and PROD*</td></tr></tbody><tbody><tr><td rowspan="3">6G-SDI</td><td>3840x2160</td><td>4:2:2 YCbCr</td><td>10b</td><td>23.98/24/25/29.97/30p</td><td>16ch</td><td>FMT-4K*</td></tr><tr><td>4096x2160</td><td>4:2:2 YCbCr</td><td>10b</td><td>23.98/24/25p</td><td>16ch</td><td>FMT-4K*</td></tr><tr><td>4096x2160</td><td>4:2:2 YCbCr</td><td>10b</td><td>29.97/30p</td><td>8ch</td><td>FMT-4K*</td></tr></tbody><tbody><tr><td rowspan="5">12G-SDI</td><td>3840x2160</td><td>4:2:2 YCbCr</td><td>10b</td><td>50/59.94/60p</td><td>16ch</td><td>FMT-4K*</td></tr><tr><td>4096x2160</td><td>4:2:2 YCbCr</td><td>10b</td><td>47.95/48/50/59.94/60p</td><td>16ch</td><td>FMT-4K*</td></tr><tr><td>3840x2160</td><td>4:4:4 RGB</td><td>10/12b</td><td>23.98/24/25/29.97/30p</td><td>16ch</td><td>FMT-4K* and PROD*</td></tr><tr><td>4096x2160</td><td>4:4:4 RGB</td><td>10/12b</td><td>23.98/24/25p</td><td>16ch</td><td>FMT-4K* and PROD*</td></tr><tr><td>4096x2160</td><td>4:4:4 RGB</td><td>10/12b</td><td>29.97/30p</td><td>8ch</td><td>FMT-4K* and PROD*</td></tr></tbody><tbody><tr><td>Quad Link 12G-SDI, Two Sample Interleave</td><td>7680x4320</td><td>4:2:2 YCbCr</td><td>10b</td><td>50/59.94/60p</td><td>32ch from Link A/B</td><td>FMT-8K*</td></tr></tbody></table>

\*When ordering MPS, MPD or MPP series add a prefix MPSDP- for the specific option for example FMT-4K would be MPSDP-FMT-4K  
Note: MPSDP-FMT-8K license includes the formats supported by MPSDP-FMT-4K license.

## Supported video formats in SMPTE 2022-6 Streams

<table><thead><tr><th>Link</th><th>Format</th><th>Sample Structure</th><th>Bits</th><th>Frame/field rate</th><th>Option</th></tr></thead><tbody><tr><td rowspan="2">SD-SDI</td><td>525i</td><td>4:2:2 YCbCr</td><td>10b</td><td>59.94i</td><td>Standard</td></tr><tr><td>625i</td><td>4:2:2 YCbCr</td><td>10b</td><td>50i</td><td>Standard</td></tr></tbody><tbody><tr><td rowspan="2">HD-SDI</td><td>1920x1080</td><td>4:2:2 YCbCr</td><td>10b</td><td>50/59.94/60i, 23.98/24/25/29.97/30p, and psF</td><td>Standard</td></tr><tr><td>1280x720</td><td>4:2:2 YCbCr</td><td>10b</td><td>23.98/24/25/29.97/30/50/59.94/60p</td><td>Standard</td></tr></tbody><tbody><tr><td rowspan="2">3G SDI Level A</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1920x1080</td><td>4:2:2 YCbCr</td><td>10b</td><td>50/59.94/60p</td><td>Standard</td></tr></tbody><tbody><tr><td rowspan="2">3G SDI Level B</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1920x1080</td><td>4:2:2 YCbCr</td><td>10b</td><td>50/59.94/60p</td><td>Standard</td></tr></tbody></table>

Not available for MPS-100, MPD-100, and MPP-100 (SDI only)

## Supported ST 2110-20 video formats

<table><thead><tr><th>Link</th><th>Format</th><th>Sample Structure</th><th>Bits</th><th>Frame/field rate</th><th>Option*</th></tr></thead><tbody><tr><td rowspan="15">ST 2110-20</td><td>525i</td><td>4:2:2 YCbCr</td><td>10b</td><td>59.94i</td><td>Standard</td></tr><tr><td>625i</td><td>4:2:2 YCbCr</td><td>10b</td><td>50i</td><td>Standard</td></tr><tr><td>1280x720</td><td>4:2:2 YCbCr</td><td>10b</td><td>23.98/24/25/29.97/30p</td><td>Standard</td></tr><tr><td>1280x720</td><td>4:2:2 YCbCr</td><td>10b</td><td>50/59.94/60p</td><td>Standard</td></tr><tr><td>1920x1080</td><td>4:2:2 YCbCr</td><td>10b</td><td>23.98/24/25/29.97/30p, 50/59.94/60i, 50/59.94/60p</td><td>Standard</td></tr><tr><td>1920x1080</td><td>4:4:4 RGB</td><td>12b</td><td>23.98/24/25/29.97/30/50/59.94/60p</td><td>PROD</td></tr><tr><td>2048x1080</td><td>4:2:2 YCbCr</td><td>10b</td><td>23.98/24/25/29.97/30/50/59.94/60p</td><td>Standard</td></tr><tr><td>2048x1080</td><td>4:4:4 RGB</td><td>12b</td><td>23.98/24/25/29.97/30/50/59.94/60p</td><td>PROD</td></tr><tr><td>3840x2160</td><td>4:2:2 YCbCr</td><td>10b</td><td>23.98/24/25/29.97/30/50p</td><td>FMT-4K</td></tr><tr><td>3840x2160</td><td>4:2:2 YCbCr</td><td>10b</td><td>59.94/60p</td><td>FMT-4K and 25GE</td></tr><tr><td>3840x2160</td><td>4:4:4 RGB</td><td>12b</td><td>23.98/24/25/29.97/30</td><td>FMT-4K and PROD</td></tr><tr><td>4096x2160</td><td>4:2:2 YCbCr</td><td>10b</td><td>23.98/24/25/29.97/30/50p</td><td>FMT-4K</td></tr><tr><td>4096x2160</td><td>4:2:2 YCbCr</td><td>10b</td><td>59.94/60p</td><td>FMT-4K and 25GE</td></tr><tr><td>4096x2160</td><td>4:4:4 RGB</td><td>12b</td><td>23.98/24/25</td><td>FMT-4K and PROD</td></tr><tr><td>4096x2160</td><td>4:4:4 RGB</td><td>12b</td><td>29.97/30</td><td>FMT-4K, PROD and 25GE</td></tr></tbody></table>

Not available for MPS-100, MPD-100, and MPP-100 (SDI only)

\*When ordering MPS, MPD or MPP series add a prefix MPSDP- for the specific option for example FMT-4K would be MPSDP-FMT-4K  
Note: MPSDP-FMT-8K license includes the formats supported by MPSDP-FMT-4K license.

## Supported ST 2110-22 video formats

<table><thead><tr><th>Link</th><th>Format</th><th>Sample Structure</th><th>Bits</th><th>Frame/field rate</th><th>Option*</th></tr></thead><tbody><tr><td rowspan="15">ST 2110-22</td><td>1280x720</td><td>4:2:2 YCbCr</td><td>10b</td><td>23.98/24/25/29.97/30p/50/59.94/60p</td><td>JPXS</td></tr><tr><td>1920x1080</td><td>4:2:2 YCbCr</td><td>10b</td><td>23.98/24/25/29.97/30p, 50/59.94/60i, 50/59.94/60p</td><td>JPXS</td></tr><tr><td>2048x1080</td><td>4:2:2 YCbCr</td><td>10b</td><td>23.98/24/25/29.97/30/50/59.94/60p</td><td>JPXS</td></tr><tr><td>3840x2160</td><td>4:2:2 YCbCr</td><td>10b</td><td>23.98/24/25/29.97/30/50p/59.94/60p</td><td>JPXS and FMT-4K</td></tr><tr><td>4096x2160</td><td>4:2:2 YCbCr</td><td>10b</td><td>23.98/24/25/29.97/30/50p/59.94/60p</td><td>JPXS and FMT-4K</td></tr></tbody></table>

## SMPTE 2110-30/31 Streams

| Conformance level   | Description                                                                                                          |
| ------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Conformance level A | Reception of 48 kHz streams with from 1 to 8 channels at packet times of 1 ms                                        |
| Conformance level B | Reception of 48kHz streams with 1 to 8 channels at packet times of 1 ms or 1 to 8 channels at packet times of 125 µs |

Reception of 48kHz streams with 16 channels at packet times of 125 µs

Not available for MPS-100, MPD-100, and MPP-100 (SDI only)

PRISM instruments with 25GE module have up to eight ST 2110 30 streams of reception with up to 16 audio channels total. One of the streams can be replaced with ST 2110-31.

## SMPTE 2110-40 Stream

PRISM supports four ST 2110-40 streams with multiple ANC packets. One of four streams can be ST2110-43 stream with TTML

Not available for MPS-100, MPD-100, and MPP-100 (SDI only)

## Connectivity and Instrument Dimensions

## MPS-100 Connectivity

[![](https://www.telestream.net/video/images/specs/MPS100Connectivity.png)](https://www.telestream.net/video/images/specs/MPS100Connectivity.png)

## MPS-100 Physical Data

<table><thead><tr><th colspan="2">Dimensions</th></tr></thead><tbody><tr><td>Height</td><td>13.30 cm (5.24 in.)</td></tr><tr><td>Width</td><td>22.00 cm (8.66 in.)</td></tr><tr><td>Depth (inc. Connectors)</td><td>13.07 cm (5.15 in.)</td></tr><tr><td>Weight</td><td>2.77 Kg (6.1 lbs.)</td></tr></tbody></table>

[![](https://www.telestream.net/video/images/specs/MPS100200300PhysicalData.png)](https://www.telestream.net/video/images/specs/MPS100200300PhysicalData.png)

## MPS-200/300 Connectivity

[![](https://www.telestream.net/video/images/specs/MPS200300Connectivity.png)](https://www.telestream.net/video/images/specs/MPS200300Connectivity.png)

## MPS-200/300 Physical Data

<table><thead><tr><th colspan="2">Dimensions</th></tr></thead><tbody><tr><td>Height</td><td>13.30 cm (5.24 in.)</td></tr><tr><td>Width</td><td>22.00 cm (8.66 in.)</td></tr><tr><td>Depth (inc. Connectors)</td><td>12.46 cm (4.91 in.)</td></tr><tr><td>Weight</td><td>2.77 Kg (6.1 lbs.)</td></tr></tbody></table>

[![](https://www.telestream.net/video/images/specs/MPS100200300PhysicalData2.png)](https://www.telestream.net/video/images/specs/MPS100200300PhysicalData2.png)

## MPD-100 Connectivity

[![](https://www.telestream.net/video/images/specs/MPD100Connectivity.png)](https://www.telestream.net/video/images/specs/MPD100Connectivity.png)

## MPD-100 Physical Data

<table><thead><tr><th colspan="2">Dimensions</th></tr></thead><tbody><tr><td>Height</td><td>13.30 cm (5.24 in.)</td></tr><tr><td>Width</td><td>44.50 cm (17.52 in.)</td></tr><tr><td>Depth (inc. Connectors)</td><td>13.07cm (5.15 in.)</td></tr><tr><td>Weight</td><td>3.95 Kg (8.7 lbs.)</td></tr></tbody></table>

[![](https://www.telestream.net/video/images/specs/MPD100physicaldata.png)](https://www.telestream.net/video/images/specs/MPD100physicaldata.png)

## MPD-200/300 Connectivity

[![](https://www.telestream.net/video/images/specs/MPD200300Connectivity.png)](https://www.telestream.net/video/images/specs/MPD200300Connectivity.png)

## MPD-200/300 Physical Data

<table><thead><tr><th colspan="2">Dimensions</th></tr></thead><tbody><tr><td>Height</td><td>13.30 cm (5.24 in.)</td></tr><tr><td>Width</td><td>44.50 cm (17.52 in.)</td></tr><tr><td>Depth (inc. Connectors)</td><td>12.46cm (4.91 in.)</td></tr><tr><td>Weight</td><td>3.95 Kg (8.7 lbs.)</td></tr></tbody></table>

[![](https://www.telestream.net/video/images/specs/MPD200300PhysicalData.png)](https://www.telestream.net/video/images/specs/MPD200300PhysicalData.png)

## MPP-100 Connectivity

[![](https://www.telestream.net/video/images/specs/mpp_front.png)](https://www.telestream.net/video/images/specs/mpp_front.png)  
[![](https://www.telestream.net/video/images/specs/mpp_back_100.png)](https://www.telestream.net/video/images/specs/mpp_back_100.png)

## MPP-100 Physical Data

<table><thead><tr><th colspan="2">Dimensions</th></tr></thead><tbody><tr><td>Height</td><td>4.4cm (1.73in.)</td></tr><tr><td>Width</td><td>48.3cm (19.01in.)</td></tr><tr><td>Depth (inc. Connectors)</td><td>31.3cm (12.32in.)</td></tr><tr><td>Weight</td><td>3.5Kg (7.72lbs.)</td></tr></tbody></table>

[![](https://www.telestream.net/video/images/specs/mpp_side.png)](https://www.telestream.net/video/images/specs/mpp_side.png)

## MPP-200/300 Connectivity

[![](https://www.telestream.net/video/images/specs/mpp_front.png)](https://www.telestream.net/video/images/specs/mpp_front.png)  
[![](https://www.telestream.net/video/images/specs/mpp_back_200-300.png)](https://www.telestream.net/video/images/specs/mpp_back_200-300.png)

## MPP-200/300 Physical Data

<table><thead><tr><th colspan="2">Dimensions</th></tr></thead><tbody><tr><td>Height</td><td>4.4cm (1.73in.)</td></tr><tr><td>Width</td><td>48.3cm (19.01in.)</td></tr><tr><td>Depth (inc. Connectors)</td><td>31.3cm (12.32in.)</td></tr><tr><td>Weight</td><td>3.6Kg (7.94lbs.)</td></tr></tbody></table>

[![](https://www.telestream.net/video/images/specs/mpp_side.png)](https://www.telestream.net/video/images/specs/mpp_side.png)

## Power Characteristics

## MPS-100/200/300

<table><thead><tr><th colspan="2">Power Consumption</th></tr></thead><tbody><tr><td>Typical</td><td>95 W/100 W/105 W</td></tr><tr><td>Maximum</td><td>160 W</td></tr><tr><td>Voltage Range</td><td>100 to 240 VAC +/- 10%, 50/60 Hz</td></tr></tbody></table>

## MPD-100/200/300

<table><thead><tr><th colspan="2">Power Consumption</th></tr></thead><tbody><tr><td>Typical</td><td>105 W/110 W/115 W</td></tr><tr><td>Maximum</td><td>160 W</td></tr><tr><td>Voltage Range</td><td>100 to 240 VAC +/- 10%, 50/60 Hz</td></tr></tbody></table>

## MPP-100/200/300

<table><thead><tr><th colspan="2">Power Consumption</th></tr></thead><tbody><tr><td>Typical</td><td>90 W/95 W/100 W</td></tr><tr><td>Maximum</td><td>160 W</td></tr><tr><td>Voltage Range</td><td>100 to 240 VAC +/- 10%, 50/60 Hz</td></tr></tbody></table>

## AUX SDI Output Characteristics

| Output Level\*                                                                      |
| ----------------------------------------------------------------------------------- |
| 800 mV +/- 10% into 75 Ω Load                                                       |
| \* AUX SDI output can be used as SDI Loop through and ST2110-20/22/30/31 IP gateway |

## Weight and Packaging Dimensions

## MPS-100/200/300 Packaging Data

<table><thead><tr><th colspan="2">Dimensions</th></tr></thead><tbody><tr><td>Height</td><td>30.5 cm (12.0 in.)</td></tr><tr><td>Width</td><td>38.1 cm (15.0 in.)</td></tr><tr><td>Depth</td><td>27.9 cm (11.0 in.)</td></tr><tr><td>Weight</td><td>4.2 Kg (9.2 lbs)</td></tr></tbody></table>

## MPD-100/200/300 Packaging Data

<table><thead><tr><th colspan="2">Dimensions</th></tr></thead><tbody><tr><td>Height</td><td>30.5 cm (12.0 in.)</td></tr><tr><td>Width</td><td>61.0 cm (24.0 in.)</td></tr><tr><td>Depth</td><td>27.9 cm (11.0 in.)</td></tr><tr><td>Weight</td><td>6.0 Kg (13.2 lbs)</td></tr></tbody></table>

## MPP-100/200/300 Packaging Data

<table><thead><tr><th colspan="2">Dimensions</th></tr></thead><tbody><tr><td>Height</td><td>20cm (11.81in.)</td></tr><tr><td>Width</td><td>63.8cm (25.12in.)</td></tr><tr><td>Depth</td><td>47.2cm (18.58in.)</td></tr><tr><td>Weight</td><td>8.0Kg (17.64lbs.)</td></tr></tbody></table>

Subject to change

## Ordering Information - Options and Applications

## Base Model Selection

| Model   | Notes                                                                                                                                                                                                                               |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MPS-100 | PRISM, MPS-100; 3RU half rack, short depth, SDI Waveform Monitor base unit with integrated touchscreen                                                                                                                              |
| MPS-200 | PRISM, MPS-200; 3RU half rack, short depth, SDI and IP Waveform Monitor base unit with integrated touchscreen                                                                                                                       |
| MPS-300 | PRISM, MPS-300; 3RU half rack, short depth, SDI and IP Waveform Monitor with SDI EYE base unit with integrated touchscreen                                                                                                          |
| MPD-100 | PRISM, MPD-100; 3RU full rack, short depth, SDI Waveform Monitor base unit with dual integrated touchscreens                                                                                                                        |
| MPD-200 | PRISM, MPD-200; 3RU full rack, short depth, SDI and IP Waveform Monitor base unit with dual integrated touchscreens                                                                                                                 |
| MPD-300 | PRISM, MPD-300; 3RU full rack, short depth, SDI and IP Waveform Monitor with SDI EYE base unit with dual integrated touchscreens                                                                                                    |
| MPP-100 | PRISM, 1RU full rack; 4 SDI Inputs, SDI Waveform Monitor with SDI loop through outputs. External display required.                                                                                                                  |
| MPP-200 | 1RU full rack; 4 SDI inputs; 2 SFP+ for 10GE. 25GE support requires MP2 25GE license. SDI and IP Waveform Monitor with SDI loop through outputs and eight channel analog output. External display required.                         |
| MPP-300 | 1RU full rack; 4 SDI Inputs; 2 SFP+ for 10GE. 25GE support requires MP2 25GE license. SDI and IP Waveform Monitor with SDI EYE base unit. With SDI loop through outputs and eight channel analog output. External display required. |

## Application Summary

| Notes                                                        | Applications                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Standard Applications (All Models)                           | ![](https://www.telestream.net/video/images/specs/icon-waveform.png) ![](https://www.telestream.net/video/images/specs/icon-vector.png) ![](https://www.telestream.net/video/images/specs/icon-diamond.png) ![](https://www.telestream.net/video/images/specs/icon-lightning.png) ![](https://www.telestream.net/video/images/specs/icon-picture.png) ![](https://www.telestream.net/video/images/specs/icon-video-session.png) ![](https://www.telestream.net/video/images/specs/icon-event-log.png) ![](https://www.telestream.net/video/images/specs/icon-timing.png) ![](https://www.telestream.net/video/images/specs/icon-ext-ref.png) ![](https://www.telestream.net/video/images/specs/icon-ip-status.png) ![](https://www.telestream.net/video/images/specs/icon-audio.png) |
| Optional Applications (All Models)                           | ![](https://www.telestream.net/video/images/specs/icon-stop-display.png) ![](https://www.telestream.net/video/images/specs/icon-cie.png) ![](https://www.telestream.net/video/images/specs/icon-cam.png) ![](https://www.telestream.net/video/images/specs/icon-channel.png) ![](https://www.telestream.net/video/images/specs/icon-dolby-status.png) ![](https://www.telestream.net/video/images/specs/icon-datalist.png) ![](https://www.telestream.net/video/images/specs/icon-anc-session.png) ![](https://www.telestream.net/video/images/specs/icon-anc-session.png) ![](https://www.telestream.net/video/images/specs/icon-avdelay.png) ![](https://www.telestream.net/video/images/specs/icon-sdi-generator.png)                                                             |
| Optional Applications for MPS200/300, MPD200/300, MPP200/300 | ![](https://www.telestream.net/video/images/specs/icon-pit-histogram.png) ![](https://www.telestream.net/video/images/specs/icon-ip-session.png) ![](https://www.telestream.net/video/images/specs/icon-stream-timing.png) ![](https://www.telestream.net/video/images/specs/icon-ip-graphs.png) ![](https://www.telestream.net/video/images/specs/icon-ptp-graphs.png) ![](https://www.telestream.net/video/images/specs/IP-Disp-Gen-4.png)                                                                                                                                                                                                                                                                                                                                         |
| Physical Layer Applications. Standard on-MPS/MPD/MPP 300.    | ![](https://www.telestream.net/video/images/specs/icon-eye.png) ![](https://www.telestream.net/video/images/specs/icon-jitter.png)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

## Software Options

| PRISM Options | Description                                                                                                                                                                                                                                                                    | Applications Enabled                                                                                                                                                                                             |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AUD\*         | License; PRISM, MPS, MPD and MPP Models, Add Software license for enhanced Audio feature sets: includes Phase, Session, Correlation, Loudness Monitoring, AES Channel Status, and Dolby E or D metadata display                                                                | ![](https://www.telestream.net/video/images/specs/icon-audio.png) ![](https://www.telestream.net/video/images/specs/icon-dolby-status.png) ![](https://www.telestream.net/video/images/specs/icon-channel.png)   |
| SRND\*        | License; PRISM, MPS, MPD and MPP Models, Add software license for Audio Surround Sound Displays (Must have Option AUD installed)                                                                                                                                               |                                                                                                                                                                                                                  |
| DLBY\*        | License; PRISM, MPS, MPD and MPP Models, Add Software license for Dolby E and Dolby D decoding.                                                                                                                                                                                |                                                                                                                                                                                                                  |
| ENG-QC\*\*    | License; For PRISM, MPS, MPD and MPP Models add this software license to enable the Engineering and QC feature sets. These include: Datalist, Closed Captions (ARIB B-37, CEA608/CEA708) / Teletext decode (OP47/ST2031), ANC Session, AV Delay and EBU R103 Gamut monitoring. | ![](https://www.telestream.net/video/images/specs/icon-datalist.png) ![](https://www.telestream.net/video/images/specs/icon-anc-session.png) ![](https://www.telestream.net/video/images/specs/icon-avdelay.png) |
| GEN\*         | License; PRISM, MPS, MPD and MPP Models, Add Software license for SDI/IP signal generator; includes IP/SDI Generator application.                                                                                                                                              | ![](https://www.telestream.net/video/images/specs/icon-sdi-generator.png) ![](https://www.telestream.net/video/images/specs/IP-Disp-Gen-4.png)                                                                   |
| PROD\*        | License; PRISM, MPS, MPD and MPP Models, Add Software license for Production feature sets: includes Stop display, Light meter, HDR/WCG Conversion, Luma Qualified CIE chart                                                                                                    | ![](https://www.telestream.net/video/images/specs/icon-stop-display.png) ![](https://www.telestream.net/video/images/specs/icon-cie.png)                                                                         |
| MULTI\*       | License; PRISM, MPS, MPD and MPP Models, Add software license for multi-channel IP / SDI input and Camera Alignment Monitoring.                                                                                                                                                | ![](https://www.telestream.net/video/images/specs/icon-cam.png)                                                                                                                                                  |
| EXTNDSP\*     | License; PRISM, MPS and MPP Models, Add software license for enabling extended desktop.                                                                                                                                                                                        |                                                                                                                                                                                                                  |

\*Requires prefix of MPSDP- for ordering

## IP Measurement Options

| Option      | Description                                                                                                                                                        | Applications Enabled                                                                                                                                                                                                                                                                                                                                                    |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IP-MEAS\*   | Add Software license for IP Measurement feature sets: includes IP/PTP Graph, IP/PTP Session, PIT Histogram, Timing, Stream Timing and Stream capture applications. | ![](https://www.telestream.net/video/images/specs/icon-pit-histogram.png) ![](https://www.telestream.net/video/images/specs/icon-ip-session.png) ![](https://www.telestream.net/video/images/specs/icon-stream-timing.png) ![](https://www.telestream.net/video/images/specs/icon-ip-graphs.png) ![](https://www.telestream.net/video/images/specs/icon-ptp-graphs.png) |
| JPXS\* \*\* | Add Software License for ST2110-22 (JPEG XS) support on PRISM, MPS, MPD and MPP Models.                                                                            |                                                                                                                                                                                                                                                                                                                                                                         |

\* Requires prefix of MPSDP- for ordering

\*\* A combination of JPEG XS license and Multi License offers 4x JPEG XS decoding. A combination of JPEG XS license and GEN license offers JPEG XS Test signal generation.

## MPS/MPD/MPP-300 Physical Layer Measurement

| Option   | Description                                                                                                                                                                                                     | Applications Enabled                                                                                                               |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Standard | SDI Physical Layer Measurement Package (incl. automated measurement of 12G/6G/3G/HD/SDI Eye pattern parameters and jitter parameters; jitter waveform display). FMT-4K license required for 12G/6G-SDI support. | ![](https://www.telestream.net/video/images/specs/icon-eye.png) ![](https://www.telestream.net/video/images/specs/icon-jitter.png) |

## Format Support Options

| Option   | Description                                                                                                                  |
| -------- | ---------------------------------------------------------------------------------------------------------------------------- |
| FMT-4K\* | License; PRISM, MPS, MPD and MPP Models, Add Software license for 4K formats and enable 6G/12G SDI.                          |
| FMT-8K\* | License; PRISM, MPS, MPD and MPP Models, Add Software license for 8K formats in Quad 12G-SDI, including MPSDP-FMT-4K License |
| 25GE\*   | License; PRISM, MPS, MPD and MPP Models, Add Software license for 25GE support                                               |

\* Requires prefix of MPSDP- for ordering

## Racks Mount Kits and Accessories

## MPS-100/200/300 Options

| Option                                                                  | Description                                                                                                                                                                                            |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [MPS-PTBL](https://www.telestream.net/pdfs/datasheets/dat-mps-ptbl.pdf) | PRISM MPS model, Portable Accessory kit includes handle, feet, protective front cover, tripod mount bracket and bracket for battery mount plate (battery, battery mount plate and tripod not included) |
| [MPS-RACK](https://www.telestream.net/pdfs/datasheets/dat-mps-rack.pdf) | PRISM MPS model, Rack mounting kit with USB cables (not for use with MPD Models)                                                                                                                       |

### MPS-PTBL - Portable Accessory Kit (Instrument not incl.)

[![](https://www.telestream.net/video/images/specs/MPS-PTBL-1.png)](https://www.telestream.net/video/images/specs/MPS-PTBL-1.png)

[![](https://www.telestream.net/video/images/specs/MPS-PTBL-2.png)](https://www.telestream.net/video/images/specs/MPS-PTBL-2.png)

### MPS-RACK - Accessories for mounting a single MPS (Instrument not incl.)

[![](https://www.telestream.net/video/images/specs/MPS-RACK-1X-1.png)](https://www.telestream.net/video/images/specs/MPS-RACK-1X-1.png)

[![](https://www.telestream.net/video/images/specs/MPS-RACK-1X-2.png)](https://www.telestream.net/video/images/specs/MPS-RACK-1X-2.png)

### MPS-RACK - Accessories for mounting two MPS units (Instrument not incl.)

[![](https://www.telestream.net/video/images/specs/MPS-RACK-2X-1.png)](https://www.telestream.net/video/images/specs/MPS-RACK-2X-1.png)

[![](https://www.telestream.net/video/images/specs/MPS-RACK-2X-2.png)](https://www.telestream.net/video/images/specs/MPS-RACK-2X-2.png)

## MPD-100/200/300 Rack Options

| Option   | Description                                                                   |
| -------- | ----------------------------------------------------------------------------- |
| Standard | PRISM MPD model, Rack Mounting ears provided as standard with the instrument. |

## MPP-100/200/300 Rack Options

| Option   | Description                                                                   |
| -------- | ----------------------------------------------------------------------------- |
| Standard | PRISM MPP model, Rack Mounting ears provided as standard with the instrument. |

## Cable Options

## Cable Options

| Option           | Description                                                                                                                              |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| MP-CBL DUALDSP   | PRISM A cable kit for MPX2 DUALDSP, Two sets of 2 M DisplayPort male to DisplayPort male cable and 2 M USB 3.0 A male to B male cable    |
| MP-CBL HDBNC-BNC | PRISM Coaxial adapter cables from high density male BNC connector to standard female BNC connector (a set of 3 cables, 75 Ω, 0.5 M long) |

## Power Cord for MPS/MPD/MPP models

| Model           | Description                               |
| --------------- | ----------------------------------------- |
| PWR CORD NA S15 | North America Power Cord, Straight 15A    |
| PWR CORD NA R15 | North America Power Cord, Right Angle 15A |
| PWR CORD NA S20 | North America Power Cord, Straight 20A    |
| PWR CORD EURO   | Universal EURO Power Cord                 |
| PWR CORD CHN    | China Power Cord                          |
| PWR CORD IN     | India Power Cord                          |
| PWR CORD UK     | United Kingdom Power Cord                 |
| PWR CORD BRZ    | Brazil Power Cord                         |
| PWR CORD AUS    | Australia Power Cord                      |
| PWR CORD CHE    | Switzerland Power Cord                    |
| PWR CORD JPN    | Japan Power Cord                          |
| PWR CORD NONE   | No Power Cord or AC Adapter               |

## SFP Modules for IP Instruments

## MPS/MPD/MPP 200/300

| Option        | Description                                                                                       |
| ------------- | ------------------------------------------------------------------------------------------------- |
| MP-SFP 10GELR | A 10G Ethernet long range 1310 nm transceiver module for SFP+ C/D socket (MPI IP STD is required) |
| MP-SFP 10GESR | A 10G Ethernet short range 850 nm transceiver module for SFP+ C/D socket (MPI IP STD is required) |
| MP-SFP 25GELR | PRISM A 25G Ethernet long range 1310 nm transceiver module.                                       |
| MP-SFP 25GESR | PRISM A 25G Ethernet short range 850 nm transceiver module.                                       |

## Service, Support

## MPS Model Service Options

| Option      | Description                                                                                                                                                                                                                                                                                                      |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MPS R1-MS01 | Annual Warranty Extension. Covers parts, labor and 2-day shipping within country. Guarantees faster repair time than without coverage. All repairs include any required software updates. Hassle free with a single call that starts the process                                                                 |
| MPS R3      | Standard Warranty Extended to 3 Years. Covers parts, labor and 2-day shipping within country. Guarantees faster repair time than without coverage. All repairs include any required software updates. Hassle free with a single call that starts the process. Can only be purchased at time of product purchase. |
| MPS R5      | Standard Warranty Extended to 5 Years. Covers parts, labor and 2-day shipping within country. Guarantees faster repair time than without coverage. All repairs include any required software updates. Hassle free with a single call that starts the process. Can only be purchased at time of product purchase. |

## MPD Model Service Options

| Option      | Description                                                                                                                                                                                                                                                                                                      |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MPD R1-MS01 | Annual Warranty Extension. Covers parts, labor and 2-day shipping within country. Guarantees faster repair time than without coverage. All repairs include any required software updates. Hassle free with a single call that starts the process.                                                                |
| MPD R3      | Standard Warranty Extended to 3 Years. Covers parts, labor and 2-day shipping within country. Guarantees faster repair time than without coverage. All repairs include any required software updates. Hassle free with a single call that starts the process. Can only be purchased at time of product purchase. |
| MPD R5      | Standard Warranty Extended to 5 Years. Covers parts, labor and 2-day shipping within country. Guarantees faster repair time than without coverage. All repairs include any required software updates. Hassle free with a single call that starts the process. Can only be purchased at time of product purchase. |

## MPP Model Service Options

| Option      | Description                                                                                                                                                                                                                                                                                                      |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MPP R1-MS01 | Annual Warranty Extension. Covers parts, labor and 2-day shipping within country. Guarantees faster repair time than without coverage. All repairs include any required software updates. Hassle free with a single call that starts the process.                                                                |
| MPP R3      | Standard Warranty Extended to 3 Years. Covers parts, labor and 2-day shipping within country. Guarantees faster repair time than without coverage. All repairs include any required software updates. Hassle free with a single call that starts the process. Can only be purchased at time of product purchase. |
| MPP R5      | Standard Warranty Extended to 5 Years. Covers parts, labor and 2-day shipping within country. Guarantees faster repair time than without coverage. All repairs include any required software updates. Hassle free with a single call that starts the process. Can only be purchased at time of product purchase. |
