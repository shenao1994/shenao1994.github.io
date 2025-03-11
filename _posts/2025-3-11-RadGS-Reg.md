---
layout:     post
title:      RadGS-Reg Project
subtitle:   RadGS-Reg 
date:       2025-3-11
author:     SA
header-img: img/xgs.png
catalog: true
tags:
    - 3DGS
---

# RadGS-Reg: Registering Spine CT with Biplanar X-rays via Joint 3D Radiative Gaussians Reconstruction and 3D/3D Registration

**First Author**\*, **Second Author**\*, Third Author

Institution Name
Conferance name and year
<sup>\*</sup>Indicates Equal Contribution

[Paper](https://arxiv.org/pdf/<ARXIV PAPER ID>.pdf) [Supplementary](static/pdfs/supplementary_material.pdf) [Code](https://github.com/YOUR REPO HERE) [arXiv](https://arxiv.org/abs/<ARXIV PAPER ID>)

## Abstract
Computed Tomography (CT)/X-ray registration in image-guided navigation remains challenging because of its stringent requirements for high accuracy and real-time performance. Traditional "render and compare" methods, relying on iterative projection and comparison, suffer from spatial information loss and domain gap. 3D reconstruction from biplanar X-rays supplements spatial and shape information for 2D/3D registration, but current methods are limited by dense-view requirements and struggles with noisy X-rays. To address these limitations, we introduce RadGS-Reg, a novel framework for vertebral-level CT/X-ray registration through joint 3D Radiative Gaussians (RadGS) reconstruction and 3D/3D registration. Specifically, our biplanar X-rays vertebral RadGS reconstruction module explores learning-based RadGS reconstruction method with a Counterfactual Attention Learning (CAL) mechanism, focusing on vertebral regions in noisy X-rays. Additionally, a patient-specific pre-training strategy progressively adapts the RadGS-Reg from simulated to real data while simultaneously learning vertebral shape prior knowledge. Experiments on in-house datasets demonstrate the state-of-the-art performance for both tasks, surpassing existing methods.

<div style="text-align: center;">
  <h1>Pipeline</h1>
  <img src="https://s1.imagehub.cc/images/2025/03/11/06dd85a04104a1797cf41d8126edb421.jpg" alt="Pipeline 图片" style="max-width: 100%;">
</div>

## Qualitative Results
<div style="text-align: center;">
  <h1>Reconstruction Results</h1>
  <img src="https://s1.imagehub.cc/images/2025/03/11/c2a55a0939ac16c6b348656463cbf5a9.jpg" alt="Pipeline 图片" style="max-width: 100%;">
</div>

<div style="text-align: center;">
  <h1>Registration Results</h1>
  <img src="https://s1.imagehub.cc/images/2025/03/11/64e7028f99dae04b3f8204c1a5eafe2c.jpg" alt="Pipeline 图片" style="max-width: 100%;">
</div>

## Video Presentation

<div id="results-carousel" class="carousel results-carousel">
  <div class="item item-video1">
    <video poster="" id="video1" autoplay controls muted loop height="100%">
      <source src="https://www.youtube.com/embed/n7KnpsTE-O8?si=UhjR7MNlQlNDETeq" type="video/mp4">
    </video>
  </div>
  <div class="item item-video2">
    <video poster="" id="video2" autoplay controls muted loop height="100%">
      <source src="https://www.youtube.com/embed/FSR02_ahQvI?si=7CUUmhc6YMrVWbAm" type="video/mp4">
    </video>
  </div>
</div>

## BibTeX