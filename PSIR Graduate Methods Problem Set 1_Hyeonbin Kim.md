---
title: "PSIR Graduate Methods Problem Set 1"
author: "Seo-young Silvia Kim"
date: "`r format(Sys.time(), '%B %d, %Y')`"
header_includes:
- \usepackage{amsmath}
- \usepackage{amssymb}
- \usepackage{amsthm}
output:
  pdf_document:
    toc: yes
    toc_depth: '3'
---

# Instructions

* All answers must be typed up and submitted electronically as a PDF file, either via LaTeX or R Markdown. Submit the corresponding .Rmd or .R file as well.
* Most problem sets should be completed within the individual assigned groups. Collaboration is not allowed for the problem sets between set groups/individuals.
* Substitute "author" with your own names for the submission.
* Problem set 1 will be completed in groups of 4-5.

# The Average Treatment Effect and the Independence Assumption: Applying it to Research

This part should have every member's individual answers assembled here as subsections. I know you already submitted the abstract/intro, but let's do the following again to clarify the RQ and the estimation strategy:

1. What is the *causal* research question that you want to tackle in the final paper? State the question clearly. This does not mean that you have a clean causal setup; even when checking for correlations, the underlying questions are typically causal.
2. How would you operationalize and measure your outcome variable?
3. How would you operationalize and measure your main explanatory variable?
4. Consider the *average treatment effect (ATE)* under the potential outcomes framework, given binary treatment. If your explanatory variable is continuous or discrete, try creating a binary explanatory variable based on it, such as dichotomizing it. Consider the difference-in-means estimator (subscripts discarded for brevity):

$$ATE = \mathop{\mathbb{E}}[Y \mid T=1] - \mathop{\mathbb{E}}[Y \mid T=0]$$

In your research question, is this a valid estimator of the average treatment effect? That is to say, is the independence assumption $Y_i(1), Y_i(0) \perp T_i$ satisfied? At this point, do not consider controlling for other variables. We will return to that possibility later in the course.


# The Average Treatment Effect in a Randomized Experiment

White evangelical Republicans often hold two identities that point in different directions on refugee policy. Republican leaders have generally favored restrictions, while Christian teachings can emphasize care for refugees and other vulnerable strangers. DeMora et al. (2024) ask whether a message framed around religious values can increase support for refugees among self-identified white evangelical Republicans.

This exercise is based on: DeMora, Stephanie L., Jennifer L. Merolla, Brian Newman, and Elizabeth J. Zechmeister. 2024. "[Jesus Was a Refugee: Religious Values Framing Can Increase Support for Refugees Among White Evangelical Republicans.](https://doi.org/10.1007/s11109-024-09912-2)" *Political Behavior* 46: 2145--2168. The authors' replication materials are available from the [Harvard Dataverse](https://doi.org/10.7910/DVN/QYZQ4Y).

Read the sections titled "An Experiment to Assess the Religious Values Frame" and "Results of the Religious Values Framing Experiment" carefully. The researchers randomly assigned respondents to a control condition, a religious-values message without a source cue, or the same message accompanied by an evangelical source cue. The control group received neither the message nor its two follow-up questions.

The supplied file, `data/demora_2024.csv`, is a simplified teaching version of the authors' cleaned YouGov sample. Each row describes one respondent. Higher values on every outcome indicate more favorable attitudes toward refugees. Do not use `sample_weight` unless a question specifically asks you to do so.

--------------------------------------------------------------------------------
 Name                       Description
 -------------------------- -----------------------------------------------------
 `respondent_id`            Anonymous row identifier

 `treatment`                Control, religious-values message, or religious-values message with a source cue

 `refugee_thermometer`      Feeling toward refugees, from 0 to 100

 `resettlement_support`     Support for refugee resettlement, from 0 to 1

 `school_support`           Support for refugee children attending public schools, from 1 to 5

 `benefits_support`         Support for refugees receiving unemployment benefits, from 1 to 5

 `age`                      Respondent's age in 2020

 `gender`                   Respondent's gender, recorded as `Male` or `Female`

 `education`                Respondent's highest level of education

 `ideology`                 Ideology from 1, very liberal, to 5, very conservative

 `sample_weight`            YouGov weight for the target population
--------------------------------------------------------------------------------

