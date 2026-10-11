# Multiplicative Interaction Models

**Full citation:** Hainmueller, J., Mummolo, J., & Xu, Y. (2019). How much should we trust estimates from multiplicative interaction models? Simple tools to improve empirical practice. *Political Analysis*, 27(2), 163–192. https://doi.org/10.1017/pan.2018.46

쪽수는 *Political Analysis* 출판본에 인쇄된 쪽수를 따른다.

## 1. What the paper establishes

*(작성 예정)*

## 2. Checks for a reviewer

**(a) 처치와 조절변수 중 적어도 하나가 연속인 상호작용에 실질적 주장을 거는 원고가, Brambor, Clark, and Golder(2006)의 권고를 지킨 것을 충분한 안전장치로 취급하는지 확인한다.** 구성항을 모두 넣고, 구성항 계수를 무조건적 효과로 읽지 않고, 선형 모형으로 계산한 한계효과와 신뢰구간을 그리는 것만으로는 이 논문이 다루는 두 문제를 드러낼 수 없다(p. 164). 두 문제란 처치 효과가 조절변수에 따라 일정한 비율로만 변한다는 선형 상호작용 효과(LIE) 가정의 위반, 그리고 효과를 보고하는 조절변수 구간에 관측치가 부족하거나 처치가 변하지 않는 공통 지지(common support)의 부족이다(pp. 164–165). 이런 원고에는 처치 집단별로 결과를 조절변수에 대해 그리고 선형 적합선과 LOESS 곡선을 겹친 원자료 진단 그림을 요구한다(p. 168).

**(b) 한계효과를 보고하는 조절변수 구간마다 관측치가 충분한지, 그리고 그 구간에서 처치가 실제로 변하는지 확인한다.** 그림 아래에 조절변수 분포가 있는지 보고, 이진 처치라면 처치 집단과 통제 집단의 분포가 나뉘어 있는지 확인한다. 없으면 요구한다. 집단을 합친 분포로는 둘째 조건을 판단하기 어렵다(p. 172 각주 19). 지지가 없는 구간의 효과는 데이터가 아니라 가정한 함수형이 만들어 낸 값이므로(p. 167, p. 178), 그 구간에 걸린 주장은 지지 범위 안으로 좁히라고 요구한다. 극단 관측치 몇 개를 뺐을 때 결론이 바뀌는지는 취약성 진단으로만 요구하고, 그 관측치를 빼는 것을 수정으로 요구하지 않는다(p. 181 각주 28).

**(c) 선형 한계효과선과 함께 유연한 추정치(조절변수 삼분위별 binning 추정치나 kernel 추정치)를 보고하는지 확인하고, 보고했다면 두 가지를 읽는다.** 첫째, 구간 추정치가 선형선에서 멀리 떨어지거나 비단조적이면 LIE 가정이 깨졌다는 증거로 읽는다(p. 173). 둘째, ‘효과가 조절변수에 따라 달라진다’는 주장이 상호작용 계수의 유의성만이 아니라 저값과 고값에서의 효과 차이 검정, 예컨대 하위 삼분위 중앙값과 상위 삼분위 중앙값에서의 효과 차이 검정으로 뒷받침되는지 확인한다(p. 183). 처치와 조절변수가 모두 연속이면 원자료 진단을 두 방향으로, 즉 조절변수가 주어졌을 때 처치의 효과와 처치가 주어졌을 때 조절변수의 효과 모두에 대해 요구한다(p. 187).

