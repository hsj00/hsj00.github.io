---
title: Python으로 수열 계산 구현
layout: post
date: 2024-03-12 20:30
tag:
    - Python
    - Mac
    - Programming
    - Study
    - Note
    - math
headerImage: false
image: null
description: 240312 `Python coding - sequence calculation`
category: blog
author: hsj00
published: true
comments: true
share: true
use_math: false
toc: false
---

# 수열 계산기

가늘고 길게, 드문드문 이어져오는 파이썬 프로그래밍 공부의 새로운 결과물이다.

ToC는 다음과 같다.

- [수열 계산기](#수열-계산기)
  - [1. 수열 계산기로 구현하고자 하는 기능](#1-수열-계산기로-구현하고자-하는-기능)
    - [1.1. 구현하려는 기능](#11-구현하려는-기능)
    - [1.2. 사용한 패키지](#12-사용한-패키지)
  - [2. `SequenceCalc.py`](#2-sequencecalcpy)
  - [3. `sequence.py`](#3-sequencepy)

## 1. 수열 계산기로 구현하고자 하는 기능

### 1.1. 구현하려는 기능

다음 네 종류의 수열을 계산하는 계산기를 구현하고자 한다.

- Mean
- Sum
- min
- Max

계산하려는 수열 종류는 다음과 같다.

- 등차수열
- 등비수열
- 조화수열
- 계차수열
- 피보나치 수열

### 1.2. 사용한 패키지

기능 구현을 위해 `scipy` 파이썬 패키지를 `import`해서 등비중항과 조화중항 계산을 위해 사용했다.

```python
# 등비중항 및 조화중항의 계산
from scipy.stats import gmean, hmean
```

다음 두 개의 파이썬 스크립트로 나눠서 기능을 구현했다.

- `SequenceCalc.py`: 각 수열마다 계산 기능을 함수로 구현한 스크립트 파일이다.
- `sequence.py`: 수열의 종류와 초항 입력, 공차/공비와 같은 수열의 특징적인 값 및 전체 항의 개수를 설정한다. `SequenceCalc.py`를 `import`해서 계산을 진행하는 스크립트 파일이다.

## 2. `SequenceCalc.py`

코드는 다음과 같다.

<details>
<summary><b> Show me the code! </b></summary>
<div markdown="1">

```python
from scipy.stats import gmean, hmean

# Series calculator
# 1. Arithmetical sequence
# 2. Geometric sequence
# 3. Harmonic sequence
# 4. Difference sequence
# 5. Fibonacci sequence

# Declaration for results of calculation and sequence list
sq_results = {"Mean": None, "Sum": None, "min": None, "Max": None}
sq_length = []

# Arithmetical sequence
    sqa_difference = float(input("Common difference: "))
    sequence_info = print(f"Common difference is {sqa_difference}.")
  
    sq_length = [sq_start]

    for i in range(1, sq_range):  
        sqa_next = sq_length[-1] + sqa_difference
        sq_length.append(sqa_next)
  
    sq_mean = sum(sq_length) / len(sq_length)
    sq_sum = sum(sq_length)
    sq_min = min(sq_length)
    sq_max = max(sq_length)

    sq_results["Mean"] = sq_mean
    sq_results["Sum"] = sq_sum
    sq_results["min"] = sq_min
    sq_results["Max"] = sq_max

    print("Result: ", sq_results)
    print("Seq list: ", sq_length)

    return sq_results, sq_length

# Geometric sequence
def generate_geometric_sequence(sq_start, sq_range):
    sqg_ratio = float(input("Common ratio: "))
    sequence_info = print(f"Common ratio is {sqg_ratio}.")

    sq_length = [sq_start * sqg_ratio**i for i in range(sq_range)]

    if sqg_ratio == 1:
        sq_sum = sq_start * sq_range
    else:
        sq_sum = sq_start * (sqg_ratio**sq_range - 1) / (sqg_ratio - 1)
  
    sq_mean = gmean(sq_length)
    sq_min = min(sq_length)
    sq_max = max(sq_length)

    sq_results["Mean"] = sq_mean
    sq_results["Sum"] = sq_sum
    sq_results["min"] = sq_min
    sq_results["Max"] = sq_max

    print("Result: ", sq_results)
    print("Seq list: ", sq_length)

    return sq_results, sq_length

# Harmonic sequence
def generate_harmonic_sequence(sq_start, sq_range):
    sqh_difference = float(input("Common difference: "))
    sequence_info = print(f"Common difference is {sqh_difference}.")


    sq_length = [sq_start / (1 + (sq_start*sqh_difference*i)) for i in range(sq_range+1)]

    sq_mean = hmean(sq_length)
    sq_sum = sum(sq_length)
    sq_min = min(sq_length)
    sq_max = max(sq_length)

    sq_results["Mean"] = sq_mean
    sq_results["Sum"] = sq_sum
    sq_results["min"] = sq_min
    sq_results["Max"] = sq_max

    print("Result: ", sq_results)
    print("Seq list: ", sq_length)

    return sq_results, sq_length

# Difference sequence including sub-sequence
def generate_difference_sequence(sq_start, sq_range, subsq_type):
    subsq_length = []
    diff_seq = []
  
    # 'if' statements for sub-sequence calculation
    # Sub: Arithmetical sequence
    if subsq_type == 1:
        sub_sqa_difference = float(input("Common difference: "))
        sequence_info = print(f"Common difference is {sub_sqa_difference}.")
  
        subsq_length = [sq_start]

        for i in range(1, sq_range):  
            sqa_next = subsq_length[-1] + sub_sqa_difference
            subsq_length.append(sqa_next)
      
        diff_seq = [subsq_length[i] - subsq_length[i-1] for i in range(1, sq_range)]

        sq_mean = sum(diff_seq) / len(diff_seq)
        sq_sum = sum(diff_seq)
        sq_min = min(diff_seq)
        sq_max = max(diff_seq)

        sq_results["Mean"] = sq_mean
        sq_results["Sum"] = sq_sum
        sq_results["min"] = sq_min
        sq_results["Max"] = sq_max

        print("Result: ", sq_results)
        print("Sub-seq list: ", subsq_length)
        print("Diff-seq list: ", diff_seq)

        return sq_results, diff_seq
  
    # Sub: Geometric sequence
    elif subsq_type == 2:
        sub_sqg_ratio = float(input("Common ratio: "))
        sequence_info = print(f"Common ratio is {sub_sqg_ratio}.")

        subsq_length = [sq_start * sub_sqg_ratio**i for i in range(sq_range)]

        diff_seq = [subsq_length[i] - subsq_length[i-1] for i in range(1, sq_range)]

        sq_mean = sum(diff_seq) / len(diff_seq)
        sq_sum = sum(diff_seq)
        sq_min = min(diff_seq)
        sq_max = max(diff_seq)

        sq_results["Mean"] = sq_mean
        sq_results["Sum"] = sq_sum
        sq_results["min"] = sq_min
        sq_results["Max"] = sq_max

        print("Result: ", sq_results)
        print("Sub-seq list: ", subsq_length)
        print("Diff-seq list: ", diff_seq)

        return sq_results, diff_seq
  
    # Sub: Difference sequence
    elif subsq_type == 3:
        sub_sqh_difference = float(input("Common difference: "))
        sequence_info = print(f"Common difference is {sub_sqh_difference}.")

        subsq_length = [sq_start / (1 + (sq_start*sub_sqh_difference*i)) for i in range(sq_range+1)]

        diff_seq = [subsq_length[i] - subsq_length[i-1] for i in range(1, sq_range)]

        sq_mean = sum(diff_seq) / len(diff_seq)
        sq_sum = sum(diff_seq)
        sq_min = min(diff_seq)
        sq_max = max(diff_seq)

        sq_results["Mean"] = sq_mean
        sq_results["Sum"] = sq_sum
        sq_results["min"] = sq_min
        sq_results["Max"] = sq_max

        print("Result: ", sq_results)
        print("Sub-seq list: ", subsq_length)
        print("Diff-seq list: ", diff_seq)

        return sq_results, diff_seq
  
    # Sub: Fibonacci sequence
    elif subsq_type == 4:
        subsq_length = [sq_start, sq_start + 1]

        for i in range(2, sq_range):
            subsqf_next = subsq_length[i - 1] + subsq_length[i - 2]
            subsq_length.append(subsqf_next)

        diff_seq = [subsq_length[i] - subsq_length[i-1] for i in range(1, sq_range)]

        sq_mean = sum(diff_seq) / len(diff_seq)
        sq_sum = sum(diff_seq)
        sq_min = min(diff_seq)
        sq_max = max(diff_seq)

        sq_results["Mean"] = sq_mean
        sq_results["Sum"] = sq_sum
        sq_results["min"] = sq_min
        sq_results["Max"] = sq_max

        print("Result: ", sq_results)
        print("Sub-seq list: ", subsq_length)
        print("Diff-seq list: ", diff_seq)

        return sq_results, diff_seq

# Fibonacci sequence
def generate_fibonacci_sequence(sq_start, sq_range):
    sq_length = [sq_start, sq_start + 1]

    for i in range(2, sq_range):
        sqf_next = sq_length[i - 1] + sq_length [i - 2]
        sq_length.append(sqf_next)

    sq_mean = sum(sq_length) / len(sq_length)
    sq_sum = sum(sq_length)
    sq_min = min(sq_length)
    sq_max = max(sq_length)

    sq_results["Mean"] = sq_mean
    sq_results["Sum"] = sq_sum
    sq_results["min"] = sq_min
    sq_results["Max"] = sq_max

    print("Result: ", sq_results)
    print("Seq list: ", sq_length)

    return sq_results, sq_length

# Declaration for executing script function directly
if __name__ == "__main__":
    print("Sequence calculator")
  
    sq_start = float(input("Initial value: "))
    sq_range = round(float(input("Total terms: ")))
  
    print("< Arithmetical sequence >")
    generate_arithmetical_sequence(sq_start, sq_range)
  
    print("< Geometric sequence >")
    generate_geometric_sequence(sq_start, sq_range)
  
    print("< Harmonic sequence >")
    generate_harmonic_sequence(sq_start, sq_range)
  
    print("< Difference sequence >")
    generate_difference_sequence(sq_start, sq_range, int(input("Sub-sequence: ")))
  
    print("< Fibonacci sequence >")
    generate_fibonacci_sequence(sq_start, sq_range)
```

</div>
</details><br>

## 3. `sequence.py`

코드는 다음과 같다.

<details>
<summary><b> Show me the code! </b></summary>
<div markdown="1">

```python
from SequenceCalc import *

# Series calculator
# 1. Arithmetical sequence
# 2. Geometric sequence
# 3. Harmonic sequence
# 4. Difference sequence
# 5. Fibonacci sequence

def sequence_calculator():
  
    sq_type = None
    sequence_info = None
  
    # Input step for sequence condition decision
    while True:
        sq_start = float(input("Sequence start: "))
        sq_range = round(float(input("Sequence length: ")))
        sq_type = round(float(input("Sequence_type (1. Arithmetical, 2. Geometric, 3. Harmonic, 4. Difference, 5. Fibonacci): ")))
      
        sequence_type = None

        if 1 <= sq_type <= 5:
            if sq_type == 1:
                sequence_type = "Arithmetical sequence"
                sequence_info = print(f"The initial term of the sequence is {sq_start}, and the length of the sequence is {sq_range}. The sequence type is {sequence_type}.")
                generate_arithmetical_sequence(sq_start, sq_range)
                break
            elif sq_type == 2:
                sequence_type = "Geometric sequence"
                sequence_info = print(f"The initial term of the sequence is {sq_start}, and the length of the sequence is {sq_range}. The sequence type is {sequence_type}.")
                generate_geometric_sequence(sq_start, sq_range)
                break
            elif sq_type == 3:
                sequence_type = "Harmonic sequence"
                sequence_info = print(f"The initial term of the sequence is {sq_start}, and the length of the sequence is {sq_range}. The sequence type is {sequence_type}.")
                generate_harmonic_sequence(sq_start, sq_range)
                break
            elif sq_type == 4:
                sequence_type = "Difference sequence"
                subsq_type = round(float(input("Sub-sequence_type (1. Arithmetical, 2. Geometric, 3. Harmonic, 4. Fibonacci): " )))
                while True:
                    if subsq_type == 1:
                        subsequence_type = "Arithmetical sequence"
                        sequence_info = print(f"The initial term of the sequence is {sq_start}, and the length of the sequence is {sq_range}. The sub-sequence type is {subsequence_type}.")
                        # generate_arithmetical_sequence(sq_start, sq_range)
                      
                    elif subsq_type == 2:
                        subsequence_type = "Geometric sequence"
                        sequence_info = print(f"The initial term of the sequence is {sq_start}, and the length of the sequence is {sq_range}. The sequence type is {subsequence_type}.")
                        # generate_geometric_sequence(sq_start, sq_range)
                      
                    elif subsq_type == 3:
                        subsequence_type = "Harmonic sequence"
                        sequence_info = print(f"The initial term of the sequence is {sq_start}, and the length of the sequence is {sq_range}. The sequence type is {subsequence_type}.")
                        # generate_harmonic_sequence(sq_start, sq_range)
                      
                    elif subsq_type == 4:
                        subsequence_type = "Fibonacci sequence"
                        sequence_info = print(f"The initial term of the sequence is {sq_start}, and the length of the sequence is {sq_range}. The sequence type is {subsequence_type}.")
                        # generate_fibonacci_sequence(sq_start, sq_range)
                      
                    else:
                        print("Invalid subsequence type. Please enter a number from '1' to '4'.")
                        continue
                    break

                sequence_info = print(f"{sequence_type} is calculating based on {subsequence_type}.")
                generate_difference_sequence(sq_start, sq_range, subsq_type)
                break
            elif sq_type == 5:
                sequence_type = "Fibonacci sequence"
                sequence_info = print(f"The initial term of the sequence is {sq_start}, and the length of the sequence is {sq_range}. The sequence type is {sequence_type}.")
                generate_fibonacci_sequence(sq_start, sq_range)
                break
        else:
            print("Invalid sequence type. Please enter a number from '1' to '5'.")


if __name__ == "__main__":
    sequence_calculator()
```

</div>
</details><br>

---

<!-- Links -->

<!-- references -->