Load the data before beginning the exercise. Beware of the relative paths; you may put the data where it suits you and edit the file path used for `read.csv`.

```{r, message=FALSE, warning=FALSE}
demora <- read.csv("data/demora_2024.csv")

demora$treatment <- factor(
  demora$treatment,
  levels = c(
    "Control",
    "Religious values message",
    "Religious values + source cue"
  )
)
```

## Question 1: Research Design

1. State the paper's causal research question in your own words.
2. What are the three experimental conditions? What features distinguish them?
3. What is the unit of random assignment? What is the unit of observation in the supplied data?
4. Focus first on the religious-values message without a source cue versus the control condition. Define $T_i$, $Y_i(1)$, $Y_i(0)$, and the average treatment effect when `refugee_thermometer` is the outcome.
5. Why can we never directly observe $Y_i(1)-Y_i(0)$ for any respondent?

--------------------------------------------------------------------------------

[PUT YOUR ANSWER HERE]
1. 이 논문의 연구질문은 "난민 수용 확대를 촉구하는 종교적 메시지가 백인 복음주의 공화당 지지자의 난민 수용태도에 미치는 영향은 무엇인가?"이다.

2. 첫 번째 조건은 종교적 가치 메시지를 받지 않은 것이다. 두 번째 조건(RV)은 종교적 가치 메시지를 받은 것이다. 세 번째 조건(RV+SC)은 종교적 가치 메시지와 그 출처 단서를 받은 것이다. 종교적 메시지를 받지 않은 조건과 나머지 두 조건은 메시지의 유무로 구별되고, RV와 RV+SC는 출처 단서의 유무로만 구별된다.

3. 무작위 배정의 단위는 개별 응답자이다. YouGov 패널 한 명 한 명이 세 조건 중 하나에 무작위로 배정되었다. 제공된 데이터의 관찰 단위도 개별 응답자이다.

4. 분석을 RV 조건과 통제 조건 응답자로 한정한다. Tᵢ는 응답자 i가 RV 메시지에 배정되면 1, 통제에 배정되면 0인 처치 지표이다. Yᵢ(1)은 응답자 i가 RV 메시지를 읽었을 때 보고할 난민 감정 온도계 점수(0-100)이고, Yᵢ(0)은 같은 응답자가 메시지를 읽지 않았을 때 보고할 점수이다. 개인의 처치효과는 $Yᵢ(1) − Yᵢ(0)$이며, 평균처치효과는 이를 모든 응답자에 대해 평균한 값, 즉 $E[Yᵢ(1) − Yᵢ(0)] = E[Yᵢ(1)] − E[Yᵢ(0)]$이다.

5. 인과 추론의 근본적 문제 때문이다. 어떤 i에 대해서도 Yᵢ(1)이나 Yᵢ(0) 둘 중 하나만 관측 가능하다.
--------------------------------------------------------------------------------

## Question 2: Exploring the Experiment

1. How many observations and variables are in the supplied data?
2. How many respondents are in each experimental condition?
3. Which variables contain missing values? Show how you checked.
4. Report the mean and standard deviation of age and the proportion of respondents recorded as female.
5. Describe the distributions and scales of the four outcome variables. Explain why their numerical values should not be compared without attending to their scales.

--------------------------------------------------------------------------------

[PUT YOUR ANSWER HERE]
1. 관측치는 682개, 변수는 11개이다.

2. 통제집단은 234개, 종교적 가치 메시지를 받은 집단은 226개, 종교적 가치 메시지와 출처 단서를 함께 받은 집단은 222개이다.

3. 결측치는 32개이다.

4. 연령의 평균은 54.96481세, 표준편차는 17.77131세이다. 여성으로 기록된 응답자의 비율은 52.78592%이다.

5. 난민 감정 온도계는 0-100점 척도이고 거의 대칭인 분포이다. 응답이 넓게 퍼져 있고 50점에 몰려 있다. 재정착 지지는 0-1지수이며 0-0.5에 집중되어 있다. 학교 문항은 1-5척도이고 평균 3.36으로 대체로 찬성 쪽이고, 실업급여는 1-5척도이고 평균 2.04로 반대 쪽에 몰려 있다. 네 변수는 단위가 서로 달라서 수치를 그대로 비교하면 잘못된 결론에 이른다. 따라서 효과를 비교하려면 척도를 표준화할 필요가 있다.

