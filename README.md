# StableDiffusion_DiscordBot

![](https://user-images.githubusercontent.com/101509164/221388737-5efbf8dc-d59a-4ab4-8770-863f96dc6f17.jpg)

텍스트로 이미지를 생성할 수 있다고 알려진 Stable Diffusion 모델을 디스코드 봇으로 사용할 수 있습니다. </br>
원본 모델은 [CompVis](https://github.com/CompVis/stable-diffusion)이며 경량화된 모델은 [여기](https://github.com/basujindal/stable-diffusion)에서 사용할 수 있습니다. 그래픽카드 VRAM이 4GB 미만이라면 경량화 모델을 사용하세요. </br>

## 필수
- VRAM이 최소 4GB 이상이 되는 그래픽 카드
- anaconda3 가상환경
- 자기 소유의 디스코드 봇 

사용하기 위해서는 먼저 [HuggingFace](https://huggingface.co/CompVis/stable-diffusion-v-1-4-original)(로그인 필수)에서 sd-v1-4.ckpt(4GB) 모델 파일을 받아야 합니다.