**(d) 결론이 어떤 형태로 서술되었는지 보고, 그 형태에 따라 결론이 어느 쪽으로 틀릴 수 있는지 확인한다.** 결론이 특정 조절변수 값에서의 효과, 예컨대 효과가 유의해지기 시작하는 문턱값이나 극단값에서의 효과 크기를 말한다면, 그 값 근처의 관측치 수와 처치 변이를 확인한다. 이 메모의 해석으로는, 이런 주장이 함수형 가정을 풀었을 때 유의성을 가장 먼저 잃는다. 반대 방향도 있다. 선형 상호작용항이 유의하지 않다는 이유로 효과가 조절변수에 따라 달라지지 않는다고 결론 내렸다면, 비단조적 이질성을 잡을 수 있는 유연한 추정이 있는지 확인한다. 약한 선형 상호작용 뒤에 강한 조건부 효과가 숨어 있을 수 있기 때문이다(p. 173). 다만 이 경우 검토자는 숨은 이질성을 단정하지 않고 가능성만 지적한다.

**(e) 이 논문의 진단을 채택한 원고가 선형성 Wald 검정에서 선형 모형을 기각하지 못한 결과를 LIE 가정이 성립한다는 증거로 쓰는지 확인한다(p. 183).** 표본이 작거나, 구간마다 관측치가 적거나, 조절변수가 치우쳐 있을 때 특히 그렇다. 그런 원고에는 binning 추정치가 선형선과 실제로 맞는지 보여 주는 그림을 함께 요구한다.

## 3. Evidence

**(a)의 근거.** 저자들은 Brambor, Clark, and Golder(2006)의 세 권고를 정리하고, 그 권고가 "nowadays often considered the best practice in political science"라고 쓴다(p. 164). 바로 뒤에서 그 지침이 놓치는 것을 지목한다: "two important problems that are currently often overlooked and not detected by scholars using the existing guidelines" (p. 164). 이 문장은 BCG를 지켰다는 사실이 두 문제에 대해 아무것도 보여 주지 않는다는 점을 직접 뒷받침한다. LIE 쪽은 같은 쪽에서 많은 결론이 "rest on a modeling artifact that goes undetected even when applying the current best practice guidelines"라고 한 번 더 말한다(p. 164). 공통 지지 쪽은 Chapman(2009) 재현에서 "The common practice of fitting the standard multiplicative interaction model and computing the conditional marginal effects from this model will not alert the researcher to this problem."이라고 쓴다(p. 178). 다만 이 문장의 ‘문제’는 공통 지지 부족을 가리키므로 LIE의 근거로 넓혀 쓰지 않는다. 요구할 진단에도 근거가 있다. 저자들이 권하는 첫 진단은 원자료 산점도이고(p. 168), 수정 체크리스트의 첫 항목도 원자료 진단 그림으로 선형 적합이 조건부 관계를 잘 근사하는지 확인하라는 것이다(p. 187).

**(b)의 근거.** 수정 체크리스트에서 저자들은 이렇게 권한다: "Researchers should avoid computing marginal effects in areas where the data is too sparse either because there are no observations for those values of the moderator or there is no variation in the treatment." (p. 187). 실패 조건 두 가지가 명시되어 있으므로, 검토자는 그림의 가로축 범위를 조절변수 분포와 맞대어 두 조건을 따로 판정할 수 있다. 집단별 분포를 요구하는 근거는 각주에 있다. 저자들은 Berry, Golder, and Milton(2012)의 분포 표시 권고에 더해 "in the case of a binary treatment it is advantageous to distinguish in the histogram between the two groups to get a better sense of the overlap across groups"라고 쓴다(p. 172 각주 19). 재현 사례는 둘째 조건이 실제로 깨지는 모습을 보여 준다. Chapman(2009)에서는 U.N. 승인이 있는 관측이 모두 조절변수의 최하위 삼분위에 있었고(p. 178), Clark and Golder(2006)에서는 조절변수의 59%가 0이었는데 그 값에서 처치가 변하지 않아 효과가 식별되지 않았다(p. 182). 검토자가 쓸 표현에도 근거가 있다. 모형이 우연히 맞는다면 지지가 없는 구간의 추정도 일치하고 불편하다(p. 167 각주 11). 따라서 그런 구간의 추정은 편향되었다고 하기보다, 가정한 함수형에 기대고 있어 "model dependent and fragile"하다고 써야 한다(p. 178). 주장을 지지 범위로 좁히라는 요구는 수정 체크리스트의 마지막 항목에서 나온다: "marginal effects should only be computed for areas with sufficient common support" (p. 187). 영향점에 대해서는, Malesky, Schuler, and Tran(2012)에서 관측의 0.9% 미만인 극단 영향점 네 개를 빼자 효과 추정치가 평평해졌다(p. 181). 그러나 저자들은 "we have no theoretical rationale to drop these data points. This is merely a robustness check"라고 밝힌다(p. 181 각주 28). 그래서 (b)는 영향점 제거를 수정이 아니라 진단으로만 요구한다.

