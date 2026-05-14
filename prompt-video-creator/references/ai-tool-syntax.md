# AI Video Tool Syntax Reference

Cú pháp đặc thù và best practice cho từng công cụ AI video.

## Table of Contents
1. [Veo 3 (Google)](#1-veo-3-google)
2. [Sora (OpenAI)](#2-sora-openai)
3. [Runway Gen-3 / Gen-4](#3-runway-gen-3-gen-4)
4. [Kling 2.0](#4-kling-2-0)
5. [Luma Dream Machine / Ray2](#5-luma-dream-machine-ray2)
6. [Pika 2.0](#6-pika-2-0)
7. [Hailuo / MiniMax](#7-hailuo-minimax)
8. [Hunyuan / Wan 2.1](#8-hunyuan-wan-2-1)

---

## 1. Veo 3 (Google)

### Đặc điểm độc đáo
- **Audio sync hoàn hảo**: Tự sinh dialogue, ambient, music, SFX khớp môi
- **Cinematic chất lượng cao** nhất hiện tại
- **8 giây/clip**, có thể nối nhiều clip
- **Xử lý phức tạp**: Nhiều subject, scene change

### Cấu trúc prompt Veo 3 chuẩn

```
[Shot type] of [subject] [action] in [setting].
[Camera movement and angle].
[Lighting and atmosphere].
[Color grading and mood].
[Visual style reference].
Audio: [ambient sounds]. [Dialogue with quotes]. [Music description].
```

### Ví dụ Veo 3 với Audio
```
Medium close-up of a young Vietnamese chef in a steamy bowl of pho restaurant kitchen, 
focused intensity as he ladles broth into a steaming bowl. 
Slow dolly in pushing toward his face revealing a satisfied smile.
Warm practical kitchen lighting with steam catching golden tones.
Cinematic warm color grade with rich oranges and browns.
In the style of food documentary cinematography.

Audio: Bubbling broth, knife on cutting board, sizzling. 
Chef whispers in Vietnamese: "Hoàn hảo." 
Subtle traditional Vietnamese music with đàn tranh.
```

### Best practices Veo 3
✅ Dialogue trong dấu ngoặc kép
✅ Mô tả chi tiết audio environment
✅ Genre nhạc cụ thể (jazz, lo-fi, orchestral)
✅ SFX riêng biệt
❌ Không quá nhiều scene change trong 8s
❌ Tránh dialogue quá dài (5-8 từ thường tốt nhất)

---

## 2. Sora (OpenAI)

### Đặc điểm
- **Dài lên đến 60 giây** (longest among consumer)
- **Scene change trong 1 prompt**: Có thể mô tả nhiều cảnh
- **Storyboard mode**: Multiple scenes với timing
- **Aspect ratio đa dạng**: 16:9, 9:16, 1:1, custom

### Cấu trúc Sora
```
[Detailed scene description with multiple beats if needed].
[Camera work throughout the sequence].
[Visual style and atmosphere].
[Specific timing if multi-scene: "Then transitions to..."]
```

### Ví dụ Sora narrative
```
A young woman walks through a misty Tokyo street at night, 
her red coat vivid against the wet pavement reflecting neon signs. 
The camera tracks beside her at eye-level, then slowly cranes up 
to reveal the towering cyberpunk cityscape stretching to the horizon.
Anamorphic 35mm cinematic lens, atmospheric blue-magenta color grade
with selective neon highlights, in the style of Blade Runner 2049 cinematography.
24fps cinematic, dreamlike rainy ambiance.
```

### Storyboard mode
```
Scene 1 (0-3s): Close-up of a coffee bean falling into water in slow motion.
Scene 2 (3-6s): Pull back to reveal a barista crafting latte art.
Scene 3 (6-10s): Wide shot of busy coffee shop atmosphere.
Consistent warm color grade throughout, gentle jazz music ambiance.
```

### Best practices Sora
✅ Mô tả cảnh dài chi tiết
✅ Nói rõ camera transitions
✅ Sora hiểu được "scene 1, scene 2"
❌ Vẫn yếu với text trong video
❌ Phức tạp với nhiều nhân vật tương tác

---

## 3. Runway Gen-3 / Gen-4

### Đặc điểm
- **Motion brush**: Vẽ vùng cần chuyển động
- **Camera control**: Specific direction (pan/tilt/zoom)
- **Image-to-video** mạnh nhất
- **10 giây/clip**
- **Stylization control**: Strength slider

### Cấu trúc Runway
```
[Shot type] of [subject] [action] in [setting].
[Specific camera movement: "Camera tilts up slowly"].
[Style reference and quality descriptors].
```

### Camera direction phrases (Runway hiểu rõ)
- "Camera tilts up/down"
- "Camera pans left/right"
- "Camera dollies in/out"
- "Camera tracks left/right"
- "Camera orbits subject"
- "Static locked-off camera"
- "Handheld natural camera shake"

### Ví dụ Runway
```
Cinematic medium shot of a wolf running through snowy forest at dusk.
Camera tracks alongside the wolf at eye-level following the motion.
Cool blue color grade with selective warm highlights from setting sun.
Anamorphic cinematic style with shallow depth of field,
realistic motion at 24fps cinematic.
```

### Motion brush usage (text description)
```
[For image-to-video] Static medium shot. 
Subject's hair gently moves in wind, 
fabric of dress flutters slightly,
background trees sway softly,
otherwise camera is locked-off.
```

---

## 4. Kling 2.0

### Đặc điểm
- **Prompt adherence cực tốt** (theo prompt sát nhất hiện tại)
- **Motion realistic** đặc biệt chuyển động người
- **Negative prompt** quan trọng
- **5-10s clip** standard
- **Camera control parameters**

### Cấu trúc Kling
```
Positive prompt: [Detailed scene with camera and style]
Negative prompt: [Things to avoid]
```

### Camera params (Kling specific)
- **Horizontal**: Pan left/right
- **Vertical**: Tilt up/down  
- **Pull/Push**: Dolly in/out
- **Zoom**: Optical zoom
- **Tilt**: Dutch angle

### Ví dụ Kling
```
Positive: Cinematic medium close-up of an elderly Vietnamese woman 
weaving traditional silk on a wooden loom, focused expression with 
weathered hands moving rhythmically. Warm golden hour light streaming 
through wooden shutters. Camera slowly pulls back revealing the 
traditional Vietnamese workshop. 35mm cinematic lens, warm earthy 
color grade, in the style of National Geographic documentary, 24fps.

Negative: blurry, distorted hands, jittery motion, watermark, 
text overlay, cartoon, anime, low quality, oversaturated, fake
```

### Best practices Kling
✅ Negative prompt đầy đủ (đặc biệt "distorted hands", "jittery motion")
✅ Camera direction cụ thể
✅ Phong cách reference rõ
❌ Tránh prompt quá phức tạp với nhiều subject

---

## 5. Luma Dream Machine / Ray2

### Đặc điểm
- **Smooth motion** mượt mà nhất
- **Realistic physics**
- **Keyframe technique**: Start frame + end frame
- **5-10s clip**
- **Multimotion**: Combine multiple motions

### Cấu trúc Luma
```
[Scene description with smooth motion focus].
[Specific motion direction and quality].
[Style and lighting].
```

### Keyframe phrasing (image-to-video)
```
Start: [Description of first image]
End: [Description of how scene changes]
Motion: [Camera and subject movement between]
```

### Ví dụ Luma
```
Smooth cinematic shot of a coffee being poured into a glass cup,
liquid flowing in beautiful slow-motion swirls creating crema on top.
Camera slowly pushes in toward the cup with steady motion.
Warm overhead café lighting with golden tones.
Realistic physics with detailed liquid simulation,
shallow depth of field, 60fps smooth slow-motion,
in the style of premium coffee commercials.
```

### Best practices Luma
✅ Tập trung vào "smooth", "realistic motion"
✅ Mô tả vật lý cụ thể (liquid, fabric, hair)
✅ Slow-motion làm nổi bật điểm mạnh
❌ Tránh chuyển động giật cục

---

## 6. Pika 2.0

### Đặc điểm
- **Pikaffects**: Special effects (melt, crush, explode, inflate, levitate)
- **Lip-sync**: Sync môi với audio
- **Ingredients (Scenes)**: Mix multiple images
- **3-10s clip**

### Special Effects (Pikaffects keywords)
- `[melt]`: Subject melts
- `[crush]`: Crushed effect
- `[explode]`: Explosion
- `[inflate]`: Inflation
- `[levitate]`: Floating
- `[ta-da]`: Reveal effect
- `[deflate]`: Shrinking
- `[squish]`: Squishing

### Ví dụ Pika với effect
```
Cinematic close-up of a chocolate cake [melt],
warm soft kitchen lighting,
shallow depth of field,
satisfying slow transformation,
in the style of food art video,
60fps smooth motion, 16:9 cinematic
```

### Pika Lip-sync
```
Medium close-up of a young woman saying "Hello, welcome to my channel!"
warm cheerful expression, smooth lip-sync to audio,
soft natural lighting, vlog aesthetic,
30fps natural motion, 9:16 vertical
```

---

## 7. Hailuo / MiniMax

### Đặc điểm
- **Character consistency** xuất sắc trong cùng video
- **6 giây/clip**
- **Subject reference** từ image
- **Smooth realistic motion**

### Ví dụ Hailuo
```
Cinematic medium shot of a young man with curly black hair and glasses, 
wearing a beige sweater, sitting at a café reading a book. 
He looks up and smiles warmly at the camera.
Soft warm café lighting, shallow depth of field,
35mm cinematic lens, golden hour warm color grade,
intimate cozy mood, 24fps cinematic,
realistic facial expressions and natural motion.
```

---

## 8. Hunyuan / Wan 2.1 (Open Source)

### Đặc điểm
- **Open source** - tự host được
- **Customizable** - LoRA training
- **Variable length**
- **Quality phụ thuộc setup**

### Cấu trúc tương tự các tool khác nhưng có thể thêm:
- **Sampler**: DPM++, Euler
- **Steps**: 25-50
- **CFG scale**: 7-9
- **Seed**: For reproducibility

---

## Bảng so sánh nhanh

| Feature | Veo 3 | Sora | Runway | Kling | Luma | Pika | Hailuo |
|---------|-------|------|--------|-------|------|------|--------|
| **Max length** | 8s | 60s | 10s | 10s | 10s | 10s | 6s |
| **Audio** | ✅ Best | ❌ | ❌ | ❌ | ❌ | Lip-sync | ❌ |
| **Image-to-video** | ✅ | ✅ | ✅ Best | ✅ | ✅ Best | ✅ | ✅ |
| **Motion quality** | ✅✅✅ | ✅✅ | ✅✅ | ✅✅✅ | ✅✅✅ | ✅✅ | ✅✅ |
| **Prompt adherence** | ✅✅ | ✅✅ | ✅✅ | ✅✅✅ | ✅✅ | ✅✅ | ✅✅ |
| **Cinematic** | ✅✅✅ | ✅✅ | ✅✅ | ✅✅ | ✅✅ | ✅ | ✅✅ |
| **Special effects** | ❌ | ❌ | Motion brush | ❌ | ❌ | Pikaffects | ❌ |
| **Character consistency** | ✅ | ✅✅ | ✅ | ✅✅ | ✅ | ✅ | ✅✅✅ |
| **Best for** | Cinematic + Audio | Long form | Stylization | Realistic | Smooth | Effects | Character |

## Negative Prompt Universal (dùng cho mọi tool)

```
blurry, low quality, distorted, deformed, ugly, bad anatomy, 
extra limbs, missing limbs, disfigured, watermark, text, logo, 
signature, jittery motion, choppy frames, frame drops, 
oversaturated, low contrast, washed out, grainy noise, 
cartoon (when wanting realistic), anime (when wanting realistic), 
3D render (when wanting filmic), AI generated artifacts, 
morphing faces, melting features
```

## Tips chung cho mọi AI video tool

### NÊN
✅ Mô tả CHUYỂN ĐỘNG cụ thể bằng động từ mạnh
✅ Nêu cinematographer/director reference khi có
✅ Specify FPS cho hiệu ứng (slow-mo, time-lapse)
✅ Aspect ratio đầu prompt
✅ Lighting + color grading rõ ràng
✅ Subject mô tả chi tiết (age, appearance, clothing)
✅ Dùng film/lens reference (anamorphic, 35mm)

### KHÔNG NÊN
❌ Quá nhiều scene change trong 1 clip
❌ Yêu cầu text/chữ trong video
❌ Mô tả mơ hồ ("đẹp", "nice", "good")
❌ Quá nhiều subject phức tạp tương tác
❌ Bỏ qua duration limit
❌ Chỉ định technical impossible (1000fps trong tool 30fps cap)
