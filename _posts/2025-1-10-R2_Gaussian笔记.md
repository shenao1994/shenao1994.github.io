---
layout:     post
title:      R2-Gaussian note
subtitle:   R2G note
date:       2025-1-10
author:     SA
header-img: img/r2gs_covert.png
catalog: true
tags:
    - 3D Gaussian
---

## Foreword

At present, the R2-Gaussian related code has been released, recording some precautions for R2-Gaussian

![cover](https://s1.imagehub.cc/images/2024/10/30/9f9774a715237602f2a59c200d517dc5.png)

![demo](https://s1.imagehub.cc/images/2024/10/30/0abd6398dd0b18f8c9f716d64b4e960d.gif)



## 1. 2-Views Reconstruction

In dataset_readers.py line 281 and 278 modify the code 

```sh

angles = np.sort(np.random.rand(50) * 360 / 180 * np.pi) + data["startAngle"] / 180 * np.pi
# angles = data_split["angles"]
        
# for i_split in range(n_split):  # default
for i_split in [0, 25]:  # 2 views

```



### Reference

- [R2_Gausssian](https://github.com/Ruyi-Zha/r2_gaussian)
 