**(c)의 근거.** 수정 체크리스트는 선형 모형을 쓸 조건을 이렇게 건다: "The standard linear interaction model and marginal-effect plots should only be used if the estimates from the binning and/or kernel estimator suggest that the interaction is really linear" (p. 187). 따라서 유연한 추정이 없는 원고는 이 조건을 충족했다는 것을 보여 주지 못한 것이다. 그림을 읽는 규칙도 저자들이 준다: "When the estimates from the binning estimator are far off the line or when they are non-monotonic, we have evidence that the LIE assumption does not hold." (p. 173). 둘째 질문은 저자들이 재현 사례를 채점한 첫째 기준에서 나온다. 저자들은 하위 삼분위 중앙값에서의 효과와 상위 삼분위 중앙값에서의 효과가 통계적으로 다른지 검정하고(p. 183), 이 기준을 이렇게 설명한다: "This criterion provides a formal test of the extent to which the data contains evidence of a significant interaction effect once we relax the stringent LIE assumption" (p. 183). 이 검정은 형식적 절차에 그치지 않는다. 저자들의 재현에서 약 70%의 사례가 LIE 가정을 풀자 전형적 저값과 고값에서 효과가 같다는 귀무가설을 기각하지 못했다(p. 164). 다만 이 수치는 문제의 규모를 보여 줄 뿐이므로 (c)의 직접 근거로는 p. 183의 정의를 쓴다. 두 방향 진단은 표준 모형이 두 방향 모두에 선형성을 가정하므로 원자료 진단 그림을 두 방향으로 그리라는 권고에서 나온다(p. 187).

**(d)의 근거.** 첫째 질문의 근거는 저자들의 관행 비판이다. 저자들은 많은 연구자가 선형 모형을 참 모형처럼 다룬다고 비판하면서, 그런 연구자들이 평균적 결론을 넘어 "instead claim to have estimated the marginal effect of the treatment at specific values of the moderator, interpretations which rely heavily on the linear functional form being correct"라고 쓴다(p. 165, 문장은 p. 164에서 시작한다). 이 인용은 검토자가 찾을 문장 형태와 그 주장이 무엇에 기대는지를 함께 보여 준다. Malesky, Schuler, and Tran(2012) 재현이 구체적인 모습을 보여 준다: "there are very few observations which exhibit levels of Internet penetration higher than about 2.5, which is the point above which the effect of the transparency intervention starts to become significant according to the original model" (p. 181). 유연한 추정에서는 지지가 희박한 구간의 신뢰구간이 넓어지는데, 저자들은 이것을 "desirable because it makes clear the increasing lack of common support"라고 평가한다(p. 175). Chapman 재현에서도 같은 모습이 나타난다(p. 178). 이 문장들에서 ‘특정 값의 주장은 유의성을 잃는 쪽으로 움직인다’는 방향을 끌어낸 것은 이 메모의 해석이며, 저자들이 일반 명제로 쓰지는 않았다. 둘째 질문의 근거는 시뮬레이션이다. 진짜 한계효과가 이차 함수인 자료(p. 168)에서 "the standard linear model indicates a slightly negative, but overall very weak, interaction effect, whereas the binning estimates reveal that the effect of D is actually strongly conditioned by X"라는 결과가 나온다(p. 173). 저자들은 효과가 "nonlinear or nonmonotonic"일 수 있다고 본다(p. 166). 그러나 근거가 시뮬레이션 하나뿐이고, 재현 표본은 상호작용을 주장한 연구만 골랐다(p. 175). 그래서 실제 원고에서 선형 상호작용의 비유의성이 이질성을 얼마나 자주 가리는지는 이 논문으로 알 수 없으며, (d)는 가능성 지적에서 멈춘다.

