import re

def swap_tone(char):
    tone_map = {
        'á': 'ả', 'à': 'ã', 'ả': 'á', 'ã': 'à',
        'é': 'ẻ', 'è': 'ẽ', 'ẻ': 'é', 'ẽ': 'è',
        'ó': 'ỏ', 'ò': 'õ', 'ỏ': 'ó', 'õ': 'ò',
        'ú': 'ủ', 'ù': 'ũ', 'ủ': 'ú', 'ũ': 'ù',
        'í': 'ỉ', 'ì': 'ĩ', 'ỉ': 'í', 'ĩ': 'ì',
        'ý': 'ỷ', 'ỳ': 'ỹ', 'ỷ': 'ý', 'ỹ': 'ỳ'
    }
    return tone_map.get(char, char)

def fix_vietnamese_tone(name):
    words = name.split()
    tone_marks = {'sắc': 0, 'hỏi': 0}
    word_tone_positions = []
    
    for i, word in enumerate(words):
        has_sac = any(c in 'áéóúíý' for c in word)
        has_hoi = any(c in 'ảẻỏủỉỷ' for c in word)
        
        if has_sac:
            tone_marks['sắc'] += 1
        if has_hoi:
            tone_marks['hỏi'] += 1
        
        if has_sac or has_hoi:
            word_tone_positions.append(i)
    
    if len(word_tone_positions) == 1 or any(count >= 2 for count in tone_marks.values()) or (tone_marks['sắc'] > 0 and tone_marks['hỏi'] > 0):
        last_word_index = word_tone_positions[-1]
        words[last_word_index] = ''.join(swap_tone(c) for c in words[last_word_index])

    return ' '.join(words)

# Test cases
names = [
    "Nguyễn Thị Lý",  # No change
    "Trần Văn Phúc",  # No change
    "Lê Thảo Ngọc Hải",  # Change last "Hải" -> "Hải"
    "Phạm Mạnh Hưng",  # No change
    "Nguyễn Sắc Sảnh",  # Change last "Sảnh" -> "Sảnh"
    'Trần Bích Thuỷ'
]

for name in names:
    print(f"Before: {name}")
    print(f"After : {fix_vietnamese_tone(name)}\n")