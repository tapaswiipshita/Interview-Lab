# Data Science Hard Questions (25 questions)

QUESTIONS = [{'topic_tag': 'Causal Inference & Propensity Score Matching',
  'question': 'Explain how Propensity Score Matching eliminates confounding bias to estimate Average Treatment Effects '
              'in observational studies.',
  'keywords': ['Causal Inference',
               'Propensity Score Matching',
               'Confounding Bias',
               'Average Treatment Effect (ATE)',
               'Counterfactual',
               'Conditional Independence'],
  'expected_concepts': ['Confounding bias: in observational studies, treatment assignment is non-random, correlated '
                        'with confounders X affecting both treatment and outcome',
                        'Propensity score e(X) = P(T=1 | X): probability of receiving treatment given baseline '
                        'covariates, collapsing high-dimensional confounders into a scalar metric',
                        'Rosenbaum & Rubin theorem: conditional on e(X), treatment assignment and potential outcomes '
                        '(Y(1), Y(0)) are conditionally independent (Unconfoundedness)',
                        'Matching algorithms (nearest neighbor, caliper matching) pair treated and control units with '
                        'identical propensity scores, ensuring covariate balance across common support'],
  'model_answer': 'In observational studies, estimating the Average Treatment Effect (ATE = E[Y(1) - Y(0)]) is '
                  'corrupted by confounding bias because treatment assignment T is non-random and confounded by '
                  'pre-treatment covariates X that simultaneously influence treatment probability and outcome Y. '
                  'Rosenbaum and Rubin (1983) proved the Propensity Score Theorem: the propensity score e(X) = P(T=1 | '
                  'X), estimated via logistic regression or gradient boosting, acts as a balancing score. Conditional '
                  'on e(X), treatment assignment T is statistically independent of potential outcomes (Y(0), Y(1)), '
                  'satisfying the unconfoundedness assumption. Propensity Score Matching (PSM) matches each treated '
                  'observation with one or more control observations possessing identical (or nearest-neighbor within '
                  'caliper) propensity scores. This effectively reconstructs a pseudo-randomized trial across the '
                  'region of common support, balancing covariate distributions between cohorts and eliminating overt '
                  'selection bias.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'In observational data, you cannot simply compare the average outcome of treated '
                                     'versus untreated groups because of confounding bias: the covariates that drive '
                                     'someone to take the treatment also affect the outcome. Propensity score matching '
                                     'solves this by reducing multidimensional confounders down to a single balancing '
                                     'scalar: the propensity score e(X), which is the predicted probability of '
                                     'receiving treatment given baseline covariates X. Rosenbaum and Rubin proved that '
                                     'if unconfoundedness holds, conditioning on the propensity score makes treatment '
                                     'assignment conditionally independent of potential outcomes. By pairing each '
                                     'treated individual with a control individual who had the same propensity score '
                                     '(using nearest neighbor or caliper matching over the region of common support), '
                                     'you simulate a randomized controlled trial and balance the covariate '
                                     'distributions, enabling an unbiased estimate of the Average Treatment Effect.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': "In observational studies, treatment isn't random, so confounders bias your "
                                     'treatment effect. Propensity score matching models the probability of getting '
                                     'treated based on covariates using logistic regression. Then it matches treated '
                                     'people to untreated people who had the same propensity score. This balances the '
                                     'covariates between groups across common support, allowing you to estimate the '
                                     'Average Treatment Effect without confounding bias.',
                      'missing_concepts': ['Rosenbaum & Rubin theorem: conditional on e(X), treatment assignment and '
                                           'potential outcomes (Y(1), Y(0)) are conditionally independent '
                                           '(Unconfoundedness)']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': "Propensity score matching is used in causal inference when you can't run an A/B "
                                     'test. You calculate a propensity score which is the probability of getting '
                                     'treatment. Then you match users with similar scores from control and treatment. '
                                     'This removes confounding variables so you can calculate the treatment effect.',
                      'missing_concepts': ['Confounding bias: in observational studies, treatment assignment is '
                                           'non-random, correlated with confounders X affecting both treatment and '
                                           'outcome',
                                           'Rosenbaum & Rubin theorem: conditional on e(X), treatment assignment and '
                                           'potential outcomes (Y(1), Y(0)) are conditionally independent '
                                           '(Unconfoundedness)']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'Propensity score matching is an algorithmic trading technique used to match buy '
                                     'orders and sell orders on the stock market based on trading volume.',
                      'missing_concepts': ['Confounding bias: in observational studies, treatment assignment is '
                                           'non-random, correlated with confounders X affecting both treatment and '
                                           'outcome',
                                           'Propensity score e(X) = P(T=1 | X): probability of receiving treatment '
                                           'given baseline covariates, collapsing high-dimensional confounders into a '
                                           'scalar metric',
                                           'Rosenbaum & Rubin theorem: conditional on e(X), treatment assignment and '
                                           'potential outcomes (Y(1), Y(0)) are conditionally independent '
                                           '(Unconfoundedness)',
                                           'Matching algorithms (nearest neighbor, caliper matching) pair treated and '
                                           'control units with identical propensity scores, ensuring covariate balance '
                                           'across common support']}]},
 {'topic_tag': 'Advanced Time Series (SARIMAX & GARCH)',
  'question': 'How do SARIMAX models integrate exogenous factors while GARCH models capture time-varying volatility '
              'clustering?',
  'keywords': ['SARIMAX',
               'GARCH',
               'Exogenous Regressors',
               'Volatility Clustering',
               'Conditional Heteroscedasticity',
               'ARCH Effects',
               'Time Series Forecasting'],
  'expected_concepts': ['SARIMAX extends seasonal ARIMA by adding linear regression on external exogenous features X_t '
                        'alongside autoregressive and moving average terms',
                        'Standard ARIMA assumes homoscedasticity (constant error variance sigma^2 over time), failing '
                        'on financial data exhibiting volatility clustering',
                        'GARCH(p, q) models conditional variance sigma_t^2 as an autoregressive process of lagged '
                        'squared residuals (ARCH terms) and lagged conditional variances (GARCH terms)',
                        'Combined workflow: SARIMAX models conditional mean trajectory while GARCH models conditional '
                        'heteroscedasticity / volatility dynamics'],
  'model_answer': 'SARIMAX and GARCH address two distinct aspects of time series modeling: conditional mean dynamics '
                  'versus conditional variance dynamics. SARIMAX(p,d,q)(P,D,Q)_s integrates seasonal differencing and '
                  'autoregressive/moving average operators with exogenous explanatory covariates X_t through linear '
                  'regression residuals: Y_t = beta * X_t + eta_t, where error eta_t follows a seasonal ARIMA process. '
                  'However, SARIMAX assumes homoscedasticity—constant error variance sigma^2. In financial and energy '
                  "series, data displays 'volatility clustering' (periods of high turbulence followed by relative "
                  'calm), termed conditional heteroscedasticity. GARCH(p,q) (Generalized Autoregressive Conditional '
                  'Heteroscedasticity) explicitly models this variance evolution: sigma_t^2 = omega + sum_{i=1}^q '
                  'alpha_i * epsilon_{t-i}^2 + sum_{j=1}^p beta_j * sigma_{t-j}^2. The combined pipeline fits SARIMAX '
                  'to model the conditional mean and passes the resulting residuals into GARCH to forecast volatility '
                  'and Value-at-Risk.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'SARIMAX and GARCH tackle completely different components of a time series: the '
                                     'mean versus the variance. SARIMAX models the conditional mean, combining '
                                     'seasonal ARIMA lag structures with external exogenous variables (like marketing '
                                     'spend or weather) through linear coefficients beta * X_t. But SARIMAX assumes '
                                     'constant error variance. In real-world financial assets, markets exhibit '
                                     'volatility clustering—where big price swings cluster together, violating '
                                     'homoscedasticity. GARCH models this conditional heteroscedasticity directly by '
                                     'modeling the variance sigma_t^2 as a dynamic process driven by past squared '
                                     'shocks (alpha * epsilon_{t-1}^2) and past forecasted variances (beta * '
                                     'sigma_{t-1}^2). In practice, you use SARIMAX to forecast the expected future '
                                     'value, and then fit GARCH on the SARIMAX residuals to forecast confidence '
                                     'intervals and volatility risk.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'SARIMAX adds exogenous external variables to seasonal ARIMA models so you can '
                                     'include predictors like promotions or temperature. However, ARIMA assumes '
                                     'constant variance. GARCH models time-varying volatility clustering, where '
                                     'periods of high variance group together. GARCH predicts the conditional variance '
                                     'using past squared errors and past variances. Often you fit SARIMAX for the mean '
                                     'prediction and GARCH for the risk and volatility bands.',
                      'missing_concepts': ['SARIMAX extends seasonal ARIMA by adding linear regression on external '
                                           'exogenous features X_t alongside autoregressive and moving average terms']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'SARIMAX is ARIMA with exogenous variables, meaning you can add other columns as '
                                     'inputs. GARCH is for stock volatility and measures risk when price changes '
                                     'cluster together. SARIMAX predicts the price and GARCH predicts the variance.',
                      'missing_concepts': ['Standard ARIMA assumes homoscedasticity (constant error variance sigma^2 '
                                           'over time), failing on financial data exhibiting volatility clustering',
                                           'GARCH(p, q) models conditional variance sigma_t^2 as an autoregressive '
                                           'process of lagged squared residuals (ARCH terms) and lagged conditional '
                                           'variances (GARCH terms)']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'SARIMAX is a database compression codec for Apache Kafka streams, and GARCH is '
                                     'an image segmentation neural network.',
                      'missing_concepts': ['SARIMAX extends seasonal ARIMA by adding linear regression on external '
                                           'exogenous features X_t alongside autoregressive and moving average terms',
                                           'Standard ARIMA assumes homoscedasticity (constant error variance sigma^2 '
                                           'over time), failing on financial data exhibiting volatility clustering',
                                           'GARCH(p, q) models conditional variance sigma_t^2 as an autoregressive '
                                           'process of lagged squared residuals (ARCH terms) and lagged conditional '
                                           'variances (GARCH terms)',
                                           'Combined workflow: SARIMAX models conditional mean trajectory while GARCH '
                                           'models conditional heteroscedasticity / volatility dynamics']}]},
 {'topic_tag': 'A/B Testing Variance Reduction (CUPED)',
  'question': 'How does the CUPED technique use pre-experiment covariate data to reduce metric variance and accelerate '
              'A/B test runtimes?',
  'keywords': ['CUPED',
               'Variance Reduction',
               'A/B Testing',
               'Covariate Adjustment',
               'Pre-Experiment Data',
               'Linear Regression',
               'Sample Size Efficiency'],
  'expected_concepts': ['CUPED (Controlled-experiment Using Pre-Experiment Data) exploits correlation between '
                        'pre-experiment metric X and in-experiment metric Y',
                        'Defines adjusted metric Y_cuped = Y - theta * (X - E[X]), where optimal scalar theta = Cov(Y, '
                        'X) / Var(X)',
                        'Variance of adjusted metric shrinks by factor (1 - rho^2): Var(Y_cuped) = Var(Y) * (1 - '
                        'rho^2), where rho is correlation between X and Y',
                        'Shrunk variance allows experiments to reach statistical significance with dramatically '
                        'smaller sample sizes (or 40-50% shorter runtimes) without introducing bias'],
  'model_answer': 'CUPED (Controlled-experiment Using Pre-Experiment Data), popularized by Deng et al. at Microsoft, '
                  'is a variance reduction technique that accelerates online experimentation without altering traffic '
                  'allocation. It leverages the historical pre-experiment value of the metric (or a correlated '
                  'covariate X) measured prior to test assignment. The CUPED-adjusted metric is formulated as: Y_cuped '
                  '= Y - theta * (X - E[X]). Because E[X] is identical between randomized groups, E[Y_cuped] = E[Y], '
                  'guaranteeing unbiased treatment effect estimation. The optimal coefficient that minimizes variance '
                  'is theta = Cov(Y, X) / Var(X), identical to OLS regression. The resulting variance of the estimator '
                  'shrinks to: Var(Y_cuped) = Var(Y) * (1 - rho^2), where rho = Corr(Y, X). If historical user '
                  'activity correlates strongly with experimental activity (e.g., rho = 0.7), variance drops by ~50%, '
                  'effectively doubling sample efficiency and slashing required experiment runtimes in half.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'CUPED reduces metric variance in A/B tests by using pre-experiment data to '
                                     "remove pre-existing user noise. If you're measuring user revenue during a test "
                                     '(Y), users who spent a lot before the test (X) will naturally spend a lot during '
                                     'the test. CUPED creates an adjusted metric: Y_cuped = Y - theta * (X - E[X]), '
                                     'where theta is Cov(Y, X) / Var(X). Because randomization guarantees that '
                                     'pre-experiment expected values are identical between control and treatment, this '
                                     'adjustment is mathematically unbiased. The variance of the adjusted metric drops '
                                     'to Var(Y) * (1 - rho^2), where rho is the correlation between pre- and '
                                     'post-metrics. If rho is 0.7, rho squared is ~0.5, meaning you eliminate 50% of '
                                     'the variance. This allows you to detect the same Minimum Detectable Effect with '
                                     'half the sample size, cutting required test duration in half.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': "CUPED uses pre-experiment data, like a user's activity before the A/B test "
                                     'started, to adjust the in-experiment metric Y. The formula is Y_cuped = Y - '
                                     'theta * (X - E[X]), where theta is based on covariance. The variance reduction '
                                     'is proportional to 1 minus the correlation squared. With lower variance, you can '
                                     'reach statistical significance much faster and detect smaller effect sizes '
                                     'without needing more users.',
                      'missing_concepts': ['Shrunk variance allows experiments to reach statistical significance with '
                                           'dramatically smaller sample sizes (or 40-50% shorter runtimes) without '
                                           'introducing bias']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'CUPED is a method developed by Microsoft to make A/B tests run faster. It uses '
                                     'historical user data from before the experiment to reduce the variance of your '
                                     'test metric. Because the variance is smaller, your p-values become significant '
                                     'faster so you can end the test earlier.',
                      'missing_concepts': ['Defines adjusted metric Y_cuped = Y - theta * (X - E[X]), where optimal '
                                           'scalar theta = Cov(Y, X) / Var(X)',
                                           'Variance of adjusted metric shrinks by factor (1 - rho^2): Var(Y_cuped) = '
                                           'Var(Y) * (1 - rho^2), where rho is correlation between X and Y']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'CUPED is a frontend JavaScript caching library that speeds up website page load '
                                     'times during browser rendering.',
                      'missing_concepts': ['CUPED (Controlled-experiment Using Pre-Experiment Data) exploits '
                                           'correlation between pre-experiment metric X and in-experiment metric Y',
                                           'Defines adjusted metric Y_cuped = Y - theta * (X - E[X]), where optimal '
                                           'scalar theta = Cov(Y, X) / Var(X)',
                                           'Variance of adjusted metric shrinks by factor (1 - rho^2): Var(Y_cuped) = '
                                           'Var(Y) * (1 - rho^2), where rho is correlation between X and Y',
                                           'Shrunk variance allows experiments to reach statistical significance with '
                                           'dramatically smaller sample sizes (or 40-50% shorter runtimes) without '
                                           'introducing bias']}]},
 {'topic_tag': 'Multiple Testing Correction (FDR)',
  'question': 'Contrast Bonferroni family-wise error rate control with the Benjamini-Hochberg False Discovery Rate '
              'procedure in high-dimensional hypothesis testing.',
  'keywords': ['Multiple Testing',
               'Bonferroni Correction',
               'Benjamini-Hochberg (BH)',
               'Family-Wise Error Rate (FWER)',
               'False Discovery Rate (FDR)',
               'p-hacking',
               'Genomics/Feature Selection'],
  'expected_concepts': ['Multiple testing problem: testing m simultaneous hypotheses at alpha = 0.05 inflates '
                        'probability of at least one false positive to 1 - (1 - alpha)^m (e.g., m=100 gives 99.4% '
                        'false positive risk)',
                        'Bonferroni controls FWER (probability of >= 1 false positive): adjusts alpha_adj = alpha / m; '
                        'extremely conservative, causing severe loss of statistical power and high Type II errors',
                        'Benjamini-Hochberg controls FDR (expected proportion of false discoveries among rejected '
                        'nulls): FDR = E[V / R]',
                        'BH procedure sorts p-values in ascending order and finds largest k such that p_(k) <= (k / m) '
                        '* Q, offering substantially higher statistical power while controlling false discovery '
                        'fraction'],
  'model_answer': 'When simultaneously testing m independent hypotheses (e.g., evaluating 10,000 genes or 50 A/B test '
                  'metric variations), the probability of committing at least one Type I error inflates exponentially: '
                  'FWER = 1 - (1 - alpha)^m. Bonferroni correction controls the Family-Wise Error Rate (FWER = P(V >= '
                  '1)) by requiring individual p-values to satisfy p_i <= alpha / m. While strictly bounding the '
                  'chance of even a single false positive, Bonferroni is savagely conservative in high dimensions, '
                  'devastating statistical power and causing pervasive Type II errors (false negatives). The '
                  'Benjamini-Hochberg (BH) procedure redefines the objective by controlling the False Discovery Rate '
                  '(FDR = E[V / R | R > 0]), which is the expected proportion of false rejections among all rejected '
                  'hypotheses. The BH algorithm sorts m p-values in ascending order (p_(1) <= ... <= p_(m)) and finds '
                  'the largest rank k satisfying p_(k) <= (k / m) * Q (target FDR). Rejecting all hypotheses from 1 to '
                  'k preserves immense statistical power while rigorously capping false discoveries at rate Q.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'When you test hundreds of hypotheses at once, the probability of getting at '
                                     'least one false positive balloons to near 100%. Bonferroni controls the '
                                     'Family-Wise Error Rate (FWER)—the probability of making even a single false '
                                     'positive—by dividing alpha by the number of tests m (alpha / m). That makes it '
                                     'practically impossible to find anything when m is large, killing statistical '
                                     'power and causing massive Type II errors. Benjamini-Hochberg takes a much more '
                                     'practical approach by controlling the False Discovery Rate (FDR), which is the '
                                     'expected proportion of false positives among all rejected discoveries (V / R). '
                                     'The procedure sorts all m p-values in ascending order and finds the highest rank '
                                     'k where p_k <= (k / m) * Q. It rejects all hypotheses up to rank k. This gives '
                                     'you vastly higher statistical power than Bonferroni while guaranteeing that only '
                                     'an acceptable fraction (e.g., 5%) of your discoveries are false alarms.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'Testing multiple hypotheses increases false positives. Bonferroni controls '
                                     'family-wise error rate by dividing alpha by m, but it is way too strict when you '
                                     'test thousands of features, missing true signals. Benjamini-Hochberg controls '
                                     'the False Discovery Rate, which is the percentage of false positives among your '
                                     'rejected tests. BH sorts p-values and applies an adaptive cutoff based on rank '
                                     '(k/m * Q), keeping much better statistical power.',
                      'missing_concepts': ['Multiple testing problem: testing m simultaneous hypotheses at alpha = '
                                           '0.05 inflates probability of at least one false positive to 1 - (1 - '
                                           'alpha)^m (e.g., m=100 gives 99.4% false positive risk)']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'If you run 100 tests at p < 0.05, you will get 5 false positives by chance. '
                                     "Bonferroni divides 0.05 by the number of tests so you don't get false positives, "
                                     "but it's very conservative. Benjamini-Hochberg is better because it controls "
                                     'false discovery rate by sorting p-values.',
                      'missing_concepts': ['Bonferroni controls FWER (probability of >= 1 false positive): adjusts '
                                           'alpha_adj = alpha / m; extremely conservative, causing severe loss of '
                                           'statistical power and high Type II errors',
                                           'BH procedure sorts p-values in ascending order and finds largest k such '
                                           'that p_(k) <= (k / m) * Q, offering substantially higher statistical power '
                                           'while controlling false discovery fraction']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'The Bonferroni correction is an encryption key used in blockchain, and '
                                     'Benjamini-Hochberg is a neural network loss function.',
                      'missing_concepts': ['Multiple testing problem: testing m simultaneous hypotheses at alpha = '
                                           '0.05 inflates probability of at least one false positive to 1 - (1 - '
                                           'alpha)^m (e.g., m=100 gives 99.4% false positive risk)',
                                           'Bonferroni controls FWER (probability of >= 1 false positive): adjusts '
                                           'alpha_adj = alpha / m; extremely conservative, causing severe loss of '
                                           'statistical power and high Type II errors',
                                           'Benjamini-Hochberg controls FDR (expected proportion of false discoveries '
                                           'among rejected nulls): FDR = E[V / R]',
                                           'BH procedure sorts p-values in ascending order and finds largest k such '
                                           'that p_(k) <= (k / m) * Q, offering substantially higher statistical power '
                                           'while controlling false discovery fraction']}]},
 {'topic_tag': 'Apache Spark Architecture & Catalyst Optimizer',
  'question': "Detail how Apache Spark's Catalyst Optimizer transforms DataFrame code from Unresolved Logical Plan to "
              'optimized Physical Execution Plan.',
  'keywords': ['Apache Spark',
               'Catalyst Optimizer',
               'Tungsten Engine',
               'Logical Plan',
               'Physical Plan',
               'Predicate Pushdown',
               'Whole-Stage Code Generation'],
  'expected_concepts': ['Analysis phase: validates unresolved logical plan against the Spark Catalog to resolve column '
                        'names and data types, producing a Resolved Logical Plan',
                        'Logical Optimization: applies rule-based optimizations such as predicate pushdown, projection '
                        'pruning, boolean expression simplification, and constant folding',
                        'Physical Planning: generates multiple physical execution strategies (e.g., Broadcast Hash '
                        'Join vs Sort-Merge Join) and selects the lowest cost plan via Cost-Based Optimizer (CBO)',
                        'Code Generation (Tungsten): Whole-Stage Code Generation compiles the final physical plan into '
                        'clean, optimized Java bytecode, eliminating virtual function calls and leveraging off-heap '
                        'memory'],
  'model_answer': "Apache Spark's Catalyst Optimizer is an extensible tree-transformation framework that compiles "
                  'relational DataFrame/Dataset transformations into high-performance JVM bytecode across four stages: '
                  '1) Analysis: Catalyst takes an Unresolved Logical Plan (where column names and relations are '
                  'unverified strings) and resolves them against the metadata Catalog, verifying schemas and data '
                  'types to output a Resolved Logical Plan; 2) Logical Optimization: It applies algebraic rule-based '
                  'optimizations, executing predicate pushdown (filtering at storage level), projection pruning '
                  '(dropping unreferenced columns), and constant folding; 3) Physical Planning: Catalyst produces '
                  'multiple valid physical plans matching the logical intent and selects the optimal physical plan '
                  'using a Cost-Based Optimizer (CBO) based on table statistics (e.g., picking BroadcastHashJoin over '
                  'SortMergeJoin when one table is smaller than spark.sql.autoBroadcastJoinThreshold); and 4) Code '
                  'Generation (Tungsten): Project Tungsten applies Whole-Stage Java Code Generation, compiling the '
                  'physical plan pipeline into tight JVM bytecode that avoids virtual function dispatch and stores '
                  'data in off-heap binary format.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': "Spark's Catalyst Optimizer transforms high-level DataFrame code into native "
                                     'execution code across four key stages. First is Analysis: Catalyst takes your '
                                     'unresolved logical plan and checks the catalog to ensure tables and columns '
                                     'actually exist and types align, yielding a resolved logical plan. Second is '
                                     'Logical Optimization: it applies rule-based transformations like predicate '
                                     'pushdown—pushing WHERE filters down to the Parquet reader—and projection pruning '
                                     'to discard unneeded columns. Third is Physical Planning: it creates several '
                                     'candidate physical execution strategies and uses a Cost-Based Optimizer (CBO) to '
                                     'pick the cheapest one, deciding for example whether to do a Broadcast Hash Join '
                                     'or a Sort-Merge Join based on table size statistics. Fourth is Tungsten Code '
                                     'Generation: Project Tungsten takes that physical plan and uses Whole-Stage Code '
                                     'Generation to compile the entire pipeline into optimized Java bytecode, keeping '
                                     'data in off-heap memory buffers and removing virtual method call overhead.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'Catalyst starts by resolving table and column names against the catalog to '
                                     'create a resolved logical plan. Then it performs logical optimization using '
                                     'rules like predicate pushdown and column pruning. Next, physical planning '
                                     'generates different ways to execute the query, choosing between joins like '
                                     'broadcast hash join or sort-merge join using cost estimates. Finally, Tungsten '
                                     'compiles the physical plan into Java bytecode with whole-stage code generation '
                                     'to run fast in memory.',
                      'missing_concepts': ['Analysis phase: validates unresolved logical plan against the Spark '
                                           'Catalog to resolve column names and data types, producing a Resolved '
                                           'Logical Plan']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': "Spark's Catalyst optimizer turns DataFrame code into physical execution. It does "
                                     'logical optimization like pushing filters down, and physical planning to choose '
                                     'which join to use. Then Tungsten generates Java bytecode to execute on the '
                                     'cluster nodes.',
                      'missing_concepts': ['Analysis phase: validates unresolved logical plan against the Spark '
                                           'Catalog to resolve column names and data types, producing a Resolved '
                                           'Logical Plan',
                                           'Physical Planning: generates multiple physical execution strategies (e.g., '
                                           'Broadcast Hash Join vs Sort-Merge Join) and selects the lowest cost plan '
                                           'via Cost-Based Optimizer (CBO)']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'Catalyst is an Apache web server plugin that converts SQL queries into HTML web '
                                     'pages for dashboard viewing.',
                      'missing_concepts': ['Analysis phase: validates unresolved logical plan against the Spark '
                                           'Catalog to resolve column names and data types, producing a Resolved '
                                           'Logical Plan',
                                           'Logical Optimization: applies rule-based optimizations such as predicate '
                                           'pushdown, projection pruning, boolean expression simplification, and '
                                           'constant folding',
                                           'Physical Planning: generates multiple physical execution strategies (e.g., '
                                           'Broadcast Hash Join vs Sort-Merge Join) and selects the lowest cost plan '
                                           'via Cost-Based Optimizer (CBO)',
                                           'Code Generation (Tungsten): Whole-Stage Code Generation compiles the final '
                                           'physical plan into clean, optimized Java bytecode, eliminating virtual '
                                           'function calls and leveraging off-heap memory']}]},
 {'topic_tag': 'Parquet File Internals & Delta Lake ACID',
  'question': 'How do Parquet columnar row-group metadata enable predicate pushdown, and how does Delta Lake enforce '
              'ACID transactions on top of object storage?',
  'keywords': ['Apache Parquet',
               'Delta Lake',
               'ACID Transactions',
               'Predicate Pushdown',
               'Row Groups',
               'Optimistic Concurrency Control',
               'Transaction Log (_delta_log)'],
  'expected_concepts': ['Parquet files partition data into self-contained Row Groups (typically 128MB-512MB), storing '
                        'per-column chunks with footer metadata recording min/max statistics and null counts',
                        'Predicate pushdown reads footer metadata first: if a WHERE filter (e.g., age > 65) falls '
                        "outside a row group's min/max range, the query engine skips reading that entire row group off "
                        'disk',
                        'Delta Lake adds an immutable, ordered JSON transaction log (_delta_log) on top of raw Parquet '
                        'files, acting as the single source of truth for table state',
                        'Enforces ACID using Optimistic Concurrency Control (OCC): transactions record file '
                        'additions/deletions atomically, detecting write conflicts and enabling Time Travel queries'],
  'model_answer': 'Apache Parquet structures columnar data into horizontal chunks called Row Groups (typically '
                  '128MB-512MB), within which individual columns are stored contiguously in typed pages. Critically, '
                  'Parquet embeds lightweight metadata in the file footer recording column chunk statistics: minimum '
                  'value, maximum value, and null counts. During query execution, query engines (Spark, Trino, DuckDB) '
                  'execute Predicate Pushdown: they parse the file footer before touching actual data pages; if a '
                  "query filter (e.g., 'WHERE timestamp >= 2024-01-01') is disjoint from a row group's min/max range, "
                  'the engine skips reading and decompressing that entire row group. Delta Lake builds upon this by '
                  'bringing ACID reliability to object storage via an append-only JSON transaction log (_delta_log/). '
                  'Every write operation writes new immutable Parquet files and commits an atomic log entry recording '
                  'added and tombstoned files. Delta Lake implements Optimistic Concurrency Control (OCC) to handle '
                  'concurrent writes, resolving commit conflicts and enabling instantaneous snapshot isolation and '
                  "'time travel' historical querying.",
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'Parquet organizes data into horizontal row groups, and inside each row group, '
                                     'columns are stored separately. Crucially, the Parquet file footer stores '
                                     'metadata containing min and max values for every column in each row group. When '
                                     'you execute a query with a filter—like WHERE user_id > 5000—the query engine '
                                     'reads the footer first: if a row group has a max user_id of 4000, it skips '
                                     'reading that entire row group from disk, cutting IO drastically. Delta Lake '
                                     'solves the lack of ACID transactions on object storage by adding an ordered '
                                     'transaction log called _delta_log. When you write or update data, Delta Lake '
                                     'writes new immutable Parquet files and commits an atomic JSON log entry listing '
                                     'which files were added and which were tombstoned. It uses Optimistic Concurrency '
                                     'Control to detect write conflicts between simultaneous jobs and provides '
                                     'snapshot isolation and time travel by replaying the log up to any specific '
                                     'historical commit.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'Parquet splits data into row groups and writes min/max statistics in the file '
                                     'footer. Predicate pushdown checks the footer first, skipping row groups that '
                                     "don't match the query filter without loading them off disk. Delta Lake brings "
                                     'ACID transactions to cloud object storage using a transaction log in _delta_log. '
                                     'It writes immutable Parquet files and records additions and deletions in the log '
                                     'using optimistic concurrency control, which also lets you query historical '
                                     'versions using time travel.',
                      'missing_concepts': ['Parquet files partition data into self-contained Row Groups (typically '
                                           '128MB-512MB), storing per-column chunks with footer metadata recording '
                                           'min/max statistics and null counts']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Parquet is a columnar format that has min and max metadata in its footer so the '
                                     "engine can skip rows that don't match the query. Delta Lake is a table format "
                                     'that adds a transaction log to Parquet files so you get ACID transactions and '
                                     'time travel in Databricks.',
                      'missing_concepts': ['Parquet files partition data into self-contained Row Groups (typically '
                                           '128MB-512MB), storing per-column chunks with footer metadata recording '
                                           'min/max statistics and null counts',
                                           'Enforces ACID using Optimistic Concurrency Control (OCC): transactions '
                                           'record file additions/deletions atomically, detecting write conflicts and '
                                           'enabling Time Travel queries']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'Parquet is an antivirus file scanning protocol, and Delta Lake is an airline '
                                     'booking database format.',
                      'missing_concepts': ['Parquet files partition data into self-contained Row Groups (typically '
                                           '128MB-512MB), storing per-column chunks with footer metadata recording '
                                           'min/max statistics and null counts',
                                           'Predicate pushdown reads footer metadata first: if a WHERE filter (e.g., '
                                           "age > 65) falls outside a row group's min/max range, the query engine "
                                           'skips reading that entire row group off disk',
                                           'Delta Lake adds an immutable, ordered JSON transaction log (_delta_log) on '
                                           'top of raw Parquet files, acting as the single source of truth for table '
                                           'state',
                                           'Enforces ACID using Optimistic Concurrency Control (OCC): transactions '
                                           'record file additions/deletions atomically, detecting write conflicts and '
                                           'enabling Time Travel queries']}]},
 {'topic_tag': 'Advanced SQL Join Algorithms',
  'question': 'Compare Hash Join, Sort-Merge Join, and Nested Loop Join execution mechanisms, memory requirements, and '
              'performance trade-offs.',
  'keywords': ['SQL Join Algorithms',
               'Hash Join',
               'Sort-Merge Join',
               'Nested Loop Join',
               'Query Optimizer',
               'In-Memory Hash Table',
               'External Spill'],
  'expected_concepts': ['Nested Loop Join: compares every row in outer table with inner table; optimal O(N * M) or O(N '
                        'log M) with index for tiny outer tables, but disastrous for large unindexed tables',
                        'Hash Join: two phases—Build phase creates in-memory hash table on the smaller build input; '
                        'Probe phase streams the larger probe input and probes hash table; optimal O(N + M) for large '
                        'unindexed equi-joins',
                        'Sort-Merge Join: sorts both tables on join keys (if unsorted) and scans concurrently in a '
                        'single linear merge pass; optimal O(N log N + M log M) for very large datasets or pre-sorted '
                        'clustered tables',
                        'Spilling behavior: Hash joins spill partition buckets to disk when memory quota (work_mem) is '
                        'exceeded; Sort-Merge joins handle memory exhaustion via external disk merge sort'],
  'model_answer': 'Database query optimizers execute relational joins using three primary physical algorithms '
                  'depending on table cardinality, indexes, and memory quotas: 1) Nested Loop Join: iterates over the '
                  'outer relation and, for each row, searches the inner relation. Highly efficient (O(N log M)) when '
                  'the outer table is tiny and the inner table has an indexed join key, but scales quadratically (O(N '
                  '* M)) on large unindexed tables; 2) Hash Join: designed for equi-joins on large, unindexed tables. '
                  'In the Build Phase, the engine loads the smaller table into an in-memory hash table; in the Probe '
                  'Phase, it streams the larger table, hashing join keys to probe for matches in O(N + M) time. If the '
                  'hash table exceeds working memory (e.g., work_mem), it degrades to a grace hash join, spilling hash '
                  'partitions to disk; and 3) Sort-Merge Join: sorts both relations on the join key (O(N log N + M log '
                  'M)) and walks both streams concurrently in a single coordinated linear scan (O(N + M)). It is '
                  'optimal when inputs are already presorted (e.g., clustered index) or when datasets exceed available '
                  'RAM, as external merge sort handles disk spills gracefully.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'Database optimizers pick between three physical join strategies. Nested Loop '
                                     "Join loops through the outer table row by row and searches the inner table. It's "
                                     'fantastic (O(N log M)) when the outer table is small and the inner table has a '
                                     'B-tree index on the join key, but catastrophic (O(N*M)) on large unindexed '
                                     'tables. Hash Join is ideal for large unindexed equi-joins: it takes the smaller '
                                     'table and builds an in-memory hash table, then streams the larger table and '
                                     'probes the hash table in linear O(N + M) time. Its weakness is memory: if the '
                                     'build table exceeds work_mem, it has to spill partition buckets to disk. '
                                     'Sort-Merge Join sorts both tables on the join keys and then steps through them '
                                     'together in a single linear pass. If the tables are already pre-sorted from an '
                                     'index, it runs in linear time without memory overhead, and if it exceeds RAM, it '
                                     'handles disk spills much more smoothly than hash joins.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'Nested loop join loops through table A and looks up matches in table B, best '
                                     'when table A is tiny and table B is indexed. Hash join builds a hash table in '
                                     'memory from the smaller table and probes it with the larger table in O(N+M) '
                                     'time, but it needs enough RAM to avoid spilling to disk. Sort-merge join sorts '
                                     'both tables and merges them linearly, which is best when the data is already '
                                     'sorted by clustered indexes or for massive datasets that exceed memory.',
                      'missing_concepts': ['Spilling behavior: Hash joins spill partition buckets to disk when memory '
                                           'quota (work_mem) is exceeded; Sort-Merge joins handle memory exhaustion '
                                           'via external disk merge sort']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Nested loop is good for small tables. Hash join makes a hash table in memory and '
                                     'is fast for large tables. Sort-merge join sorts both tables first and merges '
                                     'them together. The database optimizer picks the best one using cost estimates.',
                      'missing_concepts': ['Hash Join: two phases—Build phase creates in-memory hash table on the '
                                           'smaller build input; Probe phase streams the larger probe input and probes '
                                           'hash table; optimal O(N + M) for large unindexed equi-joins',
                                           'Spilling behavior: Hash joins spill partition buckets to disk when memory '
                                           'quota (work_mem) is exceeded; Sort-Merge joins handle memory exhaustion '
                                           'via external disk merge sort']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'Hash join is an MD5 cryptographic password validation check, and sort-merge join '
                                     'is an Excel spreadsheet macro.',
                      'missing_concepts': ['Nested Loop Join: compares every row in outer table with inner table; '
                                           'optimal O(N * M) or O(N log M) with index for tiny outer tables, but '
                                           'disastrous for large unindexed tables',
                                           'Hash Join: two phases—Build phase creates in-memory hash table on the '
                                           'smaller build input; Probe phase streams the larger probe input and probes '
                                           'hash table; optimal O(N + M) for large unindexed equi-joins',
                                           'Sort-Merge Join: sorts both tables on join keys (if unsorted) and scans '
                                           'concurrently in a single linear merge pass; optimal O(N log N + M log M) '
                                           'for very large datasets or pre-sorted clustered tables',
                                           'Spilling behavior: Hash joins spill partition buckets to disk when memory '
                                           'quota (work_mem) is exceeded; Sort-Merge joins handle memory exhaustion '
                                           'via external disk merge sort']}]},
 {'topic_tag': 'Markov Chain Monte Carlo (MCMC) Sampling',
  'question': 'Explain how the Metropolis-Hastings algorithm constructs a Markov Chain whose stationary distribution '
              'matches an intractable posterior probability distribution.',
  'keywords': ['MCMC',
               'Metropolis-Hastings',
               'Markov Chain',
               'Stationary Distribution',
               'Proposal Distribution',
               'Acceptance Probability',
               'Intractable Posterior'],
  'expected_concepts': ['Bayesian posterior P(theta|D) = [P(D|theta) * P(theta)] / P(D) has an intractable denominator '
                        'marginal integral P(D) = int P(D|theta)P(theta)dtheta in high dimensions',
                        'MCMC generates samples from the posterior without computing the normalizing denominator P(D)',
                        'Metropolis-Hastings generates a candidate state theta* from proposal distribution q(theta* | '
                        'theta_t), calculating acceptance ratio alpha = min(1, [P(D|theta*)P(theta*) '
                        'q(theta_t|theta*)] / [P(D|theta_t)P(theta_t) q(theta*|theta_t)])',
                        'Detailed balance ensures the Markov chain converges to a unique stationary distribution '
                        'matching the target posterior after discarding initial non-equilibrium burn-in samples'],
  'model_answer': 'In Bayesian inference, the posterior distribution P(theta|D) = P(D|theta)P(theta) / P(D) is '
                  'analytically intractable in high dimensions because the evidence denominator P(D) = integral '
                  'P(D|theta)P(theta) d(theta) has no closed-form solution. The Metropolis-Hastings (MH) algorithm '
                  'solves this by constructing an ergodic Markov chain whose unique stationary distribution is the '
                  'target posterior, circumventing the intractable denominator. At state theta_t, a candidate state '
                  'theta* is drawn from a proposal distribution q(theta* | theta_t). The algorithm computes the '
                  'acceptance probability alpha = min(1, [P(D|theta*) * P(theta*) * q(theta_t|theta*)] / [P(D|theta_t) '
                  '* P(theta_t) * q(theta*|theta_t)]). Because P(D) cancels out of the ratio, only unnormalized priors '
                  'and likelihoods are evaluated. A uniform random draw u ~ U(0,1) determines transition: if u <= '
                  'alpha, theta_{t+1} = theta*; else theta_{t+1} = theta_t. By satisfying the detailed balance '
                  'condition, the chain converges to the target distribution after a burn-in warmup period.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'In Bayesian inference, calculating the posterior requires computing the evidence '
                                     'integral in the denominator, which is mathematically impossible in high '
                                     'dimensions. The Metropolis-Hastings algorithm bypasses this denominator '
                                     'completely by constructing a Markov chain whose stationary distribution matches '
                                     'the posterior. At each step theta_t, you propose a new point theta* from a '
                                     'proposal distribution q. You calculate the acceptance ratio alpha: it compares '
                                     'the unnormalized posterior of the proposal against the current state, adjusted '
                                     'for proposal symmetry. Because the evidence integral P(D) is in both the '
                                     'numerator and denominator, it cancels out completely! If alpha >= 1, you accept '
                                     'the new state immediately; if alpha < 1, you accept it with probability alpha. '
                                     'This satisfies detailed balance, guaranteeing that after discarding an initial '
                                     'burn-in period, the collected samples follow the true posterior distribution.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': "Bayesian posteriors have an intractable denominator integral that can't be "
                                     'solved directly. Metropolis-Hastings samples from the posterior by proposing a '
                                     'candidate state and calculating an acceptance probability alpha. Because you '
                                     'take the ratio of the proposed state to the current state, the normalizing '
                                     'denominator cancels out. You accept or reject the candidate with probability '
                                     'alpha. After a burn-in period, the chain converges to the true posterior '
                                     'distribution.',
                      'missing_concepts': ['Detailed balance ensures the Markov chain converges to a unique stationary '
                                           'distribution matching the target posterior after discarding initial '
                                           'non-equilibrium burn-in samples']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': "MCMC is used to sample from Bayesian distributions when you can't calculate them "
                                     'with math. Metropolis-Hastings proposes a step and accepts it based on an '
                                     'acceptance probability. The denominator cancels out in the ratio. You throw away '
                                     'the burn-in samples at the start.',
                      'missing_concepts': ['Bayesian posterior P(theta|D) = [P(D|theta) * P(theta)] / P(D) has an '
                                           'intractable denominator marginal integral P(D) = int '
                                           'P(D|theta)P(theta)dtheta in high dimensions',
                                           'Detailed balance ensures the Markov chain converges to a unique stationary '
                                           'distribution matching the target posterior after discarding initial '
                                           'non-equilibrium burn-in samples']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'Markov Chain Monte Carlo is a gambling probability simulation used in Las Vegas '
                                     'casino games to predict roulette wheel outcomes.',
                      'missing_concepts': ['Bayesian posterior P(theta|D) = [P(D|theta) * P(theta)] / P(D) has an '
                                           'intractable denominator marginal integral P(D) = int '
                                           'P(D|theta)P(theta)dtheta in high dimensions',
                                           'MCMC generates samples from the posterior without computing the '
                                           'normalizing denominator P(D)',
                                           'Metropolis-Hastings generates a candidate state theta* from proposal '
                                           'distribution q(theta* | theta_t), calculating acceptance ratio alpha = '
                                           'min(1, [P(D|theta*)P(theta*) q(theta_t|theta*)] / [P(D|theta_t)P(theta_t) '
                                           'q(theta*|theta_t)])',
                                           'Detailed balance ensures the Markov chain converges to a unique stationary '
                                           'distribution matching the target posterior after discarding initial '
                                           'non-equilibrium burn-in samples']}]},
 {'topic_tag': 'Non-parametric Bootstrapping Math',
  'question': 'Detail the mathematical mechanics of non-parametric empirical bootstrapping and compare Percentile '
              'versus BCa confidence intervals.',
  'keywords': ['Non-parametric Bootstrapping',
               'Empirical Distribution Function (EDF)',
               'Sampling with Replacement',
               'Percentile Interval',
               'BCa Confidence Intervals',
               'Bias-Correction',
               'Acceleration Parameter'],
  'expected_concepts': ["Non-parametric bootstrap treats the sample's Empirical Distribution Function (EDF) F_n as a "
                        'plug-in surrogate for unknown population distribution F',
                        'Draws B independent resamples of size n with replacement from observed data, computing the '
                        'statistic of interest theta*_b for each resample',
                        'Percentile bootstrap takes the alpha/2 and 1 - alpha/2 quantiles of the bootstrap '
                        'distribution; simple but biased when the estimator is skewed or biased',
                        'BCa (Bias-Corrected and Accelerated) intervals adjust quantile endpoints for both median bias '
                        'z_0 and non-constant variance (acceleration parameter a via jackknife), achieving '
                        'second-order accuracy O(1/n)'],
  'model_answer': 'Non-parametric empirical bootstrapping (Efron, 1979) estimates sampling distributions without '
                  'assuming a parametric family. The core mathematical principle is the plug-in rule: the unknown '
                  "population distribution F is approximated by the sample's Empirical Distribution Function F_n "
                  '(placing mass 1/n on each observation x_i). By drawing B independent resamples of size n with '
                  'replacement from F_n, we compute the bootstrap replications theta*_1, ..., theta*_B. To construct '
                  'confidence intervals: 1) The standard Percentile method uses empirical quantiles [theta*_{alpha/2}, '
                  'theta*_{1 - alpha/2}]. While transformation-invariant, it is only first-order accurate '
                  '(O(1/sqrt(n))) and yields inaccurate coverage if the bootstrap distribution is biased or skewed; 2) '
                  'The BCa (Bias-Corrected and Accelerated) method adjusts the percentile bounds using two parameters: '
                  'bias correction z_0 (measuring median bias of theta* relative to sample estimate theta_hat) and '
                  'acceleration parameter a (measuring how the standard error of theta_hat changes with the true '
                  'parameter, estimated via jackknife). BCa intervals achieve second-order accuracy (O(1/n)) and '
                  'correct for skewness.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'Non-parametric bootstrapping uses the plug-in principle: it treats the empirical '
                                     'distribution of your sample F_n as a proxy for the true population distribution. '
                                     'You draw B bootstrap samples of size n with replacement, computing your '
                                     'statistic theta* on each sample to form a bootstrap distribution. To get a '
                                     'confidence interval, the simplest approach is the Percentile method, which just '
                                     'takes the 2.5th and 97.5th percentiles. However, the percentile method is only '
                                     'first-order accurate and fails when the estimator is skewed or biased. The '
                                     'BCa—Bias-Corrected and Accelerated—method fixes this. It calculates a bias '
                                     'parameter z_0 from the proportion of bootstrap estimates below the original '
                                     "point estimate, and an acceleration parameter 'a' using a jackknife to account "
                                     'for variance changing with the parameter. BCa adjusts the percentile cutoffs, '
                                     'achieving second-order accuracy O(1/n) and delivering correct coverage even on '
                                     'skewed statistics like ratios or medians.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'Bootstrapping resamples data of size n with replacement B times to build a '
                                     'sampling distribution without making normal distribution assumptions. The '
                                     'percentile interval just takes the alpha/2 and 1-alpha/2 percentiles of the '
                                     "bootstrap distribution, but it's flawed if your estimator is skewed. The BCa "
                                     'method adjusts the interval endpoints for bias using z_0 and skewness using the '
                                     "acceleration parameter 'a' from jackknife, providing much more accurate "
                                     'confidence intervals.',
                      'missing_concepts': ["Non-parametric bootstrap treats the sample's Empirical Distribution "
                                           'Function (EDF) F_n as a plug-in surrogate for unknown population '
                                           'distribution F']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Bootstrapping is sampling with replacement from your dataset 1,000 times to get '
                                     'confidence intervals for metrics like the median. The percentile method takes '
                                     'the 2.5% and 97.5% marks. BCa is a more advanced version that corrects for bias '
                                     'and skewness in the data.',
                      'missing_concepts': ["Non-parametric bootstrap treats the sample's Empirical Distribution "
                                           'Function (EDF) F_n as a plug-in surrogate for unknown population '
                                           'distribution F',
                                           'BCa (Bias-Corrected and Accelerated) intervals adjust quantile endpoints '
                                           'for both median bias z_0 and non-constant variance (acceleration parameter '
                                           'a via jackknife), achieving second-order accuracy O(1/n)']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'Bootstrapping is the process of booting up a Linux operating system kernel when '
                                     'an AWS EC2 instance starts up.',
                      'missing_concepts': ["Non-parametric bootstrap treats the sample's Empirical Distribution "
                                           'Function (EDF) F_n as a plug-in surrogate for unknown population '
                                           'distribution F',
                                           'Draws B independent resamples of size n with replacement from observed '
                                           'data, computing the statistic of interest theta*_b for each resample',
                                           'Percentile bootstrap takes the alpha/2 and 1 - alpha/2 quantiles of the '
                                           'bootstrap distribution; simple but biased when the estimator is skewed or '
                                           'biased',
                                           'BCa (Bias-Corrected and Accelerated) intervals adjust quantile endpoints '
                                           'for both median bias z_0 and non-constant variance (acceleration parameter '
                                           'a via jackknife), achieving second-order accuracy O(1/n)']}]},
 {'topic_tag': 'Bayesian Hierarchical Modeling in PyMC',
  'question': 'How do Bayesian hierarchical models use partial pooling to share statistical strength across groups '
              'while preventing over-shrinkage?',
  'keywords': ['Bayesian Hierarchical Models',
               'Partial Pooling',
               'Shrinkage',
               'Hyperpriors',
               'PyMC',
               'No-U-Turn Sampler (NUTS)',
               'Group-Level Variance'],
  'expected_concepts': ['Complete pooling treats all groups as identical (ignores group differences, high bias); No '
                        'pooling estimates each group completely independently (low bias, massive variance on small '
                        'sample groups)',
                        'Hierarchical models implement Partial Pooling: group parameters theta_j are assumed to be '
                        'drawn from a common population hyperprior distribution N(mu, tau^2)',
                        'Shrinkage mechanism: group estimates are pulled toward the global mean mu, with shrinkage '
                        'strength inversely proportional to group sample size n_j and within-group variance',
                        'Small/noisy groups borrow statistical strength from large groups without forcing large groups '
                        'with abundant data to lose their distinct estimates'],
  'model_answer': 'In multi-level data (e.g., student performance across 50 schools), analysts face a dilemma: '
                  'Complete Pooling forces all groups to share a single global parameter, obliterating real '
                  'between-group heterogeneity; No Pooling fits 50 separate parameters independently, producing noisy, '
                  'unstable estimates with massive standard errors for schools with small sample sizes. Bayesian '
                  'Hierarchical Models resolve this via Partial Pooling. Instead of treating group parameters theta_j '
                  'as unrelated fixed constants, they are modeled as draws from a shared population distribution: '
                  'theta_j ~ Normal(mu, tau^2), where global mean mu and group variance tau receive hyperpriors. In '
                  'PyMC, Hamiltonian Monte Carlo (NUTS) estimates the joint posterior. Groups with small sample sizes '
                  'n_j shrink aggressively toward the grand mean mu, borrowing statistical strength from the entire '
                  'dataset, while groups with abundant data resist shrinkage, preserving their unique signals.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'Bayesian hierarchical modeling provides the optimal middle ground between '
                                     'complete pooling and no pooling. Complete pooling lumps all groups together, '
                                     'ignoring real differences. No pooling estimates each group completely on its '
                                     'own, which causes wild overfitting and huge error bars for groups with only 2 or '
                                     "3 observations. A hierarchical model uses partial pooling: each group's "
                                     'parameter theta_j is drawn from a common hyperprior distribution, like '
                                     'Normal(mu, tau^2). The model learns both the global mean mu and the '
                                     "between-group variance tau simultaneously. This creates shrinkage: a group's "
                                     'estimate is shrunk toward the global mean in proportion to how noisy or small '
                                     'that group is. If a group has 5,000 data points, its estimate barely shrinks at '
                                     'all; if a group only has 3 data points, it heavily shrinks toward the population '
                                     'mean, borrowing statistical strength from the rest of the dataset.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'Complete pooling ignores group differences, while no pooling creates noisy '
                                     'estimates for small groups. A hierarchical model in PyMC sets up hyperpriors so '
                                     'that group parameters are drawn from a shared distribution. This causes partial '
                                     'pooling, where group estimates shrink towards the overall mean. Groups with very '
                                     'little data shrink a lot, borrowing strength from the population, while groups '
                                     'with lots of data retain their own unique values.',
                      'missing_concepts': ['Complete pooling treats all groups as identical (ignores group '
                                           'differences, high bias); No pooling estimates each group completely '
                                           'independently (low bias, massive variance on small sample groups)']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Hierarchical models in PyMC use partial pooling to connect groups together. If '
                                     'you have a school with only a few students, partial pooling pulls its score '
                                     "towards the average school score so you don't overfit. You use hyperpriors to "
                                     'control how much shrinkage happens.',
                      'missing_concepts': ['Complete pooling treats all groups as identical (ignores group '
                                           'differences, high bias); No pooling estimates each group completely '
                                           'independently (low bias, massive variance on small sample groups)',
                                           'Shrinkage mechanism: group estimates are pulled toward the global mean mu, '
                                           'with shrinkage strength inversely proportional to group sample size n_j '
                                           'and within-group variance']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'Hierarchical modeling is when you organize Python scripts into parent and child '
                                     'folders on your hard drive.',
                      'missing_concepts': ['Complete pooling treats all groups as identical (ignores group '
                                           'differences, high bias); No pooling estimates each group completely '
                                           'independently (low bias, massive variance on small sample groups)',
                                           'Hierarchical models implement Partial Pooling: group parameters theta_j '
                                           'are assumed to be drawn from a common population hyperprior distribution '
                                           'N(mu, tau^2)',
                                           'Shrinkage mechanism: group estimates are pulled toward the global mean mu, '
                                           'with shrinkage strength inversely proportional to group sample size n_j '
                                           'and within-group variance',
                                           'Small/noisy groups borrow statistical strength from large groups without '
                                           'forcing large groups with abundant data to lose their distinct '
                                           'estimates']}]},
 {'topic_tag': 'Recommender Systems Matrix Factorization (ALS)',
  'question': 'Formulate Alternating Least Squares (ALS) matrix factorization for collaborative filtering with '
              'implicit feedback datasets.',
  'keywords': ['Recommender Systems',
               'Matrix Factorization',
               'Alternating Least Squares (ALS)',
               'Implicit Feedback',
               'Latent Factors',
               'Confidence Weighting',
               'Collaborative Filtering'],
  'expected_concepts': ['Implicit feedback (clicks, watch time, purchases) lacks explicit negative ratings; '
                        'observations indicate positive preference, while unobserved interactions represent unknown '
                        'mixtures of dislike and lack of awareness',
                        'Decomposes user-item interaction matrix R (size U x I) into low-rank latent user matrix X (U '
                        'x k) and item matrix Y (I x k) such that R approx X * Y^T',
                        'Hu, Koren, Volinsky formulation introduces binary preference p_ui and confidence weights c_ui '
                        '= 1 + alpha * r_ui',
                        'Loss function is non-convex jointly, but quadratic and convex when alternating: fixes Y to '
                        'solve X in closed-form, then fixes X to solve Y, parallelizable across CPU/Spark clusters'],
  'model_answer': 'In production recommender systems, explicit ratings (1-5 stars) are rare; platforms rely on '
                  'implicit feedback (clicks, page views, stream counts). Implicit data possesses no true negative '
                  'signals: unobserved entries r_ui = 0 reflect a mixture of dislike and lack of awareness. Hu, Koren, '
                  'and Volinsky (2008) formulated Implicit Alternating Least Squares (iALS) by introducing binary '
                  'preference p_ui (1 if r_ui > 0, else 0) paired with a confidence weighting c_ui = 1 + alpha * r_ui. '
                  'The objective minimizes: sum_{u,i} c_ui * (p_ui - x_u^T y_i)^2 + lambda * (||x_u||^2 + ||y_i||^2). '
                  'Because the loss function is non-convex jointly in user factors x_u and item factors y_i, '
                  'Alternating Least Squares (ALS) alternates: fixing all item vectors Y makes the loss convex '
                  'quadratic in x_u, enabling closed-form ridge regression solutions x_u = (Y^T C^u Y + lambda I)^{-1} '
                  'Y^T C^u p_u. Then, fixing X solves for each y_i in parallel, scaling gracefully on Apache Spark '
                  'clusters.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': "Implicit feedback like clicks, video views, or purchases doesn't have 1-to-5 "
                                     "star ratings; a zero doesn't mean the user hated the item, it usually just means "
                                     'they never saw it. The Hu-Koren-Volinsky iALS algorithm maps this by converting '
                                     'raw counts into binary preferences p_ui (1 if consumed, 0 otherwise) and '
                                     'assigning confidence weights c_ui = 1 + alpha * r_ui, so frequent interactions '
                                     'carry massive confidence while zeros carry baseline confidence 1. It decomposes '
                                     'the user-item interaction matrix into low-rank latent matrices X and Y so that X '
                                     'times Y transpose approximates preferences. While the loss is non-convex when '
                                     'optimizing both matrices together, if you hold the item matrix Y fixed, the '
                                     'problem becomes convex quadratic in user matrix X, allowing you to solve for '
                                     'every user in closed-form ridge regression. Then you hold X fixed and solve for '
                                     'all items Y. You alternate back and forth until convergence, which parallelizes '
                                     'across Spark clusters.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': "Implicit feedback like clicks doesn't have negative ratings, only interaction "
                                     'counts. ALS matrix factorization decomposes the user-item matrix into user '
                                     'latent factors X and item latent factors Y. It uses binary preference p_ui and '
                                     'confidence weights c_ui that scale with interaction frequency. Because '
                                     'optimizing both matrices together is non-convex, ALS holds item vectors fixed to '
                                     'solve for user vectors using least squares, and then holds user vectors fixed to '
                                     'solve for items, alternating until convergence.',
                      'missing_concepts': ['Implicit feedback (clicks, watch time, purchases) lacks explicit negative '
                                           'ratings; observations indicate positive preference, while unobserved '
                                           'interactions represent unknown mixtures of dislike and lack of awareness']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'ALS stands for alternating least squares and is used in Spark recommendation '
                                     'systems. It factors a big matrix into user and item vectors. It fixes users to '
                                     'update items, and then fixes items to update users. Implicit feedback is used '
                                     'when you only have clicks and views instead of ratings.',
                      'missing_concepts': ['Hu, Koren, Volinsky formulation introduces binary preference p_ui and '
                                           'confidence weights c_ui = 1 + alpha * r_ui',
                                           'Loss function is non-convex jointly, but quadratic and convex when '
                                           'alternating: fixes Y to solve X in closed-form, then fixes X to solve Y, '
                                           'parallelizable across CPU/Spark clusters']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'Alternating Least Squares is an optimization algorithm used to balance wheel '
                                     'alignment on race cars.',
                      'missing_concepts': ['Implicit feedback (clicks, watch time, purchases) lacks explicit negative '
                                           'ratings; observations indicate positive preference, while unobserved '
                                           'interactions represent unknown mixtures of dislike and lack of awareness',
                                           'Decomposes user-item interaction matrix R (size U x I) into low-rank '
                                           'latent user matrix X (U x k) and item matrix Y (I x k) such that R approx '
                                           'X * Y^T',
                                           'Hu, Koren, Volinsky formulation introduces binary preference p_ui and '
                                           'confidence weights c_ui = 1 + alpha * r_ui',
                                           'Loss function is non-convex jointly, but quadratic and convex when '
                                           'alternating: fixes Y to solve X in closed-form, then fixes X to solve Y, '
                                           'parallelizable across CPU/Spark clusters']}]},
 {'topic_tag': 'High-Dimensional Outlier Detection (Isolation Forest)',
  'question': 'Derive the anomaly scoring function of Isolation Forests based on average path length in randomized '
              'isolation trees.',
  'keywords': ['Isolation Forest',
               'Anomaly Detection',
               'iTree',
               'Path Length h(x)',
               'Average Path Length c(n)',
               'Binary Search Tree',
               'Ensemble Methods'],
  'expected_concepts': ["Anomalies are 'few and different': they possess rare attribute values and isolate near the "
                        'root of randomized recursive partitioning trees with very short path lengths h(x)',
                        'An iTree recursively splits data by randomly selecting a feature and a random split value '
                        'between feature min and max until all points are isolated',
                        'Average path length of unsuccessful searches in a Binary Search Tree (BST) serves as the '
                        'normalizer: c(n) = 2 * (ln(n - 1) + 0.5772156649) - [2 * (n - 1) / n]',
                        'Anomaly score s(x, n) = 2^(- E[h(x)] / c(n)): score close to 1 indicates a definitive '
                        'anomaly; score < 0.5 indicates a normal observation'],
  'model_answer': 'Isolation Forest (Liu, Ting, Zhou 2008) detects anomalies through isolation rather than density '
                  "estimation. It relies on two core premises: anomalies are 'few and different', meaning they occupy "
                  'sparse regions of feature space. An Isolation Tree (iTree) recursively partitions a subsample of n '
                  'points by randomly selecting a feature and choosing a uniform random split value between that '
                  "feature's min and max until points are isolated into leaf nodes. Because anomalies are isolated "
                  'rapidly, they exhibit significantly shorter path lengths h(x) (number of edges traversed from root '
                  'to leaf). The algorithm normalizes path length against c(n), the average path length of '
                  'unsuccessful searches in an equivalent Binary Search Tree: c(n) = 2 * (ln(n - 1) + gamma) - 2 * (n '
                  "- 1) / n, where gamma is Euler's constant. The anomaly score is defined as: s(x, n) = 2^(- E[h(x)] "
                  '/ c(n)). When average path length E[h(x)] -> 0, s -> 1 (definite anomaly); when E[h(x)] -> c(n), s '
                  '-> 0.5 (normal instance); and when E[h(x)] -> n - 1, s -> 0.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': "Isolation Forest is built on the intuition that anomalies are 'few and "
                                     "different', which makes them much easier to isolate than normal data points. An "
                                     'isolation tree randomly picks a feature and a random split threshold between the '
                                     "feature's minimum and maximum, repeating recursively. Anomalies get separated "
                                     'from the rest of the dataset very close to the root, resulting in a short tree '
                                     'path length h(x). The algorithm averages path lengths over an ensemble of trees, '
                                     'E[h(x)], and normalizes it using c(n), which is the theoretical average path '
                                     'length of an unsuccessful search in a binary search tree. The anomaly score '
                                     'formula is s(x, n) = 2^(- E[h(x)] / c(n)). If the average path length is very '
                                     'short, the exponent approaches zero and the score approaches 1, indicating a '
                                     'clear anomaly. If the path length is around the average expected depth c(n), the '
                                     'score is around 0.5, representing a completely normal observation.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'Isolation Forest isolates outliers by randomly picking features and random split '
                                     'points to build random trees. Anomalies are isolated quickly and have short path '
                                     'lengths h(x). The anomaly score formula is s = 2 to the power of negative '
                                     'E[h(x)] divided by c(n), where c(n) is the average path length of a binary '
                                     "search tree. A score close to 1 means it's an anomaly, while around 0.5 means "
                                     'normal data.',
                      'missing_concepts': ['An iTree recursively splits data by randomly selecting a feature and a '
                                           'random split value between feature min and max until all points are '
                                           'isolated']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Isolation forest isolates anomalies by building random decision trees. Normal '
                                     'points take many splits to isolate, while outliers take very few splits because '
                                     'they are far away. The path length is converted into an anomaly score between 0 '
                                     'and 1. If the score is near 1 it is an outlier.',
                      'missing_concepts': ['Average path length of unsuccessful searches in a Binary Search Tree (BST) '
                                           'serves as the normalizer: c(n) = 2 * (ln(n - 1) + 0.5772156649) - [2 * (n '
                                           '- 1) / n]',
                                           'Anomaly score s(x, n) = 2^(- E[h(x)] / c(n)): score close to 1 indicates a '
                                           'definitive anomaly; score < 0.5 indicates a normal observation']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'An Isolation Forest is a cybersecurity firewall that isolates infected servers '
                                     'from a corporate intranet.',
                      'missing_concepts': ["Anomalies are 'few and different': they possess rare attribute values and "
                                           'isolate near the root of randomized recursive partitioning trees with very '
                                           'short path lengths h(x)',
                                           'An iTree recursively splits data by randomly selecting a feature and a '
                                           'random split value between feature min and max until all points are '
                                           'isolated',
                                           'Average path length of unsuccessful searches in a Binary Search Tree (BST) '
                                           'serves as the normalizer: c(n) = 2 * (ln(n - 1) + 0.5772156649) - [2 * (n '
                                           '- 1) / n]',
                                           'Anomaly score s(x, n) = 2^(- E[h(x)] / c(n)): score close to 1 indicates a '
                                           'definitive anomaly; score < 0.5 indicates a normal observation']}]},
 {'topic_tag': 'Feature Store Point-in-Time Join Logic',
  'question': "Explain how Point-in-Time 'As-Of' joins in feature stores prevent lookahead bias and temporal data "
              'leakage in predictive modeling.',
  'keywords': ['Feature Store',
               'Point-in-Time Join',
               'As-Of Join',
               'Temporal Data Leakage',
               'Lookahead Bias',
               'Event Timestamp',
               'Feature Timestamp'],
  'expected_concepts': ['Temporal data leakage / lookahead bias occurs when training records incorporate feature '
                        'values computed from events that occurred after the target prediction timestamp',
                        "An As-Of join matches each observation's event timestamp (t_event) to the latest feature "
                        'value whose computation timestamp satisfies t_feature <= t_event',
                        'Standard relational joins match on primary key alone, grabbing current/latest features and '
                        'causing massive optimistic bias during offline validation',
                        'Guarantees point-in-time correctness across time-varying entity features (e.g., user account '
                        'balance or 30-day transaction count at the time of loan application)'],
  'model_answer': 'In production machine learning on historical events (e.g., credit underwriting or fraud detection), '
                  'temporal data leakage is the most pernicious source of model failure. When creating a training '
                  'dataset, matching entities (e.g., user_id) using standard relational joins pulls the most recently '
                  'updated feature values—leaking future post-event information into past training instances. For '
                  'example, if a user defaulted on June 1st, joining their credit score computed on August 1st gives '
                  'the model access to future financial ruin, creating artificially stellar offline validation metrics '
                  "that collapse in production. Feature stores solve this through Point-in-Time 'As-Of' joins. For "
                  'every observation in an entity dataframe with an observation timestamp t_event, the feature store '
                  'joins the most recent feature record whose feature timestamp t_feature satisfies t_feature <= '
                  't_event. This guarantees point-in-time correctness, reconstructing historical state precisely as it '
                  'existed at the moment of prediction.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'Temporal data leakage occurs when your training features contain information '
                                     'from the future that would not have been available at the moment of prediction. '
                                     "For example, if you're predicting whether a loan application on March 1st will "
                                     "default, using a user's current account balance from December leaks 9 months of "
                                     'future data, giving you 99% validation accuracy that completely fails in '
                                     'production. A standard SQL join matches only on user_id, grabbing the latest '
                                     "row. A point-in-time 'as-of' join matches both the entity ID and the timestamp, "
                                     'joining the latest feature record where the feature timestamp is less than or '
                                     'equal to the event timestamp: t_feature <= t_event. Feature stores like Feast or '
                                     'Hopsworks automate this as-of join logic across historical time-series feature '
                                     'tables, guaranteeing that training datasets reconstruct exact historical reality '
                                     'without lookahead bias.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'Lookahead bias happens when a training dataset uses feature values calculated '
                                     'after the event took place, which inflates model accuracy. A point-in-time as-of '
                                     'join prevents this by looking up the most recent feature value that existed '
                                     'right before the event timestamp (t_feature <= t_event). Feature stores use '
                                     'as-of joins to build training datasets that reflect exactly what data was '
                                     'available at the time of prediction.',
                      'missing_concepts': ['Standard relational joins match on primary key alone, grabbing '
                                           'current/latest features and causing massive optimistic bias during offline '
                                           'validation']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Point in time joins prevent data leakage from the future into your training '
                                     "data. If you predict fraud on January 1st, you can't use features calculated on "
                                     'January 5th. As-of joins match on the entity ID and make sure the timestamp is '
                                     'in the past before the prediction.',
                      'missing_concepts': ['Temporal data leakage / lookahead bias occurs when training records '
                                           'incorporate feature values computed from events that occurred after the '
                                           'target prediction timestamp',
                                           'Guarantees point-in-time correctness across time-varying entity features '
                                           '(e.g., user account balance or 30-day transaction count at the time of '
                                           'loan application)']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'Point-in-time joins are time zone conversion functions used when translating UTC '
                                     'timestamps to Pacific Standard Time.',
                      'missing_concepts': ['Temporal data leakage / lookahead bias occurs when training records '
                                           'incorporate feature values computed from events that occurred after the '
                                           'target prediction timestamp',
                                           "An As-Of join matches each observation's event timestamp (t_event) to the "
                                           'latest feature value whose computation timestamp satisfies t_feature <= '
                                           't_event',
                                           'Standard relational joins match on primary key alone, grabbing '
                                           'current/latest features and causing massive optimistic bias during offline '
                                           'validation',
                                           'Guarantees point-in-time correctness across time-varying entity features '
                                           '(e.g., user account balance or 30-day transaction count at the time of '
                                           'loan application)']}]},
 {'topic_tag': 'Cox Proportional Hazards Math',
  'question': 'Derive the partial likelihood function of the Cox Proportional Hazards model and explain how the '
              'proportional hazards assumption is verified.',
  'keywords': ['Cox Proportional Hazards',
               'Partial Likelihood',
               'Hazard Ratio',
               'Baseline Hazard',
               'Proportional Hazards Assumption',
               'Schoenfeld Residuals'],
  'expected_concepts': ['Hazard function formulation: h(t | X) = h_0(t) * exp(beta^T X), decomposing hazard into '
                        'non-parametric baseline hazard h_0(t) and parametric relative risk exp(beta^T X)',
                        "Cox's partial likelihood eliminates baseline hazard h_0(t) completely: L_p(beta) = prod_{i: "
                        'C_i=1} [exp(beta^T X_i) / sum_{j in R(t_i)} exp(beta^T X_j)] over risk sets R(t_i)',
                        'Proportional hazards assumption: hazard ratio between any two individuals HR = exp(beta^T '
                        '(X_1 - X_2)) is constant over time and independent of t',
                        'Verification: tested via Schoenfeld residuals (which should show zero correlation with time '
                        'or rank of failure time) and log-log survival plots'],
  'model_answer': 'The Cox Proportional Hazards model (Cox, 1972) is a semi-parametric regression framework for '
                  'time-to-event data. The hazard rate is modeled as h(t | X) = h_0(t) * exp(beta^T X), where h_0(t) '
                  'is an unspecified, arbitrary baseline hazard function, and exp(beta^T X) is the parametric '
                  "covariate multiplier. Cox's mathematical breakthrough was the Partial Likelihood function: "
                  'L_p(beta) = prod_{i: event} [exp(beta^T X_i) / sum_{j in R(t_i)} exp(beta^T X_j)], where R(t_i) is '
                  'the risk set of all individuals alive and uncensored just prior to time t_i. Because h_0(t) cancels '
                  'out identically from the numerator and denominator at every event time, beta can be estimated via '
                  'maximum partial likelihood without making any parametric assumption about baseline hazard. The '
                  'fundamental Proportional Hazards Assumption requires the hazard ratio between individuals to be '
                  'time-invariant. This is verified statistically using Schoenfeld residuals (testing whether the '
                  'correlation between scaled residuals and time is zero via Grambsch-Therneau test) and graphically '
                  'via parallel log(-log(S(t))) curves.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'The Cox model expresses the hazard rate as h(t | X) = h_0(t) * exp(beta^T X), '
                                     'separating it into an unspecified non-parametric baseline hazard h_0(t) and a '
                                     "parametric relative risk multiplier. Sir David Cox's brilliant innovation was "
                                     'the Partial Likelihood. At each event time t_i, the probability that individual '
                                     'i was the one who experienced the event, out of everyone in the risk set R(t_i) '
                                     'who could have experienced it, is exp(beta^T X_i) divided by the sum of '
                                     'exp(beta^T X_j) for all individuals j in R(t_i). Notice that h_0(t_i) appears in '
                                     'both the numerator and denominator, canceling out completely! This allows us to '
                                     'estimate the regression coefficients beta without ever estimating or specifying '
                                     'baseline hazard. The central Proportional Hazards assumption requires that the '
                                     'hazard ratio between two people remains constant over time. We verify this '
                                     'assumption using Schoenfeld residuals: under the proportional hazards '
                                     'assumption, Schoenfeld residuals should be independent of time; if a statistical '
                                     'test shows significant correlation with time, the assumption is violated, '
                                     'requiring stratified models or time-varying covariates.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'The Cox model defines the hazard as h(t) = h_0(t) * exp(beta * X). It uses '
                                     'partial likelihood to estimate beta: at each event time, it calculates the ratio '
                                     "of the event subject's hazard to the sum of hazards across the entire risk set. "
                                     "Because the baseline hazard cancels out in this ratio, you don't need to model "
                                     'baseline hazard. The proportional hazards assumption states that the hazard '
                                     'ratio between groups is constant over time, which you check using Schoenfeld '
                                     'residuals.',
                      'missing_concepts': ['Verification: tested via Schoenfeld residuals (which should show zero '
                                           'correlation with time or rank of failure time) and log-log survival '
                                           'plots']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Cox regression models survival times using a hazard ratio. It uses partial '
                                     'likelihood so that the baseline hazard function cancels out when estimating beta '
                                     'coefficients. The proportional hazard assumption means the risk multiplier stays '
                                     'the same over time. You test it using Schoenfeld residuals in R or Python '
                                     'lifelines.',
                      'missing_concepts': ["Cox's partial likelihood eliminates baseline hazard h_0(t) completely: "
                                           'L_p(beta) = prod_{i: C_i=1} [exp(beta^T X_i) / sum_{j in R(t_i)} '
                                           'exp(beta^T X_j)] over risk sets R(t_i)',
                                           'Verification: tested via Schoenfeld residuals (which should show zero '
                                           'correlation with time or rank of failure time) and log-log survival '
                                           'plots']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'The Cox model is an OSHA workplace physical safety hazard evaluation checklist '
                                     'used in civil construction engineering.',
                      'missing_concepts': ['Hazard function formulation: h(t | X) = h_0(t) * exp(beta^T X), '
                                           'decomposing hazard into non-parametric baseline hazard h_0(t) and '
                                           'parametric relative risk exp(beta^T X)',
                                           "Cox's partial likelihood eliminates baseline hazard h_0(t) completely: "
                                           'L_p(beta) = prod_{i: C_i=1} [exp(beta^T X_i) / sum_{j in R(t_i)} '
                                           'exp(beta^T X_j)] over risk sets R(t_i)',
                                           'Proportional hazards assumption: hazard ratio between any two individuals '
                                           'HR = exp(beta^T (X_1 - X_2)) is constant over time and independent of t',
                                           'Verification: tested via Schoenfeld residuals (which should show zero '
                                           'correlation with time or rank of failure time) and log-log survival '
                                           'plots']}]},
 {'topic_tag': 'Graph Analytics (PageRank & Centrality)',
  'question': 'Derive the PageRank power iteration equation with damping factor d, and contrast PageRank with Degree, '
              'Betweenness, and Eigenvector centrality.',
  'keywords': ['PageRank',
               'Graph Analytics',
               'Degree Centrality',
               'Betweenness Centrality',
               'Eigenvector Centrality',
               'Power Iteration',
               'Damping Factor',
               'Markov Chain'],
  'expected_concepts': ['PageRank models a random surfer on a directed graph: with probability d (typically 0.85) '
                        'follows an outgoing link, with probability (1 - d) teleports uniformly to any node (resolving '
                        'dead ends and spider traps)',
                        'Power iteration formula: PR(u) = (1 - d) / N + d * sum_{v in In(u)} [PR(v) / L(v)], computing '
                        'stationary distribution of the stochastic transition matrix',
                        'Degree centrality counts direct edges; Betweenness centrality measures how often a node sits '
                        'on shortest paths (geodesics) between all pairs',
                        'Eigenvector centrality scores a node based on connections to other high-scoring nodes; '
                        'PageRank is a directed, damped variant of eigenvector centrality'],
  'model_answer': "PageRank (Page & Brin, 1998) quantifies node importance in a directed network by modeling a 'random "
                  "surfer'. Let N be the total number of vertices. If a surfer strictly followed out-links, the Markov "
                  'chain would get trapped in absorbing sink nodes (dead ends) or cyclical loops (spider traps). '
                  'PageRank resolves this by introducing a damping factor d (conventionally 0.85): at each step, the '
                  'surfer follows an outgoing link with probability d, and randomly teleports to any node in the graph '
                  'with probability 1 - d. The power iteration equation is: PR(u) = (1 - d)/N + d * sum_{v in In(u)} '
                  "PR(v) / L(v), where In(u) are incoming neighbors and L(v) is v's out-degree. In matrix notation: p "
                  '= d * M * p + (1 - d)/N * 1, finding the principal eigenvector of the Google matrix (lambda = 1). '
                  'Compared to other metrics: Degree centrality measures local connectivity; Betweenness centrality '
                  'measures brokerage power by counting shortest paths traversing a node; and Eigenvector centrality '
                  'measures recursive influence, of which PageRank is the directed, normalized, and teleport-damped '
                  'evolution.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'PageRank treats node importance recursively: a webpage is important if other '
                                     'important pages link to it. It models a random surfer who clicks a link with '
                                     'probability d (damping factor, usually 0.85) and teleports uniformly to any '
                                     'random page with probability (1 - d). The damping factor solves dead ends (nodes '
                                     'with no out-links) and spider traps (absorbing cycles) that would break the '
                                     'Markov chain. The power iteration equation is: PR(u) = (1 - d)/N + d * sum over '
                                     'all incoming nodes v of [PR(v) / OutDegree(v)]. It computes the principal '
                                     'eigenvector of the transition matrix. In contrast, Degree Centrality just counts '
                                     'direct connections. Betweenness Centrality counts how many shortest paths pass '
                                     'through a node, identifying critical bridge nodes. Eigenvector Centrality weighs '
                                     "connections by the neighbor's score, and PageRank is essentially a directed, "
                                     'damped, degree-normalized version of eigenvector centrality.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'PageRank uses the random surfer model where a user follows links with '
                                     'probability d (0.85) and teleports to a random page with probability 1-d. The '
                                     "formula updates each node's rank based on incoming links divided by their "
                                     'out-degree: PR(u) = (1-d)/N + d * sum(PR(v)/L(v)). It runs power iteration until '
                                     'ranks converge. Degree centrality just counts edges, while betweenness '
                                     'centrality measures shortest paths passing through a node. PageRank is a damped '
                                     'eigenvector centrality for directed graphs.',
                      'missing_concepts': ['PageRank models a random surfer on a directed graph: with probability d '
                                           '(typically 0.85) follows an outgoing link, with probability (1 - d) '
                                           'teleports uniformly to any node (resolving dead ends and spider traps)']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'PageRank was created by Google to rank web pages. The damping factor is 0.85 and '
                                     'represents a user clicking links or jumping to a new page. Degree centrality is '
                                     'how many connections a node has, and betweenness centrality is how often a node '
                                     'connects two groups.',
                      'missing_concepts': ['Power iteration formula: PR(u) = (1 - d) / N + d * sum_{v in In(u)} [PR(v) '
                                           '/ L(v)], computing stationary distribution of the stochastic transition '
                                           'matrix',
                                           'Eigenvector centrality scores a node based on connections to other '
                                           'high-scoring nodes; PageRank is a directed, damped variant of eigenvector '
                                           'centrality']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'PageRank is a CSS webpage layout styling property used in responsive web design.',
                      'missing_concepts': ['PageRank models a random surfer on a directed graph: with probability d '
                                           '(typically 0.85) follows an outgoing link, with probability (1 - d) '
                                           'teleports uniformly to any node (resolving dead ends and spider traps)',
                                           'Power iteration formula: PR(u) = (1 - d) / N + d * sum_{v in In(u)} [PR(v) '
                                           '/ L(v)], computing stationary distribution of the stochastic transition '
                                           'matrix',
                                           'Degree centrality counts direct edges; Betweenness centrality measures how '
                                           'often a node sits on shortest paths (geodesics) between all pairs',
                                           'Eigenvector centrality scores a node based on connections to other '
                                           'high-scoring nodes; PageRank is a directed, damped variant of eigenvector '
                                           'centrality']}]},
 {'topic_tag': 'Streaming Anomaly Detection via Kalman Filter',
  'question': 'How does a Kalman Filter update state estimates and use innovation residuals for streaming anomaly '
              'detection in noisy time series?',
  'keywords': ['Kalman Filter',
               'Streaming Anomaly Detection',
               'State-Space Model',
               'Innovation Residuals',
               'Kalman Gain',
               'Covariance Update',
               'Sensor Noise'],
  'expected_concepts': ['Linear dynamical state-space formulation: State equation x_k = F x_{k-1} + B u_k + w_k and '
                        'Measurement equation z_k = H x_k + v_k with Gaussian noises w_k ~ N(0, Q) and v_k ~ N(0, R)',
                        'Predict step: projects state estimate ahead x_hat^- and error covariance P^- based on process '
                        'dynamics',
                        'Update step: computes innovation residual y_k = z_k - H x_hat^-, innovation covariance S_k = '
                        'H P^- H^T + R, and optimal Kalman Gain K_k = P^- H^T S_k^-1',
                        'Anomaly detection evaluates normalized innovation squared (Mahalanobis distance) y_k^T S_k^-1 '
                        'y_k against a Chi-Square distribution threshold'],
  'model_answer': 'A Kalman Filter is an optimal recursive Bayesian estimator for linear dynamical systems corrupted '
                  'by Gaussian process noise w_k ~ N(0, Q) and measurement noise v_k ~ N(0, R). It operates in an '
                  'alternating two-phase loop: 1) Predict Step: Projects the state estimate and error covariance '
                  'forward in time: x_hat^-_k = F * x_hat_{k-1} and P^-_k = F * P_{k-1} * F^T + Q; 2) Update Step: '
                  'Computes the innovation residual y_k = z_k - H * x_hat^-_k (the discrepancy between observed '
                  'measurement and expected prediction), the innovation covariance S_k = H * P^-_k * H^T + R, and the '
                  'optimal Kalman Gain K_k = P^-_k * H^T * S_k^{-1}. The posterior state updates as x_hat_k = '
                  'x_hat^-_k + K_k * y_k. For streaming anomaly detection, rather than using raw measurement '
                  'deviations, we evaluate the Normalized Innovation Squared (NIS / Mahalanobis distance): d_k^2 = '
                  'y_k^T * S_k^{-1} * y_k. Under normal operations, d_k^2 follows a Chi-square distribution with '
                  'degrees of freedom equal to measurement dimension m; values exceeding the critical chi-square '
                  'threshold flag instantaneous streaming anomalies.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'The Kalman Filter operates in a continuous predict-update loop for state-space '
                                     'tracking in noisy streams. In the predict step, it projects the state ahead '
                                     'using physics/dynamics (x_hat^- = F * x) and projects the uncertainty covariance '
                                     'P ahead adding process noise Q. In the update step, it receives a new noisy '
                                     'measurement z_k and calculates the innovation residual y_k = z_k - H * x_hat^-, '
                                     'which is the error between what we observed and what the model expected. It '
                                     'calculates the Kalman Gain K based on the ratio of state uncertainty to sensor '
                                     'noise, and updates the state. For streaming anomaly detection, the innovation '
                                     'residual y_k is normally distributed with covariance S_k. You compute the '
                                     'Normalized Innovation Squared—essentially the Mahalanobis distance d^2 = y^T * '
                                     'S^-1 * y. Under the null hypothesis of normal operation, this follows a '
                                     'Chi-square distribution. When a sensor spikes or an anomaly hits, the '
                                     'measurement violates the expected trajectory and d^2 spikes above the chi-square '
                                     'critical threshold, triggering an immediate real-time anomaly alert.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'A Kalman filter has a predict step and an update step. Predict estimates the '
                                     'next state and covariance using the transition matrix. When a measurement '
                                     'arrives, it calculates the innovation residual y = z - H*x_hat, which is the '
                                     'prediction error. It uses the Kalman gain to blend the prediction and '
                                     'measurement. For anomaly detection, you take the innovation residual and '
                                     'calculate its Mahalanobis distance using the innovation covariance. If this '
                                     'squared residual exceeds a chi-square threshold, it flags an anomaly.',
                      'missing_concepts': ['Linear dynamical state-space formulation: State equation x_k = F x_{k-1} + '
                                           'B u_k + w_k and Measurement equation z_k = H x_k + v_k with Gaussian '
                                           'noises w_k ~ N(0, Q) and v_k ~ N(0, R)']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Kalman filters filter out sensor noise using a predict and update cycle. It '
                                     'calculates the error between the sensor reading and the predicted state, called '
                                     'the residual. If the residual is much larger than expected, the data point is '
                                     'flagged as an anomaly.',
                      'missing_concepts': ['Linear dynamical state-space formulation: State equation x_k = F x_{k-1} + '
                                           'B u_k + w_k and Measurement equation z_k = H x_k + v_k with Gaussian '
                                           'noises w_k ~ N(0, Q) and v_k ~ N(0, R)',
                                           'Anomaly detection evaluates normalized innovation squared (Mahalanobis '
                                           'distance) y_k^T S_k^-1 y_k against a Chi-Square distribution threshold']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'A Kalman filter is an oil filter replacement sensor used in automotive engines.',
                      'missing_concepts': ['Linear dynamical state-space formulation: State equation x_k = F x_{k-1} + '
                                           'B u_k + w_k and Measurement equation z_k = H x_k + v_k with Gaussian '
                                           'noises w_k ~ N(0, Q) and v_k ~ N(0, R)',
                                           'Predict step: projects state estimate ahead x_hat^- and error covariance '
                                           'P^- based on process dynamics',
                                           'Update step: computes innovation residual y_k = z_k - H x_hat^-, '
                                           'innovation covariance S_k = H P^- H^T + R, and optimal Kalman Gain K_k = '
                                           'P^- H^T S_k^-1',
                                           'Anomaly detection evaluates normalized innovation squared (Mahalanobis '
                                           'distance) y_k^T S_k^-1 y_k against a Chi-Square distribution threshold']}]},
 {'topic_tag': 'Information Theory: KL Divergence & Mutual Info',
  'question': 'Formulate Kullback-Leibler (KL) Divergence and Mutual Information, and explain why KL Divergence is '
              'asymmetric and non-negative.',
  'keywords': ['Information Theory',
               'KL Divergence',
               'Mutual Information',
               'Relative Entropy',
               'Gibbs Inequality',
               'Asymmetry',
               'Shannon Entropy'],
  'expected_concepts': ['KL Divergence (Relative Entropy) formula: D_KL(P || Q) = sum_{x} P(x) * log(P(x) / Q(x)), '
                        'measuring information lost when Q is used to approximate true distribution P',
                        'Asymmetry: D_KL(P || Q) != D_KL(Q || P), meaning KL divergence is a statistical divergence '
                        'rather than a true distance metric (violates symmetry and triangle inequality)',
                        "Non-negativity (Gibbs' Inequality): D_KL(P || Q) >= 0 for all P, Q, with equality if and only "
                        "if P = Q almost everywhere, proven via Jensen's Inequality",
                        'Mutual Information I(X; Y) = D_KL(P(X, Y) || P(X)P(Y)) = H(X) - H(X|Y), quantifying reduction '
                        'in uncertainty about X gained from observing Y'],
  'model_answer': 'In information theory (Shannon, 1948; Kullback & Leibler, 1951), KL Divergence D_KL(P || Q) '
                  '(relative entropy) quantifies the information lost when an approximating distribution Q is used to '
                  'represent a true reference distribution P: D_KL(P || Q) = sum_x P(x) * log(P(x) / Q(x)). Key '
                  'mathematical properties include: 1) Asymmetry: D_KL(P || Q) != D_KL(Q || P). In machine learning, '
                  'minimizing D_KL(P || Q) forces Q to cover all modes of P (mean-seeking/zero-avoiding), whereas '
                  'minimizing D_KL(Q || P) penalizes Q for placing mass where P is zero, causing mode-collapse '
                  '(mode-seeking/zero-forcing). Because it violates symmetry and the triangle inequality, it is a '
                  "directed divergence, not a metric; 2) Non-negativity: D_KL(P || Q) >= 0 (Gibbs' Inequality), proven "
                  "via Jensen's inequality applied to the strictly concave logarithm function (-log(x)), equaling zero "
                  'if and only if P = Q; 3) Mutual Information I(X; Y) measures the shared information between two '
                  'variables: I(X; Y) = D_KL(P(X,Y) || P(X)P(Y)) = H(X) - H(X|Y), capturing linear and non-linear '
                  'dependencies by measuring divergence from product marginal independence.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'Kullback-Leibler Divergence, or relative entropy, measures the extra information '
                                     'or bits required to encode samples from distribution P using an approximate '
                                     'distribution Q: D_KL(P || Q) = sum P(x) * log(P(x) / Q(x)). It has two critical '
                                     'properties. First, it is non-negative: D_KL(P || Q) >= 0, with equality only '
                                     "when P = Q, which is proven using Jensen's inequality on the concave log "
                                     'function. Second, it is strictly asymmetric: D_KL(P || Q) does not equal D_KL(Q '
                                     "|| P), which is why it's a divergence and not a distance metric. In variational "
                                     'inference, minimizing D_KL(P || Q) is zero-avoiding and forces Q to cover the '
                                     'entire support of P, while minimizing D_KL(Q || P) is zero-forcing and forces Q '
                                     'to collapse onto a single mode. Mutual Information I(X; Y) is simply the KL '
                                     'divergence between the joint distribution P(X, Y) and the product of the '
                                     'marginals P(X)P(Y): I(X; Y) = H(X) - H(X|Y). It equals zero if and only if X and '
                                     'Y are completely independent, capturing all linear and non-linear relationships.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'KL divergence measures how much distribution Q differs from true distribution P, '
                                     "defined as sum P(x) * log(P(x) / Q(x)). It is always non-negative by Gibbs' "
                                     'inequality, equaling zero only when P equals Q. It is asymmetric because D_KL(P '
                                     "|| Q) does not equal D_KL(Q || P), which means it's not a true mathematical "
                                     'distance. Mutual information is the KL divergence between the joint distribution '
                                     'and the independent product of marginals, measuring how much knowing Y reduces '
                                     'uncertainty about X.',
                      'missing_concepts': ['KL Divergence (Relative Entropy) formula: D_KL(P || Q) = sum_{x} P(x) * '
                                           'log(P(x) / Q(x)), measuring information lost when Q is used to approximate '
                                           'true distribution P']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'KL divergence calculates the distance between two probability distributions. It '
                                     'is always positive or zero. It is asymmetric because swapping P and Q gives a '
                                     "different result, so it's not a real distance metric. Mutual information "
                                     'measures how correlated two variables are using entropy.',
                      'missing_concepts': ['KL Divergence (Relative Entropy) formula: D_KL(P || Q) = sum_{x} P(x) * '
                                           'log(P(x) / Q(x)), measuring information lost when Q is used to approximate '
                                           'true distribution P',
                                           'Mutual Information I(X; Y) = D_KL(P(X, Y) || P(X)P(Y)) = H(X) - H(X|Y), '
                                           'quantifying reduction in uncertainty about X gained from observing Y']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'KL divergence is an optical lens refraction equation used in computer vision for '
                                     'self-driving cameras.',
                      'missing_concepts': ['KL Divergence (Relative Entropy) formula: D_KL(P || Q) = sum_{x} P(x) * '
                                           'log(P(x) / Q(x)), measuring information lost when Q is used to approximate '
                                           'true distribution P',
                                           'Asymmetry: D_KL(P || Q) != D_KL(Q || P), meaning KL divergence is a '
                                           'statistical divergence rather than a true distance metric (violates '
                                           'symmetry and triangle inequality)',
                                           "Non-negativity (Gibbs' Inequality): D_KL(P || Q) >= 0 for all P, Q, with "
                                           "equality if and only if P = Q almost everywhere, proven via Jensen's "
                                           'Inequality',
                                           'Mutual Information I(X; Y) = D_KL(P(X, Y) || P(X)P(Y)) = H(X) - H(X|Y), '
                                           'quantifying reduction in uncertainty about X gained from observing Y']}]},
 {'topic_tag': 'Extreme Value Theory for Rare Events',
  'question': 'Explain how the Generalized Extreme Value (GEV) distribution and Peaks Over Threshold (POT) approach '
              'model tail risk for rare catastrophic events.',
  'keywords': ['Extreme Value Theory (EVT)',
               'GEV Distribution',
               'Peaks Over Threshold (POT)',
               'Generalized Pareto Distribution (GPD)',
               'Block Maxima',
               'Shape Parameter (Xi)',
               'Tail Risk'],
  'expected_concepts': ['Central Limit Theorem applies to sample means; Fisher-Tippett-Gnedenko Theorem applies to '
                        'sample maxima, proving normalized maxima converge to the GEV distribution',
                        'Block Maxima approach partitions data into time blocks (e.g., annual maxima) and fits GEV: '
                        'unified into three tail types governed by shape parameter xi (Frechet heavy tail xi>0, Gumbel '
                        'exponential tail xi=0, Weibull bounded tail xi<0)',
                        'Peaks Over Threshold (POT) approach extracts all excesses over a high threshold u (Y = X - u '
                        '| X > u), utilizing data more efficiently than block maxima',
                        'Pickands-Balkema-de Haan Theorem proves threshold excesses asymptotically follow the '
                        'Generalized Pareto Distribution (GPD), critical for Value-at-Risk (VaR) and Expected '
                        'Shortfall (ES)'],
  'model_answer': 'Extreme Value Theory (EVT) provides the statistical framework for modeling the asymptotic '
                  'distribution of extreme tail observations (e.g., 100-year floods, financial market crashes), where '
                  'standard Central Limit Theorem assumptions fail. EVT operates via two foundational paradigms: 1) '
                  'Block Maxima (Fisher-Tippett-Gnedenko Theorem): Divides data into equal non-overlapping blocks of '
                  'length n (e.g., yearly intervals) and models block maxima M_n = max(X_1, ..., X_n). As n -> '
                  'infinity, normalized maxima converge to the Generalized Extreme Value (GEV) distribution: G(z) = '
                  'exp(-(1 + xi * (z - mu)/sigma)^{-1/xi}). The shape parameter xi dictates tail behavior: xi > 0 '
                  'yields Fréchet (heavy, power-law tails); xi = 0 yields Gumbel (exponential tails); and xi < 0 '
                  'yields Weibull (bounded upper limit); 2) Peaks Over Threshold (POT) (Pickands-Balkema-de Haan '
                  'Theorem): Instead of discarding intermediate data via block maxima, POT models all observations '
                  'exceeding a sufficiently high threshold u. The conditional excess distribution F_u(y) = P(X - u <= '
                  'y | X > u) converges to the Generalized Pareto Distribution (GPD). POT makes far more efficient use '
                  'of available tail data, forming the industry gold standard for calculating Value-at-Risk (VaR) and '
                  'Expected Shortfall.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'While the Central Limit Theorem tells you about the distribution of the mean, '
                                     'Extreme Value Theory tells you about the behavior of the extreme tail. There are '
                                     'two primary approaches. The first is Block Maxima, founded on the '
                                     'Fisher-Tippett-Gnedenko theorem: you split your time series into blocks (like '
                                     'annual maximum temperature) and fit the Generalized Extreme Value (GEV) '
                                     'distribution. The shape parameter xi determines tail thickness: xi > 0 is a '
                                     'heavy-tailed Fréchet distribution, xi = 0 is an exponential Gumbel tail, and xi '
                                     '< 0 is a bounded Weibull tail. The second, more data-efficient approach is Peaks '
                                     'Over Threshold (POT), governed by the Pickands-Balkema-de Haan theorem: you pick '
                                     'a high threshold u and model all excesses (X - u) that cross above it. These '
                                     'excesses asymptotically follow the Generalized Pareto Distribution (GPD). POT '
                                     'avoids discarding the second-highest extreme in a year, making it the preferred '
                                     'standard in financial risk management for computing 99.9% Value-at-Risk and '
                                     'Expected Shortfall.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'Extreme Value Theory models rare catastrophic events where normal distributions '
                                     'underestimate risk. Block Maxima takes the maximum in each time block and fits '
                                     'the GEV distribution, where the shape parameter xi controls whether tails are '
                                     'heavy, exponential, or bounded. Peaks Over Threshold (POT) is more efficient: it '
                                     'looks at all data points that exceed a high threshold u and models the excess '
                                     'using the Generalized Pareto Distribution (GPD). POT is widely used in finance '
                                     'to calculate Value at Risk.',
                      'missing_concepts': ['Central Limit Theorem applies to sample means; Fisher-Tippett-Gnedenko '
                                           'Theorem applies to sample maxima, proving normalized maxima converge to '
                                           'the GEV distribution']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Extreme value theory is for tail risk like market crashes or floods. Block '
                                     'maxima takes the highest number in each year and fits a GEV distribution. Peaks '
                                     'over threshold looks at everything above a cutoff and fits a Generalized Pareto '
                                     "Distribution. POT is better because it doesn't throw away extreme numbers.",
                      'missing_concepts': ['Central Limit Theorem applies to sample means; Fisher-Tippett-Gnedenko '
                                           'Theorem applies to sample maxima, proving normalized maxima converge to '
                                           'the GEV distribution',
                                           'Block Maxima approach partitions data into time blocks (e.g., annual '
                                           'maxima) and fits GEV: unified into three tail types governed by shape '
                                           'parameter xi (Frechet heavy tail xi>0, Gumbel exponential tail xi=0, '
                                           'Weibull bounded tail xi<0)']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'Extreme Value Theory is an extreme programming agile development methodology '
                                     'used for rapid software deployments.',
                      'missing_concepts': ['Central Limit Theorem applies to sample means; Fisher-Tippett-Gnedenko '
                                           'Theorem applies to sample maxima, proving normalized maxima converge to '
                                           'the GEV distribution',
                                           'Block Maxima approach partitions data into time blocks (e.g., annual '
                                           'maxima) and fits GEV: unified into three tail types governed by shape '
                                           'parameter xi (Frechet heavy tail xi>0, Gumbel exponential tail xi=0, '
                                           'Weibull bounded tail xi<0)',
                                           'Peaks Over Threshold (POT) approach extracts all excesses over a high '
                                           'threshold u (Y = X - u | X > u), utilizing data more efficiently than '
                                           'block maxima',
                                           'Pickands-Balkema-de Haan Theorem proves threshold excesses asymptotically '
                                           'follow the Generalized Pareto Distribution (GPD), critical for '
                                           'Value-at-Risk (VaR) and Expected Shortfall (ES)']}]},
 {'topic_tag': 'Differential Privacy Guarantees',
  'question': 'Formulate (epsilon, delta)-differential privacy and explain how the Laplace and Gaussian mechanisms '
              'inject calibrated noise based on global sensitivity.',
  'keywords': ['Differential Privacy',
               '(epsilon, delta)-DP',
               'Laplace Mechanism',
               'Gaussian Mechanism',
               'Global Sensitivity',
               'Privacy Budget',
               'Composition Theorems'],
  'expected_concepts': ['Mathematical definition: algorithm M satisfies (epsilon, delta)-DP if for all neighboring '
                        "datasets D, D' differing by at most one individual, P(M(D) in S) <= exp(epsilon) * P(M(D') in "
                        'S) + delta',
                        "Global sensitivity Delta f = max_{D, D'} ||f(D) - f(D')|| measures maximum change in query "
                        'output caused by adding or removing a single individual',
                        'Laplace Mechanism injects noise drawn from Lap(0, Delta f / epsilon), achieving pure '
                        'epsilon-differential privacy (delta = 0)',
                        'Gaussian Mechanism injects noise drawn from N(0, sigma^2) with sigma proportional to sqrt(2 * '
                        'ln(1.25 / delta)) * Delta_2 f / epsilon, achieving (epsilon, delta)-DP for multi-dimensional '
                        'vector queries'],
  'model_answer': 'Differential Privacy (Dwork et al., 2006) provides mathematical guarantees against privacy leakage '
                  'and membership inference attacks. A randomized mechanism M satisfies (epsilon, delta)-Differential '
                  "Privacy if for all neighboring datasets D and D' differing by at most one individual's record, and "
                  "for all query output subsets S: P(M(D) in S) <= exp(epsilon) * P(M(D') in S) + delta. Here, epsilon "
                  '(privacy budget) bounds the maximum relative multiplicative change in output probabilities, while '
                  'delta represents the acceptable probability of catastrophic failure (typically delta << 1/|D|). To '
                  "achieve privacy, noise is calibrated to the query's L1 or L2 Global Sensitivity: Delta f = "
                  "max_{D,D'} ||f(D) - f(D')||, the maximum impact one individual can have on query output. The "
                  'Laplace Mechanism adds zero-mean noise drawn from Lap(Delta f_1 / epsilon), satisfying pure '
                  'epsilon-DP (delta = 0). The Gaussian Mechanism adds noise from Normal(0, sigma^2) where sigma = '
                  'sqrt(2 * ln(1.25/delta)) * Delta f_2 / epsilon, satisfying (epsilon, delta)-DP, which scales more '
                  'gracefully for high-dimensional vector outputs.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'Differential privacy mathematically guarantees that an observer cannot reliably '
                                     'determine whether any single individual was included in a dataset. A randomized '
                                     'algorithm M satisfies (epsilon, delta)-DP if for any two neighboring datasets D '
                                     "and D' differing by just one person, P(M(D) in S) <= exp(epsilon) * P(M(D') in "
                                     'S) + delta. Epsilon is the privacy budget: smaller epsilon means tighter privacy '
                                     'and more noise. Delta is a tiny failure tolerance, strictly smaller than 1/N. To '
                                     "add the right amount of noise, you compute the query's Global Sensitivity Delta "
                                     'f—the maximum amount adding or removing one person can change the query answer. '
                                     'For a count query, Delta f is 1. The Laplace mechanism injects noise drawn from '
                                     'Laplace(0, Delta f / epsilon) to provide pure epsilon-DP. The Gaussian mechanism '
                                     'adds noise from Normal(0, sigma^2) calibrated to L2 sensitivity, providing '
                                     '(epsilon, delta)-DP, which is preferred for high-dimensional vector queries and '
                                     'deep learning gradients.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': "Differential privacy ensures that adding or removing one person's record doesn't "
                                     'noticeably change the output of a query. The formula is P(M(D)) <= exp(epsilon) '
                                     "* P(M(D')) + delta, where epsilon is the privacy budget. Noise is calibrated "
                                     'using global sensitivity, which is the maximum difference one person can make to '
                                     'the query output. The Laplace mechanism adds noise scaled by sensitivity divided '
                                     'by epsilon, while the Gaussian mechanism adds normal noise for (epsilon, '
                                     'delta)-differential privacy.',
                      'missing_concepts': ['Gaussian Mechanism injects noise drawn from N(0, sigma^2) with sigma '
                                           'proportional to sqrt(2 * ln(1.25 / delta)) * Delta_2 f / epsilon, '
                                           'achieving (epsilon, delta)-DP for multi-dimensional vector queries']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Differential privacy protects user data by adding noise to query results so '
                                     'nobody can tell if you are in the database. Epsilon is the privacy budget where '
                                     'smaller numbers mean more noise. You use the Laplace mechanism or Gaussian '
                                     'mechanism to add noise based on how sensitive the query is.',
                      'missing_concepts': ['Mathematical definition: algorithm M satisfies (epsilon, delta)-DP if for '
                                           "all neighboring datasets D, D' differing by at most one individual, P(M(D) "
                                           "in S) <= exp(epsilon) * P(M(D') in S) + delta",
                                           "Global sensitivity Delta f = max_{D, D'} ||f(D) - f(D')|| measures maximum "
                                           'change in query output caused by adding or removing a single individual']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'Differential privacy is a legal terms of service disclaimer displayed on web '
                                     'cookies banner popups.',
                      'missing_concepts': ['Mathematical definition: algorithm M satisfies (epsilon, delta)-DP if for '
                                           "all neighboring datasets D, D' differing by at most one individual, P(M(D) "
                                           "in S) <= exp(epsilon) * P(M(D') in S) + delta",
                                           "Global sensitivity Delta f = max_{D, D'} ||f(D) - f(D')|| measures maximum "
                                           'change in query output caused by adding or removing a single individual',
                                           'Laplace Mechanism injects noise drawn from Lap(0, Delta f / epsilon), '
                                           'achieving pure epsilon-differential privacy (delta = 0)',
                                           'Gaussian Mechanism injects noise drawn from N(0, sigma^2) with sigma '
                                           'proportional to sqrt(2 * ln(1.25 / delta)) * Delta_2 f / epsilon, '
                                           'achieving (epsilon, delta)-DP for multi-dimensional vector queries']}]},
 {'topic_tag': 'Uplift Modeling for Targeted Interventions',
  'question': 'How do two-model approaches and class transformation methods estimate Conditional Average Treatment '
              'Effects (CATE) in uplift modeling?',
  'keywords': ['Uplift Modeling',
               'CATE',
               'Persuadables vs Sleeping Dogs',
               'Two-Model Approach',
               'Class Variable Transformation',
               'Qini Curve',
               'Targeted Marketing'],
  'expected_concepts': ['Customer segmentation taxonomy: Persuadables (convert only with treatment), Sure Things '
                        '(convert regardless), Lost Causes (never convert), and Sleeping Dogs / Do Not Disturbs '
                        '(treatment triggers negative response)',
                        'Uplift models estimate Conditional Average Treatment Effect: tau(X) = E[Y(1) - Y(0) | X], '
                        'predicting incremental lift generated by treatment rather than baseline conversion '
                        'probability',
                        'Two-Model (T-Learner) fits separate model on treated group mu_1(X) and control group mu_0(X), '
                        'estimating uplift as tau(X) = mu_1(X) - mu_0(X); simple but prone to subtracting noisy '
                        'estimates',
                        'Class Transformation method defines transformed target Z_i = 2 * Y_i if T_i=1, and -2 * Y_i '
                        'if T_i=0 (for 50/50 RCT), reducing uplift estimation to a single regression or classification '
                        'task: E[Z|X] = tau(X)'],
  'model_answer': 'Standard propensity modeling predicts conversion probability P(Y=1 | X), which mistakenly targets '
                  "'Sure Things' (users who would convert anyway) while wasting budget. Uplift modeling directly "
                  'predicts the Conditional Average Treatment Effect (CATE): tau(x) = E[Y(1) - Y(0) | X = x]—the '
                  'causal incremental lift induced by the intervention. It partitions customers into four behavioral '
                  'personas: Persuadables (positive uplift, target these), Sure Things (zero uplift), Lost Causes '
                  '(zero uplift), and Sleeping Dogs (negative uplift, e.g., renewal reminder triggers cancellation). '
                  'Two primary estimation frameworks exist: 1) Two-Model Approach (T-Learner): Trains model M_1 on the '
                  'treated cohort and model M_0 on the control cohort, estimating uplift as tau(x) = M_1(x) - M_0(x). '
                  'While flexible, it can suffer from high variance because each model optimizes for baseline outcome '
                  "rather than the treatment difference; 2) Class Variable Transformation (Lai's Generalized Method): "
                  'For balanced RCT data (P(T)=0.5), defines a transformed response variable Z_i = Y_i * T_i + (1 - '
                  'Y_i) * (1 - T_i) (or Z_i = 2 * Y_i * (2 * T_i - 1)). Mathematically, E[Z_i | X = x] = tau(x), '
                  'allowing any standard regression or tree algorithm to directly optimize uplift in a single model, '
                  'evaluated via Qini curves.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'Standard response models predict who will buy, which wastes money targeting '
                                     "'Sure Things' who would buy anyway. Uplift modeling predicts the Conditional "
                                     'Average Treatment Effect (CATE): tau(X) = E[Y(1) - Y(0) | X], which is the '
                                     'incremental impact of the marketing treatment. It categorizes users into four '
                                     'personas: Persuadables (who only buy if treated—your real target), Sure Things, '
                                     'Lost Causes, and Sleeping Dogs (who unsubscribe if you contact them). There are '
                                     'two main ways to model uplift. The Two-Model approach (T-Learner) trains one '
                                     'model on the treated group and one on the control group, and subtracts their '
                                     "predictions: tau(X) = M_1(X) - M_0(X). It's simple, but because both models "
                                     'focus on predicting baseline conversion, subtracting two noisy predictions can '
                                     'yield noisy uplift estimates. The Class Transformation method creates a single '
                                     'transformed target variable: Z = 2*Y if treated, and -2*Y if control (for 50/50 '
                                     'splits). It is mathematically proven that E[Z|X] equals the true causal uplift '
                                     'tau(X). This lets you train a single standard XGBoost or Random Forest model '
                                     'directly on Z to optimize incremental lift, which you evaluate using Qini '
                                     'curves.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'Uplift modeling estimates the incremental causal effect of treatment, CATE = '
                                     'E[Y(1) - Y(0) | X], to avoid wasting budget on people who would convert anyway '
                                     "or bothering 'sleeping dogs' who churn when contacted. The Two-Model approach "
                                     'fits one model on treated users and one on control users, taking the difference '
                                     'M1(X) - M0(X). The class transformation method creates a transformed target '
                                     'variable Z where E[Z|X] equals the uplift, allowing you to train a single model '
                                     'to predict incremental gains, evaluated with Qini curves.',
                      'missing_concepts': ['Customer segmentation taxonomy: Persuadables (convert only with '
                                           'treatment), Sure Things (convert regardless), Lost Causes (never convert), '
                                           'and Sleeping Dogs / Do Not Disturbs (treatment triggers negative '
                                           'response)']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Uplift modeling predicts which customers will buy only if you send them a '
                                     'discount coupon. Two-model approach trains one model on people who got the '
                                     "coupon and one model on people who didn't, and subtracts them. Class "
                                     'transformation transforms the target so you can use one model. You evaluate it '
                                     'with a Qini curve.',
                      'missing_concepts': ['Uplift models estimate Conditional Average Treatment Effect: tau(X) = '
                                           'E[Y(1) - Y(0) | X], predicting incremental lift generated by treatment '
                                           'rather than baseline conversion probability',
                                           'Customer segmentation taxonomy: Persuadables (convert only with '
                                           'treatment), Sure Things (convert regardless), Lost Causes (never convert), '
                                           'and Sleeping Dogs / Do Not Disturbs (treatment triggers negative '
                                           'response)']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'Uplift modeling is an aerodynamic engineering simulation used to calculate '
                                     'aircraft wing lift during takeoff.',
                      'missing_concepts': ['Customer segmentation taxonomy: Persuadables (convert only with '
                                           'treatment), Sure Things (convert regardless), Lost Causes (never convert), '
                                           'and Sleeping Dogs / Do Not Disturbs (treatment triggers negative response)',
                                           'Uplift models estimate Conditional Average Treatment Effect: tau(X) = '
                                           'E[Y(1) - Y(0) | X], predicting incremental lift generated by treatment '
                                           'rather than baseline conversion probability',
                                           'Two-Model (T-Learner) fits separate model on treated group mu_1(X) and '
                                           'control group mu_0(X), estimating uplift as tau(X) = mu_1(X) - mu_0(X); '
                                           'simple but prone to subtracting noisy estimates',
                                           'Class Transformation method defines transformed target Z_i = 2 * Y_i if '
                                           'T_i=1, and -2 * Y_i if T_i=0 (for 50/50 RCT), reducing uplift estimation '
                                           'to a single regression or classification task: E[Z|X] = tau(X)']}]},
 {'topic_tag': 'Multi-Armed Bandit UCB1 & Thompson Sampling',
  'question': 'Formulate the Upper Confidence Bound (UCB1) action selection rule and Thompson Sampling posterior '
              'update for Bernoulli bandits.',
  'keywords': ['Multi-Armed Bandit',
               'UCB1',
               'Thompson Sampling',
               'Beta-Bernoulli Conjugacy',
               'Optimism in the Face of Uncertainty',
               "Hoeffding's Inequality",
               'Regret Bounds'],
  'expected_concepts': ["UCB1 implements 'optimism in the face of uncertainty': chooses arm maximizing a_t = argmax_i "
                        '[mu_hat_i + sqrt((2 * ln(t)) / n_i)], balancing empirical reward with exploration bonus',
                        "Exploration bonus sqrt((2 * ln(t)) / n_i) derives from Hoeffding's Inequality, shrinking as "
                        'arm i is pulled more often and expanding as total rounds t grow',
                        'Thompson Sampling (posterior sampling) uses Bayesian probability matching: samples theta_i ~ '
                        'Beta(alpha_i, beta_i) for each arm, choosing arm with highest sampled reward',
                        'Bernoulli conjugate updating: pulls arm a_t; if reward r=1, updates alpha_{a_t} = alpha_{a_t} '
                        '+ 1; if r=0, updates beta_{a_t} = beta_{a_t} + 1, achieving asymptotic optimal logarithmic '
                        'regret'],
  'model_answer': 'Multi-Armed Bandit algorithms solve the exploration-exploitation trade-off with sub-linear '
                  'logarithmic regret O(log T), avoiding the sub-optimal regret of epsilon-greedy. 1) UCB1 (Auer et '
                  "al., 2002) is a deterministic frequentist algorithm adhering to 'optimism in the face of "
                  "uncertainty'. It selects the arm maximizing: a_t = argmax_i [mu_hat_i + c * sqrt((2 * ln(t)) / "
                  'n_i)], where mu_hat_i is empirical mean reward, t is total rounds, and n_i is the pull count of arm '
                  "i. The exploration bonus derives from Hoeffding's inequality: arms with few pulls have wide "
                  'confidence bounds, forcing exploration; as n_i grows, the bonus shrinks, favoring exploitation; 2) '
                  'Thompson Sampling (Agrawal & Goyal, 2012) is a randomized Bayesian algorithm implementing '
                  'probability matching. For Bernoulli rewards, it maintains a conjugate Beta prior Beta(alpha_i, '
                  "beta_i) (initialized Beta(1,1)) for each arm's success probability. At step t, it draws a random "
                  'sample theta_i ~ Beta(alpha_i, beta_i) for each arm and selects arm a_t = argmax_i theta_i. Upon '
                  'observing binary reward r in {0, 1}, it updates the winner: alpha_{a_t} = alpha_{a_t} + r and '
                  'beta_{a_t} = beta_{a_t} + (1 - r). Thompson Sampling typically outperforms UCB1 empirically by '
                  'exploring smoothly without rigid confidence fences.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'UCB1 and Thompson Sampling are the two gold-standard bandit algorithms that '
                                     "achieve theoretical logarithmic regret. UCB1 follows 'optimism in the face of "
                                     "uncertainty': at each step, it picks the arm that maximizes the empirical mean "
                                     'reward plus an exploration bonus: mu_hat_i + sqrt((2 * ln(t)) / n_i). The square '
                                     "root term comes from Hoeffding's Inequality. If an arm hasn't been pulled much, "
                                     'its n_i is small, making the confidence bound huge and forcing exploration; as '
                                     'you pull it more, the bonus shrinks and exploitation takes over. Thompson '
                                     'Sampling is a Bayesian probability-matching approach. For Bernoulli conversion '
                                     'rates, each arm maintains a Beta distribution Beta(alpha_i, beta_i). At every '
                                     "round, you draw a random sample theta_i from each arm's Beta distribution and "
                                     'pull the arm with the highest sample. If it converts (r=1), you update alpha = '
                                     'alpha + 1; if not (r=0), you update beta = beta + 1. Thompson Sampling naturally '
                                     'balances exploration because uncertain arms have wide Beta distributions that '
                                     'occasionally draw high values, but as data accumulates, the posterior '
                                     'concentrates tightly on the true best arm, usually beating UCB1 in real-world '
                                     'benchmarks.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'UCB1 uses the rule: pick the arm with the highest value of mu_hat_i + sqrt(2 * '
                                     "ln(t) / n_i). The second term is an exploration bonus from Hoeffding's "
                                     'inequality that shrinks as an arm is pulled more. Thompson Sampling maintains '
                                     'Beta distributions Beta(alpha, beta) for each arm. At each step, it samples a '
                                     'random value from each Beta distribution and chooses the highest one, updating '
                                     'alpha on success and beta on failure. Both minimize cumulative regret.',
                      'missing_concepts': ["UCB1 implements 'optimism in the face of uncertainty': chooses arm "
                                           'maximizing a_t = argmax_i [mu_hat_i + sqrt((2 * ln(t)) / n_i)], balancing '
                                           'empirical reward with exploration bonus']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'UCB1 picks the arm with the highest upper confidence bound so you explore '
                                     'uncertain options. Thompson Sampling samples from Beta distributions for each '
                                     'arm and picks the highest sample, updating alpha and beta when it wins or loses. '
                                     'Both are better than epsilon-greedy.',
                      'missing_concepts': ["Exploration bonus sqrt((2 * ln(t)) / n_i) derives from Hoeffding's "
                                           'Inequality, shrinking as arm i is pulled more often and expanding as total '
                                           'rounds t grow',
                                           'Bernoulli conjugate updating: pulls arm a_t; if reward r=1, updates '
                                           'alpha_{a_t} = alpha_{a_t} + 1; if r=0, updates beta_{a_t} = beta_{a_t} + '
                                           '1, achieving asymptotic optimal logarithmic regret']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'UCB1 is a USB-C hardware communication protocol, and Thompson Sampling is an '
                                     'audio noise reduction filter in audacity.',
                      'missing_concepts': ["UCB1 implements 'optimism in the face of uncertainty': chooses arm "
                                           'maximizing a_t = argmax_i [mu_hat_i + sqrt((2 * ln(t)) / n_i)], balancing '
                                           'empirical reward with exploration bonus',
                                           "Exploration bonus sqrt((2 * ln(t)) / n_i) derives from Hoeffding's "
                                           'Inequality, shrinking as arm i is pulled more often and expanding as total '
                                           'rounds t grow',
                                           'Thompson Sampling (posterior sampling) uses Bayesian probability matching: '
                                           'samples theta_i ~ Beta(alpha_i, beta_i) for each arm, choosing arm with '
                                           'highest sampled reward',
                                           'Bernoulli conjugate updating: pulls arm a_t; if reward r=1, updates '
                                           'alpha_{a_t} = alpha_{a_t} + 1; if r=0, updates beta_{a_t} = beta_{a_t} + '
                                           '1, achieving asymptotic optimal logarithmic regret']}]},
 {'topic_tag': 'Temporal Fusion Transformers for Forecasting',
  'question': 'Analyze the architecture of Temporal Fusion Transformers (TFT) regarding Variable Selection Networks, '
              'static covariate encoders, and multi-horizon quantile forecasting.',
  'keywords': ['Temporal Fusion Transformer (TFT)',
               'Multi-Horizon Forecasting',
               'Variable Selection Network (VSN)',
               'Static Covariates',
               'Quantile Loss',
               'Self-Attention',
               'Gated Residual Networks'],
  'expected_concepts': ['Heterogeneous inputs: gracefully ingests static metadata (store ID, location), past-observed '
                        'time-varying inputs (historical sales), and known future time-varying inputs (holidays, '
                        'day-of-week)',
                        'Variable Selection Networks (VSN) use Gated Residual Networks (GRN) and softmax gating to '
                        'dynamically select relevant features per time-step and filter out uninformative noise',
                        'Static Covariate Encoders condition sequential temporal processing (LSTM / multi-head '
                        'attention) on static context vectors',
                        'Multi-horizon quantile forecasting outputs prediction intervals (e.g., 10th, 50th, 90th '
                        'percentiles) via pinball/quantile loss to provide probabilistic uncertainty bounds'],
  'model_answer': 'Temporal Fusion Transformer (TFT) (Lim et al., Google 2021) is a state-of-the-art deep learning '
                  'architecture engineered specifically for multi-horizon interpretable time series forecasting. '
                  'Unlike standard NLP transformers, TFT natively handles heterogeneous inputs across three '
                  'categories: static metadata (e.g., brand, store location), past observed-only time-varying inputs '
                  '(e.g., foot traffic, historical sales), and known future time-varying inputs (e.g., promotional '
                  'calendars, holidays). Key architectural innovations include: 1) Variable Selection Networks (VSNs): '
                  'Employ Gated Residual Networks (GRNs) to compute instance-wise softmax feature importance weights, '
                  'filtering out noisy extraneous predictors dynamically at every time step; 2) Static Covariate '
                  'Encoders: Transform static entity features into context vectors that initialize LSTM recurrent '
                  'states and modulate temporal attention layers; 3) Temporal Self-Attention: A modified multi-head '
                  'self-attention layer captures long-range temporal dependencies while preserving causality via '
                  'temporal masking; and 4) Multi-Horizon Quantile Output: Rather than single point forecasts, TFT '
                  'outputs simultaneous quantile predictions (e.g., p10, p50, p90) trained via Quantile Loss (pinball '
                  'loss), delivering full probabilistic uncertainty intervals across future forecasting horizons.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'Temporal Fusion Transformer (TFT) was built by Google specifically for '
                                     'multi-horizon time series forecasting. What makes it special is how it handles '
                                     'different types of inputs: static metadata (like store location), past-observed '
                                     'dynamic inputs (like historical demand), and known future inputs (like planned '
                                     'marketing promos or holidays). First, it uses Variable Selection Networks (VSNs) '
                                     'backed by Gated Residual Networks to dynamically weight and select the most '
                                     'relevant features per time step, ignoring noise. Second, it uses Static '
                                     'Covariate Encoders to turn static metadata into context vectors that condition '
                                     'the temporal LSTM and attention layers. Third, it applies interpretable '
                                     'multi-head self-attention with causal masking to learn long-range seasonality. '
                                     'Finally, instead of outputting a single point estimate, TFT outputs '
                                     'multi-horizon quantile predictions—like the 10th, 50th, and 90th '
                                     'percentiles—using pinball loss, providing calibrated uncertainty intervals '
                                     'essential for supply chain planning.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'TFT is a transformer model for time series forecasting that handles static '
                                     'features, past observed features, and known future features like holidays. It '
                                     'uses Variable Selection Networks to dynamically pick important features at each '
                                     'time step. Static covariate encoders incorporate metadata into the temporal '
                                     'processing. Finally, it uses quantile loss to predict uncertainty intervals '
                                     'across future time horizons like the 10th, 50th, and 90th percentiles.',
                      'missing_concepts': []},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Temporal Fusion Transformer is an attention-based neural network for forecasting '
                                     'multiple time steps ahead. It handles static data and dynamic time series using '
                                     'variable selection networks. It predicts quantiles like 10%, 50%, and 90% so you '
                                     'get confidence intervals for sales forecasts.',
                      'missing_concepts': ['Heterogeneous inputs: gracefully ingests static metadata (store ID, '
                                           'location), past-observed time-varying inputs (historical sales), and known '
                                           'future time-varying inputs (holidays, day-of-week)',
                                           'Static Covariate Encoders condition sequential temporal processing (LSTM / '
                                           'multi-head attention) on static context vectors']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'Temporal Fusion Transformers are electrical transformer hardware components used '
                                     'to regulate voltage in cloud data centers.',
                      'missing_concepts': ['Heterogeneous inputs: gracefully ingests static metadata (store ID, '
                                           'location), past-observed time-varying inputs (historical sales), and known '
                                           'future time-varying inputs (holidays, day-of-week)',
                                           'Variable Selection Networks (VSN) use Gated Residual Networks (GRN) and '
                                           'softmax gating to dynamically select relevant features per time-step and '
                                           'filter out uninformative noise',
                                           'Static Covariate Encoders condition sequential temporal processing (LSTM / '
                                           'multi-head attention) on static context vectors',
                                           'Multi-horizon quantile forecasting outputs prediction intervals (e.g., '
                                           '10th, 50th, 90th percentiles) via pinball/quantile loss to provide '
                                           'probabilistic uncertainty bounds']}]},
 {'topic_tag': "Spatial Data Science & Moran's I",
  'question': "How does Moran's I measure spatial autocorrelation using spatial weights matrices (W), and what does "
              'spatial clustering versus dispersion indicate?',
  'keywords': ['Spatial Data Science',
               'Morans I',
               'Spatial Autocorrelation',
               'Spatial Weights Matrix (W)',
               "Tobler's First Law",
               'Spatial Lag',
               'LISA'],
  'expected_concepts': ["Tobler's First Law of Geography: 'everything is related to everything else, but near things "
                        "are more related than distant things' (spatial dependence)",
                        'Spatial weights matrix W: N x N matrix defining neighborhood spatial topology (queen '
                        'contiguity, rook contiguity, k-nearest neighbors, or inverse distance decay)',
                        "Global Moran's I formula: I = [N / sum_{i,j} w_ij] * [sum_{i,j} w_ij (x_i - x_bar)(x_j - "
                        'x_bar) / sum_i (x_i - x_bar)^2], calculating spatial covariance against total variance',
                        'Interpretation: I > 0 indicates positive spatial autocorrelation (spatial clustering of '
                        'similar high/low values); I < 0 indicates negative autocorrelation (spatial dispersion / '
                        'checkerboard pattern); I approx -1/(N-1) indicates complete spatial randomness'],
  'model_answer': 'Spatial autocorrelation violates standard independent and identically distributed (i.i.d.) '
                  "regression assumptions, embodying Waldo Tobler's First Law of Geography: 'Everything is related to "
                  "everything else, but near things are more related than distant things.' Global Moran's I is the "
                  'fundamental statistic quantifying spatial autocorrelation across a geographic lattice. The spatial '
                  'configuration is formalized via an N x N Spatial Weights Matrix W, where w_ij defines spatial '
                  'connectivity between regions i and j (e.g., Queen contiguity where boundaries share an edge/vertex, '
                  "or distance-decay functions w_ij = d_ij^{-alpha}), typically row-standardized. Global Moran's I is "
                  'formulated as: I = [N / S_0] * [sum_{i=1}^N sum_{j=1}^N w_ij * (x_i - x_bar) * (x_j - x_bar)] / '
                  "sum_{i=1}^N (x_i - x_bar)^2, where S_0 = sum_{i,j} w_ij. Moran's I is effectively the correlation "
                  'coefficient between an attribute x and its spatial lag W*x. Interpretation: I > -1/(N-1) indicates '
                  'positive spatial autocorrelation (clustering: hot-spots and cold-spots); I < -1/(N-1) indicates '
                  'negative spatial autocorrelation (spatial dispersion / checkerboard pattern); and I approx -1/(N-1) '
                  'confirms Complete Spatial Randomness (CSR).',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': "Moran's I evaluates Tobler's First Law of Geography: that nearby spatial "
                                     'locations tend to have similar values, violating i.i.d. assumptions. It starts '
                                     'with a spatial weights matrix W (size N x N), which defines geographic '
                                     'neighborhood relationships—such as Queen contiguity where polygons share a '
                                     "border or vertex, or inverse distance decay. Global Moran's I computes the "
                                     'spatial covariance between attribute values at location i and location j '
                                     "weighted by w_ij, divided by the total variance. In essence, it's the slope of "
                                     "the regression of the spatial lag (W*x) on x. A Moran's I significantly greater "
                                     'than the expected value (-1/(N-1)) proves positive spatial '
                                     'autocorrelation—meaning high values cluster near high values and low values near '
                                     "low values, forming spatial hotspots. A negative Moran's I indicates negative "
                                     'autocorrelation, where high values are surrounded by low values in a '
                                     "checkerboard pattern of spatial dispersion. Testing Moran's I is critical before "
                                     'running spatial lag or spatial error regression models.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': "Moran's I measures spatial autocorrelation based on Tobler's law that near "
                                     'things are more related. You define spatial relationships using a spatial '
                                     'weights matrix W, like Queen contiguity where neighboring polygons share '
                                     "borders. Moran's I calculates the correlation between a feature and its spatial "
                                     "lag. If Moran's I is positive, you have spatial clustering of high values near "
                                     'high values. If negative, you have spatial dispersion like a checkerboard. Near '
                                     'zero means complete spatial randomness.',
                      'missing_concepts': ["Global Moran's I formula: I = [N / sum_{i,j} w_ij] * [sum_{i,j} w_ij (x_i "
                                           '- x_bar)(x_j - x_bar) / sum_i (x_i - x_bar)^2], calculating spatial '
                                           'covariance against total variance']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': "Moran's I is used in GIS and spatial data science to see if geographic data is "
                                     'clustered. It uses a spatial weights matrix to define who is neighbors with who. '
                                     "Positive Moran's I means values are clustered together on a map, and negative "
                                     'means values are scattered.',
                      'missing_concepts': ["Tobler's First Law of Geography: 'everything is related to everything "
                                           "else, but near things are more related than distant things' (spatial "
                                           'dependence)',
                                           "Global Moran's I formula: I = [N / sum_{i,j} w_ij] * [sum_{i,j} w_ij (x_i "
                                           '- x_bar)(x_j - x_bar) / sum_i (x_i - x_bar)^2], calculating spatial '
                                           'covariance against total variance']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': "Moran's I is an astronomical coordinate calculation used to measure lunar "
                                     'distances from earth orbit.',
                      'missing_concepts': ["Tobler's First Law of Geography: 'everything is related to everything "
                                           "else, but near things are more related than distant things' (spatial "
                                           'dependence)',
                                           'Spatial weights matrix W: N x N matrix defining neighborhood spatial '
                                           'topology (queen contiguity, rook contiguity, k-nearest neighbors, or '
                                           'inverse distance decay)',
                                           "Global Moran's I formula: I = [N / sum_{i,j} w_ij] * [sum_{i,j} w_ij (x_i "
                                           '- x_bar)(x_j - x_bar) / sum_i (x_i - x_bar)^2], calculating spatial '
                                           'covariance against total variance',
                                           'Interpretation: I > 0 indicates positive spatial autocorrelation (spatial '
                                           'clustering of similar high/low values); I < 0 indicates negative '
                                           'autocorrelation (spatial dispersion / checkerboard pattern); I approx '
                                           '-1/(N-1) indicates complete spatial randomness']}]},
 {'topic_tag': 'Automated Schema Drift & Great Expectations',
  'question': 'How does the Great Expectations framework profile data batches, enforce declarative assertions, and '
              'prevent silent upstream schema drift in production data pipelines?',
  'keywords': ['Great Expectations',
               'Data Quality',
               'Schema Drift',
               'Declarative Assertions',
               'Expectation Suite',
               'Data Contracts',
               'Automated Profiling'],
  'expected_concepts': ['Silent data corruption: upstream schema drift (renamed columns, unexpected null spikes, type '
                        'mismatches, range violations) cascades into downstream ML pipelines without throwing database '
                        'errors',
                        'Expectations are declarative, human-readable assertions expressed as JSON tests (e.g., '
                        'expect_column_values_to_not_be_null, expect_column_values_to_be_between)',
                        'Automated Profiling: scans existing baseline datasets to automatically generate candidate '
                        'Expectation Suites and data documentation (Data Docs)',
                        'Checkpoint execution: validates incoming data batches at pipeline boundaries '
                        '(Airflow/Dagster), failing runs or generating automated alerts before poisoned data enters '
                        'data warehouses'],
  'model_answer': "In production data engineering and MLOps, 'silent data corruption' is the most insidious pipeline "
                  'risk: upstream API modifications, database migrations, or third-party schema drift (e.g., null rate '
                  'surging from 1% to 40%, currency units switching from dollars to cents, or categorical value drift) '
                  'rarely trigger SQL execution errors, allowing corrupted data to quietly poison feature stores and '
                  "degrade deployed models. Great Expectations addresses this by operationalizing declarative 'Data "
                  "Contracts'. Data quality assertions—called Expectations—are declarative, parameterized tests (e.g., "
                  'expect_column_values_to_not_be_null, expect_column_quantile_values_to_be_between, '
                  'expect_table_columns_to_match_ordered_list). The framework provides an automated Profiler that '
                  'scans baseline batches to auto-generate candidate Expectation Suites and render human-readable HTML '
                  "'Data Docs'. In production, orchestrators (Airflow, Prefect, Dagster) trigger Great Expectations "
                  'Checkpoints at ingest boundaries: if incoming batches fail validation, the pipeline halts '
                  'immediately, quarantine logic triggers, and alerts route to Slack/PagerDuty before silent drift '
                  'corrupts production tables.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'Silent schema drift is a nightmare in machine learning pipelines: an upstream '
                                     'team renames a column or an API suddenly starts sending nulls, but because SQL '
                                     "doesn't crash, the corrupted data enters your feature store and silently tanks "
                                     'model accuracy. Great Expectations solves this by acting as a declarative '
                                     'unit-testing framework for datasets. You define data contracts called '
                                     'Expectations—such as expect_column_values_to_not_be_null or '
                                     'expect_column_values_to_be_in_set. It has an automated profiler that inspects '
                                     'clean historical batches and auto-generates an Expectation Suite and visual Data '
                                     'Docs. In production, you run Great Expectations Checkpoints inside your Airflow '
                                     'DAG at the ingestion boundary: if an incoming batch violates any expectation, '
                                     'the checkpoint fails the pipeline immediately and sends an alert before that '
                                     'poisoned data ever touches your data warehouse or training tables.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'Great Expectations prevents silent schema drift where unexpected nulls or data '
                                     'type changes corrupt downstream models without throwing errors. It uses '
                                     'declarative assertions called Expectations to test data quality, like checking '
                                     'value ranges or schema columns. You can use its profiler to automatically '
                                     'generate expectation suites from existing data. In production pipelines using '
                                     'Airflow, Checkpoints validate incoming batches and block corrupted data from '
                                     'loading into the warehouse.',
                      'missing_concepts': ['Automated Profiling: scans existing baseline datasets to automatically '
                                           'generate candidate Expectation Suites and data documentation (Data Docs)']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Great Expectations is a Python library for data testing. You write expectations '
                                     'like checking if columns have nulls or if numbers are between min and max. You '
                                     'run it in Airflow pipelines to stop bad data from getting into your database '
                                     'when upstream schemas change.',
                      'missing_concepts': ['Silent data corruption: upstream schema drift (renamed columns, unexpected '
                                           'null spikes, type mismatches, range violations) cascades into downstream '
                                           'ML pipelines without throwing database errors',
                                           'Automated Profiling: scans existing baseline datasets to automatically '
                                           'generate candidate Expectation Suites and data documentation (Data Docs)']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'Great Expectations is a Charles Dickens novel and has no relationship to '
                                     'computer software.',
                      'missing_concepts': ['Silent data corruption: upstream schema drift (renamed columns, unexpected '
                                           'null spikes, type mismatches, range violations) cascades into downstream '
                                           'ML pipelines without throwing database errors',
                                           'Expectations are declarative, human-readable assertions expressed as JSON '
                                           'tests (e.g., expect_column_values_to_not_be_null, '
                                           'expect_column_values_to_be_between)',
                                           'Automated Profiling: scans existing baseline datasets to automatically '
                                           'generate candidate Expectation Suites and data documentation (Data Docs)',
                                           'Checkpoint execution: validates incoming data batches at pipeline '
                                           'boundaries (Airflow/Dagster), failing runs or generating automated alerts '
                                           'before poisoned data enters data warehouses']}]},
 {'topic_tag': 'Causal Directed Acyclic Graphs (DAGs)',
  'question': 'Explain how d-separation rules in causal DAGs identify confounding paths versus collider stratification '
              'bias.',
  'keywords': ['Causal DAGs',
               'Judea Pearl',
               'd-separation',
               'Collider Bias',
               'Backdoor Criterion',
               'Confounding Path',
               "Berkson's Paradox"],
  'expected_concepts': ['Causal Directed Acyclic Graphs (DAGs) represent causal assumptions where nodes are random '
                        'variables and directed arrows represent direct causal mechanisms',
                        'Confounding (fork path X <- Z -> Y): common cause Z creates an open backdoor path inducing '
                        'spurious correlation; conditioning on Z blocks the path and eliminates confounding bias',
                        'Collider (inverted fork X -> C <- Y): variable C is causally influenced by both X and Y; path '
                        'is naturally blocked / d-separated when unconditioned',
                        "Collider stratification bias (Berkson's Paradox): conditioning on or controlling for a "
                        'collider (or its descendant) opens a previously blocked path, artificially creating spurious '
                        'correlation between independent causes'],
  'model_answer': "Judea Pearl's Causal Graphical Models (do-calculus) formalize causal identification using Directed "
                  'Acyclic Graphs (DAGs), where directed edges denote direct causal mechanisms. The d-separation '
                  '(directional separation) criterion determines whether two variables X and Y are conditionally '
                  'independent given a conditioning set Z by evaluating three path junctions: 1) Chain (X -> M -> Y) '
                  "and Fork (X <- Z -> Y): In a fork, Z is a common confounder that opens an unblocked 'backdoor "
                  "path', inducing spurious correlation. Conditioning on Z blocks the path, satisfying the Backdoor "
                  'Criterion and eliminating confounding bias; 2) Collider (X -> C <- Y): A collider is a node '
                  'receiving two incoming directed arrows from X and Y. Crucially, a path containing an unconditioned '
                  'collider is naturally blocked (d-separated), meaning X and Y are marginally independent. However, '
                  'conditioning on or controlling for a collider (or its descendant) unblocks the path. This induces '
                  "Collider Stratification Bias (Berkson's Fallacy), creating artificial, spurious association between "
                  "two independent causes. Therefore, blindly 'controlling for all available variables' in regressions "
                  'can introduce severe bias rather than eliminating it.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': "Judea Pearl's causal DAGs map out causal structures to determine which variables "
                                     'to control for and which variables to never touch. D-separation governs whether '
                                     'paths are open or blocked. In a fork path—X <- Z -> Y—Z is a common confounder '
                                     'causing an open backdoor path that creates spurious correlation. Conditioning on '
                                     'Z blocks this path, which is what eliminates confounding bias. But a collider '
                                     'path is the complete opposite: X -> C <- Y, where both X and Y point into node '
                                     'C. A collider naturally blocks the path, so X and Y are independent. If you make '
                                     'the rookie mistake of controlling for or conditioning on the collider C (or a '
                                     'descendant of C), you accidentally open that path! This induces Collider '
                                     "Stratification Bias, or Berkson's Paradox, artificially creating a fake "
                                     'correlation between two independent variables. This proves why throwing every '
                                     'variable into a regression model is dangerous—controlling for colliders destroys '
                                     'causal validity.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'In a causal DAG, a fork path X <- Z -> Y represents a confounder Z that creates '
                                     'an open backdoor path, and you must condition on Z to block it and remove '
                                     'confounding. A collider X -> C <- Y has arrows pointing into C from both sides. '
                                     'A collider naturally blocks the path when left alone. But if you condition on '
                                     'the collider C, you open the path and create collider stratification bias, '
                                     'creating a spurious correlation between independent variables.',
                      'missing_concepts': ["Collider stratification bias (Berkson's Paradox): conditioning on or "
                                           'controlling for a collider (or its descendant) opens a previously blocked '
                                           'path, artificially creating spurious correlation between independent '
                                           'causes']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Causal DAGs use d-separation to see if variables are independent. In a fork, Z '
                                     'is a confounder and you control for it to stop bias. In a collider, two arrows '
                                     'point into the same node. If you control for a collider you create collider '
                                     "bias, which makes independent variables look correlated. That's why you "
                                     "shouldn't control for every variable in regression.",
                      'missing_concepts': ['Causal Directed Acyclic Graphs (DAGs) represent causal assumptions where '
                                           'nodes are random variables and directed arrows represent direct causal '
                                           'mechanisms',
                                           "Collider stratification bias (Berkson's Paradox): conditioning on or "
                                           'controlling for a collider (or its descendant) opens a previously blocked '
                                           'path, artificially creating spurious correlation between independent '
                                           'causes']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'A causal DAG is a blockchain hash tree used in cryptocurrency mining rigs.',
                      'missing_concepts': ['Causal Directed Acyclic Graphs (DAGs) represent causal assumptions where '
                                           'nodes are random variables and directed arrows represent direct causal '
                                           'mechanisms',
                                           'Confounding (fork path X <- Z -> Y): common cause Z creates an open '
                                           'backdoor path inducing spurious correlation; conditioning on Z blocks the '
                                           'path and eliminates confounding bias',
                                           'Collider (inverted fork X -> C <- Y): variable C is causally influenced by '
                                           'both X and Y; path is naturally blocked / d-separated when unconditioned',
                                           "Collider stratification bias (Berkson's Paradox): conditioning on or "
                                           'controlling for a collider (or its descendant) opens a previously blocked '
                                           'path, artificially creating spurious correlation between independent '
                                           'causes']}]}]