**(e)의 근거.** 저자들은 binning 모형이 선형 모형을 특수한 경우로 품도록 다시 쓴 뒤, 추가된 여덟 개 모수가 모두 0이라는 귀무가설을 Wald 검정으로 검정한다(p. 183). 그러면서 이 귀무가설을 기각하지 못한 것이 "does not necessarily mean that the LIE assumption holds, especially when the sample size is small and the test is underpowered"라고 경고하고, 그래서 자신들의 코딩을 "lenient"하다고 부른다(p. 183). 같은 검정을 쓴 원고가 기각 실패를 선형성의 증명으로 내세운다면, 저자들이 스스로 경고한 추론을 그대로 하는 셈이다.

## 4. Scope

**공통 적용 범위.** 다섯 항목은 세 조건을 모두 갖춘 원고에서만 발동한다. 처치와 조절변수 중 적어도 하나가 연속이고, 원고의 실질적 주장이 상호작용, 즉 처치 효과가 조절변수에 따라 달라진다는 데 걸려 있으며, 그 효과를 OLS나 선형 고정효과 모형의 곱셈 상호작용으로 추정한 경우다. 이 조건은 저자들이 기존 지침의 공백을 지목한 경우(p. 164)이자 재현 표본의 선정 기준(p. 175)과 같다. 처치와 조절변수의 구분은 임의적이므로(p. 166 각주 7), 연속인 쪽을 조절변수로 놓고 읽는다. 각 항목은 이 안에서 따로 더 좁은 조건을 갖는다.

**(a).** 원고가 상호작용 주장의 근거로 구성항 포함과 선형 한계효과 그림만 제시할 때 발동한다. 원고가 이미 원자료 진단 그림이나 유연한 추정(삼분위별 분할 추정 포함)을 보고했다면 (a)는 침묵하고, 그 결과를 읽는 일은 (b)와 (c)가 맡는다. 상호작용항이 통제 목적이거나 강건성 표의 한 열로만 나오고 그 위에 실질적 주장이 없을 때도 침묵한다.

**(b).** 한계효과를 조절변수의 넓은 범위, 흔히 최솟값에서 최댓값까지 보고하면서, 조절변수가 치우쳐 있거나 처치가 조절변수와 얽혀 일부 구간에 한 집단이 거의 없을 수 있을 때 발동한다. 재현 사례 가운데 Chapman(2009)과 Clark and Golder(2006)가 그런 경우였다(p. 178, p. 182). 한계효과를 지지 범위 안에서만 그리고 집단별 분포를 함께 보여 준 원고에서는 침묵한다. 조절변수의 L-첨도가 0.16을 넘는지로 발동을 판정하지는 않는다. 그것은 저자들이 재현 사례를 코딩할 때 쓴 기준이지 일반 기준이 아니다(p. 183 각주 33). 부분 적용(이 메모의 해석): 처치가 조절변수와 무관하게 무작위 배정된 실험에서는 처치 변이 조건이 설계상 대체로 충족되므로 희박한 꼬리만 점검한다. 그렇다고 꼬리 점검까지 생략하지는 않는다. 저자들이 가정이 잘 성립한 사례로 든 Huddy, Mason, and Aarøe(2015)도 설문 실험이었지만, 충분한 지지는 0~1 척도의 약 0.3~1 범위에만 있었다(p. 176).

