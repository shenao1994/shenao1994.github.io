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

## Teaser

<video poster="" id="tree" autoplay controls muted loop height="100%">
  <source src="static/videos/banner_video.mp4" type="video/mp4">
</video>

Aliquam vitae elit ullamcorper tellus egestas pellentesque. Ut lacus tellus, maximus vel lectus at, placerat pretium mi. Maecenas dignissim tincidunt vestibulum. Sed consequat hendrerit nisl ut maximus.

## Abstract

Computed Tomography (CT)/X-ray registration in image-guided navigation remains challenging because of its stringent requirements for high accuracy and real-time performance. Traditional "render and compare" methods, relying on iterative projection and comparison, suffer from spatial information loss and domain gap. 3D reconstruction from biplanar X-rays supplements spatial and shape information for 2D/3D registration, but current methods are limited by dense-view requirements and struggles with noisy X-rays. To address these limitations, we introduce RadGS-Reg, a novel framework for vertebral-level CT/X-ray registration through joint 3D Radiative Gaussians (RadGS) reconstruction and 3D/3D registration. Specifically, our biplanar X-rays vertebral RadGS reconstruction module explores learning-based RadGS reconstruction method with a Counterfactual Attention Learning (CAL) mechanism, focusing on vertebral regions in noisy X-rays. Additionally, a patient-specific pre-training strategy progressively adapts the RadGS-Reg from simulated to real data while simultaneously learning vertebral shape prior knowledge. Experiments on in-house datasets demonstrate the state-of-the-art performance for both tasks, surpassing existing methods.
## Image Carousel

<div id="results-carousel" class="carousel results-carousel">
  <div class="item">
    <img src="img/miccai25/pipeline.jpg" alt="MY ALT TEXT"/>
    <h2 class="subtitle has-text-centered">First image description.</h2>
  </div>

[//]: # (  <div class="item">)

[//]: # (    <img src="static/images/carousel2.jpg" alt="MY ALT TEXT"/>)

[//]: # (    <h2 class="subtitle has-text-centered">Second image description.</h2>)

[//]: # (  </div>)

[//]: # (  <div class="item">)

[//]: # (    <img src="static/images/carousel3.jpg" alt="MY ALT TEXT"/>)

[//]: # (    <h2 class="subtitle has-text-centered">Third image description.</h2>)

[//]: # (  </div>)

[//]: # (  <div class="item">)

[//]: # (    <img src="static/images/carousel4.jpg" alt="MY ALT TEXT"/>)

[//]: # (    <h2 class="subtitle has-text-centered">Fourth image description.</h2>)

[//]: # (  </div>)
</div>

## Video Presentation

<div class="publication-video">
  <iframe src="https://www.youtube.com/embed/JkaxUblCGz0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</div>

## Another Carousel (Video)

<div id="results-carousel" class="carousel results-carousel">
  <div class="item item-video1">
    <video poster="" id="video1" autoplay controls muted loop height="100%">
      <source src="static/videos/carousel1.mp4" type="video/mp4">
    </video>
  </div>
  <div class="item item-video2">
    <video poster="" id="video2" autoplay controls muted loop height="100%">
      <source src="static/videos/carousel2.mp4" type="video/mp4">
    </video>
  </div>
  <div class="item item-video3">
    <video poster="" id="video3" autoplay controls muted loop height="100%">
      <source src="static/videos/carousel3.mp4" type="video/mp4">
    </video>
  </div>
</div>

[//]: # (## Poster)
[//]: # (<iframe src="static/pdfs/sample.pdf" width="100%" height="550"></iframe>)

## BibTeX