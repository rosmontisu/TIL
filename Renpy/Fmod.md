#### FMOD STUDIO
- FL Studio 와 유사한 GUI를 가진 사운드 툴
- **확장자** : .fspro / .bank 로 빌드 
#### FMOD Engine
- fmod core api 를 외부 엔진관 결합시키는데 사용
- [Core API Guide](https://www.fmod.com/docs/2.03/api/core-guide.html)


## fmod.dll
##### 1. **플랫폼에 맞는 DLL 파일 사용**

- **Windows**: FMOD은 Windows에서 `fmod.dll` 파일을 제공합니다. 만약 64비트 버전의 Ren'Py를 사용하고 있다면, 64비트용 FMOD DLL (`fmod64.dll`)을 사용해야 합니다. 반대로 32비트용 Ren'Py를 사용하고 있다면, 32비트용 FMOD DLL (`fmod.dll`)을 사용해야 합니다.
- **macOS 또는 Linux**: 이 경우, 해당 운영 체제에 맞는 `.dylib` 또는 `.so` 파일을 사용해야 합니다.

##### 2. **FMOD 버전**

- FMOD DLL은 특정 버전의 FMOD에 맞게 제공됩니다. FMOD Studio에서 빌드한 프로젝트와 동일한 버전의 FMOD DLL을 사용해야 합니다. 예를 들어, FMOD Studio 2.02 버전을 사용하여 프로젝트를 빌드했다면, `fmod.dll` 파일도 2.02 버전이어야 합니다.

##### 3. **FMOD Core API에 포함된 DLL 파일 사용**

- **FMOD Core API** 패키지를 다운로드하면, 해당 패키지에 포함된 `fmod.dll` 파일을 사용할 수 있습니다. 이 파일은 FMOD의 모든 기능을 포함하고 있으므로, 이 파일을 사용하는 것이 좋습니다.

## .bank 접근 가능 범주
```rpy
    # .bank 파일 로드
    $ load_bank("game/fSound/banks/Master.bank")
    $ load_bank("game/fSound/banks/Master.strings.bank")
```