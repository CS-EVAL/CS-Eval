import re
import json

def extract_singal_choice(gen):
    gen = gen.replace('a', 'A').replace('b', 'B').replace('c', 'C').replace('d', 'D')
    
    # 答案是A | 选项是A | 应该选A选项
    res = re.search(
        r"(?:(?:选|选择|选定)[：:]?\s*|(?:(?:答案|选项)(?![^ABCD]{0,10}?(?:不|非)[^ABCD]{0,10}?(?:是|选|为|：|:|】))[^ABCD]{0,10}?(?:是|选|为|：|:|】))[^ABCD]{0,10}?)(A|B|C|D)(?:选项)?(?:\)|。|\.|，|,|．|、|A|B|C|D|$|：|:|\)|）)",
        gen,
    )

    # A选项正确 | A选项符合题意
    if res is None:
        res = re.search(
            r"(A|B|C|D)(?:选?项)?(?![^ABCD]{0,4}?(?:不|非)[^ABCD]{0,4}?(?:正确|对[的，。：]|符合))[^ABCD]{0,4}?(?:正确|对[的，。：]|符合)",
            gen,
        )

    # 直接输出 A
    if res is None:
        res = re.search(r"^[\(（]?(A|B|C|D)(?:。|\)|）|\.|，|,|．|：|:|$)", gen)

    # 获取第一个出现的字母
    if res is None:
        res = re.search(r"(?<![a-zA-Z])(A|B|C|D)(?![a-zA-Z=])", gen)
    
    try:
        return res.group(1)
    except:
        print(f"res is {res}")
        return None

def extract_judge(gen):
    if gen[0] in ['对', '错', '是', '否']:
        return gen[0]
    else:
        for label in ['对', '错', '是', '否']:
            if label in gen:
                return label
        return None

def extract_yes_or_no(gen):
    gen = gen.lower()
    if gen.startswith("yes"):
        return "Yes"
    elif gen.startswith("no"):
        return "No"
    else:
        if gen.find('yes') != -1:
            return "Yes"
        elif gen.find('no') != -1:
            return "No"
        else:
            return None

def extract_multiple_choices(gen):
    gen = gen.replace('a', 'A').replace('b', 'B').replace('c', 'C').replace('d', 'D')
    gen = gen.replace('、', '')
    gen = gen.replace(',', '')
    gen = gen.replace('，', '')
    gen = gen.replace(' ', '')

    choices = []
    if 'A.' in gen or 'A)' in gen:
        choices.append("A")
    if 'B.' in gen or 'B)' in gen:
        choices.append("B")
    if 'C.' in gen or 'C)' in gen:
        choices.append("C")
    if 'D.' in gen or 'D)' in gen:
        choices.append("D")

    res = ''.join(choices)

    if res == '':
        res = None
    else:
        return res

    res = None

    if res is None:
        pattern_list = [
            # 答案是A|B|C 选项是A|B|C 应该选A|B|C选项
            r"(?:(?:选|选择|选定)[：:]?\s*|(?:(?:答案|选项)(?![^ABCD\uFF21\uFF22\uFF23\uFF24]{0,10}?(?:不|非)[^ABCD\uFF21\uFF22\uFF23\uFF24]{0,10}?(?:是|选|为|：|:|】))[^ABCD\uFF21\uFF22\uFF23\uFF24]{0,10}?(?:是|选|为|：|:|】))[^ABCD\uFF21\uFF22\uFF23\uFF24]{0,10}?)([ABCD\uFF21\uFF22\uFF23\uFF24]+)(?:选项)?(?:\)|。|\.|，|,|．|、|$|：|:|\)|）)",
            # A|B|C选项正确 A|B|C选项符合题意
            r"([ABCD\uFF21\uFF22\uFF23\uFF24]+)(?:选?项)?(?![^ABCD\uFF21\uFF22\uFF23\uFF24]{0,4}?(?:不|非)[^ABCD\uFF21\uFF22\uFF23\uFF24]{0,4}?(?:正确|对[的，。：]|符合))[^ABCD\uFF21\uFF22\uFF23\uFF24]{0,4}?(?:正确|对[的，。：]|符合)",
            # 获取所有出现的字母
            r"(?<![a-zA-Z])([ABCD\uFF21\uFF22\uFF23\uFF24]+)(?![a-zA-Z=])"
        ]
    
        for pattern in pattern_list:
            res = re.search(pattern, gen)
            if res:
                choices = res.group(1)
                # 去重
                choices = list(set(choices))
                choices.sort()
                return ''.join(choices)
    
    return res

def extract_choice_list(l):
    choice_list = []
    for span in l:
        if span.lower().startswith('a.') or span.lower().startswith('b.') or span.lower().startswith('b.') or span.lower().startswith('d.'):
            choice_list.append(span)
        if span.lower().startswith('a)') or span.lower().startswith('b)') or span.lower().startswith('b)') or span.lower().startswith('d)'):
            choice_list.append(span)

    return choice_list


# 读取原始答案文件
input_file = 'cs-eval-questions_qwen2-72b_result.json'
# 例如文件格式为：
# [
# {"id":xxx, "prompt":xxx, "response":xxx},
# {"id":xxx, "prompt":xxx, "response":xxx}
# ]

with open(input_file, 'r', encoding='utf-8') as f:
    answers = json.load(f)

# 正则化答案
normalized_answers = []

for answer in answers:
    if answer["prompt"].split('\n')[0] in ['单选题：', 'Single-choice question:']:
        temp_json = {}
        temp_json["question_id"] = answer["id"]
        temp_json["answer"] = extract_singal_choice(answer["response"])
        normalized_answers.append(temp_json)
    elif answer["prompt"].split('\n')[0] in ['多选题：']:
        temp_json = {}
        temp_json["question_id"] = answer["id"]
        temp_json["answer"] = extract_multiple_choices(answer["response"])
        normalized_answers.append(temp_json)
    elif answer["prompt"].split('\n')[0] in ['判断题：']:
        temp_json = {}
        temp_json["question_id"] = answer["id"]
        temp_json["answer"] = extract_judge(answer["response"])
        normalized_answers.append(temp_json)
    elif answer["prompt"].split('\n')[0] in ['Yes or No question:']:
        temp_json = {}
        temp_json["question_id"] = answer["id"]
        temp_json["answer"] = extract_yes_or_no(answer["response"])
        normalized_answers.append(temp_json)
    elif answer["prompt"].split('\n')[0] in ['知识抽取题：', 'Knowledge extraction question:']:
        temp_json = {}
        temp_json["question_id"] = answer["id"]
        temp_json["answer"] = answer["response"]
        normalized_answers.append(temp_json)

# 将结果写入result.json文件
with open(input_file+'_format.json', 'w', encoding='utf-8') as f:
    json.dump(normalized_answers, f, ensure_ascii=False, indent=4)
