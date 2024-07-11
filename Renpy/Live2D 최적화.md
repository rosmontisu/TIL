
#### 상황
- 개발 환경 : Renpy
- 고려해야될 점 
	- 윈도우 환경에서 Live2D를 적용할 예정
		- 윈도우 환경일경우 steam sdk 가 필요할수도
	- 기획상 안드로이드로 포팅이 필요한 상황
	
#### 최적화 방안
1. Live2D 모델의 복잡도(메시) 감소:
   - 예시: 캐릭터의 머리카락을 100개의 개별 메시 대신 10개의 큰 메시로 단순화합니다.
   - 효과: 렌더링 부하 감소, 메모리 사용량 감소

2. 텍스처 최적화:
   - 예시: 4096x4096 해상도의 텍스처를 2048x2048로 줄입니다.
   - 효과: 메모리 사용량 감소, 로딩 시간 단축

3. FPS 조정:
   - 예시: 60fps 애니메이션을 30fps로 조정합니다.
   - 효과: CPU 사용량 감소, 배터리 소모 감소

4. LOD (Level of Detail) 시스템 구현:
   - 예시:
   ```python
   if renpy.android:
       if renpy.get_renderer_info()['renderer'] == 'gl':
           # 고사양 기기용 고품질 모델
           renpy.show("character_hd")
       else:
           # 저사양 기기용 저품질 모델
           renpy.show("character_ld")
   ```
   - 효과: 기기 성능에 따라 적절한 품질의 모델 사용

5. 동적 리소스 로딩:
   - 예시:
   ```python
   def load_live2d_model(model_name):
       if model_name not in loaded_models:
           renpy.load_live2d(model_name)
           loaded_models.append(model_name)
   
   # 필요할 때만 모델 로드
   $ load_live2d_model("character1")
   show character1 live2d
	# Renpy 문법
	# $ ... 
	# $ 원하는 파이썬 코드 실행 가능
	# ex) $ answer = a + b
   ```
   - 효과: 메모리 사용 최적화, 초기 로딩 시간 감소

6. 캐싱 활용:
   - 예시: RenPy의 `im.Cache` 활용
   ```python
   image character_cached = im.Cache(LiveComposite(
       (300, 400),
       (0, 0), "character_base.png",
       (50, 50), "character_eyes.png"
   ))
   ```
   - 효과: 반복적인 렌더링 연산 감소

7. 불필요한 애니메이션 제거:
   - 예시: 대화 중 캐릭터가 화면에 없을 때는 애니메이션을 일시 중지합니다.
   ```python
   if character_speaking:
       renpy.show("character live2d")
   else:
       renpy.show("character live2d", pause=True)
   ```
   - 효과: CPU 사용량 감소, 배터리 소모 감소
    
8. 애셋 압축(단, 속도 최적화 X):
   - 예시: Live2D 모델 파일을 ZIP으로 압축하여 저장하고 실행 시 압축 해제
   - 효과: 앱 크기 감소, 다운로드 시간 단축

9. 백그라운드 프리로딩:
   - 예시:
   ```python
   init python:
       def preload_next_scene():
           renpy.start_predict("next_scene_bg")
           renpy.start_predict("next_character live2d")
   
   label scene1:
       # 현재 씬 코드
       $ preload_next_scene()  # 다음 씬 리소스 미리 로드
   ```
   - 효과: 씬 전환 시 로딩 시간 감소

10. 하드웨어 가속 활용:
    - 예시: RenPy 설정에서 하드웨어 가속 옵션 활성화
    ```python
    init python:
        config.gl_enable = True
    ```
    - 효과: GPU를 활용한 렌더링 성능 향상