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
1. 난민 수용 확대를 촉구하는 종교적 메시지가 백인 복음주의 공화당 지지자의 난민 수용태도에 미치는 영향은 무엇인가?
2. 첫 번째 조건은 난민 수용 확대를 촉구하는 종교적 메시지를 받지 않은 것이다. 두 번째 조건은 난민 수용 확대를 촉구하는 종교적 메시지를 받은 것이다. 세 번째 조건은 난민 수용 확대를 촉구하는 종교적 메시지와 그 단서를 받은 것이다. 각 조건을 구별하는 특징은 피실험자에 대한 실험자의 개입의 정도가 다르다는 것이다.
3. 무작위 배정의 단위는 Individual (White self-identified evangelicals)임. 제공된 데이터에서 관찰단위 또한 Individual (White self-identified evangelicals)임.
4. 평균처치효과는 $`ATE = E[Y_i \mid T_i = 1] - E[Y_i \mid T_i = 0]`$ 로 정의된다.
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
2. 통제집단은 234개, 종교적 가치 메시지를 받은 집단은 226개, 종교적 가치 메시지와 단서를 함께 받은 집단은 222개이다.
3. 결측치는 32개이다.
4. 연령의 평균은 54.96481세, 표준편차는 17.77131세이다. 여성으로 기록된 응답자의 비율은 52.78592%이다.
5. refugee_thermometer는 0-100점 척도이고 거의 대칭인 분포임. 응답이 넓게 퍼져 있고 50점에 몰려 있음.  resettlement_support는 0-1지수이며 0~0.5에 집중되어 있음. school_support는 1-5척도이고 높은 쪽에 몰려 있음. benefits_support는 1-5척도이며 낮은 쪽에 몰려 있음. 변수 간 비교를 하기 위해서는 척도를 표준화할 필요가 있음.

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
2. 종교적 가치 메시지는 난민에 대한 감정온도를 통제집단보다 9.362067점 높임. 재정착 지지는 0.01778421 정도를 높여줌. 학교 관련 지지는 -0.01826639점 낮아졌음. 복지 혜택 지지는 -0.1414795점 낮아졌음.
3. 출처 단서가 붙은 종교적 가치 메시지는 난민 감정온도를 통제집단보다 5.322929점 높임. 재정착 지지는 0.01871102 정도를 높여줌. 학교 관련 지지는 0.005890506점 높여줌, 복지 혜택 지지는 -0.1372141점 낮아졌음.
4. refugee_thermometer에서 메시지 집단은 통제집단보다 평균 9.362067점 높고, 메시지 + 출처 집단은 5.322929점 높다. resettlement_support에서 메시지 효과는 0.01778421, 메시지 + 출처 집단 효과는 0.01871102로 거의 같다. school_support에서 메시지 효과는 -0.01826639점, 메시지 + 출처 집단 효과는 0.005890506점이다. benefits_support에서 메시지 효과는 -0.1414795점, 메시지 + 출처 집단 효과는 -0.1372141점이다. 개입효과는 감정온도계에서 가장 뚜렷하다. 재정착, 학교, 복지 지지에서는 효과가 매우 작게 나타난다.

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
cue_group <- demora %>% filter(treatment == "Religious values + source cue")

mean(cue_group$refugee_thermometer, na.rm = TRUE) - mean(control$refugee_thermometer, na.rm = TRUE)
mean(cue_group$resettlement_support, na.rm = TRUE) - mean(control$resettlement_support, na.rm = TRUE)
mean(cue_group$school_support, na.rm = TRUE) - mean(control$school_support, na.rm = TRUE)
mean(cue_group$benefits_support, na.rm = TRUE) - mean(control$benefits_support, na.rm = TRUE)

##3.5.


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

```{r}
## [PUT YOUR CODE HERE]
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

--------------------------------------------------------------------------------

## Question 6: Reading the Published Results

1. Compare your unweighted estimates with Table 2 of the paper. The authors use YouGov sample weights and regression, so your estimates need not be numerically identical. Explain what each approach targets.
2. Which outcomes provide evidence that the religious-values message increased support for refugees? Which outcomes produce null results?
3. Does the paper support the hypothesis that adding an evangelical source cue makes the religious-values message more effective? Cite the relevant comparison.
4. Summarize the paper's theoretical claim and central empirical finding in no more than 150 words.
5. Propose one follow-up experiment in a different population or political context. Clearly identify the treatment, outcome, target population, and the average treatment effect of interest.

--------------------------------------------------------------------------------

[PUT YOUR ANSWER HERE]

--------------------------------------------------------------------------------

\newpage

# Digesting Cutting Edge Methods Papers into Key Takeaways (Building an Open-Source Reviewer Agent)

See [https://github.com/sysilviakim/quant-social-science-skills/tree/main/contrib](https://github.com/sysilviakim/quant-social-science-skills/tree/main/contrib). We are going to build an open-source reviewer agent focusing on quantitative methods. 

The TA has randomly assigned two papers to you. See `EXAMPLE-atsusaka_kim_2025.md` in the GitHub repository; your task is to carefully read the papers and create something equivalent for your assigned papers.

For PS1, choose one of the two assigned papers. For that paper, submit the following two items:

1. Show me that you actually did the reading. Print out the paper, take highlights and memos, and submit the outcome in person (I don't care if the memos and highlights are messy).
2. Submit a `.md` file that summarizes the paper's main points and explains what the reviewer should check for methodological integrity.