**(c).** 조절변수가 연속이거나 값이 여러 개인 순서형인데 선형항으로 들어가 있고, 조건부 효과를 선형 상호작용 모형 하나로만 추정했으며, 주장이 효과가 변하는 방향이나 크기에 걸려 있을 때 발동한다. 원고가 이미 구간별 분할 추정, GAM, kernel, 기계학습 방법으로 이질성을 추정했다면 첫째 질문(선형성)은 침묵한다. binning은 구간마다 상호작용 구성요소를 따로 적합해 LIE 가정을 완화하는 방법이고(p. 171), 저자들은 다른 유연한 방법을 비판할 의도가 없다고 밝히며(p. 163 각주 1) 기계학습 방법도 대안으로 든다(p. 187). 이때도 둘째 질문은 그 결과가 저값과 고값의 차이를 실제로 보여 주는지 읽는다. 둘째 질문은 주장이 ‘효과가 조절변수에 따라 다르다’가 아니라 ‘모든 수준에서 효과가 양(+)이다’ 같은 형태일 때 침묵한다. 부분 적용: 표본이 작아 구간마다 관측치가 적으면, 구간 추정치가 흔들리는 것을 곧바로 LIE 위반으로 읽지 않는다. 유연한 추정은 LIE가 맞을 때 선형 모형보다 덜 효율적이고, 구간을 늘리려면 관측치가 충분해야 한다(p. 170). 이때는 진단을 요구하되 판정은 유보한다.

**(d).** 첫째 질문은 초록이나 결론이 특정 조절변수 값이나 구간에서의 효과를 서술하고, 그 값이 분포의 꼬리나 처치 변이가 적은 구간에 있을 때 발동한다. 둘째 질문은 결론이 선형 상호작용항의 비유의성에 기대어 조건부 가설을 기각하거나 효과가 동질적이라고 주장하면서 유연한 추정이 없을 때 발동한다. 주장이 평균적 기울기 수준, 예컨대 ‘대체로 조절변수가 클수록 효과가 크다’에 머물면 첫째 질문은 침묵한다. 저자들도 회귀를 "a linear approximation for the unknown true model"로 쓸 수 있다고 인정한다(p. 164). 그런 평균적 주장 자체는 (c)의 저값·고값 차이 검정으로 따진다. 비유의 결과를 보고만 하고 동질성을 결론으로 쓰지 않으면 둘째 질문은 침묵한다. 부분 적용: 유연한 추정은 선형 모형보다 덜 효율적이므로(p. 170), 표본이 작을 때 둘째 질문을 숨은 이질성이 있다는 단정으로 바꾸지 않는다.

**(e).** 원고가 이 논문의 진단을 쓰고, 선형성 검정을 기각하지 못한 것을 근거로 선형 모형을 유지하며, 표본이 작거나 구간마다 관측치가 적거나 조절변수가 치우쳐 있을 때 발동한다. 진단을 쓰지 않은 원고는 (a)와 (c)의 영역이고, 검정이 선형성을 기각한 원고는 (c)의 영역이므로 (e)는 침묵한다. 구간 추정치가 선형선 위에 놓인다는 것을 그림으로도 보여 준 원고에서도 침묵한다. 그때 검정은 유일한 근거가 아니기 때문이다. 이 메모의 해석으로는, 큰 표본에서 구간 추정치가 좁은 신뢰구간으로 선형선 위에 놓인다면 "especially when the sample size is small"이라는 저자 경고(p. 183)의 무게가 약하다. 부분 적용: 저자 경고는 자신들의 Wald 검정에 대한 것이므로(p. 183), 이차항 추가 같은 다른 선형성 검정에 같은 논리를 적용할 때는 유추라고 밝힌다.