```{r}
# 2.1.
nrow(demora)
ncol(demora)

# 2.2.
table(demora$treatment)

# 2.3.
colSums(is.na(demora))

# 2.4.
mean(demora$age)
sd(demora$age)
mean(demora$gender == "Female")

# 2.5.
outcomes <- c("refugee_thermometer", "resettlement_support", "school_support", "benefits_support")

sapply(demora[outcomes], min, na.rm = TRUE)
sapply(demora[outcomes], max, na.rm = TRUE)
sapply(demora[outcomes], mean, na.rm = TRUE)
sapply(demora[outcomes], median, na.rm = TRUE)
sapply(demora[outcomes], sd, na.rm = TRUE)
```
--------------------------------------------------------------------------------

## Question 3: Estimating Average Treatment Effects

1. Calculate the unweighted mean of each outcome separately for the three experimental conditions.
2. For each outcome, estimate the effect of the religious-values message relative to the control using a difference in means.
3. For each outcome, estimate the effect of the religious-values message with a source cue relative to the control using a difference in means.
4. Interpret every estimate in the units of its outcome. For example, distinguish points on the 0--100 feeling thermometer from changes on the 0--1 resettlement scale.
5. Create one clearly labeled figure comparing mean `refugee_thermometer` scores across the three conditions. Preserve the experimental ordering shown in the variable table.
6. Based on these estimates, does the source cue appear to strengthen the message? Explain what comparison answers this question.

--------------------------------------------------------------------------------

[PUT YOUR ANSWER HERE]
1. 통제집단일 때, 비가중평균은 refugee_thermometer는 47.9, resettlement_support는 0.346, school_support는 3.36, benefits_support는 2.13이다. 종교적 가치 메시지가 개입한 집단일 때, 비가중평균은 refugee_thermometer는 57.2, resettlement_support는 0.364, school_support는 3.34, benefits_support는 1.99이다. 종교적 가치 메시지와 단서가 함께 개입한 집단일 때, 비가중평균은 refugee_thermometer는 53.2, resettlement_support는 0.365, school_support는 3.36, benefits_support는 1.99이다.

2. 종교적 가치 메시지는 난민 감정온도를 통제집단보다 9.362067점, 재정착 지지는 0.01778421 정도를 높여준다. 반면 학교 관련 지지는 -0.01826639점 그리고 실업급여 지지는 -0.1414795점 낮아졌다.

3. 출처 단서가 붙은 종교적 가치 메시지는 난민 감정온도를 통제집단보다 5.322929점, 재정착 지지는 0.01871102 정도, 그리고 학교 관련 지지는 0.005890506점 높여준다. 반면 실업급여 지지는 -0.1372141점 낮아졌다.

4. refugee_thermometer에서 종교적 가치 메시지를 받은 집단은 통제집단보다 평균 9.362067점 높고, 종교적 가치 메시지와 출처 단서를 받은 집단은 5.322929점 높다. resettlement_support에서 종교적 가치 메시지를 받은 집단의 효과는 0.01778421, 종교적 가치 메시지와 출처 단서를 받은 집단의 효과는 0.01871102로 거의 같다. school_support에서 종교적 가치 메시지를 받은 집단의 효과는 -0.01826639점, 종교적 가치 메시지와 출처 단서를 받은 집단의 효과는 0.005890506점이다. benefits_support에서 종교적 가치 메시지를 받은 집단의 효과는 -0.1414795점, 종교적 가치 메시지와 출처 단서를 받은 집단의 효과는 -0.1372141점이다. 처치효과는 난민 감정온도계에서 가장 뚜렷하다. 재정착, 학교, 실업급여 지지에서는 효과가 매우 작게 나타난다.

5. 그림은 아래와 같다.
 <img width="1066" height="693" alt="Image" src="https://github.com/user-attachments/assets/37abfc65-8a22-4d68-88fd-cafd421362bb" />

 
6. 난민 감정온도계에서는 종교적 가치 메시지와 출처 단서를 받은 집단의 평균이 종교적 가치 메시지를 받은 집단보다 -4.039138점이 낮다. 이는 종교적 가치 메시지를 받은 집단의 효과가 통제집단 대비 9.362067점에서 5.322929로 줄어든 것이므로 오히려 약화된 것으로 보인다. 재정착 지지(0.0009268118), 학교 관련 지지(0.0241569), 실업급여 지지(0.004265327)에서는 두 처치집단이 사실상 같다. 따라서 이 추정치로 보면 출처 단서는 메시지를 강화하지 않는다.


