#!/usr/bin/env python
# coding: utf-8

# ## 문제 링크
# https://school.programmers.co.kr/learn/courses/30/lessons/135807

# In[13]:


# 시간 초과 : 77.8
# 시간 : 35분 소요 
def div_check(div,lst):
    flag = True
    for val in lst:
        if val % div !=0:
            flag = False
    return flag   # True : 모두를 나눌 수 있음 , False: 모두를 나눌 수 있는 것은 아님

def div_zero(div, lst):
    flag = False
    for val in lst:
        if val % div ==0:
            flag = True
            break
    return flag  # True : 하나쯤은 공약수 존재 False : 공약수 1도 존재하지 않음 

def solution(arrayA, arrayB):
    answer = 0
 
    # 최소값 min(arrayA)
    div_a = [] # a의 공약수가 될 수 있는 후보들 
    min_a = min(arrayA) # array 최소값 
    for i in range(1, min_a+1):
        if min_a % i == 0 :
            div_a.append(i)
    
    divA_present  = []
    # 후보들로 가지고 전체 array의 공약수인지 check 
    for div in sorted(div_a, reverse = True): # 큰 후보들부터 테스트 
        if div_check(div, arrayA): # 전체 array에 대한 공약수임
            divA_present.append(div) 
            break
    
    for div in divA_present:
        if (not div_zero(div, arrayB)) & (div > answer):
            answer = div
            
    # 최소값 min(arrayA)
    div_b= [] # a의 공약수가 될 수 있는 후보들 
    min_b = min(arrayB) # array 최소값 
    for i in range(1, min_b+1):
        if min_b % i == 0 :
            div_b.append(i)
    
    divB_present  = []
    # 후보들로 가지고 전체 array의 공약수인지 check 
    for div in sorted(div_b, reverse = True): # 큰 후보들부터 테스트 
        if div_check(div, arrayB): # 전체 array에 대한 공약수임
            divB_present.append(div) 
            break
    
    for div in divB_present:
        if (not div_zero(div, arrayA)) & (div > answer):
            answer = div
        
    
    return answer


# In[10]:


# arrayA = [10, 17]
# arrayB = [5, 20]

# arrayA = [10, 20]
# arrayB = [5, 17]

arrayA = [14, 35, 119]
arrayB = [18, 30, 102]


# In[11]:


solution(arrayA, arrayB)


# ## 참고

# 유클리드 호제법 등 최대 공약수 구하는 알고리즘 다시 공부하기
