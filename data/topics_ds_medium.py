# Data Science Medium Questions (25 questions)

QUESTIONS = [{'topic_tag': 'Hypothesis Testing Framework',
  'question': 'Explain the step-by-step hypothesis testing process: defining H0/H1, selecting alpha, computing test '
              'statistics, and evaluating p-values.',
  'keywords': ['Hypothesis Testing',
               'Null Hypothesis H0',
               'Alternative Hypothesis H1',
               'p-value',
               'Significance Level Alpha',
               'Test Statistic',
               'Rejection Region'],
  'expected_concepts': ['Formulating mutually exclusive hypotheses: Null (H0: no effect or difference) versus '
                        'Alternative (H1: presence of effect/difference)',
                        'Setting significance level alpha (typically 0.05) representing threshold probability of '
                        'committing a Type I error',
                        'Calculating the test statistic (Z, t, F, or chi-square) based on sample data and underlying '
                        'sampling distribution',
                        'Comparing p-value to alpha (or test statistic to critical value): reject H0 if p <= alpha; '
                        'fail to reject H0 if p > alpha'],
  'model_answer': 'Classical frequentist hypothesis testing follows a systematic four-step procedure: 1) Formulate '
                  'hypotheses: establish the Null Hypothesis H0 representing the status quo or absence of effect, and '
                  'the Alternative Hypothesis H1 representing the hypothesized effect or difference; 2) Determine the '
                  'significance level alpha (conventionally 0.05 or 0.01), which defines the acceptable probability of '
                  'committing a Type I error (falsely rejecting a true H0); 3) Compute the appropriate test statistic '
                  '(such as a t-statistic or z-score) that quantifies how far sample observations deviate from the '
                  'null expectation relative to standard error; and 4) Decision rule: calculate the p-value—the '
                  'probability of observing a test statistic as extreme as or more extreme than the observed value '
                  'assuming H0 is true. If p <= alpha, we reject H0 in favor of H1; if p > alpha, we fail to reject '
                  'H0, concluding there is insufficient statistical evidence to claim an effect.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'Hypothesis testing follows four distinct steps. First, you state your null '
                                     'hypothesis H0, which assumes no effect or no difference, and your alternative '
                                     "hypothesis H1, which is the effect you're trying to prove. Second, you choose "
                                     'your significance level alpha—usually 0.05—which fixes your tolerance for false '
                                     'positives. Third, you collect your sample and compute a test statistic, like a '
                                     't-statistic or z-score, measuring how many standard errors your sample is from '
                                     'what the null predicts. Fourth, you calculate the p-value, which is the '
                                     'probability of seeing data this extreme purely by chance under H0. If the '
                                     "p-value is less than or equal to alpha, you reject the null hypothesis; if it's "
                                     "greater, you fail to reject H0 because there isn't enough evidence.",
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'You start by defining the null hypothesis H0 as no change, and the alternative '
                                     'hypothesis H1 as having a significant difference. Then you pick a significance '
                                     'level alpha, usually 0.05. Next, you calculate the test statistic like a t-score '
                                     'from your sample data, and find the corresponding p-value. If the p-value is '
                                     'smaller than alpha, you reject H0 and say the result is statistically '
                                     'significant.',
                      'missing_concepts': ['Setting significance level alpha (typically 0.05) representing threshold '
                                           'probability of committing a Type I error']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Hypothesis testing is checking if your test result is real. You set H0 to be no '
                                     'effect and H1 to be an effect. Then you calculate a p-value using a t-test. If '
                                     'the p-value is less than 0.05, that means your result is statistically '
                                     'significant and you accept the alternative hypothesis.',
                      'missing_concepts': ['Setting significance level alpha (typically 0.05) representing threshold '
                                           'probability of committing a Type I error',
                                           'Comparing p-value to alpha (or test statistic to critical value): reject '
                                           'H0 if p <= alpha; fail to reject H0 if p > alpha']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'Hypothesis testing is when an AI model guesses the target labels on an '
                                     'unlabelled dataset, and the p-value is the percentage of correct predictions.',
                      'missing_concepts': ['Formulating mutually exclusive hypotheses: Null (H0: no effect or '
                                           'difference) versus Alternative (H1: presence of effect/difference)',
                                           'Setting significance level alpha (typically 0.05) representing threshold '
                                           'probability of committing a Type I error',
                                           'Calculating the test statistic (Z, t, F, or chi-square) based on sample '
                                           'data and underlying sampling distribution',
                                           'Comparing p-value to alpha (or test statistic to critical value): reject '
                                           'H0 if p <= alpha; fail to reject H0 if p > alpha']}]},
 {'topic_tag': 'Type I vs Type II Errors & Statistical Power',
  'question': 'Distinguish between Type I (Alpha) and Type II (Beta) errors, and explain how statistical power (1 - '
              'Beta) relates to sample size and effect size.',
  'keywords': ['Type I Error', 'Type II Error', 'Alpha', 'Beta', 'Statistical Power', 'Sample Size', 'Effect Size'],
  'expected_concepts': ['Type I error (alpha): False Positive—rejecting a true null hypothesis when no true effect '
                        'exists',
                        'Type II error (beta): False Negative—failing to reject a false null hypothesis when a true '
                        'effect actually exists',
                        'Statistical Power (1 - beta): probability of correctly rejecting H0 when H1 is true '
                        '(detecting a true effect)',
                        "Power increases with larger sample size n, larger true effect size (Cohen's d), and higher "
                        'allowable alpha, but decreases with increased measurement variance'],
  'model_answer': 'In statistical decision theory, Type I and Type II errors capture the two modes of inferential '
                  'failure. A Type I error (probability alpha) is a false positive: rejecting the null hypothesis when '
                  'H0 is actually true (e.g., convicting an innocent defendant or rolling out an ineffective feature). '
                  'A Type II error (probability beta) is a false negative: failing to reject H0 when H0 is false and a '
                  'true effect exists (e.g., failing to detect a cure). Statistical power is defined as 1 - beta: the '
                  'probability of correctly detecting a genuine effect. Power is governed by four interconnected '
                  "parameters: sample size n, true effect size (e.g., Cohen's d), significance threshold alpha, and "
                  'data variance. Increasing sample size narrows the standard error, which directly amplifies '
                  'statistical power without requiring an inflation of Type I error risk.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'Type I error, or alpha, is a false positive—you reject the null hypothesis even '
                                     'though there was actually no effect. Type II error, or beta, is a false '
                                     'negative—you fail to detect an effect that actually exists. Statistical power is '
                                     '1 minus beta, which is your probability of correctly finding a real effect when '
                                     'one exists. Power depends heavily on sample size, effect size, and alpha. If the '
                                     'true effect size is tiny, you need a massive sample size to detect it with high '
                                     'power. Increasing your sample size shrinks standard error and moves the sampling '
                                     'distributions apart, which increases power without inflating your false positive '
                                     'rate.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 83,
                      'answer_text': 'Type I error is a false positive where you say an experiment worked when it '
                                     "didn't, set by alpha (usually 5%). Type II error is a false negative where an "
                                     'effect exists but your test failed to catch it, set by beta. Statistical power '
                                     'is 1 minus beta, usually targeted at 80%. You increase power by increasing your '
                                     'sample size or if the underlying effect size is larger.',
                      'missing_concepts': ['Power increases with larger sample size n, larger true effect size '
                                           "(Cohen's d), and higher allowable alpha, but decreases with increased "
                                           'measurement variance']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Type 1 error is false positive and Type 2 error is false negative. Power is 1 '
                                     'minus beta, which means how accurate your test is at finding an effect. If you '
                                     'have more sample size, you have more power in your test.',
                      'missing_concepts': ['Type II error (beta): False Negative—failing to reject a false null '
                                           'hypothesis when a true effect actually exists',
                                           'Power increases with larger sample size n, larger true effect size '
                                           "(Cohen's d), and higher allowable alpha, but decreases with increased "
                                           'measurement variance']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'Type 1 error occurs in Python code, and Type 2 error occurs in SQL queries. '
                                     'Statistical power is the speed of your GPU clock frequency.',
                      'missing_concepts': ['Type I error (alpha): False Positive—rejecting a true null hypothesis when '
                                           'no true effect exists',
                                           'Type II error (beta): False Negative—failing to reject a false null '
                                           'hypothesis when a true effect actually exists',
                                           'Statistical Power (1 - beta): probability of correctly rejecting H0 when '
                                           'H1 is true (detecting a true effect)',
                                           'Power increases with larger sample size n, larger true effect size '
                                           "(Cohen's d), and higher allowable alpha, but decreases with increased "
                                           'measurement variance']}]},
 {'topic_tag': 'A/B Testing Methodology & Sample Size',
  'question': 'How do you determine the required sample size for an A/B test given alpha, beta, baseline conversion '
              'rate, and Minimum Detectable Effect (MDE)?',
  'keywords': ['A/B Testing',
               'Sample Size Calculation',
               'Minimum Detectable Effect (MDE)',
               'Baseline Conversion Rate',
               'Power Analysis',
               'Randomization'],
  'expected_concepts': ['Sample size formula relies on alpha (significance), beta (1 - power), baseline rate p, and '
                        'MDE (delta)',
                        'Smaller MDE requires quadratically larger sample sizes (n proportional to 1 / delta^2) to '
                        'achieve statistical power',
                        'Variance of binary metrics is p * (1 - p); highest required sample sizes occur when baseline '
                        'conversion p is around 0.5',
                        'Stopping rules: peeking at p-values and stopping early without pre-determined sample size '
                        'inflates Type I error'],
  'model_answer': 'Determining sample size for an online A/B test requires an a priori power calculation balancing '
                  'four inputs: 1) Type I error rate alpha (typically 0.05, two-tailed z-score 1.96); 2) Statistical '
                  'power 1 - beta (typically 0.80, z-score 0.84); 3) Baseline metric variance (for proportions, '
                  'sigma^2 = p * (1 - p)); and 4) Minimum Detectable Effect (MDE, delta)—the smallest relative or '
                  'absolute lift practically meaningful to the business. The mathematical formula scales inversely '
                  'with the square of MDE: n approx 2 * (Z_alpha/2 + Z_beta)^2 * p * (1 - p) / delta^2. Because sample '
                  'size scales as 1/delta^2, detecting a subtle 1% relative lift requires roughly 100 times more '
                  'traffic than detecting a 10% lift. Pre-computing sample size is mandatory to enforce experiment run '
                  "duration and prevent the 'peeking problem', where continuously checking p-values inflates false "
                  'positives.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'To size an A/B test, you need four key parameters: your significance level alpha '
                                     '(usually 5%), desired statistical power 1 - beta (typically 80%), baseline '
                                     'metric variance (for conversion rates, p times 1 - p), and your Minimum '
                                     'Detectable Effect (MDE). The math shows that required sample size scales '
                                     'inversely with the square of the MDE (delta^2). So if you cut your MDE in half '
                                     'to catch a subtle change, you need four times the traffic. Pre-calculating this '
                                     'sample size determines your required test duration. Crucially, you must commit '
                                     'to this sample size upfront; if you peek at intermediate p-values and stop early '
                                     'as soon as p < 0.05, you severely inflate your false positive rate.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'To calculate sample size, you input alpha (usually 0.05), beta (0.2 for 80% '
                                     'power), the baseline conversion rate, and the MDE. MDE is the smallest '
                                     'improvement that matters to the business. The smaller the MDE you want to '
                                     'detect, the exponentially larger your sample size needs to be. Once you know the '
                                     'total sample size, you divide by daily traffic to find how many days to run the '
                                     'test.',
                      'missing_concepts': ['Stopping rules: peeking at p-values and stopping early without '
                                           'pre-determined sample size inflates Type I error']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'You use an online sample size calculator where you put in your baseline '
                                     'conversion rate, the minimum detectable effect, 95% confidence, and 80% power. '
                                     'It gives you the number of users needed per variant. If you want to detect a '
                                     'small change, you need more users.',
                      'missing_concepts': ['Smaller MDE requires quadratically larger sample sizes (n proportional to '
                                           '1 / delta^2) to achieve statistical power',
                                           'Stopping rules: peeking at p-values and stopping early without '
                                           'pre-determined sample size inflates Type I error']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'Sample size in A/B testing is always fixed at 1,000 users per group. You stop '
                                     'the experiment immediately as soon as variant B shows higher revenue than '
                                     'variant A.',
                      'missing_concepts': ['Sample size formula relies on alpha (significance), beta (1 - power), '
                                           'baseline rate p, and MDE (delta)',
                                           'Smaller MDE requires quadratically larger sample sizes (n proportional to '
                                           '1 / delta^2) to achieve statistical power',
                                           'Variance of binary metrics is p * (1 - p); highest required sample sizes '
                                           'occur when baseline conversion p is around 0.5',
                                           'Stopping rules: peeking at p-values and stopping early without '
                                           'pre-determined sample size inflates Type I error']}]},
 {'topic_tag': 'Chi-Square Test vs ANOVA',
  'question': 'When would you choose a Chi-Square Test for Independence versus a One-Way ANOVA?',
  'keywords': ['Chi-Square Test',
               'ANOVA',
               'Categorical vs Continuous',
               'F-statistic',
               'Contingency Table',
               'Observed vs Expected'],
  'expected_concepts': ['Chi-Square Test of Independence tests association between two categorical variables (e.g., '
                        'device type vs subscription status)',
                        'One-Way ANOVA tests difference in means of a continuous numerical dependent variable across '
                        'three or more categorical groups',
                        'Chi-Square compares observed counts against expected counts across contingency table cells '
                        'using sum((O - E)^2 / E)',
                        'ANOVA partitions total sum of squares into Between-Group and Within-Group variance, using the '
                        'F-statistic ratio (MSB / MSW)'],
  'model_answer': 'The choice between a Chi-Square Test of Independence and a One-Way Analysis of Variance (ANOVA) is '
                  'determined by variable measurement types. Use a Chi-Square Test of Independence when analyzing the '
                  'relationship between two categorical variables (e.g., browser type: Chrome/Safari/Firefox versus '
                  'purchase status: Converted/Dropped). It evaluates whether observed frequencies in a contingency '
                  'table deviate significantly from expected frequencies under independence: sum((O - E)^2 / E). In '
                  'contrast, use a One-Way ANOVA when comparing the means of a continuous numerical dependent variable '
                  'across three or more independent categorical groups (e.g., average transaction amount across '
                  'Bronze, Silver, and Gold tiers). ANOVA calculates an F-statistic that contrasts between-group '
                  'variance against within-group variance (MSB / MSW); a significant F-test indicates at least one '
                  'group mean differs.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'The fundamental difference is in the data types. You use a Chi-Square Test for '
                                     'Independence when both variables are categorical—like comparing customer segment '
                                     '(Free, Tier 1, Tier 2) against churn status (Yes/No). It builds a contingency '
                                     'table and compares observed cell frequencies against expected frequencies using '
                                     '(O-E)^2/E. You use a One-Way ANOVA when you have a continuous numerical outcome '
                                     'compared across three or more categorical groups—for example, comparing average '
                                     'session duration across three different website layouts. ANOVA partitions '
                                     'variance into between-group and within-group sum of squares to compute an '
                                     'F-statistic.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'Chi-Square is for two categorical variables, checking if there is a dependency '
                                     'between them—like user gender and product choice—by comparing observed vs '
                                     'expected counts. ANOVA is used when your outcome is a continuous number and you '
                                     'want to compare the means across 3 or more groups, like comparing average test '
                                     'scores across three schools. ANOVA gives you an F-statistic.',
                      'missing_concepts': ['ANOVA partitions total sum of squares into Between-Group and Within-Group '
                                           'variance, using the F-statistic ratio (MSB / MSW)']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Chi-Square is for categorical tables and counts. ANOVA is used for comparing '
                                     'averages across more than two groups. If you only had two groups you would use a '
                                     't-test instead of ANOVA.',
                      'missing_concepts': ['Chi-Square compares observed counts against expected counts across '
                                           'contingency table cells using sum((O - E)^2 / E)',
                                           'ANOVA partitions total sum of squares into Between-Group and Within-Group '
                                           'variance, using the F-statistic ratio (MSB / MSW)']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'Chi-Square is a machine learning classifier, and ANOVA is an unsupervised '
                                     'clustering algorithm like K-Means.',
                      'missing_concepts': ['Chi-Square Test of Independence tests association between two categorical '
                                           'variables (e.g., device type vs subscription status)',
                                           'One-Way ANOVA tests difference in means of a continuous numerical '
                                           'dependent variable across three or more categorical groups',
                                           'Chi-Square compares observed counts against expected counts across '
                                           'contingency table cells using sum((O - E)^2 / E)',
                                           'ANOVA partitions total sum of squares into Between-Group and Within-Group '
                                           'variance, using the F-statistic ratio (MSB / MSW)']}]},
 {'topic_tag': "Student's T-Test Variants",
  'question': 'Compare One-Sample, Independent Two-Sample, and Paired T-Tests in terms of assumptions, sample '
              'independence, and practical use cases.',
  'keywords': ['T-Test',
               'One-Sample T-Test',
               'Independent T-Test',
               'Paired T-Test',
               'Sample Independence',
               'Within-Subject Design'],
  'expected_concepts': ['One-Sample T-Test compares a single sample mean against a known hypothetical population '
                        'benchmark value (mu_0)',
                        'Independent Two-Sample T-Test compares means of two mutually exclusive, unrelated groups '
                        '(e.g., Control vs Treatment group in A/B testing)',
                        'Paired T-Test (Dependent) compares two measurements taken on the exact same subjects (e.g., '
                        'Pre-test vs Post-test within-subject design), controlling for subject variance',
                        'Assumptions include approximate normality of differences/data and continuous scale (with '
                        "Welch's correction used when variances are unequal)"],
  'model_answer': "The Student's t-test family compares means when population variance is unknown, categorized by "
                  "sample structure: 1) One-Sample T-Test assesses whether a single sample's mean deviates "
                  'significantly from a known constant or historical benchmark (e.g., verifying whether average '
                  'battery life meets a claimed 24-hour specification); 2) Independent Two-Sample T-Test compares '
                  'means of two unrelated cohorts where observations in group A are completely independent of group B '
                  '(e.g., A/B test comparing conversion values between control and treatment users); and 3) Paired '
                  '(Dependent) T-Test analyzes paired observations where two measurements are gathered from the exact '
                  'same subjects (e.g., patient blood pressure before and after administering medication). Paired '
                  'tests compute differences within each subject (d_i = x_after - x_before), effectively controlling '
                  'for between-subject baseline variance and dramatically increasing statistical power.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'A One-Sample T-Test checks if the mean of a single group differs from a known '
                                     'benchmark, like testing if a manufacturing batch has an average weight of 500 '
                                     'grams. An Independent Two-Sample T-Test compares two completely separate, '
                                     'independent groups, like an A/B test between new versus existing landing page '
                                     'visitors. A Paired T-Test compares two related measurements on the same '
                                     'subjects, such as a before-and-after drug trial where each patient has a '
                                     'baseline and follow-up reading. The paired test is statistically more powerful '
                                     'because it calculates differences per subject, subtracting out individual '
                                     'variation.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'One-sample compares one group to a fixed benchmark number. Independent '
                                     'two-sample compares two different groups of people, like control and treatment. '
                                     'Paired t-test is used when the same person is measured twice, like before and '
                                     'after a training program. Paired tests remove the baseline noise of the '
                                     'individuals.',
                      'missing_concepts': ['Assumptions include approximate normality of differences/data and '
                                           "continuous scale (with Welch's correction used when variances are "
                                           'unequal)']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'One-sample is testing one mean. Independent t-test is for two different groups. '
                                     'Paired t-test is for before and after data. You use them when sample size is '
                                     'small and data is normal.',
                      'missing_concepts': ['One-Sample T-Test compares a single sample mean against a known '
                                           'hypothetical population benchmark value (mu_0)',
                                           'Paired T-Test (Dependent) compares two measurements taken on the exact '
                                           'same subjects (e.g., Pre-test vs Post-test within-subject design), '
                                           'controlling for subject variance']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'T-tests are used to test if SQL queries are running within memory limits. '
                                     'One-sample tests one table, two-sample tests two tables, and paired t-test tests '
                                     'foreign key constraints.',
                      'missing_concepts': ['One-Sample T-Test compares a single sample mean against a known '
                                           'hypothetical population benchmark value (mu_0)',
                                           'Independent Two-Sample T-Test compares means of two mutually exclusive, '
                                           'unrelated groups (e.g., Control vs Treatment group in A/B testing)',
                                           'Paired T-Test (Dependent) compares two measurements taken on the exact '
                                           'same subjects (e.g., Pre-test vs Post-test within-subject design), '
                                           'controlling for subject variance',
                                           'Assumptions include approximate normality of differences/data and '
                                           "continuous scale (with Welch's correction used when variances are "
                                           'unequal)']}]},
 {'topic_tag': 'SQL Window Functions Mechanics',
  'question': 'How do SQL window functions (ROW_NUMBER, RANK, DENSE_RANK) calculate rankings across partitions without '
              'collapsing rows?',
  'keywords': ['Window Functions',
               'ROW_NUMBER()',
               'RANK()',
               'DENSE_RANK()',
               'OVER Clause',
               'PARTITION BY',
               'Ties Handling'],
  'expected_concepts': ['Window functions perform calculations across a set of table rows related to the current row '
                        'without collapsing rows into a single group like GROUP BY',
                        'OVER (PARTITION BY ... ORDER BY ...) defines the window slice and ordering per partition',
                        'ROW_NUMBER assigns strictly sequential unique integers (1, 2, 3, 4) arbitrarily breaking ties',
                        'RANK assigns identical ranks to ties and skips subsequent numbers (1, 2, 2, 4); DENSE_RANK '
                        'assigns identical ranks to ties without skipping numbers (1, 2, 2, 3)'],
  'model_answer': 'SQL window functions compute aggregations, rankings, and cumulative totals over an explicit subset '
                  'of rows—termed a window frame—defined by the OVER() clause, while preserving individual row '
                  'identities rather than collapsing them like GROUP BY. The PARTITION BY clause divides data into '
                  'independent partitions, and ORDER BY dictates the evaluation sequence within each partition. When '
                  'ranking records with identical values (ties): 1) ROW_NUMBER() assigns strictly distinct, sequential '
                  'integers (1, 2, 3, 4) regardless of ties; 2) RANK() assigns identical rank numbers to matching '
                  'ties, but leaves gaps in subsequent numbering reflecting the number of tied rows (e.g., 1, 2, 2, '
                  '4); and 3) DENSE_RANK() assigns identical rank numbers to ties without creating gaps in subsequent '
                  'numbers (e.g., 1, 2, 2, 3).',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'Unlike GROUP BY, which collapses multiple rows into a single aggregated summary '
                                     'row, window functions compute metrics across a slice of rows while keeping every '
                                     'original row in the output. You define the window using the OVER clause with '
                                     'PARTITION BY to group rows and ORDER BY to sort them. The distinction between '
                                     'the three ranking functions is how they handle ties: ROW_NUMBER gives every row '
                                     'a unique consecutive integer (1, 2, 3, 4) even if values are identical. RANK '
                                     'gives identical values the same rank but skips subsequent numbers—so a tie for '
                                     'second yields 1, 2, 2, 4. DENSE_RANK also gives identical values the same rank '
                                     'but does not skip numbers, producing 1, 2, 2, 3.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'Window functions use the OVER clause with PARTITION BY and ORDER BY. Unlike '
                                     "GROUP BY, they don't collapse rows. ROW_NUMBER assigns 1, 2, 3, 4 sequentially. "
                                     'RANK gives ties the same number but skips the next rank, like 1, 2, 2, 4. '
                                     'DENSE_RANK gives ties the same number without skipping, so you get 1, 2, 2, 3.',
                      'missing_concepts': ['Window functions perform calculations across a set of table rows related '
                                           'to the current row without collapsing rows into a single group like GROUP '
                                           'BY']},
                     {'quality_level': 'average',
                      'human_score': 63,
                      'answer_text': 'Window functions let you rank rows. ROW_NUMBER just numbers rows from 1 to N. '
                                     'RANK and DENSE_RANK handle ties. If two people tie for first, RANK skips to 3, '
                                     'but DENSE_RANK goes to 2. You use OVER (PARTITION BY) to reset the count per '
                                     'department.',
                      'missing_concepts': ['Window functions perform calculations across a set of table rows related '
                                           'to the current row without collapsing rows into a single group like GROUP '
                                           'BY',
                                           'RANK assigns identical ranks to ties and skips subsequent numbers (1, 2, '
                                           '2, 4); DENSE_RANK assigns identical ranks to ties without skipping numbers '
                                           '(1, 2, 2, 3)']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'Window functions are used in Microsoft Windows to display SQL results in '
                                     'separate GUI browser popups.',
                      'missing_concepts': ['Window functions perform calculations across a set of table rows related '
                                           'to the current row without collapsing rows into a single group like GROUP '
                                           'BY',
                                           'OVER (PARTITION BY ... ORDER BY ...) defines the window slice and ordering '
                                           'per partition',
                                           'ROW_NUMBER assigns strictly sequential unique integers (1, 2, 3, 4) '
                                           'arbitrarily breaking ties',
                                           'RANK assigns identical ranks to ties and skips subsequent numbers (1, 2, '
                                           '2, 4); DENSE_RANK assigns identical ranks to ties without skipping numbers '
                                           '(1, 2, 2, 3)']}]},
 {'topic_tag': 'Pandas Data Reshaping (Pivot & Melt)',
  'question': 'How do pivot_table() and melt() reshape DataFrames between wide and long formats, and when should you '
              'choose each?',
  'keywords': ['Pandas', 'pivot_table()', 'melt()', 'Wide vs Long Format', 'Tidy Data', 'Aggregation', 'Unstack'],
  'expected_concepts': ['pivot_table() converts long-format data into wide-format by turning unique values of a column '
                        'into new column headers, aggregating duplicate entries',
                        'melt() performs the inverse operation (wide to long): unpivots multiple column headers into '
                        'identifier variables and a single key-value column pair (variable, value)',
                        'Long (tidy) format is preferred for data visualization (Seaborn/Plotly) and statistical '
                        'modeling where each variable is a column and each observation is a row',
                        'Wide format is preferred for human-readable dashboard reporting, cross-tabulations, and '
                        'matrix-based algorithms (e.g., correlation matrices, PCA)'],
  'model_answer': 'In Pandas, pivot_table() and melt() perform inverse structural transformations adhering to Hadley '
                  "Wickham's Tidy Data paradigm. pivot_table() transforms data from 'long' (tall) to 'wide' format by "
                  'turning unique values of a specified column into separate column headers, indexing by identifier '
                  'columns, and applying an aggregation function (like mean or sum) when combinations contain multiple '
                  "records. Conversely, melt() unpivots a DataFrame from 'wide' to 'long' format: it preserves "
                  'designated identifier columns (id_vars) and collapses multiple measurement columns (value_vars) '
                  "into two consolidated columns—'variable' containing column names and 'value' containing the "
                  'corresponding numbers. Long format is industry standard for machine learning and visualization '
                  'libraries (Seaborn, ggplot), whereas wide format is standard for executive summary spreadsheets and '
                  'distance matrix computations.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'pivot_table() and melt() are inverse operations that switch between long and '
                                     'wide formats. pivot_table() takes long data and widens it: it takes unique '
                                     'values from a categorical column, turns them into new column headers, and '
                                     'aggregates the values. This is great for summary reports or correlation '
                                     'matrices. melt() does the opposite—it takes wide data and lengthens it by taking '
                                     "multiple column headers and unpivoting them into two columns: a 'variable' "
                                     "column and a 'value' column. You almost always want long, tidy data for data "
                                     'visualization in Seaborn or feeding into machine learning pipelines where each '
                                     'row represents a single observation.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'pivot_table converts data from long to wide, turning rows into columns and '
                                     'aggregating the numbers using sum or mean. melt does the reverse, turning '
                                     'columns into rows to make the data long. Long format is best for training models '
                                     'and creating plots with Seaborn, while wide format is easier for humans to read '
                                     'in a table.',
                      'missing_concepts': ['melt() performs the inverse operation (wide to long): unpivots multiple '
                                           'column headers into identifier variables and a single key-value column '
                                           'pair (variable, value)']},
                     {'quality_level': 'average',
                      'human_score': 63,
                      'answer_text': 'Pivot makes a dataframe wide by creating columns from values, like an Excel '
                                     'pivot table. Melt makes wide data tall and skinny. You use melt when you have '
                                     'too many columns and want to turn them into rows.',
                      'missing_concepts': ['pivot_table() converts long-format data into wide-format by turning unique '
                                           'values of a column into new column headers, aggregating duplicate entries',
                                           'Long (tidy) format is preferred for data visualization (Seaborn/Plotly) '
                                           'and statistical modeling where each variable is a column and each '
                                           'observation is a row']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'Pivot and melt are algorithms used to compress JSON files when transferring data '
                                     'over web sockets.',
                      'missing_concepts': ['pivot_table() converts long-format data into wide-format by turning unique '
                                           'values of a column into new column headers, aggregating duplicate entries',
                                           'melt() performs the inverse operation (wide to long): unpivots multiple '
                                           'column headers into identifier variables and a single key-value column '
                                           'pair (variable, value)',
                                           'Long (tidy) format is preferred for data visualization (Seaborn/Plotly) '
                                           'and statistical modeling where each variable is a column and each '
                                           'observation is a row',
                                           'Wide format is preferred for human-readable dashboard reporting, '
                                           'cross-tabulations, and matrix-based algorithms (e.g., correlation '
                                           'matrices, PCA)']}]},
 {'topic_tag': 'SQL CTEs vs Subqueries Optimization',
  'question': 'Compare Common Table Expressions (CTEs) with inline subqueries regarding readability, reusability, '
              'recursion, and query plan optimization.',
  'keywords': ['SQL CTE',
               'Common Table Expressions',
               'Inline Subqueries',
               'WITH Clause',
               'Recursive CTE',
               'Query Optimizer',
               'Materialization'],
  'expected_concepts': ['CTEs (WITH clause) provide top-down modular readability, breaking complex queries into named '
                        'logical blocks compared to deeply nested subqueries',
                        'CTEs can be referenced multiple times within the same query without duplicating logic, '
                        'whereas subqueries must be rewritten',
                        'CTEs support recursion (WITH RECURSIVE) to traverse tree-like hierarchical data or graphs, '
                        'which inline subqueries cannot accomplish',
                        'Optimizer behavior: modern RDBMS optimizers (Postgres, SQL Server) inline non-recursive CTEs '
                        'identically to subqueries, though historically some engines materialized CTEs as optimization '
                        'fences'],
  'model_answer': 'Common Table Expressions (CTEs), declared via the WITH clause, and inline subqueries serve similar '
                  'data transformation roles but differ sharply in readability, maintainability, and capability. '
                  'Readability: CTEs structure logic top-down in named, sequential stages, eliminating the '
                  "'inside-out' cognitive load of deeply nested subqueries. Reusability: A single CTE can be "
                  'referenced multiple times across downstream joins or unions in the same main query, whereas inline '
                  'subqueries must be duplicated verbatim. Recursion: CTEs natively support hierarchical and graph '
                  'traversals via WITH RECURSIVE, a feat impossible with standard subqueries. Optimization: In modern '
                  'database engines (e.g., PostgreSQL 12+, SQL Server), simple CTEs are inlined into the query planner '
                  'identically to subqueries; however, developers can use MATERIALIZED hints to prevent costly '
                  're-evaluations when a CTE is referenced repeatedly.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'CTEs using the WITH clause offer massive advantages in readability and '
                                     'modularity. Instead of nesting subqueries inside subqueries where you have to '
                                     'read from the inside out, CTEs let you define named temporary result sets '
                                     'sequentially from top to bottom. Second, reusability: you can reference the same '
                                     'CTE multiple times in downstream joins without re-writing the code. Third, CTEs '
                                     'support recursion (WITH RECURSIVE), which is essential for querying '
                                     "organizational hierarchies or tree structures that subqueries simply can't "
                                     'handle. In terms of optimization, modern database engines treat CTEs and '
                                     'subqueries mostly the same, inlining both into the execution plan, though older '
                                     'PostgreSQL versions used to treat CTEs as optimization fences.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'CTEs are written with the WITH clause at the top of the query, which makes '
                                     'complex SQL much easier to read than deeply nested subqueries. You can also '
                                     'reference a CTE multiple times in your query instead of copy-pasting a subquery. '
                                     'Additionally, recursive CTEs allow you to query hierarchical data like '
                                     'manager-employee trees. Modern query planners optimize CTEs just as well as '
                                     'subqueries.',
                      'missing_concepts': ['Optimizer behavior: modern RDBMS optimizers (Postgres, SQL Server) inline '
                                           'non-recursive CTEs identically to subqueries, though historically some '
                                           'engines materialized CTEs as optimization fences']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'CTEs are temporary tables you make with WITH. They are better than subqueries '
                                     'because subqueries are messy and hard to read when you put too many inside each '
                                     'other. CTEs also let you do recursive queries.',
                      'missing_concepts': ['CTEs can be referenced multiple times within the same query without '
                                           'duplicating logic, whereas subqueries must be rewritten',
                                           'Optimizer behavior: modern RDBMS optimizers (Postgres, SQL Server) inline '
                                           'non-recursive CTEs identically to subqueries, though historically some '
                                           'engines materialized CTEs as optimization fences']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'A CTE is a permanent table stored in the database disk, while a subquery is '
                                     'stored in RAM cache memory. CTEs are always 10 times slower than subqueries.',
                      'missing_concepts': ['CTEs (WITH clause) provide top-down modular readability, breaking complex '
                                           'queries into named logical blocks compared to deeply nested subqueries',
                                           'CTEs can be referenced multiple times within the same query without '
                                           'duplicating logic, whereas subqueries must be rewritten',
                                           'CTEs support recursion (WITH RECURSIVE) to traverse tree-like hierarchical '
                                           'data or graphs, which inline subqueries cannot accomplish',
                                           'Optimizer behavior: modern RDBMS optimizers (Postgres, SQL Server) inline '
                                           'non-recursive CTEs identically to subqueries, though historically some '
                                           'engines materialized CTEs as optimization fences']}]},
 {'topic_tag': 'Feature Engineering Techniques',
  'question': 'How do binning, target encoding, and polynomial interaction terms enhance predictive signals in machine '
              'learning models?',
  'keywords': ['Feature Engineering',
               'Binning',
               'Target Encoding',
               'Polynomial Features',
               'Interaction Terms',
               'Target Leakage',
               'Smoothing'],
  'expected_concepts': ['Binning (discretization) groups continuous features into categorical intervals, handling '
                        'non-linear relationships and mitigating outlier influence for linear models',
                        'Target encoding replaces high-cardinality categorical levels with the expected value of the '
                        'target variable for that level',
                        'Target encoding requires regularization (smoothing / m-estimate) and out-of-fold computation '
                        'to prevent severe target leakage and overfitting',
                        'Polynomial interaction terms (e.g., x1 * x2, x1^2) explicitly capture non-linear '
                        'multiplicative relationships for linear algorithms that cannot learn interactions natively'],
  'model_answer': 'Feature engineering constructs explicit domain representations to expose non-linear relationships: '
                  '1) Binning (discretization) segments continuous variables into discrete buckets (equal-width or '
                  'quantile-based), smoothing out noise, neutralizing extreme outliers, and enabling linear models to '
                  'capture non-monotonic step-function relationships; 2) Target encoding maps high-cardinality '
                  'categorical levels to the posterior mean of the target variable (e.g., average default rate per zip '
                  'code), condensing massive one-hot sparse matrices into a single predictive continuous column. '
                  'Crucially, target encoding must incorporate smoothing (m-estimate weighting against global mean) '
                  'and K-fold out-of-fold estimation to prevent target leakage and severe overfitting; and 3) '
                  'Polynomial interaction terms multiply features together (x1 * x2), explicitly modeling synergistic '
                  'effects (e.g., price * quantity = total spend) that linear and logistic regressions cannot compute '
                  'natively.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'Each technique solves a specific limitation. Binning takes continuous variables '
                                     'and cuts them into intervals, which tames extreme outliers and allows linear '
                                     'models to capture non-linear step patterns. Target encoding is fantastic for '
                                     'high-cardinality categoricals—like 10,000 postal codes—where one-hot encoding '
                                     'would explode dimensionality. It replaces each category with the average target '
                                     'value for that category, though you must use out-of-fold calculations and '
                                     'smoothing with the global prior to prevent target leakage. Polynomial '
                                     'interactions create cross-products like x1 times x2, explicitly handing '
                                     'non-linear synergies to linear models that cannot learn interactions without '
                                     'decision trees.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'Binning converts continuous numbers into bins, which handles outliers and '
                                     'non-linear trends. Target encoding replaces category labels with the mean of the '
                                     'target variable, which is great for high-cardinality features where one-hot '
                                     'encoding creates too many columns. However, you need smoothing to avoid '
                                     'overfitting. Polynomial interaction terms multiply features together so the '
                                     'model can learn interaction effects.',
                      'missing_concepts': ['Target encoding requires regularization (smoothing / m-estimate) and '
                                           'out-of-fold computation to prevent severe target leakage and overfitting']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Binning groups numbers into ranges like age groups. Target encoding replaces '
                                     "categories with target averages so you don't need one-hot encoding. Polynomial "
                                     'features multiply columns together to find interactions. They help models get '
                                     'higher accuracy scores.',
                      'missing_concepts': ['Binning (discretization) groups continuous features into categorical '
                                           'intervals, handling non-linear relationships and mitigating outlier '
                                           'influence for linear models',
                                           'Target encoding requires regularization (smoothing / m-estimate) and '
                                           'out-of-fold computation to prevent severe target leakage and overfitting']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'Target encoding is when you delete the target variable from your test set, and '
                                     'polynomial interactions are when you write mathematical equations in SQL '
                                     'comments.',
                      'missing_concepts': ['Binning (discretization) groups continuous features into categorical '
                                           'intervals, handling non-linear relationships and mitigating outlier '
                                           'influence for linear models',
                                           'Target encoding replaces high-cardinality categorical levels with the '
                                           'expected value of the target variable for that level',
                                           'Target encoding requires regularization (smoothing / m-estimate) and '
                                           'out-of-fold computation to prevent severe target leakage and overfitting',
                                           'Polynomial interaction terms (e.g., x1 * x2, x1^2) explicitly capture '
                                           'non-linear multiplicative relationships for linear algorithms that cannot '
                                           'learn interactions natively']}]},
 {'topic_tag': 'Time Series Decomposition & Stationarity',
  'question': 'How do you decompose a time series into trend, seasonality, and residuals, and why is stationarity '
              'required for ARIMA modeling?',
  'keywords': ['Time Series',
               'Decomposition',
               'Trend',
               'Seasonality',
               'Residuals',
               'Stationarity',
               'ARIMA',
               'Differencing'],
  'expected_concepts': ['Decomposition separates a series into Trend (long-term direction), Seasonality (repeating '
                        'cyclical pattern of fixed duration), and Residuals (irregular random noise)',
                        'Additive model (Y = T + S + R) applies when seasonal variations remain constant in magnitude; '
                        'Multiplicative (Y = T * S * R) applies when seasonal swings scale with trend level',
                        'Stationarity requires constant mean, constant variance, and autocovariance depending only on '
                        'lag, not absolute time',
                        'ARIMA requires stationarity because non-stationary series have time-dependent statistical '
                        'properties that make autoregressive parameter estimation mathematically unstable'],
  'model_answer': 'Time series decomposition isolates three structural components: 1) Trend (T_t) capturing sustained '
                  'long-term movement; 2) Seasonality (S_t) capturing periodic, recurring fluctuations of fixed '
                  'frequency (e.g., quarterly sales peaks); and 3) Residuals (R_t) representing unpredictable white '
                  'noise. An additive model (Y = T + S + R) is used when seasonal variations are constant in amplitude '
                  'regardless of trend level, whereas a multiplicative model (Y = T * S * R) is used when seasonal '
                  'fluctuations expand proportionally with trend growth. Stationarity—specifically weak '
                  'stationarity—requires that a series has a constant mean over time, constant variance '
                  '(homoscedasticity), and autocovariance that depends solely on the lag between observations rather '
                  'than time itself. ARIMA models require stationary inputs because autoregressive coefficients '
                  'estimated on non-stationary data suffer from spurious regression and explosive roots.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'Time series decomposition breaks down a series into three core parts: the '
                                     'long-term trend, the repeating cyclical seasonality, and the random residual '
                                     'noise. You choose an additive model (Trend + Seasonality + Residuals) if the '
                                     'seasonal swings stay constant in size over time, or a multiplicative model '
                                     '(Trend * Seasonality * Residuals) if the seasonal peaks grow larger as the '
                                     'overall trend grows. Stationarity means the series has a constant mean, constant '
                                     'variance, and time-invariant autocovariance. Classical models like ARIMA require '
                                     'stationarity because if the statistical properties change over time, the '
                                     'autoregressive parameter estimates become unstable, leading to spurious '
                                     "correlations. You achieve stationarity by differencing (the 'I' in ARIMA) or "
                                     'taking log transformations.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'Decomposition splits a time series into trend, seasonality, and noise. Additive '
                                     'is used when seasonality is constant, and multiplicative is used when '
                                     "seasonality grows with the trend. Stationarity means the mean and variance don't "
                                     'change over time. ARIMA requires stationarity so it can forecast using fixed '
                                     'historical patterns without the model exploding.',
                      'missing_concepts': ['Stationarity requires constant mean, constant variance, and autocovariance '
                                           'depending only on lag, not absolute time']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'You decompose time series into trend, seasonality, and residuals. Trend is where '
                                     "it's heading, seasonality is repeating cycles, and residuals is noise. "
                                     "Stationarity means the data doesn't have a trend. If your data isn't stationary, "
                                     'you have to difference it before running ARIMA.',
                      'missing_concepts': ['Additive model (Y = T + S + R) applies when seasonal variations remain '
                                           'constant in magnitude; Multiplicative (Y = T * S * R) applies when '
                                           'seasonal swings scale with trend level',
                                           'Stationarity requires constant mean, constant variance, and autocovariance '
                                           'depending only on lag, not absolute time']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'Time series decomposition is when you delete the date column from your CSV file. '
                                     'Stationarity means your server does not move across geographical cloud regions.',
                      'missing_concepts': ['Decomposition separates a series into Trend (long-term direction), '
                                           'Seasonality (repeating cyclical pattern of fixed duration), and Residuals '
                                           '(irregular random noise)',
                                           'Additive model (Y = T + S + R) applies when seasonal variations remain '
                                           'constant in magnitude; Multiplicative (Y = T * S * R) applies when '
                                           'seasonal swings scale with trend level',
                                           'Stationarity requires constant mean, constant variance, and autocovariance '
                                           'depending only on lag, not absolute time',
                                           'ARIMA requires stationarity because non-stationary series have '
                                           'time-dependent statistical properties that make autoregressive parameter '
                                           'estimation mathematically unstable']}]},
 {'topic_tag': 'Dimensionality Reduction in DS Workflows',
  'question': 'Why is dimensionality reduction critical when analyzing high-dimensional tabular data, and how does PCA '
              'find optimal projection axes?',
  'keywords': ['Dimensionality Reduction',
               'Curse of Dimensionality',
               'PCA',
               'Eigenvectors',
               'Eigenvalues',
               'Covariance Matrix',
               'Explained Variance'],
  'expected_concepts': ['Curse of dimensionality: high dimensions cause data sparsity, exponential volume growth, and '
                        'distance metric concentration (Euclidean distance becomes equidistant)',
                        'PCA identifies orthogonal principal components that maximize variance of projected data',
                        'Mathematically computes eigendecomposition or SVD on the centered covariance matrix: '
                        'eigenvectors define component directions, eigenvalues define explained variance',
                        'Reduces collinearity, compresses storage, and mitigates overfitting while retaining the vast '
                        'majority of cumulative variance'],
  'model_answer': "In high-dimensional spaces, datasets suffer from the 'Curse of Dimensionality': as feature count p "
                  'grows, the volume of feature space grows exponentially, data becomes extremely sparse, and distance '
                  'metrics (like Euclidean distance in k-NN and clustering) lose discriminative power because all '
                  'pairwise point distances converge to the same value. Furthermore, multicollinearity inflates model '
                  'variance and causes severe overfitting. Principal Component Analysis (PCA) addresses this through '
                  'unsupervised linear dimensionality reduction. After standardizing features, PCA computes the '
                  'covariance matrix and performs eigendecomposition (or Singular Value Decomposition, SVD). The '
                  'resulting eigenvectors define orthogonal axes pointing in directions of maximum data variance, '
                  'while corresponding eigenvalues quantify the variance explained by each axis. Projecting data onto '
                  'the top k components preserves maximal information while slashing feature dimensions.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'High dimensionality triggers the curse of dimensionality: data points become '
                                     'extraordinarily sparse, models easily overfit, and distance metrics like '
                                     'Euclidean distance break down because all points become roughly equidistant. '
                                     'Principal Component Analysis (PCA) fixes this by finding new orthogonal axes '
                                     'that maximize the variance of the projected data. Mathematically, it '
                                     'standardizes the data, calculates the covariance matrix, and finds its '
                                     'eigenvectors and eigenvalues. The eigenvectors define the directions of the '
                                     'principal components, and the eigenvalues tell you how much variance each '
                                     'component captures. By sorting by eigenvalues and keeping the top components '
                                     'that explain 90% or 95% of the total variance, you eliminate multicollinearity '
                                     'and drastically compress the feature space without losing major patterns.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'High-dimensional data causes the curse of dimensionality, where data becomes '
                                     'sparse and models overfit. PCA solves this by projecting the data onto a smaller '
                                     'number of uncorrelated components. It uses the covariance matrix and finds '
                                     'eigenvectors and eigenvalues. The eigenvectors are the directions of maximum '
                                     'spread, and eigenvalues tell you how much variance is explained. You keep the '
                                     'top components that cover most of the variance.',
                      'missing_concepts': ['Curse of dimensionality: high dimensions cause data sparsity, exponential '
                                           'volume growth, and distance metric concentration (Euclidean distance '
                                           'becomes equidistant)']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Too many dimensions makes your model slow and overfits, which is called the '
                                     'curse of dimensionality. PCA reduces the number of columns by combining them '
                                     'into principal components. You check the scree plot to pick how many components '
                                     'to keep.',
                      'missing_concepts': ['Curse of dimensionality: high dimensions cause data sparsity, exponential '
                                           'volume growth, and distance metric concentration (Euclidean distance '
                                           'becomes equidistant)',
                                           'Mathematically computes eigendecomposition or SVD on the centered '
                                           'covariance matrix: eigenvectors define component directions, eigenvalues '
                                           'define explained variance']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'Dimensionality reduction is when you delete columns that contain strings and '
                                     'only keep integer columns in your SQL table.',
                      'missing_concepts': ['Curse of dimensionality: high dimensions cause data sparsity, exponential '
                                           'volume growth, and distance metric concentration (Euclidean distance '
                                           'becomes equidistant)',
                                           'PCA identifies orthogonal principal components that maximize variance of '
                                           'projected data',
                                           'Mathematically computes eigendecomposition or SVD on the centered '
                                           'covariance matrix: eigenvectors define component directions, eigenvalues '
                                           'define explained variance',
                                           'Reduces collinearity, compresses storage, and mitigates overfitting while '
                                           'retaining the vast majority of cumulative variance']}]},
 {'topic_tag': 'Data Pipeline Architectures (ETL vs ELT)',
  'question': 'Compare traditional ETL architectures with modern cloud ELT architectures regarding transformation '
              'timing, scalability, and flexibility.',
  'keywords': ['ETL vs ELT',
               'Data Pipelines',
               'Cloud Data Warehouses',
               'Snowflake/BigQuery',
               'Compute Pushdown',
               'Transformation Flexibility'],
  'expected_concepts': ['ETL (Extract, Transform, Load) transforms data in a separate processing engine before loading '
                        'into the target database; historic constraint of expensive on-prem storage/compute',
                        'ELT (Extract, Load, Transform) loads raw unstructured/semi-structured data directly into '
                        'cloud data warehouses (Snowflake, BigQuery, Databricks) and transforms downstream in-place '
                        'using SQL',
                        'ELT leverages massive cloud MPP (Massively Parallel Processing) compute pushdown and infinite '
                        'decoupled storage',
                        'ELT preserves raw data immutability, enabling retrospective transformation re-runs when '
                        'business requirements change'],
  'model_answer': 'The transition from ETL to ELT represents a paradigm shift driven by cloud storage economics and '
                  'decoupled compute. In traditional ETL (Extract, Transform, Load), raw data is extracted from source '
                  'systems, transformed on an intermediate staging server (e.g., Informatica or custom scripts) to fit '
                  'a rigid schema, and then loaded into an on-premises data warehouse. This was necessary when storage '
                  'was expensive and warehouses lacked compute power, but transformations formed a bottleneck and raw '
                  'data was lost. Modern ELT (Extract, Load, Transform) extracts raw data and loads it immediately '
                  'into cloud data warehouses/lakehouses (like Snowflake, BigQuery, or Redshift). Transformations '
                  'occur inside the target engine using SQL/dbt, leveraging scalable Massively Parallel Processing '
                  '(MPP). ELT preserves raw data immutability, supports agile retrospective re-modeling, and '
                  'eliminates specialized pipeline bottlenecks.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'The difference is all about where and when the transformation happens. In '
                                     'traditional ETL, data is transformed on an intermediate compute server before '
                                     'being loaded into the warehouse. That was necessary years ago when on-prem '
                                     'warehouse storage and compute were strictly limited, but it created severe '
                                     'pipeline bottlenecks and meant raw data was discarded. Modern ELT flips this: '
                                     'tools like Fivetran extract raw data and load it immediately into cloud '
                                     'warehouses like Snowflake or BigQuery. Then transformations happen inside the '
                                     "warehouse using tools like dbt, pushing compute directly into the warehouse's "
                                     'massively parallel compute engine. ELT is far more flexible because raw data is '
                                     'preserved, meaning if business logic changes, you can re-run transformations '
                                     'retroactively without re-extracting from source systems.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'ETL transforms the data before loading it into the warehouse, which requires '
                                     'separate transformation servers. ELT loads the raw data into cloud warehouses '
                                     'like Snowflake first, and then transforms it inside the warehouse using SQL and '
                                     'dbt. ELT is faster and more scalable because cloud warehouses have elastic '
                                     'compute, and you always have the raw data available if you need to rebuild your '
                                     'models.',
                      'missing_concepts': ['ETL (Extract, Transform, Load) transforms data in a separate processing '
                                           'engine before loading into the target database; historic constraint of '
                                           'expensive on-prem storage/compute']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'ETL stands for extract transform load and ELT is extract load transform. In ETL '
                                     'you transform the data before putting it in the database. In ELT you load it '
                                     'first and then transform it with SQL queries. ELT is newer and used with '
                                     'Snowflake.',
                      'missing_concepts': ['ELT leverages massive cloud MPP (Massively Parallel Processing) compute '
                                           'pushdown and infinite decoupled storage',
                                           'ELT preserves raw data immutability, enabling retrospective transformation '
                                           're-runs when business requirements change']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'ETL is used for Python scripts, while ELT is a networking protocol for '
                                     'transmitting IoT sensor packets over Bluetooth.',
                      'missing_concepts': ['ETL (Extract, Transform, Load) transforms data in a separate processing '
                                           'engine before loading into the target database; historic constraint of '
                                           'expensive on-prem storage/compute',
                                           'ELT (Extract, Load, Transform) loads raw unstructured/semi-structured data '
                                           'directly into cloud data warehouses (Snowflake, BigQuery, Databricks) and '
                                           'transforms downstream in-place using SQL',
                                           'ELT leverages massive cloud MPP (Massively Parallel Processing) compute '
                                           'pushdown and infinite decoupled storage',
                                           'ELT preserves raw data immutability, enabling retrospective transformation '
                                           're-runs when business requirements change']}]},
 {'topic_tag': 'Data Warehouse vs Data Lake vs Lakehouse',
  'question': 'Compare Data Warehouses, Data Lakes, and Data Lakehouses regarding data structure, schema enforcement, '
              'and analytical performance.',
  'keywords': ['Data Warehouse',
               'Data Lake',
               'Data Lakehouse',
               'Schema-on-Write',
               'Schema-on-Read',
               'ACID Transactions',
               'Delta Lake/Apache Iceberg'],
  'expected_concepts': ['Data Warehouse: highly structured, curated relational tables, schema-on-write, optimized for '
                        'fast SQL BI queries, but expensive and poor for unstructured data',
                        'Data Lake: cheap object storage (S3/GCS) storing raw structured, semi-structured, and '
                        'unstructured data, schema-on-read, but lacks ACID guarantees and prone to data swamps',
                        'Data Lakehouse: modern hybrid architecture combining low-cost object storage with an open '
                        'table format layer (Delta Lake, Apache Iceberg) providing ACID transactions, schema '
                        'enforcement, and BI performance',
                        'Lakehouses unify BI SQL analytics and machine learning workloads directly on a single source '
                        'of truth'],
  'model_answer': 'Data architecture has evolved across three generations: 1) Data Warehouses (e.g., Teradata, '
                  "Snowflake) store highly structured, relational data governed by strict 'schema-on-write'. They "
                  'deliver blazingly fast SQL query performance and ACID transactions for business intelligence, but '
                  'are expensive and cannot store unstructured data (audio, images, logs); 2) Data Lakes (e.g., AWS '
                  'S3, Hadoop HDFS) store raw structured, semi-structured, and unstructured files cheaply with '
                  "'schema-on-read', serving ML data science workloads, but historically suffered from lack of ACID "
                  "transactions, poor query performance, and degeneration into 'data swamps'; 3) Data Lakehouses "
                  '(e.g., Databricks Delta Lake, Apache Iceberg) unify both paradigms. They sit on cheap object '
                  'storage while introducing an open transactional metadata layer that enforces schemas, supports ACID '
                  'transactions, and enables BI-grade query performance alongside native machine learning compute on '
                  'one shared source of truth.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'A Data Warehouse is built on curated, structured relational tables with strict '
                                     "schema-on-write. It gives phenomenal SQL performance for BI dashboards, but it's "
                                     "expensive and can't handle raw unstructured data like video or JSON logs. A Data "
                                     'Lake uses cheap cloud object storage like S3 to dump raw data of any format with '
                                     'schema-on-read, great for machine learning, but historically lacked ACID '
                                     'transactions and often turned into unmanageable data swamps. A Data Lakehouse '
                                     'bridges both worlds: it stores data on cheap object storage like S3 using open '
                                     'table formats like Delta Lake or Apache Iceberg, adding an ACID metadata layer '
                                     'with schema enforcement, time travel, and indexing. This allows companies to run '
                                     'both fast SQL BI queries and machine learning training directly off the same '
                                     'storage layer.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'Data Warehouses are for structured relational data with schema-on-write, perfect '
                                     'for SQL queries and reports. Data Lakes store raw files of all types cheaply on '
                                     'S3 with schema-on-read, but can get messy without ACID transactions. A Lakehouse '
                                     'combines them by putting an ACID metadata layer like Delta Lake on top of object '
                                     'storage, so you get the low cost of a lake with the performance and reliability '
                                     'of a warehouse.',
                      'missing_concepts': ['Lakehouses unify BI SQL analytics and machine learning workloads directly '
                                           'on a single source of truth']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Warehouses store clean SQL tables. Lakes store raw data files like JSON and '
                                     'images. Lakehouse is a combination of both made by Databricks that uses Delta '
                                     'Lake so you can run SQL on raw data.',
                      'missing_concepts': ['Data Warehouse: highly structured, curated relational tables, '
                                           'schema-on-write, optimized for fast SQL BI queries, but expensive and poor '
                                           'for unstructured data',
                                           'Data Lake: cheap object storage (S3/GCS) storing raw structured, '
                                           'semi-structured, and unstructured data, schema-on-read, but lacks ACID '
                                           'guarantees and prone to data swamps']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'A Data Lakehouse is a residential house near a lake where data engineers work '
                                     'remotely during summer.',
                      'missing_concepts': ['Data Warehouse: highly structured, curated relational tables, '
                                           'schema-on-write, optimized for fast SQL BI queries, but expensive and poor '
                                           'for unstructured data',
                                           'Data Lake: cheap object storage (S3/GCS) storing raw structured, '
                                           'semi-structured, and unstructured data, schema-on-read, but lacks ACID '
                                           'guarantees and prone to data swamps',
                                           'Data Lakehouse: modern hybrid architecture combining low-cost object '
                                           'storage with an open table format layer (Delta Lake, Apache Iceberg) '
                                           'providing ACID transactions, schema enforcement, and BI performance',
                                           'Lakehouses unify BI SQL analytics and machine learning workloads directly '
                                           'on a single source of truth']}]},
 {'topic_tag': 'Stratified vs Simple Random Sampling',
  'question': 'Why is Stratified Random Sampling preferred over Simple Random Sampling when evaluating machine '
              'learning models on imbalanced datasets?',
  'keywords': ['Stratified Sampling',
               'Simple Random Sampling',
               'Class Imbalance',
               'Subgroup Representation',
               'Sampling Variance',
               'Train-Test Split'],
  'expected_concepts': ['Simple Random Sampling draws individuals purely at random, risking severe underrepresentation '
                        'or complete absence of rare minority classes',
                        'Stratified Sampling partitions the population into non-overlapping homogeneous strata '
                        '(classes/demographics) and samples proportionally from each stratum',
                        'Preserves identical class balance ratios across train, validation, and test splits, '
                        'preventing distribution shift during evaluation',
                        'Reduces sampling variance of estimators, ensuring precise performance metrics on '
                        'low-frequency critical cohorts (e.g., fraud cases)'],
  'model_answer': 'In statistical sampling and model validation, Simple Random Sampling (SRS) assigns every member of '
                  'a population an equal probability of selection. While unbiased in expectation, SRS exhibits high '
                  'sampling variability when dealing with skewed populations: in an imbalanced dataset (e.g., 99% '
                  'non-fraud, 1% fraud), a standard random split can easily under-sample or completely omit rare fraud '
                  'cases from the test fold. Stratified Random Sampling resolves this by partitioning the population '
                  'into mutually exclusive subgroups (strata) based on key attributes—such as the target class or '
                  'demographic segment—and then drawing independent random samples from within each stratum. This '
                  'guarantees that train, validation, and test sets maintain the exact target distribution of the '
                  'parent dataset, eliminating split-induced distribution shift and drastically reducing the variance '
                  'of evaluation metrics.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'Simple random sampling gives every row an equal probability of selection, but on '
                                     'an imbalanced dataset—like fraud detection with a 0.5% fraud rate—a random split '
                                     'can result in some folds having almost zero fraud cases, leading to wildly '
                                     'unstable evaluation metrics. Stratified sampling divides the dataset into '
                                     'distinct strata based on the target class and samples proportionally from each '
                                     'stratum. This guarantees that your training set, validation set, and test set '
                                     'all mirror the exact same minority class proportion as the overall population. '
                                     'It preserves statistical representation, eliminates split-induced distribution '
                                     'shift, and ensures your cross-validation metrics accurately reflect production '
                                     'performance.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'Simple random sampling picks rows randomly, which can accidentally leave out '
                                     'rare classes in an imbalanced dataset. Stratified sampling groups data by the '
                                     'target class first and samples from each group proportionally. This makes sure '
                                     'that your training and test sets have the exact same percentage of positive and '
                                     "negative classes, so your model evaluation isn't distorted by a lucky or unlucky "
                                     'split.',
                      'missing_concepts': ['Reduces sampling variance of estimators, ensuring precise performance '
                                           'metrics on low-frequency critical cohorts (e.g., fraud cases)']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Stratified sampling is better than random sampling because it keeps the same '
                                     'ratio of classes in the train and test split. If you have imbalanced data and '
                                     'use train_test_split without stratify=y, you might get a test set with no fraud '
                                     'cases. Stratified sampling fixes that.',
                      'missing_concepts': ['Stratified Sampling partitions the population into non-overlapping '
                                           'homogeneous strata (classes/demographics) and samples proportionally from '
                                           'each stratum',
                                           'Reduces sampling variance of estimators, ensuring precise performance '
                                           'metrics on low-frequency critical cohorts (e.g., fraud cases)']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'Stratified sampling is an unsupervised clustering algorithm that removes all '
                                     'outlier rows from the training set before running random sampling.',
                      'missing_concepts': ['Simple Random Sampling draws individuals purely at random, risking severe '
                                           'underrepresentation or complete absence of rare minority classes',
                                           'Stratified Sampling partitions the population into non-overlapping '
                                           'homogeneous strata (classes/demographics) and samples proportionally from '
                                           'each stratum',
                                           'Preserves identical class balance ratios across train, validation, and '
                                           'test splits, preventing distribution shift during evaluation',
                                           'Reduces sampling variance of estimators, ensuring precise performance '
                                           'metrics on low-frequency critical cohorts (e.g., fraud cases)']}]},
 {'topic_tag': 'Bayesian vs Frequentist Paradigms',
  'question': 'Contrast Frequentist p-value significance testing with Bayesian posterior probability distributions and '
              'Credible Intervals.',
  'keywords': ['Bayesian vs Frequentist',
               'p-value',
               'Posterior Distribution',
               'Credible Interval',
               'Confidence Interval',
               'Prior Beliefs',
               'MCMC'],
  'expected_concepts': ['Frequentist treats parameters as fixed, unknown constants; probability represents long-run '
                        'frequency of events in repeated hypothetical experiments',
                        'Frequentist 95% Confidence Interval means 95% of constructed intervals from repeated trials '
                        'contain the true fixed parameter, NOT a 95% probability for the specific interval',
                        'Bayesian treats parameters as random variables with probability distributions; incorporates '
                        "prior beliefs P(theta) updated with observed likelihood P(D|theta) via Bayes' Theorem to "
                        'yield posterior P(theta|D)',
                        'Bayesian 95% Credible Interval has an intuitive direct probabilistic interpretation: there is '
                        'a 95% probability that the true parameter lies within that specific interval'],
  'model_answer': 'The philosophical divide between Frequentist and Bayesian paradigms centers on the definition of '
                  'probability and parameter nature. The Frequentist paradigm views parameters (e.g., conversion rate '
                  'difference theta) as fixed, deterministic unknown constants, interpreting probability as the '
                  'relative limiting frequency of events across infinitely repeated experiments. A frequentist p-value '
                  'evaluates P(Data|H0), and a 95% Confidence Interval denotes that in 95% of hypothetical repeated '
                  'identical experiments, the generated interval will bracket the true fixed parameter. In contrast, '
                  'the Bayesian paradigm treats the parameter itself as a random variable described by a probability '
                  'distribution. By combining prior knowledge P(theta) with observed data likelihood P(Data|theta) via '
                  "Bayes' rule, it produces a posterior distribution P(theta|Data). Consequently, a Bayesian 95% "
                  'Credible Interval offers the direct, intuitive statement that there is a 95% probability that the '
                  'true parameter lies inside the interval.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'The core distinction is how they treat parameters and probability. Frequentists '
                                     'treat the unknown parameter as a fixed constant and define probability as '
                                     'long-run frequency in repeated experiments. A p-value is P(Data|H0), and a 95% '
                                     'Confidence Interval means that if you repeated the experiment 100 times, 95 of '
                                     "those intervals would cover the true fixed parameter—you cannot say there's a "
                                     '95% chance the parameter is in your specific interval. Bayesians treat the '
                                     'parameter as a random variable with a probability distribution. You start with a '
                                     'prior distribution reflecting prior knowledge, update it with observed '
                                     "likelihood using Bayes' Theorem, and get a posterior distribution. A Bayesian "
                                     '95% Credible Interval has the intuitive meaning everyone wants: given our data '
                                     'and prior, there is genuinely a 95% probability that the parameter lies within '
                                     'that interval.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'Frequentists treat parameters as fixed numbers and rely on p-values and '
                                     'confidence intervals based on repeated sampling. A confidence interval does not '
                                     'mean a 95% chance the parameter is inside it. Bayesians treat parameters as '
                                     'probability distributions. They use prior beliefs and update them with evidence '
                                     'to get a posterior distribution. A Bayesian credible interval actually means '
                                     'there is a 95% probability that the true value falls inside the bounds.',
                      'missing_concepts': ['Frequentist treats parameters as fixed, unknown constants; probability '
                                           'represents long-run frequency of events in repeated hypothetical '
                                           'experiments']},
                     {'quality_level': 'average',
                      'human_score': 63,
                      'answer_text': 'Frequentist uses p-values to reject the null hypothesis, while Bayesian uses '
                                     "prior distributions and Bayes' theorem. In Bayesian you get a credible interval "
                                     'which tells you the probability of the parameter, whereas frequentist confidence '
                                     'intervals are based on repeating the experiment many times.',
                      'missing_concepts': ['Frequentist 95% Confidence Interval means 95% of constructed intervals '
                                           'from repeated trials contain the true fixed parameter, NOT a 95% '
                                           'probability for the specific interval',
                                           'Bayesian treats parameters as random variables with probability '
                                           'distributions; incorporates prior beliefs P(theta) updated with observed '
                                           "likelihood P(D|theta) via Bayes' Theorem to yield posterior P(theta|D)"]},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'Frequentist means running a script frequently on a cron job, while Bayesian is '
                                     'an obsolete statistical theory from the 18th century that has been replaced by '
                                     'deep neural networks.',
                      'missing_concepts': ['Frequentist treats parameters as fixed, unknown constants; probability '
                                           'represents long-run frequency of events in repeated hypothetical '
                                           'experiments',
                                           'Frequentist 95% Confidence Interval means 95% of constructed intervals '
                                           'from repeated trials contain the true fixed parameter, NOT a 95% '
                                           'probability for the specific interval',
                                           'Bayesian treats parameters as random variables with probability '
                                           'distributions; incorporates prior beliefs P(theta) updated with observed '
                                           "likelihood P(D|theta) via Bayes' Theorem to yield posterior P(theta|D)",
                                           'Bayesian 95% Credible Interval has an intuitive direct probabilistic '
                                           'interpretation: there is a 95% probability that the true parameter lies '
                                           'within that specific interval']}]},
 {'topic_tag': 'Feature Selection Strategies',
  'question': 'Compare Filter, Wrapper, and Embedded feature selection methods in terms of computational complexity, '
              'model dependency, and overfitting risk.',
  'keywords': ['Feature Selection',
               'Filter Methods',
               'Wrapper Methods',
               'Embedded Methods',
               'RFE',
               'Lasso L1 Regularization',
               'Overfitting'],
  'expected_concepts': ['Filter methods evaluate intrinsic statistical properties (correlation, mutual info, '
                        'chi-square) independently of any learning algorithm; computationally fast, but ignore feature '
                        'interactions',
                        'Wrapper methods (e.g., RFE, Forward/Backward selection) use a predictive model as an '
                        'evaluation engine, searching feature subsets; captures interactions but computationally '
                        'expensive and prone to overfitting',
                        'Embedded methods (e.g., Lasso L1 penalty, tree feature importances) perform feature selection '
                        'natively during model training',
                        'Trade-off summary: Filter is fast and model-agnostic; Wrapper is slow, model-specific, and '
                        'high-performing; Embedded balances efficiency and interaction modeling'],
  'model_answer': 'Feature selection techniques optimize model performance, interpretability, and training speed by '
                  'removing redundant or noisy attributes, broadly categorized into three paradigms: 1) Filter methods '
                  'assess statistical relevance independently of any machine learning model using univariate metrics '
                  '(e.g., Pearson correlation, Mutual Information, Chi-Square, ANOVA F-test). They are computationally '
                  'blazingly fast (O(p)) and scale to millions of features, but evaluate features in isolation, '
                  'ignoring multi-feature interactions; 2) Wrapper methods (e.g., Recursive Feature Elimination [RFE], '
                  'sequential forward/backward selection) treat the model as a black-box evaluation engine, '
                  'iteratively training models on feature subsets to optimize cross-validation score. They capture '
                  'complex feature synergies but are computationally expensive (O(2^p) or O(p^2)) and carry high '
                  'overfitting risk on small samples; and 3) Embedded methods (e.g., Lasso L1 regularization, '
                  'tree-based Gini/gain importances) perform feature selection natively during mathematical '
                  'optimization, offering an optimal balance of computational speed and interaction awareness.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'Feature selection falls into three distinct buckets. Filter methods evaluate '
                                     'features based on standalone statistical metrics like correlation, mutual '
                                     'information, or chi-square, completely independent of any machine learning '
                                     'model. They are blazingly fast and model-agnostic, but they evaluate features in '
                                     'isolation and miss non-linear interactions. Wrapper methods, like Recursive '
                                     'Feature Elimination (RFE) or forward selection, use the actual machine learning '
                                     'algorithm to evaluate subsets of features. They catch complex feature synergies '
                                     'and yield great performance, but they are computationally expensive and prone to '
                                     'overfitting on small datasets. Embedded methods perform selection directly '
                                     'during model training—like Lasso L1 regularization shrinking irrelevant '
                                     'coefficients to zero, or tree algorithms selecting split variables. Embedded '
                                     'methods provide the sweet spot: they consider interactions while training in a '
                                     'single pass.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'Filter methods use statistical tests like correlation or mutual info without '
                                     'involving a model, making them very fast. Wrapper methods, like RFE, train '
                                     'models repeatedly on different subsets to find the best combination, which '
                                     'captures interactions but is very slow. Embedded methods do selection '
                                     'automatically during model training, like Lasso regression with L1 '
                                     'regularization or Random Forest feature importance.',
                      'missing_concepts': ['Wrapper methods (e.g., RFE, Forward/Backward selection) use a predictive '
                                           'model as an evaluation engine, searching feature subsets; captures '
                                           'interactions but computationally expensive and prone to overfitting']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Filter is checking correlation before training. Wrapper is running RFE to find '
                                     'the best features. Embedded is using Lasso regression because L1 regularization '
                                     'sets coefficients to zero. Filter is fastest and wrapper is slowest.',
                      'missing_concepts': ['Filter methods evaluate intrinsic statistical properties (correlation, '
                                           'mutual info, chi-square) independently of any learning algorithm; '
                                           'computationally fast, but ignore feature interactions',
                                           'Wrapper methods (e.g., RFE, Forward/Backward selection) use a predictive '
                                           'model as an evaluation engine, searching feature subsets; captures '
                                           'interactions but computationally expensive and prone to overfitting']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'Filter methods are used in Photoshop for image processing, wrapper methods are '
                                     'used to wrap Python code in C++, and embedded methods are only used for '
                                     'microcontrollers.',
                      'missing_concepts': ['Filter methods evaluate intrinsic statistical properties (correlation, '
                                           'mutual info, chi-square) independently of any learning algorithm; '
                                           'computationally fast, but ignore feature interactions',
                                           'Wrapper methods (e.g., RFE, Forward/Backward selection) use a predictive '
                                           'model as an evaluation engine, searching feature subsets; captures '
                                           'interactions but computationally expensive and prone to overfitting',
                                           'Embedded methods (e.g., Lasso L1 penalty, tree feature importances) '
                                           'perform feature selection natively during model training',
                                           'Trade-off summary: Filter is fast and model-agnostic; Wrapper is slow, '
                                           'model-specific, and high-performing; Embedded balances efficiency and '
                                           'interaction modeling']}]},
 {'topic_tag': 'Class Imbalance Handling Strategies',
  'question': 'How do SMOTE synthetic oversampling, undersampling, and class weight adjustments mitigate '
              'classification bias on heavily imbalanced datasets?',
  'keywords': ['Class Imbalance',
               'SMOTE',
               'Random Undersampling',
               'Class Weights',
               'Focal Loss',
               'PR-AUC',
               'Synthetic Minority Oversampling'],
  'expected_concepts': ['Class imbalance causes algorithms optimizing accuracy to predict the majority class '
                        'exclusively, leading to high accuracy but near-zero recall on minority classes',
                        'SMOTE creates synthetic minority instances by interpolating along line segments connecting '
                        'k-nearest neighbors in feature space (must be applied strictly to training fold)',
                        'Random undersampling discards majority instances, reducing training time but throwing away '
                        'potentially valuable majority data',
                        'Cost-sensitive learning / class weights penalize minority misclassification errors inversely '
                        'proportional to class frequency in the loss function without modifying data distributions'],
  'model_answer': 'Class imbalance severely degrades standard classifiers because loss functions minimizing global '
                  'error are dominated by the majority class, yielding deceptive 99% accuracy while exhibiting zero '
                  'minority recall. Data scientists counter this through data-level and algorithmic-level strategies: '
                  '1) SMOTE (Synthetic Minority Over-sampling Technique) generates synthetic minority examples by '
                  'taking k-nearest neighbors of minority points and interpolating synthetic samples along line '
                  'segments between them. Critically, SMOTE must be executed strictly within training folds to avoid '
                  'data leakage; 2) Random undersampling drops majority class records to equalize class balance; while '
                  'computationally efficient, it discards valuable majority information; and 3) Algorithmic '
                  'cost-sensitive learning modifies the loss function directly via class weights (e.g., '
                  "scale_pos_weight in XGBoost or class_weight='balanced' in sklearn), penalizing minority "
                  'misclassifications inversely proportional to class frequencies. Cost-sensitive weighting is '
                  'frequently preferred in production because it avoids data alteration, synthetic noise, and '
                  'information loss.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'When a dataset is heavily imbalanced, standard algorithms optimize for accuracy '
                                     'by predicting the majority class for everything. You have three main ways to fix '
                                     'this. SMOTE synthesizes new minority points by finding k-nearest neighbors in '
                                     'feature space and interpolating between them. You must apply SMOTE only inside '
                                     'the training fold of cross-validation to prevent severe data leakage. '
                                     'Undersampling drops majority rows to balance the classes; it speeds up training '
                                     'but discards valuable information. Algorithmic weighting, like '
                                     "class_weight='balanced' or scale_pos_weight in XGBoost, modifies the loss "
                                     'function to heavily penalize errors on minority cases without altering the '
                                     'actual data. In industry, adjusting class weights or tuning decision thresholds '
                                     "on PR-AUC is usually preferred over SMOTE because it doesn't create synthetic "
                                     'hallucinations in high-dimensional space.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'SMOTE generates synthetic examples of the minority class by interpolating '
                                     'between nearby points using k-NN. Undersampling randomly removes majority class '
                                     'examples to balance the dataset, though you lose data. Class weighting changes '
                                     'the loss function to make mistakes on the minority class much more expensive. '
                                     "Class weighting is usually better in production because you don't distort the "
                                     'data or add fake synthetic points.',
                      'missing_concepts': ['SMOTE creates synthetic minority instances by interpolating along line '
                                           'segments connecting k-nearest neighbors in feature space (must be applied '
                                           'strictly to training fold)']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'SMOTE creates fake data points for the small class so the classes are equal. '
                                     'Undersampling deletes rows from the big class. Class weights tells the model to '
                                     'pay more attention to the minority class. You should use PR-AUC instead of '
                                     'ROC-AUC to evaluate imbalanced models.',
                      'missing_concepts': ['SMOTE creates synthetic minority instances by interpolating along line '
                                           'segments connecting k-nearest neighbors in feature space (must be applied '
                                           'strictly to training fold)',
                                           'Random undersampling discards majority instances, reducing training time '
                                           'but throwing away potentially valuable majority data']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'SMOTE is an encryption algorithm that hides sensitive customer IDs. Class '
                                     'weights refer to the file size of your training dataset in megabytes.',
                      'missing_concepts': ['Class imbalance causes algorithms optimizing accuracy to predict the '
                                           'majority class exclusively, leading to high accuracy but near-zero recall '
                                           'on minority classes',
                                           'SMOTE creates synthetic minority instances by interpolating along line '
                                           'segments connecting k-nearest neighbors in feature space (must be applied '
                                           'strictly to training fold)',
                                           'Random undersampling discards majority instances, reducing training time '
                                           'but throwing away potentially valuable majority data',
                                           'Cost-sensitive learning / class weights penalize minority '
                                           'misclassification errors inversely proportional to class frequency in the '
                                           'loss function without modifying data distributions']}]},
 {'topic_tag': 'SQL Query Optimization & Indexing',
  'question': 'How do B-Tree indexes speed up SQL query execution, and when does a non-sargable predicate cause a full '
              'table scan?',
  'keywords': ['SQL Optimization',
               'B-Tree Index',
               'Sargable Predicates',
               'Full Table Scan',
               'Execution Plan',
               'EXPLAIN',
               'Index Seek vs Scan'],
  'expected_concepts': ['B-Tree indexes organize sorted key values in a balanced hierarchical tree, providing '
                        'logarithmic O(log N) lookup time via Index Seek',
                        'A predicate is SARGable (Search Argument Able) when the database engine can directly exploit '
                        'an index on that column without row-by-row function evaluation',
                        'Wrapping indexed columns in functions (e.g., WHERE YEAR(order_date) = 2024 or WHERE '
                        "LOWER(email) = '...') breaks sargability, forcing a full table scan",
                        'Composite indexes require leading column matching (Left-to-Right Prefix rule) to be utilized '
                        'effectively by the optimizer'],
  'model_answer': 'B-Tree (Balanced Tree) indexes accelerate SQL query execution by maintaining a self-balancing, '
                  'sorted multi-level tree of indexed keys pointing to physical row IDs (RIDs/TIDs). Instead of '
                  'scanning every page on disk (Full Table Scan, O(N)), the database engine traverses the B-Tree from '
                  'root to leaf via Index Seek in O(log N) operations. However, index utilization relies on SARGable '
                  '(Search Argument Able) predicates. A predicate becomes non-sargable when an indexed column is '
                  "wrapped in an expression or scalar function—such as 'WHERE YEAR(created_at) = 2023' or 'WHERE "
                  "SUBSTRING(name, 1, 3) = 'ABC''. Because the engine cannot know the function output without "
                  'evaluating every row, it abandons the index seek and falls back to an expensive full table scan. '
                  "Rewriting to a sargable range condition ('WHERE created_at >= '2023-01-01' AND created_at < "
                  "'2024-01-01'') restores logarithmic index seeks.",
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'A B-Tree index maintains a sorted tree structure of column values that lets the '
                                     'engine perform an index seek in O(log N) time instead of scanning millions of '
                                     'rows sequentially. A predicate is SARGable—meaning Search Argument Able—if the '
                                     'query optimizer can use the index directly. You make a predicate non-sargable '
                                     'whenever you apply a function or transformation to the indexed column in the '
                                     "WHERE clause. For instance, writing 'WHERE YEAR(order_date) = 2023' forces the "
                                     'database to evaluate the YEAR() function on every single row in the table, '
                                     'completely bypassing your index and causing a full table scan. Rewriting it to a '
                                     "sargable range—'WHERE order_date >= '2023-01-01' AND order_date < "
                                     "'2024-01-01''—lets the B-tree immediately jump to the start of the range and "
                                     'perform a fast index seek.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'B-Tree indexes sort your data in a tree so the database can find rows in log(N) '
                                     'time instead of scanning the whole table. A non-sargable query is when you wrap '
                                     "an indexed column in a function, like WHERE UPPER(name) = 'JOHN'. The engine "
                                     "can't use the index because it has to run the UPPER function on every row, "
                                     'causing a full table scan. You should rewrite queries so the column stands alone '
                                     'without functions.',
                      'missing_concepts': ['Composite indexes require leading column matching (Left-to-Right Prefix '
                                           'rule) to be utilized effectively by the optimizer']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': "B-Trees make queries faster by indexing columns so you don't do full table "
                                     'scans. If you write bad SQL like putting a function in the WHERE clause or using '
                                     "wildcards like '%text', the index won't work and the database has to scan every "
                                     "row. You can use EXPLAIN to see if it's doing an index scan or table scan.",
                      'missing_concepts': ['B-Tree indexes organize sorted key values in a balanced hierarchical tree, '
                                           'providing logarithmic O(log N) lookup time via Index Seek',
                                           'A predicate is SARGable (Search Argument Able) when the database engine '
                                           'can directly exploit an index on that column without row-by-row function '
                                           'evaluation']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'A B-Tree index deletes duplicate rows from the hard drive, and non-sargable '
                                     'means the query has a syntax error that crashes the database server.',
                      'missing_concepts': ['B-Tree indexes organize sorted key values in a balanced hierarchical tree, '
                                           'providing logarithmic O(log N) lookup time via Index Seek',
                                           'A predicate is SARGable (Search Argument Able) when the database engine '
                                           'can directly exploit an index on that column without row-by-row function '
                                           'evaluation',
                                           'Wrapping indexed columns in functions (e.g., WHERE YEAR(order_date) = 2024 '
                                           "or WHERE LOWER(email) = '...') breaks sargability, forcing a full table "
                                           'scan',
                                           'Composite indexes require leading column matching (Left-to-Right Prefix '
                                           'rule) to be utilized effectively by the optimizer']}]},
 {'topic_tag': 'Feature Store Architecture in MLOps',
  'question': 'What role does a Feature Store play in maintaining point-in-time correctness and preventing '
              'training-serving skew in MLOps systems?',
  'keywords': ['Feature Store',
               'MLOps',
               'Point-in-Time Correctness',
               'Training-Serving Skew',
               'Online Store (Redis)',
               'Offline Store (Parquet/Snowflake)',
               'Feature Sharing'],
  'expected_concepts': ['Feature store acts as centralized repository for discovering, computing, storing, and serving '
                        'curated ML features across teams',
                        'Dual-storage architecture: Offline store (Parquet, Snowflake, BigQuery) for high-throughput '
                        'batch training; Online store (Redis, DynamoDB) for ultra-low latency real-time inference',
                        'Point-in-time correctness (time-travel / as-of joins) guarantees training data reconstructs '
                        'historical feature states exactly as they were at the event timestamp, preventing future data '
                        'leakage',
                        'Eliminates training-serving skew by sharing a single unified transformation pipeline for both '
                        'offline batch training and online production serving'],
  'model_answer': 'In production MLOps, a Feature Store (such as Feast, Hopsworks, or Tecton) provides a centralized '
                  'data layer managing the lifecycle of machine learning features. It solves two critical failure '
                  'modes: training-serving skew and historical data leakage. A feature store implements a dual-storage '
                  'architecture: 1) an offline store (data warehouse or object storage like Snowflake/Parquet) '
                  'optimized for massive, high-throughput historical batch queries during model training; and 2) an '
                  'online store (low-latency key-value cache like Redis or DynamoDB) serving real-time feature vectors '
                  'in milliseconds during live model inference. It prevents training-serving skew by using identical '
                  'transformation logic for both pipelines. Furthermore, it enforces point-in-time correctness '
                  "('time-travel' or 'as-of' joins): when generating training data for an event that occurred on May "
                  '1st at 2:00 PM, the feature store reconstructs features exactly as they existed at that moment, '
                  'strictly preventing future data leakage from contaminating training datasets.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'A feature store is a centralized platform for managing, sharing, and serving '
                                     'machine learning features. It addresses two massive production headaches: '
                                     'training-serving skew and data leakage. Training-serving skew happens when '
                                     'features are computed differently in batch training than in the live production '
                                     'API; a feature store unifies the transformation pipeline so both use identical '
                                     'definitions. It maintains a dual storage backend: an offline store like BigQuery '
                                     'or Snowflake for generating batch training datasets, and a low-latency online '
                                     'store like Redis for sub-10ms real-time lookups during model inference. Most '
                                     'importantly, it guarantees point-in-time correctness through time-travel '
                                     'joins—meaning when you train on an event that happened six months ago, it pulls '
                                     'the exact feature values that existed at that precise timestamp, preventing '
                                     'future information from leaking into the past.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'A feature store centralizes features so multiple models can share them. It has '
                                     'an offline store like Snowflake for batch training and an online store like '
                                     'Redis for low-latency inference. This prevents training-serving skew because '
                                     'both training and production use the exact same feature definitions. It also '
                                     'handles point-in-time correctness by reconstructing historical feature values '
                                     'without looking ahead into the future.',
                      'missing_concepts': ['Dual-storage architecture: Offline store (Parquet, Snowflake, BigQuery) '
                                           'for high-throughput batch training; Online store (Redis, DynamoDB) for '
                                           'ultra-low latency real-time inference']},
                     {'quality_level': 'average',
                      'human_score': 63,
                      'answer_text': 'A feature store is a database for machine learning features like Feast. It keeps '
                                     "features consistent between training and production so you don't get "
                                     "training-serving skew. It also does time travel queries so you don't leak future "
                                     'data into your training set.',
                      'missing_concepts': ['Dual-storage architecture: Offline store (Parquet, Snowflake, BigQuery) '
                                           'for high-throughput batch training; Online store (Redis, DynamoDB) for '
                                           'ultra-low latency real-time inference',
                                           'Point-in-time correctness (time-travel / as-of joins) guarantees training '
                                           'data reconstructs historical feature states exactly as they were at the '
                                           'event timestamp, preventing future data leakage']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'A feature store is an e-commerce website where data scientists purchase '
                                     'pre-trained neural networks and machine learning APIs with credit cards.',
                      'missing_concepts': ['Feature store acts as centralized repository for discovering, computing, '
                                           'storing, and serving curated ML features across teams',
                                           'Dual-storage architecture: Offline store (Parquet, Snowflake, BigQuery) '
                                           'for high-throughput batch training; Online store (Redis, DynamoDB) for '
                                           'ultra-low latency real-time inference',
                                           'Point-in-time correctness (time-travel / as-of joins) guarantees training '
                                           'data reconstructs historical feature states exactly as they were at the '
                                           'event timestamp, preventing future data leakage',
                                           'Eliminates training-serving skew by sharing a single unified '
                                           'transformation pipeline for both offline batch training and online '
                                           'production serving']}]},
 {'topic_tag': 'Data Drift vs Concept Drift Monitoring',
  'question': 'How do you monitor Population Stability Index (PSI) and Kolmogorov-Smirnov tests to detect data drift '
              'versus concept drift in production models?',
  'keywords': ['Data Drift',
               'Concept Drift',
               'Population Stability Index (PSI)',
               'Kolmogorov-Smirnov (KS) Test',
               'Covariate Shift',
               'Model Monitoring',
               'Ground Truth Lag'],
  'expected_concepts': ['Data drift (covariate shift): distribution of input features P(X) changes over time while the '
                        'underlying relationship P(Y|X) remains constant',
                        'Concept drift: statistical relationship between input features and target variable P(Y|X) '
                        'changes (e.g., consumer behavior shifts post-pandemic)',
                        'Population Stability Index (PSI) measures shift in binned feature distributions: PSI < 0.1 '
                        'indicates stability, 0.1 <= PSI < 0.2 indicates moderate shift, PSI >= 0.2 requires '
                        'retraining',
                        'KS-test compares empirical cumulative distributions (eCDF) of continuous features between '
                        'baseline and production without requiring ground truth labels'],
  'model_answer': 'In production ML monitoring, model performance degrades via two distinct mechanisms: 1) Data drift '
                  '(covariate shift) occurs when the input feature distribution changes over time—P(X_production) != '
                  'P(X_training)—while the conditional relationship P(Y|X) remains static (e.g., marketing attracts a '
                  'younger demographic); 2) Concept drift occurs when the fundamental relationship between inputs and '
                  'targets shifts—P(Y|X_production) != P(Y|X_training)—such as buying habits shifting during '
                  'macro-economic crises. Data drift can be monitored immediately without ground truth labels using '
                  'statistical divergence tests: Kolmogorov-Smirnov (KS) test evaluates the maximum vertical distance '
                  'between empirical cumulative distribution functions (eCDFs) of a continuous feature, flagging drift '
                  'if p < 0.05. The Population Stability Index (PSI) bins features and computes sum((Actual% - '
                  'Expected%) * ln(Actual% / Expected%)). PSI < 0.1 signals stability, 0.1-0.2 indicates moderate '
                  'change, and PSI >= 0.2 triggers mandatory model retraining.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'Data drift is a shift in the distribution of your input features, P(X), while '
                                     'the underlying relationship with the target stays the same. Concept drift is '
                                     'when the actual relationship between inputs and outputs changes, P(Y|X)—like '
                                     'purchasing patterns changing overnight during COVID. You can monitor data drift '
                                     'immediately without waiting for ground truth labels using statistical tests. The '
                                     'Kolmogorov-Smirnov (KS) test compares the empirical cumulative distribution '
                                     'functions (eCDF) of a feature between training and production data to see if the '
                                     'maximum difference is statistically significant. The Population Stability Index '
                                     '(PSI) bins the feature and measures divergence: a PSI under 0.1 means stable, '
                                     'between 0.1 and 0.2 means slight drift, and a PSI over 0.2 indicates significant '
                                     'drift, serving as an automated alert to retrain the model.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'Data drift means your incoming feature distributions P(X) have shifted compared '
                                     'to your training data. Concept drift means the relationship between features and '
                                     'the target P(Y|X) has changed. You can monitor data drift using the KS-test, '
                                     'which compares cumulative distributions, and PSI. A PSI over 0.2 means the '
                                     'population has changed significantly and you need to retrain the model.',
                      'missing_concepts': ['Concept drift: statistical relationship between input features and target '
                                           'variable P(Y|X) changes (e.g., consumer behavior shifts post-pandemic)']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Data drift is when input features change, and concept drift is when the model '
                                     'accuracy drops because consumer habits changed. You use PSI to measure drift, '
                                     'and if PSI is greater than 0.2, you retrain your model. KS test also checks if '
                                     'two distributions are the same.',
                      'missing_concepts': ['Population Stability Index (PSI) measures shift in binned feature '
                                           'distributions: PSI < 0.1 indicates stability, 0.1 <= PSI < 0.2 indicates '
                                           'moderate shift, PSI >= 0.2 requires retraining',
                                           'KS-test compares empirical cumulative distributions (eCDF) of continuous '
                                           'features between baseline and production without requiring ground truth '
                                           'labels']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'Data drift is when your hard drive runs out of storage space, and concept drift '
                                     'is when software engineers forget the original product design requirements.',
                      'missing_concepts': ['Data drift (covariate shift): distribution of input features P(X) changes '
                                           'over time while the underlying relationship P(Y|X) remains constant',
                                           'Concept drift: statistical relationship between input features and target '
                                           'variable P(Y|X) changes (e.g., consumer behavior shifts post-pandemic)',
                                           'Population Stability Index (PSI) measures shift in binned feature '
                                           'distributions: PSI < 0.1 indicates stability, 0.1 <= PSI < 0.2 indicates '
                                           'moderate shift, PSI >= 0.2 requires retraining',
                                           'KS-test compares empirical cumulative distributions (eCDF) of continuous '
                                           'features between baseline and production without requiring ground truth '
                                           'labels']}]},
 {'topic_tag': 'Survival Analysis & Kaplan-Meier Estimator',
  'question': 'How does the Kaplan-Meier estimator construct survival curves while rigorously handling right-censored '
              'observation data?',
  'keywords': ['Survival Analysis',
               'Kaplan-Meier Estimator',
               'Right-Censoring',
               'Hazard Rate',
               'Time-to-Event',
               'Product-Limit Estimator'],
  'expected_concepts': ['Time-to-event data involves right-censoring: subjects leave the study, churn, or the study '
                        'ends before the target event occurs, meaning true event time is unobserved',
                        'Naive approaches (dropping censored rows or treating last contact as event time) severely '
                        'bias survival probability estimates downward or upward',
                        'Kaplan-Meier is a non-parametric product-limit estimator: S(t) = prod_{t_i <= t} [1 - (d_i / '
                        'n_i)], calculating probability of surviving past t_i conditional on surviving just prior',
                        'At each event time t_i, risk set n_i drops by the number of events d_i and censored '
                        'individuals, adjusting the baseline denominator dynamically'],
  'model_answer': 'Survival analysis models time-to-event outcomes (e.g., customer churn, medical mortality, machine '
                  'failure). Standard regression cannot handle this data because of right-censoring: subjects leave '
                  'the study, are lost to follow-up, or remain active when observation terminates, meaning we only '
                  "know their survival duration was 'at least' time t. Dropping censored subjects induces survival "
                  'bias, while treating censoring as failure grossly overestimates hazard. The Kaplan-Meier estimator '
                  'is a non-parametric product-limit estimator that solves this by calculating step-wise conditional '
                  'probabilities: S(t) = prod_{t_i <= t} (1 - d_i / n_i), where t_i are ordered event times, d_i is '
                  'the number of events at t_i, and n_i is the number of subjects at risk just prior to t_i. When a '
                  'censored subject reaches their termination time without failing, they drop out of the risk set n_i '
                  'for subsequent time steps without triggering a downward step in S(t), preserving unbiased '
                  'cumulative survival probabilities.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'Survival analysis models time-to-event data, like customer churn or equipment '
                                     'failure. The primary challenge is right-censoring: when a study ends, many users '
                                     "haven't churned yet, so you only know they survived at least up to that date. If "
                                     'you delete censored users or pretend they failed, you introduce massive '
                                     'statistical bias. The Kaplan-Meier estimator solves this using the product-limit '
                                     'formula: S(t) equals the product of (1 - d_i / n_i) for all event times up to t, '
                                     'where d_i is the number of events and n_i is the number of people at risk. At '
                                     'each failure time, the survival curve takes a downward step proportional to the '
                                     'fraction of remaining subjects who failed. If someone gets censored, they are '
                                     'simply removed from the at-risk denominator n_i for subsequent time steps '
                                     'without causing a downward step in the curve. This produces an unbiased, '
                                     'non-parametric survival curve over time.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'Survival analysis handles time until an event happens, like user churn. '
                                     "Right-censoring happens when someone hasn't experienced the event before the "
                                     "study ends. You can't just delete them or assume they failed. Kaplan-Meier "
                                     'estimates the survival curve as a step function by calculating the fraction of '
                                     'people at risk who survive at each event time. Censored people drop out of the '
                                     'risk pool at their last known time without dropping the survival curve.',
                      'missing_concepts': ['Kaplan-Meier is a non-parametric product-limit estimator: S(t) = prod_{t_i '
                                           '<= t} [1 - (d_i / n_i)], calculating probability of surviving past t_i '
                                           'conditional on surviving just prior']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Kaplan-Meier plots a survival curve that drops down every time an event happens. '
                                     "Right-censored data means patients who didn't die yet or left the study. "
                                     "Kaplan-Meier handles censored data so your survival probabilities don't get "
                                     'messed up.',
                      'missing_concepts': ['Naive approaches (dropping censored rows or treating last contact as event '
                                           'time) severely bias survival probability estimates downward or upward',
                                           'Kaplan-Meier is a non-parametric product-limit estimator: S(t) = prod_{t_i '
                                           '<= t} [1 - (d_i / n_i)], calculating probability of surviving past t_i '
                                           'conditional on surviving just prior']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'The Kaplan-Meier estimator is a tool used in gaming analytics to calculate how '
                                     'many players survive until the end of a battle royale match.',
                      'missing_concepts': ['Time-to-event data involves right-censoring: subjects leave the study, '
                                           'churn, or the study ends before the target event occurs, meaning true '
                                           'event time is unobserved',
                                           'Naive approaches (dropping censored rows or treating last contact as event '
                                           'time) severely bias survival probability estimates downward or upward',
                                           'Kaplan-Meier is a non-parametric product-limit estimator: S(t) = prod_{t_i '
                                           '<= t} [1 - (d_i / n_i)], calculating probability of surviving past t_i '
                                           'conditional on surviving just prior',
                                           'At each event time t_i, risk set n_i drops by the number of events d_i and '
                                           'censored individuals, adjusting the baseline denominator dynamically']}]},
 {'topic_tag': 'Association Rule Mining (Apriori Algorithm)',
  'question': 'Explain how the Apriori algorithm evaluates Support, Confidence, and Lift, and leverages the downward '
              'closure property.',
  'keywords': ['Association Rule Mining',
               'Apriori Algorithm',
               'Support',
               'Confidence',
               'Lift',
               'Downward Closure Property',
               'Market Basket Analysis'],
  'expected_concepts': ['Support measures itemset frequency: P(A union B) = count(A and B) / total transactions',
                        'Confidence measures conditional rule reliability: P(B|A) = Support(A union B) / Support(A)',
                        'Lift evaluates independence: P(B|A) / P(B) = Support(A union B) / [Support(A) * Support(B)]; '
                        'Lift > 1 indicates positive association beyond random chance',
                        'Downward closure (Apriori principle): all subsets of a frequent itemset must also be '
                        'frequent; if an itemset is infrequent, all its supersets are pruned immediately'],
  'model_answer': 'Association Rule Mining discovers co-occurrence patterns in transactional datasets (e.g., market '
                  'basket analysis: {Beer} -> {Diapers}). Rules {A} -> {B} are evaluated via three core metrics: 1) '
                  'Support = count(A and B) / N, representing the proportion of all transactions containing both '
                  'items; 2) Confidence = Support(A union B) / Support(A) = P(B|A), measuring how frequently item B '
                  'appears in transactions containing A; and 3) Lift = Support(A union B) / [Support(A) * Support(B)] '
                  '= P(B|A) / P(B). A Lift of 1 implies independent occurrence; Lift > 1 indicates that purchasing A '
                  'significantly increases the likelihood of purchasing B beyond random chance. The Apriori algorithm '
                  'traverses massive combinatorial itemset spaces efficiently using the Downward Closure Property '
                  '(Apriori Principle): any subset of a frequent itemset must also be frequent. Consequently, if an '
                  'itemset {X} fails the minimum support threshold, all supersets containing {X} are pruned '
                  'immediately without counting, drastically cutting computation.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': "Association rule mining looks for patterns like 'if a customer buys A, they also "
                                     "buy B'. It relies on three metrics: Support is the percentage of all "
                                     'transactions that contain both A and B. Confidence is the conditional '
                                     'probability P(B|A)—out of all baskets containing A, what percentage also had B? '
                                     'Lift measures correlation strength against independence: Lift = Support(A and B) '
                                     '/ (Support(A) * Support(B)). A lift of 1 means A and B are totally independent; '
                                     'lift > 1 proves that buying A actually increases the likelihood of buying B. The '
                                     'computational genius of the Apriori algorithm is the Downward Closure Property: '
                                     'every subset of a frequent itemset must also be frequent. If a 1-itemset like '
                                     '{Cereal} is infrequent, the algorithm immediately prunes every larger '
                                     'combination containing Cereal without checking the database, preventing '
                                     'combinatorial explosion.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'Support is how often items A and B appear together in all transactions. '
                                     'Confidence is the probability of buying B given you bought A. Lift measures if '
                                     'the rule is stronger than random chance—if lift is greater than 1, there is a '
                                     'positive association. The Apriori principle states that if an itemset is '
                                     'infrequent, all its supersets will also be infrequent, which lets the algorithm '
                                     'prune huge branches of combinations.',
                      'missing_concepts': ['Lift evaluates independence: P(B|A) / P(B) = Support(A union B) / '
                                           '[Support(A) * Support(B)]; Lift > 1 indicates positive association beyond '
                                           'random chance']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Apriori is used for market basket analysis to see what items customers buy '
                                     'together like beer and diapers. Support is how common the items are, confidence '
                                     'is how sure the rule is, and lift tells you if the items are correlated. Apriori '
                                     "prunes items that don't have enough support.",
                      'missing_concepts': ['Confidence measures conditional rule reliability: P(B|A) = Support(A union '
                                           'B) / Support(A)',
                                           'Downward closure (Apriori principle): all subsets of a frequent itemset '
                                           'must also be frequent; if an itemset is infrequent, all its supersets are '
                                           'pruned immediately']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'The Apriori algorithm is a supervised deep learning algorithm used to train '
                                     'autonomous self-driving cars.',
                      'missing_concepts': ['Support measures itemset frequency: P(A union B) = count(A and B) / total '
                                           'transactions',
                                           'Confidence measures conditional rule reliability: P(B|A) = Support(A union '
                                           'B) / Support(A)',
                                           'Lift evaluates independence: P(B|A) / P(B) = Support(A union B) / '
                                           '[Support(A) * Support(B)]; Lift > 1 indicates positive association beyond '
                                           'random chance',
                                           'Downward closure (Apriori principle): all subsets of a frequent itemset '
                                           'must also be frequent; if an itemset is infrequent, all its supersets are '
                                           'pruned immediately']}]},
 {'topic_tag': 'Multi-Armed Bandits vs A/B Testing',
  'question': 'Why do Multi-Armed Bandit algorithms minimize regret faster than traditional fixed-horizon A/B testing '
              'in dynamic environments?',
  'keywords': ['Multi-Armed Bandit',
               'A/B Testing',
               'Regret Minimization',
               'Exploration vs Exploitation',
               'Epsilon-Greedy',
               'Thompson Sampling',
               'Dynamic Allocation'],
  'expected_concepts': ['Traditional A/B testing enforces a rigid 50/50 split across a fixed time horizon, incurring '
                        'high opportunity cost (regret) by exposing 50% of users to an inferior variant',
                        'Multi-Armed Bandits dynamically balance the Exploration vs Exploitation trade-off in '
                        'real-time, routing increasing traffic to winning arms as evidence accumulates',
                        'Bandit algorithms (e.g., Epsilon-Greedy, Upper Confidence Bound [UCB], Thompson Sampling) '
                        'mathematically minimize cumulative regret',
                        'A/B testing is preferred when clean statistical inference and unbiased hypothesis testing are '
                        'required; Bandits are preferred for short-lived optimization (e.g., Black Friday headlines)'],
  'model_answer': 'Traditional A/B testing operates on a fixed-horizon exploration paradigm: traffic is split equally '
                  '(e.g., 50% variant A, 50% variant B) until statistical power is achieved. While optimal for '
                  'unbiased scientific inference and clean p-value calculation, it incurs substantial opportunity cost '
                  '(cumulative regret) by routing half your traffic to a demonstrably losing variant throughout the '
                  'test duration. Multi-Armed Bandit (MAB) algorithms directly address this by dynamically balancing '
                  'exploration (gathering information on uncertain variants) and exploitation (capitalizing on the '
                  'current best variant). Algorithms like Thompson Sampling or UCB1 route increasing traffic shares to '
                  'higher-performing variants in real-time as evidence mounts. MAB minimizes cumulative regret '
                  'exponentially faster, making it vastly superior for short-lifecycle opportunities (e.g., holiday '
                  'promotions, news headlines) where maximizing conversions outweighs strict parameter estimation.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'In a standard A/B test, you commit to a fixed 50/50 traffic split for a fixed '
                                     'duration. If variant B is significantly worse, you still force 50% of your users '
                                     'to see it for two weeks, suffering massive opportunity cost—known as cumulative '
                                     'regret. Multi-Armed Bandits solve the exploration versus exploitation dilemma '
                                     'dynamically: they start by testing all variants, but as soon as one variant '
                                     'starts pulling ahead, algorithms like Thompson Sampling or UCB dynamically shift '
                                     'more traffic to the winning variant while continuing to allocate a small '
                                     'percentage to explore the others. Bandits mathematically minimize regret, making '
                                     'them ideal for short-lived promotions or ad campaigns where your primary goal is '
                                     'maximizing revenue rather than computing a pure p-value.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'A/B testing sends 50% of traffic to both variants for the whole duration, which '
                                     'loses money if one variant is clearly worse. Multi-Armed Bandits solve the '
                                     'exploration vs exploitation tradeoff by dynamically shifting traffic to the '
                                     'winning variant as data comes in. Algorithms like Epsilon-Greedy or Thompson '
                                     'Sampling minimize regret, making them great for short promotions like Black '
                                     'Friday sales.',
                      'missing_concepts': ['A/B testing is preferred when clean statistical inference and unbiased '
                                           'hypothesis testing are required; Bandits are preferred for short-lived '
                                           'optimization (e.g., Black Friday headlines)']},
                     {'quality_level': 'average',
                      'human_score': 63,
                      'answer_text': 'Multi-armed bandits are better than A/B tests because they automatically send '
                                     'more users to the better option instead of keeping it 50-50. This reduces regret '
                                     'and makes more money during marketing tests.',
                      'missing_concepts': ['Multi-Armed Bandits dynamically balance the Exploration vs Exploitation '
                                           'trade-off in real-time, routing increasing traffic to winning arms as '
                                           'evidence accumulates',
                                           'A/B testing is preferred when clean statistical inference and unbiased '
                                           'hypothesis testing are required; Bandits are preferred for short-lived '
                                           'optimization (e.g., Black Friday headlines)']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'Multi-armed bandit is a casino game algorithm used to hack online slot machines, '
                                     'and has no application in web development.',
                      'missing_concepts': ['Traditional A/B testing enforces a rigid 50/50 split across a fixed time '
                                           'horizon, incurring high opportunity cost (regret) by exposing 50% of users '
                                           'to an inferior variant',
                                           'Multi-Armed Bandits dynamically balance the Exploration vs Exploitation '
                                           'trade-off in real-time, routing increasing traffic to winning arms as '
                                           'evidence accumulates',
                                           'Bandit algorithms (e.g., Epsilon-Greedy, Upper Confidence Bound [UCB], '
                                           'Thompson Sampling) mathematically minimize cumulative regret',
                                           'A/B testing is preferred when clean statistical inference and unbiased '
                                           'hypothesis testing are required; Bandits are preferred for short-lived '
                                           'optimization (e.g., Black Friday headlines)']}]},
 {'topic_tag': 'Augmented Dickey-Fuller Stationarity Test',
  'question': 'How does the Augmented Dickey-Fuller (ADF) test verify unit root non-stationarity in autoregressive '
              'time series models?',
  'keywords': ['ADF Test',
               'Augmented Dickey-Fuller',
               'Unit Root',
               'Stationarity',
               'Autoregressive AR(p)',
               'P-value',
               'Differencing'],
  'expected_concepts': ['Null hypothesis H0 posits presence of a unit root (gamma = 0 / phi = 1), meaning the time '
                        'series is non-stationary and has a stochastic trend',
                        'Alternative hypothesis H1 posits the process is stationary (gamma < 0), meaning shocks '
                        'dissipate over time',
                        'Augmented aspect includes lagged first-difference terms Delta Y_{t-k} to absorb higher-order '
                        'serial correlation in residuals',
                        'Decision rule: if ADF test statistic is more negative than the critical value (p-value < '
                        '0.05), reject H0, concluding the series is stationary'],
  'model_answer': 'The Augmented Dickey-Fuller (ADF) test is a formal hypothesis test to determine whether a '
                  'univariate time series possesses a unit root, which indicates non-stationarity. It fits the '
                  'regression: Delta Y_t = alpha + beta * t + gamma * Y_{t-1} + sum_{k=1}^p delta_k * Delta Y_{t-k} + '
                  "epsilon_t. The 'augmented' lagged differences Delta Y_{t-k} are crucial: they absorb higher-order "
                  'autoregressive serial correlation in error terms. The Null Hypothesis H0 is gamma = 0 (equivalent '
                  'to autoregressive coefficient phi = 1, a unit root exists, indicating non-stationarity). The '
                  'Alternative Hypothesis H1 is gamma < 0 (the series is stationary). Because the test statistic does '
                  "not follow a standard Student's t-distribution under the null, Dickey-Fuller critical values are "
                  'used. If the ADF test statistic is strictly more negative than critical thresholds (or p < 0.05), '
                  'we reject H0 and confirm stationarity.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'The Augmented Dickey-Fuller (ADF) test checks whether a time series has a unit '
                                     'root, which makes it non-stationary. The null hypothesis H0 is that a unit root '
                                     'exists (gamma = 0), meaning the series is non-stationary and exhibits a random '
                                     'walk trend. The alternative hypothesis H1 is that the series is stationary. The '
                                     "'augmented' part refers to adding lagged differences of the series into the "
                                     'regression to eliminate serial correlation in the error terms. Because the test '
                                     'statistic follows a non-standard Dickey-Fuller distribution, you look for a '
                                     'strongly negative test statistic: if the p-value is less than 0.05 (test '
                                     'statistic more negative than critical values), you reject the null hypothesis '
                                     'and conclude the time series is stationary.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'The ADF test checks if a time series has a unit root. The null hypothesis is '
                                     'that the series has a unit root and is non-stationary. The alternative is that '
                                     'it is stationary. The augmented part adds lagged differences to remove '
                                     'autocorrelation in the residuals. If the p-value is below 0.05, you reject the '
                                     'null hypothesis and know the series is stationary.',
                      'missing_concepts': ['Null hypothesis H0 posits presence of a unit root (gamma = 0 / phi = 1), '
                                           'meaning the time series is non-stationary and has a stochastic trend']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'ADF test tests if your time series is stationary before you run ARIMA. The null '
                                     "hypothesis is that it's not stationary. If the p-value is less than 0.05, you "
                                     "reject the null and say the data is stationary. If it's not, you have to "
                                     'difference the data.',
                      'missing_concepts': ['Augmented aspect includes lagged first-difference terms Delta Y_{t-k} to '
                                           'absorb higher-order serial correlation in residuals',
                                           'Decision rule: if ADF test statistic is more negative than the critical '
                                           'value (p-value < 0.05), reject H0, concluding the series is stationary']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'The Dickey-Fuller test is used to measure audio distortion in microphone '
                                     'frequencies for speech recognition models.',
                      'missing_concepts': ['Null hypothesis H0 posits presence of a unit root (gamma = 0 / phi = 1), '
                                           'meaning the time series is non-stationary and has a stochastic trend',
                                           'Alternative hypothesis H1 posits the process is stationary (gamma < 0), '
                                           'meaning shocks dissipate over time',
                                           'Augmented aspect includes lagged first-difference terms Delta Y_{t-k} to '
                                           'absorb higher-order serial correlation in residuals',
                                           'Decision rule: if ADF test statistic is more negative than the critical '
                                           'value (p-value < 0.05), reject H0, concluding the series is stationary']}]},
 {'topic_tag': 'SQL Self-Joins & Hierarchical Data',
  'question': 'How do SQL self-joins and recursive CTEs query parent-child hierarchical trees (e.g., employee manager '
              'relationships)?',
  'keywords': ['SQL Self-Join',
               'Recursive CTE',
               'Hierarchical Data',
               'Parent-Child Adjacency List',
               'Anchor Member',
               'Recursive Member',
               'Termination Condition'],
  'expected_concepts': ['A self-join joins a table to itself using distinct aliases (e.g., employees e JOIN employees '
                        'm ON e.manager_id = m.employee_id) to resolve single-level parent-child pairs',
                        'Self-joins only resolve a fixed, predetermined depth (e.g., employee to direct manager); '
                        'traversing arbitrary tree depths requires recursive CTEs',
                        'Recursive CTE consists of an Anchor Member (base query selecting root nodes, e.g. CEO where '
                        'manager_id IS NULL) UNION ALL a Recursive Member',
                        'Recursive Member joins the previous iteration result back to the base table, incrementing '
                        'depth level until the join returns empty (termination condition)'],
  'model_answer': 'In relational schemas, hierarchical data (such as organizational charts or bill-of-materials) is '
                  'typically modeled as an adjacency list with a foreign key referencing the primary key of the same '
                  'table (e.g., manager_id -> employee_id). A self-join joins the table to itself using distinct '
                  "aliases: 'FROM employees e LEFT JOIN employees m ON e.manager_id = m.employee_id'. However, "
                  'self-joins can only traverse fixed, predetermined hierarchy depths (requiring N joins for N '
                  'levels). To query arbitrary, unknown hierarchy depths, modern SQL uses Recursive CTEs (WITH '
                  'RECURSIVE). A recursive CTE comprises: 1) an Anchor Member selecting root nodes (e.g., WHERE '
                  'manager_id IS NULL, depth=1); 2) UNION ALL; and 3) a Recursive Member that joins the anchor result '
                  'set back to the base table on parent-child keys, incrementing a depth counter. The engine executes '
                  'iteratively until the recursive join produces zero rows, terminating automatically.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'When you have parent-child hierarchies like an employee table with a manager_id '
                                     "column, a self-join joins the table to itself with two aliases: 'FROM employees "
                                     "e LEFT JOIN employees m ON e.manager_id = m.employee_id'. That works fine for "
                                     "one level, like finding an employee's direct manager. But if you need to "
                                     'traverse an entire org tree of arbitrary depth, self-joins fail because you '
                                     "don't know how many joins to write. For arbitrary depth, you use a Recursive CTE "
                                     'with two parts: the Anchor Member selects the root nodes—like the CEO where '
                                     'manager_id IS NULL—and then UNION ALL connects to the Recursive Member, which '
                                     'joins the previous recursive result back to the employees table. The database '
                                     'repeats this step level-by-level until it hits leaves and returns zero rows, '
                                     'terminating the recursion.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'A self-join joins a table to itself using aliases, like employees e JOIN '
                                     'employees m ON e.manager_id = m.id, to find who reports to whom. For multi-level '
                                     "hierarchies where you don't know the depth, you use a recursive CTE. It starts "
                                     'with an anchor query finding the top-level bosses, and a recursive query that '
                                     'joins down through each reporting layer until there are no more employees left.',
                      'missing_concepts': ['Recursive Member joins the previous iteration result back to the base '
                                           'table, incrementing depth level until the join returns empty (termination '
                                           'condition)']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'A self-join is joining a table to itself with two different names like a and b '
                                     'to see managers and employees. If you want to get the whole tree of an '
                                     'organization, you have to use a recursive CTE with UNION ALL until it finishes.',
                      'missing_concepts': ['Self-joins only resolve a fixed, predetermined depth (e.g., employee to '
                                           'direct manager); traversing arbitrary tree depths requires recursive CTEs',
                                           'Recursive CTE consists of an Anchor Member (base query selecting root '
                                           'nodes, e.g. CEO where manager_id IS NULL) UNION ALL a Recursive Member']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'Self-joins are prohibited in SQL because joining a table to itself causes an '
                                     'infinite recursion loop that crashes the server.',
                      'missing_concepts': ['A self-join joins a table to itself using distinct aliases (e.g., '
                                           'employees e JOIN employees m ON e.manager_id = m.employee_id) to resolve '
                                           'single-level parent-child pairs',
                                           'Self-joins only resolve a fixed, predetermined depth (e.g., employee to '
                                           'direct manager); traversing arbitrary tree depths requires recursive CTEs',
                                           'Recursive CTE consists of an Anchor Member (base query selecting root '
                                           'nodes, e.g. CEO where manager_id IS NULL) UNION ALL a Recursive Member',
                                           'Recursive Member joins the previous iteration result back to the base '
                                           'table, incrementing depth level until the join returns empty (termination '
                                           'condition)']}]}]