```{r}
##3.1.
library(tidyverse)

demora %>% group_by(treatment) %>% summarize(mean_thermometer = mean(refugee_thermometer, na.rm = TRUE), mean_resettlement = mean(resettlement_support, na.rm = TRUE), mean_school = mean(school_support, na.rm = TRUE), mean_benefits = mean(benefits_support, na.rm = TRUE))

##3.2.
control <- demora %>% filter(treatment == "Control")
message <- demora %>% filter(treatment == "Religious values message")

mean(message$refugee_thermometer, na.rm = TRUE) - mean(control$refugee_thermometer, na.rm = TRUE)
mean(message$resettlement_support, na.rm = TRUE) - mean(control$resettlement_support, na.rm = TRUE)
mean(message$school_support, na.rm = TRUE) - mean(control$school_support, na.rm = TRUE)
mean(message$benefits_support, na.rm = TRUE) - mean(control$benefits_support, na.rm = TRUE)

##3.3.
message_cue <- demora %>% filter(treatment == "Religious values + source cue")

mean(message_cue$refugee_thermometer, na.rm = TRUE) - mean(control$refugee_thermometer, na.rm = TRUE)
mean(message_cue$resettlement_support, na.rm = TRUE) - mean(control$resettlement_support, na.rm = TRUE)
mean(message_cue$school_support, na.rm = TRUE) - mean(control$school_support, na.rm = TRUE)
mean(message_cue$benefits_support, na.rm = TRUE) - mean(control$benefits_support, na.rm = TRUE)

##3.5.
thermo_means <- demora %>% group_by(treatment) %>% summarize(mean_thermometer = mean(refugee_thermometer, na.rm = TRUE))
ggplot(thermo_means, aes(x = treatment, y= mean_thermometer)) + geom_col() + expand_limits(y = c(0, 100)) + labs(title = "Mean Refugee Feeling Thermomether by Experimental Condition", x = "Experimental condition", y = "Mean feeling thermometer score (0-100)")

##3.6.
mean(message_cue$refugee_thermometer, na.rm = TRUE) - mean(message$refugee_thermometer, na.rm = TRUE)
mean(message_cue$resettlement_support, na.rm = TRUE) - mean(message$resettlement_support, na.rm = TRUE)
mean(message_cue$school_support, na.rm = TRUE) - mean(message$school_support, na.rm = TRUE)
mean(message_cue$benefits_support, na.rm = TRUE) - mean(message$benefits_support, na.rm = TRUE)

```
--------------------------------------------------------------------------------

## Question 4: Randomization and Independence

1. Compare age, gender, education, and ideology across the three conditions. Present a readable balance table. You will need to explain how you summarized categorical variables.
2. Are the groups exactly identical on these observed pretreatment characteristics? Should random assignment make them exactly identical in this realized sample?
3. What does random assignment imply about the relationship between treatment assignment and both observed and unobserved pretreatment characteristics across repeated assignments?
4. Based on the research design, is $Y_i(1),Y_i(0) \perp T_i$ plausible for the religious-values-message-versus-control comparison? Explain why the design, rather than the observed balance table alone, is the basis for your answer.
5. Suppose one balance difference is statistically significant at the 0.05 level after examining twenty pretreatment variables. Would this fact alone invalidate the experiment? Explain.

--------------------------------------------------------------------------------

[PUT YOUR ANSWER HERE]
1. 나이와 이념은 수치형 변수이므로 실험 조건별 평균을 구했고, 성별과 학력은 범주형 변수라 평균을 낼 수 없어 각 범주에 속한 응답자의 비율을 조건별로 계산했다. 성별은 여성 비율로, 학력은 6개 범주 각각의 비율로 요약하였다. 나이, 성별, 이념은 세 조건 간 차이가 거의 없었다. 학력은 상대적으로 차이가 커서, 대학원 졸업자 비율이 통제집단 10.7%, 메시지 집단 4.9%, 메시지 + 출처 단서 집단 7.2%이고, 대학 중퇴 등의 비율은 통제집단이 두 처치집단보다 8%p가량 낮다.

