# Data Science Easy Questions (25 questions)

QUESTIONS = [{'topic_tag': 'Data Science CRISP-DM Workflow',
  'question': 'What are the six phases of the CRISP-DM data science project lifecycle and how do they interconnect?',
  'keywords': ['CRISP-DM',
               'Business Understanding',
               'Data Understanding',
               'Data Preparation',
               'Modeling',
               'Evaluation',
               'Deployment'],
  'expected_concepts': ['CRISP-DM encompasses six phases: Business Understanding, Data Understanding, Data '
                        'Preparation, Modeling, Evaluation, and Deployment',
                        'The process is iterative and non-linear, with frequent feedback loops (e.g., Evaluation loop '
                        'back to Business Understanding)',
                        'Data Preparation typically consumes the majority of project effort and informs modeling '
                        'feasibility',
                        'Deployment bridges technical model outputs into operational business decisions or production '
                        'systems'],
  'model_answer': 'CRISP-DM defines a six-phase iterative lifecycle: Business Understanding, Data Understanding, Data '
                  'Preparation, Modeling, Evaluation, and Deployment. The cycle begins by translating business '
                  'objectives into a data science problem. Data Understanding involves initial data collection, '
                  'exploration, and identifying quality issues. Data Preparation transforms raw data through cleaning, '
                  'feature engineering, and normalization, which feeds into Modeling where algorithms are trained and '
                  'tuned. Evaluation assesses model results strictly against the original business objectives, often '
                  'revealing gaps that require looping back to Business Understanding before proceeding to Deployment, '
                  'where models are integrated into operational workflows for business value.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 96,
                      'answer_text': 'CRISP-DM breaks a data science project down into six core stages: Business '
                                     'Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, and '
                                     "Deployment. What makes it practical is that it's inherently cyclical rather than "
                                     'a rigid waterfall. You start with defining the business problem, explore the raw '
                                     'data, and spend a significant portion of time in data prep and feature '
                                     "engineering. When you train your models and evaluate them, you don't just look "
                                     'at accuracy—you check whether it solves the business goal. If evaluation fails '
                                     'or reveals flaws, you often iterate right back to business understanding or data '
                                     'prep before ever deploying.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'CRISP-DM has six main phases: business understanding, data understanding, data '
                                     'prep, modeling, evaluation, and deployment. You begin by understanding what the '
                                     'stakeholder needs, gather and inspect the data, clean it, train machine learning '
                                     'models, and evaluate performance. If the metrics look solid, you deploy it into '
                                     "production. It's iterative, so you often jump between data preparation and "
                                     'modeling as you discover new features.',
                      'missing_concepts': ['The process is iterative and non-linear, with frequent feedback loops '
                                           '(e.g., Evaluation loop back to Business Understanding)']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'CRISP-DM is a methodology for data mining projects. It has several steps like '
                                     'getting the business requirements, exploring the data, preparing the dataset, '
                                     'and running machine learning models. Then you evaluate how accurate the model is '
                                     'and put it into production. Most of the time is spent on data cleaning before '
                                     'running the algorithms.',
                      'missing_concepts': ['The process is iterative and non-linear, with frequent feedback loops '
                                           '(e.g., Evaluation loop back to Business Understanding)',
                                           'Deployment bridges technical model outputs into operational business '
                                           'decisions or production systems']},
                     {'quality_level': 'poor',
                      'human_score': 28,
                      'answer_text': "CRISP-DM is an agile software development sprint framework used in Scrum. It's "
                                     'about writing code in two-week sprints, deploying microservices to Docker '
                                     'containers, and managing CI/CD pipelines for data engineering teams.',
                      'missing_concepts': ['CRISP-DM encompasses six phases: Business Understanding, Data '
                                           'Understanding, Data Preparation, Modeling, Evaluation, and Deployment',
                                           'The process is iterative and non-linear, with frequent feedback loops '
                                           '(e.g., Evaluation loop back to Business Understanding)',
                                           'Data Preparation typically consumes the majority of project effort and '
                                           'informs modeling feasibility',
                                           'Deployment bridges technical model outputs into operational business '
                                           'decisions or production systems']}]},
 {'topic_tag': 'Mean vs Median vs Mode',
  'question': 'How do Mean, Median, and Mode behave when calculated on positively skewed, negatively skewed, and '
              'symmetric data distributions?',
  'keywords': ['Mean', 'Median', 'Mode', 'Positive Skew', 'Negative Skew', 'Symmetric Distribution', 'Outliers'],
  'expected_concepts': ['In a symmetric distribution (e.g., normal), Mean, Median, and Mode coincide at the center',
                        'In right/positive skew, extreme high outliers pull the Mean rightward: Mode < Median < Mean',
                        'In left/negative skew, extreme low values pull the Mean leftward: Mean < Median < Mode',
                        'Median is robust and resistant to extreme outliers, whereas Mean is sensitive to extreme '
                        'values'],
  'model_answer': 'In a perfectly symmetric, unimodal distribution, the Mean, Median, and Mode are identical and sit '
                  'at the center. When a distribution is positively skewed (skewed to the right), a long tail of large '
                  'values pulls the arithmetic Mean to the right, yielding the typical ordering: Mode < Median < Mean. '
                  'Conversely, in a negatively skewed distribution (skewed to the left), an extreme left tail pulls '
                  'the Mean downward, resulting in: Mean < Median < Mode. The Median remains resistant and robust '
                  'against outliers because it depends on positional rank rather than magnitude, making it the '
                  'preferred measure of central tendency for skewed datasets like income or housing prices.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'In a symmetric distribution like a standard bell curve, the mean, median, and '
                                     'mode are all equal and sit right in the middle. When data is positively '
                                     "skewed—meaning there's a long right tail of extreme values—the mean gets dragged "
                                     'toward the tail, so you get Mode < Median < Mean. In negatively skewed data with '
                                     'a long left tail, the opposite happens: Mean < Median < Mode. The reason the '
                                     "median stays in between is that it's non-parametric and resistant to outliers, "
                                     'depending on rank rather than actual values.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 83,
                      'answer_text': 'When data is symmetrical, mean, median, and mode are identical. In positively '
                                     'skewed distributions, extreme large numbers pull the mean up, so the mean is '
                                     'greater than the median, which is greater than the mode. In negatively skewed '
                                     'distributions, small extreme values drag the mean down below the median. Median '
                                     'is generally safer to report than mean when you have outliers.',
                      'missing_concepts': ['In left/negative skew, extreme low values pull the Mean leftward: Mean < '
                                           'Median < Mode']},
                     {'quality_level': 'average',
                      'human_score': 64,
                      'answer_text': 'Mean is the average, median is the middle number, and mode is the most frequent '
                                     "value. In normal data they're about the same. In skewed data, the mean shifts "
                                     "towards the outliers, so if you have high values the mean gets bigger. That's "
                                     'why people use median instead of mean for salaries.',
                      'missing_concepts': ['In right/positive skew, extreme high outliers pull the Mean rightward: '
                                           'Mode < Median < Mean',
                                           'In left/negative skew, extreme low values pull the Mean leftward: Mean < '
                                           'Median < Mode']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'Mean, median, and mode are always equal regardless of the shape of the data '
                                     'because they all calculate the center point. If a dataset is skewed, you just '
                                     'square the numbers to make the mean equal the mode again.',
                      'missing_concepts': ['In a symmetric distribution (e.g., normal), Mean, Median, and Mode '
                                           'coincide at the center',
                                           'In right/positive skew, extreme high outliers pull the Mean rightward: '
                                           'Mode < Median < Mean',
                                           'In left/negative skew, extreme low values pull the Mean leftward: Mean < '
                                           'Median < Mode',
                                           'Median is robust and resistant to extreme outliers, whereas Mean is '
                                           'sensitive to extreme values']}]},
 {'topic_tag': 'Standard Deviation vs Variance',
  'question': 'What is the relationship between Standard Deviation and Variance, and why do data scientists often '
              'prefer reporting Standard Deviation?',
  'keywords': ['Standard Deviation',
               'Variance',
               'Squared Units',
               'Interpretable Units',
               'Degrees of Freedom',
               'Dispersion'],
  'expected_concepts': ['Variance is the average of squared deviations from the mean; Standard Deviation is the '
                        'positive square root of Variance',
                        'Variance is expressed in squared units of the original measurement (e.g., dollars squared, '
                        'meters squared), making it non-intuitive to interpret directly',
                        'Standard Deviation returns dispersion back to the original units of the data, allowing direct '
                        'comparison with the mean',
                        'Both metrics quantify statistical dispersion and spread around the central mean'],
  'model_answer': 'Variance measures the average squared deviation of each data point from the mean, calculated as the '
                  'sum of squared differences divided by N (or N-1 for sample variance). Standard deviation is simply '
                  'the square root of the variance. While variance is mathematically convenient for theoretical '
                  'derivations, analysis of variance (ANOVA), and regression math, its unit of measurement is squared '
                  '(such as squared dollars or squared kilograms). Data scientists prefer reporting standard deviation '
                  'because taking the square root restores the metric to the original unit of measurement, enabling '
                  'direct contextual interpretation alongside the mean (e.g., mean salary $70k +/- std dev $15k).',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 96,
                      'answer_text': 'Variance is the average of the squared distances of each data point from the '
                                     'mean, while standard deviation is simply the square root of that variance. The '
                                     'primary reason we prefer reporting standard deviation in practice is unit '
                                     'interpretability. If you are measuring house prices in dollars, the variance is '
                                     "in dollars squared, which doesn't mean much to stakeholders. Taking the square "
                                     'root gives you standard deviation back in actual dollars, allowing you to say '
                                     'the average price is $400,000 with a standard deviation of $50,000.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'Standard deviation is the square root of variance. Both measure the spread of '
                                     'data around the mean. We prefer standard deviation because variance is expressed '
                                     'in squared units, which is hard to explain in real life. Standard deviation is '
                                     "in the same units as the original data, so it's much easier to interpret "
                                     'alongside the mean.',
                      'missing_concepts': ['Variance is expressed in squared units of the original measurement (e.g., '
                                           'dollars squared, meters squared), making it non-intuitive to interpret '
                                           'directly']},
                     {'quality_level': 'average',
                      'human_score': 63,
                      'answer_text': 'Variance and standard deviation both tell you how spread out your data is. '
                                     'Variance squares all the differences from the mean, and standard deviation is '
                                     'the root of that. People report standard deviation more often because the '
                                     'numbers are smaller and easier to read than variance.',
                      'missing_concepts': ['Variance is expressed in squared units of the original measurement (e.g., '
                                           'dollars squared, meters squared), making it non-intuitive to interpret '
                                           'directly',
                                           'Standard Deviation returns dispersion back to the original units of the '
                                           'data, allowing direct comparison with the mean']},
                     {'quality_level': 'poor',
                      'human_score': 30,
                      'answer_text': 'Standard deviation measures the accuracy of your machine learning model, while '
                                     'variance tells you how many variables are in your dataset. You prefer standard '
                                     'deviation because it tells you if the model is overfitted or underfitted.',
                      'missing_concepts': ['Variance is the average of squared deviations from the mean; Standard '
                                           'Deviation is the positive square root of Variance',
                                           'Variance is expressed in squared units of the original measurement (e.g., '
                                           'dollars squared, meters squared), making it non-intuitive to interpret '
                                           'directly',
                                           'Standard Deviation returns dispersion back to the original units of the '
                                           'data, allowing direct comparison with the mean',
                                           'Both metrics quantify statistical dispersion and spread around the central '
                                           'mean']}]},
 {'topic_tag': 'SQL SELECT Clause Execution Order',
  'question': 'What is the logical execution order of SQL query clauses (FROM, WHERE, GROUP BY, HAVING, SELECT, ORDER '
              'BY, LIMIT) versus lexical written order?',
  'keywords': ['SQL Execution Order', 'FROM/JOIN', 'WHERE', 'GROUP BY', 'HAVING', 'SELECT', 'ORDER BY', 'LIMIT'],
  'expected_concepts': ['Logical order is: FROM/JOIN -> WHERE -> GROUP BY -> HAVING -> SELECT (with aliases) -> ORDER '
                        'BY -> LIMIT/OFFSET',
                        'Lexical (written) order begins with SELECT, but the database engine processes table '
                        'references and filters first',
                        'Column aliases created in SELECT cannot be referenced in WHERE because WHERE evaluates before '
                        'SELECT',
                        'HAVING filters aggregated groups after GROUP BY, whereas WHERE filters individual rows before '
                        'grouping'],
  'model_answer': 'Although a SQL query is written starting with SELECT, the database engine executes clauses in a '
                  'strict logical order: 1) FROM and JOIN to identify and combine target tables; 2) WHERE to filter '
                  'individual rows; 3) GROUP BY to aggregate rows into groups; 4) HAVING to filter aggregated groups; '
                  '5) SELECT to compute expressions and assign column aliases; 6) DISTINCT to eliminate duplicate '
                  'rows; 7) ORDER BY to sort results; and 8) LIMIT or OFFSET to restrict output count. This order '
                  'explains why column aliases defined in SELECT cannot be used in WHERE or GROUP BY clauses in '
                  'standard SQL—the SELECT step has not yet evaluated when row-filtering occurs.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'Even though we write SELECT first, the SQL engine executes: FROM and JOINs '
                                     'first, then WHERE to filter raw rows, then GROUP BY to create groups, then '
                                     'HAVING to filter those groups, then SELECT to project columns and assign '
                                     'aliases, then ORDER BY, and finally LIMIT. This sequence is why you cannot use a '
                                     'SELECT column alias inside a WHERE clause—the WHERE filter executes long before '
                                     'SELECT creates that alias. It also explains why HAVING requires aggregate '
                                     'functions while WHERE works on row-level data.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 82,
                      'answer_text': 'The execution order is FROM and JOIN first, then WHERE, GROUP BY, HAVING, '
                                     'SELECT, and finally ORDER BY and LIMIT. Because WHERE runs before SELECT, you '
                                     "can't use aliases created in SELECT inside WHERE. HAVING runs after GROUP BY to "
                                     'filter grouped results.',
                      'missing_concepts': ['Column aliases created in SELECT cannot be referenced in WHERE because '
                                           'WHERE evaluates before SELECT']},
                     {'quality_level': 'average',
                      'human_score': 60,
                      'answer_text': "The database doesn't run SQL in the order you write it. It starts with FROM to "
                                     'find the table, then filters with WHERE, then groups the data with GROUP BY, and '
                                     "then picks the columns in SELECT. Order by and limit happen at the end. That's "
                                     "why you can't filter aliases sometimes.",
                      'missing_concepts': ['HAVING filters aggregated groups after GROUP BY, whereas WHERE filters '
                                           'individual rows before grouping',
                                           'Column aliases created in SELECT cannot be referenced in WHERE because '
                                           'WHERE evaluates before SELECT']},
                     {'quality_level': 'poor',
                      'human_score': 26,
                      'answer_text': 'SQL executes exactly in the order you write it: SELECT first pulls all columns '
                                     'into memory, then FROM chooses the table, and then WHERE and ORDER BY filter the '
                                     'list in memory. If you put LIMIT first it runs faster.',
                      'missing_concepts': ['Logical order is: FROM/JOIN -> WHERE -> GROUP BY -> HAVING -> SELECT (with '
                                           'aliases) -> ORDER BY -> LIMIT/OFFSET',
                                           'Lexical (written) order begins with SELECT, but the database engine '
                                           'processes table references and filters first',
                                           'Column aliases created in SELECT cannot be referenced in WHERE because '
                                           'WHERE evaluates before SELECT',
                                           'HAVING filters aggregated groups after GROUP BY, whereas WHERE filters '
                                           'individual rows before grouping']}]},
 {'topic_tag': 'SQL JOIN Types Explained',
  'question': 'Explain the difference in output rows produced by INNER JOIN, LEFT OUTER JOIN, RIGHT OUTER JOIN, and '
              'FULL OUTER JOIN.',
  'keywords': ['INNER JOIN', 'LEFT JOIN', 'RIGHT JOIN', 'FULL OUTER JOIN', 'NULL Matching', 'Cartesian Product'],
  'expected_concepts': ['INNER JOIN returns only rows that satisfy the join condition in both tables',
                        'LEFT JOIN returns all rows from the left table, with matching right table rows or NULL where '
                        'no match exists',
                        'RIGHT JOIN returns all rows from the right table, with left matches or NULLs',
                        'FULL OUTER JOIN combines left and right joins, returning all rows from both tables and '
                        'filling non-matches with NULLs'],
  'model_answer': 'SQL joins combine tables based on matching predicate keys. INNER JOIN returns only records where '
                  'matching keys exist in both tables, omitting unmatched rows from either side. LEFT JOIN (or LEFT '
                  'OUTER JOIN) returns every row from the left table; when a match exists in the right table, '
                  'right-side columns are populated, and when no match exists, NULL values fill the right columns. '
                  'RIGHT JOIN does the symmetric reverse, preserving all right table rows. FULL OUTER JOIN preserves '
                  'all rows from both tables, filling with NULL values on either side whenever a corresponding match '
                  'is absent.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 95,
                      'answer_text': 'INNER JOIN returns only the intersection where the join condition matches in '
                                     'both tables—unmatched rows are dropped. LEFT JOIN keeps all rows from the left '
                                     'table, matching rows from the right table where possible and inserting NULLs for '
                                     'right table columns when there is no match. RIGHT JOIN is the exact mirror of '
                                     'LEFT JOIN, keeping all rows from the right table. FULL OUTER JOIN keeps all '
                                     'records from both tables, pairing them where keys match and padding with NULLs '
                                     'on either side where no match exists.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 83,
                      'answer_text': 'INNER JOIN only gives you records that match in both tables. LEFT JOIN gives all '
                                     'records from the left table plus matching rows from the right table, putting '
                                     'NULL if there is no match. FULL OUTER JOIN gives everything from both tables, '
                                     "with NULLs wherever a key doesn't match up. RIGHT JOIN is just like left join "
                                     'but keeps all rows from the right table.',
                      'missing_concepts': ['RIGHT JOIN returns all rows from the right table, with left matches or '
                                           'NULLs']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'INNER JOIN joins two tables where IDs match. LEFT JOIN keeps everything from the '
                                     'first table and adds the second table data if it finds it. FULL JOIN combines '
                                     'all rows from both tables. If something is missing it puts blank or null values.',
                      'missing_concepts': ['RIGHT JOIN returns all rows from the right table, with left matches or '
                                           'NULLs',
                                           'FULL OUTER JOIN combines left and right joins, returning all rows from '
                                           'both tables and filling non-matches with NULLs']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'INNER JOIN is when you join tables inside the same database, and OUTER JOIN is '
                                     'when you connect to an external API or remote server. LEFT and RIGHT refer to '
                                     'whether the table is stored in local memory or on SSD.',
                      'missing_concepts': ['INNER JOIN returns only rows that satisfy the join condition in both '
                                           'tables',
                                           'LEFT JOIN returns all rows from the left table, with matching right table '
                                           'rows or NULL where no match exists',
                                           'RIGHT JOIN returns all rows from the right table, with left matches or '
                                           'NULLs',
                                           'FULL OUTER JOIN combines left and right joins, returning all rows from '
                                           'both tables and filling non-matches with NULLs']}]},
 {'topic_tag': 'Handling Missing Data Strategies',
  'question': 'Compare Mean/Median Imputation against row deletion when dealing with MCAR, MAR, and MNAR data.',
  'keywords': ['Missing Data', 'Imputation', 'MCAR', 'MAR', 'MNAR', 'Listwise Deletion', 'Bias'],
  'expected_concepts': ['Missingness mechanisms dictate validity: MCAR (completely at random), MAR (at random '
                        'conditional on observed data), MNAR (not at random / dependent on unobserved missing value)',
                        'Row deletion (listwise deletion) discards samples, reducing statistical power and introducing '
                        'severe selection bias if data is not MCAR',
                        'Mean/median imputation preserves sample size but artificially shrinks variance and distorts '
                        'covariance structures',
                        'MNAR requires specialized modeling (e.g., Heckman selection or pattern-mixture models) rather '
                        'than naive imputation'],
  'model_answer': 'Handling missing data depends fundamentally on the missingness mechanism: Missing Completely at '
                  'Random (MCAR), Missing at Random (MAR), or Missing Not at Random (MNAR). Listwise deletion removes '
                  'rows with missing values; while unbiased under MCAR, it discards valuable statistical power and '
                  'introduces severe selection bias under MAR or MNAR. Mean or median imputation replaces missing '
                  'values with univariate statistics, preserving sample size; however, it artificially attenuates '
                  'variance, distorts correlations between features, and understates standard errors. In practice, '
                  'modern techniques like MICE (Multiple Imputation by Chained Equations) or k-NN imputation are '
                  'preferred for MAR, whereas MNAR requires domain-specific modeling or indicator variables to capture '
                  'informative missingness.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'Your choice depends on the underlying mechanism—whether the data is MCAR, MAR, '
                                     'or MNAR. Listwise deletion is only unbiased if the data is strictly MCAR, but '
                                     'you sacrifice sample size and power, and under MAR or MNAR it causes severe '
                                     'bias. Mean or median imputation keeps your row count intact, but it introduces '
                                     'an artificial spike at the center, artificially shrinking variance and weakening '
                                     'correlations between variables. If missingness is informative (MNAR), neither '
                                     'deletion nor simple imputation works well; you typically need to model the '
                                     'missingness mechanism directly or include missingness indicator flags.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': "Dropping rows is simple, but if data isn't missing completely at random, you "
                                     'introduce huge bias and lose data points. Mean or median imputation fixes the '
                                     'missing rows without shrinking your dataset, but it reduces the variance of the '
                                     'feature because you are stuffing the average value into every blank cell. For '
                                     'skewed features, median is safer than mean.',
                      'missing_concepts': ['MNAR requires specialized modeling (e.g., Heckman selection or '
                                           'pattern-mixture models) rather than naive imputation']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'When you have missing data, you can either delete the row with dropna() or fill '
                                     "it in with the mean or median using fillna(). Deleting rows is bad if you don't "
                                     'have much data. Filling with median is better than mean because mean gets '
                                     'affected by outliers, but it can still mess up your distribution if there are '
                                     'too many nulls.',
                      'missing_concepts': ['Missingness mechanisms dictate validity: MCAR (completely at random), MAR '
                                           '(at random conditional on observed data), MNAR (not at random / dependent '
                                           'on unobserved missing value)',
                                           'MNAR requires specialized modeling (e.g., Heckman selection or '
                                           'pattern-mixture models) rather than naive imputation']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'Missing data is caused by bad SQL queries. You should always impute missing '
                                     'values with zero or delete all columns that have null values so your machine '
                                     "learning model doesn't throw a syntax error during compilation.",
                      'missing_concepts': ['Missingness mechanisms dictate validity: MCAR (completely at random), MAR '
                                           '(at random conditional on observed data), MNAR (not at random / dependent '
                                           'on unobserved missing value)',
                                           'Row deletion (listwise deletion) discards samples, reducing statistical '
                                           'power and introducing severe selection bias if data is not MCAR',
                                           'Mean/median imputation preserves sample size but artificially shrinks '
                                           'variance and distorts covariance structures',
                                           'MNAR requires specialized modeling (e.g., Heckman selection or '
                                           'pattern-mixture models) rather than naive imputation']}]},
 {'topic_tag': 'Exploratory Data Analysis Objectives',
  'question': 'What are the primary goals of conducting Exploratory Data Analysis (EDA) on a new tabular dataset?',
  'keywords': ['EDA',
               'Data Distributions',
               'Outlier Identification',
               'Missing Value Profiling',
               'Feature Correlation',
               'Hypothesis Generation'],
  'expected_concepts': ['EDA uncovers underlying distributions, central tendencies, and spread of individual features',
                        'Profiles data hygiene: identifies missing value patterns, duplicates, data type mismatches, '
                        'and anomalies/outliers',
                        'Discovers pairwise relationships, collinearity, and interactions between predictors and the '
                        'target variable',
                        'Generates domain hypotheses and guides downstream feature engineering, transformations, and '
                        'model selection'],
  'model_answer': 'Exploratory Data Analysis (EDA), pioneered by John Tukey, serves four primary objectives before '
                  'model development: 1) Understanding data structure and hygiene—verifying data types, quantifying '
                  'missingness patterns, and uncovering anomalous records or entry errors; 2) Analyzing univariate '
                  'distributions—assessing skewness, kurtosis, variance, and identifying extreme outliers; 3) '
                  'Uncovering bivariate and multivariate relationships—computing correlation matrices, scatter plots, '
                  'and contingency tables to identify potential collinearity or non-linear associations with the '
                  'target variable; and 4) Informing data preprocessing and modeling strategy—deciding appropriate '
                  'transformations (e.g., log transforms, scaling), feature engineering opportunities, and algorithm '
                  'choice based on data geometry.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 96,
                      'answer_text': 'EDA is all about getting intimate with your data before touching an algorithm. '
                                     'First, you assess data health—missing value mechanisms, duplicates, cardinality, '
                                     'and unexpected data types. Second, you examine univariate distributions to see '
                                     'skewness, spreads, and outliers that might require log transforms or clipping. '
                                     'Third, you explore multivariate relationships through correlation matrices and '
                                     'scatter plots to detect multicollinearity and strong predictor signals for the '
                                     'target. Ultimately, EDA guides your feature engineering, transformations, and '
                                     'baseline model architecture.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 83,
                      'answer_text': 'The main goals of EDA are to inspect data quality, see the distribution of '
                                     'features, check for missing values and outliers, and analyze correlations '
                                     'between variables and the target. You do this using summary statistics like '
                                     'describe() and plots like histograms and pairplots to figure out what data '
                                     'cleaning and feature engineering you need before training models.',
                      'missing_concepts': ['Generates domain hypotheses and guides downstream feature engineering, '
                                           'transformations, and model selection']},
                     {'quality_level': 'average',
                      'human_score': 64,
                      'answer_text': 'EDA means looking at the data first. You check df.info() and df.describe(), make '
                                     'some charts like histograms and heatmaps, and see if there are any outliers or '
                                     'null values. It helps you understand what the data looks like so you know which '
                                     'columns to drop before running scikit-learn.',
                      'missing_concepts': ['Discovers pairwise relationships, collinearity, and interactions between '
                                           'predictors and the target variable',
                                           'Generates domain hypotheses and guides downstream feature engineering, '
                                           'transformations, and model selection']},
                     {'quality_level': 'poor',
                      'human_score': 26,
                      'answer_text': "EDA stands for Electronic Data Architecture. It's when you format a CSV into an "
                                     'SQL table and deploy it to AWS S3 so other microservices can access the '
                                     'database.',
                      'missing_concepts': ['EDA uncovers underlying distributions, central tendencies, and spread of '
                                           'individual features',
                                           'Profiles data hygiene: identifies missing value patterns, duplicates, data '
                                           'type mismatches, and anomalies/outliers',
                                           'Discovers pairwise relationships, collinearity, and interactions between '
                                           'predictors and the target variable',
                                           'Generates domain hypotheses and guides downstream feature engineering, '
                                           'transformations, and model selection']}]},
 {'topic_tag': 'Pandas DataFrame vs Series',
  'question': 'How do Pandas Series and DataFrame structures differ in dimensions, indexing, and internal memory '
              'layout?',
  'keywords': ['Pandas', 'DataFrame', 'Series', '1D vs 2D', 'BlockManager', 'Homogeneous vs Heterogeneous Dtypes'],
  'expected_concepts': ['A Series is a one-dimensional labeled array supporting a single homogeneous data type; a '
                        'DataFrame is a two-dimensional tabular structure composed of aligned Series columns',
                        'A Series has a single Index; a DataFrame has two axes: a row Index (axis 0) and column labels '
                        '(axis 1)',
                        'Internally, DataFrames manage memory via a BlockManager that groups columns of identical '
                        'primitive NumPy dtypes into contiguous 2D ndarray blocks',
                        'Selecting a single column from a DataFrame yields a Series that typically shares the '
                        'underlying memory buffer (view vs copy)'],
  'model_answer': 'In Pandas, a Series is a one-dimensional labeled array capable of holding data of any single, '
                  'homogeneous datatype (e.g., int64, float64, object), accompanied by an explicit index. A DataFrame '
                  'is a two-dimensional, size-mutable tabular data structure with labeled axes: row index (axis 0) and '
                  'column labels (axis 1), conceptually representing a dictionary of aligned Series. Under the hood, '
                  'Pandas historically organizes DataFrame memory using the BlockManager, which consolidates columns '
                  'sharing the same primitive dtype (e.g., all float64 columns) into contiguous 2D NumPy memory '
                  'blocks. Selecting a single column from a DataFrame returns a Series view into that BlockManager '
                  'slice, avoiding expensive memory copies unless mutations trigger copy-on-write semantics.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 96,
                      'answer_text': 'The fundamental difference starts with dimensionality: a Series is 1D with a '
                                     'single index and a homogeneous dtype, whereas a DataFrame is a 2D tabular '
                                     'container with both a row index (axis 0) and column index (axis 1). Internally, '
                                     "a DataFrame isn't just a list of separate Series; it uses a BlockManager that "
                                     'packs columns of the same NumPy dtype into shared 2D contiguous memory blocks '
                                     'for computational efficiency. When you index a column from a DataFrame, it '
                                     'returns a Series that references that underlying block without copying data.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'A Series is a 1D labeled array with one index, containing elements of the same '
                                     'data type. A DataFrame is 2D with rows and columns, where each column is '
                                     'essentially a Series, allowing different data types across different columns. '
                                     'Pulling out a single column from a DataFrame gives you a Series. Under the hood, '
                                     'Pandas uses NumPy arrays to store the data.',
                      'missing_concepts': ['Internally, DataFrames manage memory via a BlockManager that groups '
                                           'columns of identical primitive NumPy dtypes into contiguous 2D ndarray '
                                           'blocks']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'A Series is just one column, while a DataFrame is a whole table with multiple '
                                     'rows and columns. A Series only has one index for rows, but a DataFrame has row '
                                     'names and column names. You can make a DataFrame by putting multiple Series '
                                     'together.',
                      'missing_concepts': ['Internally, DataFrames manage memory via a BlockManager that groups '
                                           'columns of identical primitive NumPy dtypes into contiguous 2D ndarray '
                                           'blocks',
                                           'Selecting a single column from a DataFrame yields a Series that typically '
                                           'shares the underlying memory buffer (view vs copy)']},
                     {'quality_level': 'poor',
                      'human_score': 28,
                      'answer_text': 'A DataFrame is stored on your hard drive in SQL format, while a Series is a '
                                     'temporary variable stored in CPU cache. You use Series when working with '
                                     'integers and DataFrames when working with text strings.',
                      'missing_concepts': ['A Series is a one-dimensional labeled array supporting a single '
                                           'homogeneous data type; a DataFrame is a two-dimensional tabular structure '
                                           'composed of aligned Series columns',
                                           'A Series has a single Index; a DataFrame has two axes: a row Index (axis '
                                           '0) and column labels (axis 1)',
                                           'Internally, DataFrames manage memory via a BlockManager that groups '
                                           'columns of identical primitive NumPy dtypes into contiguous 2D ndarray '
                                           'blocks',
                                           'Selecting a single column from a DataFrame yields a Series that typically '
                                           'shares the underlying memory buffer (view vs copy)']}]},
 {'topic_tag': 'NumPy Arrays vs Python Lists',
  'question': 'Why are NumPy arrays significantly faster and more memory-efficient than native Python lists for '
              'numerical operations?',
  'keywords': ['NumPy Arrays',
               'Python Lists',
               'Contiguous Memory',
               'Pointer Indirection',
               'Vectorization',
               'SIMD Hardware Instructions',
               'Homogeneous Type'],
  'expected_concepts': ['Python lists store pointers (references) to disparate PyObject instances, incurring pointer '
                        'indirection, cache misses, and object header overhead',
                        'NumPy ndarrays store homogeneous raw binary data in a single contiguous block of C-memory '
                        'without per-element object headers',
                        'NumPy leverages vectorized C loops and CPU SIMD (Single Instruction, Multiple Data) '
                        'instructions, eliminating Python interpreter loop overhead',
                        'Homogeneous dtypes eliminate runtime type checking during mathematical operations'],
  'model_answer': 'NumPy arrays outperform Python lists due to three core architectural advantages: memory layout, '
                  'type overhead, and vectorized execution. A standard Python list is an array of pointers referencing '
                  'discrete PyObject heap allocations; each element carries roughly 28 bytes of overhead (reference '
                  'count, type pointer, value) and causes frequent CPU cache misses due to memory fragmentation. '
                  'Conversely, a NumPy ndarray allocates a single contiguous C-level memory buffer containing raw '
                  'packed binary primitives of a homogeneous dtype (e.g., 8 bytes per float64). Furthermore, NumPy '
                  'operations execute pre-compiled C/Fortran routines that bypass the Python interpreter loop and '
                  'utilize CPU SIMD vector registers to process multiple numbers per clock cycle.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'The speedup comes down to memory layout and execution model. A native Python '
                                     'list is an array of 8-byte pointers pointing to separate PyObject instances '
                                     'scattered around the heap. Every integer has its own 28-byte overhead and '
                                     'requires pointer indirection, destroying CPU L1/L2 cache locality and forcing '
                                     'dynamic type checking on every iteration. NumPy arrays store homogeneous raw '
                                     'binary data in a single contiguous memory buffer. Because the data type is fixed '
                                     'and contiguous, NumPy runs compiled C loops that exploit hardware SIMD '
                                     'instructions to execute operations in parallel across CPU vector registers '
                                     'without Python interpreter overhead.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'NumPy arrays are faster because they store elements in contiguous memory blocks, '
                                     'whereas Python lists store pointers to objects scattered in memory. Also, NumPy '
                                     'arrays require all elements to have the same data type, which eliminates dynamic '
                                     'type checking at runtime. When you run operations like a + b, NumPy executes '
                                     'compiled C code under the hood instead of slow Python for-loops.',
                      'missing_concepts': ['NumPy leverages vectorized C loops and CPU SIMD (Single Instruction, '
                                           'Multiple Data) instructions, eliminating Python interpreter loop '
                                           'overhead']},
                     {'quality_level': 'average',
                      'human_score': 63,
                      'answer_text': 'Python lists are slow because they are dynamic and can hold any type of object, '
                                     'like strings and numbers mixed together. NumPy is written in C and forces '
                                     'everything to be the same type, so it does vector math without writing loops. It '
                                     "also uses less RAM because it doesn't store object metadata for every single "
                                     'number.',
                      'missing_concepts': ['Python lists store pointers (references) to disparate PyObject instances, '
                                           'incurring pointer indirection, cache misses, and object header overhead',
                                           'NumPy leverages vectorized C loops and CPU SIMD (Single Instruction, '
                                           'Multiple Data) instructions, eliminating Python interpreter loop '
                                           'overhead']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'NumPy arrays are faster because they run on the GPU by default using CUDA cores, '
                                     'whereas Python lists only run on a single CPU thread. Python lists are also '
                                     'immutable which slows them down.',
                      'missing_concepts': ['Python lists store pointers (references) to disparate PyObject instances, '
                                           'incurring pointer indirection, cache misses, and object header overhead',
                                           'NumPy ndarrays store homogeneous raw binary data in a single contiguous '
                                           'block of C-memory without per-element object headers',
                                           'NumPy leverages vectorized C loops and CPU SIMD (Single Instruction, '
                                           'Multiple Data) instructions, eliminating Python interpreter loop overhead',
                                           'Homogeneous dtypes eliminate runtime type checking during mathematical '
                                           'operations']}]},
 {'topic_tag': 'Data Types Taxonomy',
  'question': 'Explain Nominal, Ordinal, Interval, and Ratio data types with concrete statistical examples.',
  'keywords': ['Nominal', 'Ordinal', 'Interval', 'Ratio', 'Stevens Taxonomy', 'True Zero', 'Meaningful Differences'],
  'expected_concepts': ['Nominal: qualitative categories with no intrinsic order (e.g., blood type, country, colors); '
                        'supports mode and frequency counting',
                        'Ordinal: categorical data with ordered ranking but non-uniform intervals between ranks (e.g., '
                        'education level, Likert scale); supports median and rank correlation',
                        'Interval: quantitative numerical data with equal intervals but arbitrary/non-true zero point '
                        '(e.g., Celsius/Fahrenheit temperature); supports addition/subtraction and mean, but ratios '
                        'are meaningless',
                        'Ratio: quantitative numerical data with a true, non-arbitrary absolute zero (e.g., weight, '
                        'salary, distance); supports multiplication, division, and meaningful ratios (e.g., $100 is '
                        'double $50)'],
  'model_answer': 'Stanley Smith Stevens defined four levels of measurement: Nominal, Ordinal, Interval, and Ratio. '
                  'Nominal data represents unordered categories (e.g., blood types A, B, O, or marital status) where '
                  'only equality testing and mode calculations are permissible. Ordinal data features ranked '
                  'categories where relative order is defined but intervals between ranks are unequal or unknown '
                  '(e.g., customer satisfaction: low, medium, high; military ranks), enabling median and percentile '
                  'calculations. Interval data possesses constant, measurable distances between values but lacks a '
                  'true absolute zero (e.g., Celsius temperature, where 0°C does not mean total absence of heat, and '
                  '40°C is not twice as hot as 20°C). Ratio data has consistent intervals and a true absolute zero '
                  'representing absence of the attribute (e.g., annual salary, weight, age), allowing meaningful '
                  'multiplication and ratios (e.g., $80k is twice $40k).',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': "Stevens' taxonomy classifies data into four hierarchical levels: Nominal, "
                                     'Ordinal, Interval, and Ratio. Nominal is purely qualitative without ranking—like '
                                     'postal codes or eye colors—where you can only calculate modes. Ordinal adds '
                                     'intrinsic order but lacks consistent spacing—like education levels or survey '
                                     'ratings (agree, neutral, disagree)—where median and percentiles apply. Interval '
                                     'data has equal units between measurements but no true zero—like Celsius '
                                     "temperature or calendar years—meaning subtraction makes sense, but you can't say "
                                     '20 degrees is twice as hot as 10 degrees. Finally, Ratio data has a true '
                                     'physical zero representing absence—like revenue, height, or time—allowing valid '
                                     'ratios, where $100 is legitimately twice $50.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 83,
                      'answer_text': 'Nominal is categorical with no order, like gender or city names. Ordinal has a '
                                     'clear order, like movie star ratings or t-shirt sizes (S, M, L), but the gap '
                                     "between sizes isn't fixed. Interval data has equal spacing but no real zero, "
                                     'like temperature in Celsius. Ratio data has a true zero point, like weight or '
                                     'income, which allows you to multiply and divide meaningfully.',
                      'missing_concepts': ['Interval: quantitative numerical data with equal intervals but '
                                           'arbitrary/non-true zero point (e.g., Celsius/Fahrenheit temperature); '
                                           'supports addition/subtraction and mean, but ratios are meaningless']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Nominal data is names and labels with no order. Ordinal data is things you can '
                                     'sort like 1st, 2nd, 3rd place. Interval and ratio are numerical, but ratio has a '
                                     "zero while interval doesn't. For example, age is ratio because zero age means "
                                     'not born, while temperature is interval.',
                      'missing_concepts': ['Ordinal: categorical data with ordered ranking but non-uniform intervals '
                                           'between ranks (e.g., education level, Likert scale); supports median and '
                                           'rank correlation',
                                           'Ratio: quantitative numerical data with a true, non-arbitrary absolute '
                                           'zero (e.g., weight, salary, distance); supports multiplication, division, '
                                           'and meaningful ratios (e.g., $100 is double $50)']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'Nominal data is numbers in scientific notation. Ordinal data is timestamps '
                                     'formatted as strings. Interval data is SQL boolean true/false values, and Ratio '
                                     'data is floating point decimal precision.',
                      'missing_concepts': ['Nominal: qualitative categories with no intrinsic order (e.g., blood type, '
                                           'country, colors); supports mode and frequency counting',
                                           'Ordinal: categorical data with ordered ranking but non-uniform intervals '
                                           'between ranks (e.g., education level, Likert scale); supports median and '
                                           'rank correlation',
                                           'Interval: quantitative numerical data with equal intervals but '
                                           'arbitrary/non-true zero point (e.g., Celsius/Fahrenheit temperature); '
                                           'supports addition/subtraction and mean, but ratios are meaningless',
                                           'Ratio: quantitative numerical data with a true, non-arbitrary absolute '
                                           'zero (e.g., weight, salary, distance); supports multiplication, division, '
                                           'and meaningful ratios (e.g., $100 is double $50)']}]},
 {'topic_tag': 'Histograms vs Boxplots Outlier Detection',
  'question': 'How do boxplots visually indicate outliers using the Interquartile Range compared to frequency '
              'distributions in histograms?',
  'keywords': ['Boxplots',
               'Histograms',
               'IQR',
               'Tukey Whiskers',
               'Outlier Thresholds',
               'Modality',
               'Distribution Shape'],
  'expected_concepts': ['Boxplots visualize 5-number summary (Min, Q1, Median, Q3, Max) with whiskers extending to 1.5 '
                        '* IQR from quartiles',
                        'Data points beyond whiskers (Q1 - 1.5*IQR or Q3 + 1.5*IQR) are plotted individually as '
                        'outlier points',
                        'Histograms display continuous frequency distribution across bins, revealing multimodality '
                        '(e.g., bimodal peaks) that boxplots conceal',
                        'Combining both offers full distribution context: boxplot for objective outlier flags and '
                        'histogram for density and skewness'],
  'model_answer': 'Boxplots and histograms provide complementary visual perspectives on numerical distributions. A '
                  "boxplot illustrates John Tukey's 5-number summary: the central box represents the Interquartile "
                  'Range (IQR = Q3 - Q1) enclosing the middle 50% of data, with a line at the median. Whiskers extend '
                  'outward to the furthest non-outlier data points within 1.5 * IQR of the quartiles; any observation '
                  'beyond these thresholds is plotted as an explicit outlier dot. However, boxplots cannot reveal '
                  'multimodality. In contrast, a histogram divides continuous data into contiguous bins, displaying '
                  'sample frequency on the y-axis to expose bimodal or multimodal peaks and tail decay that boxplots '
                  'flatten. Data scientists often pair both plots to detect outliers while confirming overall '
                  'distribution modality.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 96,
                      'answer_text': "Boxplots use Tukey's IQR rule to explicitly pinpoint outliers: the box captures "
                                     'Q1 to Q3, and whiskers stretch out to 1.5 times the IQR. Anything beyond the '
                                     'whiskers is plotted individually as an outlier dot, giving you an immediate '
                                     'objective visual marker. Histograms, on the other hand, group data into '
                                     "frequency bins. While a histogram shows extreme tail bins, it doesn't "
                                     'automatically highlight individual points. However, histograms show '
                                     'multimodality—like a bimodal distribution with two distinct peaks—which a '
                                     'boxplot completely obscures because it only summarizes five percentiles.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'A boxplot shows the median and the IQR between the 25th and 75th percentiles. '
                                     'The whiskers go up to 1.5 times the IQR, and points outside that are plotted as '
                                     'dots representing outliers. Histograms show the actual frequency distribution of '
                                     'the data in bins. A histogram is great for seeing whether data is bell-shaped or '
                                     'skewed, while a boxplot is faster for spotting outliers across multiple '
                                     'categories.',
                      'missing_concepts': ['Histograms display continuous frequency distribution across bins, '
                                           'revealing multimodality (e.g., bimodal peaks) that boxplots conceal']},
                     {'quality_level': 'average',
                      'human_score': 63,
                      'answer_text': 'A boxplot is a box with lines called whiskers. If a number is too far out past '
                                     "the whiskers, it shows up as a circle which means it's an outlier. A histogram "
                                     'is a bar chart that shows how many items are in each range. Boxplots are easier '
                                     'to see outliers, but histograms show the shape of the data.',
                      'missing_concepts': ['Boxplots visualize 5-number summary (Min, Q1, Median, Q3, Max) with '
                                           'whiskers extending to 1.5 * IQR from quartiles',
                                           'Histograms display continuous frequency distribution across bins, '
                                           'revealing multimodality (e.g., bimodal peaks) that boxplots conceal']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'A histogram is used for categorical pie charts and boxplots are only used for '
                                     'time series data. You detect outliers in a histogram by checking which bar is '
                                     'colored red.',
                      'missing_concepts': ['Boxplots visualize 5-number summary (Min, Q1, Median, Q3, Max) with '
                                           'whiskers extending to 1.5 * IQR from quartiles',
                                           'Data points beyond whiskers (Q1 - 1.5*IQR or Q3 + 1.5*IQR) are plotted '
                                           'individually as outlier points',
                                           'Histograms display continuous frequency distribution across bins, '
                                           'revealing multimodality (e.g., bimodal peaks) that boxplots conceal',
                                           'Combining both offers full distribution context: boxplot for objective '
                                           'outlier flags and histogram for density and skewness']}]},
 {'topic_tag': 'Correlation vs Causation',
  'question': 'Why does a strong Pearson correlation coefficient between two variables not imply a causal '
              'relationship? Give an example of a confounding variable.',
  'keywords': ['Correlation vs Causation',
               'Pearson Correlation',
               'Confounding Variable',
               'Spurious Correlation',
               'Reverse Causality',
               'Randomized Controlled Trial'],
  'expected_concepts': ['Pearson correlation measures linear association strength (-1 to +1), not causal mechanisms or '
                        'directional influence',
                        'A third unobserved confounding variable (lurking variable) can drive simultaneous variation '
                        'in both observed variables, generating spurious correlation',
                        'Classic confounding example: Ice cream sales and drowning rates correlate strongly because '
                        'outdoor temperature / summer weather is the common cause',
                        'Establishing causality requires experimental intervention (RCTs), instrumental variables, or '
                        'causal DAG structural modeling'],
  'model_answer': "Pearson's correlation coefficient r measures the strength and direction of a linear association "
                  'between two variables, but it cannot determine causality, direction of influence, or underlying '
                  'mechanism. A high correlation often arises from: 1) a common confounding variable driving both '
                  'metrics; 2) reverse causality (Y causes X instead of X causing Y); or 3) pure random coincidence '
                  '(spurious correlation). A classic textbook example is the strong positive correlation between ice '
                  'cream sales and drowning incidents. Eating ice cream does not cause drowning; rather, high outdoor '
                  'summer temperatures serve as the confounding variable that independently increases both beach '
                  'attendance and ice cream consumption. Establishing true causality requires controlled '
                  'experimentation (e.g., A/B testing, RCTs) or causal inference techniques like instrumental '
                  'variables and difference-in-differences.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'Correlation measures whether two variables move together linearly, but it '
                                     "doesn't tell you if one causes the other, if the causality is reversed, or if a "
                                     'third confounding variable is responsible. The classic example is the '
                                     'correlation between ice cream sales and drowning deaths. They correlate '
                                     "strongly, but eating ice cream doesn't cause drowning. The confounder is hot "
                                     "summer weather—when it's hot, more people buy ice cream and more people swim, "
                                     'increasing drowning risk. To prove causality, you need randomized controlled '
                                     'trials or causal inference frameworks like propensity score matching or '
                                     'instrumental variables.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': "Correlation just means two things move in tandem, but it doesn't establish cause "
                                     "and effect. Often there's a third lurking variable called a confounder. For "
                                     'example, ice cream sales and shark attacks both spike at the same time, but ice '
                                     "cream doesn't attract sharks—summer weather causes more people to swim in the "
                                     'ocean and also causes more ice cream sales. To verify causality you need an A/B '
                                     'test.',
                      'missing_concepts': ['Pearson correlation measures linear association strength (-1 to +1), not '
                                           'causal mechanisms or directional influence']},
                     {'quality_level': 'average',
                      'human_score': 63,
                      'answer_text': "Just because two variables have a high correlation doesn't mean one causes the "
                                     "other. It could just be a coincidence or there's an outside factor. Like ice "
                                     "cream sales and sunburns go up together because it's sunny outside. You have to "
                                     'run experiments to know if one thing actually causes the other.',
                      'missing_concepts': ['Pearson correlation measures linear association strength (-1 to +1), not '
                                           'causal mechanisms or directional influence',
                                           'Establishing causality requires experimental intervention (RCTs), '
                                           'instrumental variables, or causal DAG structural modeling']},
                     {'quality_level': 'poor',
                      'human_score': 26,
                      'answer_text': 'If the Pearson correlation is above 0.8, it mathematically proves causality. If '
                                     'it is below 0.5, it is a confounding variable.',
                      'missing_concepts': ['Pearson correlation measures linear association strength (-1 to +1), not '
                                           'causal mechanisms or directional influence',
                                           'A third unobserved confounding variable (lurking variable) can drive '
                                           'simultaneous variation in both observed variables, generating spurious '
                                           'correlation',
                                           'Classic confounding example: Ice cream sales and drowning rates correlate '
                                           'strongly because outdoor temperature / summer weather is the common cause',
                                           'Establishing causality requires experimental intervention (RCTs), '
                                           'instrumental variables, or causal DAG structural modeling']}]},
 {'topic_tag': 'Outlier Detection Methods (IQR & Z-score)',
  'question': 'How do IQR-based thresholds (1.5xIQR) and Z-score thresholds (|Z| > 3) differ when identifying '
              'univariate outliers?',
  'keywords': ['Outlier Detection',
               'IQR Method',
               'Z-score Method',
               'Normal Distribution Assumption',
               'Robust Statistics',
               'Parametric vs Non-parametric'],
  'expected_concepts': ['Z-score is parametric: relies on mean and standard deviation, assuming the underlying data '
                        'follows an approximately Gaussian normal distribution',
                        'IQR is non-parametric: relies on quartiles (Q1, Q3, median) and makes no distributional '
                        'assumptions, making it resistant to masking effects',
                        'Z-score threshold (|Z| > 3) flags observations beyond 3 standard deviations, but extreme '
                        'outliers distort the mean and inflate std dev (masking outliers)',
                        'IQR threshold ([Q1 - 1.5*IQR, Q3 + 1.5*IQR]) remains robust against severe skewness and '
                        'heavy-tailed distributions'],
  'model_answer': 'Z-score and IQR-based filtering represent parametric versus non-parametric approaches to univariate '
                  'outlier detection. The Z-score measures how many standard deviations an observation lies from the '
                  'arithmetic mean: Z = (x - mu) / sigma. It assumes the underlying data follows an approximately '
                  'normal distribution, flagging values with |Z| > 3. However, severe outliers artificially inflate '
                  'both the sample mean and standard deviation, causing a masking effect where true outliers reduce '
                  'their own Z-scores. Conversely, the IQR method computes IQR = Q3 - Q1 and flags points outside [Q1 '
                  '- 1.5*IQR, Q3 + 1.5*IQR]. Because quartiles depend on ordinal rank rather than numeric magnitude, '
                  'the IQR method is robust, resistant to extreme values, and reliable across skewed and non-normal '
                  'distributions.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'The main distinction is parametric versus non-parametric. Z-score assumes data '
                                     'is roughly normally distributed and calculates how many standard deviations a '
                                     'point is from the mean, typically flagging values where absolute Z is greater '
                                     'than 3. The fatal flaw with Z-score is masking: extreme outliers pull the mean '
                                     'toward them and inflate the standard deviation, dampening their own Z-scores. '
                                     'IQR is non-parametric and rank-based; it calculates the spread between Q1 and Q3 '
                                     'and sets bounds at 1.5 times IQR. Because medians and quartiles are resistant to '
                                     'extreme values, IQR does not suffer from masking and works reliably even on '
                                     'heavily skewed distributions.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'Z-score uses the mean and standard deviation and assumes the data is normal, '
                                     'flagging anything where |Z| > 3. IQR uses quartiles: Q1 minus 1.5 IQR and Q3 '
                                     "plus 1.5 IQR. IQR is better for skewed data because median and percentiles don't "
                                     'get shifted by crazy extreme numbers, while the mean in Z-score gets distorted '
                                     'by the very outliers you are trying to find.',
                      'missing_concepts': ['Z-score threshold (|Z| > 3) flags observations beyond 3 standard '
                                           'deviations, but extreme outliers distort the mean and inflate std dev '
                                           '(masking outliers)']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': "Z-score tells you how many standard deviations away a point is, and if it's over "
                                     "3 it's an outlier. IQR is the difference between the 75th and 25th percentile, "
                                     'and you multiply by 1.5 to get the cutoff. Z-score is for bell curves, and IQR '
                                     "is for when your data has outliers or isn't normal.",
                      'missing_concepts': ['Z-score is parametric: relies on mean and standard deviation, assuming the '
                                           'underlying data follows an approximately Gaussian normal distribution',
                                           'Z-score threshold (|Z| > 3) flags observations beyond 3 standard '
                                           'deviations, but extreme outliers distort the mean and inflate std dev '
                                           '(masking outliers)']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'Z-score is an algorithm used for 3D computer graphics coordinates. IQR is a '
                                     'database query indexing method in PostgreSQL.',
                      'missing_concepts': ['Z-score is parametric: relies on mean and standard deviation, assuming the '
                                           'underlying data follows an approximately Gaussian normal distribution',
                                           'IQR is non-parametric: relies on quartiles (Q1, Q3, median) and makes no '
                                           'distributional assumptions, making it resistant to masking effects',
                                           'Z-score threshold (|Z| > 3) flags observations beyond 3 standard '
                                           'deviations, but extreme outliers distort the mean and inflate std dev '
                                           '(masking outliers)',
                                           'IQR threshold ([Q1 - 1.5*IQR, Q3 + 1.5*IQR]) remains robust against severe '
                                           'skewness and heavy-tailed distributions']}]},
 {'topic_tag': 'Skewness & Kurtosis Concepts',
  'question': "What do positive skewness and high kurtosis reveal about a dataset's distribution shape, tails, and "
              'outlier propensity?',
  'keywords': ['Skewness',
               'Kurtosis',
               'Leptokurtic',
               'Platykurtic',
               'Tail Heaviness',
               'Outlier Propensity',
               'Normal Distribution'],
  'expected_concepts': ['Skewness measures distribution asymmetry: positive skew indicates a right tail longer/fatter '
                        'than the left tail',
                        'Kurtosis (specifically excess kurtosis) measures tail heaviness and propensity for extreme '
                        'outliers, not merely peak sharpness',
                        'Leptokurtic distributions (excess kurtosis > 0) have heavy, fat tails and higher probability '
                        'of extreme events compared to normal distribution',
                        'Financial risk and insurance models rely heavily on kurtosis to guard against tail risk / '
                        'black swan outliers'],
  'model_answer': 'Skewness and kurtosis characterize the third and fourth standardized moments of a probability '
                  'distribution. Skewness measures horizontal asymmetry around the mean; positive skewness indicates '
                  'an asymmetric distribution with a long, extended right tail, meaning the mass of data is '
                  'concentrated on the left with sporadic high extreme values. Kurtosis measures tail heaviness '
                  'relative to a Gaussian distribution (which has kurtosis 3, or excess kurtosis 0). High positive '
                  'excess kurtosis denotes a leptokurtic distribution with fat tails and an elevated propensity for '
                  'extreme outliers. In quantitative finance and data science, high kurtosis signals tail risk, '
                  'warning modelers that normal distribution assumptions will dangerously underestimate the frequency '
                  'of extreme events.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'Skewness reflects asymmetry, while kurtosis reflects tail heaviness. Positive '
                                     'skewness means the distribution stretches out to the right with a long tail of '
                                     'high values, while most of the data points sit on the left. High '
                                     'kurtosis—specifically positive excess kurtosis or leptokurtic distribution—means '
                                     'the tails are fatter than a standard Gaussian bell curve. This means there is a '
                                     'much higher probability of seeing extreme outliers. In domains like algorithmic '
                                     'trading or fraud detection, ignoring high kurtosis leads to severely '
                                     'underestimating tail risk and rare catastrophic losses.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 83,
                      'answer_text': 'Skewness tells you if data leans left or right. Positive skew has a long right '
                                     'tail of extreme high numbers. Kurtosis tells you how heavy the tails are '
                                     'compared to a normal distribution. High kurtosis means fat tails, which means '
                                     'you get a lot more outliers than you would expect from a standard bell curve.',
                      'missing_concepts': ['Financial risk and insurance models rely heavily on kurtosis to guard '
                                           'against tail risk / black swan outliers']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Skewness is whether the curve is tilted to the left or right, and positive skew '
                                     'means it has a tail on the positive side. Kurtosis is how pointy the peak is or '
                                     'how flat it is. If you have high kurtosis, you have more outliers in your '
                                     'dataset.',
                      'missing_concepts': ['Kurtosis (specifically excess kurtosis) measures tail heaviness and '
                                           'propensity for extreme outliers, not merely peak sharpness',
                                           'Financial risk and insurance models rely heavily on kurtosis to guard '
                                           'against tail risk / black swan outliers']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'Skewness and kurtosis are hyperparameter settings in gradient boosted trees that '
                                     'control learning rate and tree depth.',
                      'missing_concepts': ['Skewness measures distribution asymmetry: positive skew indicates a right '
                                           'tail longer/fatter than the left tail',
                                           'Kurtosis (specifically excess kurtosis) measures tail heaviness and '
                                           'propensity for extreme outliers, not merely peak sharpness',
                                           'Leptokurtic distributions (excess kurtosis > 0) have heavy, fat tails and '
                                           'higher probability of extreme events compared to normal distribution',
                                           'Financial risk and insurance models rely heavily on kurtosis to guard '
                                           'against tail risk / black swan outliers']}]},
 {'topic_tag': 'Data Cleaning Best Practices',
  'question': 'What routine cleaning steps should be performed on raw datasets before feeding them into analytical '
              'workflows?',
  'keywords': ['Data Cleaning',
               'Deduplication',
               'Schema Validation',
               'Type Casting',
               'String Normalization',
               'Outlier Handling',
               'Missing Values'],
  'expected_concepts': ['De-duplicating records based on primary business keys or identical row content',
                        'Type casting and schema validation: converting date strings to datetime, parsing numerical '
                        'values with currency symbols',
                        'Handling missingness systematically (deletion, imputation, or missing indicator flags) rather '
                        'than dropping blindly',
                        'String normalization: stripping whitespace, lowercasing, handling encoding artifacts, and '
                        'standardizing categorical levels'],
  'model_answer': 'Robust data cleaning prepares raw, messy data for statistical analysis and modeling through several '
                  'systematic steps: 1) Deduplication: identifying and removing duplicate rows or contradictory '
                  'records based on unique business keys; 2) Schema validation and type coercion: parsing ISO '
                  "datetimes, converting stringified numbers (e.g., removing '$' and commas), and casting categories "
                  'to appropriate dtypes; 3) Text and categorical standardization: stripping leading/trailing '
                  'whitespace, standardizing case, fixing typographical inconsistencies, and collapsing rare '
                  'categorical levels; 4) Missing value remediation: profiling missingness patterns (MCAR/MAR/MNAR) '
                  'and applying principled imputation or indicator flags; and 5) Outlier and anomaly audit: validating '
                  'numerical bounds against domain logic (e.g., negative ages, impossible coordinates) and applying '
                  'capping or transformations.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 96,
                      'answer_text': 'A standard data cleaning checklist begins with checking schema integrity and '
                                     'type casting—parsing dates into real datetimes, stripping dollar signs or commas '
                                     'from numeric strings, and encoding categorical variables. Next is deduplication, '
                                     "ensuring you aren't double-counting rows on business keys. Then you standardize "
                                     'strings—trimming whitespace, unifying lowercase casing, and merging misspelled '
                                     "categories like 'NY' and 'New York'. After that, you handle missing values "
                                     'deliberately based on whether they are MCAR or MAR rather than blindly running '
                                     'dropna. Finally, you run domain sanity checks to catch physically impossible '
                                     'outliers like negative blood pressure or 200-year-old users.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'Before doing any analysis, you should remove duplicate rows, fix data types like '
                                     'turning string dates into datetime objects, and clean up messy text by stripping '
                                     'spaces and fixing misspellings. Then you check for missing data and decide '
                                     'whether to drop or impute it. Lastly, you look for obvious data entry errors or '
                                     'crazy outliers that violate business logic.',
                      'missing_concepts': ['Handling missingness systematically (deletion, imputation, or missing '
                                           'indicator flags) rather than dropping blindly']},
                     {'quality_level': 'average',
                      'human_score': 63,
                      'answer_text': 'You should check df.isnull().sum() and drop or fill the missing values, run '
                                     'drop_duplicates() to get rid of duplicate records, and convert text columns to '
                                     'numbers using one-hot encoding. You also remove outliers that look too big.',
                      'missing_concepts': ['Type casting and schema validation: converting date strings to datetime, '
                                           'parsing numerical values with currency symbols',
                                           'String normalization: stripping whitespace, lowercasing, handling encoding '
                                           'artifacts, and standardizing categorical levels']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'Data cleaning is just deleting all rows that contain text and converting all '
                                     "numbers to integers between 0 and 1 so your database doesn't crash.",
                      'missing_concepts': ['De-duplicating records based on primary business keys or identical row '
                                           'content',
                                           'Type casting and schema validation: converting date strings to datetime, '
                                           'parsing numerical values with currency symbols',
                                           'Handling missingness systematically (deletion, imputation, or missing '
                                           'indicator flags) rather than dropping blindly',
                                           'String normalization: stripping whitespace, lowercasing, handling encoding '
                                           'artifacts, and standardizing categorical levels']}]},
 {'topic_tag': 'Descriptive vs Inferential Statistics',
  'question': 'Contrast Descriptive Statistics with Inferential Statistics regarding goals, data scope, and confidence '
              'intervals.',
  'keywords': ['Descriptive Statistics',
               'Inferential Statistics',
               'Population vs Sample',
               'Confidence Intervals',
               'Hypothesis Testing',
               'Generalization'],
  'expected_concepts': ['Descriptive statistics summarizes and describes the properties of an observed sample without '
                        'drawing conclusions beyond the data',
                        'Inferential statistics uses sample data to make probabilistic generalizations, parameter '
                        'estimates, and predictions about an unobserved wider population',
                        'Descriptive tools include mean, median, standard deviation, percentiles, and histograms',
                        'Inferential tools include confidence intervals, p-values, hypothesis tests (t-tests, ANOVA), '
                        'and regression modeling to quantify uncertainty'],
  'model_answer': 'Descriptive statistics focuses solely on summarizing, organizing, and presenting the '
                  'characteristics of an existing, observed dataset. It employs summary metrics such as mean, median, '
                  "variance, range, and visual representations like histograms to describe 'what the data shows' "
                  'without making claims beyond that specific dataset. Conversely, inferential statistics utilizes '
                  'sample data to draw probabilistic conclusions and generalizations about a larger, unobserved target '
                  'population. Because sample data inherently contains sampling variability, inferential statistics '
                  'employs mathematical frameworks—such as hypothesis testing, standard errors, and confidence '
                  'intervals—to quantify the uncertainty and precision of population parameter estimates.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 96,
                      'answer_text': 'Descriptive statistics is all about summarizing the data you actually have in '
                                     'front of you—metrics like mean, median, standard deviation, and histograms that '
                                     'describe the sample without making claims beyond it. Inferential statistics '
                                     'takes that sample and makes probabilistic inferences about the entire '
                                     "population. Because you haven't measured every person in the population, there "
                                     'is sampling error, so inferential statistics uses tools like confidence '
                                     'intervals, standard errors, and p-values to quantify uncertainty and tell you '
                                     'how likely your sample findings generalize to the broader population.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'Descriptive statistics summarizes your current dataset using things like '
                                     'averages, medians, and plots. Inferential statistics uses a small sample to draw '
                                     'conclusions about a whole population. For example, inferential stats uses '
                                     'confidence intervals and hypothesis tests like t-tests to see if differences are '
                                     'statistically significant or just random noise.',
                      'missing_concepts': ['Descriptive tools include mean, median, standard deviation, percentiles, '
                                           'and histograms']},
                     {'quality_level': 'average',
                      'human_score': 61,
                      'answer_text': 'Descriptive statistics describes the dataset with means and graphs. Inferential '
                                     'statistics makes predictions and tests hypotheses. Inferential uses things like '
                                     'p-values and confidence intervals to see if your model is accurate.',
                      'missing_concepts': ['Inferential statistics uses sample data to make probabilistic '
                                           'generalizations, parameter estimates, and predictions about an unobserved '
                                           'wider population',
                                           'Descriptive tools include mean, median, standard deviation, percentiles, '
                                           'and histograms']},
                     {'quality_level': 'poor',
                      'human_score': 26,
                      'answer_text': 'Descriptive statistics is for SQL databases, while inferential statistics is '
                                     'only used for deep learning neural networks.',
                      'missing_concepts': ['Descriptive statistics summarizes and describes the properties of an '
                                           'observed sample without drawing conclusions beyond the data',
                                           'Inferential statistics uses sample data to make probabilistic '
                                           'generalizations, parameter estimates, and predictions about an unobserved '
                                           'wider population',
                                           'Descriptive tools include mean, median, standard deviation, percentiles, '
                                           'and histograms',
                                           'Inferential tools include confidence intervals, p-values, hypothesis tests '
                                           '(t-tests, ANOVA), and regression modeling to quantify uncertainty']}]},
 {'topic_tag': 'Empirical Rule (68-95-99.7)',
  'question': 'How does the 68-95-99.7 Empirical Rule apply to standard normal distributions and z-score standard '
              'deviations?',
  'keywords': ['Empirical Rule', 'Normal Distribution', 'Standard Deviation', '68%', '95%', '99.7%', 'Z-scores'],
  'expected_concepts': ['Applies strictly to symmetric, unimodal, bell-shaped Gaussian normal distributions',
                        'Approximately 68.27% of observations fall within +/- 1 standard deviation of the mean (mu +/- '
                        '1 sigma, |z| <= 1)',
                        'Approximately 95.45% of observations fall within +/- 2 standard deviations of the mean (mu '
                        '+/- 2 sigma, |z| <= 2)',
                        'Approximately 99.73% of observations fall within +/- 3 standard deviations of the mean (mu '
                        '+/- 3 sigma, |z| <= 3), leaving only ~0.27% in extreme outer tails'],
  'model_answer': 'The Empirical Rule (also known as the Three-Sigma Rule) applies specifically to unimodal, symmetric '
                  'normal distributions. It states that: 1) approximately 68.27% of all data points lie within one '
                  'standard deviation of the mean (mu +/- 1 sigma, corresponding to z-scores between -1 and +1); 2) '
                  'approximately 95.45% lie within two standard deviations (mu +/- 2 sigma, z-scores between -2 and '
                  '+2); and 3) approximately 99.73% lie within three standard deviations (mu +/- 3 sigma, z-scores '
                  'between -3 and +3). This leaves only 0.27% of observations in the extreme tails (0.135% on either '
                  'side), providing the theoretical foundation for using |z| > 3 as a conventional cutoff for outlier '
                  'detection in Gaussian data.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 98,
                      'answer_text': 'The Empirical Rule, or 68-95-99.7 rule, applies to bell-shaped, Gaussian normal '
                                     'distributions. It tells us that roughly 68% of the data falls within one '
                                     'standard deviation of the mean (z-score between -1 and 1), about 95% falls '
                                     'within two standard deviations (z-score between -2 and 2), and 99.7% falls '
                                     'within three standard deviations. That means only about 0.3% of points lie '
                                     'beyond three standard deviations, which is why a z-score greater than 3 is '
                                     'standard practice for flagging statistical outliers in normally distributed '
                                     'features.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 85,
                      'answer_text': 'For a normal distribution, the 68-95-99.7 rule means 68% of your values are '
                                     'within one standard deviation of the mean, 95% are within two standard '
                                     'deviations, and 99.7% are within three standard deviations. Anything with a '
                                     'z-score above 3 or below -3 is in that remaining 0.3%, which makes it an extreme '
                                     'outlier.',
                      'missing_concepts': ['Applies strictly to symmetric, unimodal, bell-shaped Gaussian normal '
                                           'distributions']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'The rule says that 68% of data is in 1 standard deviation, 95% is in 2, and 99% '
                                     'is in 3. You can use it to see if numbers are outliers by calculating their '
                                     'z-score.',
                      'missing_concepts': ['Applies strictly to symmetric, unimodal, bell-shaped Gaussian normal '
                                           'distributions',
                                           'Approximately 99.73% of observations fall within +/- 3 standard deviations '
                                           'of the mean (mu +/- 3 sigma, |z| <= 3), leaving only ~0.27% in extreme '
                                           'outer tails']},
                     {'quality_level': 'poor',
                      'human_score': 23,
                      'answer_text': 'The empirical rule applies to all datasets regardless of distribution, stating '
                                     'that 68% of machine learning predictions are true positives, 95% are true '
                                     'negatives, and 99.7% are model accuracy.',
                      'missing_concepts': ['Applies strictly to symmetric, unimodal, bell-shaped Gaussian normal '
                                           'distributions',
                                           'Approximately 68.27% of observations fall within +/- 1 standard deviation '
                                           'of the mean (mu +/- 1 sigma, |z| <= 1)',
                                           'Approximately 95.45% of observations fall within +/- 2 standard deviations '
                                           'of the mean (mu +/- 2 sigma, |z| <= 2)',
                                           'Approximately 99.73% of observations fall within +/- 3 standard deviations '
                                           'of the mean (mu +/- 3 sigma, |z| <= 3), leaving only ~0.27% in extreme '
                                           'outer tails']}]},
 {'topic_tag': 'SQL Aggregate Functions',
  'question': 'How do COUNT(), SUM(), AVG(), MIN(), and MAX() operate when encountering NULL values in relational '
              'columns?',
  'keywords': ['SQL Aggregates', 'COUNT(*)', 'COUNT(column)', 'SUM()', 'AVG()', 'NULL Handling', 'Three-Valued Logic'],
  'expected_concepts': ['COUNT(*) counts all rows including rows with NULL values; COUNT(column_name) counts only '
                        'non-NULL entries in that column',
                        'SUM(), AVG(), MIN(), and MAX() completely ignore/exclude NULL values during computation',
                        'AVG(column) divides the sum of non-NULLs by the count of non-NULLs, NOT by total rows (which '
                        'can surprise developers)',
                        'If all rows in a group contain NULL, SUM, AVG, MIN, and MAX return NULL, whereas '
                        'COUNT(column) returns 0'],
  'model_answer': 'In ANSI SQL, aggregate functions treat NULL values with specific rules: 1) COUNT(*) counts every '
                  'qualifying row regardless of column content, including rows where all columns are NULL; 2) '
                  'COUNT(column_name) counts only rows where the specified column is NOT NULL; 3) SUM(), AVG(), MIN(), '
                  'and MAX() explicitly ignore NULL values. Crucially, AVG(column) calculates the sum of non-NULL '
                  'values divided strictly by the count of non-NULL values; if 5 out of 10 rows are NULL and the other '
                  '5 sum to 50, AVG() returns 10, not 5. Finally, if an entire column or group consists solely of '
                  'NULLs, SUM, AVG, MIN, and MAX return NULL, while COUNT(column) evaluates to 0.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'SQL aggregate functions ignore NULLs, with one key distinction between COUNT(*) '
                                     'and COUNT(col). COUNT(*) counts all rows regardless of NULLs, but '
                                     'COUNT(column_name) only counts rows where that specific column is not NULL. SUM, '
                                     'AVG, MIN, and MAX completely skip NULL values. The biggest trap is AVG(): it '
                                     'divides the sum of non-NULL rows by the count of non-NULL rows, not the total '
                                     'row count. So if you have 10 rows and 5 are NULL with values 10, 10, 10, 10, 10, '
                                     "AVG gives you 10, whereas if you expected NULL to mean zero, you'd need "
                                     'COALESCE(col, 0) to get 5. If a column has only NULLs, COUNT returns 0, but SUM '
                                     'and AVG return NULL.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'COUNT(*) counts every row in the table, while COUNT(column) only counts rows '
                                     "that aren't NULL. Functions like SUM, AVG, MIN, and MAX simply ignore NULL "
                                     'values. So AVG only averages across rows that have real numbers. If you want '
                                     'NULLs treated as zero in an average, you have to use COALESCE.',
                      'missing_concepts': ['If all rows in a group contain NULL, SUM, AVG, MIN, and MAX return NULL, '
                                           'whereas COUNT(column) returns 0']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'SQL functions like SUM and AVG skip null values. COUNT(*) counts all the rows, '
                                     'but count of a column only counts non-nulls. If you have nulls in your column, '
                                     'AVG will just calculate the average of whatever numbers are there.',
                      'missing_concepts': ['AVG(column) divides the sum of non-NULLs by the count of non-NULLs, NOT by '
                                           'total rows (which can surprise developers)',
                                           'If all rows in a group contain NULL, SUM, AVG, MIN, and MAX return NULL, '
                                           'whereas COUNT(column) returns 0']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'If a column contains any NULL values, SUM and AVG throw a syntax runtime error '
                                     'and rollback the transaction unless you disable strict SQL mode.',
                      'missing_concepts': ['COUNT(*) counts all rows including rows with NULL values; '
                                           'COUNT(column_name) counts only non-NULL entries in that column',
                                           'SUM(), AVG(), MIN(), and MAX() completely ignore/exclude NULL values '
                                           'during computation',
                                           'AVG(column) divides the sum of non-NULLs by the count of non-NULLs, NOT by '
                                           'total rows (which can surprise developers)',
                                           'If all rows in a group contain NULL, SUM, AVG, MIN, and MAX return NULL, '
                                           'whereas COUNT(column) returns 0']}]},
 {'topic_tag': 'Pandas Merge vs Join vs Concat',
  'question': 'Distinguish between Pandas merge(), join(), and concat() methods for combining tabular DataFrames.',
  'keywords': ['Pandas', 'merge()', 'join()', 'concat()', 'Relational Joins', 'Index Stacking', 'Axis Alignment'],
  'expected_concepts': ['pd.merge() performs SQL-style relational database joins on one or more arbitrary column keys '
                        'or indexes (inner, left, right, outer)',
                        'df.join() is a convenience wrapper around merge() that defaults to joining on DataFrame Index '
                        'labels rather than columns',
                        'pd.concat() stacks or concatenates DataFrames along a specific axis (axis=0 for row stacking, '
                        'axis=1 for column side-by-side concatenation) based on index alignment',
                        'merge/join combine based on matching key values; concat binds blocks of data along an axis'],
  'model_answer': 'Pandas provides three primary functions to combine DataFrames: 1) pd.merge() is the most flexible, '
                  'full-featured SQL-style relational join tool, matching records on specified key columns or index '
                  "levels via 'how' parameters ('inner', 'left', 'right', 'outer'); 2) DataFrame.join() is a "
                  'convenient shorthand built atop merge that defaults to joining on row indexes (or a column to an '
                  'index) rather than arbitrary columns; 3) pd.concat() performs physical stacking or gluing of '
                  'DataFrames along a chosen axis—axis=0 stacks rows vertically (e.g., appending monthly logs), while '
                  'axis=1 aligns side-by-side on index. Unlike merge, concat does not join on column values, but '
                  'rather aligns and glues arrays along index labels.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 96,
                      'answer_text': 'pd.merge() is your SQL-style relational joiner—you use it when you want to join '
                                     'on common columns or key values with inner, left, right, or outer joins. '
                                     'DataFrame.join() is basically a specialized convenience method that joins tables '
                                     'specifically on their index labels by default. pd.concat(), on the other hand, '
                                     'is for stacking data along an axis: axis=0 binds rows vertically (like appending '
                                     'identical schemas), while axis=1 sticks columns together side by side matching '
                                     'index labels. So merge is for key-based relational joins, while concat is for '
                                     'axis-based physical concatenation.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 83,
                      'answer_text': 'pd.merge is like SQL joins where you match on column keys using inner, outer, '
                                     'left, or right joins. join() is a DataFrame method that does the same thing but '
                                     'specifically matches on DataFrame indexes. concat() is used when you want to '
                                     'glue two DataFrames together, either stacking them on top of each other with '
                                     'axis=0 or side by side with axis=1.',
                      'missing_concepts': ['df.join() is a convenience wrapper around merge() that defaults to joining '
                                           'on DataFrame Index labels rather than columns']},
                     {'quality_level': 'average',
                      'human_score': 63,
                      'answer_text': 'Merge is for SQL joins like inner join on columns. Join is for joining indexes. '
                                     'Concat is for appending rows from one dataframe to another. They all combine '
                                     'dataframes in different ways.',
                      'missing_concepts': ['pd.concat() stacks or concatenates DataFrames along a specific axis '
                                           '(axis=0 for row stacking, axis=1 for column side-by-side concatenation) '
                                           'based on index alignment',
                                           'df.join() is a convenience wrapper around merge() that defaults to joining '
                                           'on DataFrame Index labels rather than columns']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'Merge is for NumPy arrays, join is for Python string concatenation, and concat '
                                     'is a command line tool in Linux bash for printing text files.',
                      'missing_concepts': ['pd.merge() performs SQL-style relational database joins on one or more '
                                           'arbitrary column keys or indexes (inner, left, right, outer)',
                                           'df.join() is a convenience wrapper around merge() that defaults to joining '
                                           'on DataFrame Index labels rather than columns',
                                           'pd.concat() stacks or concatenates DataFrames along a specific axis '
                                           '(axis=0 for row stacking, axis=1 for column side-by-side concatenation) '
                                           'based on index alignment',
                                           'merge/join combine based on matching key values; concat binds blocks of '
                                           'data along an axis']}]},
 {'topic_tag': 'Data Visualization Selection Guide',
  'question': 'When should you select a scatter plot, bar chart, line chart, or boxplot to communicate insights '
              'effectively?',
  'keywords': ['Data Visualization',
               'Scatter Plot',
               'Bar Chart',
               'Line Chart',
               'Boxplot',
               'Data Storytelling',
               'Visual Encoding'],
  'expected_concepts': ['Scatter plots communicate relationships, correlations, and clusters between two continuous '
                        'numerical variables',
                        'Line charts display trends, temporal dynamics, and continuous changes over ordered intervals '
                        '(usually time)',
                        'Bar charts compare discrete categorical groups against a numerical aggregate metric (e.g., '
                        'revenue by country)',
                        'Boxplots compare distributions, median spread, and outliers across multiple categorical '
                        'cohorts'],
  'model_answer': 'Choosing the appropriate visualization depends on variable data types and the analytical question: '
                  '1) Scatter plots are ideal for examining bivariate relationships, correlation strength, non-linear '
                  'patterns, and clustering between two continuous numerical variables (e.g., marketing spend vs '
                  'revenue); 2) Line charts are best suited for displaying trends and continuity across an ordered '
                  'dimension, predominantly time series (e.g., monthly churn over 3 years); 3) Bar charts compare '
                  'discrete categorical entities along a numerical magnitude (e.g., sales across 5 regional '
                  'territories), leveraging human visual acuity for length comparison; and 4) Boxplots are suited for '
                  'comparing continuous distributions, quartiles, and outlier dispersion across categorical segments '
                  '(e.g., salary distributions by job title).',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'The choice comes down to data types and the narrative. Use a scatter plot when '
                                     'exploring the relationship or correlation between two continuous variables, like '
                                     'price versus square footage. Use a line chart when tracking a continuous trend '
                                     'over an ordered sequence, almost always time series data. Use a bar chart when '
                                     'comparing discrete categories against a summary metric, like revenue by product '
                                     'category, because human perception is extremely accurate at judging bar heights. '
                                     'Finally, use a boxplot when you want to compare the distribution, median, '
                                     'spread, and outliers of a continuous variable across multiple categorical '
                                     'cohorts, like salaries across departments.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'Scatter plots are for seeing correlations between two numeric numbers. Line '
                                     'charts are for time series trends showing change over time. Bar charts compare '
                                     'categorical groups against a metric, like sales per department. Boxplots are '
                                     'used when you want to compare distributions and see outliers across groups.',
                      'missing_concepts': ['Boxplots compare distributions, median spread, and outliers across '
                                           'multiple categorical cohorts']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'Line charts are for dates and time. Bar charts are for comparing categories. '
                                     'Scatter plots show dots for two numbers to see if they line up. Boxplots show '
                                     'the minimum, maximum, and median for groups of data.',
                      'missing_concepts': ['Scatter plots communicate relationships, correlations, and clusters '
                                           'between two continuous numerical variables',
                                           'Boxplots compare distributions, median spread, and outliers across '
                                           'multiple categorical cohorts']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'You should always use 3D pie charts because they present all dimensions '
                                     'simultaneously. Bar charts and scatter plots are obsolete in modern business '
                                     'intelligence dashboards.',
                      'missing_concepts': ['Scatter plots communicate relationships, correlations, and clusters '
                                           'between two continuous numerical variables',
                                           'Line charts display trends, temporal dynamics, and continuous changes over '
                                           'ordered intervals (usually time)',
                                           'Bar charts compare discrete categorical groups against a numerical '
                                           'aggregate metric (e.g., revenue by country)',
                                           'Boxplots compare distributions, median spread, and outliers across '
                                           'multiple categorical cohorts']}]},
 {'topic_tag': 'Central Limit Theorem (CLT)',
  'question': 'Why is the Central Limit Theorem fundamental to inferential statistics, and what conditions are '
              'required for its sampling distribution of the sample mean?',
  'keywords': ['Central Limit Theorem',
               'CLT',
               'Sampling Distribution',
               'Sample Mean',
               'Standard Error',
               'Independent Identically Distributed (i.i.d.)',
               'Sample Size n >= 30'],
  'expected_concepts': ['CLT states that the sampling distribution of the sample mean approaches a normal distribution '
                        "as sample size n increases, regardless of the underlying population's shape",
                        'Requires observations to be independent and identically distributed (i.i.d.) with a finite '
                        'variance sigma^2',
                        'The mean of the sampling distribution equals population mean mu, with standard error sigma / '
                        'sqrt(n)',
                        'Enables parametric hypothesis testing (Z-tests, t-tests) and confidence interval construction '
                        'on real-world non-normal populations when n is sufficiently large (typically n >= 30)'],
  'model_answer': 'The Central Limit Theorem (CLT) is the cornerstone of inferential statistics. It proves that given '
                  'independent and identically distributed (i.i.d.) random variables drawn from any population with a '
                  'finite mean mu and finite variance sigma^2, the sampling distribution of the sample mean approaches '
                  'a Gaussian normal distribution N(mu, sigma^2 / n) as sample size n grows large, regardless of how '
                  'skewed or non-normal the original population distribution was. The standard error decreases '
                  'proportionally to 1/sqrt(n). This result is profound because it allows statisticians to compute '
                  'confidence intervals, p-values, and parametric tests (Z-tests, t-tests) on real-world data (such as '
                  'web conversion rates, incomes, or user click counts) without requiring the underlying population '
                  'itself to be normally distributed, typically provided n >= 30.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'The Central Limit Theorem states that if you take repeated random samples of '
                                     'size n from virtually any population with finite variance, the distribution of '
                                     'the sample means will converge to a normal distribution as n increases, '
                                     'regardless of whether the underlying population is skewed, uniform, or bimodal. '
                                     'The sampling distribution will have the same mean as the population, and its '
                                     'spread—the standard error—equals sigma divided by the square root of n. The '
                                     'required conditions are that observations are independent and identically '
                                     'distributed (i.i.d.) and sample size is reasonably large, usually rule-of-thumb '
                                     'n >= 30. CLT is the foundation of inferential statistics because it justifies '
                                     'using z-tests, t-tests, and confidence intervals on non-normal data.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'CLT says that when you take large enough samples (typically n >= 30) from any '
                                     'distribution, the average of those samples will follow a normal bell curve. The '
                                     'mean of this distribution is the true population mean, and the spread is sigma '
                                     'over root n. The data points must be independent. This is why we can use normal '
                                     'distribution formulas for hypothesis testing even when the original data is '
                                     'skewed.',
                      'missing_concepts': ['Requires observations to be independent and identically distributed '
                                           '(i.i.d.) with a finite variance sigma^2']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'The Central Limit Theorem means that as you collect more data (at least 30 '
                                     "samples), your dataset turns into a normal distribution. Because it's normal, "
                                     'you can calculate the mean and standard deviation to do hypothesis tests.',
                      'missing_concepts': ['CLT states that the sampling distribution of the sample mean approaches a '
                                           'normal distribution as sample size n increases, regardless of the '
                                           "underlying population's shape",
                                           'Requires observations to be independent and identically distributed '
                                           '(i.i.d.) with a finite variance sigma^2']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'The Central Limit Theorem states that every machine learning dataset eventually '
                                     'converges to an accuracy of 95% if trained for more than 30 epochs.',
                      'missing_concepts': ['CLT states that the sampling distribution of the sample mean approaches a '
                                           'normal distribution as sample size n increases, regardless of the '
                                           "underlying population's shape",
                                           'Requires observations to be independent and identically distributed '
                                           '(i.i.d.) with a finite variance sigma^2',
                                           'The mean of the sampling distribution equals population mean mu, with '
                                           'standard error sigma / sqrt(n)',
                                           'Enables parametric hypothesis testing (Z-tests, t-tests) and confidence '
                                           'interval construction on real-world non-normal populations when n is '
                                           'sufficiently large (typically n >= 30)']}]},
 {'topic_tag': 'Conditional Probability & Bayes Basics',
  'question': "Formulate Bayes' Rule and define conditional probability P(A|B), prior probability, and posterior "
              'probability in a diagnostic test context.',
  'keywords': ['Bayes Rule',
               'Conditional Probability',
               'Prior Probability',
               'Posterior Probability',
               'Likelihood',
               'Base Rate Fallacy'],
  'expected_concepts': ['Formula: P(A|B) = [P(B|A) * P(A)] / P(B), where P(B) is total probability sum P(B|A)P(A) + '
                        'P(B|~A)P(~A)',
                        'Prior probability P(A) is initial baseline belief before observing evidence; Posterior P(A|B) '
                        'is updated belief after evidence B',
                        'Likelihood P(B|A) is probability of observing evidence given hypothesis A (e.g., test '
                        'sensitivity)',
                        'Base rate fallacy: ignoring low prior P(A) causes people to severely overestimate posterior '
                        'probability of a rare disease after a positive test'],
  'model_answer': "Bayes' Rule calculates updated conditional probability based on prior beliefs and observed "
                  'evidence: P(A|B) = [P(B|A) * P(A)] / P(B). In medical diagnostics: 1) Prior P(Disease) is the '
                  'baseline disease prevalence in the population before taking a test; 2) Likelihood '
                  'P(Positive|Disease) is the test sensitivity; 3) Marginal probability P(Positive) is the total '
                  'probability of testing positive across both diseased and healthy populations: P(Pos|Dis)P(Dis) + '
                  'P(Pos|Healthy)P(Healthy); and 4) Posterior P(Disease|Positive) is the revised probability that the '
                  'patient actually has the disease given a positive result. When disease prevalence is rare (e.g., '
                  '0.1%), the base rate fallacy leads people to assume a 99% accurate test guarantees sickness, '
                  'whereas false positives in the massive healthy population can cause the true posterior probability '
                  'to remain surprisingly low.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': "Bayes' Rule states P(A|B) = [P(B|A) * P(A)] / P(B). In a medical diagnostic "
                                     "context: P(Disease) is your prior probability—the disease's base prevalence in "
                                     'the general population. P(Positive|Disease) is the likelihood, or test '
                                     'sensitivity. P(Positive) is the total probability of testing positive, expanded '
                                     'via the law of total probability. P(Disease|Positive) is the posterior '
                                     'probability—the probability you actually have the disease given a positive test. '
                                     'The base rate fallacy occurs when people ignore a tiny prior: if a disease '
                                     'affects only 1 in 1,000 people, even a 99% accurate test can yield more false '
                                     'positives than true positives, meaning your actual posterior probability of '
                                     'having the disease is much lower than 99%.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 83,
                      'answer_text': "Bayes' Theorem is P(A|B) equals P(B|A) times P(A) divided by P(B). The prior is "
                                     'the initial probability of having a disease before testing. The posterior is the '
                                     'updated probability of having the disease after getting a positive test. P(B|A) '
                                     'is the likelihood. If the disease is very rare, even an accurate test can have '
                                     'lots of false positives because of the low base rate.',
                      'missing_concepts': ['Formula: P(A|B) = [P(B|A) * P(A)] / P(B), where P(B) is total probability '
                                           'sum P(B|A)P(A) + P(B|~A)P(~A)']},
                     {'quality_level': 'average',
                      'human_score': 63,
                      'answer_text': 'Bayes rule updates probability when you get new evidence. P(A|B) means the '
                                     'probability of A given B. The prior is what you thought before, and the '
                                     'posterior is what you calculate after the test. If you get a positive test, '
                                     'Bayes rule calculates if you are really sick.',
                      'missing_concepts': ['Formula: P(A|B) = [P(B|A) * P(A)] / P(B), where P(B) is total probability '
                                           'sum P(B|A)P(A) + P(B|~A)P(~A)',
                                           'Base rate fallacy: ignoring low prior P(A) causes people to severely '
                                           'overestimate posterior probability of a rare disease after a positive '
                                           'test']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'Bayes rule proves that if a medical test is 95% accurate, the patient has '
                                     'exactly a 95% chance of being sick, regardless of population size.',
                      'missing_concepts': ['Formula: P(A|B) = [P(B|A) * P(A)] / P(B), where P(B) is total probability '
                                           'sum P(B|A)P(A) + P(B|~A)P(~A)',
                                           'Prior probability P(A) is initial baseline belief before observing '
                                           'evidence; Posterior P(A|B) is updated belief after evidence B',
                                           'Likelihood P(B|A) is probability of observing evidence given hypothesis A '
                                           '(e.g., test sensitivity)',
                                           'Base rate fallacy: ignoring low prior P(A) causes people to severely '
                                           'overestimate posterior probability of a rare disease after a positive '
                                           'test']}]},
 {'topic_tag': 'Quantitative vs Qualitative Attributes',
  'question': 'What is the difference between quantitative numerical variables (discrete vs continuous) and '
              'qualitative categorical variables?',
  'keywords': ['Quantitative Variables',
               'Qualitative Variables',
               'Discrete vs Continuous',
               'Categorical Data',
               'Measurement Scale',
               'Encoding Techniques'],
  'expected_concepts': ['Quantitative variables represent measurable numerical quantities where arithmetic operations '
                        '(+, -, *, /) are mathematically meaningful',
                        'Discrete quantitative variables represent countable integers (e.g., number of transactions, '
                        'customer visits); continuous variables represent infinite real values within an interval '
                        '(e.g., temperature, latency, weight)',
                        'Qualitative variables represent non-numeric categories or labels (e.g., hair color, country) '
                        'describing attributes or qualities',
                        'Qualitative variables require encoding (one-hot, label, or target encoding) before ingestion '
                        'into mathematical machine learning models'],
  'model_answer': 'In statistical data modeling, variables divide into quantitative (numerical) and qualitative '
                  '(categorical). Quantitative variables represent measurable numeric amounts where arithmetic '
                  'calculations like means and variances are mathematically valid. They subdivide into: 1) discrete '
                  'variables, which take on countable, distinct values—typically non-negative integers like number of '
                  'customer support tickets or items in a shopping cart; and 2) continuous variables, which can assume '
                  'any real value along an unbroken continuum within an interval, limited only by measurement '
                  'precision, like latency in milliseconds or revenue. In contrast, qualitative variables describe '
                  'qualities, states, or classes (e.g., user device type, shipping tier). Because machine learning '
                  'algorithms require numerical matrices, qualitative features must undergo encoding '
                  'transformations—such as one-hot encoding or target encoding—before modeling.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 96,
                      'answer_text': 'Quantitative variables are numerical measurements where mathematical operations '
                                     'like calculating an average make real sense. They split into discrete, which are '
                                     'countable whole numbers like number of orders or website clicks, and continuous, '
                                     'which can take any real value on a continuum like time in seconds or salary. '
                                     'Qualitative variables are categorical labels or descriptions, like device '
                                     "operating system or payment method. You can't compute a mathematical average of "
                                     'operating systems, so for machine learning pipelines you have to encode '
                                     'qualitative variables using techniques like one-hot encoding or ordinal mapping.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'Quantitative data is numbers you can measure. Discrete means countable integers '
                                     'like number of cars, while continuous can have decimals like height or '
                                     'temperature. Qualitative data is categories or text labels like color or brand '
                                     'name. You have to convert qualitative data into numbers using one-hot encoding '
                                     'before passing it to machine learning algorithms.',
                      'missing_concepts': ['Quantitative variables represent measurable numerical quantities where '
                                           'arithmetic operations (+, -, *, /) are mathematically meaningful']},
                     {'quality_level': 'average',
                      'human_score': 63,
                      'answer_text': 'Quantitative is numbers and qualitative is words. Discrete is whole numbers and '
                                     'continuous has decimals. Qualitative is categories like male or female, and you '
                                     'have to turn them into 0 and 1 for models.',
                      'missing_concepts': ['Quantitative variables represent measurable numerical quantities where '
                                           'arithmetic operations (+, -, *, /) are mathematically meaningful',
                                           'Qualitative variables require encoding (one-hot, label, or target '
                                           'encoding) before ingestion into mathematical machine learning models']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'Quantitative means high quality data, and qualitative means low quality or '
                                     'unverified data that needs to be deleted from the database.',
                      'missing_concepts': ['Quantitative variables represent measurable numerical quantities where '
                                           'arithmetic operations (+, -, *, /) are mathematically meaningful',
                                           'Discrete quantitative variables represent countable integers (e.g., number '
                                           'of transactions, customer visits); continuous variables represent infinite '
                                           'real values within an interval (e.g., temperature, latency, weight)',
                                           'Qualitative variables represent non-numeric categories or labels (e.g., '
                                           'hair color, country) describing attributes or qualities',
                                           'Qualitative variables require encoding (one-hot, label, or target '
                                           'encoding) before ingestion into mathematical machine learning models']}]},
 {'topic_tag': 'SQL WHERE vs HAVING Filtering',
  'question': "Why can't you use SQL aggregate functions inside a WHERE clause, and how does HAVING resolve this "
              'limitation?',
  'keywords': ['SQL', 'WHERE', 'HAVING', 'GROUP BY', 'Aggregate Functions', 'Filtering Order', 'Query Optimization'],
  'expected_concepts': ['WHERE filters individual raw table rows before any grouping or aggregation takes place in the '
                        'query execution pipeline',
                        'Aggregate functions (SUM, COUNT, AVG) compute values across groups of rows, which do not '
                        'exist when WHERE executes',
                        'HAVING executes after GROUP BY, enabling filtering predicates on the aggregated group results',
                        'Best practice: filter row-level conditions in WHERE first to minimize the dataset before '
                        'GROUP BY and HAVING evaluate'],
  'model_answer': 'In SQL logical query execution, the WHERE clause evaluates immediately after the FROM/JOIN clause '
                  'and before the GROUP BY clause. Consequently, WHERE operates strictly on individual, unaggregated '
                  'table rows. Because aggregate functions—like SUM(sales) or COUNT(user_id)—compute summary '
                  'statistics across groups of rows, their values do not exist yet when WHERE is evaluated, making '
                  "constructs like 'WHERE SUM(sales) > 1000' syntactically invalid. The HAVING clause was introduced "
                  'specifically to solve this problem: it executes after GROUP BY, applying filtering predicates '
                  'directly to the grouped and aggregated summary rows. Best query optimization practice dictates '
                  'using WHERE for all row-level predicates to reduce the dataset size prior to aggregation, and '
                  'reserving HAVING strictly for conditions on aggregate metrics.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': 'The reason comes down to the SQL execution lifecycle. WHERE evaluates before the '
                                     'GROUP BY clause on individual rows. Because aggregate functions like COUNT or '
                                     "SUM summarize groups of rows, their values haven't been computed yet when WHERE "
                                     'runs, so putting an aggregate in WHERE causes a syntax error. HAVING was '
                                     'designed specifically to run after GROUP BY, allowing you to filter based on '
                                     "aggregated results, like 'HAVING COUNT(*) > 5'. For performance, you should "
                                     'always push row-level filters into WHERE to shrink the table before aggregation, '
                                     'and only use HAVING for conditions on the aggregates themselves.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 83,
                      'answer_text': 'WHERE runs before GROUP BY to filter individual rows, so aggregate functions '
                                     "like SUM or COUNT don't exist yet when WHERE executes. HAVING runs after GROUP "
                                     'BY, so it can filter the grouped results based on aggregate calculations like '
                                     'HAVING SUM(amount) > 500. You should use WHERE to filter rows first and HAVING '
                                     'for aggregates.',
                      'missing_concepts': ['Best practice: filter row-level conditions in WHERE first to minimize the '
                                           'dataset before GROUP BY and HAVING evaluate']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': "You can't use aggregates in WHERE because WHERE is for normal columns. If you "
                                     'want to filter by an aggregate like COUNT or AVG, you have to use HAVING after '
                                     "GROUP BY. That's just how SQL syntax works.",
                      'missing_concepts': ['WHERE filters individual raw table rows before any grouping or aggregation '
                                           'takes place in the query execution pipeline',
                                           'Best practice: filter row-level conditions in WHERE first to minimize the '
                                           'dataset before GROUP BY and HAVING evaluate']},
                     {'quality_level': 'poor',
                      'human_score': 24,
                      'answer_text': 'WHERE and HAVING are completely identical synonyms in modern SQL dialects, and '
                                     'you can use them interchangeably anywhere in a SELECT query.',
                      'missing_concepts': ['WHERE filters individual raw table rows before any grouping or aggregation '
                                           'takes place in the query execution pipeline',
                                           'Aggregate functions (SUM, COUNT, AVG) compute values across groups of '
                                           'rows, which do not exist when WHERE executes',
                                           'HAVING executes after GROUP BY, enabling filtering predicates on the '
                                           'aggregated group results',
                                           'Best practice: filter row-level conditions in WHERE first to minimize the '
                                           'dataset before GROUP BY and HAVING evaluate']}]},
 {'topic_tag': 'CSV vs Parquet Storage Formats',
  'question': 'Compare CSV row-based text storage with Apache Parquet columnar binary storage in terms of compression, '
              'query performance, and disk footprint.',
  'keywords': ['CSV',
               'Parquet',
               'Row-based vs Columnar',
               'Compression (Snappy/Gzip)',
               'Predicate Pushdown',
               'Projection Pushdown',
               'Data Lakehouse'],
  'expected_concepts': ['CSV is row-oriented, plain-text format: human-readable but uncompressed, verbose, and lacking '
                        'embedded schema metadata (forces full table scan)',
                        'Parquet is columnar, binary format: stores values column-by-column, enabling superior '
                        'compression ratios (Snappy, ZSTD) on homogeneous data types',
                        'Projection pushdown: analytical queries scanning 3 columns out of 50 only read relevant '
                        'column chunks from disk, reducing IO exponentially',
                        'Predicate pushdown: Parquet file statistics (min/max per row group) allow the query engine to '
                        'skip entire blocks without reading them'],
  'model_answer': 'CSV and Apache Parquet represent row-oriented text versus columnar binary storage paradigms. CSV '
                  'stores data as uncompressed ASCII/UTF-8 rows separated by delimiters; it lacks embedded schema '
                  'metadata, requires expensive string parsing on read, and forces query engines to scan the entire '
                  'file across all columns even when querying a single attribute. In contrast, Parquet stores data '
                  'column-by-column in a binary, typed format with embedded metadata. Because adjacent values share '
                  'the same data type, Parquet achieves dramatic compression ratios (typically 75-90% smaller than raw '
                  'CSV) using dictionary encoding, run-length encoding, and Snappy/Zstandard compression. Furthermore, '
                  'Parquet enables projection pushdown (reading only requested columns) and predicate pushdown '
                  '(skipping irrelevant row groups using min/max chunk statistics), accelerating analytical queries in '
                  'Spark, DuckDB, and Snowflake by orders of magnitude.',
  'sample_answers': [{'quality_level': 'excellent',
                      'human_score': 97,
                      'answer_text': "CSV is a row-oriented, plain text format. While it's human-readable, it has "
                                     'massive downsides for analytics: it has no embedded schema, requires heavy CPU '
                                     'string parsing, and forces the engine to read every single column and row off '
                                     'disk even if your query only needs one column. Parquet is a binary, columnar '
                                     'format designed for data lakes. Because values in each column share the same '
                                     'data type, it achieves phenomenal compression using algorithms like Snappy and '
                                     'dictionary encoding, often shrinking file sizes by 80%. More importantly, '
                                     'Parquet supports projection pushdown—so if you only SELECT two columns out of a '
                                     '100-column table, it only reads those two column chunks—and predicate pushdown, '
                                     'where min/max metadata allows engines to skip entire row groups without reading '
                                     'them.',
                      'missing_concepts': []},
                     {'quality_level': 'good',
                      'human_score': 84,
                      'answer_text': 'CSV stores data row by row as plain text, which is easy to open in Excel but '
                                     'takes up huge disk space and is slow to query because the database has to scan '
                                     'the whole file. Parquet stores data by column in binary format. It compresses '
                                     'much better because all values in a column have the same type, and queries run '
                                     'much faster because you only read the columns you need and can skip rows using '
                                     'min/max metadata.',
                      'missing_concepts': ['CSV is row-oriented, plain-text format: human-readable but uncompressed, '
                                           'verbose, and lacking embedded schema metadata (forces full table scan)']},
                     {'quality_level': 'average',
                      'human_score': 62,
                      'answer_text': 'CSV is text files where values are separated by commas. Parquet is a compressed '
                                     'binary file used in big data like Hadoop and Spark. Parquet is smaller on disk '
                                     "and loads faster than CSV because it's columnar.",
                      'missing_concepts': ['Projection pushdown: analytical queries scanning 3 columns out of 50 only '
                                           'read relevant column chunks from disk, reducing IO exponentially',
                                           'Predicate pushdown: Parquet file statistics (min/max per row group) allow '
                                           'the query engine to skip entire blocks without reading them']},
                     {'quality_level': 'poor',
                      'human_score': 25,
                      'answer_text': 'CSV is a high-performance binary database format developed by Microsoft, while '
                                     'Parquet is a legacy text format that was deprecated in 2012.',
                      'missing_concepts': ['CSV is row-oriented, plain-text format: human-readable but uncompressed, '
                                           'verbose, and lacking embedded schema metadata (forces full table scan)',
                                           'Parquet is columnar, binary format: stores values column-by-column, '
                                           'enabling superior compression ratios (Snappy, ZSTD) on homogeneous data '
                                           'types',
                                           'Projection pushdown: analytical queries scanning 3 columns out of 50 only '
                                           'read relevant column chunks from disk, reducing IO exponentially',
                                           'Predicate pushdown: Parquet file statistics (min/max per row group) allow '
                                           'the query engine to skip entire blocks without reading them']}]}]

