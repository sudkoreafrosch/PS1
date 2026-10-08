[PSIR Graduate Methods Problem Set 1_Hyeonbin.md](https://github.com/user-attachments/files/33220700/PSIR.Graduate.Methods.Problem.Set.1_Hyeonbin.md)
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
1. The research question of this paper is: “What is the effect of a religious message that calls for accepting more refugees on white evangelical Republicans’ attitudes toward accepting refugees?”

2. In the first condition, respondents do not receive the religious-values message. In the second condition (RV), respondents receive the religious-values message. In the third condition (RV+SC), respondents receive the religious-values message together with its source cue. The first condition differs from the other two in whether a message is given at all. RV and RV+SC differ only in whether a source cue is included.

3. The unit of random assignment is the individual respondent. Each YouGov panelist was randomly assigned to one of the three conditions. The unit of observation in the supplied data is also the individual respondent.

4. We limit the analysis to respondents in the RV condition and the control condition. Tᵢ is a treatment indicator that equals 1 if respondent i is assigned to the RV message and 0 if assigned to the control condition. Yᵢ(1) is the refugee feeling thermometer score (0–100) that respondent i would report after reading the RV message, and Yᵢ(0) is the score the same respondent would report without reading the message. The individual treatment effect is $Yᵢ(1) − Yᵢ(0)$, and the average treatment effect is the average of this value across all respondents: $E[Yᵢ(1) − Yᵢ(0)] = E[Yᵢ(1)] − E[Yᵢ(0)]$.

5. This is because of the fundamental problem of causal inference. For any respondent i, we can observe only one of Yᵢ(1) or Yᵢ(0).
--------------------------------------------------------------------------------

## Question 2: Exploring the Experiment

1. How many observations and variables are in the supplied data?
2. How many respondents are in each experimental condition?
3. Which variables contain missing values? Show how you checked.
4. Report the mean and standard deviation of age and the proportion of respondents recorded as female.
5. Describe the distributions and scales of the four outcome variables. Explain why their numerical values should not be compared without attending to their scales.

--------------------------------------------------------------------------------

[PUT YOUR ANSWER HERE]
1. There are 682 observations and 11 variables.

2. The control group has 234 respondents, the group that received the religious-values message has 226 respondents, and the group that received the religious-values message with a source cue has 222 respondents.

3. There are 32 missing values.

4. The mean age is 54.96 years, and the standard deviation is 17.77 years. The share of respondents recorded as female is 52.79%.

5. The refugee feeling thermometer is on a 0–100 scale and has a nearly symmetric distribution. Responses are widely spread and cluster around 50. Resettlement support is a 0–1 index and is concentrated between 0 and 0.5. The schooling item is on a 1–5 scale with a mean of 3.36, so responses lean toward support. The unemployment benefits item is also on a 1–5 scale with a mean of 2.04, so responses cluster on the opposing side. Because the four variables use different units, comparing their raw values directly leads to wrong conclusions. Therefore, to compare effects, we need to standardize the scales.

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
1. For the control group, the unweighted means are 47.9 for refugee_thermometer, 0.346 for resettlement_support, 3.36 for school_support, and 2.13 for benefits_support. For the group that received the religious-values message, the unweighted means are 57.2 for refugee_thermometer, 0.364 for resettlement_support, 3.34 for school_support, and 1.99 for benefits_support. For the group that received the religious-values message with the source cue, the unweighted means are 53.2 for refugee_thermometer, 0.365 for resettlement_support, 3.36 for school_support, and 1.99 for benefits_support.

2. Compared with the control group, the religious-values message raises the refugee feeling thermometer by 9.36 points and resettlement support by 0.018. In contrast, school support is lower by 0.018 points, and unemployment benefits support is lower by 0.141 points.

3. Compared with the control group, the religious-values message with a source cue raises the refugee feeling thermometer by 5.32 points, resettlement support by 0.019, and school support by 0.006 points. In contrast, unemployment benefits support is lower by 0.137 points.

4. On refugee_thermometer, which runs from 0 to 100, the group that received the religious-values message scores 9.36 points higher on average than the control group, and the group that received the message with the source cue scores 5.32 points higher. These are changes of about 9% and 5% of the full scale. On resettlement_support, which runs from 0 to 1, the effects are 0.018 and 0.019, or about 2 percentage points of the scale range, so the two treatments are almost the same. On school_support, which runs from 1 to 5, the effects are −0.018 points for the religious-values message and 0.006 points for the message with the source cue, which are close to zero. On benefits_support, also a 1–5 scale, the effects are −0.141 points and −0.137 points. The treatment effect is clearest for the refugee feeling thermometer, while the effects on resettlement, school, and unemployment benefits support are very small.

5. The figure is shown below.
 <img width="1066" height="693" alt="Image" src="https://github.com/user-attachments/assets/37abfc65-8a22-4d68-88fd-cafd421362bb" />

 
6. On the refugee feeling thermometer, the mean of the group that received the message with the source cue is 4.04 points lower than the mean of the group that received the religious-values message alone. In other words, the effect relative to the control group drops from 9.36 points without the source cue to 5.32 points with it, so the source cue seems to weaken the message rather than strengthen it. For resettlement support (0.001), school support (0.024), and unemployment benefits support (0.004), the two treatment groups are essentially the same. Therefore, based on these estimates, the source cue does not strengthen the message.

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
1. Age and ideology are numeric variables, so we computed their means for each experimental condition. Gender and education are categorical variables, so we cannot take their means. Instead, we calculated the share of respondents in each category for each condition. Gender is summarized as the share of women, and education is summarized as the share in each of its six categories. Age, gender, and ideology show almost no differences across the three conditions. Education shows relatively larger differences. The share of respondents with a graduate degree is 10.7% in the control group, 4.9% in the message group, and 7.2% in the message-plus-source-cue group. The share with some college but no degree is about 8 percentage points lower in the control group than in the two treatment groups.

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

2. The three groups are not exactly the same on observed pre-treatment characteristics. Age, gender, and ideology differ only very slightly, but they are not identical. Education differs more, so the groups can be seen as different on this variable. However, random assignment does not need to make the groups exactly equal in the one sample that was actually drawn. Random assignment guarantees balance in expectation.

3. Under random assignment, treatment is determined only by chance, so assignment is independent of both observed and unobserved characteristics. Therefore, if the assignment were repeated, the expected difference in group means would be zero for any pre-treatment characteristic, and any imbalance in a single assignment is just a random, non-systematic difference. As a result, the groups are comparable on average except for the treatment, and the difference in mean outcomes is an unbiased estimate of the treatment effect.

4. The assumption is plausible because treatment was assigned by random draw and is therefore independent of respondents’ potential outcomes. This comes from the design, that is, the assignment procedure, not from the balance table of observed variables.

5. One significant difference out of 20 at the 5% level is about what we would expect by chance, so it does not make the experiment invalid. The validity of the experiment comes from the design of random assignment, not from the balance table.

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
1. The advantage is that combining the two items reduces measurement error, so the treatment effect can be estimated more precisely. In fact, the two items are highly correlated, and Cronbach's alpha is high at 0.92. The disadvantage is that if attitudes toward resettlement differ at the national level and the local community level, we cannot tell which one the message moved.

2. The control group received neither the message nor the questions that asked respondents to think about it again. So the estimated effect is not the effect of the message alone but the effect of a bundled treatment: the message plus the reflection questions. We cannot rule out that reflection or pressure to stay consistent, created while answering the questions, made the effect larger. Therefore, we cannot simply call the treatment "the message."

3. Prior exposure does not violate random assignment. Whether a respondent had heard the message before is a characteristic fixed before the experiment, so random assignment spreads it evenly across the three conditions on average. However, prior exposure changes the meaning of the estimated effect. The effect in this experiment is not the effect of hearing the message for the first time but the effect of being exposed again to a familiar message. People who have already been influenced by the message have less room to move, so the estimated effect may be smaller than the effect of first exposure.

4. In this study, SUTVA means two things. First, respondent i's outcome depends only on which condition i was assigned to and is not affected by other respondents' assignments. Second, all respondents assigned to the same condition receive the same treatment. As an example of treatment variation, imagine an experiment testing the effect of a cold medicine in which every child is given the medicine. If some children take a whole pill and others take only half, they all belong to the group that took the medicine, but the treatment they actually received is different.

5. First, it is hard to generalize the results to other populations. In fact, in the experiment with non-evangelicals, no effect on the feeling thermometer appeared. Second, the effects come from people who read the message carefully. In real life, people often skim messages, so the real-world effect may be smaller.

6. What this experiment allows us to conclude is a short-term effect: the religious-values message shifts the attitudes toward refugees that respondents report in a survey right after reading it. We can say that, right after seeing the message, warmth toward refugees and support for resettlement were higher than in the control group. However, there are three things we cannot conclude. First, we do not know whether the effect lasts for days or weeks. Second, we do not know whether a change in survey answers also leads to a change in behavior. Third, we do not know whether the effect holds in a real-world setting where opposing messages are also present.

--------------------------------------------------------------------------------

## Question 6: Reading the Published Results

1. Compare your unweighted estimates with Table 2 of the paper. The authors use YouGov sample weights and regression, so your estimates need not be numerically identical. Explain what each approach targets.
2. Which outcomes provide evidence that the religious-values message increased support for refugees? Which outcomes produce null results?
3. Does the paper support the hypothesis that adding an evangelical source cue makes the religious-values message more effective? Cite the relevant comparison.
4. Summarize the paper's theoretical claim and central empirical finding in no more than 150 words.
5. Propose one follow-up experiment in a different population or political context. Clearly identify the treatment, outcome, target population, and the average treatment effect of interest.

--------------------------------------------------------------------------------

[PUT YOUR ANSWER HERE]
1. Comparing the unweighted difference-in-means estimates with Table 2, the effect of the religious-values message is 9.36 points versus 11.39 points on the feeling thermometer and 0.018 versus 0.05 on resettlement support. The effect of the message with a source cue is 5.32 points versus 7.18 points on the feeling thermometer and −0.137 points versus −0.25 points on unemployment benefits support. The direction of the effects is the same, but the weighted estimates are generally larger.
The two approaches target different quantities. The unweighted difference in means gives equal weight to all 682 respondents, so it estimates the average treatment effect in this analysis sample. In contrast, the authors’ weighted regression adjusts the sample to match the makeup of the population estimated by Pew, so it targets the average treatment effect in that population.

2. The outcomes that provide evidence that the religious-values message increased support for refugees are the feeling thermometer and resettlement support. The feeling thermometer is 11.39 points higher than in the control group and is statistically significant at the p<0.01 level, so it is strong evidence. Resettlement support is 0.05 higher but is significant only at the p<0.10 level, so it is relatively weak evidence. In contrast, the schooling item and the unemployment benefits item show null results that are not statistically significant.

3. The paper does not support Hypothesis 2. The message with a source cue and the message without one use the same wording except for the source cue, so the difference between them is the effect of the source cue itself. Table 2 also shows no evidence that the source cue made the effect larger. On the feeling thermometer, the effect of the message with a source cue (7.18 points) is smaller than that of the message without one (11.39 points), and resettlement support was weakly significant only for the message without a source cue. Neither treatment had an effect on the schooling item, and unemployment benefits support actually decreased only for the message with a source cue.

4. This paper argues that even in the Trump era, when partisanship was strong, messages that appeal to a group’s core values can move partisans away from their party’s position. The authors randomly showed white evangelical Republicans a pro-refugee message based on the teachings of Jesus. The message raised warmth toward refugees by about 11 points on a 0–100 scale and slightly increased support for resettlement. However, it did not increase support for public benefits for refugees, and adding a source cue from evangelical leaders did not make the message more effective. The effect was larger for people with a stronger evangelical identity, and even people with a strong Republican identity did not push back against the message.

5. As a follow-up study, we could test whether showing a religious-values message to conservative Protestants in South Korea changes their attitudes toward sexual minorities. In South Korea, there has been a long debate over passing an anti-discrimination law, and conservative Protestant groups have strongly opposed this law. The target population is conservative party supporters who identify themselves as Protestant, and the treatment is a religious message that emphasizes loving one’s neighbor. These respondents are randomly divided into two groups: the treatment group reads the religious message, and the control group sees no message.
The outcome is a feeling thermometer score in which respondents rate their feelings toward sexual minorities from 0 to 100. The average treatment effect of interest is the average, across this whole population, of the difference in feeling thermometer scores between reading and not reading the message.
--------------------------------------------------------------------------------

\newpage

# Digesting Cutting Edge Methods Papers into Key Takeaways (Building an Open-Source Reviewer Agent)

See [https://github.com/sysilviakim/quant-social-science-skills/tree/main/contrib](https://github.com/sysilviakim/quant-social-science-skills/tree/main/contrib). We are going to build an open-source reviewer agent focusing on quantitative methods. 

The TA has randomly assigned two papers to you. See `EXAMPLE-atsusaka_kim_2025.md` in the GitHub repository; your task is to carefully read the papers and create something equivalent for your assigned papers.

For PS1, choose one of the two assigned papers. For that paper, submit the following two items:

1. Show me that you actually did the reading. Print out the paper, take highlights and memos, and submit the outcome in person (I don't care if the memos and highlights are messy).
2. Submit a `.md` file that summarizes the paper's main points and explains what the reviewer should check for methodological integrity.