**Table 1.** Readable balance table

| Variable | Control | Religious values message | Religious values + source cue |
|---|---|---|---|
| N | 234 | 226 | 222 |
| Age, mean (SD) | 55.1 (18.4) | 55.5 (17.0) | 54.3 (17.9) |
| Female (%) | 53.0 | 53.1 | 52.3 |
| Ideology, mean (1–5) | 4.37 | 4.35 | 4.35 |
| No high school diploma (%) | 1.7 | 2.2 | 3.2 |
| High school graduate (%) | 36.3 | 37.6 | 35.6 |
| Some college (%) | 19.2 | 27.0 | 27.5 |
| Two-year degree (%) | 13.2 | 11.1 | 13.5 |
| Four-year degree (%) | 18.8 | 17.3 | 13.1 |
| Postgraduate degree (%) | 10.7 | 4.9 | 7.2 |

2. 세 집단은 관측된 사전 특성에서 정확히 같지 않다. 나이, 성별, 이념 모두 차이가 아주 작지만 같지 않다. 학력은 차이가 더 커서 다르다고 볼 수 있다. 그러나 무작위 배정이 실제로 뽑힌 하나의 표본에서 집단을 정확히 같게 만들어야 하는 것은 아니다. 무작위 배정은 기댓값에서의 균형을 담보한다.

3. 무작위 배정에서는 처치가 우연에 의해서만 결정되므로 배정은 관측된 특성과 관측되지 않은 특성 모두와 독립이다. 따라서 배정을 반복하면 어떤 사전 특성이든 집단 간 평균 차이의 기댓값은 0이 되고, 개별 배정에서 생기는 불균형은 체계적이지 않은 우연한 차이일뿐이다. 따라서 집단들은 처치를 제외하면 평균적으로 비교 가능하며, 결과변수의 평균 차이는 처치 효과의 편향되지 않은 추정치가 된다.

4. 처치는 무작위 추첨으로 배정되어 응답자의 잠재적 결과와 독립이므로 타당하며, 이는 관찰된 변수의 Balance Table이 아니라 배정 절차라는 설계에서 비롯된다.

5. 20개 중 1개가 5% 수준에서 유의한 것은 우연으로 예상되는 수준이므로 실험이 무효가 되지 않으며, 실험의 타당성은 Balance Table이 아니라 무작위 배정이라는 설계에서 비롯되는 것이다.

```{r}
## 4.1.
balance_table <- demora %>% group_by(treatment) %>% summarize(n = n(), age_mean = round(mean(age), 1), age_sd = round(sd(age), 1), female_pct = round(mean(gender == "Female") * 100, 1), ideology_mean = round(mean(ideology, na.rm = TRUE), 2), edu_no_hs_pct = round(mean(education == "No high school diploma") * 100, 1), edu_hs_pct = round(mean(education == "High school graduate") * 100, 1), edu_somecol_pct = round(mean(education == "Some college") * 100, 1), edu_2yr_pct = round(mean(education == "Two-year degree") * 100, 1), edu_4yr_pct = round(mean(education == "Four-year degree") * 100, 1), edu_postgrad_pct = round(mean(education == "Postgraduate degree") * 100, 1))

t(balance_table)


```

--------------------------------------------------------------------------------

## Question 5: Measurement, Assumptions, and Generalization

1. The `resettlement_support` outcome combines support for resettlement in the respondent's local community and in the United States. Discuss one advantage and one disadvantage of combining the two items.
2. The authors note that the treatment technically consists of a message plus two questions that ask respondents to reflect on it. What complication does this create when naming the causal treatment?
3. About 77 percent of treated respondents reported having heard the message previously. Does prior exposure violate random assignment? How might it affect the treatment effect estimated in this experiment?
4. State the Stable Unit Treatment Value Assumption (SUTVA) in this study. Give one plausible example of interference or treatment variation.
5. The analytic sample consists of self-identified white evangelical Republicans who passed the authors' prespecified reading-speed screen. Identify two limits this places on external validity.
6. The outcomes are survey responses measured shortly after treatment. What can and cannot be concluded about lasting changes in attitudes or political behavior?

--------------------------------------------------------------------------------

