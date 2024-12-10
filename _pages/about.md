---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am currently pursuing an M.S. in Computer Science at ShanghaiTech University under the guidance of Prof. [Qian Wang (王乾)](https://qianwang.space/). I also completed my Bachelor’s degree in Computer Science at ShanghaiTech University. I have published serveral papers about medical image and computer vision with total <a href='https://scholar.google.com/citations?user=UR1eH9cAAAAJ'><img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2FAbsterZhu%2FAbsterZhu.github.io@google-scholar-stats%2Fgs_data_shieldsio.json&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>.

My research is driven by the goal of advancing multimodal healthcare in the foundation model era. Below are my key areas of interest:
- Application of pre-trained models in medical imaging scenarios.
- Deep Learning Multimodal Research in Images, Text, and 3D.
- 3D human body reconstruction and 3D interaction between humans and objects.


# 🔥 News
- *2024.12*: &nbsp;🎉🎉 One paper accepted by AAAI 2025. 
- *2024.05*: &nbsp;🎉🎉 One paper accepted by IEEE TMI. 
- *2024.02*: &nbsp;🎉🎉 Two papers accepted by ISBI 2024. 

# 📖 Educations
<div style="display: flex; align-items:center; padding-top: 10px">
    <img style="margin-right: 30px" src="images/上科大校徽.png" alt="image" width="90" height="90">
    <p style="margin:0; flex: 1;">
        <font size="4"><b>ShanghaiTech University, Shanghai, China</b></font><br>
        <font size="3">Sept. 2022 - Present</font><br>
        <font size="3"><i>M.S.</i> in Computer Science</font><br>
        <font size="3">Supervisor: Prof. <a href="https://qianwang.space/">Qian Wang</a></font>
    </p>
</div>

<div style="display: flex; align-items:center; padding-top: 10px">
    <img style="margin-right: 30px" src="images/上科大校徽.png" alt="image" width="90" height="90">
    <p style="margin:0; flex: 1;">
        <font size="4"><b>ShanghaiTech University, Shanghai, China</b></font><br>
        <font size="3">Sept. 2018 - 2022</font><br>
        <font size="3"><i>B.E.</i> in Computer Science</font><br>
    </p>
</div>

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv</div><img src='images/mitracker_new.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MITracker: Multi-View Integration for Visual Object Tracking]()

Mengjie Xu\*, **Yitao Zhu\***, Haotian Jiang, Jiaming Li, Zhenrong Shen, Sheng Wang, Haolin Huang, Xinyu Wang, Han Zhang, Qing Yang, Qian Wang<sup>+</sup><br>

- Introduces MVTrack, a large-scale dataset with 234K frames and precise annotations for 27 object categories, providing a benchmark for class-agnostic multi-view object tracking.
- Proposes MITracker, a method leveraging BEV-guided 3D feature volumes and spatial-enhanced attention for robust target recovery in multi-view tracking.
- Demonstrates that MITracker achieves state-of-the-art performance, improving recovery rates from 56.7% to 79.2% on MVTrack and GMTD datasets.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2025</div><img src='images/muc_pipeline_new.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MUC: Mixture of Uncalibrated Cameras for Robust 3D Human Body Reconstruction](https://arxiv.org/pdf/2403.05055v1.pdf)

**Yitao Zhu\***, Sheng Wang*, Mengjie Xu, Zixu Zhuang, Zhixin Wang, Kaidong Wang, Han Zhang, Qian Wang<sup>+</sup><br>

- Introduces a technique for accurately reconstructing 3D human poses and shapes from images captured by uncalibrated cameras.
- Utilizes pre-trained monocular models to estimate camera positions and employs a distance ranking optimization strategy for precise joint fusion, addressing self-occlusion issues.
- Deploys a model to reweight human surface for accurate body shape estimation.outputs.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE TMI</div><img src='images/chatcad+_new.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Chatcad+: Towards a Universal and Reliable Interactive CAD using LLMs](https://arxiv.org/pdf/2305.15964)

Zihao Zhao\*, Sheng Wang\*, Jinchen Gu\*, **Yitao Zhu\***, Lanzhuju Mei, Zixu Zhuang, Zhiming Cui, Qian Wang, Dinggang Shen<sup>+</sup><br>

[**Project**](https://github.com/zhaozh10/ChatCAD) <strong><span class='show_paper_citations' data='UR1eH9cAAAAJ:u-x6o8ySG0sC'></span></strong> | <img src="https://img.shields.io/github/stars/zhaozh10/ChatCAD?style=social&amp;label=Stars">
- Integrates medical imaging and a professional knowledge base to enhance the reliability of Large Language Models in healthcare.
- Trains CLIP models on various medical imaging modalities for disease classification and designs an efficient mechanism to retrieve relevant medical expertise based on user statements.
- Uses the retrieved information to provide references, improving the trustworthiness of LLM outputs.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ISBI 2024 (oral)</div><img src='images/melo_new.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Melo: Low-rank Adaptation is Better than Fine-tuning for Medical Image Diagnosis](https://arxiv.org/pdf/2311.08236.pdf)

**Yitao Zhu**, Zhenrong Shen, Zihao Zhao, Sheng Wang, Xin Wang, Xiangyu Zhao, Dinggang Shen, Qian Wang<sup>+</sup><br>

[**Project**](https://github.com/JamesQFreeman/LoRA-ViT) <strong><span class='show_paper_citations' data='UR1eH9cAAAAJ:d1gkVwhDpl0C'></span></strong> | <img src="https://img.shields.io/github/stars/JamesQFreeman/LoRA-ViT?style=social&amp;label=Stars">
- Transfers natural image pre-trained models to medical image diagnostic tasks using just 0.17% trainable parameters, achieving performance comparable to full model fine-tuning across various medical imaging modalities.
- Provides rapid task-switching capabilities and reduced memory usage in clinical deployment scenarios.outputs.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv</div><img src='images/doctorglm_new.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Doctorglm: Fine-tuning Your Chinese Doctor is not a Herculean Task](https://arxiv.org/pdf/2304.01097.pdf)

Honglin Xiong\*, Sheng Wang\*, **Yitao Zhu\***, Zihao Zhao\*, Yuxiao Liu, Linlin Huang, Qian Wang, Dinggang Sheng<sup>+</sup><br>

[**Project**](https://github.com/xionghonglin/DoctorGLM) <strong><span class='show_paper_citations' data='UR1eH9cAAAAJ:u5HHmVD_uO8C'></span></strong> | <img src="https://img.shields.io/github/stars/xionghonglin/DoctorGLM?style=social&amp;label=Stars">
- Developed the first Chinese medical dialogue model in China using a subset of Chinese medical dialogues, supplemented with translated high-quality English medical data and Q&A responses generated from Chinese medical textbooks.
- Employed advanced fine-tuning techniques like LoRA and p-tuning to optimize training strategies, supported by an active open-source community and enriched by over 40,000 pieces of user feedback.outputs.
</div>
</div>

- [Inter-slice Super-resolution of Magnetic Resonance Images by Pre-training and Self-supervised Fine-tuning](https://arxiv.org/pdf/2406.05974), Xin Wang\*, Zhiyun Song\*, **Yitao Zhu**, Sheng Wang, Lichi Zhang, Dinggang Shen, Qian Wang, **ISBI 2024**

# 🎖 Honors and Awards
- *2019.10*, Outstanding individual in social practice of ShanghaiTech University. 
- *2020.09*, Yangtze River Delta Financial Big Data Application Ability Competition, First Prize.
- *2022.11*, Academic Scholarships, ShanghaiTech University.
- *2023.11*, Academic Scholarships, ShanghaiTech University.
- *2024.11*, Academic Scholarships, ShanghaiTech University.

# 💻 Teaching Assistant
- *2023.3 - 2023.7*, BME2106 Medical Big-Data and Artificial Intelligence, ShanghaiTech University.

# 🌍 Visitors
<div style="display:inline-block;width:300px;"><script type='text/javascript' id='clustrmaps' src='//cdn.clustrmaps.com/map_v2.js?cl=ffffff&w=a&t=tt&d=ZKonaVTdvqlX8gAHyqzcU1QgAN38-pUmfvVAl0xBuaw'></script></div>