# Multiplicative Interaction Models

**Full citation:** Hainmueller, J., Mummolo, J., & Xu, Y. (2019). How much should we trust estimates from multiplicative interaction models? Simple tools to improve empirical practice. *Political Analysis*, 27(2), 163–192. https://doi.org/10.1017/pan.2018.46

*Page numbers are the printed page numbers of the published article.*

---

## 1. What the paper establishes

*(to be written)*

## 2. Checks for a reviewer

**(a) In the Linear Interaction Diagnostic (LID) plot, check whether the linear and LOESS fits pull apart in either treatment group, and whether the moderator or the treatment is highly skewed.** The conditional effect is the gap between the two groups' regression lines, so the linear interaction effect (LIE) assumption fails if either line is misspecified by a nonlinear or non-monotonic pattern or by a skewed variable. If a variable is highly skewed, check whether the authors considered a power or root transformation.

**(b) At each moderator value where the manuscript reports a marginal effect, check whether there are enough observations nearby and whether those observations vary in the treatment.** Compare the range of the marginal-effect plot with the moderator's distribution. With a binary treatment, both treated and control units must be present at that value.

**(c) Check whether the manuscript shows LID plots for linearity and box plots of the moderator by treatment group for common support.** An LID plot shows the outcome against the moderator for each treatment group, with a linear fit and a LOESS fit. If both the treatment and the moderator are continuous, check whether the sample is split into terciles of the moderator and the outcome is plotted against the treatment within each tercile. If these plots are missing, ask for them.

**(d) If the manuscript reports binning estimates, check whether they sit far from the linear marginal-effect line or rise and then fall across bins.** Either pattern is evidence against the LIE assumption. If the manuscript reports no binning estimates, ask for them before accepting the linear model.

**(e) If the manuscript reports kernel estimates, check whether its claims rest on moderator values where the confidence intervals widen sharply.** Wide intervals there show that the data are too sparse to estimate the effect, so a claim in that region relies on the assumed functional form rather than on the data.

## 3. Evidence

**For (a).** The authors explain that "the LIE assumption will fail if one or both functions are misspecified due to nonlinearities, nonmonotonicities, or a skewed distribution of X and/or D" (p. 167). With a binary treatment, the two functions are the regression lines of the outcome on the moderator for the treated and control groups (Equation 3, p. 167), and the LID plot tests each line by checking whether its linear and LOESS fits diverge (p. 168). For a skewed variable, the authors recommend that researchers "use appropriate power and/or root transformations to reduce skewness" (p. 187).

**For (b).** The revised checklist states: "Researchers should avoid computing marginal effects in areas where the data is too sparse either because there are no observations for those values of the moderator or there is no variation in the treatment." (p. 187). These two conditions are the two questions in (b), and a reviewer can answer both by laying the range of the marginal-effect plot over the moderator's distribution. In the Chapman (2009) replication, all observations with a U.N. authorization fall in the lowest tercile of the moderator, so the linear model's effects outside that narrow range are "based purely on extrapolation" (p. 178).

**For (c).** The revised checklist opens with this step: "Generate the LID plot to check whether the conditional relationships between the outcome, treatment, and moderator are well approximated by a linear fit" (p. 187). The same step asks researchers to check common support (p. 187), which the LID figure does with its box plots: "The box plots near the center of the figures display quantiles of the moderator at each level of the treatment." (p. 169). When both the treatment and the moderator are continuous, the authors split the sample into terciles of the moderator and plot the outcome against the treatment within each tercile (p. 170).

**For (d).** The authors give the reading rule directly: "When the estimates from the binning estimator are far off the line or when they are non-monotonic, we have evidence that the LIE assumption does not hold." (p. 173). Here the line is the linear model's marginal-effect line, on which the authors plot the three bin estimates (p. 172). The revised checklist adds that the linear model should be used only if the binning or kernel estimates "suggest that the interaction is really linear" (p. 187), so a manuscript without binning estimates should be asked for them.