[PUT YOUR ANSWER HERE]
1. 장점은 두 문장을 결합했을 때 측정오차가 줄어들어 처치효과를 더 정밀하게 추정할 수 있다는 것이다. 실제로 두 문항은 상관이 높아 크론바흐 알파값이 0.92로 높게 나타난다. 단점은 국가 차원과 지역사회 차원의 재정착 태도가 다를 경우 메시지가 어느 쪽을 움직였는지 구분할 수 없게 된다는 것이다.

2. 통제집단은 메시지와 그 메시지를 다시 생각하게 하는 질문도 받지 않았으므로 추정된 효과는 메시지만의 효과가 아니라 '메시지와 숙고 질문'을 묶은 처치 효과이다. 질문에 답하는 과정에서 생긴 숙고나 일관성 압력이 효과를 키웠을 가능성을 배제할 수 없으므로, 처치를 단순히 '메시지'라고 부를 수는 없다.

3. 사전 노출은 무작위 배정을 위반하지 않는다. 메시지를 들어본 적이 있는지는 실험 전에 정해진 응답자의 특성이므로, 무작위 배정에 의해 세 조건에 평균적으로 고르게 분포한다. 다만 사전 노출은 추정된 효과의 의미를 바꾼다. 이 실험의 효과는 처음 듣는 메시지의 효과가 아니라 익숙한 메시지에 다시 노출되는 효과이다. 이미 메시지의 영향을 받은 사람은 더 움직일 여지가 적으므로, 추정된 효과는 메시지를 처음 접할 때의 효과보다 작게 나왔을 가능성이 있다.

4. 이 연구에서 SUTVA는 첫째, 응답자 i의 결과는 i자신이 어느 조건에 배정되었는지에만 달려 있고 다른 응답자의 배정에는 영향받지 않는다는 의미이다. 둘째, 같은 조건에 배정된 응답자는 모두 같은 처지를 받는다는 것이다. 처치 변이의 사례로 감기약의 효과를 알아보는 실험에서 아이들에게 모두 약을 주었다고 하자. 그런데 어떤 아이는 한 알을 먹고, 어떤 아이는 반 알만 먹었다면, 모두 약을 먹은 집단에 속해도 실제로 받은 처치는 서로 다를 수 있다.

5. 첫째, 결과를 다른 모집단으로 일반화하기 어렵다. 실제로 비복음주의자를 대상으로 한 실험에서는 감정 온도계 효과가 나타나지 않았다. 둘째, 메시지를 주의 깊게 읽은 사람에게서 나온 효과라는 한계가 있다. 현실에서는 메시지를 대충 훑고 지나가므로 실제 효과는 더 작을 수도 있다.

6. 이 실험으로 결론 내릴 수 있는 것은, 종교적 가치 메시지가 읽은 직후 설문에서 응답자가 밝히는 난민 태도를 움직인다는 단기적 효과이다. 메시지를 접한 직후에는 난민에 대한 호감과 재정착 지지가 통제 집단보다는 높았다는 것까지는 말할 수 있다. 반면 결론 내릴 수 없는 것은 세 가지이다. 첫째, 효과가 며칠이나 몇주 뒤에도 유지되는지 알 수 없다. 둘째, 설문 응답이 바뀌었다고 행동까지 바뀌는지 알 수 없다. 셋째, 현실처럼 반대 메시지가 함께 오가는 환경에서도 효과가 유지되는지 알 수 없다.

--------------------------------------------------------------------------------

## Question 6: Reading the Published Results

1. Compare your unweighted estimates with Table 2 of the paper. The authors use YouGov sample weights and regression, so your estimates need not be numerically identical. Explain what each approach targets.
2. Which outcomes provide evidence that the religious-values message increased support for refugees? Which outcomes produce null results?
3. Does the paper support the hypothesis that adding an evangelical source cue makes the religious-values message more effective? Cite the relevant comparison.
4. Summarize the paper's theoretical claim and central empirical finding in no more than 150 words.
5. Propose one follow-up experiment in a different population or political context. Clearly identify the treatment, outcome, target population, and the average treatment effect of interest.

--------------------------------------------------------------------------------

