---
layout:     post
title:      X-Gaussian note
subtitle:   XG note
date:       2025-1-11
author:     SA
header-img: img/xgs.png
catalog: true
tags:
    - 3D Gaussian
---

## Foreword

At present, the X-Gaussian related code has been released, recording some precautions for X-Gaussian

## 1. Train rendering command


```sh

python .\train.py --config .\config\vert.yaml --eval

```
2-Views Training modify the dataset_readers.py line 447

```
ap_la_indices = [0, 24]
scene_info = SceneInfo(point_cloud=pcd,
                       # train_cameras=train_cam_infos[:train_num],
                       train_cameras=[train_cam_infos[i] for i in ap_la_indices],
                       test_cameras=test_cam_infos,
                       add_cameras=add_cam_infos,
                       nerf_normalization=nerf_normalization,
                       ply_path=ply_path)
```

### Reference

- [X_Gausssian](https://github.com/caiyuanhao1998/X-Gaussian)
 