**For (e).** On the kernel estimates, the authors write: "The fact that the confidence intervals grow wider at those points is desirable because it makes clear the increasing lack of common support." (p. 175). Widening intervals are therefore the estimator's signal of where the data run out, not a flaw, and the reviewer's task is to see whether the manuscript's claims sit in that region. In the Chapman (2009) replication, the kernel intervals "blow up" outside the narrow range where the treatment varies, so the effect there "cannot be estimated" (p. 178).

## 4. Scope

**Applies to:** manuscripts whose substantive claim rests on a multiplicative interaction in which at least one of the two interacted variables is continuous, estimated by OLS or a linear fixed-effects model. This is the setting the authors say the existing guidelines miss (p. 164) and the one they sampled for their replications (p. 175). Within this scope, each check has its own trigger and its own silent case.

**(a)** applies once an LID plot is available, either in the manuscript or after (c) asks for it. Its skewness part applies whenever the moderator or the treatment has a long tail or many cases at a single value. It stays silent when both variables take only a few values and the model is fully saturated, with a dummy for each value and all their interactions, because that model makes no linearity assumption (p. 166).

**(b)** applies when marginal effects are reported over a wide range of the moderator, especially when the treatment is concentrated in part of that range. Chapman (2009) and Clark and Golder (2006) are such cases; in the second, 59% of observations sit at a moderator value of zero, where the treatment does not vary (p. 178; p. 182). It stays silent when the manuscript reports effects only inside the bulk of the data and shows both groups there. In a randomized experiment, the treatment-variation part largely holds by design (this memo's reading), but thin tails still need checking: even in the authors' well-behaved case, Huddy, Mason, and Aarøe (2015), good support covered only about 0.3 to 1 on a 0-to-1 moderator (p. 176).

**(c)** applies to any manuscript in scope that shows neither LID plots nor box plots. Its tercile version applies only when both the treatment and the moderator are continuous (p. 170). It stays silent when both variables are binary or take only a few values, because the authors recommend a saturated model there (p. 166). Its linearity part also stays silent when a continuous-by-continuous design is shown with a GAM surface, which the authors offer as an alternative to the scatterplot (p. 190).

**(d)** applies when the manuscript draws its conclusions from the linear model's marginal-effect line. It stays silent when the conditional effect is already estimated without the linear form, for example by separate regressions for each tercile of the moderator, a GAM, or a kernel estimator. Binning itself works by fitting each bin separately (p. 171), and the authors do not criticize other flexible methods (p. 163, n. 1). In small samples, a modest gap between the bin estimates and the line is weak evidence, because flexible estimators are less efficient when the linear model is right (p. 170).

**(e)** applies only when kernel estimates are reported and a claim refers to a specific range of the moderator. It stays silent when the claim concerns only values where the intervals stay narrow. Wider intervals at the edges of the plot are expected, and they are not a flaw in themselves (p. 175).

**Does not apply to** identification. The authors state that following their guidelines "does not guarantee that the model will be correctly specified" (p. 187) and that the checks "cannot help with other common problems such as endogeneity or omitted variables" (p. 188). These checks should not be used to argue about whether the moderator is exogenous, and passing them does not make a conditional effect causal. They also do not apply to mediation analysis (p. 166, n. 6), or to regressions without an interaction term, even though the authors note that similar problems can arise there (p. 165).

**Partial application:** interactions in logit, probit, or other nonlinear models, and triple interactions. The replications covered only OLS and linear fixed-effects models and excluded triple interactions because they "impose even more demanding assumptions" (p. 175). Flag the concern, but do not assert that the diagnostics apply as they are.

## 5. What failure looks like

A manuscript rests its conclusion on one marginal-effect plot from the linear interaction model: a straight line with a confidence band that runs from the minimum to the maximum of the moderator. Neither the text nor the appendix shows an LID plot, box plots or a histogram of the moderator by treatment group, or binning or kernel estimates. The moderator is skewed, with most cases at one value or a long thin tail, yet the text interprets the effect in the thin part, for example by stating that the effect becomes significant only above some threshold. When binning estimates are reported, they sit off the line or rise and then fall, but the paper keeps the linear model. When kernel estimates are reported, the claim sits exactly where their intervals balloon.

## 6. Test cases

*(to be written)*