[PUT YOUR ANSWER HERE]
1. 비가중 평균 차이 추정치를 Table 2와 비교하면, 종교적 가치 메시지의 효과는 감정 온도계에서 9.362067점 대 11.39점, 재정착 지지에서 0.01778421 대 0.05이고, 출처 단서가 붙은 메시지 효과는 감정 온도계에서 5.322929점 대 7.18점, 실업급여 지지에서 -0.1414795점 대 -0.25점이다. 효과의 방향은 같지만 가중 추정치가 대체로 더 크다.
두 접근은 추정 대상이 다르다. 비가중 평균 차이는 응답자 682명에게 같은 무게를 주어, 이 분석 표본에서의 평균처치효과를 추정한다. 반면 저자들의 가중 회귀는 표본 구성을 Pew가 추정한 모집단의 구성에 맞게 재조정하므로, 그 모집단엣의 평균처치효과를 목표로 한다.

2. 종교적 가치 메시지가 난민 지지를 높였다는 증거를 보인 결과변수는 감정 온도계와 재정착 지지이다. 감정 온도계는 통제 집단보다 11.39점 높고 p<0.01 수준에서 통계적으로 유의해 강한 증거이며, 재정착 지지는 0.05 높지만 p<0.10 수준에서만 통계적으로 유의해 상대적으로 약한 증거이다. 반면 학교 문항과 실업급여 문항은 통계적으로 유의하지 않은 영 결과이다.

3. 본 논문은 가설 2를 지지하지 않는다. 출처 단서가 붙은 메시지와 출처 단서가 없는 메시지라는 조건은 출처 단서 외에는 문구가 같으므로, 이 차이가 곧 출처 단서의 효과이다. 표2에서도 출처 단서가 효과를 키웠다는 증거는 없다. 감정 온도계 효과는 출처 단서가 붙은 메시지가 7.18점으로 출처 단서가 없는 메시지의 11.39점보다 작고, 재정착 지지는 출처 단서가 없는 메시지에서만 약하게 유의했다. 학교 문항에서는 두 처치 모두 효과가 없었으며, 실업급여 지지는 출처 단서가 없는 메시지에서만 오히려 낮아졌다.

4. 본 논문의 이론적 함의는 당파성이 지배적인 상황에서도 집단의 핵심 가치에 호소하는 도덕 프레임은 당파적 여론을 움직일 수 있으며, 그 효과는 사회적 정체성의 강도에 따라 달라진다는 것이다. 실천적 함의는 난민 지지를 이끌어내려면 대상 집단의 종교적 가치에 맞춘 메시지가 유효하지만, 정책 지지로 이어지게 하려면 정부 정책을 직접 다루는 메시지가 필요하다는 것이다.

5. 후속 연구로 한국 보수 개신교인에게 종교적 가치 메시지를 보여주면 성소수자에 대한 태도가 달라지는지 검증할 수 있다. 한국에서는 차별금지법 제정을 두고 오랫동안 논쟁이 이어졌고, 보수 개신교계는 이 법에 반대하는 목소리를 크게 내 왔다. 목표 모집단은 스스로 개신교인이라고 밝힌 보수 정당 지지자이며, 처치는 이웃 사랑을 강조하는 종교적 메시지이다. 이들을 무작위로 두 집단으로 나누어 처치집단에는 종교적 메시지를 읽게 하고, 통제 집단에는 아무 메시지도 보여주지 않는다.
결과변수는 성소소자에게 느끼는 감정을 0-100점까지 표시하게 한 감정 온도계 점수이다. 관심 대상인 평균처치효과는 메시지를 읽었을 때와 읽지 않았을 때의 감정 온도계 점수 차이를 이 모집단 전체에 대해 평균한 값이다. 
--------------------------------------------------------------------------------

\newpage

# Digesting Cutting Edge Methods Papers into Key Takeaways (Building an Open-Source Reviewer Agent)

See [https://github.com/sysilviakim/quant-social-science-skills/tree/main/contrib](https://github.com/sysilviakim/quant-social-science-skills/tree/main/contrib). We are going to build an open-source reviewer agent focusing on quantitative methods. 

The TA has randomly assigned two papers to you. See `EXAMPLE-atsusaka_kim_2025.md` in the GitHub repository; your task is to carefully read the papers and create something equivalent for your assigned papers.

For PS1, choose one of the two assigned papers. For that paper, submit the following two items:

1. Show me that you actually did the reading. Print out the paper, take highlights and memos, and submit the outcome in person (I don't care if the memos and highlights are messy).
2. Submit a `.md` file that summarizes the paper's main points and explains what the reviewer should check for methodological integrity.