**모든 항목이 침묵하는 인접 사례.** 처치와 조절변수가 둘 다 이진이거나 값이 몇 개 안 되는 범주라면, 저자들은 범주마다 더미를 두고 모든 상호작용을 넣은 완전 포화 모형을 쓰라고 한다(p. 166). 포화 모형에는 LIE 가정이 없으므로, 2×2 요인 실험 같은 설계에서는 다섯 항목이 모두 침묵한다. 매개 분석에서도 침묵한다. 저자들은 조절변수와 매개변수를 구분한다(p. 166 각주 6). 상호작용이 없는 회귀에서도 침묵한다. 저자들은 함수형 오설정과 공통 지지 문제가 상호작용 없는 회귀에도 있다고 하지만(p. 165), 이 메모의 항목은 조건부 한계효과의 추정과 해석에 대한 것이다.

**저자들이 밝힌 한계에서 나오는 경계.** 가장 날카로운 경계는 결론 단락에 있다. 저자들은 수정 지침을 따라도 "does not guarantee that the model will be correctly specified"라고 쓰고(p. 187), 진단이 "cannot help with other common problems such as endogeneity or omitted variables"라고 밝힌다(p. 188). 따라서 이 메모의 항목을 조절변수의 외생성이나 상호작용의 인과적 해석을 문제 삼는 데 쓰지 않는다. 반대로 다섯 항목을 모두 통과한 원고를 모형이 맞거나 효과가 식별된 것으로 읽지도 않는다. 저자들은 공변량이 정확히 명세되었다고 가정하므로(p. 166), 공변량의 함수형 문제도 이 메모의 영역이 아니다.

**부분 적용: 비선형 모형과 삼중 상호작용.** 저자들의 재현 표본은 OLS와 선형 고정효과 모형만 포함했고, 삼중 상호작용은 "even more demanding assumptions"를 이유로 뺐다(p. 175). 로짓이나 프로빗 같은 비선형 모형의 상호작용, 그리고 삼중 상호작용에서는 우려를 제기하되 이 논문의 진단과 추정량이 그대로 적용된다고 단정하지 않는다.

## 5. What failure looks like

원고는 연속 조절변수와의 상호작용에서 실질적 결론을 끌어내면서, 방법 절에서는 Brambor, Clark, and Golder(2006)를 따라 구성항을 모두 넣었다는 점만 안전장치로 밝힌다. 근거는 선형 상호작용 모형으로 계산한 한계효과 그림 하나다. 그림의 한계효과선은 조절변수의 최솟값에서 최댓값까지 이어지는 곧은 직선인데, 이 직선 모양은 데이터가 아니라 모형이 정한 것이다(p. 166의 식 (2)). 그림 아래에는 조절변수 분포가 없거나, 처치 집단과 통제 집단을 합친 러그 플롯만 있다. 결론 문장은 특정 값에서의 효과를 말한다. 효과가 어떤 문턱값을 넘어야 유의해진다거나, 조절변수가 가장 클 때 효과가 가장 크다는 식이다. 그러나 그 구간에 관측치가 몇 개인지, 처치 집단과 통제 집단이 둘 다 있는지는 본문에도 부록에도 없다. 처치 집단별 원자료 산점도, 삼분위 binning 추정치, kernel 추정치, 저값·고값 효과 차이 검정, 극단 관측치를 뺀 결과도 없다. 저자들이 재현한 Malesky, Schuler, and Tran(2012)에서는 이 문제가 수치로 드러난다. 조절변수 밀도의 약 80%가 한계효과를 그린 범위의 11%에 몰려 있었고(p. 183 각주 33), 음(-)의 상호작용 주장을 떠받친 하향 기울기는 두 대도시권의 극단값이 만들었다(p. 181).

실패는 반대 방향으로도 나타난다. 상호작용항이 유의하지 않다는 회귀표 한 줄을 근거로 ‘효과는 조절변수와 무관하다’고 결론 내리면서, 구간별 추정은 보여 주지 않는 원고다. 이 논문의 진단을 채택한 원고에서는 실패가 또 다른 모습을 띤다. 선형성 Wald 검정의 p값만 보고하고 ‘선형성이 확인되었다’고 쓰지만, 표본이 작은데도 구간 추정치를 선형선 위에 겹친 그림은 없다.

## 6. Test cases

*(작성 예정)*
