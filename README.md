# StableDiffusion_DiscordBot

![](https://user-images.githubusercontent.com/101509164/221388737-5efbf8dc-d59a-4ab4-8770-863f96dc6f17.jpg)

텍스트로 이미지를 생성할 수 있다고 알려진 Stable Diffusion 모델을 디스코드 봇으로 사용할 수 있습니다. </br>
원본 모델은 [CompVis](https://github.com/CompVis/stable-diffusion)이며 경량화된 모델은 [여기](https://github.com/basujindal/stable-diffusion)에서 사용할 수 있습니다. </br>
그래픽카드 VRAM이 4GB 미만이라면 경량화 모델을 사용하세요. </br> </br>
[디스코드 주소](discord.gg/vSQMkCNZc2)

## 필수
- 윈도우 (MacOS 안됨)
- VRAM이 최소 4GB 이상이 되는 그래픽 카드
- anaconda3 가상환경
---

## 모델 다운로드
사용하기 위해서는 먼저 [HuggingFace](https://huggingface.co/CompVis/stable-diffusion-v-1-4-original)(로그인 필수)에서 sd-v1-4.ckpt(4GB) 모델 파일을 받아야 합니다. </br>
모델을 다운로드 받았다면 이름을 **model.ckpt**로 변경한 뒤 **/models/ldm/stable-diffusion-v1** 폴더 안에 넣으세요. </br>

## 아나콘다 세팅
cmd 창을 키고 **cd C:\뭐시기뭐시기\StableDIffusion_DiscordBot** 로 폴더를 옮겨주신 뒤 아나콘다를 실행하고 </br>
**conda env create -f environment.yaml**을 입력해 가상환경을 만들어 주세요. 생성된 가상환경의 이름은 ldm </br>
파이썬 버전이 **3.8.5**가 아니라면 정상적인 작동이 되지 않습니다. </br>

## 사용
[디스코드 개발자 어플리케이션](https://discord.com/developers/applications/)에 들어가 **New Application**을 선택하고 이름을 지어 앱을 만들어줍니다. </br> </br>
![](https://user-images.githubusercontent.com/101509164/221389149-a3b5c7d7-d00e-4456-a39e-661b64f6a912.png) </br>
![](https://user-images.githubusercontent.com/101509164/221389164-a85747c1-bb1b-4bb7-aa12-900fa5a35769.png)
다음으로 좌측의 Bot 카테고리에 들어가 Add Bot을 선택해주고 위와 같이 봇 설정들을 체크해 줍니다. </br> </br> </br>

![](https://user-images.githubusercontent.com/101509164/221389284-af0b30c9-2025-4a1c-ba9a-2f782fec9642.png)
설정을 끝내고 봇 아래의 **View Token**이나 **Reset Token**으로 봇 토큰을 복사한 뒤 DiscordBot.py에 사용할 봇의 토큰을 복붙해주세요. </br>
좌측 **OAuth2**의 **URL Generator**에 들어가 **bot**을 선택해 준 뒤 아까와 같이 선택하고 링크를 인터넷 창에 복붙해 서버에 봇을 초대해주세요. </br>

![](https://user-images.githubusercontent.com/101509164/221389436-c59b4a03-7323-4e89-ab7f-5d58e803af4b.png)
그리고 DiscordBot.py의 **save_path**에 사진 저장 경로를 지정해준 뒤 **디스코드 설정->고급->개발자 모드**를 켜 주시고 서버 채팅 채널을 우클릭하면 </br> 
**ID 복사하기**가 있는데 복사한 뒤 **get_channel()** 안의 작은따옴표를 제거하고 복붙해주시면 됩니다. </br> </br> </br>

마지막으로 VSCode나 PyCharm등의 IDEA를 이용해 DiscordBot.py를 실행한 뒤 터미널에 **python DiscordBot.py**를 입력해주시면 작동이 됩니다.

- 만들어지는 사진의 크기는 **512 x 512** (사양에 따라 더 높일 수 있음)
- 사진의 퀄리티를 높이고 싶다면 더 자세한 키워드 삽입
- 최대 대기열은 10개까지
- 이미지 만들기 : !makeimg "대충 문장 형식의 키워드"
- ex) !makeimg "An astronaut riding a horse on Mars"
