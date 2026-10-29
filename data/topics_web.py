# Web Development Domain Topics (25 easy, 25 medium, 25 hard)

WEB_TOPICS = {'easy': [{'topic_tag': 'HTML5 Semantic Elements Benefits',
           'question': 'What are the SEO, accessibility, and structure benefits of using HTML5 semantic elements like '
                       '<header>, <nav>, and <article>?',
           'keywords': ['Semantic HTML',
                        'Accessibility',
                        'SEO Optimization',
                        'Header/Nav/Section',
                        'Screen Readers',
                        'Document Outline'],
           'expected_concepts': ['Semantic HTML uses meaningful tags (<header>, <nav>, <main>, <article>, <aside>, '
                                 '<footer>) that convey structural intent rather than generic <div> tags',
                                 'Accessibility (a11y) enhancement: Screen readers use semantic elements as landmark '
                                 'roles, enabling visually impaired users to jump directly to navigation, main '
                                 'content, or articles',
                                 'SEO benefits: Search engine web crawlers (like Googlebot) better understand document '
                                 'hierarchy and index the most important content more accurately',
                                 'Maintainability and structure: Cleaner document outline improves developer '
                                 "readability and reduces excessive class naming ('div soup')"],
           'model_answer': 'HTML5 semantic elements—such as <header>, <nav>, <main>, <article>, <section>, <aside>, '
                           'and <footer>—provide three primary advantages over generic <div> and <span> tags: 1. '
                           'Accessibility (a11y): Assistive technologies like screen readers map HTML5 semantic tags '
                           "directly to ARIA landmark roles (e.g., <nav> maps to role='navigation', <main> to "
                           "role='main'). This allows visually impaired users to press shortcut keys to quickly jump "
                           'between major regions of a webpage rather than listening to the entire page sequentially. '
                           '2. Search Engine Optimization (SEO): Search engine crawlers (Googlebot, Bingbot) use '
                           'semantic markup to decipher the information hierarchy of the page. An <article> signals '
                           'self-contained, syndicateable content (such as a blog post or news story), while <nav> '
                           'signals internal site architecture. This targeted parsing helps search engines identify '
                           'primary keywords and index content with higher contextual relevance. 3. Code '
                           "Maintainability: Semantic tags eliminate 'div soup'—excessively nested generic containers "
                           'with arbitrary class names—making the DOM tree self-documenting, easier to debug, and '
                           'faster for team members to collaborate on.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'Using HTML5 semantic elements instead of generic divs gives you three '
                                              'huge benefits: accessibility, SEO, and code maintainability. From an '
                                              'accessibility standpoint, screen readers and assistive devices '
                                              'automatically recognize semantic tags like <nav>, <main>, and <aside> '
                                              'as native landmark roles. That means a visually impaired user can use '
                                              'keyboard shortcuts to skip directly to the main content or jump between '
                                              'navigation links without having to listen to the entire header every '
                                              'single time. For SEO, search engine crawlers like Googlebot parse '
                                              "semantic tags to understand the page structure and prioritize what's "
                                              'actually important. For example, text wrapped in an <article> tag is '
                                              'weighted as standalone, indexable content, whereas an <aside> is '
                                              'recognized as secondary sidebar content. Finally, for team '
                                              "maintainability, it avoids what developers call 'div soup'. It's much "
                                              'easier to inspect and style a clean DOM tree that uses <header>, '
                                              '<section>, and <footer> compared to dozens of nested unsemantic divs '
                                              'with custom class names.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'HTML5 semantic elements like <header>, <nav>, and <article> make your '
                                              'code much more meaningful. The biggest benefit is accessibility because '
                                              "screen readers can tell the user when they're entering a navigation bar "
                                              'or reading the main article. It also really helps with SEO because '
                                              'search engines can parse the structure of your page better and know '
                                              'which part is the actual content versus the navigation or footer. And '
                                              'it makes your HTML much cleaner and easier to read for other developers '
                                              'compared to using nested div tags everywhere.',
                               'missing_concepts': ['Accessibility (a11y) enhancement: Screen readers use semantic '
                                                    'elements as landmark roles, enabling visually impaired users to '
                                                    'jump directly to navigation, main content, or articles']},
                              {'quality_level': 'average',
                               'human_score': 62,
                               'answer_text': 'Semantic elements are tags that describe their meaning, like <header> '
                                              'for the top of the page, <nav> for menu links, and <footer> for '
                                              'copyright at the bottom. Before HTML5, everyone used <div '
                                              "class='header'> and <div class='nav'>. Semantic tags help search "
                                              'engines index the site better because Google knows where the navigation '
                                              'is. They also make the HTML cleaner to read in code editors instead of '
                                              'having divs everywhere.',
                               'missing_concepts': ['Accessibility (a11y) enhancement: Screen readers use semantic '
                                                    'elements as landmark roles, enabling visually impaired users to '
                                                    'jump directly to navigation, main content, or articles',
                                                    'SEO benefits: Search engine web crawlers (like Googlebot) better '
                                                    'understand document hierarchy and index the most important '
                                                    'content more accurately']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'HTML5 semantic elements are tags that automatically apply CSS styling '
                                              'without writing CSS rules. For example, using <header> automatically '
                                              'makes the text bold and 24 pixels, and <nav> automatically turns links '
                                              'into a blue menu bar. It improves SEO because browsers render semantic '
                                              'tags on the GPU faster than divs.',
                               'missing_concepts': ['Semantic HTML uses meaningful tags (<header>, <nav>, <main>, '
                                                    '<article>, <aside>, <footer>) that convey structural intent '
                                                    'rather than generic <div> tags',
                                                    'Accessibility (a11y) enhancement: Screen readers use semantic '
                                                    'elements as landmark roles, enabling visually impaired users to '
                                                    'jump directly to navigation, main content, or articles',
                                                    'SEO benefits: Search engine web crawlers (like Googlebot) better '
                                                    'understand document hierarchy and index the most important '
                                                    'content more accurately',
                                                    'Maintainability and structure: Cleaner document outline improves '
                                                    "developer readability and reduces excessive class naming ('div "
                                                    "soup')"]}]},
          {'topic_tag': 'CSS Flexbox Layout Properties',
           'question': 'How do justify-content and align-items control layout alignment along flexbox axes?',
           'keywords': ['Flexbox',
                        'justify-content',
                        'align-items',
                        'flex-direction',
                        'Flex Container',
                        'Main Axis/Cross Axis'],
           'expected_concepts': ['Flexbox operates on two perpendicular axes: the Main Axis and the Cross Axis, '
                                 'determined by flex-direction (row vs column)',
                                 'justify-content aligns child flex items along the Main Axis (e.g., flex-start, '
                                 'center, flex-end, space-between, space-around, space-evenly)',
                                 'align-items aligns child flex items along the Cross Axis (e.g., stretch, flex-start, '
                                 'center, flex-end, baseline)',
                                 "Axis swapping: When flex-direction is changed to 'column', the Main Axis becomes "
                                 'vertical and Cross Axis becomes horizontal, swapping the visual orientation '
                                 'controlled by each property'],
           'model_answer': 'In CSS Flexible Box Layout (Flexbox), element alignment is governed by two perpendicular '
                           'axes: the Main Axis and the Cross Axis. 1. Defining the axes: The orientation of the axes '
                           "is defined by the container's flex-direction property. By default, flex-direction is "
                           "'row', meaning the Main Axis runs horizontally from left to right (in LTR writing modes) "
                           'and the Cross Axis runs vertically from top to bottom. If flex-direction is set to '
                           "'column', the axes swap: the Main Axis runs vertically and the Cross Axis runs "
                           'horizontally. 2. justify-content: This property controls distribution and alignment of '
                           "flex items along the Main Axis. Common values include 'flex-start' (items packed at the "
                           "beginning), 'center' (items centered along the axis), 'flex-end' (packed at the end), "
                           "'space-between' (items distributed with equal space between them, first and last touching "
                           "container edges), and 'space-around' / 'space-evenly'. 3. align-items: This property "
                           "controls alignment of flex items along the Cross Axis. Common values include 'stretch' "
                           "(default: items stretch to fill the container's cross-axis height/width), 'flex-start', "
                           "'center', 'flex-end', and 'baseline' (aligned by text baselines). To center a child "
                           'element perfectly both vertically and horizontally, you apply display: flex, '
                           'justify-content: center, and align-items: center.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'In Flexbox, layout alignment is governed by two perpendicular axes: the '
                                              'Main Axis and the Cross Axis. Which axis is which depends on the '
                                              "flex-direction property. In the default 'row' direction, the Main Axis "
                                              'is horizontal and the Cross Axis is vertical. The justify-content '
                                              'property always controls alignment along the Main Axis. You can use '
                                              'values like center, flex-start, flex-end, space-between, or '
                                              'space-evenly to distribute the remaining space between items along the '
                                              'row. On the other hand, align-items always controls alignment along the '
                                              'Cross Axis—which in row mode is vertical. Its values include stretch, '
                                              'center, flex-start, flex-end, and baseline. The key thing that trips '
                                              "people up is changing flex-direction to 'column': when you do that, the "
                                              'Main Axis becomes vertical and the Cross Axis becomes horizontal. So in '
                                              'column mode, justify-content suddenly controls vertical distribution, '
                                              'and align-items controls horizontal alignment.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'In flexbox, justify-content controls the alignment along the main axis, '
                                              'and align-items controls the alignment along the cross axis. By default '
                                              'in a row layout, justify-content aligns items horizontally—like using '
                                              'space-between, center, or flex-start. Align-items aligns them '
                                              'vertically, like centering an item vertically or stretching it. If you '
                                              'want to center something in both directions, you set display flex with '
                                              'justify-content center and align-items center. If you change '
                                              'flex-direction to column, their directions swap.',
                               'missing_concepts': ['align-items aligns child flex items along the Cross Axis (e.g., '
                                                    'stretch, flex-start, center, flex-end, baseline)']},
                              {'quality_level': 'average',
                               'human_score': 61,
                               'answer_text': 'Justify-content is used to align items horizontally left to right, like '
                                              'centering them or putting space between them. Align-items is used to '
                                              'align items vertically up and down. If you want to center a div inside '
                                              'another div, you put display flex, justify-content center, and '
                                              'align-items center on the parent container. If you use flex-direction '
                                              'column, it stacks items on top of each other.',
                               'missing_concepts': ['Flexbox operates on two perpendicular axes: the Main Axis and the '
                                                    'Cross Axis, determined by flex-direction (row vs column)',
                                                    "Axis swapping: When flex-direction is changed to 'column', the "
                                                    'Main Axis becomes vertical and Cross Axis becomes horizontal, '
                                                    'swapping the visual orientation controlled by each property']},
                              {'quality_level': 'poor',
                               'human_score': 26,
                               'answer_text': 'Justify-content is used for text justification like in Microsoft Word '
                                              'to make the text align on both left and right margins. Align-items is '
                                              'used for floating elements like float: left. Flexbox only works if you '
                                              'specify fixed pixel widths on every child item.',
                               'missing_concepts': ['Flexbox operates on two perpendicular axes: the Main Axis and the '
                                                    'Cross Axis, determined by flex-direction (row vs column)',
                                                    'justify-content aligns child flex items along the Main Axis '
                                                    '(e.g., flex-start, center, flex-end, space-between, space-around, '
                                                    'space-evenly)',
                                                    'align-items aligns child flex items along the Cross Axis (e.g., '
                                                    'stretch, flex-start, center, flex-end, baseline)',
                                                    "Axis swapping: When flex-direction is changed to 'column', the "
                                                    'Main Axis becomes vertical and Cross Axis becomes horizontal, '
                                                    'swapping the visual orientation controlled by each property']}]},
          {'topic_tag': 'CSS Box Model Breakdown',
           'question': 'Describe the four layers of the CSS Box Model and explain how box-sizing: border-box changes '
                       'element sizing.',
           'keywords': ['Box Model', 'Content', 'Padding', 'Border', 'Margin', 'box-sizing: border-box'],
           'expected_concepts': ['The four concentric layers of the CSS box model are: Content (text/media), Padding '
                                 '(transparent inner space), Border (drawn edge), and Margin (transparent outer '
                                 'separation)',
                                 'Default box-sizing: content-box calculates total rendered width as width + '
                                 'padding-left + padding-right + border-left + border-right',
                                 'box-sizing: border-box includes padding and border within the specified width and '
                                 "height, keeping the element's outer rendered size fixed",
                                 'Practical layout advantage: border-box prevents accidental container overflow and '
                                 'broken multi-column grid/flex layouts when padding or borders are added'],
           'model_answer': 'Every HTML element rendered in a browser is represented as a rectangular box defined by '
                           'the CSS Box Model, composed of four concentric layers from inside out: 1. Content: The '
                           'innermost area where text, images, or child elements reside. Its dimensions are determined '
                           "by the 'width' and 'height' properties. 2. Padding: The transparent spacing immediately "
                           'surrounding the content area, creating breathing room between content and the border. 3. '
                           'Border: The line wrapping around the padding and content, styled with width, style, and '
                           'color properties. 4. Margin: The outermost transparent clearance area separating the '
                           "element from neighboring elements. Crucially, the calculation of an element's total "
                           "rendered width depends on the 'box-sizing' property: Under the default 'content-box', "
                           "declaring 'width: 200px', 'padding: 20px', and 'border: 5px solid' yields an actual "
                           "rendered width of 200 + 40 + 10 = 250px. Adding padding expands the element's physical "
                           "footprint, frequently breaking responsive grid layouts. When using 'box-sizing: "
                           "border-box', the specified 'width' includes both padding and border; the browser "
                           'automatically shrinks the inner content area (to 200 - 40 - 10 = 150px) so the total '
                           'rendered box remains exactly 200px. This predictable behavior is why modern CSS resets '
                           "typically apply '* { box-sizing: border-box; }' universally.",
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'The CSS Box Model consists of four nested layers: 1. Content: the '
                                              'actual text, image, or child elements. 2. Padding: the clear space '
                                              'between the content and the border. 3. Border: the outline wrapping '
                                              'around the padding. 4. Margin: the outer space that separates this '
                                              'element from adjacent elements in the layout. The key difference with '
                                              "box-sizing comes down to how the browser calculates an element's total "
                                              "rendered width. By default, the browser uses 'box-sizing: content-box'. "
                                              'In this mode, if you specify width: 300px, padding: 20px, and border: '
                                              '5px, the total width on screen is 300 + 40 + 10 = 350px. That means '
                                              'adding padding or borders expands the box and often causes child '
                                              "elements to overflow or break grid columns. When you set 'box-sizing: "
                                              "border-box', the width you declare is the total outer width including "
                                              'the border and padding. So for a 300px box, the browser automatically '
                                              'reduces the content area to 250px so the entire element stays exactly '
                                              "300px. That's why almost every modern CSS reset applies 'box-sizing: "
                                              "border-box' across all elements using the universal selector.",
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 82,
                               'answer_text': 'The CSS box model has four layers: content at the center, padding '
                                              'around the content, border around the padding, and margin on the '
                                              'outside to push other elements away. With the default content-box, when '
                                              'you set a width of 100px and add 10px of padding on both sides, the '
                                              'total width becomes 120px because padding is added on top of width. But '
                                              'with box-sizing: border-box, the padding and border are included inside '
                                              "the 100px width, so the element doesn't expand unexpectedly. This makes "
                                              'building layouts much easier.',
                               'missing_concepts': ['Practical layout advantage: border-box prevents accidental '
                                                    'container overflow and broken multi-column grid/flex layouts when '
                                                    'padding or borders are added']},
                              {'quality_level': 'average',
                               'human_score': 61,
                               'answer_text': 'The box model has content, padding, border, and margin. Padding is '
                                              'inside the border, and margin is outside the border. Box-sizing '
                                              "border-box makes it so that when you add padding, it doesn't make the "
                                              'box bigger than the width you specified. Under normal CSS, if you add '
                                              'padding, the element grows wider and can push other elements down the '
                                              'page. So developers use border-box to keep boxes at fixed sizes.',
                               'missing_concepts': ['Default box-sizing: content-box calculates total rendered width '
                                                    'as width + padding-left + padding-right + border-left + '
                                                    'border-right',
                                                    'Practical layout advantage: border-box prevents accidental '
                                                    'container overflow and broken multi-column grid/flex layouts when '
                                                    'padding or borders are added']},
                              {'quality_level': 'poor',
                               'human_score': 26,
                               'answer_text': 'The CSS box model is used to create 3D shadow boxes using box-shadow. '
                                              'The four layers are red, green, blue, and alpha channels. Border-box '
                                              'turns the div into an HTML table with rounded corners, while '
                                              'content-box turns it into an SVG canvas.',
                               'missing_concepts': ['The four concentric layers of the CSS box model are: Content '
                                                    '(text/media), Padding (transparent inner space), Border (drawn '
                                                    'edge), and Margin (transparent outer separation)',
                                                    'Default box-sizing: content-box calculates total rendered width '
                                                    'as width + padding-left + padding-right + border-left + '
                                                    'border-right',
                                                    'box-sizing: border-box includes padding and border within the '
                                                    "specified width and height, keeping the element's outer rendered "
                                                    'size fixed',
                                                    'Practical layout advantage: border-box prevents accidental '
                                                    'container overflow and broken multi-column grid/flex layouts when '
                                                    'padding or borders are added']}]},
          {'topic_tag': 'Primitive vs Reference JavaScript Types',
           'question': 'How does JavaScript handle Primitive Data Types versus Reference Data Types in memory '
                       'allocation?',
           'keywords': ['Primitive Types',
                        'Reference Types',
                        'Value vs Reference',
                        'Stack vs Heap',
                        'Immutability',
                        'Memory Allocation'],
           'expected_concepts': ['Primitive types (string, number, boolean, undefined, null, symbol, bigint) are '
                                 'immutable and stored directly by value in call stack memory',
                                 'Reference types (objects, arrays, functions) are mutable and allocated in the heap '
                                 'memory; variables hold a reference/pointer to the heap address stored on the stack',
                                 'Copying behavior: Copying a primitive copies the literal value; copying a reference '
                                 'copies the memory address pointer, so mutating one affects both',
                                 'Equality comparisons: Primitive comparison (===) checks value equality; reference '
                                 'comparison (===) checks memory reference identity, not structural equality'],
           'model_answer': 'In JavaScript, data types are divided into two fundamental memory categories: Primitive '
                           'Types and Reference Types. 1. Primitive Types: These include string, number, boolean, '
                           'undefined, null, symbol, and bigint. Primitives are immutable and have a fixed memory '
                           'footprint. In V8 and JavaScript engines, they are stored directly on the call stack (or '
                           'optimized inline within execution contexts). When you assign a primitive to a new variable '
                           '(let b = a), JavaScript creates an entirely independent copy of the value in stack memory; '
                           "modifying 'b' has zero effect on 'a'. 2. Reference Types: These encompass Objects, Arrays, "
                           'and Functions. Because reference types are dynamically sized and mutable, their actual '
                           'data payload is allocated on the heap memory. The variable on the stack merely holds a '
                           'reference—a memory address pointer—directing the engine to the heap location. When you '
                           'assign a reference type to a new variable (let obj2 = obj1), JavaScript only copies the '
                           'pointer on the stack, not the underlying heap object. Consequently, both variables point '
                           'to the identical heap address; modifying a property via obj2.x = 5 instantly mutates the '
                           'object visible through obj1.x. Furthermore, strict equality (===) between primitives '
                           "compares actual values ('hello' === 'hello'), whereas for reference types it checks "
                           'whether both operands point to the exact same heap address ({a:1} !== {a:1}).',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 97,
                               'answer_text': 'In JavaScript, memory allocation and assignment behavior differ '
                                              'fundamentally between primitives and reference types. Primitive '
                                              'types—numbers, strings, booleans, null, undefined, symbols, and '
                                              'bigints—are immutable and have fixed sizes. They are stored directly on '
                                              'the execution stack. When you assign a primitive to another variable, '
                                              'it copies the actual value. If I do let x = 10; let y = x; y = 20; x is '
                                              'still 10 because y received a completely separate copy on the stack. In '
                                              'contrast, reference types—which are objects, arrays, and functions—are '
                                              'mutable and can grow dynamically. Their contents are stored on the heap '
                                              'memory, while the variable on the stack simply holds a pointer '
                                              'containing the heap memory address. When you assign an object to '
                                              "another variable, say let b = a, you're only copying the memory address "
                                              'on the stack. Both variables now point to the exact same object in the '
                                              "heap. So if you do b.name = 'Alice', a.name also changes to 'Alice'. "
                                              'This also explains equality comparisons: primitives are compared by '
                                              "their value, but objects are compared by reference. That's why {} === "
                                              '{} evaluates to false, because they are two separate objects allocated '
                                              'at different heap addresses.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 82,
                               'answer_text': 'Primitive types like numbers, strings, and booleans are stored by value '
                                              'on the stack. When you copy a primitive variable, JavaScript makes an '
                                              "independent copy of the value, so changing one variable doesn't affect "
                                              'the other. Reference types like objects and arrays are stored on the '
                                              'heap, and the variable on the stack just stores a pointer to that '
                                              'memory address. If you copy an object variable, you copy the reference '
                                              'pointer. So both variables point to the same object, and modifying one '
                                              'will modify both. Also, comparing two objects with triple equals checks '
                                              'if they point to the same reference.',
                               'missing_concepts': ['Primitive types (string, number, boolean, undefined, null, '
                                                    'symbol, bigint) are immutable and stored directly by value in '
                                                    'call stack memory']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'Primitives are basic types like string, number, and boolean. Reference '
                                              'types are objects and arrays. Primitives are stored in stack memory and '
                                              'reference types are stored in heap memory. When you copy a primitive, '
                                              'it copies the value. When you copy an object, it copies the reference, '
                                              'so if you edit the second object, the first one also changes unless you '
                                              'do a deep copy like JSON.parse(JSON.stringify()).',
                               'missing_concepts': ['Primitive types (string, number, boolean, undefined, null, '
                                                    'symbol, bigint) are immutable and stored directly by value in '
                                                    'call stack memory',
                                                    'Equality comparisons: Primitive comparison (===) checks value '
                                                    'equality; reference comparison (===) checks memory reference '
                                                    'identity, not structural equality']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'Primitive types are older types from ES5 that use 8-bit memory, while '
                                              'reference types are modern ES6 classes that use 64-bit memory. '
                                              'Primitives cannot be used in functions. Reference types are called '
                                              "reference types because you have to reference them using the 'this' "
                                              'keyword.',
                               'missing_concepts': ['Primitive types (string, number, boolean, undefined, null, '
                                                    'symbol, bigint) are immutable and stored directly by value in '
                                                    'call stack memory',
                                                    'Reference types (objects, arrays, functions) are mutable and '
                                                    'allocated in the heap memory; variables hold a reference/pointer '
                                                    'to the heap address stored on the stack',
                                                    'Copying behavior: Copying a primitive copies the literal value; '
                                                    'copying a reference copies the memory address pointer, so '
                                                    'mutating one affects both',
                                                    'Equality comparisons: Primitive comparison (===) checks value '
                                                    'equality; reference comparison (===) checks memory reference '
                                                    'identity, not structural equality']}]},
          {'topic_tag': 'var vs let vs const Scope',
           'question': 'What are the scoping, hoisting, and re-assignment differences between var, let, and const in '
                       'modern JavaScript?',
           'keywords': ['var', 'let', 'const', 'Block Scope', 'Function Scope', 'Hoisting'],
           'expected_concepts': ["Scope: 'var' is function-scoped (or globally scoped), leaking outside of "
                                 "if-statements and loops; 'let' and 'const' are strictly block-scoped (bounded by "
                                 'curly braces {})',
                                 "Hoisting: 'var' declarations are hoisted and initialized to 'undefined'; 'let' and "
                                 "'const' declarations are hoisted but remain uninitialized in the Temporal Dead Zone "
                                 '(TDZ) until evaluation',
                                 "Re-assignment / Mutation: 'var' and 'let' can be reassigned; 'const' cannot be "
                                 'reassigned (immutable binding), though the internal contents of const objects/arrays '
                                 'can still be mutated',
                                 "Global object attachment: In browser environments, global 'var' attaches as a "
                                 "property on 'window', while global 'let' and 'const' do not pollute window"],
           'model_answer': "In modern ECMAScript, 'var', 'let', and 'const' differ across three fundamental axes: 1. "
                           "Scope: 'var' declarations are function-scoped. If declared inside an if-statement or "
                           "for-loop, a 'var' variable leaks outside that block into the surrounding function or "
                           "global scope. Conversely, 'let' and 'const' are block-scoped, meaning their visibility is "
                           'strictly confined within the nearest enclosing curly braces {}. 2. Hoisting and Temporal '
                           'Dead Zone (TDZ): All variable declarations are hoisted to the top of their enclosing scope '
                           "during the compilation phase. However, 'var' is hoisted and automatically initialized with "
                           "the value 'undefined'; accessing a 'var' before its line of declaration returns "
                           "'undefined' without throwing an error. In contrast, 'let' and 'const' are hoisted but left "
                           'uninitialized in the Temporal Dead Zone (TDZ). Attempting to read or write a let/const '
                           'variable before its declaration line throws a runtime ReferenceError. 3. Re-assignment and '
                           "Mutation: 'var' allows both redeclaration and reassignment. 'let' prevents redeclaration "
                           "within the same scope but allows reassignment (let x = 1; x = 2). 'const' creates an "
                           'immutable binding—it must be initialized at declaration and cannot be reassigned (const x '
                           "= 1; x = 2 throws TypeError). However, 'const' does not make data structures immutable: "
                           'you can mutate properties of a const object or push elements into a const array.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'The differences between var, let, and const come down to scoping, '
                                              'hoisting behavior, and reassignment rules. First, scoping: var is '
                                              'function-scoped. If you declare a var inside an if-statement or a '
                                              'for-loop, it leaks out into the enclosing function or global scope. Let '
                                              'and const are block-scoped, so they are contained strictly within the '
                                              'curly braces where they were defined. Second, hoisting: while all three '
                                              'are hoisted during compilation, var is hoisted and initialized to '
                                              "'undefined'. So if you log a var before declaring it, you get "
                                              'undefined. Let and const are hoisted but kept in the Temporal Dead Zone '
                                              '(TDZ) without initialization; accessing them before declaration throws '
                                              'a ReferenceError. Third, reassignment: var can be redeclared and '
                                              'reassigned. Let cannot be redeclared in the same scope, but it can be '
                                              'reassigned. Const cannot be reassigned or redeclared—it must be '
                                              'initialized immediately. But note that const is about the variable '
                                              'binding, not object immutability: you can still mutate properties on a '
                                              'const object or push items into a const array. Also, at the global '
                                              'level in browsers, var attaches itself as a property on the window '
                                              'object, while let and const do not.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'Var is function-scoped, whereas let and const are block-scoped to the '
                                              'nearest curly braces. When it comes to hoisting, var is hoisted and '
                                              'gets initialized to undefined, so accessing it early returns undefined. '
                                              'Let and const are hoisted too, but you cannot access them before the '
                                              'declaration because of the Temporal Dead Zone, which throws an error. '
                                              'For reassignment, let can be reassigned but const cannot be reassigned. '
                                              'With const objects, you can still modify properties inside the object, '
                                              "you just can't point the variable to a new object.",
                               'missing_concepts': ["Global object attachment: In browser environments, global 'var' "
                                                    "attaches as a property on 'window', while global 'let' and "
                                                    "'const' do not pollute window"]},
                              {'quality_level': 'average',
                               'human_score': 61,
                               'answer_text': 'Var is the old way to define variables in JavaScript and let and const '
                                              'are from ES6. Var has function scope, while let and const have block '
                                              'scope. Let allows you to change the value later, like in a counter in a '
                                              'loop, while const cannot be changed once assigned. Var gets hoisted to '
                                              "the top so it doesn't give an error if you use it before declaring it, "
                                              'but let and const will give an error if used before definition.',
                               'missing_concepts': ["Hoisting: 'var' declarations are hoisted and initialized to "
                                                    "'undefined'; 'let' and 'const' declarations are hoisted but "
                                                    'remain uninitialized in the Temporal Dead Zone (TDZ) until '
                                                    'evaluation',
                                                    "Global object attachment: In browser environments, global 'var' "
                                                    "attaches as a property on 'window', while global 'let' and "
                                                    "'const' do not pollute window"]},
                              {'quality_level': 'poor',
                               'human_score': 26,
                               'answer_text': 'Var is used for numbers, let is used for strings, and const is used for '
                                              'constants. Var is fast, let is slower, and const uses read-only hard '
                                              'drive memory. Const completely prevents any property from ever being '
                                              'added to an object.',
                               'missing_concepts': ["Scope: 'var' is function-scoped (or globally scoped), leaking "
                                                    "outside of if-statements and loops; 'let' and 'const' are "
                                                    'strictly block-scoped (bounded by curly braces {})',
                                                    "Hoisting: 'var' declarations are hoisted and initialized to "
                                                    "'undefined'; 'let' and 'const' declarations are hoisted but "
                                                    'remain uninitialized in the Temporal Dead Zone (TDZ) until '
                                                    'evaluation',
                                                    "Re-assignment / Mutation: 'var' and 'let' can be reassigned; "
                                                    "'const' cannot be reassigned (immutable binding), though the "
                                                    'internal contents of const objects/arrays can still be mutated',
                                                    "Global object attachment: In browser environments, global 'var' "
                                                    "attaches as a property on 'window', while global 'let' and "
                                                    "'const' do not pollute window"]}]},
          {'topic_tag': 'JavaScript Event Loop Single Thread',
           'question': 'How does the single-threaded JavaScript Event Loop execute non-blocking asynchronous '
                       'callbacks?',
           'keywords': ['Event Loop',
                        'Single Thread',
                        'Call Stack',
                        'Callback Queue',
                        'Non-Blocking I/O',
                        'Asynchronous Execution'],
           'expected_concepts': ['JavaScript runtime has a single call stack executing synchronous code one frame at a '
                                 'time (run-to-completion)',
                                 'Asynchronous operations (setTimeout, fetch, DOM events) are offloaded to host '
                                 'browser Web APIs (or Node C++ worker threads)',
                                 'When asynchronous operations finish, their callbacks are queued: microtasks (Promise '
                                 'then/catch, queueMicrotask) vs macrotasks/task queue (setTimeout, setInterval, I/O)',
                                 'Event Loop mechanism: When the Call Stack is empty, it processes ALL queued '
                                 'microtasks first, then dequeues one macrotask from the Task Queue, repeating '
                                 'continuously'],
           'model_answer': 'JavaScript is a single-threaded language, meaning it possesses a single Call Stack and can '
                           'execute only one instruction at a time under a run-to-completion model. To achieve '
                           'non-blocking concurrency without locking the main thread, the JavaScript engine relies on '
                           'the Event Loop and host environment Web APIs. When an asynchronous operation is '
                           'encountered—such as setTimeout, a network fetch(), or a DOM event listener—the Call Stack '
                           "offloads the operation to the browser's Web API environment. The main thread immediately "
                           'continues executing subsequent synchronous lines. When the Web API completes its '
                           'background work (e.g., the timer fires or the HTTP response arrives), it pushes the '
                           'associated callback function into one of two queues: 1. Microtask Queue: Handles Promise '
                           'callbacks (.then(), .catch(), .finally()), async/await resumptions, and queueMicrotask(). '
                           '2. Task Queue (Macrotask Queue): Handles setTimeout, setInterval, setImmediate, and UI '
                           "rendering events. The Event Loop's job is to continually monitor the Call Stack. The "
                           'moment the Call Stack is completely empty, the Event Loop first drains the entire '
                           'Microtask Queue to completion (including any new microtasks queued during execution). Only '
                           'when the microtask queue is entirely empty does the Event Loop take the oldest callback '
                           'from the Macrotask Queue and push it onto the Call Stack to execute.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 97,
                               'answer_text': 'JavaScript is single-threaded, meaning it has one call stack and '
                                              'executes one frame at a time. The reason it can handle non-blocking '
                                              'asynchronous I/O is because of the event loop working in conjunction '
                                              'with browser Web APIs. When you call an asynchronous function like '
                                              'setTimeout or fetch(), the call stack hands off the timer or network '
                                              "request to the browser's C++ Web API threads in the background. The "
                                              'JavaScript call stack is freed up immediately to keep running '
                                              'synchronous code. Once the background timer finishes or network '
                                              'response comes back, the Web API puts the callback into a queue. There '
                                              'are actually two queues: the microtask queue for Promise callbacks and '
                                              'async/await resumptions, and the macrotask queue for things like '
                                              "setTimeout and setInterval. The event loop's job is a continuous "
                                              'while-loop checking if the call stack is empty. When the stack is '
                                              'empty, it drains all pending microtasks first. If running a microtask '
                                              'schedules another microtask, it runs that too until the microtask queue '
                                              'is completely dry. Only then does it pop one macrotask from the task '
                                              'queue onto the call stack, render UI changes if needed, and repeat the '
                                              'cycle.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'JavaScript runs on a single thread with one call stack. When you call '
                                              'something asynchronous like setTimeout or fetch, the browser handles '
                                              "the waiting in the background using Web APIs so the main thread isn't "
                                              'blocked. Once the task finishes, its callback function is pushed into '
                                              'the callback queue. The event loop constantly checks if the call stack '
                                              'is empty. As soon as the stack is empty, it takes the callback from the '
                                              'queue and pushes it onto the call stack to run. Microtasks from '
                                              'Promises have higher priority than macrotasks like setTimeout.',
                               'missing_concepts': ['Event Loop mechanism: When the Call Stack is empty, it processes '
                                                    'ALL queued microtasks first, then dequeues one macrotask from the '
                                                    'Task Queue, repeating continuously']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'The event loop makes JavaScript feel multi-threaded even though it only '
                                              'has one thread. When you run an async function or setTimeout, it '
                                              "doesn't block the page. The browser waits for the timer to finish and "
                                              'puts the callback in a callback queue. When the call stack finishes '
                                              'running all the normal JavaScript code, the event loop picks up the '
                                              'callbacks from the queue and runs them one by one. This is how '
                                              'async/await works without freezing the browser.',
                               'missing_concepts': ['Asynchronous operations (setTimeout, fetch, DOM events) are '
                                                    'offloaded to host browser Web APIs (or Node C++ worker threads)',
                                                    'When asynchronous operations finish, their callbacks are queued: '
                                                    'microtasks (Promise then/catch, queueMicrotask) vs '
                                                    'macrotasks/task queue (setTimeout, setInterval, I/O)']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'The event loop is a while-true loop that spawns new CPU threads for '
                                              'every setTimeout callback. JavaScript is multi-threaded in Chrome but '
                                              'single-threaded in Firefox. When you call async/await, JavaScript '
                                              'pauses the entire operating system thread until the database query '
                                              'returns.',
                               'missing_concepts': ['JavaScript runtime has a single call stack executing synchronous '
                                                    'code one frame at a time (run-to-completion)',
                                                    'Asynchronous operations (setTimeout, fetch, DOM events) are '
                                                    'offloaded to host browser Web APIs (or Node C++ worker threads)',
                                                    'When asynchronous operations finish, their callbacks are queued: '
                                                    'microtasks (Promise then/catch, queueMicrotask) vs '
                                                    'macrotasks/task queue (setTimeout, setInterval, I/O)',
                                                    'Event Loop mechanism: When the Call Stack is empty, it processes '
                                                    'ALL queued microtasks first, then dequeues one macrotask from the '
                                                    'Task Queue, repeating continuously']}]},
          {'topic_tag': 'DOM Selection Methods',
           'question': 'Compare document.getElementById with document.querySelector in terms of performance and '
                       'flexibility.',
           'keywords': ['getElementById', 'querySelector', 'DOM Tree', 'NodeList', 'HTMLCollection', 'Performance'],
           'expected_concepts': ['Flexibility: getElementById only matches elements by their literal ID string; '
                                 'querySelector matches any valid CSS selector (classes, pseudo-classes, attribute '
                                 'selectors, descendant combinators)',
                                 'Performance: getElementById is significantly faster because browsers maintain an '
                                 'internal hash table mapping ID strings directly to DOM nodes; querySelector must '
                                 'parse and execute the CSS selector engine',
                                 'Return types for multi-element queries: getElementsByClassName/TagName returns a '
                                 'live HTMLCollection; querySelectorAll returns a static (non-live) NodeList',
                                 'Scope: getElementById exists only on the document object; '
                                 'querySelector/querySelectorAll exists on both document and any individual Element '
                                 'node'],
           'model_answer': "Comparing 'document.getElementById' and 'document.querySelector' highlights a classic "
                           'trade-off between raw lookup performance and CSS selector flexibility: 1. Flexibility: '
                           "'document.getElementById(id)' is strictly limited to selecting a single element matching a "
                           "plain ID attribute string. In contrast, 'document.querySelector(selector)' is vastly more "
                           'flexible: it accepts any valid CSS selector, including class names (.btn), attribute '
                           "selectors (input[type='text']), combinators (div > ul li:first-child), and complex "
                           'pseudo-classes. Furthermore, querySelector can be called on any Element node '
                           '(element.querySelector) to scope searches within subtrees, whereas getElementById exists '
                           "solely on the global 'document' interface. 2. Performance: 'getElementById' is orders of "
                           'magnitude faster in benchmarks. Web browsers maintain an internal hash map indexing ID '
                           'attributes directly to their corresponding DOM node references, executing in near O(1) '
                           "time. Conversely, 'querySelector' invokes the browser's CSS selector engine to parse the "
                           'selector string and traverse the DOM tree, introducing parsing and evaluation overhead. 3. '
                           "Return types: When querying multiple elements, 'getElementsByClassName' or "
                           "'getElementsByTagName' returns a live HTMLCollection that dynamically updates when DOM "
                           "mutations occur, whereas 'querySelectorAll' returns a static (snapshot) NodeList that does "
                           'not auto-update when the DOM changes.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'The choice between document.getElementById and document.querySelector '
                                              'comes down to performance versus selector flexibility. In terms of '
                                              'flexibility, querySelector is much more powerful because it accepts any '
                                              'standard CSS selector string. You can select by class, by attribute '
                                              "like input[type='email'], by descendant hierarchy like 'nav > ul "
                                              "li.active', or by pseudo-selectors. You can also call querySelector on "
                                              'any DOM element to search just inside that subtree, whereas '
                                              'getElementById only exists on the document object. On the other hand, '
                                              'getElementById is significantly faster. Browsers maintain an internal '
                                              'hash map of element IDs to DOM references, so getElementById is '
                                              'practically an O(1) lookup. QuerySelector has to parse the selector '
                                              "string and run it through the browser's CSS query engine. A related "
                                              'difference to note when querying multiple items is that '
                                              'getElementsByClassName returns a live HTMLCollection that updates '
                                              'automatically if the DOM changes, while querySelectorAll returns a '
                                              "static NodeList snapshot that doesn't change when elements are added or "
                                              'removed.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'Document.getElementById takes an ID string and returns that single '
                                              'element. It is very fast because the browser has an internal lookup '
                                              'table mapping IDs to elements. Document.querySelector is much more '
                                              'flexible because it uses CSS selector syntax, so you can select by '
                                              "class name, tag, or complex selector like 'div.card > button'. It's "
                                              'slightly slower because the browser has to parse the CSS selector. '
                                              'Also, querySelector can be called on child elements, while '
                                              'getElementById can only be called on document.',
                               'missing_concepts': ['Return types for multi-element queries: '
                                                    'getElementsByClassName/TagName returns a live HTMLCollection; '
                                                    'querySelectorAll returns a static (non-live) NodeList']},
                              {'quality_level': 'average',
                               'human_score': 61,
                               'answer_text': 'GetElementById gets an element by its ID attribute, so you pass '
                                              "'my-btn'. QuerySelector is newer and uses CSS style selectors, so you "
                                              "have to pass '#my-btn' with a hash symbol. GetElementById is faster for "
                                              'IDs, but querySelector is more popular nowadays because you can also '
                                              "use it for classes like '.container' and tags like 'p'. "
                                              'QuerySelectorAll gets all matching elements instead of just the first '
                                              'one.',
                               'missing_concepts': ['Performance: getElementById is significantly faster because '
                                                    'browsers maintain an internal hash table mapping ID strings '
                                                    'directly to DOM nodes; querySelector must parse and execute the '
                                                    'CSS selector engine',
                                                    'Return types for multi-element queries: '
                                                    'getElementsByClassName/TagName returns a live HTMLCollection; '
                                                    'querySelectorAll returns a static (non-live) NodeList']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'GetElementById is deprecated in HTML5 because IDs are no longer '
                                              'supported in modern web development. QuerySelector is used to run SQL '
                                              'queries against the client-side database. It returns a JSON object '
                                              'rather than a DOM node.',
                               'missing_concepts': ['Flexibility: getElementById only matches elements by their '
                                                    'literal ID string; querySelector matches any valid CSS selector '
                                                    '(classes, pseudo-classes, attribute selectors, descendant '
                                                    'combinators)',
                                                    'Performance: getElementById is significantly faster because '
                                                    'browsers maintain an internal hash table mapping ID strings '
                                                    'directly to DOM nodes; querySelector must parse and execute the '
                                                    'CSS selector engine',
                                                    'Return types for multi-element queries: '
                                                    'getElementsByClassName/TagName returns a live HTMLCollection; '
                                                    'querySelectorAll returns a static (non-live) NodeList',
                                                    'Scope: getElementById exists only on the document object; '
                                                    'querySelector/querySelectorAll exists on both document and any '
                                                    'individual Element node']}]},
          {'topic_tag': 'HTTP Methods Semantics',
           'question': 'What are the semantic definitions and idempotency guarantees of GET, POST, PUT, and DELETE '
                       'HTTP methods?',
           'keywords': ['GET', 'POST', 'PUT', 'DELETE', 'Idempotency', 'Request Body'],
           'expected_concepts': ['Safe methods: Methods that do not alter server state (read-only operations); GET is '
                                 'both safe and idempotent',
                                 'Idempotency: An operation is idempotent if executing it N times produces the '
                                 'identical server state as executing it once; GET, PUT, and DELETE are idempotent; '
                                 'POST is not',
                                 'Semantic roles: GET retrieves resources; POST creates a new subordinate resource; '
                                 'PUT creates or replaces a resource in its entirety at a specific URI; DELETE removes '
                                 'a resource',
                                 'PUT vs POST / PATCH distinction: PUT requires sending the full resource payload for '
                                 'replacement, whereas PATCH performs partial updates and POST delegates URI '
                                 'generation to the server'],
           'model_answer': 'In HTTP/1.1 (RFC 7231 and RFC 9110), HTTP request methods are classified by their semantic '
                           "purpose, safety, and idempotency guarantees: 1. Safety: A method is 'safe' if it "
                           'represents a read-only retrieval that produces no side effects on server state. GET (and '
                           'HEAD) are safe methods; clients can invoke them repeatedly without altering server data. '
                           'POST, PUT, and DELETE are unsafe because they modify state. 2. Idempotency: An HTTP method '
                           "is 'idempotent' if making N identical requests yields the exact same server resource state "
                           'as making a single request. 3. Specific method semantics: - GET: Used to retrieve a '
                           'representation of a resource. It is safe and idempotent. It carries no request body. - '
                           'POST: Used to submit data to be processed by the server, typically creating a new '
                           'subordinate resource under a collection URI (/users). POST is neither safe nor idempotent; '
                           'sending five identical POST requests will create five separate records with distinct IDs. '
                           '- PUT: Replaces the resource at the specified target URI in its entirety (or creates it if '
                           'it does not exist at that specific URI). PUT is idempotent because overwriting an existing '
                           'resource with identical data five times leaves the resource state identical to the first '
                           'write. (Unlike PATCH, which applies partial updates). - DELETE: Deletes the resource '
                           'identified by the target URI. DELETE is idempotent; whether you delete user 42 once or '
                           'five times, user 42 is removed and the server state remains unchanged (even if subsequent '
                           'HTTP status codes change from 200/204 to 404).',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'HTTP methods are defined by their semantic purpose and whether they are '
                                              "safe and idempotent. A 'safe' method means it does not mutate server "
                                              "state—it's purely read-only. An 'idempotent' method means executing the "
                                              'request multiple times produces the exact same server state as '
                                              'executing it just once. Here is the breakdown: 1. GET is used to '
                                              'retrieve data from a resource URI. It is both safe and idempotent. '
                                              'Calling GET /users/123 ten times changes nothing on the server. 2. POST '
                                              'is used to create a new resource or process data. It is neither safe '
                                              'nor idempotent. If you send the same POST /orders request three times, '
                                              'you will create three separate orders and charge the customer three '
                                              'times. 3. PUT is used for full replacement of a resource at a specific '
                                              'URI. It is unsafe because it modifies data, but it is idempotent. If '
                                              'you send PUT /users/123 with a full user object five times, the '
                                              'resulting database state is identical every time. 4. DELETE is used to '
                                              'remove a resource at a given URI. It is unsafe, but it is idempotent. '
                                              'Deleting user 123 once deletes the user; deleting it four more times '
                                              'leaves the user deleted. The HTTP status code might go from 204 to 404, '
                                              'but the server state remains identical.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'GET is for reading data, POST is for creating data, PUT is for updating '
                                              'or replacing a whole resource, and DELETE is for deleting a resource. '
                                              'Idempotent means that if you make the same request multiple times, the '
                                              'final result on the server is the same. GET, PUT, and DELETE are '
                                              'idempotent because getting a user, overwriting a user with PUT, or '
                                              'deleting a user results in the same state no matter how many times you '
                                              'do it. POST is not idempotent because repeating a POST request creates '
                                              'new duplicate items every time.',
                               'missing_concepts': ['Safe methods: Methods that do not alter server state (read-only '
                                                    'operations); GET is both safe and idempotent']},
                              {'quality_level': 'average',
                               'human_score': 62,
                               'answer_text': "GET retrieves data from the API and doesn't change anything on the "
                                              'server. POST creates new items in the database. PUT updates an existing '
                                              'item by replacing it, and DELETE removes the item. Idempotency means '
                                              'you can repeat the action without causing duplicate errors. GET, PUT, '
                                              'and DELETE are idempotent, but POST is not because submitting a form '
                                              'twice creates two records.',
                               'missing_concepts': ['Safe methods: Methods that do not alter server state (read-only '
                                                    'operations); GET is both safe and idempotent',
                                                    'PUT vs POST / PATCH distinction: PUT requires sending the full '
                                                    'resource payload for replacement, whereas PATCH performs partial '
                                                    'updates and POST delegates URI generation to the server']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'GET and POST are the only two real HTTP methods; PUT and DELETE are '
                                              'just aliases added in HTML5. Idempotent means the browser caches the '
                                              'data in LocalStorage. POST is safer than GET because GET passwords show '
                                              'up in the URL bar, while POST encrypts everything with SSL '
                                              'automatically.',
                               'missing_concepts': ['Safe methods: Methods that do not alter server state (read-only '
                                                    'operations); GET is both safe and idempotent',
                                                    'Idempotency: An operation is idempotent if executing it N times '
                                                    'produces the identical server state as executing it once; GET, '
                                                    'PUT, and DELETE are idempotent; POST is not',
                                                    'Semantic roles: GET retrieves resources; POST creates a new '
                                                    'subordinate resource; PUT creates or replaces a resource in its '
                                                    'entirety at a specific URI; DELETE removes a resource',
                                                    'PUT vs POST / PATCH distinction: PUT requires sending the full '
                                                    'resource payload for replacement, whereas PATCH performs partial '
                                                    'updates and POST delegates URI generation to the server']}]},
          {'topic_tag': 'HTTP Status Codes Interpretation',
           'question': 'What do 200, 201, 400, 401, 404, and 500 status codes signify in web APIs?',
           'keywords': ['200 OK',
                        '201 Created',
                        '400 Bad Request',
                        '401 Unauthorized',
                        '404 Not Found',
                        '500 Internal Error'],
           'expected_concepts': ['Status code categories: 2xx represents successful requests, 4xx represents '
                                 'client-side errors, and 5xx represents server-side errors',
                                 '200 OK indicates standard success with response payload; 201 Created indicates '
                                 'successful creation of a new resource (typically returning Location header and '
                                 'resource body)',
                                 '400 Bad Request indicates malformed syntax or schema validation failure; 401 '
                                 'Unauthorized indicates missing or invalid authentication credentials (distinguished '
                                 'from 403 Forbidden which indicates authenticated but lacking authorization)',
                                 '404 Not Found indicates the requested resource URI does not exist on the server; 500 '
                                 'Internal Server Error indicates an unhandled server-side exception or crash'],
           'model_answer': 'HTTP response status codes are standardized three-digit integers grouped into five '
                           'functional categories: 2xx (Success), 4xx (Client Errors), and 5xx (Server Errors). 1. 200 '
                           'OK: Indicates that the HTTP request succeeded. In a GET request, the payload contains the '
                           'requested resource; in a PUT or PATCH request, it often returns the updated entity '
                           'representation. 2. 201 Created: Returned primarily by POST requests to signify that the '
                           'request succeeded and resulted in the creation of a new resource. The response typically '
                           "includes a 'Location' header pointing to the URI of the newly created resource and the "
                           'entity in the body. 3. 400 Bad Request: Indicates that the server cannot process the '
                           'request due to perceived client error, such as malformed JSON syntax, invalid query '
                           'parameters, or payload validation failures. 4. 401 Unauthorized: Indicates that the '
                           'request lacks valid authentication credentials. The user must authenticate (e.g., via '
                           'Bearer token, session cookie, or basic auth) before retrying. Note: Despite its name, 401 '
                           "strictly means 'unauthenticated'; 403 Forbidden means 'unauthorized' (the server knows who "
                           'you are, but you lack sufficient permissions). 5. 404 Not Found: Signifies that the server '
                           'cannot find a resource matching the requested URI. 6. 500 Internal Server Error: A generic '
                           'error indicating that the server encountered an unexpected exception, bug, or database '
                           'crash that prevented it from fulfilling the request.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'HTTP status codes are divided into 100-level categories: 2xx is '
                                              'success, 4xx is client error, and 5xx is server error. Here is what '
                                              'each specific code represents: 1. 200 OK: The standard success code for '
                                              'GET, PUT, or DELETE requests when the operation succeeded and returns '
                                              'data. 2. 201 Created: Used after a successful POST request when a new '
                                              'resource was actually created in the database, often returning the '
                                              'newly created object and a Location header. 3. 400 Bad Request: The '
                                              'client sent invalid data—like malformed JSON, a missing required field, '
                                              'or failing input validation rules. 4. 401 Unauthorized: This '
                                              "specifically means unauthenticated. The client either didn't send an "
                                              'auth token or sent an expired/invalid token. (If they are authenticated '
                                              'but lack permissions, you should return 403 Forbidden instead). 5. 404 '
                                              'Not Found: The requested endpoint or resource ID does not exist on the '
                                              'server. 6. 500 Internal Server Error: The server crashed or encountered '
                                              'an unhandled exception, like an uncaught TypeError or database '
                                              'connection timeout.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': '200 means OK, meaning the request was successful and data is returned. '
                                              '201 Created is returned when a POST request successfully creates a new '
                                              'record. 400 Bad Request means the client sent bad input or invalid '
                                              'JSON. 401 Unauthorized means the user is not logged in or the token is '
                                              'missing. 404 Not Found means the URL path or ID does not exist. 500 '
                                              'Internal Server Error means an error occurred on the server side like a '
                                              'crash or bug.',
                               'missing_concepts': ['Status code categories: 2xx represents successful requests, 4xx '
                                                    'represents client-side errors, and 5xx represents server-side '
                                                    'errors']},
                              {'quality_level': 'average',
                               'human_score': 61,
                               'answer_text': '200 is success for when a web page or API call works. 201 means '
                                              'created, used for POST calls when you add a user. 400 is bad request if '
                                              "you send bad data. 401 means unauthorized so you don't have permission "
                                              'to view the page. 404 is page not found. 500 is server error when the '
                                              'backend code breaks.',
                               'missing_concepts': ['Status code categories: 2xx represents successful requests, 4xx '
                                                    'represents client-side errors, and 5xx represents server-side '
                                                    'errors',
                                                    '400 Bad Request indicates malformed syntax or schema validation '
                                                    'failure; 401 Unauthorized indicates missing or invalid '
                                                    'authentication credentials (distinguished from 403 Forbidden '
                                                    'which indicates authenticated but lacking authorization)']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': '200 means the server is running out of memory. 401 means the page has '
                                              "moved permanently to a new domain. 404 means the user's internet is "
                                              'disconnected. 500 means the client forgot to install NodeJS.',
                               'missing_concepts': ['Status code categories: 2xx represents successful requests, 4xx '
                                                    'represents client-side errors, and 5xx represents server-side '
                                                    'errors',
                                                    '200 OK indicates standard success with response payload; 201 '
                                                    'Created indicates successful creation of a new resource '
                                                    '(typically returning Location header and resource body)',
                                                    '400 Bad Request indicates malformed syntax or schema validation '
                                                    'failure; 401 Unauthorized indicates missing or invalid '
                                                    'authentication credentials (distinguished from 403 Forbidden '
                                                    'which indicates authenticated but lacking authorization)',
                                                    '404 Not Found indicates the requested resource URI does not exist '
                                                    'on the server; 500 Internal Server Error indicates an unhandled '
                                                    'server-side exception or crash']}]},
          {'topic_tag': 'RESTful API Principles',
           'question': 'What are the key architectural constraints of RESTful web services?',
           'keywords': ['REST',
                        'Statelessness',
                        'Resource URI',
                        'HTTP Verbs',
                        'JSON Response',
                        'Client-Server Separation'],
           'expected_concepts': ['Client-Server Separation: User interface concerns are decoupled from data storage '
                                 'concerns, allowing independent evolution of frontend and backend',
                                 'Statelessness: Each request from client to server must contain all necessary context '
                                 'and authentication; no client session state is stored on the server',
                                 'Cacheability: Responses must explicitly define themselves as cacheable or '
                                 'non-cacheable to improve network efficiency',
                                 'Uniform Interface: Resource-based URIs (nouns, not verbs), standard HTTP methods '
                                 '(GET, POST, PUT, DELETE), self-descriptive messages, and HATEOAS'],
           'model_answer': 'REST (Representational State Transfer), formulated by Roy Fielding in his 2000 doctoral '
                           'dissertation, defines six architectural constraints for scalable distributed systems: 1. '
                           'Client-Server Separation: The user interface and client concerns are completely decoupled '
                           'from data storage and server processing. This enables frontends (web, mobile, IoT) to '
                           'evolve independently of backend microservices. 2. Statelessness: The server stores no '
                           'client session context between requests. Every single request from client to server must '
                           'contain all the information necessary to understand and authenticate that request (e.g., '
                           'via JWT tokens or API keys). Statelessness enables horizontal scalability, as any server '
                           'instance can handle any incoming request. 3. Cacheability: Server responses must '
                           'explicitly label themselves as cacheable or non-cacheable (via HTTP headers like '
                           'Cache-Control and ETag) to prevent clients from reusing stale data while minimizing '
                           'redundant network roundtrips. 4. Uniform Interface: The cornerstone of REST, requiring: '
                           'resource identification via URIs using nouns rather than action verbs (/api/v1/users, not '
                           '/getUser); resource manipulation through representations (JSON/XML); self-descriptive '
                           'messages (using standard MIME types and HTTP status codes); and hypermedia as the engine '
                           'of application state (HATEOAS). 5. Layered System: The client cannot tell whether it is '
                           'connected directly to the end server or an intermediate proxy, load balancer, or CDN. 6. '
                           'Code on Demand (optional): Servers can temporarily extend client functionality by '
                           'transferring executable scripts (e.g., JavaScript).',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'REST is an architectural style defined by Roy Fielding that relies on '
                                              'several core constraints: 1. Client-Server separation: The frontend and '
                                              "backend are completely decoupled. The server doesn't care about the UI, "
                                              "and the client doesn't care about database storage, so you can build "
                                              'web, iOS, and Android clients against the exact same API. 2. '
                                              'Statelessness: This is critical—the server does not store any session '
                                              'state about the client. Every incoming HTTP request must include all '
                                              'the credentials, headers, and data necessary to fulfill it. This makes '
                                              'horizontal scaling trivial because any server behind a load balancer '
                                              'can handle any request. 3. Cacheability: Responses must specify whether '
                                              'they can be cached by the browser or CDN using headers like '
                                              'Cache-Control and ETag to reduce latency. 4. Uniform Interface: '
                                              'Resources are identified by URIs using nouns—like /users/123/orders '
                                              'instead of /getUserOrders. We use standard HTTP verbs (GET, POST, PUT, '
                                              'DELETE) to express actions, standard status codes for responses, and '
                                              'ideally HATEOAS links to navigate resources. 5. Layered system: The '
                                              'architecture can contain proxies, API gateways, and CDNs without the '
                                              'client having to know about them.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 82,
                               'answer_text': 'The main principles of REST are client-server separation, '
                                              'statelessness, cacheability, and a uniform interface. Client-server '
                                              'means the frontend and backend are separated. Statelessness means the '
                                              'server does not store session state between requests; every request '
                                              'must carry its own authentication token. Uniform interface means using '
                                              'nouns for URLs like /api/products, and using standard HTTP methods like '
                                              'GET to read and POST to create. Responses should also be cacheable when '
                                              'appropriate.',
                               'missing_concepts': ['Uniform Interface: Resource-based URIs (nouns, not verbs), '
                                                    'standard HTTP methods (GET, POST, PUT, DELETE), self-descriptive '
                                                    'messages, and HATEOAS']},
                              {'quality_level': 'average',
                               'human_score': 61,
                               'answer_text': 'RESTful APIs use HTTP requests to communicate using JSON format. The '
                                              'key rules are that you use resource URLs with nouns like /users instead '
                                              'of verbs, and you use HTTP methods like GET, POST, PUT, and DELETE for '
                                              "CRUD operations. It is also stateless, which means the server doesn't "
                                              'store session data and you have to send an auth token with every '
                                              'request. It allows frontend apps like React to talk to backend servers '
                                              'like Node or Python.',
                               'missing_concepts': ['Client-Server Separation: User interface concerns are decoupled '
                                                    'from data storage concerns, allowing independent evolution of '
                                                    'frontend and backend',
                                                    'Cacheability: Responses must explicitly define themselves as '
                                                    'cacheable or non-cacheable to improve network efficiency']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'REST stands for React Endpoint State Transfer. It requires using '
                                              'GraphQL queries over web sockets. The main rule of REST is that every '
                                              "endpoint must store user passwords in server RAM so the client doesn't "
                                              'have to log in again.',
                               'missing_concepts': ['Client-Server Separation: User interface concerns are decoupled '
                                                    'from data storage concerns, allowing independent evolution of '
                                                    'frontend and backend',
                                                    'Statelessness: Each request from client to server must contain '
                                                    'all necessary context and authentication; no client session state '
                                                    'is stored on the server',
                                                    'Cacheability: Responses must explicitly define themselves as '
                                                    'cacheable or non-cacheable to improve network efficiency',
                                                    'Uniform Interface: Resource-based URIs (nouns, not verbs), '
                                                    'standard HTTP methods (GET, POST, PUT, DELETE), self-descriptive '
                                                    'messages, and HATEOAS']}]},
          {'topic_tag': 'Browser Storage Options',
           'question': 'Compare LocalStorage, SessionStorage, and Cookies regarding capacity, expiration, and server '
                       'accessibility.',
           'keywords': ['LocalStorage', 'SessionStorage', 'Cookies', 'Expiration', 'Storage Limit', 'Domain Scope'],
           'expected_concepts': ['Capacity limits: Cookies have ~4KB limit per domain; LocalStorage and SessionStorage '
                                 'provide ~5MB to 10MB per origin',
                                 'Lifespan / Expiration: LocalStorage persists indefinitely until explicitly cleared; '
                                 'SessionStorage survives page reloads but clears when the tab/window closes; Cookies '
                                 'expire according to Expires or Max-Age attributes (or end of session if omitted)',
                                 'Server accessibility: Cookies are automatically attached and transmitted in the HTTP '
                                 'Cookie header on every request to matching domains; LocalStorage and SessionStorage '
                                 'are strictly client-side and never sent to the server automatically',
                                 'Security attributes: Cookies support HttpOnly (blocking XSS script access) and '
                                 'Secure/SameSite flags; LocalStorage/SessionStorage are accessible via JavaScript '
                                 'window.localStorage, making them vulnerable to XSS token theft'],
           'model_answer': 'Web browsers provide three primary client-side storage mechanisms with contrasting '
                           'capacities, lifecycles, and network characteristics: 1. Cookies: Capacity is limited to '
                           'approximately 4KB per domain. Cookies were designed for server-client state management: '
                           "they are automatically transmitted in the 'Cookie' HTTP request header on every single "
                           'request made to matching domains and paths. Cookies have configurable lifespans set via '
                           "'Expires' or 'Max-Age' headers; omitting them creates a session cookie deleted when the "
                           "browser closes. From a security standpoint, cookies can be protected with the 'HttpOnly' "
                           'flag (which blocks JavaScript access via document.cookie, mitigating XSS token theft), the '
                           "'Secure' flag (HTTPS only), and 'SameSite=Lax/Strict' (mitigating CSRF). 2. LocalStorage: "
                           'Provides a much larger capacity of approximately 5MB to 10MB per origin. It stores data as '
                           'key-value strings purely on the client side; data is never transmitted to the server '
                           'automatically. LocalStorage has no expiration: data persists indefinitely across browser '
                           'restarts until cleared programmatically or by the user. Because it is completely '
                           'accessible to client-side JavaScript, storing sensitive authentication tokens in '
                           "LocalStorage introduces severe XSS vulnerability. 3. SessionStorage: Shares LocalStorage's "
                           '~5MB capacity and client-only API. However, its lifespan is strictly tied to the lifetime '
                           'of the specific browser tab. Closing the tab immediately destroys the sessionStorage data, '
                           'though it survives page reloads within that tab. Data is not shared across different tabs '
                           'even if navigating to the same URL.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': "Let's compare Cookies, LocalStorage, and SessionStorage across "
                                              'capacity, expiration, and server communication. 1. Storage Capacity: '
                                              'Cookies are tiny, limited to about 4KB per domain. LocalStorage and '
                                              'SessionStorage offer significantly more space, typically 5MB to 10MB '
                                              'per origin. 2. Server Transmission: Cookies are automatically included '
                                              'in the HTTP headers of every single request sent to matching domains, '
                                              'which is why they are used for session management. LocalStorage and '
                                              'SessionStorage are strictly client-side—their data is never sent to the '
                                              'server over HTTP automatically. 3. Expiration and Lifetime: '
                                              'LocalStorage persists indefinitely until manually cleared by code or '
                                              'user cache clearing. SessionStorage persists only for the lifetime of '
                                              'that specific browser tab—refreshing the page keeps it, but closing the '
                                              'tab deletes it completely. Cookies have configurable expiration dates '
                                              'using Expires or Max-Age; if none is set, they expire when the browser '
                                              'session ends. 4. Security: Cookies can be configured with the HttpOnly '
                                              'flag, which prevents JavaScript from reading them and protects against '
                                              'XSS token theft, along with Secure and SameSite flags for CSRF '
                                              'protection. LocalStorage and SessionStorage are always accessible via '
                                              'JavaScript, meaning if your site has an XSS vulnerability, an attacker '
                                              'can trivially steal any tokens stored in them.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'Cookies have a 4KB limit and are automatically sent to the server on '
                                              'every HTTP request. They can have an expiration date set by the server. '
                                              'LocalStorage has around 5MB to 10MB of storage and persists forever '
                                              'until you clear your browser cache; it is never sent to the server '
                                              'automatically. SessionStorage also has about 5MB of storage, but it '
                                              'gets deleted as soon as you close the browser tab. A key security '
                                              'difference is that cookies can use the HttpOnly flag to prevent XSS '
                                              'attacks from reading auth tokens.',
                               'missing_concepts': ['Security attributes: Cookies support HttpOnly (blocking XSS '
                                                    'script access) and Secure/SameSite flags; '
                                                    'LocalStorage/SessionStorage are accessible via JavaScript '
                                                    'window.localStorage, making them vulnerable to XSS token theft']},
                              {'quality_level': 'average',
                               'human_score': 61,
                               'answer_text': 'Cookies are used to track user logins and have a small 4KB size limit. '
                                              'LocalStorage has 5MB of storage and keeps data permanently even if you '
                                              'restart your computer. SessionStorage also has 5MB, but it only lasts '
                                              'while the tab is open and disappears when you close the tab. Cookies '
                                              'get sent to the server with every request, but LocalStorage and '
                                              'SessionStorage stay on the client side only.',
                               'missing_concepts': ['Security attributes: Cookies support HttpOnly (blocking XSS '
                                                    'script access) and Secure/SameSite flags; '
                                                    'LocalStorage/SessionStorage are accessible via JavaScript '
                                                    'window.localStorage, making them vulnerable to XSS token theft',
                                                    'Lifespan / Expiration: LocalStorage persists indefinitely until '
                                                    'explicitly cleared; SessionStorage survives page reloads but '
                                                    'clears when the tab/window closes; Cookies expire according to '
                                                    'Expires or Max-Age attributes (or end of session if omitted)']},
                              {'quality_level': 'poor',
                               'human_score': 26,
                               'answer_text': 'LocalStorage is stored in the cloud on AWS. Cookies are stored in the '
                                              "user's RAM and have unlimited capacity. SessionStorage is an encrypted "
                                              'blockchain database built into Chrome. You should always store user '
                                              'passwords in LocalStorage because it never expires.',
                               'missing_concepts': ['Capacity limits: Cookies have ~4KB limit per domain; LocalStorage '
                                                    'and SessionStorage provide ~5MB to 10MB per origin',
                                                    'Lifespan / Expiration: LocalStorage persists indefinitely until '
                                                    'explicitly cleared; SessionStorage survives page reloads but '
                                                    'clears when the tab/window closes; Cookies expire according to '
                                                    'Expires or Max-Age attributes (or end of session if omitted)',
                                                    'Server accessibility: Cookies are automatically attached and '
                                                    'transmitted in the HTTP Cookie header on every request to '
                                                    'matching domains; LocalStorage and SessionStorage are strictly '
                                                    'client-side and never sent to the server automatically',
                                                    'Security attributes: Cookies support HttpOnly (blocking XSS '
                                                    'script access) and Secure/SameSite flags; '
                                                    'LocalStorage/SessionStorage are accessible via JavaScript '
                                                    'window.localStorage, making them vulnerable to XSS token '
                                                    'theft']}]},
          {'topic_tag': 'CSS Grid vs Flexbox Use Cases',
           'question': 'When should you use CSS Grid instead of Flexbox for building web application layouts?',
           'keywords': ['CSS Grid',
                        'Flexbox',
                        'Two-Dimensional Layout',
                        'One-Dimensional Layout',
                        'Grid Template Areas',
                        'Alignment'],
           'expected_concepts': ['Dimensionality: Flexbox is primarily a one-dimensional layout system (row OR column '
                                 'at a time); CSS Grid is a two-dimensional system (rows AND columns simultaneously)',
                                 'Layout direction: Grid is layout-first (you define the grid structure on the parent '
                                 'container and place items into cells); Flexbox is content-first (items dictate their '
                                 'own width/height and wrap)',
                                 'CSS Grid features: Supports explicit overlapping elements, grid-template-areas for '
                                 'visual page scaffolding, and minmax() / repeat(auto-fit) for responsive columns '
                                 'without media queries',
                                 'Ideal use cases: Use Grid for overall page scaffolding, photo galleries, dashboards, '
                                 'and card matrices; use Flexbox for navigation bars, button groups, and 1D component '
                                 'alignment'],
           'model_answer': 'The decision between CSS Grid and Flexbox hinges on dimensional control and layout '
                           'philosophy: 1. Dimensionality (1D vs 2D): Flexbox is fundamentally a one-dimensional '
                           'layout model. It distributes items along a single axis at a time (either horizontally as a '
                           "row or vertically as a column). While 'flex-wrap: wrap' allows items to flow onto new "
                           'lines, items on subsequent lines do not align their column boundaries with items on '
                           'previous lines. In contrast, CSS Grid is a true two-dimensional layout system that manages '
                           'rows and columns simultaneously. Grid items align strictly along both horizontal and '
                           "vertical grid tracks. 2. Layout-First vs Content-First: Grid is 'layout-first'—you define "
                           'the overall columns, rows, and grid areas on the parent container (e.g., using '
                           "'grid-template-columns: repeat(auto-fit, minmax(250px, 1fr))'), and child elements slot "
                           "into that predefined scaffold. Flexbox is 'content-first'—the dimensions and content size "
                           'of the flex items largely dictate how space is distributed. 3. Practical Use Cases: - '
                           'Choose CSS Grid for whole-page layout skeletons (header, sidebar, main content, footer via '
                           "'grid-template-areas'), complex dashboards, image galleries, and data tables where "
                           'elements must align across both axes or overlap (via z-index and shared grid lines). - '
                           'Choose Flexbox for one-dimensional UI components: navigation bars, button clusters, form '
                           'input-with-icon groupings, and centering elements inside a container.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'The rule of thumb is: Flexbox is for one-dimensional layouts, and CSS '
                                              'Grid is for two-dimensional layouts. Flexbox excels when you are laying '
                                              'out items along a single axis—either in a row or in a column. Even when '
                                              'flex items wrap to the next line with flex-wrap, each line is its own '
                                              "independent flex container, so items on row two don't line up with "
                                              'items on row one. CSS Grid, on the other hand, controls both rows and '
                                              'columns simultaneously. Every cell is anchored to both horizontal and '
                                              'vertical grid tracks. Another conceptual difference is that Grid is '
                                              "'layout-first', meaning you define the grid tracks on the parent "
                                              'container with things like grid-template-columns: repeat(auto-fit, '
                                              'minmax(200px, 1fr)), and the children slot into place. Flexbox is '
                                              "'content-first', where the size of each child item helps determine the "
                                              'layout. In practice, you should use Grid for macro-layouts—like the '
                                              'overall page structure with headers, sidebars, and main content areas, '
                                              'or photo galleries and card matrices where cards must align in both '
                                              'directions. You should use Flexbox for micro-layouts—like a navigation '
                                              'bar, a button group with an icon and text, or centering an item inside '
                                              'a card.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'You should use CSS Grid when you need a two-dimensional layout that '
                                              'controls both rows and columns at the same time. Flexbox is '
                                              'one-dimensional, meaning it aligns items along a row or along a column, '
                                              'but not both simultaneously. If flex items wrap to the next line, they '
                                              "don't align with the items above them. Grid is perfect for overall page "
                                              'layouts, like defining header, sidebar, main content, and footer using '
                                              'grid-template-areas, or for responsive card galleries. Flexbox is best '
                                              'for 1D component alignment, like navigation menus and button groups.',
                               'missing_concepts': ['Layout direction: Grid is layout-first (you define the grid '
                                                    'structure on the parent container and place items into cells); '
                                                    'Flexbox is content-first (items dictate their own width/height '
                                                    'and wrap)']},
                              {'quality_level': 'average',
                               'human_score': 61,
                               'answer_text': 'Grid is 2D and Flexbox is 1D. You use Flexbox when you want to put '
                                              'things in a single line, like buttons in a row or links in a navbar. '
                                              'You use CSS Grid when you have a grid of items with rows and columns, '
                                              'like a dashboard or an image gallery. Grid lets you define '
                                              'grid-template-columns so the items line up nicely in columns. Flexbox '
                                              'is simpler for quick alignment, while Grid is better for complex '
                                              'layouts.',
                               'missing_concepts': ['Layout direction: Grid is layout-first (you define the grid '
                                                    'structure on the parent container and place items into cells); '
                                                    'Flexbox is content-first (items dictate their own width/height '
                                                    'and wrap)',
                                                    'CSS Grid features: Supports explicit overlapping elements, '
                                                    'grid-template-areas for visual page scaffolding, and minmax() / '
                                                    'repeat(auto-fit) for responsive columns without media queries']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'CSS Grid is an outdated technology that was replaced by Flexbox in '
                                              'CSS3. You should only use Grid if you are supporting Internet Explorer '
                                              '6. Flexbox can do everything Grid does, including 3D graphics.',
                               'missing_concepts': ['Dimensionality: Flexbox is primarily a one-dimensional layout '
                                                    'system (row OR column at a time); CSS Grid is a two-dimensional '
                                                    'system (rows AND columns simultaneously)',
                                                    'Layout direction: Grid is layout-first (you define the grid '
                                                    'structure on the parent container and place items into cells); '
                                                    'Flexbox is content-first (items dictate their own width/height '
                                                    'and wrap)',
                                                    'CSS Grid features: Supports explicit overlapping elements, '
                                                    'grid-template-areas for visual page scaffolding, and minmax() / '
                                                    'repeat(auto-fit) for responsive columns without media queries',
                                                    'Ideal use cases: Use Grid for overall page scaffolding, photo '
                                                    'galleries, dashboards, and card matrices; use Flexbox for '
                                                    'navigation bars, button groups, and 1D component alignment']}]},
          {'topic_tag': 'Arrow Functions vs Traditional Functions',
           'question': "How do Arrow Functions handle the 'this' keyword and 'arguments' object differently than "
                       'traditional functions?',
           'keywords': ['Arrow Functions',
                        'Traditional Functions',
                        'this Binding',
                        'arguments Object',
                        'Constructor Function',
                        'Lexical Scope'],
           'expected_concepts': ["Lexical 'this' binding: Arrow functions do not define their own 'this'; they inherit "
                                 "'this' lexically from their enclosing execution context",
                                 "Dynamic 'this' binding: Traditional functions bind 'this' dynamically based on how "
                                 'they are called (e.g., method call, standalone function call, or call/apply/bind)',
                                 "arguments object: Traditional functions have their own local 'arguments' object "
                                 "containing passed parameters; arrow functions do not have an 'arguments' object and "
                                 'use rest parameters (...args) instead',
                                 "Constructors: Traditional functions can be invoked with 'new' to construct instances "
                                 "(possessing a 'prototype' property); arrow functions cannot be constructors and "
                                 "throw a TypeError if called with 'new'"],
           'model_answer': 'Introduced in ES6, arrow functions (() => {}) differ fundamentally from traditional '
                           'function declarations (function() {}) in how they handle context binding, arguments, and '
                           "instantiation: 1. 'this' Binding: Traditional functions define their own 'this' "
                           "dynamically at runtime based on invocation context. In a standard function call, 'this' "
                           'refers to the global object (or undefined in strict mode); in a method call (obj.fn()), '
                           "'this' refers to the calling object; and it can be explicitly rebound using '.bind()', "
                           "'.call()', or '.apply()'. Arrow functions do not have their own 'this' binding at all; "
                           "they capture 'this' lexically from their enclosing lexical context at definition time. "
                           "Calling .bind() or .call() on an arrow function cannot alter its 'this'. This makes arrow "
                           'functions ideal for callbacks (e.g., inside setTimeout or array methods) where you want to '
                           "retain the outer class or component instance. 2. 'arguments' Object: Traditional functions "
                           "expose a local, array-like 'arguments' object containing all arguments passed to the "
                           "function. Arrow functions do not possess an 'arguments' object; referencing 'arguments' "
                           "inside an arrow function simply resolves to the outer enclosing scope's arguments object. "
                           'In modern JavaScript, arrow functions use rest parameters (...args) instead. 3. '
                           "Constructor Capabilities: Traditional functions have a 'prototype' property and internal "
                           "[[Construct]] method, allowing them to be instantiated via 'new Person()'. Arrow functions "
                           "lack [[Construct]] and a prototype property; invoking an arrow function with 'new' throws "
                           'a runtime TypeError.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'The two biggest differences between arrow functions and traditional '
                                              "functions are the 'this' binding and the 'arguments' object, along with "
                                              "constructor behavior. 1. The 'this' keyword: Traditional functions "
                                              "determine 'this' dynamically at runtime based on how the function was "
                                              "called. If it's called as a method like obj.method(), 'this' is obj; if "
                                              "called standalone, 'this' is window or undefined in strict mode. You "
                                              'can also rebind it using call, apply, or bind. Arrow functions do not '
                                              "have their own 'this' at all—they inherit 'this' lexically from the "
                                              'scope where they were written. This is why arrow functions are so '
                                              'useful in callbacks like setTimeout or event listeners, because you '
                                              "don't lose the outer class or object context. 2. The 'arguments' "
                                              "object: Traditional functions have a built-in array-like 'arguments' "
                                              "object containing all passed arguments. Arrow functions don't have an "
                                              "arguments object; if you try to access 'arguments' inside an arrow "
                                              'function, it either throws an error or grabs the arguments of the '
                                              'enclosing outer traditional function. With arrow functions, you use ES6 '
                                              'rest parameters (...args) instead. 3. Constructors: Traditional '
                                              "functions can be used as constructors with the 'new' keyword because "
                                              'they have a prototype property. Arrow functions do not have a prototype '
                                              "and cannot be called with 'new'—doing so throws a TypeError.",
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': "Arrow functions handle 'this' lexically, meaning they borrow 'this' "
                                              'from the enclosing scope where the function was created. Traditional '
                                              "functions bind 'this' dynamically depending on how they are invoked, "
                                              "which is why in traditional callbacks you often had to do 'const self = "
                                              "this' or use .bind(this). For the 'arguments' object, traditional "
                                              'functions have a special arguments variable holding all parameters, '
                                              'while arrow functions do not have their own arguments object—you have '
                                              'to use rest parameters like (...args) instead. Also, arrow functions '
                                              'cannot be used as constructors with the new keyword.',
                               'missing_concepts': ["Dynamic 'this' binding: Traditional functions bind 'this' "
                                                    'dynamically based on how they are called (e.g., method call, '
                                                    'standalone function call, or call/apply/bind)']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'Arrow functions are a shorter syntax introduced in ES6 using the arrow '
                                              "=> symbol. The main difference is that arrow functions don't have their "
                                              "own 'this'. In traditional functions, 'this' changes depending on who "
                                              'calls the function, which causes bugs in callbacks. In arrow functions, '
                                              "'this' always points to the parent scope. Also, arrow functions don't "
                                              'have the arguments keyword, so you have to use rest parameters with '
                                              'three dots.',
                               'missing_concepts': ["Dynamic 'this' binding: Traditional functions bind 'this' "
                                                    'dynamically based on how they are called (e.g., method call, '
                                                    'standalone function call, or call/apply/bind)',
                                                    "Constructors: Traditional functions can be invoked with 'new' to "
                                                    "construct instances (possessing a 'prototype' property); arrow "
                                                    'functions cannot be constructors and throw a TypeError if called '
                                                    "with 'new'"]},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'Arrow functions are asynchronous and traditional functions are '
                                              "synchronous. In arrow functions, 'this' always refers to the HTML "
                                              'document. You cannot pass arguments to an arrow function because they '
                                              'take zero parameters.',
                               'missing_concepts': ["Lexical 'this' binding: Arrow functions do not define their own "
                                                    "'this'; they inherit 'this' lexically from their enclosing "
                                                    'execution context',
                                                    "Dynamic 'this' binding: Traditional functions bind 'this' "
                                                    'dynamically based on how they are called (e.g., method call, '
                                                    'standalone function call, or call/apply/bind)',
                                                    'arguments object: Traditional functions have their own local '
                                                    "'arguments' object containing passed parameters; arrow functions "
                                                    "do not have an 'arguments' object and use rest parameters "
                                                    '(...args) instead',
                                                    "Constructors: Traditional functions can be invoked with 'new' to "
                                                    "construct instances (possessing a 'prototype' property); arrow "
                                                    'functions cannot be constructors and throw a TypeError if called '
                                                    "with 'new'"]}]},
          {'topic_tag': 'Asynchronous JS: Promises & Async/Await',
           'question': 'How do JavaScript Promises and async/await simplify handling asynchronous operations compared '
                       'to callbacks?',
           'keywords': ['Promises',
                        'async/await',
                        'Promise Chains',
                        'Reject/Resolve',
                        'Error Handling',
                        'Non-blocking'],
           'expected_concepts': ["Callback limitations: Nested callbacks lead to 'callback hell' (pyramid of doom), "
                                 'fragmented error handling (err-first callbacks), and inversion of control',
                                 'Promises represent an eventual completion/failure of an asynchronous operation with '
                                 'three states: pending, fulfilled, or rejected',
                                 'Promise chaining (.then().then().catch()) flattens nested asynchronous flows and '
                                 'centralizes error handling into a single .catch() block',
                                 'async/await provides syntactic sugar over Promises, allowing developers to write '
                                 'asynchronous code with synchronous readability and standard try/catch blocks'],
           'model_answer': 'Prior to ES6, asynchronous JavaScript relied heavily on callbacks. When multiple dependent '
                           'asynchronous tasks were sequenced (e.g., fetch user, fetch user orders, fetch order '
                           "details), callbacks resulted in 'callback hell'—deeply nested code ('pyramid of doom') "
                           'that was difficult to read, debug, and maintain. Moreover, error handling was fragmented, '
                           "requiring manual checks for 'err' in every single callback, and suffered from inversion of "
                           'control where third-party libraries controlled callback execution. 1. Promises: A Promise '
                           'is an object representing the eventual result of an asynchronous operation, existing in '
                           'one of three states: pending, fulfilled (resolved with a value), or rejected (with an '
                           'error). Promises solve nesting through chaining: each .then() returns a new Promise, '
                           'allowing linear sequential flows. Unhandled rejections propagate down the chain until '
                           'caught by a single centralized .catch() block. 2. async/await (ES2017): Built on top of '
                           "Promises and Generators, async/await provides clean syntactic sugar. An 'async' function "
                           "always returns a Promise, and the 'await' keyword pauses function execution until the "
                           'Promise settles. This transforms asynchronous code into linear, synchronous-looking code, '
                           'allowing developers to use standard control flow (for-loops, if-statements) and native '
                           'try/catch blocks for intuitive error handling without blocking the main thread.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'Before Promises, handling asynchronous operations in JavaScript '
                                              'required passing callback functions. When you had several dependent '
                                              'async calls—like fetching a user, then fetching their posts, then '
                                              "fetching comments—you ended up with 'callback hell' or the pyramid of "
                                              'doom. This caused three big problems: hard-to-read nested code, '
                                              "fragmented error handling where you had to check 'if (err)' in every "
                                              'single callback, and inversion of control where an external function '
                                              'decides when and how to call your callback. Promises solved this by '
                                              'encapsulating the async operation into an object with three states: '
                                              'pending, fulfilled, or rejected. Instead of nesting, you chain .then() '
                                              'calls linearly, and any error anywhere in the chain falls through to a '
                                              'single .catch() at the bottom. Async/await took this a step further by '
                                              'providing syntactic sugar over Promises. An async function lets you use '
                                              "the 'await' keyword, which pauses the execution of that specific "
                                              'function until the Promise resolves, without blocking the browser '
                                              'thread. It lets you write asynchronous code that reads like synchronous '
                                              'code, and you can handle errors cleanly using standard try/catch '
                                              'blocks.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'Callbacks caused callback hell where code was nested five or six levels '
                                              'deep, making it hard to follow and debug. Promises improved this by '
                                              'introducing .then() and .catch() methods, so you can chain operations '
                                              'one after another in a flat structure and handle all errors in one '
                                              '.catch() block. Async/await is even better because it allows you to '
                                              'write asynchronous code using regular try/catch blocks and the await '
                                              'keyword, making it look like synchronous code while still running '
                                              'non-blocking in the background.',
                               'missing_concepts': ['Promises represent an eventual completion/failure of an '
                                                    'asynchronous operation with three states: pending, fulfilled, or '
                                                    'rejected']},
                              {'quality_level': 'average',
                               'human_score': 61,
                               'answer_text': 'Callbacks are older and when you have many callbacks inside callbacks, '
                                              "it's called callback hell. Promises fix that by using .then() to do "
                                              'things in sequence and .catch() to catch errors. Async/await is the '
                                              'newest way where you put async in front of the function and await in '
                                              'front of the fetch request. It makes the code much cleaner than using '
                                              '.then() chains and avoids deeply nested code.',
                               'missing_concepts': ["Callback limitations: Nested callbacks lead to 'callback hell' "
                                                    '(pyramid of doom), fragmented error handling (err-first '
                                                    'callbacks), and inversion of control',
                                                    'Promises represent an eventual completion/failure of an '
                                                    'asynchronous operation with three states: pending, fulfilled, or '
                                                    'rejected']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'Promises make asynchronous code run synchronously on multiple CPU '
                                              'cores. A Promise has two states: true and false. Async/await is used to '
                                              'prevent the browser from needing an internet connection during API '
                                              'calls.',
                               'missing_concepts': ["Callback limitations: Nested callbacks lead to 'callback hell' "
                                                    '(pyramid of doom), fragmented error handling (err-first '
                                                    'callbacks), and inversion of control',
                                                    'Promises represent an eventual completion/failure of an '
                                                    'asynchronous operation with three states: pending, fulfilled, or '
                                                    'rejected',
                                                    'Promise chaining (.then().then().catch()) flattens nested '
                                                    'asynchronous flows and centralizes error handling into a single '
                                                    '.catch() block',
                                                    'async/await provides syntactic sugar over Promises, allowing '
                                                    'developers to write asynchronous code with synchronous '
                                                    'readability and standard try/catch blocks']}]},
          {'topic_tag': 'CORS Security Mechanics',
           'question': 'What is Cross-Origin Resource Sharing (CORS), and why do browsers send preflight OPTIONS '
                       'requests?',
           'keywords': ['CORS',
                        'Cross-Origin Resource Sharing',
                        'Same-Origin Policy',
                        'Access-Control-Allow-Origin',
                        'Preflight Request',
                        'Headers'],
           'expected_concepts': ['Same-Origin Policy (SOP) is a core browser security mechanism that blocks client '
                                 'scripts on one origin (scheme, host, port) from accessing resources on a different '
                                 'origin',
                                 'CORS is an HTTP-header based relaxation mechanism allowing servers to declare which '
                                 'origins are permitted to access their resources (e.g., Access-Control-Allow-Origin)',
                                 'Simple requests (GET, POST, HEAD with standard headers like Content-Type: '
                                 'application/x-www-form-urlencoded or text/plain) are sent directly without preflight',
                                 "Preflight OPTIONS request is sent automatically by browsers prior to 'non-simple' "
                                 'requests (custom headers like Authorization, Content-Type: application/json, '
                                 'PUT/DELETE) to check server permissions before executing the actual request'],
           'model_answer': 'Cross-Origin Resource Sharing (CORS) is a browser security mechanism that relaxes the '
                           'strict Same-Origin Policy (SOP). Under SOP, browsers prohibit client-side scripts running '
                           'on Origin A (defined by protocol, domain, and port, e.g., https://myfrontend.com:443) from '
                           'reading HTTP response data from Origin B (e.g., https://api.backend.com:443). CORS allows '
                           'the server at Origin B to explicitly grant permission by returning response headers such '
                           "as 'Access-Control-Allow-Origin: https://myfrontend.com'. To determine safety, browsers "
                           'classify cross-origin HTTP requests into two categories: 1. Simple Requests: Requests '
                           'using GET, HEAD, or POST, containing only safe-listed headers (Accept, Accept-Language, '
                           'Content-Language) and simple Content-Types (application/x-www-form-urlencoded, '
                           'multipart/form-data, text/plain). These are dispatched directly. 2. Preflighted Requests: '
                           'Any request that could have server-side side effects or uses non-standard '
                           'configurations—including HTTP methods like PUT, DELETE, or PATCH, custom headers like '
                           "'Authorization', or 'Content-Type: application/json'—triggers an automatic preflight "
                           "request. Before sending the actual request, the browser sends an HTTP 'OPTIONS' request "
                           "with 'Origin', 'Access-Control-Request-Method', and 'Access-Control-Request-Headers'. The "
                           "server must respond with 200/204 and appropriate 'Access-Control-Allow-*' headers. Only if "
                           'the preflight succeeds does the browser dispatch the actual payload, protecting legacy '
                           'servers from unintended state modifications.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': "CORS stands for Cross-Origin Resource Sharing. It's a browser mechanism "
                                              'that works alongside the Same-Origin Policy (SOP). The Same-Origin '
                                              'Policy prevents a web app running on one origin—defined by protocol, '
                                              'domain, and port—from reading data from a different origin. CORS '
                                              "provides a secure way for the backend server to tell the browser: 'I "
                                              "trust this frontend origin, go ahead and let it read my response', "
                                              'using headers like Access-Control-Allow-Origin. The reason browsers '
                                              'send a preflight request comes down to protecting servers from '
                                              'unexpected requests that could alter data. Browsers divide requests '
                                              "into 'simple' and 'non-simple'. If a request is simple—like a basic GET "
                                              'or a form POST with standard headers—it sends it directly. But if a '
                                              "request is non-simple—such as sending JSON with 'Content-Type: "
                                              "application/json', sending custom headers like 'Authorization: Bearer "
                                              "token', or using methods like PUT or DELETE—the browser automatically "
                                              'sends an HTTP OPTIONS request first. This preflight checks whether the '
                                              'server understands CORS and permits those specific methods and headers. '
                                              'If the server responds with 200 OK and the right Access-Control-Allow '
                                              'headers, only then does the browser send the actual API call.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'CORS is a security feature enforced by browsers that stops client-side '
                                              'code on one website from making unauthorized requests to an API hosted '
                                              'on another domain. By default, the Same-Origin Policy blocks '
                                              'cross-origin requests. The backend can allow it by returning the header '
                                              'Access-Control-Allow-Origin. The browser sends a preflight OPTIONS '
                                              'request before making the real request if you use methods like PUT or '
                                              'DELETE, or if you send custom headers like Authorization or JSON '
                                              'content-type. The preflight checks if the server allows the request '
                                              'before sending the actual data.',
                               'missing_concepts': ['Simple requests (GET, POST, HEAD with standard headers like '
                                                    'Content-Type: application/x-www-form-urlencoded or text/plain) '
                                                    'are sent directly without preflight']},
                              {'quality_level': 'average',
                               'human_score': 61,
                               'answer_text': 'CORS is an error you get in the browser console when your React '
                                              'frontend on localhost:3000 tries to call your Node backend on '
                                              'localhost:5000. It happens because they are on different ports. To fix '
                                              'it, you have to enable CORS on the server with cors middleware and set '
                                              'Access-Control-Allow-Origin to star. The browser sends an OPTIONS '
                                              'preflight request before the real request to check if the server is '
                                              'alive and accepting requests from that domain.',
                               'missing_concepts': ['Same-Origin Policy (SOP) is a core browser security mechanism '
                                                    'that blocks client scripts on one origin (scheme, host, port) '
                                                    'from accessing resources on a different origin',
                                                    'Simple requests (GET, POST, HEAD with standard headers like '
                                                    'Content-Type: application/x-www-form-urlencoded or text/plain) '
                                                    'are sent directly without preflight']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'CORS is a firewall installed on routers that prevents hackers from '
                                              'reading your database. Browsers send preflight OPTIONS requests to '
                                              "check the user's GPS coordinates before loading the website. You can "
                                              "bypass CORS completely by disabling your computer's internet security "
                                              'settings.',
                               'missing_concepts': ['Same-Origin Policy (SOP) is a core browser security mechanism '
                                                    'that blocks client scripts on one origin (scheme, host, port) '
                                                    'from accessing resources on a different origin',
                                                    'CORS is an HTTP-header based relaxation mechanism allowing '
                                                    'servers to declare which origins are permitted to access their '
                                                    'resources (e.g., Access-Control-Allow-Origin)',
                                                    'Simple requests (GET, POST, HEAD with standard headers like '
                                                    'Content-Type: application/x-www-form-urlencoded or text/plain) '
                                                    'are sent directly without preflight',
                                                    'Preflight OPTIONS request is sent automatically by browsers prior '
                                                    "to 'non-simple' requests (custom headers like Authorization, "
                                                    'Content-Type: application/json, PUT/DELETE) to check server '
                                                    'permissions before executing the actual request']}]},
          {'topic_tag': 'Responsive Design & Media Queries',
           'question': 'How do CSS media queries and viewport meta tags enable responsive web design across devices?',
           'keywords': ['Responsive Web Design',
                        'Media Queries',
                        'Viewport Meta Tag',
                        'Fluid Layouts',
                        'Breakpoints',
                        'Mobile-First'],
           'expected_concepts': ["Viewport meta tag (<meta name='viewport' content='width=device-width, "
                                 "initial-scale=1.0'>) instructs mobile browsers to render at device physical pixel "
                                 'width rather than scaling a 980px desktop canvas',
                                 'CSS media queries (@media (min-width: 768px)) conditionally apply style rules based '
                                 'on device characteristics (screen width, orientation, resolution)',
                                 'Mobile-first design philosophy: Write base styles for small mobile screens first '
                                 'without queries, then use min-width queries to progressively enhance layouts for '
                                 'tablets and desktops',
                                 'Fluid layouts and flexible units: Responsive design combines media query breakpoints '
                                 'with relative units (%, vw/vh, rem) and CSS Grid / Flexbox to fluidly adapt between '
                                 'breakpoints'],
           'model_answer': 'Responsive Web Design (RWD) ensures web applications adapt seamlessly across phones, '
                           'tablets, laptops, and 4K displays through the interplay of three core mechanisms: 1. The '
                           'Viewport Meta Tag: Without \'<meta name="viewport" content="width=device-width, '
                           'initial-scale=1.0">\', mobile browsers assume a desktop webpage and render at a virtual '
                           'canvas of 980px, zooming out so text becomes illegibly tiny. The viewport tag commands the '
                           'browser to set the viewport width equal to the physical screen width of the device '
                           "('width=device-width') and sets the initial zoom level to 100% ('initial-scale=1.0'). 2. "
                           'CSS Media Queries: Media queries allow developers to apply CSS rules conditionally based '
                           "on device capabilities: '@media (min-width: 768px) { ... }'. Common breakpoint ranges "
                           'target mobile (<640px), tablet (640px - 1024px), desktop (1024px - 1280px), and large '
                           'screens (>1280px). 3. Mobile-First Architecture: In modern CSS, best practice dictates '
                           'writing mobile styles as default base CSS (outside media queries). Media queries are then '
                           "introduced using 'min-width' rules to progressively layer on desktop enhancements (e.g., "
                           'expanding a single-column stacked layout into a multi-column CSS Grid). 4. Fluidity: Media '
                           'queries are coupled with relative units (%, rem, vw, vh, and clamp(1rem, 2.5vw, 2rem)) and '
                           'flexbox/grid containers to ensure smooth layout scaling between distinct breakpoint '
                           'thresholds.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'Responsive web design is built on the combination of the viewport meta '
                                              'tag, CSS media queries, and fluid layout units. First, the viewport '
                                              "meta tag is essential: <meta name='viewport' "
                                              "content='width=device-width, initial-scale=1.0'>. If you omit this tag, "
                                              'mobile browsers assume they are loading a legacy desktop site and '
                                              'render the page on a default 980px wide canvas, zooming out so '
                                              'everything looks microscopic. Setting width=device-width tells the '
                                              'browser to match the viewport to the actual screen width at a 1:1 '
                                              'scale. Second, CSS media queries allow you to set breakpoints based on '
                                              'screen width using @media rules. In modern web development, we use a '
                                              'mobile-first approach: you write your base CSS for single-column mobile '
                                              'screens without any media query, and then use @media (min-width: 768px) '
                                              'and @media (min-width: 1024px) to progressively enhance the layout into '
                                              'multi-column layouts for tablets and desktops. Third, between '
                                              'breakpoints, you maintain fluid layouts using relative units like '
                                              'percentages, rems, vw/vh, and modern CSS functions like clamp() '
                                              'alongside Flexbox and Grid so elements adapt smoothly without '
                                              'horizontal scrollbars.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'The viewport meta tag width=device-width tells mobile devices to render '
                                              'the page at their actual screen width rather than zooming out a desktop '
                                              'view. Media queries in CSS let you change styles at different screen '
                                              'sizes using breakpoints, like @media screen and (min-width: 768px) for '
                                              'tablets and 1024px for desktops. A mobile-first approach is best where '
                                              'you style for mobile first and use min-width queries to add desktop '
                                              'styling. You also combine this with fluid percentage widths so the '
                                              'design scales smoothly.',
                               'missing_concepts': ['Fluid layouts and flexible units: Responsive design combines '
                                                    'media query breakpoints with relative units (%, vw/vh, rem) and '
                                                    'CSS Grid / Flexbox to fluidly adapt between breakpoints']},
                              {'quality_level': 'average',
                               'human_score': 61,
                               'answer_text': 'Media queries let you write CSS rules that only apply on certain screen '
                                              'sizes. For example, on a phone you show items in a single column, and '
                                              'on desktop with @media (min-width: 1024px) you change it to three '
                                              'columns using Flexbox. The viewport meta tag is placed in the HTML '
                                              "<head> so mobile phones don't zoom out the page. Together they make a "
                                              'website responsive on iPhones and laptops.',
                               'missing_concepts': ['Mobile-first design philosophy: Write base styles for small '
                                                    'mobile screens first without queries, then use min-width queries '
                                                    'to progressively enhance layouts for tablets and desktops',
                                                    'Fluid layouts and flexible units: Responsive design combines '
                                                    'media query breakpoints with relative units (%, vw/vh, rem) and '
                                                    'CSS Grid / Flexbox to fluidly adapt between breakpoints']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'Media queries are used to play audio and video media files in HTML5. '
                                              "Responsive design means using JavaScript to detect the user's phone "
                                              'brand and redirecting them to a separate m.website.com domain. The '
                                              'viewport tag is only used for virtual reality headsets.',
                               'missing_concepts': ["Viewport meta tag (<meta name='viewport' "
                                                    "content='width=device-width, initial-scale=1.0'>) instructs "
                                                    'mobile browsers to render at device physical pixel width rather '
                                                    'than scaling a 980px desktop canvas',
                                                    'CSS media queries (@media (min-width: 768px)) conditionally apply '
                                                    'style rules based on device characteristics (screen width, '
                                                    'orientation, resolution)',
                                                    'Mobile-first design philosophy: Write base styles for small '
                                                    'mobile screens first without queries, then use min-width queries '
                                                    'to progressively enhance layouts for tablets and desktops',
                                                    'Fluid layouts and flexible units: Responsive design combines '
                                                    'media query breakpoints with relative units (%, vw/vh, rem) and '
                                                    'CSS Grid / Flexbox to fluidly adapt between breakpoints']}]},
          {'topic_tag': 'React Functional vs Class Components',
           'question': 'Why have functional components with React Hooks largely superseded class components in modern '
                       'React?',
           'keywords': ['Functional Components',
                        'Class Components',
                        'React Hooks',
                        'Lifecycle Methods',
                        'State Management',
                        'JSX'],
           'expected_concepts': ["Boilerplate and 'this' binding: Class components required constructor boilerplate, "
                                 'explicit event handler binding (this.handleClick = this.handleClick.bind(this)), and '
                                 "confusing 'this' semantics",
                                 'Fragmented lifecycle logic: Class lifecycle methods (componentDidMount, '
                                 'componentDidUpdate, componentWillUnmount) forced related logic (e.g. event '
                                 'subscription and cleanup) to be split across multiple methods',
                                 'Hooks composability: Custom Hooks allow encapsulating and reusing stateful business '
                                 'logic across components cleanly, replacing brittle HOCs (Higher Order Components) '
                                 'and Render Props',
                                 'Simpler mental model & optimization: Functional components are pure JavaScript '
                                 'functions returning JSX, resulting in less code, easier testing, and better '
                                 'minification/tree-shaking by bundlers'],
           'model_answer': 'In modern React (since React 16.8), functional components equipped with Hooks (useState, '
                           'useEffect, useContext, custom hooks) have replaced class components (React.Component) as '
                           "the standard development paradigm for four key reasons: 1. Elimination of 'this' Binding "
                           'and Boilerplate: Class components required substantial boilerplate: extending '
                           'React.Component, implementing constructors, and explicitly binding event handlers '
                           "(this.handleClick.bind(this)) to prevent 'this' from resolving to undefined at runtime. "
                           'Functional components are plain JavaScript functions that capture scope lexically, '
                           "completely eliminating 'this' confusion. 2. Unified Lifecycle Management: In class "
                           'components, related logic was artificially fragmented across lifecycle methods. For '
                           'example, subscribing to a WebSocket required opening the connection in '
                           "'componentDidMount', checking prop changes in 'componentDidUpdate', and closing it in "
                           "'componentWillUnmount'. The 'useEffect' hook unifies setup, reactive updates (via "
                           'dependency arrays), and cleanup (via return functions) in a single localized code block. '
                           '3. Reusability via Custom Hooks: Prior to Hooks, sharing stateful logic between class '
                           'components required complex patterns like Higher-Order Components (HOCs) or Render Props, '
                           "which created 'wrapper hell' in component trees. Custom Hooks allow developers to extract "
                           'and share stateful logic as simple, composable JavaScript functions (e.g., useAuth(), '
                           'useFetch()). 4. Tooling and Minification: Functional components minify better because '
                           'function and variable names can be mangled aggressively by bundlers, whereas class method '
                           'names cannot be mangled without breaking prototype lookups.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'Functional components with Hooks have superseded class components for '
                                              "several major reasons: 1. No more 'this' binding: In class components, "
                                              'handling event listeners required either manual binding in the '
                                              'constructor—like this.handleClick = this.handleClick.bind(this)—or '
                                              "arrow class fields. JavaScript's dynamic 'this' was a huge source of "
                                              'bugs for developers. Functional components are just plain functions '
                                              'where variables are scoped lexically. 2. Unified lifecycle logic: In '
                                              'class components, related logic was split across componentDidMount, '
                                              'componentDidUpdate, and componentWillUnmount. For example, if you set '
                                              'up an event listener or a timer, you started it in componentDidMount, '
                                              'updated it in componentDidUpdate, and cleaned it up in '
                                              'componentWillUnmount. With the useEffect hook, you put the setup and '
                                              'the return cleanup function together in a single place. 3. Code reuse '
                                              'with Custom Hooks: In class components, if you wanted to share stateful '
                                              'logic between components, you had to use Higher-Order Components (HOCs) '
                                              "or Render Props, which created massive 'wrapper hell' in the React "
                                              'DevTools. With custom hooks, you can extract stateful logic into a '
                                              'simple function and reuse it anywhere without changing component '
                                              'hierarchy. 4. Better performance and smaller bundles: Functional '
                                              'components have less boilerplate, are easier for build tools to minify '
                                              "and tree-shake, and fit React's functional, declarative mental model "
                                              'much better.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'Functional components with hooks replaced class components because they '
                                              'are much simpler to write and read. Class components required extending '
                                              "React.Component, writing constructors, and dealing with 'this' binding "
                                              'issues. In class components, you also had lifecycle methods like '
                                              'componentDidMount and componentWillUnmount where you had to split up '
                                              'code for timers or subscriptions. With useEffect, all of that logic '
                                              'lives in one hook with a cleanup function. Hooks also make it easy to '
                                              'create custom hooks to share stateful logic across multiple components '
                                              'without wrapper hell.',
                               'missing_concepts': ['Simpler mental model & optimization: Functional components are '
                                                    'pure JavaScript functions returning JSX, resulting in less code, '
                                                    'easier testing, and better minification/tree-shaking by '
                                                    'bundlers']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'Class components are the older way of writing React using classes and '
                                              'lifecycle methods like componentDidMount and render(). Functional '
                                              'components are regular functions that return JSX. React introduced '
                                              'Hooks like useState and useEffect in React 16.8 so that functional '
                                              'components could have state and lifecycle effects. Functional '
                                              "components are preferred because they have less code, don't need 'this' "
                                              'keyword, and are faster for React to render.',
                               'missing_concepts': ['Fragmented lifecycle logic: Class lifecycle methods '
                                                    '(componentDidMount, componentDidUpdate, componentWillUnmount) '
                                                    'forced related logic (e.g. event subscription and cleanup) to be '
                                                    'split across multiple methods',
                                                    'Hooks composability: Custom Hooks allow encapsulating and reusing '
                                                    'stateful business logic across components cleanly, replacing '
                                                    'brittle HOCs (Higher Order Components) and Render Props']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'Class components were deprecated in React because JavaScript removed '
                                              'classes from the language. Functional components are used because they '
                                              "don't use the DOM. Hooks are global variables that store database "
                                              'connections on the server.',
                               'missing_concepts': ["Boilerplate and 'this' binding: Class components required "
                                                    'constructor boilerplate, explicit event handler binding '
                                                    '(this.handleClick = this.handleClick.bind(this)), and confusing '
                                                    "'this' semantics",
                                                    'Fragmented lifecycle logic: Class lifecycle methods '
                                                    '(componentDidMount, componentDidUpdate, componentWillUnmount) '
                                                    'forced related logic (e.g. event subscription and cleanup) to be '
                                                    'split across multiple methods',
                                                    'Hooks composability: Custom Hooks allow encapsulating and reusing '
                                                    'stateful business logic across components cleanly, replacing '
                                                    'brittle HOCs (Higher Order Components) and Render Props',
                                                    'Simpler mental model & optimization: Functional components are '
                                                    'pure JavaScript functions returning JSX, resulting in less code, '
                                                    'easier testing, and better minification/tree-shaking by '
                                                    'bundlers']}]},
          {'topic_tag': 'React Props vs State',
           'question': 'Explain the difference between Props and State in React component architecture.',
           'keywords': ['React Props',
                        'React State',
                        'Unidirectional Data Flow',
                        'Immutability',
                        'Component Re-render',
                        'Parent-Child Communication'],
           'expected_concepts': ['Ownership and Scope: Props (properties) are passed into a component from its parent '
                                 '(external inputs); State is managed internally within the component (local private '
                                 'data)',
                                 'Mutability: Props are strictly read-only and immutable for the receiving component; '
                                 'State is mutable via its dedicated setter function (e.g. useState or this.setState)',
                                 'Unidirectional data flow: Data flows down from parent to child via props; children '
                                 'notify parents of changes by invoking callback functions passed down as props',
                                 'Re-render triggers: Changes to either props or state signal React to schedule a '
                                 're-render of the component and its children'],
           'model_answer': "In React's declarative component model, Props and State represent the two primary "
                           'mechanisms for handling data, differing fundamentally in ownership, mutability, and '
                           'purpose: 1. Props (short for Properties): Props are external configuration inputs passed '
                           'from a parent component down to a child component (e.g., <UserProfile name="Alice" '
                           "age={30} />). In adhering to React's pure component philosophy and unidirectional data "
                           "flow, props are strictly read-only (immutable) from the child's perspective. A child "
                           "component must never attempt to modify its own props (props.name = 'Bob' is an "
                           'anti-pattern and will fail or warn). 2. State: State represents internal, private data '
                           'managed locally within a component that changes over time in response to user actions, '
                           'network responses, or timers. State is initialized inside the component (via useState in '
                           'functional components or this.state in classes) and can only be updated using its '
                           'corresponding setter function (setCount(newCount)). 3. Communication: Props facilitate '
                           'top-down parent-to-child communication. When a child needs to communicate back up to a '
                           'parent, the parent passes down a callback function as a prop, which the child invokes with '
                           "data. 4. Re-rendering: Whenever a component's internal state updates OR new props are "
                           'received from its parent, React schedules a re-render of that component and recursively '
                           're-renders its child subtree (unless optimized via React.memo).',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'In React, Props and State represent external inputs versus internal '
                                              'data. 1. Props (properties) are passed down from a parent component to '
                                              "a child component, like arguments passed to a function. In React's "
                                              'unidirectional data flow, props are strictly read-only and immutable '
                                              'inside the child component—a child should never modify the props it '
                                              "receives. 2. State is the component's internal, private data store that "
                                              'it controls and can mutate over time, like in response to a user '
                                              'clicking a button or an API response coming back. In functional '
                                              'components, you manage state using the useState hook, and you update it '
                                              'by calling the setter function. 3. When it comes to communication, data '
                                              'flows down from parent to child via props. If a child needs to send '
                                              'data up to its parent, the parent passes a callback function down as a '
                                              'prop, and the child calls that function with the updated value. 4. '
                                              'Crucially, whenever either props change or state updates, React '
                                              'triggers a re-render of that component and its children so the UI '
                                              'reflects the latest data.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'Props are passed into a component from the outside by its parent '
                                              'component, and they are read-only so the child cannot change them. '
                                              'State is local to the component, managed with useState, and can be '
                                              'changed by the component using the setter function. For example, a '
                                              'parent can pass a title prop to a child button, but the button might '
                                              'have internal hover state. When either state or props change, React '
                                              're-renders the component.',
                               'missing_concepts': ['Unidirectional data flow: Data flows down from parent to child '
                                                    'via props; children notify parents of changes by invoking '
                                                    'callback functions passed down as props']},
                              {'quality_level': 'average',
                               'human_score': 61,
                               'answer_text': 'Props are like HTML attributes that you pass to a component, like <Card '
                                              "title='Hello' />. State is used inside the component for variables that "
                                              'change, like a counter or form inputs. Props cannot be changed by the '
                                              'component because they belong to the parent, but state can be changed '
                                              'using setState. Both cause the screen to refresh when they change.',
                               'missing_concepts': ['Unidirectional data flow: Data flows down from parent to child '
                                                    'via props; children notify parents of changes by invoking '
                                                    'callback functions passed down as props',
                                                    'Ownership and Scope: Props (properties) are passed into a '
                                                    'component from its parent (external inputs); State is managed '
                                                    'internally within the component (local private data)']},
                              {'quality_level': 'poor',
                               'human_score': 26,
                               'answer_text': "Props are stored in the browser's Redux store, and State is stored on "
                                              'the backend Node server. Props are mutable and can be overwritten by '
                                              'any child component. State is read-only and cannot be updated once the '
                                              'page loads.',
                               'missing_concepts': ['Ownership and Scope: Props (properties) are passed into a '
                                                    'component from its parent (external inputs); State is managed '
                                                    'internally within the component (local private data)',
                                                    'Mutability: Props are strictly read-only and immutable for the '
                                                    'receiving component; State is mutable via its dedicated setter '
                                                    'function (e.g. useState or this.setState)',
                                                    'Unidirectional data flow: Data flows down from parent to child '
                                                    'via props; children notify parents of changes by invoking '
                                                    'callback functions passed down as props',
                                                    'Re-render triggers: Changes to either props or state signal React '
                                                    'to schedule a re-render of the component and its children']}]},
          {'topic_tag': 'React useState Hook Workflow',
           'question': 'How does the useState hook manage local component state and trigger re-renders in React?',
           'keywords': ['useState',
                        'State Variable',
                        'Setter Function',
                        'Initial State',
                        'Re-render Trigger',
                        'Functional Updates'],
           'expected_concepts': ['useState syntax and return: const [state, setState] = useState(initialState) returns '
                                 "a stateful value and a setter function linked to React's internal fiber node",
                                 'Re-render scheduling: Calling the setter function (setState) notifies React of a '
                                 'state update, causing React to schedule a re-render and re-execute the component '
                                 'function',
                                 'Functional updates for asynchronous/batched state: Using setState(prevState => '
                                 'prevState + 1) ensures access to the freshest state value and avoids stale closure '
                                 'bugs',
                                 'Automatic batching: React batches multiple state updates occurring within event '
                                 'handlers and asynchronous callbacks to prevent unnecessary intermediate re-renders'],
           'model_answer': "The 'useState' hook allows React functional components to declare and manage local, "
                           'persistent state across renders: 1. Declaration and Internal Mechanics: When you write '
                           "'const [count, setCount] = useState(0)', React associates this state cell with the "
                           "component's Fiber node in the Virtual DOM tree. During the initial mount, React stores the "
                           'initial state (or executes a lazy initializer function like useState(() => '
                           'computeInitialValue())). On subsequent renders, React ignores the initial argument and '
                           'returns the current persisted state value along with the stable dispatch setter function. '
                           "2. Triggering Re-renders: When 'setCount(newValue)' is called, React compares the new "
                           'value against the current state using Object.is() equality. If the value has changed, '
                           'React marks the fiber node as dirty and schedules a re-render. During the re-render, the '
                           'functional component executes again from top to bottom, and useState returns the updated '
                           'state value. 3. Functional Updates: Because state updates are asynchronous and batched, '
                           'directly referencing state in sequential calls (e.g., setCount(count + 1); setCount(count '
                           "+ 1);) causes stale closure bugs because both calls capture the identical 'count' value "
                           "from the current render frame. Passing a functional updater: 'setCount(prev => prev + 1)' "
                           'guarantees that React passes the freshest pending state to the callback. 4. Automatic '
                           'Batching (React 18): React automatically batches multiple state updates into a single '
                           're-render, even inside Promises, setTimeout callbacks, and native event listeners, '
                           'ensuring optimal performance.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': "The useState hook is declared as 'const [state, setState] = "
                                              "useState(initialState)'. Under the hood, React maintains a linked list "
                                              "of hook records attached to the component's Fiber node. On the initial "
                                              'render, React initializes the state. On subsequent renders, React '
                                              'preserves the state across renders and returns the latest value. When '
                                              'you invoke the setter function, say setState(newValue), React checks if '
                                              'the value changed using Object.is(). If it did, React schedules a '
                                              're-render of the component. When the component re-executes, useState '
                                              'returns the updated value. There are two critical nuances: First, '
                                              'functional updates. If your new state depends on the previous '
                                              'state—especially during async operations or rapid events—you should '
                                              "pass an updater callback like 'setCount(prev => prev + 1)'. This "
                                              'prevents stale closure bugs where the function closes over an outdated '
                                              'state value. Second, batching. In modern React 18, React automatically '
                                              'batches state updates together—whether inside event handlers, promises, '
                                              'or setTimeout—so multiple setState calls in the same tick trigger only '
                                              'a single re-render instead of multiple unnecessary renders.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'useState returns an array with two elements: the current state value '
                                              'and a setter function to update it. When you call the setter function, '
                                              'React schedules a re-render of the component and updates the virtual '
                                              'DOM with the new value. If your new state depends on the old state, you '
                                              'should use the functional updater pattern, like setCount(prevCount => '
                                              "prevCount + 1), so you don't run into issues with stale state. React "
                                              'also batches state updates to avoid unnecessary renders.',
                               'missing_concepts': ['useState syntax and return: const [state, setState] = '
                                                    'useState(initialState) returns a stateful value and a setter '
                                                    "function linked to React's internal fiber node"]},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'You use useState by writing const [count, setCount] = useState(0). '
                                              'Count is the variable and setCount is the function you call to change '
                                              'it. When you call setCount(count + 1), it changes the count and causes '
                                              'React to re-render the component on the screen with the new number. You '
                                              "shouldn't modify count directly like count = 5 because React won't know "
                                              'to re-render.',
                               'missing_concepts': ['Functional updates for asynchronous/batched state: Using '
                                                    'setState(prevState => prevState + 1) ensures access to the '
                                                    'freshest state value and avoids stale closure bugs',
                                                    'Automatic batching: React batches multiple state updates '
                                                    'occurring within event handlers and asynchronous callbacks to '
                                                    'prevent unnecessary intermediate re-renders']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'useState is a function that creates a global Redux store for the whole '
                                              'website. Calling the setter function reboots the browser tab to reload '
                                              'the HTML. You can call useState inside if-statements and while-loops '
                                              'without any restrictions.',
                               'missing_concepts': ['useState syntax and return: const [state, setState] = '
                                                    'useState(initialState) returns a stateful value and a setter '
                                                    "function linked to React's internal fiber node",
                                                    'Re-render scheduling: Calling the setter function (setState) '
                                                    'notifies React of a state update, causing React to schedule a '
                                                    're-render and re-execute the component function',
                                                    'Functional updates for asynchronous/batched state: Using '
                                                    'setState(prevState => prevState + 1) ensures access to the '
                                                    'freshest state value and avoids stale closure bugs',
                                                    'Automatic batching: React batches multiple state updates '
                                                    'occurring within event handlers and asynchronous callbacks to '
                                                    'prevent unnecessary intermediate re-renders']}]},
          {'topic_tag': 'HTML5 Form Native Validation',
           'question': 'How do HTML5 form validation attributes like required, pattern, and type work natively?',
           'keywords': ['HTML5 Form Validation',
                        'required Attribute',
                        'pattern Regex',
                        'type Validation',
                        'Validity State API',
                        'User Feedback'],
           'expected_concepts': ["Native declarative attributes: 'required' ensures field cannot be empty; 'type' "
                                 "(email, url, number) validates format; 'pattern' tests input against a regular "
                                 "expression; 'min'/'max'/'maxlength' enforce range/length bounds",
                                 'Automatic browser intervention: On form submit, the browser intercepts submission, '
                                 'blocks the submit event if invalid, focuses the first invalid element, and displays '
                                 'a localized error tooltip',
                                 'CSS pseudo-classes: Browsers dynamically apply :valid and :invalid pseudo-classes to '
                                 'form inputs and parent forms for immediate visual styling feedback',
                                 'JavaScript Constraint Validation API: Developers can query input.validity (valid, '
                                 'valueMissing, typeMismatch, patternMismatch), call checkValidity() / '
                                 'reportValidity(), and set custom error messages via setCustomValidity()'],
           'model_answer': 'HTML5 introduced native client-side form validation, allowing developers to enforce data '
                           'constraints declaratively without writing custom JavaScript: 1. Declarative Attributes: - '
                           "'required': Specifies that the input field must have a non-empty value before submission. "
                           '- \'type\': Enforces semantic data types; for instance, \'type="email"\' validates '
                           'RFC-compliant email syntax, \'type="url"\' requires a protocol, and \'type="number"\' '
                           "enforces numeric input with 'min', 'max', and 'step' constraints. - 'pattern': Accepts a "
                           'regular expression (e.g., \'pattern="[0-9]{5}"\') that the entire input value must match. '
                           "- 'minlength' / 'maxlength': Restricts string character counts. 2. Browser Interception: "
                           'When a user clicks a submit button inside a form, the browser automatically executes '
                           'constraint validation. If any field fails, the browser cancels the submit event, scrolls '
                           'and focuses the first invalid field, and renders a native localized validation bubble. 3. '
                           'CSS Styling: The browser continuously updates validation state, matching pseudo-classes '
                           "':valid', ':invalid', ':required', and ':optional', allowing live styling (e.g., "
                           'input:invalid { border-color: red; }). 4. Constraint Validation API: In JavaScript, '
                           "developers can interact with native validation using the 'validity' object "
                           '(input.validity.valueMissing, typeMismatch, patternMismatch), trigger validation with '
                           "'input.checkValidity()' or 'input.reportValidity()', and inject localized custom error "
                           "strings via 'input.setCustomValidity('Please enter your 5-digit postal code')'.",
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'HTML5 native form validation provides client-side validation right out '
                                              'of the box using declarative attributes and the Constraint Validation '
                                              "API. 1. Declarative attributes: 'required' ensures the input is not "
                                              "empty. The 'type' attribute validates formats—like type='email' "
                                              "ensuring an @ and domain, type='url' requiring a valid URL, or "
                                              "type='number'. The 'pattern' attribute lets you specify a custom "
                                              'regular expression that the input must match. You also have min, max, '
                                              'minlength, and maxlength. 2. Native browser behavior: When the user '
                                              'submits the form, the browser automatically intercepts it. If any field '
                                              'fails validation, the browser blocks the submit event, shifts focus to '
                                              'the first invalid field, and displays a native localized tooltip '
                                              'explaining the error. 3. CSS integration: The browser dynamically '
                                              'applies the :valid and :invalid pseudo-classes, so you can style inputs '
                                              'with green or red borders instantly as the user types. 4. JavaScript '
                                              "Constraint Validation API: In JS, every input has a 'validity' property "
                                              'containing booleans like validity.valueMissing, validity.typeMismatch, '
                                              'and validity.patternMismatch. You can trigger validation manually using '
                                              'checkValidity() or reportValidity(), and set custom error messages with '
                                              'setCustomValidity().',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'HTML5 form validation works through HTML attributes on input fields. '
                                              "The required attribute makes sure the user doesn't leave the field "
                                              "blank. The type attribute like type='email' or type='number' ensures "
                                              'the user enters the right data format. The pattern attribute lets you '
                                              'pass a regex to match specific formats like phone numbers. When the '
                                              'form is submitted, the browser automatically blocks submission and '
                                              'shows an error message popup if any field is invalid. You can also '
                                              'style them with CSS using :valid and :invalid pseudo-classes.',
                               'missing_concepts': ['JavaScript Constraint Validation API: Developers can query '
                                                    'input.validity (valid, valueMissing, typeMismatch, '
                                                    'patternMismatch), call checkValidity() / reportValidity(), and '
                                                    'set custom error messages via setCustomValidity()']},
                              {'quality_level': 'average',
                               'human_score': 61,
                               'answer_text': "HTML5 has built-in validation attributes so you don't need JavaScript "
                                              "for simple forms. 'required' means the field cannot be empty. "
                                              "'type=email' checks that there is an @ symbol in the email. 'pattern' "
                                              'lets you use regex to check things like zip codes. When you submit the '
                                              'form and something is wrong, the browser shows a little popup bubble '
                                              "saying 'Please fill out this field'. You can style invalid inputs using "
                                              'CSS :invalid.',
                               'missing_concepts': ['Automatic browser intervention: On form submit, the browser '
                                                    'intercepts submission, blocks the submit event if invalid, '
                                                    'focuses the first invalid element, and displays a localized error '
                                                    'tooltip',
                                                    'JavaScript Constraint Validation API: Developers can query '
                                                    'input.validity (valid, valueMissing, typeMismatch, '
                                                    'patternMismatch), call checkValidity() / reportValidity(), and '
                                                    'set custom error messages via setCustomValidity()']},
                              {'quality_level': 'poor',
                               'human_score': 26,
                               'answer_text': 'HTML5 form validation sends the input values to the backend server in '
                                              'real time over WebSockets to validate against the SQL database. The '
                                              'pattern attribute is used to apply background image patterns to the '
                                              'input box. Required only works in Google Chrome.',
                               'missing_concepts': ["Native declarative attributes: 'required' ensures field cannot be "
                                                    "empty; 'type' (email, url, number) validates format; 'pattern' "
                                                    "tests input against a regular expression; 'min'/'max'/'maxlength' "
                                                    'enforce range/length bounds',
                                                    'Automatic browser intervention: On form submit, the browser '
                                                    'intercepts submission, blocks the submit event if invalid, '
                                                    'focuses the first invalid element, and displays a localized error '
                                                    'tooltip',
                                                    'CSS pseudo-classes: Browsers dynamically apply :valid and '
                                                    ':invalid pseudo-classes to form inputs and parent forms for '
                                                    'immediate visual styling feedback',
                                                    'JavaScript Constraint Validation API: Developers can query '
                                                    'input.validity (valid, valueMissing, typeMismatch, '
                                                    'patternMismatch), call checkValidity() / reportValidity(), and '
                                                    'set custom error messages via setCustomValidity()']}]},
          {'topic_tag': 'CSS Specificity Rules',
           'question': 'How is CSS specificity calculated when multiple selectors target the same element?',
           'keywords': ['CSS Specificity',
                        'Inline Styles',
                        'ID Selectors',
                        'Class Selectors',
                        'Element Selectors',
                        '!important Rule'],
           'expected_concepts': ['Specificity hierarchy is represented as a 4-part scoring tuple (a, b, c, d): Inline '
                                 'styles (a), IDs (b), Classes/attributes/pseudo-classes (c), Elements/pseudo-elements '
                                 '(d)',
                                 'Scoring weights: Inline style = (1, 0, 0, 0); ID selector = (0, 1, 0, 0); Class, '
                                 'attribute, and pseudo-class (:hover) = (0, 0, 1, 0); Element and pseudo-element '
                                 '(::before) = (0, 0, 0, 1)',
                                 'Comparison rule: Specificity is compared position by position from left to right; a '
                                 'higher value in an earlier column always beats any number in a subsequent column '
                                 '(e.g., 1 ID beats 100 classes)',
                                 '!important and universal selector: Universal selector (*), combinators (+, >, ~), '
                                 "and :where() have (0, 0, 0, 0) specificity; '!important' overrides normal "
                                 'specificity by taking precedence in the cascade'],
           'model_answer': 'When multiple conflicting CSS rules target the same element, the browser resolves the '
                           'cascade by calculating CSS Specificity, represented as a four-component vector (a, b, c, '
                           "d): 1. Component 'a' (Inline Styles): Styles applied directly on the HTML element via the "
                           '\'style="..."\' attribute carry a specificity value of (1, 0, 0, 0). 2. Component \'b\' '
                           "(IDs): Each ID selector (#header, #main-nav) adds (0, 1, 0, 0). 3. Component 'c' (Classes, "
                           'Attributes, and Pseudo-classes): Each class selector (.btn), attribute selector '
                           '([type="text"]), and pseudo-class (:hover, :focus, :nth-child) adds (0, 0, 1, 0). 4. '
                           "Component 'd' (Elements and Pseudo-elements): Each element tag name (div, h1, p) and "
                           'pseudo-element (::before, ::after) adds (0, 0, 0, 1). 5. Comparison Rules: Specificity '
                           'vectors are evaluated lexicographically from left to right. A single ID selector (0, 1, 0, '
                           "0) will override a selector with twenty classes (0, 0, 20, 0) because 1 in column 'b' "
                           "beats 0, regardless of column 'c'. If two selectors have identical specificity, the one "
                           'declared later in the CSS stylesheet wins (source order). 6. Exceptions: The universal '
                           "selector (*), combinators (+, >, ~), and the ':where()' pseudo-class add (0, 0, 0, 0). The "
                           "'!important' declaration is not part of the specificity tuple itself; it operates on the "
                           'cascade level, overriding any normal specificity declaration unless countered by another '
                           "'!important' rule with equal or higher specificity.",
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'CSS specificity is calculated using a four-category scoring system, '
                                              "often visualized as a tuple (a, b, c, d): 1. 'a' is for inline styles "
                                              "written directly on the element in HTML, like style='color: red', which "
                                              "gives (1, 0, 0, 0). 2. 'b' is the count of ID selectors, like #nav or "
                                              "#submit-btn, each giving (0, 1, 0, 0). 3. 'c' is the count of class "
                                              "selectors (.card), attribute selectors ([type='checkbox']), and "
                                              "pseudo-classes (:hover, :active), each giving (0, 0, 1, 0). 4. 'd' is "
                                              'the count of element tag selectors (div, p) and pseudo-elements '
                                              '(::before, ::after), each giving (0, 0, 0, 1). When the browser '
                                              "compares two selectors, it compares them from left to right. Column 'b' "
                                              "beats column 'c' no matter how many classes you have—so a single ID "
                                              'selector (0, 1, 0, 0) will always override 10 or even 100 classes (0, '
                                              '0, 10, 0). If two selectors have the exact same specificity score, the '
                                              'one written later in the CSS file wins by source order. The universal '
                                              'selector (*) and combinators like > or + contribute zero specificity. '
                                              "Finally, !important isn't a specificity score; it's a cascade override "
                                              'that beats all standard declarations regardless of specificity.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'CSS specificity is calculated based on the types of selectors used. '
                                              'Inline styles have the highest specificity with 1000 points. IDs give '
                                              '100 points, classes, pseudo-classes, and attributes give 10 points, and '
                                              'element tags give 1 point. If two rules target the same element, the '
                                              'one with the higher score wins. For example, #my-id has 100 points and '
                                              'beats .my-class which has 10 points. If scores are tied, the rule '
                                              'defined later in the CSS file applies. You can also use !important to '
                                              'override regular specificity.',
                               'missing_concepts': ['Comparison rule: Specificity is compared position by position '
                                                    'from left to right; a higher value in an earlier column always '
                                                    'beats any number in a subsequent column (e.g., 1 ID beats 100 '
                                                    'classes)']},
                              {'quality_level': 'average',
                               'human_score': 61,
                               'answer_text': 'Specificity determines which CSS rule gets applied when there is a '
                                              'conflict. Inline styles are the strongest, followed by ID selectors '
                                              'with #, then class selectors with ., and finally element tags like div '
                                              'or p. If you have conflicting styles, the ID selector will win over the '
                                              'class selector. If you want a style to apply no matter what, you add '
                                              '!important to the end of the line.',
                               'missing_concepts': ['Specificity hierarchy is represented as a 4-part scoring tuple '
                                                    '(a, b, c, d): Inline styles (a), IDs (b), '
                                                    'Classes/attributes/pseudo-classes (c), Elements/pseudo-elements '
                                                    '(d)',
                                                    'Comparison rule: Specificity is compared position by position '
                                                    'from left to right; a higher value in an earlier column always '
                                                    'beats any number in a subsequent column (e.g., 1 ID beats 100 '
                                                    'classes)']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'Specificity is calculated by counting the number of letters in the CSS '
                                              'selector; longer class names always have higher specificity than short '
                                              'class names. Inline styles are ignored if you have an external CSS '
                                              'stylesheet. You can increase specificity by capitalizing CSS property '
                                              'names.',
                               'missing_concepts': ['Specificity hierarchy is represented as a 4-part scoring tuple '
                                                    '(a, b, c, d): Inline styles (a), IDs (b), '
                                                    'Classes/attributes/pseudo-classes (c), Elements/pseudo-elements '
                                                    '(d)',
                                                    'Scoring weights: Inline style = (1, 0, 0, 0); ID selector = (0, '
                                                    '1, 0, 0); Class, attribute, and pseudo-class (:hover) = (0, 0, 1, '
                                                    '0); Element and pseudo-element (::before) = (0, 0, 0, 1)',
                                                    'Comparison rule: Specificity is compared position by position '
                                                    'from left to right; a higher value in an earlier column always '
                                                    'beats any number in a subsequent column (e.g., 1 ID beats 100 '
                                                    'classes)',
                                                    '!important and universal selector: Universal selector (*), '
                                                    'combinators (+, >, ~), and :where() have (0, 0, 0, 0) '
                                                    "specificity; '!important' overrides normal specificity by taking "
                                                    'precedence in the cascade']}]},
          {'topic_tag': 'Git Version Control Fundamentals',
           'question': 'Describe the standard Git feature branch workflow from cloning to merging a pull request.',
           'keywords': ['Git', 'Repository', 'Commit', 'Branch', 'Merge', 'Pull Request'],
           'expected_concepts': ["Cloning & branch creation: Clone remote repository ('git clone <url>'), ensure main "
                                 "is up to date ('git pull'), and branch off for feature development ('git checkout -b "
                                 "feature/xyz')",
                                 "Staging & atomic commits: Make local changes, inspect status/diff ('git status', "
                                 "'git diff'), stage files ('git add .'), and create descriptive commits ('git commit "
                                 "-m '...')",
                                 "Remote synchronization: Push local feature branch to remote origin ('git push -u "
                                 "origin feature/xyz')",
                                 'Pull Request & merge lifecycle: Open PR on GitHub/GitLab, conduct code review, '
                                 'execute automated CI/CD test checks, resolve merge conflicts, and merge (squash & '
                                 'merge or rebase) into main'],
           'model_answer': 'The Git Feature Branch Workflow is the industry standard for collaborative software '
                           'development: 1. Initialization and Branching: A developer clones the remote repository '
                           "locally ('git clone <url>'). Before beginning work, they ensure the base branch is current "
                           "('git checkout main && git pull'). They then create an isolated branch for the specific "
                           "feature or bugfix: 'git checkout -b feature/user-authentication'. 2. Local Development and "
                           "Staging: The developer makes incremental code modifications. They review changes with 'git "
                           "status' and 'git diff'. Work is staged into Git's index using 'git add <files>' and "
                           'committed with clear, atomic commit messages using \'git commit -m "feat: add JWT '
                           'authentication middleware"\'. 3. Remote Push: Once complete, the branch is pushed to the '
                           "remote repository (e.g., GitHub or GitLab) with upstream tracking: 'git push -u origin "
                           "feature/user-authentication'. 4. Pull Request (PR) & Code Review: The developer opens a "
                           "Pull Request targeting the 'main' branch. Team members review the code diff, leave inline "
                           'comments, and automated CI/CD pipelines run linters, unit tests, and build checks. 5. '
                           'Conflict Resolution & Merge: If main has diverged, the developer rebases or merges main '
                           'into the feature branch to resolve conflicts. Once approved and CI passes, the PR is '
                           "merged into main (often using 'Squash and Merge' to keep main's history clean), and the "
                           'feature branch is deleted.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'The standard Git feature branch workflow follows these steps: 1. Clone '
                                              "& Branch: You clone the repo using 'git clone <url>', make sure your "
                                              "local main branch is up to date with 'git checkout main && git pull', "
                                              "and create a dedicated feature branch using 'git checkout -b "
                                              "feature/login-page'. Working on an isolated branch prevents breaking "
                                              'the shared main branch. 2. Develop & Commit: As you work, you check '
                                              "changes with 'git status' and 'git diff'. You stage files using 'git "
                                              "add' and make focused, atomic commits with descriptive messages using "
                                              '\'git commit -m "feat: add login form validation"\'. 3. Push to Remote: '
                                              "You push the feature branch to the remote repository using 'git push -u "
                                              "origin feature/login-page', which sets up upstream tracking. 4. Open "
                                              'Pull Request (PR): On GitHub or GitLab, you open a Pull Request against '
                                              'main. This kicks off automated CI/CD pipelines to run test suites and '
                                              'linters, and team members perform peer code reviews and leave feedback. '
                                              '5. Resolve & Merge: If other team members merged changes to main, you '
                                              'rebase or merge main into your branch to resolve any merge conflicts '
                                              'locally. Once approved and tests pass, the PR is merged into '
                                              'main—typically via Squash and Merge to keep a clean commit history—and '
                                              'the feature branch is deleted.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'The feature branch workflow starts by cloning the repository with git '
                                              'clone. Then you create a new feature branch from main using git '
                                              'checkout -b feature-name. You make your code changes, stage them with '
                                              "git add, and commit them with git commit -m 'commit message'. Next, you "
                                              'push the branch to the remote repository using git push origin '
                                              'feature-name. Then you open a Pull Request on GitHub so other '
                                              'developers can review your code and CI tests can run. After receiving '
                                              'approval, the pull request is merged into main and the feature branch '
                                              'is deleted.',
                               'missing_concepts': ["Cloning & branch creation: Clone remote repository ('git clone "
                                                    "<url>'), ensure main is up to date ('git pull'), and branch off "
                                                    "for feature development ('git checkout -b feature/xyz')"]},
                              {'quality_level': 'average',
                               'human_score': 61,
                               'answer_text': 'First you clone the project using git clone. You create a new branch '
                                              "with git branch or git checkout -b so you don't commit directly to "
                                              'main. You make changes to files, run git add to stage them, and git '
                                              'commit to save the changes. Then you do git push to upload the branch '
                                              'to GitHub. On GitHub you create a Pull Request for your team to check '
                                              'your code. When they approve it, you hit the merge button to combine it '
                                              'into the main branch.',
                               'missing_concepts': ["Cloning & branch creation: Clone remote repository ('git clone "
                                                    "<url>'), ensure main is up to date ('git pull'), and branch off "
                                                    "for feature development ('git checkout -b feature/xyz')",
                                                    'Pull Request & merge lifecycle: Open PR on GitHub/GitLab, conduct '
                                                    'code review, execute automated CI/CD test checks, resolve merge '
                                                    'conflicts, and merge (squash & merge or rebase) into main']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'You do git clone to download the code, then edit files directly on the '
                                              'main branch. Once finished, you do git push --force directly to main so '
                                              "you don't have to deal with pull requests or branch merging. Commits "
                                              'are only needed when you are leaving the company.',
                               'missing_concepts': ["Cloning & branch creation: Clone remote repository ('git clone "
                                                    "<url>'), ensure main is up to date ('git pull'), and branch off "
                                                    "for feature development ('git checkout -b feature/xyz')",
                                                    'Staging & atomic commits: Make local changes, inspect status/diff '
                                                    "('git status', 'git diff'), stage files ('git add .'), and create "
                                                    "descriptive commits ('git commit -m '...')",
                                                    'Remote synchronization: Push local feature branch to remote '
                                                    "origin ('git push -u origin feature/xyz')",
                                                    'Pull Request & merge lifecycle: Open PR on GitHub/GitLab, conduct '
                                                    'code review, execute automated CI/CD test checks, resolve merge '
                                                    'conflicts, and merge (squash & merge or rebase) into main']}]},
          {'topic_tag': 'JSON Format & Parsing Syntax',
           'question': 'How do JSON.parse() and JSON.stringify() handle data conversion in JavaScript?',
           'keywords': ['JSON',
                        'JSON.parse()',
                        'JSON.stringify()',
                        'Key-Value Pairs',
                        'Data Serialization',
                        'Syntax Rules'],
           'expected_concepts': ['JSON data format rules: Plain text data interchange format; keys must be '
                                 'double-quoted strings; values must be strings, numbers, booleans, null, arrays, or '
                                 'nested objects (no undefined, functions, or circular references)',
                                 'JSON.stringify(value, replacer, space): Serializes JavaScript objects into JSON '
                                 'strings; silently omits functions, undefined, and symbols (or turns them into null '
                                 'inside arrays); throws TypeError on circular references',
                                 'JSON.parse(text, reviver): Deserializes a valid JSON string into a JavaScript '
                                 'object/value; throws a SyntaxError if the string is malformed (e.g. single quotes or '
                                 'trailing commas)',
                                 'Replacer and Reviver parameters: Optional second arguments allow custom '
                                 'transformation during serialization (filtering/formatting keys) and deserialization '
                                 '(e.g., converting ISO date strings back into Date objects)'],
           'model_answer': 'JSON (JavaScript Object Notation) is a lightweight, language-agnostic text serialization '
                           'format. In JavaScript, conversions between in-memory objects and serialized JSON strings '
                           "are handled by two core static methods on the global 'JSON' object: 1. "
                           'JSON.stringify(value, replacer, space): This method serializes a JavaScript data structure '
                           'into a formatted JSON string. - Handling of unsupported types: JSON format only supports '
                           'strings, numbers, booleans, null, objects, and arrays. When stringifying an object, '
                           "properties whose values are 'undefined', functions, or Symbols are silently omitted. If "
                           "encountered in an array, they are converted to 'null'. - Circular references: If an object "
                           'contains a circular reference (obj.self = obj), JSON.stringify throws a TypeError '
                           "('Converting circular structure to JSON'). - Parameters: The optional 'replacer' parameter "
                           "(function or array) filters or transforms values, and 'space' (e.g., 2 or 4) formats "
                           'output with indentation for readability. 2. JSON.parse(text, reviver): This method parses '
                           'a JSON string, reconstructing the JavaScript object or value. - Syntax strictness: The '
                           'input string must strictly conform to JSON grammar—keys and strings must use double quotes '
                           '(not single quotes), and trailing commas are prohibited; any deviation throws a '
                           "SyntaxError. - Reviver parameter: The optional 'reviver(key, value)' function runs on "
                           'every key-value pair during parsing, enabling post-processing, such as detecting ISO date '
                           'strings and converting them into native JavaScript Date instances.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'JSON.stringify and JSON.parse handle serialization and deserialization '
                                              'between JavaScript objects and JSON strings. 1. JSON.stringify(value, '
                                              'replacer, space): It converts a JavaScript object into a JSON-formatted '
                                              'string. Because JSON syntax is strict, stringify omits functions, '
                                              'undefined, and symbols from objects. If they appear inside an array, it '
                                              'converts them to null. A common gotcha is circular references: if an '
                                              'object references itself, JSON.stringify throws a TypeError. It also '
                                              "accepts an optional 'replacer' function to filter or modify properties, "
                                              "and an indentation 'space' argument for pretty-printing. 2. "
                                              'JSON.parse(text, reviver): It takes a JSON string and reconstructs the '
                                              'JavaScript object. JSON requires double quotes around keys and strings '
                                              'and forbids trailing commas—if the string violates this, JSON.parse '
                                              "throws a SyntaxError. It also accepts an optional 'reviver' function "
                                              'that lets you transform values as they are parsed; for example, '
                                              'converting ISO date strings back into native Date objects since JSON '
                                              'has no native Date type.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'JSON.stringify converts a JavaScript object into a JSON string, which '
                                              'is useful when sending data in an HTTP request body or storing it in '
                                              'LocalStorage. It ignores functions and undefined values, and throws an '
                                              'error if there are circular references. JSON.parse takes a JSON string '
                                              'and turns it back into a JavaScript object. It will throw a SyntaxError '
                                              'if the JSON has single quotes or trailing commas because JSON syntax '
                                              'requires double quotes.',
                               'missing_concepts': ['Replacer and Reviver parameters: Optional second arguments allow '
                                                    'custom transformation during serialization (filtering/formatting '
                                                    'keys) and deserialization (e.g., converting ISO date strings back '
                                                    'into Date objects)']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'JSON.stringify is used to convert a JavaScript object into a text '
                                              'string so you can send it to an API or save it in LocalStorage. '
                                              'JSON.parse takes that string and turns it back into an object so you '
                                              'can access properties like user.name. In JSON, all keys must have '
                                              'double quotes around them. If the JSON string has bad formatting, '
                                              'JSON.parse throws an error.',
                               'missing_concepts': ['JSON.stringify(value, replacer, space): Serializes JavaScript '
                                                    'objects into JSON strings; silently omits functions, undefined, '
                                                    'and symbols (or turns them into null inside arrays); throws '
                                                    'TypeError on circular references',
                                                    'Replacer and Reviver parameters: Optional second arguments allow '
                                                    'custom transformation during serialization (filtering/formatting '
                                                    'keys) and deserialization (e.g., converting ISO date strings back '
                                                    'into Date objects)']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'JSON.parse converts a JavaScript file into a SQL database table. '
                                              'JSON.stringify turns strings into binary machine code. In JSON, keys '
                                              'can be numbers, variables, or functions without quotes.',
                               'missing_concepts': ['JSON data format rules: Plain text data interchange format; keys '
                                                    'must be double-quoted strings; values must be strings, numbers, '
                                                    'booleans, null, arrays, or nested objects (no undefined, '
                                                    'functions, or circular references)',
                                                    'JSON.stringify(value, replacer, space): Serializes JavaScript '
                                                    'objects into JSON strings; silently omits functions, undefined, '
                                                    'and symbols (or turns them into null inside arrays); throws '
                                                    'TypeError on circular references',
                                                    'JSON.parse(text, reviver): Deserializes a valid JSON string into '
                                                    'a JavaScript object/value; throws a SyntaxError if the string is '
                                                    'malformed (e.g. single quotes or trailing commas)',
                                                    'Replacer and Reviver parameters: Optional second arguments allow '
                                                    'custom transformation during serialization (filtering/formatting '
                                                    'keys) and deserialization (e.g., converting ISO date strings back '
                                                    'into Date objects)']}]},
          {'topic_tag': 'Client-Side vs Server-Side Rendering',
           'question': 'Compare Client-Side Rendering (CSR) and Server-Side Rendering (SSR) regarding initial load '
                       'performance and SEO.',
           'keywords': ['Client-Side Rendering',
                        'Server-Side Rendering',
                        'Initial Page Load',
                        'SEO Impact',
                        'Bundle Size',
                        'HTML Generation'],
           'expected_concepts': ['Rendering architecture: CSR generates HTML dynamically in the browser via '
                                 'JavaScript; SSR renders full HTML strings on the web server per request and sends '
                                 'them to the browser',
                                 'Initial load metrics: CSR sends a minimal HTML shell with a large JS bundle, '
                                 'resulting in slower First Contentful Paint (FCP) and Largest Contentful Paint (LCP); '
                                 'SSR delivers pre-rendered HTML immediately, offering fast FCP and LCP',
                                 'Hydration requirement: SSR requires client-side hydration, where JavaScript '
                                 'downloads and attaches event listeners to pre-rendered HTML before the page becomes '
                                 'interactive (Time to Interactive - TTI)',
                                 'SEO implications: Search engine crawlers can immediately parse complete text content '
                                 'from SSR HTML; CSR relies on crawler JavaScript execution, which can cause indexing '
                                 'delays or failures'],
           'model_answer': 'Client-Side Rendering (CSR) and Server-Side Rendering (SSR) represent contrasting '
                           'rendering strategies with distinct trade-offs in performance, search engine indexing, and '
                           'server load: 1. Architecture: In standard CSR (traditional Single Page Applications using '
                           'Create React App or Vite), the server returns an essentially empty HTML document '
                           'containing a single root div (\'<div id="root"></div>\') and a large JavaScript bundle '
                           'tag. The browser downloads, parses, and executes the JavaScript, which then fetches data '
                           'via APIs and constructs the DOM entirely client-side. In SSR (using frameworks like '
                           "Next.js or Remix), the server receives the user's HTTP request, fetches necessary data, "
                           'executes the React component tree into a complete HTML string on the server, and returns '
                           'fully populated HTML to the browser. 2. Initial Load Performance (FCP & LCP): - CSR '
                           'suffers from slower First Contentful Paint (FCP) and Largest Contentful Paint (LCP), '
                           'especially on low-power mobile devices or slow networks, because users see a blank white '
                           'screen or loading spinner until the entire JavaScript bundle is downloaded and evaluated. '
                           '- SSR provides superior FCP and LCP because the browser receives and displays meaningful '
                           'HTML text and imagery on the very first round trip. 3. Interactivity and Hydration: In '
                           'SSR, although HTML displays immediately, the page is not interactive until the JavaScript '
                           "bundle downloads and executes 'hydration'—the process where React attaches event listeners "
                           'to existing DOM nodes. If hydration is slow, it creates a gap between FCP and Time to '
                           'Interactive (TTI). 4. SEO Impact: SSR is vastly superior for Search Engine Optimization. '
                           'Web crawlers (Googlebot, Bingbot, social media scrapers) can immediately parse content and '
                           'meta tags from the raw HTML response. While Googlebot executes JavaScript, it operates on '
                           'a separate deferred render queue; social media link previews (Twitter cards, Facebook '
                           'OpenGraph) do not execute JavaScript at all and fail on pure CSR pages.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'The core difference between Client-Side Rendering (CSR) and Server-Side '
                                              'Rendering (SSR) lies in where the HTML is generated, which dramatically '
                                              'impacts initial load performance and SEO. In CSR—typical of traditional '
                                              'SPAs—the server sends back an empty HTML shell with just a <div '
                                              "id='root'></div> and a script tag pointing to a big JavaScript bundle. "
                                              'The browser has to download, parse, and execute all that JavaScript, '
                                              'make API calls, and build the DOM dynamically. This results in a poor '
                                              'First Contentful Paint (FCP) and Largest Contentful Paint (LCP) because '
                                              'the user is stuck looking at a blank screen or a spinner until the '
                                              'bundle finishes executing. In SSR—used in frameworks like Next.js—the '
                                              'server executes the components on the backend for each incoming '
                                              'request, fetches data, and returns fully rendered HTML to the browser. '
                                              'The browser can paint that HTML immediately, resulting in fast FCP and '
                                              "LCP. However, SSR requires 'hydration': the client still has to "
                                              'download JavaScript and attach event listeners to that HTML before the '
                                              'page is actually interactive (Time to Interactive). When it comes to '
                                              'SEO, SSR is significantly better. Web crawlers and social media link '
                                              'scrapers like Twitter or LinkedIn receive full HTML with all content '
                                              'and meta tags immediately. While Googlebot can execute JS, it uses a '
                                              'deferred queue that can delay indexing by days, and social media '
                                              "scrapers don't run JavaScript at all.",
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'In Client-Side Rendering, the server returns an empty HTML file and a '
                                              'JavaScript bundle, and the browser builds the entire page using '
                                              'JavaScript. This makes initial load slower because the user has to wait '
                                              'for JavaScript to download and run before seeing content. In '
                                              'Server-Side Rendering, the server generates the HTML with content '
                                              'already inside and sends it to the browser, so the user sees the page '
                                              'much faster. SSR is also much better for SEO because search engine bots '
                                              'can easily read the content in the HTML without needing to execute '
                                              'JavaScript, whereas CSR can cause indexing issues.',
                               'missing_concepts': ['Hydration requirement: SSR requires client-side hydration, where '
                                                    'JavaScript downloads and attaches event listeners to pre-rendered '
                                                    'HTML before the page becomes interactive (Time to Interactive - '
                                                    'TTI)']},
                              {'quality_level': 'average',
                               'human_score': 61,
                               'answer_text': "CSR is client-side rendering where React runs in the user's browser, "
                                              'like in standard SPAs. SSR is server-side rendering where the server '
                                              'generates the HTML, like in Next.js. SSR is faster for the initial page '
                                              'load because the server already created the HTML. SSR is also much '
                                              'better for SEO because Google can read the text directly in the HTML '
                                              'source code, while CSR shows an empty div tag in view source.',
                               'missing_concepts': ['Initial load metrics: CSR sends a minimal HTML shell with a large '
                                                    'JS bundle, resulting in slower First Contentful Paint (FCP) and '
                                                    'Largest Contentful Paint (LCP); SSR delivers pre-rendered HTML '
                                                    'immediately, offering fast FCP and LCP',
                                                    'Hydration requirement: SSR requires client-side hydration, where '
                                                    'JavaScript downloads and attaches event listeners to pre-rendered '
                                                    'HTML before the page becomes interactive (Time to Interactive - '
                                                    'TTI)']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': "CSR runs on the database server and SSR runs inside the user's "
                                              'smartphone CPU. SSR makes website bundle sizes 10 times larger than '
                                              'CSR. Google cannot index SSR websites because server-side rendering '
                                              'encrypts the HTML.',
                               'missing_concepts': ['Rendering architecture: CSR generates HTML dynamically in the '
                                                    'browser via JavaScript; SSR renders full HTML strings on the web '
                                                    'server per request and sends them to the browser',
                                                    'Initial load metrics: CSR sends a minimal HTML shell with a large '
                                                    'JS bundle, resulting in slower First Contentful Paint (FCP) and '
                                                    'Largest Contentful Paint (LCP); SSR delivers pre-rendered HTML '
                                                    'immediately, offering fast FCP and LCP',
                                                    'Hydration requirement: SSR requires client-side hydration, where '
                                                    'JavaScript downloads and attaches event listeners to pre-rendered '
                                                    'HTML before the page becomes interactive (Time to Interactive - '
                                                    'TTI)',
                                                    'SEO implications: Search engine crawlers can immediately parse '
                                                    'complete text content from SSR HTML; CSR relies on crawler '
                                                    'JavaScript execution, which can cause indexing delays or '
                                                    'failures']}]},
          {'topic_tag': 'Web Accessibility (WCAG & ARIA)',
           'question': 'How do WCAG accessibility guidelines and WAI-ARIA roles make web applications accessible to '
                       'screen readers?',
           'keywords': ['Web Accessibility',
                        'WCAG Guidelines',
                        'ARIA Attributes',
                        'Screen Readers',
                        'Keyboard Navigation',
                        'Color Contrast'],
           'expected_concepts': ['WCAG Principles (POUR): Web Content Accessibility Guidelines are built around four '
                                 'core principles: Perceivable, Operable, Understandable, and Robust',
                                 'Semantic HTML as the baseline: Native HTML elements (<button>, <input>, <nav>) '
                                 'provide built-in keyboard accessibility (Tab navigation) and native accessibility '
                                 'tree roles',
                                 "WAI-ARIA roles and states: ARIA attributes (role='dialog', aria-expanded, "
                                 'aria-label, aria-live) bridge semantic gaps for custom interactive widgets without '
                                 'changing visual appearance',
                                 'Visual and physical accessibility: Meeting contrast requirements (minimum 4.5:1 for '
                                 'standard text), supporting full keyboard navigation (focus rings, no keyboard '
                                 'traps), and screen reader announcements'],
           'model_answer': 'Web accessibility (a11y) ensures that digital products are usable by individuals with '
                           'visual, auditory, motor, or cognitive disabilities. 1. WCAG Guidelines (POUR): The Web '
                           'Content Accessibility Guidelines (WCAG 2.1 / 2.2), developed by the W3C, are structured '
                           'around four foundational principles: - Perceivable: Information and UI components must be '
                           'presentable to users in ways they can perceive (e.g., text alternatives via alt '
                           'attributes, minimum 4.5:1 color contrast ratio for normal text). - Operable: UI components '
                           'and navigation must be operable (e.g., full keyboard accessibility without requiring a '
                           'mouse, clear visual focus indicators, and no keyboard traps). - Understandable: '
                           'Information and UI operation must be understandable (e.g., predictable navigation, clear '
                           'form error identification). - Robust: Content must be robust enough to be reliably '
                           'interpreted by assistive technologies. 2. Semantic HTML First: The first rule of '
                           'accessibility is to use native semantic HTML elements whenever possible (<button> instead '
                           'of <div onclick>). Native elements automatically expose accessible names, keyboard '
                           'focusability via Tab, and built-in keyboard event handlers (Enter/Space). 3. WAI-ARIA '
                           '(Accessible Rich Internet Applications): When building custom complex UI widgets (modals, '
                           'accordions, tabs, comboboxes) where native HTML falls short, ARIA fills the semantic gap: '
                           "- Roles: Define widget type (role='dialog', role='tablist', role='progressbar'). - States "
                           '& Properties: Communicate dynamic state changes to screen readers '
                           "(aria-expanded='true/false', aria-checked, aria-disabled). - Accessible Names: Provide "
                           "labels when visible text is absent (aria-label='Close menu'). - Live Regions: "
                           '\'aria-live="polite/assertive"\' informs screen readers to announce dynamic content '
                           'updates (like toast alerts or shopping cart totals) without requiring user focus.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'Web accessibility ensures that all users, including those relying on '
                                              'screen readers or keyboard navigation, can perceive and interact with '
                                              'web applications. WCAG is structured around four core principles, known '
                                              'as POUR: Perceivable (like providing alt text on images and maintaining '
                                              'a 4.5:1 color contrast ratio), Operable (meaning all functionality must '
                                              'be navigable using only the keyboard without keyboard traps), '
                                              'Understandable (clear labels and error messages), and Robust '
                                              '(compatible with screen readers like NVDA or VoiceOver). The foundation '
                                              'of accessibility is semantic HTML: using native <button>, <input>, and '
                                              '<nav> tags gives you built-in keyboard focusability with Tab and '
                                              'Space/Enter key handlers for free. WAI-ARIA comes in when native HTML '
                                              'cannot describe a custom widget. ARIA provides three key things: 1. '
                                              "Roles, like role='dialog' or role='tab', which tell the screen reader "
                                              'what kind of component it is. 2. States and properties, like '
                                              "aria-expanded='true' on an accordion or aria-haspopup='menu', which "
                                              'inform the user about dynamic changes. 3. Accessible labeling and live '
                                              'regions, like aria-label for icon buttons that have no visible text, '
                                              "and aria-live='polite' so that screen readers automatically announce "
                                              'dynamic content updates like toast notifications without moving the '
                                              "user's focus.",
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'WCAG defines accessibility standards based on four principles: '
                                              'perceivable, operable, understandable, and robust. It covers things '
                                              'like having good color contrast so text is readable, and making sure '
                                              'the entire website can be navigated using only the keyboard. Using '
                                              'native semantic HTML elements like button and nav is the best practice '
                                              'because they have accessibility built in. WAI-ARIA attributes help when '
                                              "you build custom components like modals or tabs. You use role='dialog', "
                                              'aria-label to give text to icon buttons, and aria-expanded to tell '
                                              'screen readers if a dropdown menu is open or closed.',
                               'missing_concepts': ['Visual and physical accessibility: Meeting contrast requirements '
                                                    '(minimum 4.5:1 for standard text), supporting full keyboard '
                                                    'navigation (focus rings, no keyboard traps), and screen reader '
                                                    'announcements']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'WCAG is the web accessibility guidelines that websites must follow so '
                                              'disabled users can use the site. Screen readers like VoiceOver read out '
                                              'the HTML to blind users. You should always use semantic HTML tags like '
                                              '<button> instead of <div> tags. ARIA attributes are extra HTML '
                                              'attributes like aria-label and role that help screen readers understand '
                                              "custom dropdowns or modals when plain HTML doesn't have a tag for it. "
                                              'It also requires good color contrast.',
                               'missing_concepts': ['WCAG Principles (POUR): Web Content Accessibility Guidelines are '
                                                    'built around four core principles: Perceivable, Operable, '
                                                    'Understandable, and Robust',
                                                    'Visual and physical accessibility: Meeting contrast requirements '
                                                    '(minimum 4.5:1 for standard text), supporting full keyboard '
                                                    'navigation (focus rings, no keyboard traps), and screen reader '
                                                    'announcements']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'Accessibility means making sure the website loads in under 1 second. '
                                              'ARIA is a CSS framework like Bootstrap that adds icons to buttons. '
                                              'Screen readers cannot read HTML text unless it is translated into '
                                              'Braille binary code using JavaScript.',
                               'missing_concepts': ['WCAG Principles (POUR): Web Content Accessibility Guidelines are '
                                                    'built around four core principles: Perceivable, Operable, '
                                                    'Understandable, and Robust',
                                                    'Semantic HTML as the baseline: Native HTML elements (<button>, '
                                                    '<input>, <nav>) provide built-in keyboard accessibility (Tab '
                                                    'navigation) and native accessibility tree roles',
                                                    "WAI-ARIA roles and states: ARIA attributes (role='dialog', "
                                                    'aria-expanded, aria-label, aria-live) bridge semantic gaps for '
                                                    'custom interactive widgets without changing visual appearance',
                                                    'Visual and physical accessibility: Meeting contrast requirements '
                                                    '(minimum 4.5:1 for standard text), supporting full keyboard '
                                                    'navigation (focus rings, no keyboard traps), and screen reader '
                                                    'announcements']}]}],
 'medium': [{'topic_tag': 'React useEffect Hook Cleanup',
             'question': "Why is the cleanup function essential in React's useEffect hook when setting up event "
                         'listeners or timers?',
             'keywords': ['useEffect',
                          'Dependency Array',
                          'Cleanup Function',
                          'Side Effects',
                          'Component Unmount',
                          'Infinite Loop Prevention'],
             'expected_concepts': ['Cleanup timing: The returned cleanup function runs both when the component '
                                   'unmounts AND right before re-running the effect on dependency change',
                                   'Preventing memory leaks: Leaving subscriptions, timers (setInterval/setTimeout), '
                                   'or global event listeners active causes orphaned references in memory',
                                   'Preventing stale closures and duplicate callbacks: Uncleaned window/DOM listeners '
                                   'accumulate on every render, executing multiple duplicate callbacks with outdated '
                                   'state closures',
                                   'Cancelling network requests: AbortController can be wired into the cleanup '
                                   'function to cancel inflight HTTP fetches if dependencies change or component '
                                   'unmounts'],
             'model_answer': "In React's 'useEffect' hook, returning a cleanup function (return () => { ... }) is "
                             'critical for managing component side effects safely. 1. Execution Timing: A common '
                             'misconception is that the cleanup function only runs on component unmount. In reality, '
                             'React executes the cleanup function in two scenarios: first, immediately prior to '
                             're-executing the effect when any value in the dependency array changes; and second, when '
                             'the component unmounts from the DOM. 2. Preventing Memory Leaks: If an effect '
                             "establishes a persistent resource—such as starting a 'setInterval', subscribing to a "
                             'WebSocket, or registering an observer (IntersectionObserver)—omitting a cleanup function '
                             'leaves that background process running indefinitely after the component has unmounted. '
                             'These orphaned callbacks retain references to component scope, preventing garbage '
                             'collection and leaking memory. 3. Preventing Duplicate Event Handlers & Stale Closures: '
                             "If you attach a global event listener (window.addEventListener('resize', handleResize)) "
                             'without removing it in cleanup (window.removeEventListener), every single render that '
                             'triggers the effect adds an additional event listener. Over time, a single resize event '
                             'fires dozens of duplicate callbacks, each closing over stale props or state from '
                             'previous render cycles. 4. Aborting In-Flight Requests: Wiring an AbortController into '
                             'useEffect cleanup allows developers to abort obsolete network fetches '
                             '(controller.abort()) when users navigate away or update query filters, preventing race '
                             'conditions and warnings about state updates on unmounted components.',
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 96,
                                 'answer_text': 'The cleanup function in useEffect is essential for two reasons: '
                                                'preventing memory leaks and avoiding duplicate event handlers with '
                                                "stale closures. It's important to understand when the cleanup "
                                                'function actually runs: it runs when the component unmounts, but it '
                                                'also runs right before the effect re-runs whenever any dependency in '
                                                'the dependency array changes. If you set up a timer like setInterval '
                                                "or an event listener like window.addEventListener('scroll', onScroll) "
                                                'without returning a cleanup function that calls clearInterval or '
                                                'removeEventListener, several bad things happen: First, on every '
                                                're-render where dependencies change, you add another event listener '
                                                'without removing the old one. If the component re-renders five times, '
                                                'five separate callbacks fire on every scroll event. Second, those '
                                                'orphaned listeners hold onto closures containing outdated state and '
                                                'props from earlier renders, causing subtle stale-state bugs. Third, '
                                                'once the component unmounts, the interval or listener keeps running '
                                                'in the background, holding memory and potentially calling setState on '
                                                'an unmounted component. Another great practical use is with fetch '
                                                'requests: you can create an AbortController in the effect and call '
                                                'controller.abort() in the cleanup function so that if the user clicks '
                                                'away or changes a filter before the request finishes, the pending '
                                                'network request is cleanly cancelled.',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'The cleanup function in useEffect is necessary to clean up side '
                                                'effects before the component unmounts or before the effect runs '
                                                'again. If you set up an interval with setInterval or add an event '
                                                'listener to the window object, you must remove them in the cleanup '
                                                'function using clearInterval or window.removeEventListener. '
                                                'Otherwise, those listeners will accumulate on every render, causing '
                                                'memory leaks and running multiple duplicate callbacks. You can also '
                                                'use the cleanup function with an AbortController to cancel pending '
                                                'API calls when dependencies change.',
                                 'missing_concepts': ['Preventing stale closures and duplicate callbacks: Uncleaned '
                                                      'window/DOM listeners accumulate on every render, executing '
                                                      'multiple duplicate callbacks with outdated state closures']},
                                {'quality_level': 'average',
                                 'human_score': 61,
                                 'answer_text': 'The cleanup function in useEffect is a function that you return at '
                                                'the end of the effect, like return () => clearInterval(timer). It '
                                                'runs when the component unmounts to prevent memory leaks. If you '
                                                "don't clean up a setInterval timer, it will keep running in the "
                                                "background forever even after the user leaves the page. It's the "
                                                'functional equivalent of componentWillUnmount in old class '
                                                'components.',
                                 'missing_concepts': ['Cleanup timing: The returned cleanup function runs both when '
                                                      'the component unmounts AND right before re-running the effect '
                                                      'on dependency change',
                                                      'Cancelling network requests: AbortController can be wired into '
                                                      'the cleanup function to cancel inflight HTTP fetches if '
                                                      'dependencies change or component unmounts']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': "The cleanup function is used to delete the component's state from the "
                                                "Redux store. If you don't return a cleanup function, React crashes "
                                                'with an infinite re-render error. You should only use cleanup '
                                                'functions when connecting to MongoDB databases.',
                                 'missing_concepts': ['Cleanup timing: The returned cleanup function runs both when '
                                                      'the component unmounts AND right before re-running the effect '
                                                      'on dependency change',
                                                      'Preventing memory leaks: Leaving subscriptions, timers '
                                                      '(setInterval/setTimeout), or global event listeners active '
                                                      'causes orphaned references in memory',
                                                      'Preventing stale closures and duplicate callbacks: Uncleaned '
                                                      'window/DOM listeners accumulate on every render, executing '
                                                      'multiple duplicate callbacks with outdated state closures',
                                                      'Cancelling network requests: AbortController can be wired into '
                                                      'the cleanup function to cancel inflight HTTP fetches if '
                                                      'dependencies change or component unmounts']}]},
            {'topic_tag': 'React Virtual DOM & Reconciliation',
             'question': "How does React's Fiber reconciliation algorithm update the real DOM efficiently using "
                         'Virtual DOM diffing?',
             'keywords': ['Virtual DOM',
                          'Reconciliation',
                          'Fiber Architecture',
                          'Diffing Algorithm',
                          'Batching Updates',
                          'DOM Operations'],
             'expected_concepts': ['Virtual DOM is an in-memory lightweight JavaScript object tree mirroring the '
                                   'actual DOM, enabling cheap diffing without touching slow browser layout engines',
                                   'Heuristic O(n) diffing assumptions: Two elements of different types produce '
                                   'different trees; keys uniquely identify children across renders to handle '
                                   'reordering efficiently',
                                   'React Fiber two-phase architecture: Render phase (asynchronous, interruptible, '
                                   'calculates work-in-progress fiber tree and diffs changes) vs Commit phase '
                                   '(synchronous, executes real DOM mutations and layout)',
                                   'Time-slicing and prioritization: Fiber splits reconciliation into discrete units '
                                   'of work, yielding control back to the browser main thread to maintain 60fps '
                                   'responsiveness during heavy updates'],
             'model_answer': 'React optimizes DOM manipulation—traditionally the slowest operation in browser '
                             'rendering—through the Virtual DOM (VDOM) and the Fiber reconciliation engine: 1. The '
                             'Virtual DOM: The VDOM is an in-memory tree of lightweight JavaScript objects '
                             'representing the desired UI state. Creating and comparing plain JS objects takes '
                             'fractions of a millisecond, avoiding expensive browser layout recalculations and '
                             'repaints. 2. Heuristic O(n) Diffing Algorithm: Finding the minimum edit distance between '
                             'two arbitrary trees has O(n^3) complexity, which is unacceptable for UI. React applies '
                             'two practical heuristics to achieve linear O(n) diffing: - Different Types: If an '
                             'element changes type (<div> to <span>, or <Header> to <Nav>), React unmounts the old '
                             'subtree completely and builds the new tree from scratch. - Keys in Lists: When diffing '
                             "child collections, React relies on stable 'key' props. Instead of re-rendering every "
                             'item when a new element is inserted at the start of a list, keys allow React to identify '
                             'moved, inserted, or deleted nodes. 3. React Fiber Architecture: React 16 completely '
                             "rewrote the reconciler with 'Fiber'—a singly linked list tree of fiber nodes "
                             'representing units of work. Fiber divides rendering into two distinct phases: - Render '
                             'Phase (Reconciliation): Asynchronous and interruptible. React walks the fiber tree, '
                             'evaluates component functions, diffs changes against the current fiber tree, and flags '
                             "'effects' (insertions, updates, deletions). If higher-priority work (user typing, "
                             'animations) arrives, Fiber can pause, abort, or yield work to the browser main thread '
                             '(cooperative multitasking/time-slicing). - Commit Phase: Synchronous and '
                             'non-interruptible. React takes the completed work-in-progress fiber tree and applies all '
                             'mutations to the real host DOM in one rapid batch, invoking lifecycle hooks and layout '
                             'effects.',
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 97,
                                 'answer_text': "React's reconciliation engine uses an in-memory Virtual DOM combined "
                                                'with the Fiber architecture to update the real DOM with maximum '
                                                'efficiency. Direct DOM manipulation is expensive because reading and '
                                                'writing to the real DOM forces the browser to recalculate styles, '
                                                'execute layout, and repaint pixels. React solves this by keeping an '
                                                'in-memory tree of plain JavaScript objects representing the UI. To '
                                                'make tree comparison practical, React uses an O(n) heuristic diffing '
                                                'algorithm based on two assumptions: First, if two elements have '
                                                'different types (like changing a <div> to a <section>), React tears '
                                                'down the old subtree completely. Second, in lists of children, stable '
                                                'keys allow React to track which items moved, were added, or were '
                                                'removed rather than mutating every node. The true magic came with the '
                                                'React 16 Fiber rewrite. In the old stack reconciler, reconciliation '
                                                'was recursive and synchronous—meaning a large component update would '
                                                'freeze the browser main thread and drop frames. Fiber restructured '
                                                "the tree into a linked list where each component is a 'fiber' "
                                                'representing a unit of work. This divides reconciliation into two '
                                                'phases: The Render phase is asynchronous and interruptible. React can '
                                                'pause work, yield to the browser to handle user keystrokes or '
                                                'animations (time-slicing), and resume later. Once all diffing is '
                                                'complete, it enters the Commit phase, which is synchronous and very '
                                                'fast, applying all the calculated DOM mutations in one batch so the '
                                                'browser only repaints once.',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'The Virtual DOM is a lightweight JavaScript representation of the '
                                                'actual DOM. When state changes, React builds a new Virtual DOM tree '
                                                'and compares it to the previous one using an O(n) diffing algorithm. '
                                                'It checks if element types have changed and uses key attributes to '
                                                'track items in lists. With the Fiber architecture, React splits this '
                                                'work into small units. The Render phase is interruptible, meaning '
                                                'React can pause diffing if higher priority tasks like user input '
                                                'arrive. Once the diffing is finished, the Commit phase applies all '
                                                'the actual DOM updates to the browser synchronously in a single batch '
                                                'to avoid layout thrashing.',
                                 'missing_concepts': ['Time-slicing and prioritization: Fiber splits reconciliation '
                                                      'into discrete units of work, yielding control back to the '
                                                      'browser main thread to maintain 60fps responsiveness during '
                                                      'heavy updates']},
                                {'quality_level': 'average',
                                 'human_score': 61,
                                 'answer_text': 'The Virtual DOM is a copy of the real DOM kept in memory. When you '
                                                'update state, React creates a new virtual DOM and compares it with '
                                                'the old virtual DOM to see what changed, which is called diffing. It '
                                                'then only updates the specific HTML elements that changed in the real '
                                                'DOM instead of reloading the entire page. Fiber is the internal '
                                                'algorithm in React that makes this diffing process faster and allows '
                                                'React to prioritize important updates like button clicks.',
                                 'missing_concepts': ['Heuristic O(n) diffing assumptions: Two elements of different '
                                                      'types produce different trees; keys uniquely identify children '
                                                      'across renders to handle reordering efficiently',
                                                      'React Fiber two-phase architecture: Render phase (asynchronous, '
                                                      'interruptible, calculates work-in-progress fiber tree and diffs '
                                                      'changes) vs Commit phase (synchronous, executes real DOM '
                                                      'mutations and layout)']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': 'The Virtual DOM is a WebGL 3D rendering engine built into React. '
                                                'Fiber is a fiber-optic cable protocol that sends HTML directly from '
                                                'the server to the graphics card. Reconciliation is when React deletes '
                                                'the entire HTML document and downloads a fresh copy from GitHub.',
                                 'missing_concepts': ['Virtual DOM is an in-memory lightweight JavaScript object tree '
                                                      'mirroring the actual DOM, enabling cheap diffing without '
                                                      'touching slow browser layout engines',
                                                      'Heuristic O(n) diffing assumptions: Two elements of different '
                                                      'types produce different trees; keys uniquely identify children '
                                                      'across renders to handle reordering efficiently',
                                                      'React Fiber two-phase architecture: Render phase (asynchronous, '
                                                      'interruptible, calculates work-in-progress fiber tree and diffs '
                                                      'changes) vs Commit phase (synchronous, executes real DOM '
                                                      'mutations and layout)',
                                                      'Time-slicing and prioritization: Fiber splits reconciliation '
                                                      'into discrete units of work, yielding control back to the '
                                                      'browser main thread to maintain 60fps responsiveness during '
                                                      'heavy updates']}]},
            {'topic_tag': 'State Management Libraries Comparison',
             'question': 'Compare Redux Toolkit, Context API, and Zustand for state management in large-scale React '
                         'applications.',
             'keywords': ['Redux Toolkit', 'Context API', 'Zustand', 'Global State', 'Prop Drilling', 'Store Slices'],
             'expected_concepts': ['React Context API: Built-in solution ideal for low-frequency global state (theme, '
                                   'auth); suffers from performance bottlenecks because any state change re-renders '
                                   'all consuming components regardless of which slice they use',
                                   'Redux Toolkit (RTK): Centralized immutable store with unidirectional data flow '
                                   '(actions, reducers, createSlice, RTK Query); excellent debugging with Redux '
                                   'DevTools and time-travel, but carries more boilerplate and conceptual overhead',
                                   'Zustand: Minimalist hook-based store (~1KB) outside React tree; supports '
                                   'fine-grained selector subscriptions (only re-renders component when selected state '
                                   'changes) with zero boilerplate and no Provider wrapper',
                                   'Selection criteria for large apps: Use Context for static/infrequent data; use '
                                   'Zustand for simple-to-medium dynamic state with minimal bundle cost; use RTK for '
                                   'complex, multi-developer enterprise apps needing strict patterns and caching'],
             'model_answer': 'Choosing among React Context API, Redux Toolkit (RTK), and Zustand requires evaluating '
                             'application complexity, developer ergonomics, and re-rendering performance: 1. React '
                             'Context API: Context is built directly into React (createContext, useContext) and '
                             'requires no external dependencies. It is ideal for low-frequency, static global data '
                             'like user authentication sessions, localization strings, or UI themes. However, Context '
                             'is not a true state management library—it is a dependency injection mechanism. Its '
                             'primary architectural flaw in large applications is re-rendering: whenever the Context '
                             'value updates, every component subscribed via useContext re-renders, even if it only '
                             'consumes an unchanged property on that object. Mitigating this requires fragmenting '
                             'state across dozens of nested Context Providers. 2. Redux Toolkit (RTK): RTK is the '
                             'opinionated, industry-standard implementation of Redux. It enforces strict '
                             'unidirectional data flow through slices (createSlice), immutable updates via Immer, '
                             'typed dispatch, and async data management with RTK Query. Its strengths are '
                             'enterprise-grade predictability, powerful middleware, and unmatched debugging through '
                             'Redux DevTools (time-travel debugging). Its drawbacks are a steeper learning curve, '
                             'higher boilerplate than competitors, and a larger bundle footprint. 3. Zustand: A '
                             'lightweight (~1KB), hook-based state management library created by Poimandres. Zustand '
                             'stores live outside the React tree, requiring no Provider wrapper. Its defining '
                             "advantage is selector-based subscriptions: 'const bears = useStore(state => "
                             "state.bears)'. A component re-renders ONLY when the specific sliced value returned by "
                             "its selector changes, solving Context's re-render bottleneck with near-zero boilerplate. "
                             'Zustand also supports middleware (persist, devtools, immer) seamlessly. Summary: Use '
                             'Context for infrequent global settings; choose Zustand for high-performance, modern '
                             'React apps prioritizing simplicity and speed; choose Redux Toolkit for complex '
                             'enterprise architectures requiring strict conventions, complex caching (RTK Query), and '
                             'comprehensive audit trails.',
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 96,
                                 'answer_text': 'Comparing Context API, Redux Toolkit, and Zustand comes down to '
                                                'performance, boilerplate, and application scale. 1. Context API is '
                                                "built directly into React, so there are no extra dependencies. It's "
                                                'great for low-velocity global state that rarely changes, like dark '
                                                'mode theme or current user auth. The critical downside in large apps '
                                                'is re-rendering: when a Context value changes, every single component '
                                                'using useContext(MyContext) re-renders, even if the specific property '
                                                "that component cares about didn't change. Splitting state into "
                                                "multiple separate Context providers helps, but leads to 'provider "
                                                "hell'. 2. Redux Toolkit (RTK) is the official, modernized version of "
                                                'Redux. It enforces strict unidirectional data flow using createSlice '
                                                'and Immer for immutable state. Its greatest strength is '
                                                'predictability in large enterprise teams, along with Redux DevTools '
                                                'for time-travel debugging and RTK Query for automated server state '
                                                'caching. The trade-off is higher boilerplate, steeper learning curve, '
                                                'and a larger bundle size. 3. Zustand is a modern, lightweight (around '
                                                '1KB) store that lives outside the React component tree, meaning you '
                                                "don't even need a top-level Provider. Its superpower is "
                                                "selector-based subscriptions: you write 'const name = useStore(s => "
                                                "s.name)', and that component will ONLY re-render when 'name' changes. "
                                                'It gives you the performance and selector power of Redux with almost '
                                                'zero boilerplate. In a large app, I use Context for themes, Zustand '
                                                'for shared client state, and RTK or TanStack Query if there is '
                                                'complex data fetching and enterprise tooling requirements.',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'Context API is built into React and is great for simple things like '
                                                'theme switching or language preferences. However, it causes '
                                                'performance issues in large apps because whenever the context value '
                                                'changes, every component consuming that context re-renders. Redux '
                                                'Toolkit provides a centralized store with actions, reducers, and '
                                                'slices. It is very predictable, has great DevTools for debugging, and '
                                                'includes RTK Query for caching, but it has more boilerplate. Zustand '
                                                "is a lightweight alternative that uses hooks and doesn't require a "
                                                'Provider. It uses selectors so components only re-render when the '
                                                'selected piece of state changes, making it much faster than Context '
                                                'with very little boilerplate.',
                                 'missing_concepts': ['Selection criteria for large apps: Use Context for '
                                                      'static/infrequent data; use Zustand for simple-to-medium '
                                                      'dynamic state with minimal bundle cost; use RTK for complex, '
                                                      'multi-developer enterprise apps needing strict patterns and '
                                                      'caching']},
                                {'quality_level': 'average',
                                 'human_score': 61,
                                 'answer_text': "Context API comes with React so you don't need to install npm "
                                                'packages. It avoids prop drilling by letting you pass data directly '
                                                'to deep components. Redux Toolkit is the standard state library that '
                                                "uses actions, reducers, and dispatch. It's used by big companies "
                                                'because it has Redux DevTools to track state changes. Zustand is a '
                                                'newer, simpler library that lets you create a global store using a '
                                                'custom hook without wrapping your app in a Provider. Zustand is '
                                                'easier to learn than Redux.',
                                 'missing_concepts': ['React Context API: Built-in solution ideal for low-frequency '
                                                      'global state (theme, auth); suffers from performance '
                                                      'bottlenecks because any state change re-renders all consuming '
                                                      'components regardless of which slice they use',
                                                      'Zustand: Minimalist hook-based store (~1KB) outside React tree; '
                                                      'supports fine-grained selector subscriptions (only re-renders '
                                                      'component when selected state changes) with zero boilerplate '
                                                      'and no Provider wrapper']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': 'Redux Toolkit is deprecated in React 18 and was replaced by Context '
                                                'API. Zustand is a CSS styling framework. In large-scale apps, you '
                                                'should store all global state in localStorage and read it '
                                                'synchronously in every component render.',
                                 'missing_concepts': ['React Context API: Built-in solution ideal for low-frequency '
                                                      'global state (theme, auth); suffers from performance '
                                                      'bottlenecks because any state change re-renders all consuming '
                                                      'components regardless of which slice they use',
                                                      'Redux Toolkit (RTK): Centralized immutable store with '
                                                      'unidirectional data flow (actions, reducers, createSlice, RTK '
                                                      'Query); excellent debugging with Redux DevTools and '
                                                      'time-travel, but carries more boilerplate and conceptual '
                                                      'overhead',
                                                      'Zustand: Minimalist hook-based store (~1KB) outside React tree; '
                                                      'supports fine-grained selector subscriptions (only re-renders '
                                                      'component when selected state changes) with zero boilerplate '
                                                      'and no Provider wrapper',
                                                      'Selection criteria for large apps: Use Context for '
                                                      'static/infrequent data; use Zustand for simple-to-medium '
                                                      'dynamic state with minimal bundle cost; use RTK for complex, '
                                                      'multi-developer enterprise apps needing strict patterns and '
                                                      'caching']}]},
            {'topic_tag': 'JavaScript Closures & Lexical Scope',
             'question': 'What is a JavaScript closure, and how does it maintain access to outer lexical scope '
                         'variables after the outer function returns?',
             'keywords': ['Closure',
                          'Lexical Scope',
                          'Outer Function Scope',
                          'Encapsulation',
                          'Private Variables',
                          'Memory Retention'],
             'expected_concepts': ['Definition: A closure is the combination of a function bundled together with '
                                   'references to its surrounding lexical environment (its outer lexical scope)',
                                   'Mechanism: In JavaScript, functions retain a hidden [[Environment]] reference to '
                                   'the Lexical Environment record where they were declared, keeping referenced outer '
                                   "variables alive on the heap even after the outer function's execution context is "
                                   'popped off the call stack',
                                   'Use cases: Data encapsulation and private variables (factory functions/module '
                                   'pattern), function currying/partial application, and memoization',
                                   'Memory considerations: Closures prevent garbage collection of captured variables, '
                                   'so unneeded long-lived closures or circular references can cause unintentional '
                                   'memory leaks'],
             'model_answer': 'In JavaScript, a closure is the combination of a function bundled together with '
                             'references to its surrounding lexical environment. Formally, every JavaScript function '
                             'maintains an internal reference—the [[Environment]] internal slot—pointing to the '
                             'Lexical Environment record in which it was instantiated. 1. Mechanics of Scope '
                             'Retention: When an outer function executes, the JavaScript engine creates an Execution '
                             'Context and allocates an environment record holding its local variables. Normally, when '
                             'a function finishes executing, its execution context is popped off the Call Stack and '
                             'its memory is marked for garbage collection. However, if that outer function returns an '
                             'inner function that references those outer variables, a closure is formed. Because the '
                             'inner function maintains an active reference to the outer Lexical Environment, the '
                             'garbage collector recognizes that those outer variables are still reachable. '
                             'Consequently, the variables are preserved in heap memory, allowing the inner function to '
                             'read and mutate them long after the outer function has completed execution. 2. Practical '
                             'Applications: Closures are foundational to modern JavaScript: - Data Privacy / '
                             'Encapsulation: Emulating private object properties (e.g., function createCounter() { let '
                             "count = 0; return { increment() { count++; return count; } }; }). The variable 'count' "
                             'cannot be accessed or modified directly from outside code. - Function Factories and '
                             'Currying: Generating specialized functions (e.g., const multiplyByTwo = multiply(2)). - '
                             "State in React Hooks: The 'useState' and 'useEffect' hooks rely directly on closures to "
                             'preserve state values across successive component render executions. 3. Memory Caveats: '
                             'Captured variables remain in memory as long as the closure exists; failing to nullify '
                             'closures attached to global events can prevent garbage collection.',
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 96,
                                 'answer_text': 'A closure is a function bundled together with its surrounding lexical '
                                                'environment. In plain English, a closure gives an inner function '
                                                "access to an outer function's variables even after that outer "
                                                "function has returned. Here's how it works under the hood: In "
                                                'JavaScript, functions are first-class citizens and have an internal '
                                                'hidden property called [[Environment]] that stores a reference to the '
                                                'lexical scope where the function was born. When an outer function '
                                                'runs, its execution context is pushed onto the call stack and its '
                                                'local variables are created. When the function returns, its execution '
                                                'context is popped off the stack. Normally, those variables would be '
                                                'garbage collected. But if the outer function returns an inner '
                                                "function that references those outer variables, the inner function's "
                                                '[[Environment]] keeps a live pointer to that outer lexical '
                                                'environment. Because there is still an active reference in memory, '
                                                'the JavaScript garbage collector cannot sweep those variables—they '
                                                'are kept alive on the heap. This enables two massive patterns in '
                                                'JavaScript: First, data encapsulation and private variables—like a '
                                                'counter function where the count variable is private and can only be '
                                                'modified through exposed increment/decrement methods. Second, React '
                                                'Hooks like useState and useEffect rely directly on closures to '
                                                'remember state between component re-renders.',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'A closure happens when an inner function remembers and accesses '
                                                "variables from its outer function's scope, even after the outer "
                                                'function has finished executing and returned. When the outer function '
                                                'finishes, normally its variables would be cleaned up by garbage '
                                                'collection. But because the inner function still holds a reference to '
                                                'those variables in its lexical scope, JavaScript keeps them alive in '
                                                'memory. Closures are commonly used to create private variables that '
                                                'cannot be accessed directly from the outside, like creating a counter '
                                                'with getCount and increment methods, and they are also the foundation '
                                                'of how React hooks preserve state.',
                                 'missing_concepts': ['Memory considerations: Closures prevent garbage collection of '
                                                      'captured variables, so unneeded long-lived closures or circular '
                                                      'references can cause unintentional memory leaks']},
                                {'quality_level': 'average',
                                 'human_score': 61,
                                 'answer_text': 'A closure is when you have a function inside another function, and '
                                                'the inside function can use the variables of the outside function. '
                                                'Even after you call outer() and it finishes, if you save the inner '
                                                'function to a variable and call it later, it still remembers the '
                                                'outer variables. It is used to make private variables in JavaScript '
                                                "because JS didn't have private class fields in the past. It can "
                                                'sometimes cause memory leaks if you keep too many variables in '
                                                'memory.',
                                 'missing_concepts': ['Mechanism: In JavaScript, functions retain a hidden '
                                                      '[[Environment]] reference to the Lexical Environment record '
                                                      'where they were declared, keeping referenced outer variables '
                                                      "alive on the heap even after the outer function's execution "
                                                      'context is popped off the call stack',
                                                      'Use cases: Data encapsulation and private variables (factory '
                                                      'functions/module pattern), function currying/partial '
                                                      'application, and memoization']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': 'A closure is when you close a browser tab and JavaScript saves your '
                                                'variables to the hard drive. You create a closure by putting the '
                                                "'close' keyword inside a function. Closures only work in Node.js "
                                                'backend code.',
                                 'missing_concepts': ['Definition: A closure is the combination of a function bundled '
                                                      'together with references to its surrounding lexical environment '
                                                      '(its outer lexical scope)',
                                                      'Mechanism: In JavaScript, functions retain a hidden '
                                                      '[[Environment]] reference to the Lexical Environment record '
                                                      'where they were declared, keeping referenced outer variables '
                                                      "alive on the heap even after the outer function's execution "
                                                      'context is popped off the call stack',
                                                      'Use cases: Data encapsulation and private variables (factory '
                                                      'functions/module pattern), function currying/partial '
                                                      'application, and memoization',
                                                      'Memory considerations: Closures prevent garbage collection of '
                                                      'captured variables, so unneeded long-lived closures or circular '
                                                      'references can cause unintentional memory leaks']}]},
            {'topic_tag': 'JavaScript Prototype Chain',
             'question': 'How does prototypal inheritance work in JavaScript when resolving properties up the '
                         'prototype chain?',
             'keywords': ['Prototype Chain',
                          '__proto__',
                          'prototype Property',
                          'Inheritance',
                          'Object.create()',
                          'Property Lookup'],
             'expected_concepts': ['Prototypal inheritance model: Unlike classical class-based languages, JavaScript '
                                   'objects inherit directly from other objects via an internal link [[Prototype]] '
                                   '(accessible via Object.getPrototypeOf() or legacy __proto__)',
                                   'Property lookup mechanism: When accessing obj.prop, the engine checks obj; if not '
                                   'found, it ascends obj.[[Prototype]], continuing recursively until found or '
                                   'reaching null (the end of the prototype chain: Object.prototype.[[Prototype]] === '
                                   'null)',
                                   'Constructor.prototype vs instance.__proto__: Function constructors have a '
                                   "'prototype' property that becomes the [[Prototype]] assigned to all instances "
                                   "instantiated with 'new Constructor()'",
                                   "Shadowing and performance: Defining a property directly on an instance 'shadows' "
                                   'matching properties on its prototype; deep prototype chains can slow down property '
                                   'lookup for missing properties'],
             'model_answer': 'JavaScript is built on a prototypal inheritance model rather than classical class-based '
                             "inheritance (the 'class' syntax introduced in ES6 is purely syntactic sugar over "
                             'prototypes): 1. The [[Prototype]] Link: Every JavaScript object possesses an internal '
                             'hidden property known in ECMAScript specifications as [[Prototype]]. In modern code, '
                             "this prototype is inspected via 'Object.getPrototypeOf(obj)' or set via "
                             "'Object.setPrototypeOf()' / 'Object.create(proto)'. 2. Property Lookup Resolution: When "
                             "accessing a property on an object (e.g., 'user.toString()'): - The engine first inspects "
                             "the object's own direct properties ('own properties'). If found, it returns the value "
                             'immediately. - If the property does not exist on the object, the engine steps up the '
                             "prototype chain to inspect 'obj.[[Prototype]]'. - This search ascends recursively up the "
                             'linked chain. For instance: array -> Array.prototype -> Object.prototype -> null. - If '
                             'the property is found anywhere on the chain, lookup terminates and returns the value. - '
                             "If the lookup ascends all the way to 'Object.prototype.[[Prototype]]', which is strictly "
                             "'null', the chain terminates and the engine returns 'undefined'. 3. Function 'prototype' "
                             "vs Instance '[[Prototype]]': A common confusion exists between 'Constructor.prototype' "
                             "and an instance's '__proto__': - A function's 'prototype' property is an object "
                             'automatically created on functions that serves as the blueprint assigned to the '
                             "[[Prototype]] of instances created via 'new Constructor()'. - Thus: 'const arr = new "
                             "Array(); Object.getPrototypeOf(arr) === Array.prototype'. 4. Property Shadowing: "
                             "Assigning 'obj.prop = value' defines the property directly on 'obj' itself, effectively "
                             'shadowing any property with the same name located higher on the prototype chain without '
                             'mutating the shared prototype.',
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 96,
                                 'answer_text': 'JavaScript does not use classical inheritance; it uses prototypal '
                                                'inheritance, where objects inherit directly from other objects '
                                                'through a chain of references. Every object in JavaScript has an '
                                                'internal link called [[Prototype]], which you can access in modern '
                                                'JavaScript using Object.getPrototypeOf(obj) or the legacy __proto__ '
                                                'accessor. When you try to access a property or method on an '
                                                'object—like myDog.bark()—the JavaScript engine follows a strict '
                                                'lookup sequence: 1. It checks if the property exists directly on '
                                                "myDog as an 'own property'. If so, it returns it. 2. If it's not "
                                                "found, it steps up the prototype chain to myDog's prototype, which is "
                                                "Dog.prototype. 3. If it's still not found, it steps up to "
                                                "Dog.prototype's prototype, which is Object.prototype. 4. If it's not "
                                                "on Object.prototype, it checks Object.prototype's [[Prototype]], "
                                                'which is null. That is the end of the chain, and the engine returns '
                                                'undefined. An important distinction to keep straight is between a '
                                                "function's 'prototype' property and an object's [[Prototype]]. "
                                                'Function constructors like function Dog() {} have a .prototype '
                                                "property. When you do 'const myDog = new Dog()', JavaScript sets "
                                                "myDog's internal [[Prototype]] to point to Dog.prototype. Finally, if "
                                                'you assign a property directly to an instance, say myDog.bark = '
                                                "function(){}, it creates an own property that 'shadows' the method on "
                                                'the prototype without modifying the prototype itself.',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'In JavaScript, every object has an internal prototype link called '
                                                '[[Prototype]], accessible through Object.getPrototypeOf or __proto__. '
                                                'When you look up a property on an object, JavaScript first looks on '
                                                "the object itself. If it doesn't find it, it traverses up the "
                                                "prototype chain to the object's prototype. It keeps searching up the "
                                                'chain until it finds the property or reaches Object.prototype. If '
                                                "it's not found on Object.prototype, it reaches null and returns "
                                                'undefined. When you use constructor functions or classes, methods are '
                                                'stored on the Constructor.prototype object so that all instances '
                                                'share the same methods in memory.',
                                 'missing_concepts': ['Shadowing and performance: Defining a property directly on an '
                                                      "instance 'shadows' matching properties on its prototype; deep "
                                                      'prototype chains can slow down property lookup for missing '
                                                      'properties']},
                                {'quality_level': 'average',
                                 'human_score': 60,
                                 'answer_text': 'Prototypal inheritance is how JavaScript objects share methods. Every '
                                                'object has a __proto__ property that points to its parent prototype. '
                                                'When you call a method like array.map(), JavaScript looks for map on '
                                                "the array, and when it doesn't find it, it checks Array.prototype. "
                                                'The prototype chain continues all the way up to Object.prototype and '
                                                'ends at null. ES6 classes are just syntactic sugar over this '
                                                'prototype system.',
                                 'missing_concepts': ['Constructor.prototype vs instance.__proto__: Function '
                                                      "constructors have a 'prototype' property that becomes the "
                                                      "[[Prototype]] assigned to all instances instantiated with 'new "
                                                      "Constructor()'",
                                                      'Shadowing and performance: Defining a property directly on an '
                                                      "instance 'shadows' matching properties on its prototype; deep "
                                                      'prototype chains can slow down property lookup for missing '
                                                      'properties']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': 'Prototypes are draft versions of JavaScript code before you publish '
                                                'to production. The prototype chain is when you chain multiple .then() '
                                                'promises together. In JavaScript, classes are identical to Java '
                                                'classes and do not use object pointers.',
                                 'missing_concepts': ['Prototypal inheritance model: Unlike classical class-based '
                                                      'languages, JavaScript objects inherit directly from other '
                                                      'objects via an internal link [[Prototype]] (accessible via '
                                                      'Object.getPrototypeOf() or legacy __proto__)',
                                                      'Property lookup mechanism: When accessing obj.prop, the engine '
                                                      'checks obj; if not found, it ascends obj.[[Prototype]], '
                                                      'continuing recursively until found or reaching null (the end of '
                                                      'the prototype chain: Object.prototype.[[Prototype]] === null)',
                                                      'Constructor.prototype vs instance.__proto__: Function '
                                                      "constructors have a 'prototype' property that becomes the "
                                                      "[[Prototype]] assigned to all instances instantiated with 'new "
                                                      "Constructor()'",
                                                      'Shadowing and performance: Defining a property directly on an '
                                                      "instance 'shadows' matching properties on its prototype; deep "
                                                      'prototype chains can slow down property lookup for missing '
                                                      'properties']}]},
            {'topic_tag': 'Debouncing vs Throttling Handlers',
             'question': 'Compare debouncing and throttling event handlers when optimizing window resize or scroll '
                         'performance.',
             'keywords': ['Debouncing',
                          'Throttling',
                          'Event Frequency',
                          'Timer Management',
                          'Resize/Scroll Events',
                          'Performance Optimization'],
             'expected_concepts': ['Problem definition: Rapidly firing browser events (resize, scroll, keyup, '
                                   'mousemove) trigger hundreds of times per second, causing layout thrashing, DOM '
                                   'repaints, and UI jank if unconstrained',
                                   'Debouncing mechanism: Postpones function execution until a specified delay (e.g. '
                                   '300ms) has elapsed since the LAST event firing, continuously resetting the timer '
                                   'on new inputs',
                                   'Throttling mechanism: Guarantees function execution at regular periodic intervals '
                                   '(at most once every N milliseconds) regardless of how many times the event fires',
                                   'Ideal use cases: Debouncing is ideal for search autocomplete inputs, auto-save '
                                   'drafts, and window resize re-layouts; Throttling is ideal for infinite scroll '
                                   'position tracking and gaming mouse movement'],
             'model_answer': 'Both debouncing and throttling are rate-limiting techniques designed to optimize '
                             'performance by controlling how frequently an expensive event handler executes when '
                             'high-frequency DOM events (scroll, resize, mousemove, keyup) fire hundreds of times per '
                             'second: 1. Debouncing: - Mechanism: Debouncing groups a burst of sequential events into '
                             'a single execution. It sets a timer and postpones calling the handler until a specified '
                             'period of inactivity (e.g., 300ms) has elapsed since the LAST event call. If a new event '
                             'fires before the timer expires, the previous timer is cancelled and reset. - Real-world '
                             'use case: Search input autocomplete. You do not want to trigger an API request on every '
                             "keystroke as the user types 'laptop'; you want to wait until they pause typing for "
                             '300ms. Debouncing is also used for auto-saving form drafts and recalculating complex '
                             'layouts after a user finishes resizing their browser window. 2. Throttling: - Mechanism: '
                             'Throttling enforces a maximum frequency limit on function execution. It guarantees that '
                             'the handler will execute at most once every N milliseconds (e.g., once every 100ms) '
                             'throughout the continuous stream of events. - Real-world use case: Scroll event '
                             'tracking. In an infinite scroll list or sticky header progress bar, waiting for the user '
                             'to completely stop scrolling (debounce) would deliver a broken, delayed experience. '
                             'Throttling samples the scroll position at predictable 100ms intervals, providing smooth '
                             'UI updates while preventing CPU overload. 3. Implementation: Debouncing relies on '
                             "'clearTimeout(timer)' and 'setTimeout()'; throttling tracks timestamps ('Date.now() - "
                             "lastExecution >= delay') or uses leading/trailing flags.",
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 96,
                                 'answer_text': 'Both debouncing and throttling are rate-limiting techniques used to '
                                                'control how frequently an event handler fires, preventing browser '
                                                'performance bottlenecks from high-frequency events like window '
                                                'resize, scroll, or keystrokes that fire dozens of times per second. '
                                                '1. Debouncing delays function execution until a specified period of '
                                                'silence has elapsed since the LAST event. Every time the event fires, '
                                                'it cancels the previous timer and starts a new one. The function only '
                                                'executes once the user stops triggering events. The classic use case '
                                                "is a search bar with autocomplete: you don't want to make an HTTP "
                                                "request for every single letter while someone types 'headphones'; you "
                                                "wait until they pause typing for 300ms. It's also ideal for window "
                                                'resize if you only want to recalculate a chart after the user '
                                                'finishes dragging the browser window. 2. Throttling enforces a steady '
                                                'cadence: it guarantees that the function executes at most once every '
                                                'N milliseconds, no matter how many times the event fires. The '
                                                'function runs periodically at regular intervals while the event is '
                                                'ongoing. The classic use case is infinite scrolling or a scroll-based '
                                                "reading progress bar: you can't wait until the user stops scrolling "
                                                "(debounce) because the UI would feel laggy, but you also can't run on "
                                                'every scroll event (which fires 60+ times a second). Throttling the '
                                                'scroll handler to run once every 100ms gives smooth visual updates '
                                                'while saving CPU and battery life.',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'Debouncing and throttling both limit how often a function runs during '
                                                'rapid events like scrolling or typing. Debouncing waits until the '
                                                'user stops triggering the event for a set amount of time before '
                                                'running the function. For example, in a search box, it waits 300ms '
                                                'after the user stops typing to send the API request. Throttling runs '
                                                'the function at most once per fixed time interval, like once every '
                                                '100ms, even if the user is continuously scrolling. So for infinite '
                                                'scroll, throttling is better because you need continuous updates '
                                                'while scrolling, while debouncing is better for search inputs.',
                                 'missing_concepts': ['Problem definition: Rapidly firing browser events (resize, '
                                                      'scroll, keyup, mousemove) trigger hundreds of times per second, '
                                                      'causing layout thrashing, DOM repaints, and UI jank if '
                                                      'unconstrained']},
                                {'quality_level': 'average',
                                 'human_score': 60,
                                 'answer_text': 'Debounce and throttle make web pages faster by reducing function '
                                                'calls. Debounce means you wait until the user is done doing an '
                                                'action, like waiting until they finish typing before searching. '
                                                'Throttle means you only allow the function to run once every few '
                                                'milliseconds, like running a scroll handler at most once every '
                                                'second. Both use setTimeout under the hood to control the timing.',
                                 'missing_concepts': ['Problem definition: Rapidly firing browser events (resize, '
                                                      'scroll, keyup, mousemove) trigger hundreds of times per second, '
                                                      'causing layout thrashing, DOM repaints, and UI jank if '
                                                      'unconstrained',
                                                      'Ideal use cases: Debouncing is ideal for search autocomplete '
                                                      'inputs, auto-save drafts, and window resize re-layouts; '
                                                      'Throttling is ideal for infinite scroll position tracking and '
                                                      'gaming mouse movement']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': 'Debouncing is an algorithm for cleaning lint errors from JavaScript '
                                                'code. Throttling is when the web hosting provider slows down your '
                                                'internet connection because of high bandwidth usage. You should '
                                                'always use debouncing on database queries to make SQL run faster.',
                                 'missing_concepts': ['Problem definition: Rapidly firing browser events (resize, '
                                                      'scroll, keyup, mousemove) trigger hundreds of times per second, '
                                                      'causing layout thrashing, DOM repaints, and UI jank if '
                                                      'unconstrained',
                                                      'Debouncing mechanism: Postpones function execution until a '
                                                      'specified delay (e.g. 300ms) has elapsed since the LAST event '
                                                      'firing, continuously resetting the timer on new inputs',
                                                      'Throttling mechanism: Guarantees function execution at regular '
                                                      'periodic intervals (at most once every N milliseconds) '
                                                      'regardless of how many times the event fires',
                                                      'Ideal use cases: Debouncing is ideal for search autocomplete '
                                                      'inputs, auto-save drafts, and window resize re-layouts; '
                                                      'Throttling is ideal for infinite scroll position tracking and '
                                                      'gaming mouse movement']}]},
            {'topic_tag': 'WebSockets vs SSE vs Long Polling',
             'question': 'Compare WebSockets, Server-Sent Events (SSE), and HTTP Long Polling for real-time '
                         'bidirectional web communications.',
             'keywords': ['WebSockets',
                          'Server-Sent Events',
                          'Long Polling',
                          'Bi-directional Communication',
                          'HTTP Overhead',
                          'Real-Time Updates'],
             'expected_concepts': ['Directionality: WebSockets provide full-duplex bidirectional communication; SSE '
                                   'provides unidirectional server-to-client streaming; Long Polling emulates push via '
                                   'repeated client-initiated HTTP requests',
                                   'Protocol and transport: WebSockets upgrade from HTTP to a persistent TCP '
                                   'connection via ws:// or wss://; SSE operates over standard HTTP/1.1 or HTTP/2 '
                                   'using Content-Type: text/event-stream; Long Polling uses standard HTTP requests '
                                   'held open until data is ready',
                                   'Overhead and efficiency: WebSockets have tiny 2-10 byte frame headers with no HTTP '
                                   'overhead; Long Polling incurs full HTTP request/response headers and TCP handshake '
                                   'overhead on every message',
                                   'Ideal use cases: WebSockets for multiplayer gaming, chat apps, collaborative '
                                   'whiteboards; SSE for live stock tickers, sports scores, and LLM text streaming; '
                                   'Long Polling as legacy fallback'],
             'model_answer': 'When designing real-time web architectures, three primary protocols provide contrasting '
                             'directionality, transport protocols, and resource overhead: 1. HTTP Long Polling: The '
                             'client sends a standard HTTP request to the server, which holds the connection open '
                             'until new data arrives or a timeout occurs. Once data is returned, the client '
                             'immediately initiates a new HTTP request. While simple to implement and compatible with '
                             'all proxies and legacy firewalls, Long Polling suffers from severe overhead: every '
                             'message incurs full HTTP request/response headers, TLS renegotiation, and high server '
                             'connection churn. It is considered a legacy fallback. 2. Server-Sent Events (SSE): A '
                             'standardized W3C API (EventSource) that provides unidirectional streaming from server to '
                             "client over standard HTTP/1.1 or HTTP/2 using 'Content-Type: text/event-stream'. The "
                             'client opens a single persistent connection, and the server pushes text events formatted '
                             "as 'data: ...\\n\\n'. SSE features built-in automatic reconnection, event IDs, and "
                             'native browser support. Because it runs over standard HTTP, it seamlessly leverages '
                             'HTTP/2 multiplexing, corporate firewalls, and CDN proxies. Ideal for live stock tickers, '
                             'sports scores, system notifications, and LLM token streaming (e.g., ChatGPT responses). '
                             '3. WebSockets: Established via an HTTP Upgrade handshake (HTTP 101 Switching Protocols), '
                             'WebSockets create a persistent, full-duplex, bidirectional TCP socket between client and '
                             'server (ws:// or wss://). Both client and server can send text or binary frames at any '
                             'time with minimal 2-10 byte frame overhead. Ideal for applications requiring low-latency '
                             'bidirectional interaction: multiplayer gaming, financial trading platforms, '
                             'collaborative editing (Figma), and chat applications.',
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 96,
                                 'answer_text': 'Choosing between WebSockets, Server-Sent Events, and Long Polling '
                                                'comes down to directionality, overhead, and protocol transport: 1. '
                                                'HTTP Long Polling is the oldest approach. The client sends an HTTP '
                                                'request, and the server hangs onto the request until new data is '
                                                'ready. Once data is returned, the connection closes, and the client '
                                                'immediately opens a new request. The problem is massive overhead: '
                                                'every single message has to carry full HTTP headers, cookie payloads, '
                                                "and handle TCP reconnection overhead. It's strictly a legacy fallback "
                                                'today. 2. Server-Sent Events (SSE) provide unidirectional, '
                                                'server-to-client streaming over standard HTTP. The browser uses the '
                                                'native EventSource API to connect with Content-Type: '
                                                'text/event-stream. The server pushes text data down whenever it '
                                                'wants, and the browser handles automatic reconnection and message IDs '
                                                "out of the box. Because it's plain HTTP, it works seamlessly with "
                                                "HTTP/2 multiplexing, load balancers, and corporate firewalls. It's "
                                                'the perfect choice for one-way streams like live dashboard metrics, '
                                                'stock tickers, or streaming LLM text output like ChatGPT. 3. '
                                                'WebSockets provide full-duplex, bidirectional communication. The '
                                                'connection starts as an HTTP request and upgrades to the WebSocket '
                                                "protocol via an HTTP 101 Switching Protocols header. After that, it's "
                                                'a raw persistent TCP socket where both client and server can send '
                                                'binary or text frames anytime with only 2 to 10 bytes of framing '
                                                'overhead. You should choose WebSockets when you need low-latency '
                                                'two-way communication, such as multiplayer games, collaborative '
                                                'whiteboard tools like Figma, or real-time chat rooms.',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'WebSockets allow full-duplex bidirectional communication between '
                                                'client and server over a persistent TCP connection with very low '
                                                'overhead. Both sides can send data at any time, making it ideal for '
                                                'chat apps and multiplayer games. Server-Sent Events (SSE) is '
                                                'unidirectional from server to client over standard HTTP. It has '
                                                'built-in auto-reconnect and is great for live updates like stock '
                                                'prices or LLM token streaming. Long polling is when the client makes '
                                                'an HTTP request that the server holds open until data is ready, and '
                                                'then the client makes another request. Long polling has the highest '
                                                'overhead because it repeats the full HTTP header exchange on every '
                                                'single message.',
                                 'missing_concepts': ['Protocol and transport: WebSockets upgrade from HTTP to a '
                                                      'persistent TCP connection via ws:// or wss://; SSE operates '
                                                      'over standard HTTP/1.1 or HTTP/2 using Content-Type: '
                                                      'text/event-stream; Long Polling uses standard HTTP requests '
                                                      'held open until data is ready']},
                                {'quality_level': 'average',
                                 'human_score': 60,
                                 'answer_text': 'WebSockets is for two-way communication where both browser and server '
                                                'can talk to each other in real time, like in a chat app. SSE is '
                                                'one-way communication from server to browser using standard HTTP, '
                                                'which is good for notifications and news feeds. Long polling is an '
                                                'older technique where the client repeatedly asks the server for data '
                                                "with timeouts. WebSockets is the fastest because it doesn't send HTTP "
                                                'headers with every message.',
                                 'missing_concepts': ['Protocol and transport: WebSockets upgrade from HTTP to a '
                                                      'persistent TCP connection via ws:// or wss://; SSE operates '
                                                      'over standard HTTP/1.1 or HTTP/2 using Content-Type: '
                                                      'text/event-stream; Long Polling uses standard HTTP requests '
                                                      'held open until data is ready',
                                                      'Ideal use cases: WebSockets for multiplayer gaming, chat apps, '
                                                      'collaborative whiteboards; SSE for live stock tickers, sports '
                                                      'scores, and LLM text streaming; Long Polling as legacy '
                                                      'fallback']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': "WebSockets are wireless Bluetooth connections between the client's "
                                                'laptop and the server. Server-Sent Events requires installing an '
                                                "Apache server on the client's browser. Long polling is when the "
                                                'browser downloads the entire database in a single ZIP file.',
                                 'missing_concepts': ['Directionality: WebSockets provide full-duplex bidirectional '
                                                      'communication; SSE provides unidirectional server-to-client '
                                                      'streaming; Long Polling emulates push via repeated '
                                                      'client-initiated HTTP requests',
                                                      'Protocol and transport: WebSockets upgrade from HTTP to a '
                                                      'persistent TCP connection via ws:// or wss://; SSE operates '
                                                      'over standard HTTP/1.1 or HTTP/2 using Content-Type: '
                                                      'text/event-stream; Long Polling uses standard HTTP requests '
                                                      'held open until data is ready',
                                                      'Overhead and efficiency: WebSockets have tiny 2-10 byte frame '
                                                      'headers with no HTTP overhead; Long Polling incurs full HTTP '
                                                      'request/response headers and TCP handshake overhead on every '
                                                      'message',
                                                      'Ideal use cases: WebSockets for multiplayer gaming, chat apps, '
                                                      'collaborative whiteboards; SSE for live stock tickers, sports '
                                                      'scores, and LLM text streaming; Long Polling as legacy '
                                                      'fallback']}]},
            {'topic_tag': 'JWT Authentication & Storage Security',
             'question': 'How does JSON Web Token (JWT) authentication work, and why should sensitive tokens be stored '
                         'in HttpOnly cookies instead of LocalStorage?',
             'keywords': ['JWT',
                          'Header Payload Signature',
                          'Bearer Token',
                          'HttpOnly Cookies',
                          'XSS Risk',
                          'Token Expiration'],
             'expected_concepts': ['JWT structure: Three Base64URL-encoded parts separated by dots '
                                   '(header.payload.signature); payload holds claims (sub, exp, roles); signature '
                                   'ensures tamper detection via HMAC-SHA256 or RSA',
                                   'Stateless authentication flow: Client sends credentials -> server signs JWT and '
                                   'returns it -> client sends token in Authorization: Bearer <token> or cookie -> '
                                   'server validates signature without database lookup',
                                   'Vulnerability of LocalStorage: Any Cross-Site Scripting (XSS) vulnerability allows '
                                   'malicious scripts (window.localStorage.getItem) to steal tokens immediately and '
                                   'exfiltrate them',
                                   'HttpOnly cookies mitigation: Setting HttpOnly flag blocks JavaScript access, '
                                   'neutralizing XSS token theft; CSRF risk is mitigated by SameSite=Lax/Strict flags '
                                   'and anti-CSRF tokens'],
             'model_answer': 'JSON Web Token (JWT) is an open standard (RFC 7519) for securely transmitting claims '
                             'between parties as a compact, self-contained JSON object: 1. Token Structure: A JWT '
                             'comprises three Base64URL-encoded sections separated by dots: - Header: Specifies the '
                             "token type ('JWT') and cryptographic signing algorithm ('HS256' or 'RS256'). - Payload: "
                             "Contains the claims—statements about the user and metadata, such as subject ('sub'), "
                             "expiration timestamp ('exp'), issuer ('iss'), and authorization roles. - Signature: "
                             'Generated by hashing the encoded header, encoded payload, and a secret key: '
                             "HMACSHA256(base64(header) + '.' + base64(payload), secret). Crucially, JWT payloads are "
                             'encoded, not encrypted; anyone can decode and inspect the payload, but any tampering '
                             'invalidates the signature. 2. Stateless Authentication: Because the server can verify '
                             'the signature mathematically using its private secret/public key, it does not need to '
                             'query a session database or Redis cache on every request, making JWTs highly scalable '
                             'for distributed microservices. 3. Storage Security (LocalStorage vs HttpOnly Cookie): - '
                             'LocalStorage vulnerability: LocalStorage is accessible to any JavaScript running on the '
                             'page origin. If the web application has a single Cross-Site Scripting (XSS) '
                             'vulnerability (via a third-party script, unsanitized input, or npm package compromise), '
                             "the attacker can execute 'localStorage.getItem('token')' and exfiltrate the JWT to their "
                             'server, gaining permanent access until token expiry. - HttpOnly Cookies: Storing the JWT '
                             "inside a cookie marked with the 'HttpOnly' flag prevents client-side JavaScript from "
                             "reading or accessing 'document.cookie'. Even if an attacker executes arbitrary XSS "
                             "scripts, they cannot extract the token. When combined with the 'Secure' flag (HTTPS "
                             "only) and 'SameSite=Lax' or 'SameSite=Strict' flags (preventing Cross-Site Request "
                             'Forgery), HttpOnly cookies provide the industry-recommended security posture for '
                             'sensitive authentication tokens.',
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 96,
                                 'answer_text': 'A JWT consists of three Base64URL-encoded parts separated by dots: '
                                                'the Header (which specifies the algorithm, like HS256), the Payload '
                                                '(which holds the claims, like user ID and expiration timestamp), and '
                                                'the Signature (which is computed by hashing the header and payload '
                                                'with a server secret). A vital thing people forget is that JWTs are '
                                                'signed, not encrypted—anyone can decode the payload, but only the '
                                                'server with the secret key can generate a valid signature. In a '
                                                'stateless authentication flow, the client logs in, the server '
                                                'generates the signed JWT, and on future requests, the client presents '
                                                'the token. The server verifies the signature without needing to query '
                                                'a session database, making it very scalable. The debate over where to '
                                                'store the token is critical for security. Many tutorials put JWTs in '
                                                'LocalStorage, but LocalStorage is completely accessible to '
                                                'client-side JavaScript. That means if your application has even one '
                                                'Cross-Site Scripting (XSS) flaw—like an unsanitized input or a '
                                                'compromised third-party npm package—an attacker can run '
                                                "'localStorage.getItem('token')' and steal the user's session "
                                                'immediately. Storing the JWT in an HttpOnly cookie solves this '
                                                'because the browser strictly forbids JavaScript from reading HttpOnly '
                                                'cookies. Even if an attacker injects malicious JS via XSS, they '
                                                'cannot steal the token. To protect against CSRF attacks with cookies, '
                                                'you configure the cookie with SameSite=Lax or Strict, along with the '
                                                'Secure flag so it is only transmitted over HTTPS.',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'A JWT has three parts: header, payload, and signature separated by '
                                                'dots. The payload contains claims like the user ID and expiration '
                                                "date, and the signature verifies that the token wasn't tampered with. "
                                                'The server validates the token without needing to check a session '
                                                'database. You should never store JWTs in LocalStorage because any XSS '
                                                'vulnerability allows an attacker to run JavaScript and steal the '
                                                'token from localStorage. By storing the token in an HttpOnly cookie, '
                                                'JavaScript cannot read it, preventing token theft. You also use '
                                                'SameSite and Secure flags to protect against CSRF.',
                                 'missing_concepts': ['Stateless authentication flow: Client sends credentials -> '
                                                      'server signs JWT and returns it -> client sends token in '
                                                      'Authorization: Bearer <token> or cookie -> server validates '
                                                      'signature without database lookup']},
                                {'quality_level': 'average',
                                 'human_score': 60,
                                 'answer_text': 'JWT stands for JSON Web Token and is used for user authentication. It '
                                                'has three parts: header, payload, and signature. When you log in, the '
                                                'server sends back a token that you send in the Authorization header. '
                                                "You shouldn't put JWTs in LocalStorage because hackers can steal them "
                                                'using XSS attacks with malicious script tags. HttpOnly cookies are '
                                                "safer because JavaScript cannot access them, so hackers can't read "
                                                'the token.',
                                 'missing_concepts': ['JWT structure: Three Base64URL-encoded parts separated by dots '
                                                      '(header.payload.signature); payload holds claims (sub, exp, '
                                                      'roles); signature ensures tamper detection via HMAC-SHA256 or '
                                                      'RSA',
                                                      'HttpOnly cookies mitigation: Setting HttpOnly flag blocks '
                                                      'JavaScript access, neutralizing XSS token theft; CSRF risk is '
                                                      'mitigated by SameSite=Lax/Strict flags and anti-CSRF tokens']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': 'JWT is an encrypted password stored inside the HTML DOM. LocalStorage '
                                                'is more secure than cookies because LocalStorage is encrypted by '
                                                'Windows. HttpOnly cookies were deprecated because they block Google '
                                                'Analytics.',
                                 'missing_concepts': ['JWT structure: Three Base64URL-encoded parts separated by dots '
                                                      '(header.payload.signature); payload holds claims (sub, exp, '
                                                      'roles); signature ensures tamper detection via HMAC-SHA256 or '
                                                      'RSA',
                                                      'Stateless authentication flow: Client sends credentials -> '
                                                      'server signs JWT and returns it -> client sends token in '
                                                      'Authorization: Bearer <token> or cookie -> server validates '
                                                      'signature without database lookup',
                                                      'Vulnerability of LocalStorage: Any Cross-Site Scripting (XSS) '
                                                      'vulnerability allows malicious scripts '
                                                      '(window.localStorage.getItem) to steal tokens immediately and '
                                                      'exfiltrate them',
                                                      'HttpOnly cookies mitigation: Setting HttpOnly flag blocks '
                                                      'JavaScript access, neutralizing XSS token theft; CSRF risk is '
                                                      'mitigated by SameSite=Lax/Strict flags and anti-CSRF tokens']}]},
            {'topic_tag': 'HTTPS & TLS/SSL Handshake Sequence',
             'question': 'Explain the step-by-step sequence of a TLS/SSL handshake when establishing a secure HTTPS '
                         'connection.',
             'keywords': ['HTTPS',
                          'TLS/SSL Handshake',
                          'Asymmetric Encryption',
                          'Symmetric Encryption',
                          'Certificate Authority',
                          'Public Key'],
             'expected_concepts': ['Client Hello: Client sends supported TLS version, cipher suites, and a random byte '
                                   'string (Client Random)',
                                   'Server Hello & Certificate: Server responds with chosen cipher suite, Server '
                                   'Random, and SSL/TLS certificate containing its public key signed by a trusted '
                                   'Certificate Authority (CA)',
                                   'Certificate verification & Key exchange: Client verifies CA signature chain; '
                                   'client and server perform asymmetric key exchange (e.g. ECDHE) to agree on a '
                                   'shared Pre-Master Secret',
                                   'Symmetric session key derivation: Both sides independently derive identical '
                                   'symmetric session keys from Client Random, Server Random, and Pre-Master Secret; '
                                   'subsequent communication uses fast symmetric encryption (AES-GCM)'],
             'model_answer': 'HTTPS establishes secure, encrypted communication over TCP port 443 by executing a TLS '
                             '(Transport Layer Security) handshake. Modern TLS 1.3/1.2 combines asymmetric '
                             'cryptography (for identity authentication and key exchange) with symmetric cryptography '
                             '(for fast data encryption): 1. Client Hello: The client initiates the handshake by '
                             'transmitting: supported TLS versions (e.g., TLS 1.3), a list of supported cryptographic '
                             'cipher suites (e.g., TLS_AES_256_GCM_SHA384), and a client-generated random byte string '
                             "('Client Random'). In TLS 1.3, it also includes key-share parameters. 2. Server Hello: "
                             'The server responds with the chosen TLS version, selected cipher suite, and its own '
                             "random byte string ('Server Random'). 3. Server Certificate & Verification: The server "
                             'presents its X.509 digital certificate, containing its domain name, public key, and the '
                             "digital signature of a trusted Certificate Authority (CA). The client's operating system "
                             'or browser checks the certificate against its pre-installed Root CA store, verifying the '
                             'signature chain, domain name, and revocation status (OCSP/CRL). 4. Key Exchange (ECDHE): '
                             'In modern handshakes using Elliptic Curve Diffie-Hellman Ephemeral (ECDHE), the client '
                             'and server exchange public key parameters to calculate a shared secret known as the '
                             "'Pre-Master Secret'. Because ECDHE is ephemeral, it guarantees Perfect Forward Secrecy "
                             "(PFS)—past captured traffic cannot be decrypted even if the server's private key is "
                             'compromised in the future. 5. Session Key Derivation: Both client and server '
                             'independently feed the Client Random, Server Random, and Pre-Master Secret into a '
                             'pseudorandom function (PRF) to generate identical symmetric session keys. 6. Finished '
                             "Messages: Both sides exchange encrypted 'Finished' verification messages confirming the "
                             'handshake was not tampered with. All subsequent HTTP application data is encrypted '
                             'symmetrically using AES-GCM or ChaCha20-Poly1305.',
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 96,
                                 'answer_text': 'The TLS handshake sets up an encrypted HTTPS connection by combining '
                                                'asymmetric encryption for identity verification and key exchange, and '
                                                'symmetric encryption for fast data transfer. Here is the step-by-step '
                                                'sequence: 1. Client Hello: The browser sends supported TLS versions, '
                                                'a list of supported cipher suites, and a random number called the '
                                                'Client Random. 2. Server Hello: The server replies with its chosen '
                                                'cipher suite, the Server Random, and its digital SSL certificate. 3. '
                                                "Certificate Verification: The browser verifies the certificate's "
                                                'authenticity against trusted root Certificate Authorities (CAs) in '
                                                'its trust store to ensure the server is legitimate and not a '
                                                'man-in-the-middle attacker. The certificate also contains the '
                                                "server's public key. 4. Key Exchange: Using an algorithm like ECDHE "
                                                '(Elliptic Curve Diffie-Hellman), the client and server exchange '
                                                'ephemeral parameters to compute a shared Pre-Master Secret. Using '
                                                'ephemeral keys provides Perfect Forward Secrecy, so future key leaks '
                                                'cannot decrypt past recordings. 5. Deriving Session Keys: Both sides '
                                                'independently take the Client Random, Server Random, and Pre-Master '
                                                'Secret and run them through a key derivation function to generate '
                                                'identical symmetric encryption keys. 6. Finished: Both parties send '
                                                'encrypted verification messages to prove the handshake was authentic. '
                                                'From this point forward, all HTTP requests and responses are '
                                                'encrypted using fast symmetric encryption like AES-GCM.',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'The TLS handshake establishes a secure connection in a few steps. '
                                                'First, the client sends a Client Hello with supported cipher suites '
                                                'and a client random. The server responds with Server Hello, its '
                                                'selected cipher suite, a server random, and its SSL certificate '
                                                'containing its public key. The client verifies the certificate using '
                                                'trusted Certificate Authorities. Then, they use Diffie-Hellman key '
                                                'exchange to agree on a pre-master secret. Both sides use the client '
                                                'random, server random, and pre-master secret to generate symmetric '
                                                'session keys. After sending finished messages, all future traffic is '
                                                'encrypted using the symmetric key.',
                                 'missing_concepts': ['Symmetric session key derivation: Both sides independently '
                                                      'derive identical symmetric session keys from Client Random, '
                                                      'Server Random, and Pre-Master Secret; subsequent communication '
                                                      'uses fast symmetric encryption (AES-GCM)']},
                                {'quality_level': 'average',
                                 'human_score': 60,
                                 'answer_text': 'The TLS handshake is what turns HTTP into HTTPS. The browser connects '
                                                'to the server and the server sends its SSL certificate. The browser '
                                                'checks that the certificate is signed by a valid authority like '
                                                "DigiCert or Let's Encrypt. Then the client uses the server's public "
                                                'key to encrypt a secret key and sends it to the server. The server '
                                                'decrypts it with its private key. After that, both sides use that '
                                                'shared key to encrypt all web traffic with symmetric encryption.',
                                 'missing_concepts': ['Client Hello: Client sends supported TLS version, cipher '
                                                      'suites, and a random byte string (Client Random)',
                                                      'Certificate verification & Key exchange: Client verifies CA '
                                                      'signature chain; client and server perform asymmetric key '
                                                      'exchange (e.g. ECDHE) to agree on a shared Pre-Master Secret']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': 'The SSL handshake happens when the user types their credit card '
                                                "number. The browser hashes the user's password using MD5 and sends it "
                                                'in plain text to the server. If the hash matches, HTTPS unlocks port '
                                                '80 on the firewall.',
                                 'missing_concepts': ['Client Hello: Client sends supported TLS version, cipher '
                                                      'suites, and a random byte string (Client Random)',
                                                      'Server Hello & Certificate: Server responds with chosen cipher '
                                                      'suite, Server Random, and SSL/TLS certificate containing its '
                                                      'public key signed by a trusted Certificate Authority (CA)',
                                                      'Certificate verification & Key exchange: Client verifies CA '
                                                      'signature chain; client and server perform asymmetric key '
                                                      'exchange (e.g. ECDHE) to agree on a shared Pre-Master Secret',
                                                      'Symmetric session key derivation: Both sides independently '
                                                      'derive identical symmetric session keys from Client Random, '
                                                      'Server Random, and Pre-Master Secret; subsequent communication '
                                                      'uses fast symmetric encryption (AES-GCM)']}]},
            {'topic_tag': 'CSS Positioning Modes',
             'question': 'Distinguish between static, relative, absolute, fixed, and sticky CSS positioning modes.',
             'keywords': ['Position Static', 'Relative', 'Absolute', 'Fixed', 'Sticky', 'Containing Block'],
             'expected_concepts': ['position: static: Default normal document flow; top/right/bottom/left and z-index '
                                   'properties have no effect',
                                   'position: relative: Element remains in normal flow, but top/left offsets move its '
                                   'visual rendering relative to its own default position without altering surrounding '
                                   'element placement; establishes containing block for absolute children',
                                   'position: absolute: Removed completely from normal document flow; positioned '
                                   'relative to nearest positioned ancestor (position != static); collapses space in '
                                   'normal flow',
                                   'position: fixed vs sticky: Fixed is anchored relative to the viewport window and '
                                   'stays fixed during scrolling; Sticky is a hybrid that acts relative within its '
                                   'parent until a specified scroll offset is reached, then sticks until its parent '
                                   'container ends'],
             'model_answer': "In CSS, the 'position' property dictates how an element is placed within the document "
                             'layout and how it relates to its containing block: 1. position: static (Default): The '
                             'element resides in the normal document flow according to standard block/inline '
                             "formatting rules. Offset properties ('top', 'bottom', 'left', 'right') and 'z-index' are "
                             'completely ignored. 2. position: relative: The element remains in the normal document '
                             'flow, reserving its original dimensional footprint so surrounding elements are '
                             "unaffected. However, offset properties ('top: 10px', 'left: 20px') visually shift the "
                             "rendered element relative to its own original position. Crucially, declaring 'position: "
                             "relative' establishes a containing block anchor for any descendant elements with "
                             'absolute positioning. 3. position: absolute: The element is removed entirely from normal '
                             'document flow; no space is reserved for it, causing surrounding elements to collapse '
                             'into its space. It is positioned relative to its nearest positioned ancestor (the '
                             "nearest ancestor with position other than 'static'). If no such ancestor exists, it "
                             'positions relative to the Initial Containing Block (the viewport/root HTML). 4. '
                             'position: fixed: The element is removed from normal flow and positioned relative to the '
                             'browser viewport window (or an ancestor with transform/perspective/filter). It remains '
                             'pinned to that exact screen coordinate during scrolling. Ideal for persistent navigation '
                             'bars, modal overlays, or back-to-top floating buttons. 5. position: sticky: A contextual '
                             "hybrid between relative and fixed positioning. The element behaves as 'relative' within "
                             'its parent container until the scroll container reaches a specified threshold (e.g., '
                             "'top: 0'), at which point it 'sticks' in place like fixed positioning. Crucially, a "
                             'sticky element is bound by its parent container: once the parent container scrolls out '
                             'of view, the sticky element scrolls off with it.',
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 96,
                                 'answer_text': 'CSS positioning modes control how elements are placed relative to the '
                                                'document flow and their containing blocks: 1. static: The default. '
                                                'The element stays in normal document flow. Properties like top, left, '
                                                'and z-index have zero effect. 2. relative: The element stays in the '
                                                'normal flow, meaning its original space is preserved and neighboring '
                                                "elements don't move. However, you can nudge it visually using top, "
                                                'right, bottom, or left relative to where it normally would sit. It '
                                                'also serves as the containing block anchor for any child elements '
                                                'with absolute positioning. 3. absolute: The element is pulled '
                                                'completely out of the normal document flow—no space is reserved for '
                                                'it. It positions itself relative to its nearest ancestor that has a '
                                                'position other than static (like a relative parent). If none exists, '
                                                'it anchors to the document root. 4. fixed: Also pulled out of the '
                                                'flow, but it positions relative to the browser viewport. It stays '
                                                'pinned in the exact same spot on the screen even when the user '
                                                'scrolls, which is how you build fixed navigation bars or modal '
                                                'backdrops. 5. sticky: A hybrid between relative and fixed. It behaves '
                                                'like relative positioning until you scroll past a threshold—like top: '
                                                '0—at which point it sticks to that position like fixed. But unlike '
                                                'fixed, it is constrained within its parent container: when the parent '
                                                'container scrolls out of view, the sticky element scrolls away with '
                                                'it.',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'Static is the default where elements follow normal document flow and '
                                                "top/left don't work. Relative keeps the element in flow, but lets you "
                                                'offset it from where it normally sits, and it acts as an anchor for '
                                                'absolute children. Absolute pulls the element out of the flow and '
                                                'positions it relative to the nearest positioned parent container. '
                                                'Fixed positions the element relative to the screen viewport so it '
                                                'never moves when scrolling. Sticky acts relative until you scroll '
                                                'past it, and then it sticks to the top of the screen until its parent '
                                                'finishes scrolling.',
                                 'missing_concepts': ['position: relative: Element remains in normal flow, but '
                                                      'top/left offsets move its visual rendering relative to its own '
                                                      'default position without altering surrounding element '
                                                      'placement; establishes containing block for absolute children']},
                                {'quality_level': 'average',
                                 'human_score': 60,
                                 'answer_text': 'Static is standard positioning. Relative lets you move an element '
                                                'using top and left relative to itself. Absolute takes the element out '
                                                'of the page flow and positions it inside a relative parent div. Fixed '
                                                'keeps an element pinned to the screen like a floating navbar. Sticky '
                                                'is used for table headers or menus that stay at the top when you '
                                                'scroll down the page.',
                                 'missing_concepts': ['position: relative: Element remains in normal flow, but '
                                                      'top/left offsets move its visual rendering relative to its own '
                                                      'default position without altering surrounding element '
                                                      'placement; establishes containing block for absolute children',
                                                      'position: fixed vs sticky: Fixed is anchored relative to the '
                                                      'viewport window and stays fixed during scrolling; Sticky is a '
                                                      'hybrid that acts relative within its parent until a specified '
                                                      'scroll offset is reached, then sticks until its parent '
                                                      'container ends']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': 'Position static means the website cannot be viewed on mobile devices. '
                                                'Absolute positioning is required for all elements in modern CSS. '
                                                'Sticky positioning is used to make images load faster from the CDN.',
                                 'missing_concepts': ['position: static: Default normal document flow; '
                                                      'top/right/bottom/left and z-index properties have no effect',
                                                      'position: relative: Element remains in normal flow, but '
                                                      'top/left offsets move its visual rendering relative to its own '
                                                      'default position without altering surrounding element '
                                                      'placement; establishes containing block for absolute children',
                                                      'position: absolute: Removed completely from normal document '
                                                      'flow; positioned relative to nearest positioned ancestor '
                                                      '(position != static); collapses space in normal flow',
                                                      'position: fixed vs sticky: Fixed is anchored relative to the '
                                                      'viewport window and stays fixed during scrolling; Sticky is a '
                                                      'hybrid that acts relative within its parent until a specified '
                                                      'scroll offset is reached, then sticks until its parent '
                                                      'container ends']}]},
            {'topic_tag': 'Node.js Event Loop Phases',
             'question': "Explain the event loop phases in Node.js (Timers, I/O Poll, Check phase) and libuv's role.",
             'keywords': ['Node.js Event Loop',
                          'Timers Phase',
                          'Poll Phase',
                          'Check Phase',
                          'libuv',
                          'Microtask Queue'],
             'expected_concepts': ['libuv role: Multi-platform C library providing the event loop, non-blocking '
                                   'asynchronous I/O abstractions, and the background thread pool (default 4 threads '
                                   'for file I/O, DNS, crypto)',
                                   'Six discrete event loop phases executed in order: 1. Timers '
                                   '(setTimeout/setInterval); 2. Pending callbacks (system I/O errors); 3. Idle, '
                                   'prepare; 4. Poll (fetches new I/O events, blocks when idle); 5. Check (executes '
                                   'setImmediate callbacks); 6. Close callbacks',
                                   'setImmediate vs setTimeout(..., 0): setImmediate executes in the Check phase '
                                   'immediately after the Poll phase; setTimeout(..., 0) executes in the Timers phase',
                                   'Microtask draining priority: process.nextTick queue runs with highest priority, '
                                   'followed by Promise jobs; microtasks are drained completely immediately after each '
                                   'callback and between phase transitions'],
             'model_answer': 'In Node.js, asynchronous I/O concurrency is powered by libuv, a multi-platform C library '
                             'that manages the event loop, asynchronous socket abstraction, and a background thread '
                             'pool (default 4 threads used for expensive blocking operations like fs filesystem calls, '
                             "dns lookups, and crypto). Unlike the browser's simplified task/microtask loop, the "
                             'Node.js event loop executes through six distinct phases in a strict order: 1. Timers '
                             "Phase: Executes callbacks scheduled by 'setTimeout()' and 'setInterval()' whose "
                             'threshold duration has expired. 2. Pending Callbacks Phase: Executes I/O callbacks '
                             'deferred from previous iterations, such as certain system-level TCP error notifications '
                             '(e.g., ECONNREFUSED). 3. Idle, Prepare Phase: Internal libuv operations. 4. Poll Phase: '
                             'The heart of the event loop. The loop calculates how long it should block for incoming '
                             'I/O events, polls the OS for new network sockets and file events, and executes their '
                             'callbacks. If the poll queue is empty, the loop either moves to the Check phase (if '
                             'setImmediate scripts exist) or waits for new incoming I/O. 5. Check Phase: Dedicated '
                             "exclusively to executing callbacks scheduled via 'setImmediate()'. Crucially, if "
                             'scheduled inside an I/O callback (e.g., inside fs.readFile), setImmediate will always '
                             'execute before any timer because the Check phase immediately succeeds the Poll phase. 6. '
                             'Close Callbacks Phase: Executes close events, such as \'socket.on("close", ...)\'. '
                             "Microtask Processing: Crucially, 'process.nextTick' and Promise microtasks do not belong "
                             'to a specific phase. In modern Node.js, the microtask queue is drained immediately after '
                             "the completion of each individual callback, with 'process.nextTick' taking precedence "
                             'over Promise resolutions.',
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 97,
                                 'answer_text': 'Node.js relies on libuv—a C library that provides the event loop and '
                                                "manages a background thread pool for operations that can't be handled "
                                                'asynchronously by the OS kernel, like filesystem I/O and crypto. The '
                                                'Node.js event loop executes through six distinct phases in a '
                                                'continuous loop: 1. Timers: Executes callbacks from setTimeout() and '
                                                'setInterval() whose threshold timers have expired. 2. Pending '
                                                'callbacks: Executes deferred I/O callbacks, like system-level TCP '
                                                'errors. 3. Idle, prepare: Used internally by libuv. 4. Poll phase: '
                                                'The core I/O phase. It retrieves new incoming I/O events from the OS '
                                                'and executes their callbacks. If no timers are ready, it will block '
                                                'and wait for incoming connections. 5. Check phase: Specifically '
                                                'executes setImmediate() callbacks. If you schedule setImmediate '
                                                'inside an I/O callback, it is guaranteed to execute before any '
                                                'setTimeout because Check immediately follows Poll. 6. Close '
                                                "callbacks: Handles cleanup events like socket.on('close'). A crucial "
                                                'detail is microtasks: process.nextTick and Promise microtasks do not '
                                                'belong to a single phase. Node.js drains microtasks immediately after '
                                                'any individual callback completes, with process.nextTick having '
                                                'higher priority than Promise resolutions.',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'Node.js uses libuv to handle asynchronous non-blocking I/O and thread '
                                                'pooling. The event loop has several phases that run in order: the '
                                                'Timers phase runs setTimeout and setInterval callbacks; the Poll '
                                                'phase handles incoming I/O events like network connections and '
                                                'database responses; and the Check phase runs setImmediate callbacks. '
                                                'If you are inside an I/O callback, setImmediate runs before '
                                                'setTimeout(..., 0) because Check comes right after Poll. Microtasks '
                                                'like process.nextTick and Promises run immediately between phase '
                                                'transitions.',
                                 'missing_concepts': ['Microtask draining priority: process.nextTick queue runs with '
                                                      'highest priority, followed by Promise jobs; microtasks are '
                                                      'drained completely immediately after each callback and between '
                                                      'phase transitions']},
                                {'quality_level': 'average',
                                 'human_score': 61,
                                 'answer_text': 'Node.js uses libuv to run non-blocking code. The event loop has '
                                                'phases including Timers for setTimeout, Poll for I/O operations, and '
                                                'Check for setImmediate. setImmediate is designed to run right after '
                                                'the I/O poll phase. Node also has process.nextTick which runs before '
                                                'promises. This is how Node handles thousands of connections on a '
                                                'single thread.',
                                 'missing_concepts': ['libuv role: Multi-platform C library providing the event loop, '
                                                      'non-blocking asynchronous I/O abstractions, and the background '
                                                      'thread pool (default 4 threads for file I/O, DNS, crypto)',
                                                      'Six discrete event loop phases executed in order: 1. Timers '
                                                      '(setTimeout/setInterval); 2. Pending callbacks (system I/O '
                                                      'errors); 3. Idle, prepare; 4. Poll (fetches new I/O events, '
                                                      'blocks when idle); 5. Check (executes setImmediate callbacks); '
                                                      '6. Close callbacks']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': 'libuv is a Node.js package that you install from npm to compile '
                                                'TypeScript. The event loop has two phases: frontend and backend. '
                                                'setImmediate is deprecated and was replaced by setTimeout. Timers '
                                                'phase runs on the GPU.',
                                 'missing_concepts': ['libuv role: Multi-platform C library providing the event loop, '
                                                      'non-blocking asynchronous I/O abstractions, and the background '
                                                      'thread pool (default 4 threads for file I/O, DNS, crypto)',
                                                      'Six discrete event loop phases executed in order: 1. Timers '
                                                      '(setTimeout/setInterval); 2. Pending callbacks (system I/O '
                                                      'errors); 3. Idle, prepare; 4. Poll (fetches new I/O events, '
                                                      'blocks when idle); 5. Check (executes setImmediate callbacks); '
                                                      '6. Close callbacks',
                                                      'setImmediate vs setTimeout(..., 0): setImmediate executes in '
                                                      'the Check phase immediately after the Poll phase; '
                                                      'setTimeout(..., 0) executes in the Timers phase',
                                                      'Microtask draining priority: process.nextTick queue runs with '
                                                      'highest priority, followed by Promise jobs; microtasks are '
                                                      'drained completely immediately after each callback and between '
                                                      'phase transitions']}]},
            {'topic_tag': 'Next.js Rendering Modes (SSR/SSG/ISR)',
             'question': 'How do SSR, SSG, and Incremental Static Regeneration (ISR) operate in Next.js applications?',
             'keywords': ['Next.js',
                          'Server-Side Rendering',
                          'Static Site Generation',
                          'Incremental Static Regeneration',
                          'GetStaticProps',
                          'GetServerSideProps'],
             'expected_concepts': ['SSG (Static Site Generation): HTML is pre-rendered at build time (getStaticProps / '
                                   'static generation); pages are cached on CDN edges, offering near-instant TTFB and '
                                   'zero runtime server compute',
                                   'SSR (Server-Side Rendering): HTML is generated dynamically on every incoming '
                                   'request (getServerSideProps); allows access to request headers/cookies and '
                                   'guarantees fresh data at the expense of server CPU and higher TTFB',
                                   "ISR (Incremental Static Regeneration): Extends SSG by adding a 'revalidate' "
                                   'threshold; serves cached static HTML immediately while rebuilding the page in the '
                                   'background upon incoming requests after the interval expires',
                                   'Use case alignment: SSG for marketing landing pages and documentation; SSR for '
                                   'personalized user dashboards and authenticated feeds; ISR for e-commerce product '
                                   'catalogs and large blog systems'],
             'model_answer': 'Next.js provides hybrid rendering capabilities, allowing developers to configure the '
                             'rendering strategy on a per-page basis: 1. Static Site Generation (SSG): - Mechanism: In '
                             "SSG (using 'getStaticProps' or static page export), HTML and JSON data payloads are "
                             'pre-rendered once at build time. The static HTML files are deployed and cached across '
                             'CDN edge nodes worldwide. - Pros/Cons: Delivers lightning-fast Time to First Byte (TTFB) '
                             'and optimal SEO with zero server runtime compute costs. However, content is static; '
                             'updating data requires triggering a complete project rebuild and deployment. - Ideal '
                             'for: Marketing pages, documentation, blog posts, and static marketing landing pages. 2. '
                             "Server-Side Rendering (SSR): - Mechanism: In SSR (using 'getServerSideProps' or dynamic "
                             'Server Components), the Node.js server executes data fetching and renders the React '
                             'component tree into HTML dynamically for every incoming HTTP request. - Pros/Cons: '
                             'Guarantees 100% real-time data freshness and provides access to request-specific data '
                             '(cookies, query params, auth headers). However, TTFB is slower because the user waits '
                             'for the server to fetch data and render, and high traffic increases backend compute load '
                             'and hosting costs. - Ideal for: Highly dynamic, authenticated pages like banking '
                             'dashboards, user account settings, and live inventory portals. 3. Incremental Static '
                             "Regeneration (ISR): - Mechanism: ISR bridges SSG and SSR by adding a 'revalidate' "
                             "parameter (e.g., 'revalidate: 60') to static generation. The initial build generates "
                             'static HTML cached at the CDN. When a request arrives after the 60-second window: '
                             'Next.js serves the cached static page instantly (stale-while-revalidate), while spawning '
                             'a background regeneration task. Once the new page builds successfully, the CDN cache is '
                             'updated; subsequent visitors see the new page without any rebuild. - Ideal for: Massive '
                             'e-commerce catalogs (millions of product pages) and content platforms where data changes '
                             'periodically but cannot justify full rebuilds.',
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 96,
                                 'answer_text': 'Next.js offers a hybrid rendering architecture where you can choose '
                                                "between SSG, SSR, and ISR based on the specific page's needs: 1. "
                                                'Static Site Generation (SSG): The HTML is generated at build time '
                                                'using getStaticProps. The compiled HTML is deployed to global CDN '
                                                'edge caches. Visitors get near-instant Time to First Byte (TTFB), '
                                                'great SEO, and zero server compute costs. The drawback is that data '
                                                'is static—if you update your CMS, you have to trigger a full site '
                                                "rebuild. It's best for marketing sites, documentation, and blog "
                                                'posts. 2. Server-Side Rendering (SSR): The page is generated on the '
                                                'server for every single incoming request using getServerSideProps. It '
                                                'gives you real-time data and access to incoming request headers and '
                                                'cookies, making it great for authenticated dashboards or personalized '
                                                'feeds. The downside is higher server cost and slower TTFB because the '
                                                'user waits for the server to query the database and render the HTML. '
                                                '3. Incremental Static Regeneration (ISR): This is the best of both '
                                                'worlds. You generate static pages like SSG, but you define a '
                                                "'revalidate' time, say 60 seconds. Visitors get the cached static "
                                                'page instantly from the CDN. When a request comes in after 60 '
                                                'seconds, Next.js serves the stale cached page immediately '
                                                '(stale-while-revalidate) while triggering a background rebuild of '
                                                'that specific page. Once built, the cache updates seamlessly. This '
                                                'allows huge e-commerce sites with 100,000 product pages to have fast '
                                                'static performance without 10-hour rebuilds.',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'SSG generates HTML at build time using getStaticProps. The pages are '
                                                'cached on a CDN, giving very fast page load times and great SEO, but '
                                                'you have to rebuild the site to update content. SSR generates the '
                                                'HTML on the server on every request using getServerSideProps, which '
                                                'is necessary for private user dashboards with auth cookies, though '
                                                'TTFB is slower. ISR lets you update static pages in the background '
                                                'without rebuilding the whole site by specifying a revalidate period '
                                                'in getStaticProps, serving cached static pages while refreshing them '
                                                'periodically.',
                                 'missing_concepts': ['Use case alignment: SSG for marketing landing pages and '
                                                      'documentation; SSR for personalized user dashboards and '
                                                      'authenticated feeds; ISR for e-commerce product catalogs and '
                                                      'large blog systems']},
                                {'quality_level': 'average',
                                 'human_score': 61,
                                 'answer_text': 'SSG is static site generation where Next.js creates the HTML files '
                                                'when you run npm run build. SSR is server-side rendering where the '
                                                'server creates the HTML every time someone visits the page using '
                                                'getServerSideProps. ISR is incremental static regeneration, which is '
                                                'like SSG but it automatically reloads the page in the background '
                                                'after a certain number of seconds using the revalidate property. SSG '
                                                'is fastest and SSR is best for dynamic data.',
                                 'missing_concepts': ['SSG (Static Site Generation): HTML is pre-rendered at build '
                                                      'time (getStaticProps / static generation); pages are cached on '
                                                      'CDN edges, offering near-instant TTFB and zero runtime server '
                                                      'compute',
                                                      'ISR (Incremental Static Regeneration): Extends SSG by adding a '
                                                      "'revalidate' threshold; serves cached static HTML immediately "
                                                      'while rebuilding the page in the background upon incoming '
                                                      'requests after the interval expires']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': 'SSG stands for Server Side Generation and SSR stands for Static Site '
                                                'Rendering. In Next.js, ISR is an AI bot that rewrites your React code '
                                                'while users are browsing. You should always use SSR for marketing '
                                                'landing pages because it has zero server cost.',
                                 'missing_concepts': ['SSG (Static Site Generation): HTML is pre-rendered at build '
                                                      'time (getStaticProps / static generation); pages are cached on '
                                                      'CDN edges, offering near-instant TTFB and zero runtime server '
                                                      'compute',
                                                      'SSR (Server-Side Rendering): HTML is generated dynamically on '
                                                      'every incoming request (getServerSideProps); allows access to '
                                                      'request headers/cookies and guarantees fresh data at the '
                                                      'expense of server CPU and higher TTFB',
                                                      'ISR (Incremental Static Regeneration): Extends SSG by adding a '
                                                      "'revalidate' threshold; serves cached static HTML immediately "
                                                      'while rebuilding the page in the background upon incoming '
                                                      'requests after the interval expires',
                                                      'Use case alignment: SSG for marketing landing pages and '
                                                      'documentation; SSR for personalized user dashboards and '
                                                      'authenticated feeds; ISR for e-commerce product catalogs and '
                                                      'large blog systems']}]},
            {'topic_tag': 'XSS Attack Prevention Techniques',
             'question': 'How do Cross-Site Scripting (XSS) attacks exploit un-sanitized input, and how can Content '
                         'Security Policy (CSP) mitigate them?',
             'keywords': ['XSS',
                          'Cross-Site Scripting',
                          'Input Sanitization',
                          'Content Security Policy',
                          'HTML Escaping',
                          'Reflected vs Stored XSS'],
             'expected_concepts': ['XSS classification: Stored XSS (malicious script permanently stored in DB and '
                                   'served to users); Reflected XSS (script reflected off server in query param/URL); '
                                   'DOM-based XSS (client JS insecurely inserts payload into DOM via innerHTML)',
                                   'Root vulnerability: Occurs when user input is rendered into HTML/DOM without '
                                   'proper context-aware sanitization or escaping, allowing attacker JavaScript to '
                                   'execute in victim browsers to steal cookies/tokens or perform actions',
                                   'Defense-in-depth prevention: Context-aware output encoding (converting <, >, &, ", '
                                   "' to HTML entities), using safe DOM APIs (textContent instead of innerHTML), and "
                                   'sanitizing rich HTML using DOMPurify',
                                   'Content Security Policy (CSP): HTTP response header (Content-Security-Policy) that '
                                   'restricts sources from which scripts can load, disables unsafe inline scripts '
                                   "('unsafe-inline'), and blocks eval() ('unsafe-eval') using nonces or hashes"],
             'model_answer': 'Cross-Site Scripting (XSS) is a code-injection vulnerability where malicious JavaScript '
                             "is injected into trusted websites and executed in the victim's browser: 1. Types of XSS: "
                             '- Stored XSS (Persistent): The attacker submits a malicious script (e.g., in a comment '
                             'or profile bio) that the server saves to a database. Every user who loads that page '
                             'subsequently executes the payload. - Reflected XSS: The payload is embedded in a request '
                             "(e.g., in a URL search parameter like '?q=<script>...') and the server reflects it "
                             'unescaped directly into the HTML response. - DOM-based XSS: The vulnerability exists '
                             'purely in client-side JavaScript. Untrusted data (e.g., location.hash) is written into '
                             "an unsafe sink like 'element.innerHTML' or 'eval()'. 2. Consequences: Once executed, "
                             "attacker JavaScript operates with full privileges of the victim's origin—stealing "
                             'session cookies (if not HttpOnly), reading LocalStorage tokens, logging keystrokes, or '
                             "issuing unauthorized API requests on the user's behalf. 3. Primary Mitigations: - "
                             'Context-Aware Output Escaping: Convert special characters to HTML entities (&lt;, &gt;, '
                             '&quot;, &#x27;, &amp;). Modern frameworks like React escape JSX expressions '
                             "({userInput}) automatically. - Safe DOM Methods: Use 'element.textContent' instead of "
                             "'innerHTML'. When rich HTML formatting is required, sanitize markup using robust "
                             'libraries like DOMPurify. - HttpOnly Cookies: Mitigates session hijacking by blocking '
                             'JavaScript access to authentication cookies. 4. Content Security Policy (CSP): CSP is a '
                             "defense-in-depth HTTP response header ('Content-Security-Policy: default-src 'self'; "
                             "script-src 'self' https://trusted.cdn.com; object-src 'none'') that restricts where "
                             'executable scripts, styles, and media can load from. By default, a strict CSP disallows '
                             "inline scripts (<script>...</script> and onclick handlers) and blocks 'eval()'. "
                             "Legitimate inline scripts must use cryptographic nonces (script-src 'nonce-random123') "
                             'or SHA-256 hashes.',
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 96,
                                 'answer_text': 'Cross-Site Scripting (XSS) occurs when an application includes '
                                                'untrusted user input into the DOM or HTML without proper escaping, '
                                                "allowing an attacker to execute arbitrary JavaScript in the victim's "
                                                'browser. There are three main types: 1. Stored XSS: The malicious '
                                                'payload is saved permanently in a database (like in a user comment) '
                                                'and runs for everyone viewing that page. 2. Reflected XSS: The '
                                                'payload is in a URL parameter or form submission and reflected '
                                                'immediately in the server response. 3. DOM-based XSS: The '
                                                'vulnerability is entirely in client-side code, where JavaScript reads '
                                                'from an untrusted source like location.search and passes it to an '
                                                "unsafe sink like innerHTML. Once the attacker's script executes, it "
                                                'can steal localStorage tokens, log user keystrokes, or make API calls '
                                                'as the user. Prevention requires defense-in-depth: First, '
                                                'context-aware output encoding and using safe APIs—like using '
                                                'textContent instead of innerHTML, or using DOMPurify if you must '
                                                'render HTML. Modern frameworks like React escape JSX strings by '
                                                'default. Second, storing auth tokens in HttpOnly cookies so '
                                                'JavaScript cannot steal them. Third, implementing a strong Content '
                                                'Security Policy (CSP). CSP is an HTTP response header that defines an '
                                                'allowlist of trusted sources for scripts and assets (like script-src '
                                                "'self' https://apis.google.com). A strict CSP disables inline script "
                                                'execution and eval() unless accompanied by a cryptographic nonce, so '
                                                'even if an attacker manages to inject a <script> tag into the HTML, '
                                                'the browser will refuse to execute it.',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'XSS occurs when an attacker injects malicious JavaScript into a '
                                                "website that gets executed in a user's browser. There is Stored XSS "
                                                'where the script is saved in the database, Reflected XSS where the '
                                                'script comes from a link or query parameter, and DOM-based XSS where '
                                                'client JavaScript uses innerHTML unsafely. The attacker can steal '
                                                'tokens or session data. To prevent it, you must sanitize and escape '
                                                'user input, use textContent instead of innerHTML, and use libraries '
                                                'like DOMPurify. Content Security Policy (CSP) is an HTTP header that '
                                                'specifies where scripts are allowed to load from and blocks inline '
                                                'scripts, stopping injected scripts from running.',
                                 'missing_concepts': ['Defense-in-depth prevention: Context-aware output encoding '
                                                      '(converting <, >, &, ", \' to HTML entities), using safe DOM '
                                                      'APIs (textContent instead of innerHTML), and sanitizing rich '
                                                      'HTML using DOMPurify']},
                                {'quality_level': 'average',
                                 'human_score': 60,
                                 'answer_text': 'XSS is Cross-Site Scripting where a hacker enters HTML script tags '
                                                "into an input field, like <script>alert('hacked')</script>. If the "
                                                'website displays the text without escaping, the script runs in other '
                                                "users' browsers and steals their cookies. You prevent it by escaping "
                                                'special characters like < and > and using React which does this '
                                                'automatically. Content Security Policy is a server header that blocks '
                                                "scripts that don't come from trusted domains.",
                                 'missing_concepts': ['XSS classification: Stored XSS (malicious script permanently '
                                                      'stored in DB and served to users); Reflected XSS (script '
                                                      'reflected off server in query param/URL); DOM-based XSS (client '
                                                      'JS insecurely inserts payload into DOM via innerHTML)',
                                                      'Content Security Policy (CSP): HTTP response header '
                                                      '(Content-Security-Policy) that restricts sources from which '
                                                      'scripts can load, disables unsafe inline scripts '
                                                      "('unsafe-inline'), and blocks eval() ('unsafe-eval') using "
                                                      'nonces or hashes']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': 'XSS is when someone hacks your CSS styling to change the website '
                                                'colors to black. Content Security Policy is an antivirus software '
                                                "installed on the web server. You can stop XSS by adding the 'secure' "
                                                'attribute to your HTML form tag.',
                                 'missing_concepts': ['XSS classification: Stored XSS (malicious script permanently '
                                                      'stored in DB and served to users); Reflected XSS (script '
                                                      'reflected off server in query param/URL); DOM-based XSS (client '
                                                      'JS insecurely inserts payload into DOM via innerHTML)',
                                                      'Root vulnerability: Occurs when user input is rendered into '
                                                      'HTML/DOM without proper context-aware sanitization or escaping, '
                                                      'allowing attacker JavaScript to execute in victim browsers to '
                                                      'steal cookies/tokens or perform actions',
                                                      'Defense-in-depth prevention: Context-aware output encoding '
                                                      '(converting <, >, &, ", \' to HTML entities), using safe DOM '
                                                      'APIs (textContent instead of innerHTML), and sanitizing rich '
                                                      'HTML using DOMPurify',
                                                      'Content Security Policy (CSP): HTTP response header '
                                                      '(Content-Security-Policy) that restricts sources from which '
                                                      'scripts can load, disables unsafe inline scripts '
                                                      "('unsafe-inline'), and blocks eval() ('unsafe-eval') using "
                                                      'nonces or hashes']}]},
            {'topic_tag': 'CSRF Tokens & SameSite Cookie Protection',
             'question': 'How do Anti-CSRF tokens and SameSite cookie attributes defend against Cross-Site Request '
                         'Forgery attacks?',
             'keywords': ['CSRF',
                          'Cross-Site Request Forgery',
                          'Anti-CSRF Tokens',
                          'SameSite Cookie Attribute',
                          'State-Changing Requests',
                          'Origin Header'],
             'expected_concepts': ['CSRF attack vector: Exploits ambient browser authentication (session cookies '
                                   'automatically attached to cross-site requests) to execute unauthorized '
                                   'state-changing actions (e.g. POST /transfer)',
                                   'Anti-CSRF tokens (Synchronizer Token Pattern): Server generates a unique, '
                                   'cryptographically random, unpredictable token tied to the user session; token must '
                                   'be submitted in request headers or body, which cross-origin attackers cannot read '
                                   'due to SOP',
                                   'SameSite cookie attribute: SameSite=Strict prevents cookies from being sent on any '
                                   'cross-site request; SameSite=Lax (browser default) permits cookies only on '
                                   'top-level safe GET navigations, blocking cross-site POST form submissions',
                                   'Defense-in-depth: Combining SameSite cookies with CSRF tokens, verifying '
                                   'Origin/Referer headers, and avoiding state changes via GET requests provides '
                                   'comprehensive protection'],
             'model_answer': 'Cross-Site Request Forgery (CSRF) is an attack where a malicious website tricks a '
                             "victim's authenticated browser into executing unauthorized, state-changing HTTP requests "
                             'against a vulnerable target application: 1. Attack Mechanism: Because browsers '
                             'automatically attach stored session cookies to any outgoing HTTP request matching the '
                             'target domain—even if initiated by an external site (e.g., via a hidden form submission '
                             '\'<form action="https://bank.com/transfer" method="POST">\' or an image tag)—the target '
                             'server blindly authenticates the request as coming from the victim. 2. Anti-CSRF Tokens '
                             '(Synchronizer Token Pattern): To defeat CSRF, the server generates a unique, '
                             "cryptographically random token associated with the user's current session. When "
                             'rendering a form or responding to an initial API handshake, this token is injected into '
                             "a hidden form input or custom HTTP header (e.g., 'X-CSRF-Token'). When a state-changing "
                             'request (POST, PUT, DELETE) is submitted, the server compares the submitted token '
                             'against the session token. Because the Same-Origin Policy (SOP) prohibits malicious '
                             'third-party origins from reading response bodies or DOM contents on target domains, the '
                             'attacker cannot obtain or guess this token, causing forged requests to be rejected. 3. '
                             'SameSite Cookie Attribute: SameSite provides browser-level defense by restricting when '
                             'cookies are sent on cross-origin requests: - SameSite=Strict: The cookie is never sent '
                             'on any cross-site request, even when following a normal link from an external search '
                             'engine. - SameSite=Lax (Modern Default): The cookie is withheld on cross-site '
                             'sub-requests (such as cross-origin images, iframes, or POST form submissions), but '
                             'permitted on safe, top-level navigations (e.g., clicking a standard <a> link that '
                             "performs a GET). - SameSite=None: Requires the 'Secure' flag (HTTPS) and permits "
                             'cross-site transmission. Modern security best practice employs SameSite=Lax/Strict as '
                             'the primary defense while retaining anti-CSRF tokens for defense-in-depth.',
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 96,
                                 'answer_text': 'CSRF attacks exploit the fact that browsers automatically attach '
                                                'ambient credentials—specifically session cookies—to any outgoing HTTP '
                                                'request targeting a domain, even if that request was triggered by a '
                                                'completely different malicious website. For instance, if you are '
                                                'logged into your bank and visit evil.com, that site could have a '
                                                'hidden form that auto-submits a POST request to bank.com/transfer. '
                                                'Because your browser sends your bank session cookie, the bank '
                                                'processes the transfer thinking it was you. We defend against this '
                                                'using two primary techniques: 1. Anti-CSRF Tokens (Synchronizer Token '
                                                'Pattern): The server generates a secret, cryptographically random '
                                                "token tied to the user's session and embeds it in a hidden form input "
                                                "or returns it to be sent in an 'X-CSRF-Token' header on AJAX calls. "
                                                'When a state-changing POST or PUT request arrives, the server '
                                                'verifies that this token matches. Because the Same-Origin Policy '
                                                'prevents external sites from reading the DOM or API responses of your '
                                                'application, evil.com cannot read your CSRF token and cannot forge a '
                                                'valid request. 2. SameSite Cookie Attribute: This is a browser-level '
                                                'defense that tells the browser whether cookies should be included on '
                                                'cross-site requests. SameSite=Strict blocks the cookie on all '
                                                'cross-site requests, meaning if you click a link from an external '
                                                "email to your bank, you won't even be logged in initially. "
                                                'SameSite=Lax—which is the modern browser default—strikes a great '
                                                'balance: it blocks cookies on cross-site POST form submissions, '
                                                'images, and iframes, but still attaches cookies on top-level safe GET '
                                                'navigations when a user clicks a regular link. Combining SameSite=Lax '
                                                'cookies with anti-CSRF tokens gives you airtight defense-in-depth.',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'CSRF happens when a malicious website triggers a request to another '
                                                'website where the user is already authenticated, because the browser '
                                                "automatically sends the user's session cookies with the request. "
                                                'Anti-CSRF tokens prevent this by requiring a secret, random token to '
                                                'be included in the form or headers. Since the attacker cannot read '
                                                'this token due to the Same-Origin Policy, they cannot forge the '
                                                'request. The SameSite cookie attribute also stops CSRF: SameSite=Lax '
                                                'prevents cookies from being sent on cross-site POST requests, and '
                                                'SameSite=Strict blocks cookies on all cross-origin requests.',
                                 'missing_concepts': ['Defense-in-depth: Combining SameSite cookies with CSRF tokens, '
                                                      'verifying Origin/Referer headers, and avoiding state changes '
                                                      'via GET requests provides comprehensive protection']},
                                {'quality_level': 'average',
                                 'human_score': 60,
                                 'answer_text': 'CSRF is Cross-Site Request Forgery where a hacker tricks your browser '
                                                'into making requests to another site while you are logged in. To stop '
                                                'it, servers use CSRF tokens which are random strings generated by the '
                                                'server that the frontend has to send back with every POST request. '
                                                'SameSite cookies also protect against CSRF because SameSite=Lax stops '
                                                'cookies from being sent from other websites. This prevents hackers '
                                                'from submitting forms on your behalf.',
                                 'missing_concepts': ['CSRF attack vector: Exploits ambient browser authentication '
                                                      '(session cookies automatically attached to cross-site requests) '
                                                      'to execute unauthorized state-changing actions (e.g. POST '
                                                      '/transfer)',
                                                      'Defense-in-depth: Combining SameSite cookies with CSRF tokens, '
                                                      'verifying Origin/Referer headers, and avoiding state changes '
                                                      'via GET requests provides comprehensive protection']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': 'CSRF is when a hacker steals your password using a keylogger. '
                                                'Anti-CSRF tokens encrypt the database using AES encryption. SameSite '
                                                'attribute means that the website can only be visited from the same '
                                                'city as the web server.',
                                 'missing_concepts': ['CSRF attack vector: Exploits ambient browser authentication '
                                                      '(session cookies automatically attached to cross-site requests) '
                                                      'to execute unauthorized state-changing actions (e.g. POST '
                                                      '/transfer)',
                                                      'Anti-CSRF tokens (Synchronizer Token Pattern): Server generates '
                                                      'a unique, cryptographically random, unpredictable token tied to '
                                                      'the user session; token must be submitted in request headers or '
                                                      'body, which cross-origin attackers cannot read due to SOP',
                                                      'SameSite cookie attribute: SameSite=Strict prevents cookies '
                                                      'from being sent on any cross-site request; SameSite=Lax '
                                                      '(browser default) permits cookies only on top-level safe GET '
                                                      'navigations, blocking cross-site POST form submissions',
                                                      'Defense-in-depth: Combining SameSite cookies with CSRF tokens, '
                                                      'verifying Origin/Referer headers, and avoiding state changes '
                                                      'via GET requests provides comprehensive protection']}]},
            {'topic_tag': 'Web Performance Code Splitting',
             'question': 'How do code splitting and lazy loading reduce initial JavaScript bundle sizes in modern web '
                         'applications?',
             'keywords': ['Code Splitting',
                          'Lazy Loading',
                          'Dynamic Import()',
                          'Bundle Analyzer',
                          'Tree Shaking',
                          'Asset Optimization'],
             'expected_concepts': ['Problem of monolithic bundles: Bundling all application code into a single massive '
                                   'JS file forces users to download, parse, and compile code for routes and features '
                                   'they may never visit, degrading TTI and FCP',
                                   "Dynamic imports syntax: Using dynamic 'import('./Module')' instructs bundlers "
                                   '(Webpack, Vite, Rollup) to split code into separate on-demand asynchronous chunks',
                                   'Route-level & component-level lazy loading: Combining React.lazy() and Suspense '
                                   'splits bundles along route boundaries, loading code only when the user navigates '
                                   'to that route',
                                   'Tree shaking synergy: ES module static import/export syntax allows bundlers to '
                                   'detect and eliminate dead code (unused exports), reducing bundle size before code '
                                   'splitting occurs'],
             'model_answer': 'In modern Single Page Applications (SPAs), failing to manage asset delivery results in a '
                             'monolithic JavaScript bundle (often several megabytes) that users must download, parse, '
                             'compile, and execute before seeing an interactive UI. Code splitting and lazy loading '
                             'address this performance bottleneck: 1. Mechanism of Code Splitting: Code splitting '
                             'divides a monolithic bundle into smaller, discrete chunks that can be loaded on demand '
                             'or in parallel. Under the hood, bundlers like Webpack, Vite, and Rollup leverage '
                             'ECMAScript dynamic imports: \'import("./Dashboard.js")\'. When the bundler encounters a '
                             'dynamic import, it automatically treats that module as an entry point for a separate '
                             'bundle chunk. 2. Lazy Loading with React.lazy and Suspense: In React, route-based code '
                             "splitting is the most impactful pattern: 'const Dashboard = React.lazy(() => "
                             'import("./Dashboard"))\'. Wrapping these components in \'<Suspense fallback={<Spinner '
                             "/>}><Dashboard /></Suspense>' ensures that the JavaScript chunk for the '/dashboard' "
                             'route is only fetched across the network when the user actually navigates to that route. '
                             '3. Component and Library Splitting: Beyond routes, heavy third-party libraries (e.g., '
                             'charting libraries like Chart.js, PDF generators, rich text editors) can be lazy loaded '
                             'inside event handlers (e.g., dynamically importing the PDF library only when the user '
                             "clicks 'Export to PDF'). 4. Tree Shaking: Working in tandem with code splitting, tree "
                             "shaking analyzes static ES module 'import' and 'export' statements during build time to "
                             'eliminate unused dead code, ensuring split chunks contain only reachable logic.',
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 96,
                                 'answer_text': 'Code splitting and lazy loading optimize performance by preventing '
                                                'monolithic JavaScript bundles. In a standard SPA build, all your '
                                                'components, routes, and third-party libraries are bundled into one '
                                                'huge JavaScript file. That means a user landing on your homepage is '
                                                'forced to download, parse, and compile JavaScript for your admin '
                                                'dashboard, checkout flows, and analytics charts before the page even '
                                                'becomes interactive. Code splitting uses ES dynamic imports—syntax '
                                                "like 'import('./MyComponent')'—to signal to bundlers like Vite or "
                                                'Webpack that this module should be compiled into a separate, '
                                                'independent chunk file. In React, we implement this at the route '
                                                "level using React.lazy and Suspense: 'const Admin = React.lazy(() => "
                                                "import('./Admin'))'. The browser only requests the admin chunk over "
                                                'the network when the user actually navigates to the /admin route, '
                                                'showing a Suspense fallback spinner while it loads. You can also do '
                                                'feature-based lazy loading—like dynamically importing a heavy 500KB '
                                                "PDF export library only when the user clicks the 'Download PDF' "
                                                'button. Combined with tree shaking, which strips out unused exports '
                                                'at build time, code splitting slashes initial bundle sizes, '
                                                'dramatically improving First Contentful Paint (FCP) and Time to '
                                                'Interactive (TTI).',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'Code splitting breaks a large JavaScript bundle into smaller chunks '
                                                'that can be loaded on demand. In large web apps, having one big '
                                                'bundle slows down the initial page load because the browser has to '
                                                'parse and compile everything at once. By using dynamic imports with '
                                                'import() and React.lazy, you can load code only when a user visits a '
                                                'specific route or opens a modal. This is called lazy loading. Using '
                                                'React Suspense provides a loading fallback while the chunk is '
                                                'downloading. This significantly reduces initial bundle size and '
                                                'speeds up Time to Interactive.',
                                 'missing_concepts': ['Tree shaking synergy: ES module static import/export syntax '
                                                      'allows bundlers to detect and eliminate dead code (unused '
                                                      'exports), reducing bundle size before code splitting occurs']},
                                {'quality_level': 'average',
                                 'human_score': 60,
                                 'answer_text': 'Code splitting is splitting your JavaScript into smaller files so the '
                                                'initial download is faster. In React you use React.lazy and Suspense '
                                                'to lazy load pages. When a user clicks on a page, React downloads '
                                                'that chunk from the server instead of downloading all pages at the '
                                                'beginning. Tools like Webpack Bundle Analyzer help you see which npm '
                                                'packages are making your bundle too big.',
                                 'missing_concepts': ["Dynamic imports syntax: Using dynamic 'import('./Module')' "
                                                      'instructs bundlers (Webpack, Vite, Rollup) to split code into '
                                                      'separate on-demand asynchronous chunks',
                                                      'Tree shaking synergy: ES module static import/export syntax '
                                                      'allows bundlers to detect and eliminate dead code (unused '
                                                      'exports), reducing bundle size before code splitting occurs']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': 'Code splitting is when you split your CSS file into HTML and '
                                                'JavaScript. Lazy loading means the CPU waits 5 seconds before '
                                                'executing JavaScript to save battery. It makes websites load slower '
                                                'but uses less memory.',
                                 'missing_concepts': ['Problem of monolithic bundles: Bundling all application code '
                                                      'into a single massive JS file forces users to download, parse, '
                                                      'and compile code for routes and features they may never visit, '
                                                      'degrading TTI and FCP',
                                                      "Dynamic imports syntax: Using dynamic 'import('./Module')' "
                                                      'instructs bundlers (Webpack, Vite, Rollup) to split code into '
                                                      'separate on-demand asynchronous chunks',
                                                      'Route-level & component-level lazy loading: Combining '
                                                      'React.lazy() and Suspense splits bundles along route '
                                                      'boundaries, loading code only when the user navigates to that '
                                                      'route',
                                                      'Tree shaking synergy: ES module static import/export syntax '
                                                      'allows bundlers to detect and eliminate dead code (unused '
                                                      'exports), reducing bundle size before code splitting occurs']}]},
            {'topic_tag': 'Browser Caching & ETag Headers',
             'question': 'How do Cache-Control directives and ETag validation headers work together to optimize '
                         'browser caching?',
             'keywords': ['Cache-Control',
                          'ETag Header',
                          'Max-Age',
                          'Must-Revalidate',
                          'Conditional GET',
                          '304 Not Modified'],
             'expected_concepts': ["Cache-Control directives: 'max-age=N' defines freshness lifetime in seconds; "
                                   "'no-cache' mandates server validation before using cached copy; 'no-store' forbids "
                                   "any caching; 'immutable' indicates asset content will never change",
                                   'ETag (Entity Tag) mechanism: An HTTP response header providing a cryptographic '
                                   'hash or version identifier representing the exact state of the resource '
                                   'representation',
                                   'Conditional GET requests: When cached asset freshness expires, the browser issues '
                                   "a conditional request with 'If-None-Match: <etag>'; if content is unchanged, "
                                   "server responds with '304 Not Modified' with no body, saving bandwidth",
                                   'Modern deployment caching strategy: Content-hashed static assets (bundle.a8f9.js) '
                                   'use long-lived caching (max-age=31536000, immutable); HTML files use no-cache with '
                                   'ETags to ensure instant deployment updates'],
             'model_answer': 'Browser caching optimizes network performance by coordinating freshness checks '
                             '(Cache-Control) and validation mechanisms (ETag): 1. Cache-Control (Freshness Lifetime): '
                             "The 'Cache-Control' HTTP header governs where and for how long a response can be cached: "
                             "- 'max-age=3600': The cached representation is considered 'fresh' for 3600 seconds. "
                             'While fresh, the browser serves the asset directly from disk/memory cache without making '
                             "any network request. - 'no-cache': Misunderstood directive; it does NOT mean 'do not "
                             "cache'. It instructs the browser to cache the response, but forces it to validate "
                             "freshness with the origin server (using ETags) before using it. - 'no-store': Completely "
                             'forbids any browser or intermediate proxy from storing the response in cache (essential '
                             "for sensitive financial or auth data). - 'immutable': Informs the browser that the "
                             'response body will never change during its max-age lifetime. 2. ETag (Validation & '
                             'Conditional GET): An ETag (Entity Tag) is a unique fingerprint—typically a cryptographic '
                             'hash of the resource content (e.g., ETag: "686897696a7c76"). - When a cached asset\'s '
                             'max-age expires, the browser does not re-download the entire file. Instead, it sends a '
                             '\'Conditional GET\' request containing the \'If-None-Match: "686897696a7c76"\' header. - '
                             "If the resource has not changed on the server, the server responds with '304 Not "
                             "Modified' and an empty response body. The browser immediately refreshes its local cache "
                             'timer. 3. Optimal Web Deployment Strategy: Modern SPAs split caching into two rules: - '
                             "HTML documents (index.html): 'Cache-Control: no-cache' with ETags. This guarantees users "
                             'always check with the server and receive new deployments instantly. - Hashed Static '
                             "Assets (main.d41d8c.js, style.7b5f.css): 'Cache-Control: public, max-age=31536000, "
                             "immutable'. Because file names change upon every build, they can be cached forever "
                             'safely.',
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 96,
                                 'answer_text': 'Cache-Control and ETag headers work hand-in-hand to balance '
                                                'performance and freshness by separating freshness validation from '
                                                'conditional revalidation: 1. Cache-Control controls freshness: It '
                                                'tells the browser whether it can serve an asset directly from cache '
                                                "without hitting the network. Directives like 'max-age=86400' tell the "
                                                'browser the asset is fresh for 24 hours. A critical directive is '
                                                "'no-cache': it doesn't mean 'don't cache'—it means the browser CAN "
                                                'store the file, but must revalidate with the server before using it. '
                                                "In contrast, 'no-store' means do not cache at all, which is what you "
                                                'use for sensitive user data. 2. ETag enables conditional '
                                                'revalidation: An ETag is an entity tag—usually an MD5 or SHA hash of '
                                                "the file content sent by the server. When a cached file's max-age "
                                                "expires, the browser doesn't download the whole file again blindly. "
                                                "It issues a conditional GET request with the header 'If-None-Match: "
                                                "<etag>'. The server compares this hash to the current version. If the "
                                                "file hasn't changed, the server responds with a lightweight '304 Not "
                                                "Modified' status with zero response body. The browser continues using "
                                                'its cached copy, saving immense bandwidth. 3. Modern caching pattern: '
                                                "In modern production apps, you serve index.html with 'Cache-Control: "
                                                "no-cache' and ETags, so new deploys are detected immediately. "
                                                'Meanwhile, your JavaScript and CSS files have content hashes in their '
                                                'filenames (like app.a8b3.js), so you can serve them with '
                                                "'Cache-Control: max-age=31536000, immutable' and cache them for a "
                                                'full year without ever worrying about stale code.',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'Cache-Control defines how long an asset can be cached using max-age '
                                                'in seconds. When an asset is within its max-age, the browser loads it '
                                                'directly from the cache without making any network request. Once '
                                                'max-age expires, the browser uses the ETag header for validation. The '
                                                'browser sends a request with If-None-Match containing the ETag hash. '
                                                "If the file on the server hasn't changed, the server returns 304 Not "
                                                'Modified with no body, and the browser reuses the cached file. This '
                                                'saves server bandwidth.',
                                 'missing_concepts': ['Modern deployment caching strategy: Content-hashed static '
                                                      'assets (bundle.a8f9.js) use long-lived caching '
                                                      '(max-age=31536000, immutable); HTML files use no-cache with '
                                                      'ETags to ensure instant deployment updates']},
                                {'quality_level': 'average',
                                 'human_score': 61,
                                 'answer_text': 'Cache-Control is a header that tells the browser how many seconds to '
                                                'cache a file, like max-age=3600 for one hour. no-cache means the '
                                                'browser has to check with the server before using the cached version. '
                                                'ETag is a hash of the file that the server sends. When the browser '
                                                'requests the file again, it sends the ETag back. If the file is still '
                                                "the same, the server returns 304 so the browser doesn't have to "
                                                'download it again.',
                                 'missing_concepts': ['Conditional GET requests: When cached asset freshness expires, '
                                                      "the browser issues a conditional request with 'If-None-Match: "
                                                      "<etag>'; if content is unchanged, server responds with '304 Not "
                                                      "Modified' with no body, saving bandwidth",
                                                      'Modern deployment caching strategy: Content-hashed static '
                                                      'assets (bundle.a8f9.js) use long-lived caching '
                                                      '(max-age=31536000, immutable); HTML files use no-cache with '
                                                      'ETags to ensure instant deployment updates']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': 'ETag is an electronic tag used by RFID readers on website servers. '
                                                'Cache-Control is a CSS rule that hides images when the user is on 3G. '
                                                'When the server returns 304 Not Modified, it means the database is '
                                                'locked and the user must refresh.',
                                 'missing_concepts': ["Cache-Control directives: 'max-age=N' defines freshness "
                                                      "lifetime in seconds; 'no-cache' mandates server validation "
                                                      "before using cached copy; 'no-store' forbids any caching; "
                                                      "'immutable' indicates asset content will never change",
                                                      'ETag (Entity Tag) mechanism: An HTTP response header providing '
                                                      'a cryptographic hash or version identifier representing the '
                                                      'exact state of the resource representation',
                                                      'Conditional GET requests: When cached asset freshness expires, '
                                                      "the browser issues a conditional request with 'If-None-Match: "
                                                      "<etag>'; if content is unchanged, server responds with '304 Not "
                                                      "Modified' with no body, saving bandwidth",
                                                      'Modern deployment caching strategy: Content-hashed static '
                                                      'assets (bundle.a8f9.js) use long-lived caching '
                                                      '(max-age=31536000, immutable); HTML files use no-cache with '
                                                      'ETags to ensure instant deployment updates']}]},
            {'topic_tag': 'GraphQL vs REST Architecture',
             'question': 'What architectural advantages and trade-offs does GraphQL offer over traditional REST APIs '
                         'regarding data fetching?',
             'keywords': ['GraphQL', 'REST', 'Over-fetching', 'Under-fetching', 'Schema Definition', 'Single Endpoint'],
             'expected_concepts': ['Solving Over-fetching and Under-fetching: REST endpoints return fixed data '
                                   'structures; GraphQL allows clients to query exact fields needed in a single '
                                   'request, preventing over-fetching and eliminating multiple roundtrips '
                                   '(under-fetching)',
                                   'Schema Definition Language (SDL) & Strict Typing: GraphQL APIs are contract-driven '
                                   'with a strongly typed schema, providing automated documentation, introspection, '
                                   'and client-side code generation (TypeScript types)',
                                   'Single Endpoint Architecture: REST uses multiple resource-based URIs with HTTP '
                                   'verbs; GraphQL routes all queries, mutations, and subscriptions through a single '
                                   'POST endpoint (/graphql)',
                                   'Trade-offs and challenges: GraphQL shifts complexity to the backend (N+1 database '
                                   'query problem requiring DataLoader), loses out-of-the-box HTTP response caching '
                                   '(requires client caches like Apollo/Relay), and is vulnerable to deeply nested '
                                   'query denial-of-service'],
             'model_answer': 'GraphQL, created by Facebook, is an open-source data query and manipulation language '
                             'that presents a fundamentally different architectural model than REST: 1. Core '
                             'Architectural Advantages: - Eliminating Over-fetching and Under-fetching: In REST, '
                             "endpoint responses are fixed. A mobile client requesting '/users/1' receives a large "
                             'JSON payload with 40 fields even if it only needs the username (over-fetching). '
                             'Conversely, displaying a user profile with their recent orders and reviews often '
                             "requires three roundtrips: '/users/1', '/users/1/orders', and '/users/1/reviews' "
                             '(under-fetching / waterfall requests). GraphQL allows the client to formulate a single '
                             "declarative query specifying the exact fields across relationships: '{ user(id: 1) { "
                             "name orders { total } } }'. - Strongly Typed Schema (SDL): GraphQL schemas act as a "
                             'strict type contract. This enables automated documentation, playground exploration '
                             '(GraphiQL), and compile-time TypeScript type generation (via GraphQL Code Generator). 2. '
                             'Key Architectural Trade-offs: - HTTP Caching Difficulties: REST natively leverages '
                             'standard HTTP status codes, ETags, and CDN edge caching via GET requests. Because '
                             "GraphQL operations typically execute as POST requests to a single endpoint ('/graphql'), "
                             'standard HTTP caching fails; caching must be managed on the client side using normalized '
                             'cache graphs (e.g., Apollo Client, Urql). - The N+1 Database Problem: In GraphQL, nested '
                             'field resolvers execute independently. Querying 10 users and their posts naively '
                             'executes 1 query for users plus 10 queries for posts (N+1 problem), requiring batching '
                             "and caching utilities like Facebook's DataLoader. - Security and Query Complexity: "
                             "Malicious clients can submit deeply nested circular queries ('user { friends { friends { "
                             "friends ... } } }'), overwhelming database servers unless query depth limiting and cost "
                             'analysis are enforced.',
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 96,
                                 'answer_text': 'GraphQL and REST represent two different philosophies for '
                                                'client-server communication. The primary motivation for GraphQL is '
                                                'solving over-fetching and under-fetching: In REST, endpoints return '
                                                'fixed payloads. If you fetch /users/123, you might get 50 fields when '
                                                "your mobile app only needs the username—that's over-fetching, which "
                                                "wastes bandwidth. At the same time, if you need a user's posts and "
                                                "comments, REST requires three separate sequential API calls—that's "
                                                'under-fetching, which creates network waterfalls. GraphQL solves both '
                                                'by exposing a single endpoint (typically POST /graphql) and allowing '
                                                'the client to specify the exact shape and nested fields it needs in a '
                                                'single declarative query. Furthermore, GraphQL is strictly typed '
                                                'using Schema Definition Language (SDL), which enables incredible '
                                                'developer tooling like automatic TypeScript type generation and '
                                                'GraphiQL introspection. However, GraphQL introduces real '
                                                'architectural trade-offs: 1. Caching is much harder. In REST, you can '
                                                'cache GET /products/123 at the browser or CDN level using standard '
                                                'HTTP headers like Cache-Control and ETags. In GraphQL, because '
                                                'everything is a POST request to one URL, standard HTTP caching '
                                                "doesn't work; you have to rely on complex normalized client-side "
                                                'caches like Apollo. 2. Backend complexity: GraphQL resolvers can '
                                                'easily trigger the N+1 database problem when querying relations, '
                                                'requiring tools like DataLoader to batch SQL queries. 3. Security: '
                                                'Malicious users can send deeply nested queries that exhaust server '
                                                'CPU unless you implement query complexity analysis and depth '
                                                'limiting.',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'GraphQL offers major advantages over REST by eliminating '
                                                'over-fetching and under-fetching. With REST, you hit fixed endpoints '
                                                'and often get more data than you need, or you have to make multiple '
                                                'API requests to fetch related data. With GraphQL, the client asks for '
                                                'exactly the fields it needs in a single request to a single /graphql '
                                                'endpoint. It also has a strongly typed schema that helps with '
                                                'TypeScript generation. The trade-offs are that HTTP caching is harder '
                                                'because all queries are POST requests, and on the backend, resolvers '
                                                'can suffer from the N+1 query problem, requiring DataLoader to batch '
                                                'database calls.',
                                 'missing_concepts': ['Trade-offs and challenges: GraphQL shifts complexity to the '
                                                      'backend (N+1 database query problem requiring DataLoader), '
                                                      'loses out-of-the-box HTTP response caching (requires client '
                                                      'caches like Apollo/Relay), and is vulnerable to deeply nested '
                                                      'query denial-of-service']},
                                {'quality_level': 'average',
                                 'human_score': 61,
                                 'answer_text': 'REST uses multiple endpoints like /users and /posts with HTTP verbs '
                                                'like GET and POST. GraphQL has only one endpoint and lets the '
                                                'frontend ask for exactly the fields it wants, which stops '
                                                'over-fetching and under-fetching. The backend uses a schema with '
                                                'types and queries. The downside of GraphQL is that it is more '
                                                'complicated to set up on the backend than REST, and caching is harder '
                                                "because you can't use normal browser HTTP caching.",
                                 'missing_concepts': ['Schema Definition Language (SDL) & Strict Typing: GraphQL APIs '
                                                      'are contract-driven with a strongly typed schema, providing '
                                                      'automated documentation, introspection, and client-side code '
                                                      'generation (TypeScript types)',
                                                      'Trade-offs and challenges: GraphQL shifts complexity to the '
                                                      'backend (N+1 database query problem requiring DataLoader), '
                                                      'loses out-of-the-box HTTP response caching (requires client '
                                                      'caches like Apollo/Relay), and is vulnerable to deeply nested '
                                                      'query denial-of-service']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': 'GraphQL is a database that replaces MongoDB and PostgreSQL. REST APIs '
                                                'are deprecated because they can only transfer plain text, while '
                                                'GraphQL transfers binary data. GraphQL runs on port 8080 and does not '
                                                'use HTTP.',
                                 'missing_concepts': ['Solving Over-fetching and Under-fetching: REST endpoints return '
                                                      'fixed data structures; GraphQL allows clients to query exact '
                                                      'fields needed in a single request, preventing over-fetching and '
                                                      'eliminating multiple roundtrips (under-fetching)',
                                                      'Schema Definition Language (SDL) & Strict Typing: GraphQL APIs '
                                                      'are contract-driven with a strongly typed schema, providing '
                                                      'automated documentation, introspection, and client-side code '
                                                      'generation (TypeScript types)',
                                                      'Single Endpoint Architecture: REST uses multiple resource-based '
                                                      'URIs with HTTP verbs; GraphQL routes all queries, mutations, '
                                                      'and subscriptions through a single POST endpoint (/graphql)',
                                                      'Trade-offs and challenges: GraphQL shifts complexity to the '
                                                      'backend (N+1 database query problem requiring DataLoader), '
                                                      'loses out-of-the-box HTTP response caching (requires client '
                                                      'caches like Apollo/Relay), and is vulnerable to deeply nested '
                                                      'query denial-of-service']}]},
            {'topic_tag': 'Node.js Streams & Backpressure',
             'question': 'How do Node.js readable/writable streams handle backpressure when reading large data '
                         'payloads?',
             'keywords': ['Streams',
                          'Readable/Writable Stream',
                          'Pipe()',
                          'Backpressure',
                          'Buffer Management',
                          'Memory Efficiency'],
             'expected_concepts': ['Memory efficiency of streams: Streams process data chunk-by-chunk in small buffer '
                                   'chunks rather than buffering entire multi-gigabyte files into RAM',
                                   'Backpressure defined: Occurs when a Readable stream produces data faster than a '
                                   'Writable stream can consume/write it (e.g., fast SSD read to slow network socket)',
                                   'Backpressure signaling mechanism: writable.write(chunk) returns false when its '
                                   'internal buffer exceeds highWaterMark (default 16KB/64KB); readable calls '
                                   "readable.pause() and resumes only when writable emits the 'drain' event",
                                   'Automatic management via pipe(): readable.pipe(writable) or pipeline() handles '
                                   'this pause/drain negotiation automatically, preventing RAM exhaustion'],
             'model_answer': 'In Node.js, streams provide an asynchronous, chunk-by-chunk data processing abstraction '
                             'that handles massive payloads (multi-gigabyte video files, log streams) with constant, '
                             'minimal memory consumption: 1. The Backpressure Problem: Backpressure occurs when the '
                             'data producer (Readable stream) emits data at a rate faster than the data consumer '
                             '(Writable stream) can process and write it. For example, reading a file from a '
                             'high-speed NVMe SSD at 500 MB/s and streaming it over a slow 1 MB/s mobile TCP '
                             'connection. If unmanaged, incoming chunks accumulate in memory buffers until Node.js '
                             'crashes with an out-of-memory error (JavaScript heap out of memory). 2. The Backpressure '
                             'Signaling Mechanism: - Every stream has an internal buffer governed by the '
                             "'highWaterMark' threshold (typically 16KB for object mode or 64KB for binary streams). - "
                             "When data is written to a writable stream via 'writable.write(chunk)', the method "
                             "returns a boolean: 'true' if the internal buffer is below highWaterMark, or 'false' if "
                             "the buffer is full and backpressure has triggered. - Upon receiving 'false', the "
                             "producer MUST pause: 'readable.pause()'. - Once the consumer finishes processing and "
                             "flushes its internal buffer, the writable stream emits the 'drain' event. - The producer "
                             'listens for \'writable.once("drain", () => readable.resume())\' and restarts reading '
                             'chunks. 3. Automated Handling with pipe() and pipeline(): Developers rarely implement '
                             "manual pause/drain logic. The native 'readable.pipe(writable)' method (and "
                             "'stream.pipeline()' from the stream module) automatically manages backpressure, pausing "
                             'the readable stream when the writable buffer fills and resuming on drain while ensuring '
                             'clean error cleanup.',
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 97,
                                 'answer_text': 'In Node.js, streams process data chunk by chunk rather than loading '
                                                'entire files into memory. Backpressure occurs when the producer (a '
                                                'Readable stream) reads data faster than the consumer (a Writable '
                                                'stream) can write or send it. A classic example is reading a 5GB file '
                                                'from an NVMe SSD and streaming it over a slow mobile network '
                                                'connection. If there were no backpressure, the reader would dump all '
                                                "5GB into Node's internal memory buffer in seconds, blowing through "
                                                'the V8 heap limit and crashing the server. Node.js handles '
                                                'backpressure through a built-in signaling mechanism governed by a '
                                                'threshold called highWaterMark (which defaults to 64KB for byte '
                                                'streams): 1. The readable stream pushes chunks to the writable stream '
                                                "using 'writable.write(chunk)'. 2. If the writable stream's internal "
                                                "buffer exceeds highWaterMark, 'writable.write()' returns false. This "
                                                'boolean is the backpressure signal. 3. Upon receiving false, the '
                                                'readable stream must immediately stop reading by calling '
                                                "'readable.pause()'. 4. When the writable stream finishes sending "
                                                'those bytes over the network and flushes its buffer, it emits a '
                                                "'drain' event. 5. The readable stream listens for the 'drain' event, "
                                                "calls 'readable.resume()', and resumes streaming. If you use "
                                                "'readable.pipe(writable)' or modern 'stream.pipeline()', Node handles "
                                                'this entire pause and drain handshake automatically behind the '
                                                'scenes.',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'Streams in Node.js process data in small chunks to avoid loading huge '
                                                'files into RAM. Backpressure happens when the readable stream reads '
                                                'data faster than the writable stream can process it, like reading '
                                                'from disk and writing to a slow network socket. When the writable '
                                                "stream's internal buffer reaches the highWaterMark, "
                                                'writable.write(chunk) returns false. The readable stream then pauses. '
                                                "Once the writable stream empties its buffer, it emits a 'drain' "
                                                'event, which tells the readable stream to resume sending chunks. '
                                                'Using readable.pipe(writable) handles this automatically.',
                                 'missing_concepts': ['Memory efficiency of streams: Streams process data '
                                                      'chunk-by-chunk in small buffer chunks rather than buffering '
                                                      'entire multi-gigabyte files into RAM']},
                                {'quality_level': 'average',
                                 'human_score': 60,
                                 'answer_text': 'Backpressure is when data comes in faster than Node can write it. If '
                                                'you read a 10GB file without streams, your server crashes with out of '
                                                'memory. Streams fix this by reading chunk by chunk. When the writable '
                                                'buffer gets full, it tells the readable stream to stop sending data '
                                                'until it finishes writing, and then it continues using the drain '
                                                'event. You usually just use pipe() to connect readable and writable '
                                                'streams together.',
                                 'missing_concepts': ['Backpressure signaling mechanism: writable.write(chunk) returns '
                                                      'false when its internal buffer exceeds highWaterMark (default '
                                                      '16KB/64KB); readable calls readable.pause() and resumes only '
                                                      "when writable emits the 'drain' event",
                                                      'Automatic management via pipe(): readable.pipe(writable) or '
                                                      'pipeline() handles this pause/drain negotiation automatically, '
                                                      'preventing RAM exhaustion']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': 'Backpressure is a technique used in CSS Flexbox to reverse the '
                                                'direction of items. Node.js streams are used to stream Netflix movies '
                                                'over WebSockets. If backpressure happens, you fix it by increasing '
                                                "your computer's virtual RAM in Windows settings.",
                                 'missing_concepts': ['Memory efficiency of streams: Streams process data '
                                                      'chunk-by-chunk in small buffer chunks rather than buffering '
                                                      'entire multi-gigabyte files into RAM',
                                                      'Backpressure defined: Occurs when a Readable stream produces '
                                                      'data faster than a Writable stream can consume/write it (e.g., '
                                                      'fast SSD read to slow network socket)',
                                                      'Backpressure signaling mechanism: writable.write(chunk) returns '
                                                      'false when its internal buffer exceeds highWaterMark (default '
                                                      '16KB/64KB); readable calls readable.pause() and resumes only '
                                                      "when writable emits the 'drain' event",
                                                      'Automatic management via pipe(): readable.pipe(writable) or '
                                                      'pipeline() handles this pause/drain negotiation automatically, '
                                                      'preventing RAM exhaustion']}]},
            {'topic_tag': 'Web Workers Multithreading',
             'question': 'How do Web Workers allow running CPU-intensive JavaScript tasks on background threads '
                         'without freezing the UI?',
             'keywords': ['Web Workers',
                          'Dedicated Worker',
                          'PostMessage()',
                          'Main Thread Unblocking',
                          'Worker Scope',
                          'No DOM Access'],
             'expected_concepts': ['Main thread limitation: Browser UI rendering, user interaction, and JavaScript '
                                   'execution share a single main thread; heavy CPU operations (image processing, big '
                                   'data calculation, cryptography) cause UI jank and dropped frames',
                                   'Dedicated Worker architecture: Web Workers run on isolated OS background threads, '
                                   "executing code concurrently without interfering with the main thread's 60fps "
                                   'render loop',
                                   'Communication via postMessage: Main thread and worker communicate strictly via '
                                   'asynchronous message passing (postMessage and onmessage) using the structured '
                                   'clone algorithm or Transferable Objects',
                                   'Environment constraints: Workers run in WorkerGlobalScope (self), having NO access '
                                   'to the DOM (document/window), but retaining access to fetch, WebSockets, '
                                   'IndexedDB, and timers'],
             'model_answer': 'Because JavaScript in the browser is single-threaded, any computationally intensive '
                             'task—such as client-side image filtering, ray tracing, large CSV/JSON parsing, or '
                             'cryptographic hashing—monopolizes the main thread. This prevents the browser from '
                             'processing user clicks or executing layout/paint passes, causing the page to freeze '
                             "('jank') and triggering browser 'Page Unresponsive' warnings. Web Workers solve this by "
                             'introducing true multithreading to web applications: 1. Architecture: A Dedicated Worker '
                             '(\'const worker = new Worker("worker.js")\') runs in a completely separate operating '
                             'system background thread. Heavy computations execute concurrently on that background '
                             'thread while the main thread remains 100% idle and responsive to handle UI animations at '
                             '60/120 fps. 2. Message-Passing Communication: The main thread and worker communicate '
                             "exclusively through an asynchronous messaging interface: - 'worker.postMessage(data)' "
                             "dispatches messages. - 'worker.onmessage = (e) => { console.log(e.data); }' receives "
                             'results. - Data transferred via postMessage is serialized using the Structured Clone '
                             'Algorithm (deep copy). For high-performance binary data (e.g., large ArrayBuffers or '
                             'ImageData), developers can transfer ownership using Transferable Objects '
                             "('worker.postMessage(buffer, [buffer])'), transferring memory pointers in zero-copy O(1) "
                             'time. 3. Execution Scope Restrictions: To prevent race conditions and thread '
                             'synchronization hazards (like deadlocks), Web Workers run in an isolated '
                             "'DedicatedWorkerGlobalScope' ('self'): - No DOM access: Workers cannot access 'window', "
                             "'document', or DOM elements directly. - Permitted APIs: Workers can utilize 'fetch()', "
                             "'XMLHttpRequest', 'WebSockets', 'IndexedDB', 'crypto', and standard JavaScript timers.",
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 96,
                                 'answer_text': "Because JavaScript's main thread handles both code execution and UI "
                                                'rendering, running a heavy CPU task—like client-side image '
                                                'processing, large dataset sorting, or encryption—blocks the main '
                                                "thread completely. The user can't click buttons, scroll, or see CSS "
                                                'animations, and the UI completely freezes. Web Workers solve this by '
                                                'running code on a completely separate operating system thread in the '
                                                "background. You instantiate a worker by calling 'const worker = new "
                                                "Worker('worker.js')'. The worker runs its heavy loop on its own "
                                                "thread without ever interrupting the main thread's 60fps render loop. "
                                                'Communication between the main thread and the worker happens strictly '
                                                "via asynchronous message passing: you call 'worker.postMessage(data)' "
                                                "to send work, and listen with 'worker.onmessage' to receive results. "
                                                'By default, data is copied using the structured clone algorithm, but '
                                                'for large binary data like image pixels or ArrayBuffers, you can pass '
                                                'them as Transferable Objects to transfer memory ownership in O(1) '
                                                'time without copying. The critical constraint to remember is that Web '
                                                'Workers run in WorkerGlobalScope—they have zero access to the DOM, '
                                                'window, or document. This prevents race conditions like deadlocks. '
                                                'However, they can still make network calls with fetch, use IndexedDB, '
                                                'and set timers.',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'Web Workers allow JavaScript to run tasks on background threads so '
                                                "that heavy computations don't freeze the main UI thread. In normal "
                                                'JavaScript, running a long computation blocks user interactions and '
                                                'animations. A Web Worker runs on an isolated background thread and '
                                                'communicates with the main thread using postMessage and onmessage '
                                                'event listeners. The data passed between them is copied. The main '
                                                'limitation is that Web Workers do not have access to the DOM or '
                                                'window object, but they can still use fetch and perform CPU-intensive '
                                                'tasks.',
                                 'missing_concepts': ['Communication via postMessage: Main thread and worker '
                                                      'communicate strictly via asynchronous message passing '
                                                      '(postMessage and onmessage) using the structured clone '
                                                      'algorithm or Transferable Objects']},
                                {'quality_level': 'average',
                                 'human_score': 60,
                                 'answer_text': 'Web Workers are used for multi-threading in JavaScript. Normally '
                                                'JavaScript only has one thread, so if you run a heavy loop, the '
                                                'browser freezes. A Web Worker runs the code in the background on '
                                                'another thread so the page stays smooth. You talk to the worker using '
                                                'worker.postMessage() and receive data with onmessage. Workers cannot '
                                                'touch the DOM directly, so they have to send the calculated data back '
                                                'to the main thread to update the HTML.',
                                 'missing_concepts': ['Main thread limitation: Browser UI rendering, user interaction, '
                                                      'and JavaScript execution share a single main thread; heavy CPU '
                                                      'operations (image processing, big data calculation, '
                                                      'cryptography) cause UI jank and dropped frames',
                                                      'Environment constraints: Workers run in WorkerGlobalScope '
                                                      '(self), having NO access to the DOM (document/window), but '
                                                      'retaining access to fetch, WebSockets, IndexedDB, and timers']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': 'Web Workers are human freelancers hired by Google to monitor websites '
                                                'for bugs. In JavaScript, a Web Worker is created by adding <worker> '
                                                'tags into the HTML head. Web Workers have full access to modify DOM '
                                                'nodes and style sheets directly.',
                                 'missing_concepts': ['Main thread limitation: Browser UI rendering, user interaction, '
                                                      'and JavaScript execution share a single main thread; heavy CPU '
                                                      'operations (image processing, big data calculation, '
                                                      'cryptography) cause UI jank and dropped frames',
                                                      'Dedicated Worker architecture: Web Workers run on isolated OS '
                                                      'background threads, executing code concurrently without '
                                                      "interfering with the main thread's 60fps render loop",
                                                      'Communication via postMessage: Main thread and worker '
                                                      'communicate strictly via asynchronous message passing '
                                                      '(postMessage and onmessage) using the structured clone '
                                                      'algorithm or Transferable Objects',
                                                      'Environment constraints: Workers run in WorkerGlobalScope '
                                                      '(self), having NO access to the DOM (document/window), but '
                                                      'retaining access to fetch, WebSockets, IndexedDB, and '
                                                      'timers']}]},
            {'topic_tag': 'Service Workers & PWA Caching',
             'question': 'How do Service Workers intercept fetch events to enable offline caching in Progressive Web '
                         'Apps (PWAs)?',
             'keywords': ['Service Worker',
                          'Cache Storage API',
                          'Fetch Event',
                          'Offline Mode',
                          'PWA Manifest',
                          'Background Sync'],
             'expected_concepts': ['Service Worker lifecycle and role: Programmable client-side network proxy running '
                                   "on a separate thread, registered by the page and controlling an origin's network "
                                   'requests',
                                   "Fetch event interception: Listens to the 'fetch' event "
                                   "(self.addEventListener('fetch', event => ...)), allowing programmatic interception "
                                   'of every HTTP request made by the web app',
                                   "Cache Storage API: Works with CacheStorage (caches.open('v1'), cache.put(), "
                                   'cache.match()) to persist request/response pairs for offline retrieval',
                                   'Caching strategies: Implements architectural caching patterns such as Cache-First '
                                   '(instant offline load for static assets), Network-First (freshest data with '
                                   'offline fallback), and Stale-While-Revalidate'],
             'model_answer': 'Service Workers are the foundational technology powering Progressive Web Apps (PWAs), '
                             'acting as programmable, client-side network proxies between the browser, web '
                             'application, and network: 1. Architecture and Lifecycle: A Service Worker is an '
                             "event-driven worker registered via 'navigator.serviceWorker.register('/sw.js')'. It runs "
                             'on an independent background thread, possesses no DOM access, and operates over HTTPS '
                             "for security. It progresses through a strict lifecycle: 'install' (where initial core "
                             "app assets are pre-cached), 'activate' (where outdated cache versions are purged), and "
                             'running/idle. 2. Fetch Event Interception: Once activated, the Service Worker intercepts '
                             "every single network request originating from pages within its scope via the 'fetch' "
                             'event listener: \'self.addEventListener("fetch", event => { ... })\'. Inside this '
                             'handler, the Service Worker can inspect the request and take complete control using '
                             "'event.respondWith()'. It can forward the request to the network, return a locally "
                             'cached response, synthesize a custom response, or combine them. 3. Cache Storage API '
                             'Integration: Service Workers use the CacheStorage interface to store raw '
                             "Request/Response pairs. Inside 'event.respondWith()', common caching strategies are "
                             'implemented: - Cache-First (Falling back to Network): Inspects '
                             "'caches.match(event.request)'. If a match exists, it serves the cached asset instantly "
                             'without network latency. If missing, it fetches from the network and caches the '
                             'response. Ideal for static assets (JS, CSS, images, fonts). - Network-First (Falling '
                             "back to Cache): Attempts 'fetch(event.request)' first to obtain the freshest data. If "
                             'offline or the network fails, it catches the error and serves the cached copy. Ideal for '
                             'live data feeds. - Stale-While-Revalidate: Returns the cached response immediately for '
                             'instant speed, while simultaneously making a background network fetch to update the '
                             'cache for the next page view.',
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 96,
                                 'answer_text': 'A Service Worker is an event-driven background worker that acts as a '
                                                'programmable proxy sitting between the browser, the web app, and the '
                                                'internet. Once registered and activated, the Service Worker '
                                                'intercepts every single HTTP request made by the web app through its '
                                                "'fetch' event listener: 'self.addEventListener('fetch', event => { "
                                                "... })'. Inside this listener, you call 'event.respondWith()', which "
                                                'allows you to completely hijack the response. You can serve assets '
                                                'directly from the Cache Storage API instead of going to the network, '
                                                'enabling complete offline functionality. There are three main caching '
                                                'strategies used in PWAs: 1. Cache-First: The Service Worker checks '
                                                "'caches.match(event.request)' first. If the file is in cache, it "
                                                'returns it instantly with zero network delay. If not, it fetches from '
                                                'the network and stores it in cache. This is ideal for static assets '
                                                'like JavaScript bundles, CSS, and fonts. 2. Network-First: The '
                                                'Service Worker attempts to fetch over the network first to get the '
                                                'freshest data. If the user is offline or the request fails, it falls '
                                                'back to the cached version. This is great for dynamic API data. 3. '
                                                'Stale-While-Revalidate: It serves the cached version immediately for '
                                                'instant page loads, while simultaneously fetching an updated copy in '
                                                'the background to refresh the cache for next time. Combined with a '
                                                'Web App Manifest, Service Workers turn a website into an installable, '
                                                'offline-capable PWA.',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'Service Workers enable offline mode in PWAs by acting as a network '
                                                'proxy. When your app makes any network request, the service worker '
                                                "intercepts it using self.addEventListener('fetch'). It uses the Cache "
                                                'Storage API to store request and response pairs. In '
                                                'event.respondWith(), you can implement caching strategies: a '
                                                'Cache-First strategy checks the cache first and serves the asset '
                                                'offline if the network is down, while a Network-First strategy tries '
                                                'the internet first and falls back to cache. This lets web apps load '
                                                'and work even when completely offline.',
                                 'missing_concepts': ['Caching strategies: Implements architectural caching patterns '
                                                      'such as Cache-First (instant offline load for static assets), '
                                                      'Network-First (freshest data with offline fallback), and '
                                                      'Stale-While-Revalidate']},
                                {'quality_level': 'average',
                                 'human_score': 61,
                                 'answer_text': 'Service Workers are JavaScript files that run in the background to '
                                                'make Progressive Web Apps work offline. They listen for fetch events '
                                                "and check if the requested file is stored in the browser's Cache "
                                                'Storage. If the user has no internet connection, the service worker '
                                                'returns the cached file so the app still loads. You also need a '
                                                "manifest.json file so users can install the PWA to their phone's home "
                                                'screen.',
                                 'missing_concepts': ['Service Worker lifecycle and role: Programmable client-side '
                                                      'network proxy running on a separate thread, registered by the '
                                                      "page and controlling an origin's network requests",
                                                      'Caching strategies: Implements architectural caching patterns '
                                                      'such as Cache-First (instant offline load for static assets), '
                                                      'Network-First (freshest data with offline fallback), and '
                                                      'Stale-While-Revalidate']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': 'Service Workers are server administrators who manage AWS hosting. PWA '
                                                "offline caching works by downloading the entire server's MySQL "
                                                "database into the browser's cookies. Fetch events only happen when "
                                                'you use the jQuery ajax library.',
                                 'missing_concepts': ['Service Worker lifecycle and role: Programmable client-side '
                                                      'network proxy running on a separate thread, registered by the '
                                                      "page and controlling an origin's network requests",
                                                      "Fetch event interception: Listens to the 'fetch' event "
                                                      "(self.addEventListener('fetch', event => ...)), allowing "
                                                      'programmatic interception of every HTTP request made by the web '
                                                      'app',
                                                      "Cache Storage API: Works with CacheStorage (caches.open('v1'), "
                                                      'cache.put(), cache.match()) to persist request/response pairs '
                                                      'for offline retrieval',
                                                      'Caching strategies: Implements architectural caching patterns '
                                                      'such as Cache-First (instant offline load for static assets), '
                                                      'Network-First (freshest data with offline fallback), and '
                                                      'Stale-While-Revalidate']}]},
            {'topic_tag': 'TypeScript Interfaces vs Type Aliases',
             'question': 'Compare TypeScript Interfaces and Type Aliases regarding declaration merging, union types, '
                         'and extensibility.',
             'keywords': ['TypeScript Interfaces',
                          'Type Aliases',
                          'Union Types',
                          'Interface Merging',
                          'Generics',
                          'Type Safety'],
             'expected_concepts': ['Declaration merging: Multiple interface declarations with the same name '
                                   'automatically merge their member definitions into a single interface; Type Aliases '
                                   'throw a compile-time duplicate identifier error',
                                   'Union, primitive, and tuple types: Type Aliases can define unions (type Status = '
                                   "'open' | 'closed'), primitives (type ID = string | number), and tuples; Interfaces "
                                   'are strictly limited to describing object shapes',
                                   "Extensibility syntax: Interfaces extend other interfaces via the 'extends' "
                                   'keyword; Type Aliases achieve inheritance/combination using intersection operators '
                                   '(&)',
                                   'Industry guidelines: Use Interfaces for public API object definitions and '
                                   'object-oriented contracts (allowing consumer extension); use Type Aliases for '
                                   'unions, utility types, and complex type transformations'],
             'model_answer': "In TypeScript, both Interfaces ('interface User {}') and Type Aliases ('type User = {}') "
                             'define structural shapes and contracts, but they differ across critical functional and '
                             'architectural dimensions: 1. Declaration Merging: - Interfaces support automatic '
                             "declaration merging. If you declare 'interface Window { myGlobal: string; }' multiple "
                             'times, TypeScript merges all declarations into a single unified interface. This is '
                             'essential for third-party library typing, polyfills, and ambient module augmentation. - '
                             "Type Aliases do not support declaration merging. Defining 'type Point = { x: number }; "
                             "type Point = { y: number };' throws a compile-time Duplicate Identifier error. 2. "
                             'Unions, Primitives, and Mapped Types: - Type Aliases are vastly more expressive. A type '
                             "alias can define union types ('type Status = 'pending' | 'success' | 'failed''), "
                             "primitive aliases ('type UUID = string'), tuples ('type Coordinates = [number, "
                             "number]'), and mapped/conditional types. - Interfaces can ONLY define object shapes and "
                             'method signatures; they cannot represent union types or alias primitive types directly. '
                             '3. Extensibility and Inheritance: - Interfaces extend other interfaces using the '
                             "'extends' keyword: 'interface Admin extends User { role: string; }'. The TypeScript "
                             'compiler validates that extending does not produce incompatible conflicting property '
                             "types. - Type Aliases combine shapes using intersection operators (&): 'type Admin = "
                             "User & { role: string; }'. 4. Best Practice Guideline: Modern TypeScript style guides "
                             'recommend using Interfaces for object contracts and public-facing APIs (enabling '
                             'consumers to extend them via declaration merging), and using Type Aliases for union '
                             'types, tuples, function signatures, and complex type-level programming.',
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 96,
                                 'answer_text': 'In TypeScript, both Interfaces and Type Aliases define data shapes, '
                                                'but they differ in declaration merging, union capabilities, and '
                                                'extensibility syntax: 1. Declaration Merging: This is the biggest '
                                                'difference. If you declare an interface with the same name twice in '
                                                'the same scope, TypeScript automatically merges their definitions '
                                                'into one interface. This is crucial when augmenting existing '
                                                'libraries or extending the global Window object. Type aliases, '
                                                "however, cannot be merged—declaring 'type Person' twice in the same "
                                                'file throws a duplicate identifier error. 2. Unions and Primitives: '
                                                'Type aliases are much more versatile. A type alias can represent '
                                                "union types like 'type Status = 'loading' | 'success' | 'error'', "
                                                "primitive aliases like 'type ID = string | number', tuple types, and "
                                                'advanced mapped or conditional types. Interfaces can only define the '
                                                'shape of an object or function; you cannot create an interface that '
                                                'is a union of strings. 3. Extensibility syntax: Interfaces extend '
                                                "other interfaces using the clean 'extends' keyword: 'interface Admin "
                                                "extends User { role: string }'. Type aliases achieve combination "
                                                "using intersection types with the ampersand operator: 'type Admin = "
                                                "User & { role: string }'. 4. Best practices: The common rule of thumb "
                                                'is to use Interfaces for object models and public API contracts where '
                                                'consumers might need to extend them via declaration merging, and use '
                                                'Type Aliases for unions, utility types, and complex type '
                                                'transformations.',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'Interfaces and Type Aliases can both describe object shapes in '
                                                'TypeScript. The main difference is declaration merging: if you '
                                                'declare the same interface twice, TypeScript merges them together '
                                                'automatically, which is useful for extending library types. Type '
                                                'aliases cannot be merged and will throw an error if defined twice. '
                                                "However, type aliases can do union types like 'type ID = string | "
                                                "number' and tuples, which interfaces cannot do. Interfaces extend "
                                                'each other using the extends keyword, while types use intersection '
                                                'with the & symbol.',
                                 'missing_concepts': ['Industry guidelines: Use Interfaces for public API object '
                                                      'definitions and object-oriented contracts (allowing consumer '
                                                      'extension); use Type Aliases for unions, utility types, and '
                                                      'complex type transformations']},
                                {'quality_level': 'average',
                                 'human_score': 61,
                                 'answer_text': 'Interfaces use the interface keyword and types use the type keyword. '
                                                "You can use types to create unions like type Theme = 'dark' | "
                                                "'light', which interfaces cannot do. Interfaces are used for objects "
                                                'and classes. Interfaces can extend other interfaces using extends. '
                                                'Type aliases can combine objects using the & operator. Most '
                                                'developers use interfaces for objects and types for unions.',
                                 'missing_concepts': ['Declaration merging: Multiple interface declarations with the '
                                                      'same name automatically merge their member definitions into a '
                                                      'single interface; Type Aliases throw a compile-time duplicate '
                                                      'identifier error',
                                                      'Extensibility syntax: Interfaces extend other interfaces via '
                                                      "the 'extends' keyword; Type Aliases achieve "
                                                      'inheritance/combination using intersection operators (&)']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': 'Interfaces are compiled into JavaScript objects at runtime, while '
                                                'type aliases are completely deleted by the compiler. Type aliases are '
                                                'only available in TypeScript 5.0. Interfaces cannot have optional '
                                                'properties.',
                                 'missing_concepts': ['Declaration merging: Multiple interface declarations with the '
                                                      'same name automatically merge their member definitions into a '
                                                      'single interface; Type Aliases throw a compile-time duplicate '
                                                      'identifier error',
                                                      'Union, primitive, and tuple types: Type Aliases can define '
                                                      "unions (type Status = 'open' | 'closed'), primitives (type ID = "
                                                      'string | number), and tuples; Interfaces are strictly limited '
                                                      'to describing object shapes',
                                                      'Extensibility syntax: Interfaces extend other interfaces via '
                                                      "the 'extends' keyword; Type Aliases achieve "
                                                      'inheritance/combination using intersection operators (&)',
                                                      'Industry guidelines: Use Interfaces for public API object '
                                                      'definitions and object-oriented contracts (allowing consumer '
                                                      'extension); use Type Aliases for unions, utility types, and '
                                                      'complex type transformations']}]},
            {'topic_tag': 'CSS Architecture (BEM vs Tailwind)',
             'question': 'Compare BEM methodology, CSS Modules, and Tailwind CSS in managing CSS maintainability and '
                         'global specificity wars.',
             'keywords': ['BEM Methodology',
                          'Tailwind CSS',
                          'CSS Modules',
                          'Utility-First',
                          'Maintainability',
                          'Specificity Wars'],
             'expected_concepts': ['Root problem: Global CSS namespace causes accidental style leaks, cascading '
                                   "conflicts, and escalating 'specificity wars' (!important arms races) in large "
                                   'codebases',
                                   'BEM (Block Element Modifier): Naming convention (.card, .card__header, '
                                   '.card__header--active) that enforces flat class-only specificity (0, 0, 1, 0) and '
                                   'structural readability, but requires writing manual CSS and long class names',
                                   'CSS Modules: Scopes CSS locally to a component by hashing class names at compile '
                                   'time (.button_x8f2), eliminating global namespace collisions while allowing '
                                   'standard CSS syntax',
                                   'Tailwind CSS (Utility-First): Composes pre-defined utility classes directly in '
                                   'markup (flex, p-4, bg-blue-500); completely eliminates specificity wars (all '
                                   'utilities have equal class specificity) and dead CSS via PurgeCSS/JIT'],
             'model_answer': 'In large-scale web applications, vanilla CSS suffers from a fundamental flaw: the global '
                             "namespace. Any CSS class declared anywhere can leak, collide, and cause 'specificity "
                             "wars' where developers use increasingly complex selectors or '!important' to override "
                             'conflicting rules. Three primary architectural philosophies address this challenge: 1. '
                             'BEM (Block, Element, Modifier): - Philosophy: A strict naming convention developed by '
                             "Yandex that organizes styles hierarchically: 'Block' (standalone component, e.g., "
                             "'.card'), 'Element' (sub-part tied to block, e.g., '.card__title'), and 'Modifier' "
                             "(state or theme variant, e.g., '.card__title--featured'). - Benefits & Trade-offs: "
                             'Enforces a strictly flat specificity model—every selector consists of a single class '
                             '(specificity 0, 0, 1, 0), eliminating specificity wars without build tools. However, '
                             'class names become extremely verbose, and it relies entirely on developer discipline to '
                             'avoid naming collisions. 2. CSS Modules: - Philosophy: Scopes CSS locally to individual '
                             'component files by hooking into bundlers (Webpack, Vite). A file named '
                             "'Button.module.css' declaring '.btn' is compiled into a unique, hashed class name in "
                             "production (e.g., '.Button_btn__a83b9'). - Benefits & Trade-offs: Completely eliminates "
                             'global namespace collisions automatically while letting developers write standard, '
                             'expressive CSS. However, sharing variables or global themes requires CSS variables or '
                             'preprocessors (Sass). 3. Tailwind CSS (Utility-First): - Philosophy: Rather than '
                             'authoring custom semantic CSS classes, developers compose single-purpose, pre-defined '
                             'utility classes directly inside HTML/JSX (e.g., \'class="flex items-center p-4 bg-white '
                             'rounded-lg shadow-md"\'). - Benefits & Trade-offs: Completely solves specificity wars '
                             'because all utility classes have identical specificity (0, 0, 1, 0). Its JIT compiler '
                             'generates only the classes actually used in source code, resulting in tiny production '
                             'CSS bundles (<10KB) regardless of application scale. The trade-off is crowded HTML/JSX '
                             'markup and an initial learning curve for utility class names.',
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 96,
                                 'answer_text': 'Managing CSS in large applications is all about avoiding global '
                                                'namespace pollution and specificity wars, where developers fight over '
                                                'cascaded styles and resort to !important. Here is how BEM, CSS '
                                                'Modules, and Tailwind approach this: 1. BEM (Block Element Modifier): '
                                                'BEM is a naming convention that creates structure using classes like '
                                                '.btn, .btn__icon, and .btn--large. The genius of BEM is that it keeps '
                                                'specificity completely flat—every selector is just a single class '
                                                'with specificity (0, 0, 1, 0). There are no nested tag selectors or '
                                                'ID selectors. The downside is that class names get very verbose, and '
                                                'it relies entirely on team discipline because CSS is still globally '
                                                'scoped. 2. CSS Modules: CSS Modules solve the global namespace '
                                                'problem automatically at build time. You write normal CSS in a file '
                                                'like Button.module.css, and your bundler hashes the class names in '
                                                'production, turning .btn into .Button_btn_8f7b2. This provides '
                                                'complete local scoping with zero risk of style leakage, while still '
                                                'letting you write familiar CSS syntax. 3. Tailwind CSS '
                                                '(Utility-First): Tailwind takes a completely different route. Instead '
                                                'of writing custom CSS, you build components by combining atomic '
                                                "utility classes directly in your markup, like 'flex p-4 bg-blue-500 "
                                                "rounded hover:bg-blue-600'. This eliminates specificity wars entirely "
                                                'because all utility classes share the exact same single-class '
                                                "specificity. Furthermore, Tailwind's JIT compiler purges unused "
                                                'classes, meaning your production CSS bundle stays tiny—often under '
                                                '10KB—no matter how large the app grows. The trade-off is messy, long '
                                                'class lists in your JSX.',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'BEM, CSS Modules, and Tailwind are different solutions to solve '
                                                'global CSS conflicts. BEM uses naming conventions like '
                                                'block__element--modifier to keep CSS specificity flat so selectors '
                                                "don't conflict, but it requires writing long class names manually. "
                                                'CSS Modules scope CSS to individual components by generating unique '
                                                'hashed class names at build time, preventing any style leaking. '
                                                'Tailwind is a utility-first framework where you style directly in '
                                                'HTML using atomic classes like flex and text-center. It solves '
                                                'specificity wars and keeps bundle sizes small, though it makes HTML '
                                                'classes long.',
                                 'missing_concepts': ['Root problem: Global CSS namespace causes accidental style '
                                                      "leaks, cascading conflicts, and escalating 'specificity wars' "
                                                      '(!important arms races) in large codebases']},
                                {'quality_level': 'average',
                                 'human_score': 60,
                                 'answer_text': 'BEM is a way of naming CSS classes with underscores and dashes like '
                                                '.card__title to keep styles organized. CSS Modules is a tool that '
                                                'renames your CSS classes into random hashes so styles in one '
                                                "component don't break styles in another component. Tailwind CSS is a "
                                                "utility framework where you don't write CSS files at all, you just "
                                                'use pre-made classes like p-4 and bg-red-500 in your HTML. Tailwind '
                                                'is very popular because it is fast to build with.',
                                 'missing_concepts': ['Root problem: Global CSS namespace causes accidental style '
                                                      "leaks, cascading conflicts, and escalating 'specificity wars' "
                                                      '(!important arms races) in large codebases',
                                                      'Tailwind CSS (Utility-First): Composes pre-defined utility '
                                                      'classes directly in markup (flex, p-4, bg-blue-500); completely '
                                                      'eliminates specificity wars (all utilities have equal class '
                                                      'specificity) and dead CSS via PurgeCSS/JIT']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': 'BEM is a CSS preprocessor written in Python. CSS Modules were '
                                                'replaced by HTML6 inline styles. Tailwind CSS is slow because it '
                                                'downloads 50 megabytes of CSS on every page load. You should always '
                                                'use !important on every line of CSS to guarantee your styles apply.',
                                 'missing_concepts': ['Root problem: Global CSS namespace causes accidental style '
                                                      "leaks, cascading conflicts, and escalating 'specificity wars' "
                                                      '(!important arms races) in large codebases',
                                                      'BEM (Block Element Modifier): Naming convention (.card, '
                                                      '.card__header, .card__header--active) that enforces flat '
                                                      'class-only specificity (0, 0, 1, 0) and structural readability, '
                                                      'but requires writing manual CSS and long class names',
                                                      'CSS Modules: Scopes CSS locally to a component by hashing class '
                                                      'names at compile time (.button_x8f2), eliminating global '
                                                      'namespace collisions while allowing standard CSS syntax',
                                                      'Tailwind CSS (Utility-First): Composes pre-defined utility '
                                                      'classes directly in markup (flex, p-4, bg-blue-500); completely '
                                                      'eliminates specificity wars (all utilities have equal class '
                                                      'specificity) and dead CSS via PurgeCSS/JIT']}]},
            {'topic_tag': 'Event Bubbling vs Event Capturing',
             'question': 'Explain Event Bubbling versus Event Capturing, and show how event delegation optimizes '
                         'memory usage.',
             'keywords': ['Event Bubbling',
                          'Event Capturing',
                          'Event Delegation',
                          'stopPropagation()',
                          'Target vs CurrentTarget',
                          'Event Listener Phase'],
             'expected_concepts': ['DOM Event Flow: Standard W3C event propagation consists of three phases: 1. '
                                   'Capturing phase (trickles down from window to target); 2. Target phase; 3. '
                                   'Bubbling phase (bubbles up from target back to window)',
                                   'Bubbling vs Capturing listener configuration: addEventListener defaults to '
                                   'bubbling (third param false); passing { capture: true } or true registers the '
                                   'listener in the capturing phase',
                                   'Stopping propagation and target differentiation: event.stopPropagation() halts '
                                   'further propagation up or down the DOM; event.target is the element that '
                                   'originated the event, while event.currentTarget is the element handling the event '
                                   'listener',
                                   'Event Delegation pattern: Attaching a single event listener to a common ancestor '
                                   'to manage events from hundreds of current or dynamically added child elements, '
                                   'drastically reducing memory usage'],
             'model_answer': 'In the DOM event model, event dispatch follows a standardized three-phase lifecycle '
                             'known as the DOM Event Flow: 1. Three Phases of Event Flow: - Phase 1: Capturing Phase '
                             '(Trickling): When an event occurs (e.g., clicking a button inside a div), the event '
                             "originates at the 'window' object and travels downwards through ancestors ('document', "
                             "'<html>', '<body>', '<div>') toward the target element. - Phase 2: Target Phase: The "
                             "event reaches the actual element that triggered the interaction ('event.target'). - "
                             'Phase 3: Bubbling Phase: The event reverses direction and travels upwards from the '
                             "target element through all parent ancestors back up to the 'window'. 2. Registering "
                             'Listeners: By default, \'element.addEventListener("click", handler)\' listens during the '
                             "Bubbling phase (equivalent to 'false' as the third argument). To listen during the "
                             "Capturing phase, you pass 'true' or '{ capture: true }'. Calling "
                             "'event.stopPropagation()' halts propagation along the chain. 3. Target vs CurrentTarget: "
                             "- 'event.target': The exact innermost DOM element that originated the event (e.g., the "
                             "<i> icon inside a button). - 'event.currentTarget': The element to which the event "
                             'handler is currently attached (e.g., the parent <ul>). 4. Event Delegation: Event '
                             'delegation leverages bubbling to optimize performance and memory. If you have an '
                             'un-ordered list with 1,000 <li> items, attaching 1,000 separate event listeners consumes '
                             'substantial memory and requires re-binding whenever new items are added dynamically. '
                             "With event delegation, you attach a single listener to the parent '<ul>'. When any <li> "
                             "is clicked, the click bubbles up to the '<ul>', which inspects "
                             '\'event.target.closest("li")\' and handles the action. This uses a single listener in '
                             'memory and automatically handles dynamic child insertions.',
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 97,
                                 'answer_text': 'DOM event propagation follows a three-phase lifecycle: 1. The '
                                                'Capturing Phase: The event starts at the window and travels down the '
                                                'DOM tree through parents to the target element. 2. The Target Phase: '
                                                'The event reaches the actual element clicked. 3. The Bubbling Phase: '
                                                'The event bubbles back up from the target element through all its '
                                                'parent ancestors to the window. By default, addEventListener listens '
                                                'during the bubbling phase. If you pass true or { capture: true } as '
                                                'the third argument, it intercepts the event during the capturing '
                                                "phase instead. Inside the event handler, 'event.target' is the "
                                                'element that actually triggered the event (like the icon inside a '
                                                "button), whereas 'event.currentTarget' is the element that owns the "
                                                "event listener. Calling 'event.stopPropagation()' stops the event "
                                                'from continuing up or down the tree. The most powerful practical '
                                                'application of bubbling is Event Delegation. Imagine an e-commerce '
                                                'table with 1,000 rows, each with a delete button. Attaching 1,000 '
                                                'individual event listeners wastes memory and requires manually '
                                                'attaching listeners every time a new row is added via AJAX. Instead, '
                                                'with event delegation, you attach ONE event listener to the parent '
                                                '<table>. Because click events bubble up from the button to the table, '
                                                'the table listener catches the event, checks '
                                                "'event.target.closest('.delete-btn')', and performs the delete. This "
                                                'drastically reduces memory footprint and handles dynamic elements '
                                                'automatically.',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'Event propagation has three phases: capturing, target, and bubbling. '
                                                'In capturing, the event travels down from the window to the target '
                                                'element. In bubbling, it travels back up from the target element to '
                                                'the window. By default, addEventListener listens during bubbling. You '
                                                'can stop it using event.stopPropagation(). Event delegation takes '
                                                'advantage of bubbling: instead of adding event listeners to hundreds '
                                                'of child elements like list items, you attach a single listener to '
                                                'the parent element. When a child is clicked, the event bubbles up to '
                                                'the parent, which checks event.target to handle the click, saving '
                                                'memory.',
                                 'missing_concepts': ['Stopping propagation and target differentiation: '
                                                      'event.stopPropagation() halts further propagation up or down '
                                                      'the DOM; event.target is the element that originated the event, '
                                                      'while event.currentTarget is the element handling the event '
                                                      'listener']},
                                {'quality_level': 'average',
                                 'human_score': 60,
                                 'answer_text': 'Event bubbling means that when you click an element, the click event '
                                                'bubbles up to its parent and all grandparent tags. Capturing is the '
                                                'opposite where it goes down from the root to the element. Event '
                                                'delegation is when you put one event listener on a parent <ul> '
                                                'instead of putting listeners on every <li>. When you click a list '
                                                'item, the event bubbles up to the parent. This makes your app faster '
                                                'and uses less memory.',
                                 'missing_concepts': ['Bubbling vs Capturing listener configuration: addEventListener '
                                                      'defaults to bubbling (third param false); passing { capture: '
                                                      'true } or true registers the listener in the capturing phase',
                                                      'Stopping propagation and target differentiation: '
                                                      'event.stopPropagation() halts further propagation up or down '
                                                      'the DOM; event.target is the element that originated the event, '
                                                      'while event.currentTarget is the element handling the event '
                                                      'listener']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': 'Event bubbling is when the browser displays bubble tooltips on button '
                                                "hover. Event capturing means recording the user's screen using "
                                                'WebRTC. Event delegation is when you delegate JavaScript execution to '
                                                'a Web Worker on the server.',
                                 'missing_concepts': ['DOM Event Flow: Standard W3C event propagation consists of '
                                                      'three phases: 1. Capturing phase (trickles down from window to '
                                                      'target); 2. Target phase; 3. Bubbling phase (bubbles up from '
                                                      'target back to window)',
                                                      'Bubbling vs Capturing listener configuration: addEventListener '
                                                      'defaults to bubbling (third param false); passing { capture: '
                                                      'true } or true registers the listener in the capturing phase',
                                                      'Stopping propagation and target differentiation: '
                                                      'event.stopPropagation() halts further propagation up or down '
                                                      'the DOM; event.target is the element that originated the event, '
                                                      'while event.currentTarget is the element handling the event '
                                                      'listener',
                                                      'Event Delegation pattern: Attaching a single event listener to '
                                                      'a common ancestor to manage events from hundreds of current or '
                                                      'dynamically added child elements, drastically reducing memory '
                                                      'usage']}]},
            {'topic_tag': 'Micro-frontend Architecture Basics',
             'question': 'What is a micro-frontend architecture, and how does Webpack Module Federation enable '
                         'independent frontend deployment?',
             'keywords': ['Micro-frontends',
                          'Module Federation',
                          'Independent Deployment',
                          'Domain Sub-apps',
                          'Shared Dependencies',
                          'Router Orchestration'],
             'expected_concepts': ['Micro-frontend architectural concept: Decomposes a large monolithic frontend SPA '
                                   'into smaller, semi-autonomous applications organized around business sub-domains '
                                   '(e.g., checkout, search, account)',
                                   'Independent lifecycle: Autonomous engineering teams can develop, test, and deploy '
                                   'their sub-applications independently without rebuilding or redeploying the entire '
                                   'host application',
                                   'Webpack 5 Module Federation mechanism: Enables a JavaScript application to '
                                   'dynamically load compiled chunks (remotes) from other independent applications '
                                   'over the network at runtime without npm package publishing',
                                   'Shared dependencies management: Module Federation configures shared libraries '
                                   '(e.g., sharing a single runtime instance of React and React-DOM) with semantic '
                                   'version negotiation (singleton: true) to avoid duplicate bundle bloat'],
             'model_answer': 'Micro-frontends extend the architectural principles of backend microservices to '
                             'client-side applications. Instead of maintaining a massive monolithic Single Page '
                             'Application (SPA) where dozens of teams commit to a single codebase with coupled release '
                             'cycles, a micro-frontend architecture decomposes the application into smaller, '
                             'domain-driven sub-applications (e.g., Header/Nav, Product Catalog, Checkout, and User '
                             'Dashboard). 1. Core Architectural Advantages: - Independent Development & Deployment: '
                             'Each sub-app lives in its own Git repository, has its own CI/CD pipeline, and can be '
                             'deployed to production multiple times a day without rebuilding the host shell. - '
                             'Autonomous Tech Stacks: Teams can theoretically choose appropriate tools, though '
                             'standardized frameworks are recommended to control bundle bloat. 2. Webpack 5 Module '
                             'Federation: Historically, sharing code between frontends required publishing npm '
                             'packages (which required host app rebuilds) or embedding <iframe> tags (which caused '
                             'terrible UX, styling isolation issues, and accessibility barriers). Webpack 5 Module '
                             'Federation revolutionized this by enabling dynamic runtime module sharing across build '
                             "boundaries: - Host vs Remote: A 'Host' application dynamically imports modules exposed "
                             "by independent 'Remote' applications over HTTP at runtime using a lightweight manifest "
                             "('remoteEntry.js'). - Shared Dependencies: Module Federation includes a 'shared' "
                             'configuration where sub-apps share common libraries—most crucially React, React-DOM, and '
                             "shared state stores. By specifying '{ react: { singleton: true, requiredVersion: "
                             '"^18.0.0" } }\', Module Federation negotiates dependencies at runtime and loads only a '
                             'single instance of React, preventing runtime errors and eliminating duplicate bundle '
                             'overhead.',
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 96,
                                 'answer_text': 'Micro-frontends apply microservice principles to frontend '
                                                'development. In large organizations, a monolithic frontend SPA '
                                                'becomes a bottleneck: hundreds of developers commit to one repo, PRs '
                                                'cause merge conflicts, CI test suites take hours, and a bug in the '
                                                'settings page can block deploying the checkout flow. A micro-frontend '
                                                'architecture breaks the application down into independent '
                                                'sub-applications organized by business domain—like a Search app, a '
                                                'Product app, and a Checkout app—orchestrated by a lightweight host '
                                                'shell. Webpack 5 Module Federation is the game-changer that makes '
                                                'this practical. Previously, teams tried using iframes—which had '
                                                'terrible performance and routing issues—or internal npm packages, '
                                                'which still required rebuilding and deploying the entire host app '
                                                'every time a dependency updated. Module Federation allows an '
                                                'application to dynamically load code from another independently '
                                                'deployed application at runtime over HTTP via a remoteEntry.js file. '
                                                'The host app imports the remote component just like a regular dynamic '
                                                "import: 'import('checkout/Cart')'. Crucially, Module Federation "
                                                'handles shared dependencies: you can configure React and React-DOM as '
                                                'singletons with semver checks. If both the host and the remote use '
                                                'React 18, the browser only downloads React once, preventing '
                                                'multi-instance runtime crashes and eliminating bundle bloat. This '
                                                'allows teams to deploy new features to production independently in '
                                                'seconds.',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'Micro-frontends split a large monolithic frontend into smaller, '
                                                'independent sub-apps owned by different teams, like separating the '
                                                'header, cart, and product catalog. Each team can develop and deploy '
                                                'their sub-app independently without redeploying the main website. '
                                                'Webpack 5 Module Federation makes this possible by allowing apps to '
                                                'import components from remote apps at runtime over the network. It '
                                                'also manages shared dependencies like React so that multiple sub-apps '
                                                'share a single instance of React in memory, avoiding duplicate '
                                                'downloads.',
                                 'missing_concepts': ['Webpack 5 Module Federation mechanism: Enables a JavaScript '
                                                      'application to dynamically load compiled chunks (remotes) from '
                                                      'other independent applications over the network at runtime '
                                                      'without npm package publishing']},
                                {'quality_level': 'average',
                                 'human_score': 60,
                                 'answer_text': 'Micro-frontends are like backend microservices for the frontend. '
                                                'Instead of one big React app, you have multiple small React apps '
                                                'running on the same page. Webpack Module Federation lets you share '
                                                'components between different apps at runtime without having to '
                                                'publish them to npm. It helps big companies have separate teams '
                                                'deploy different parts of the website independently.',
                                 'missing_concepts': ['Independent lifecycle: Autonomous engineering teams can '
                                                      'develop, test, and deploy their sub-applications independently '
                                                      'without rebuilding or redeploying the entire host application',
                                                      'Shared dependencies management: Module Federation configures '
                                                      'shared libraries (e.g., sharing a single runtime instance of '
                                                      'React and React-DOM) with semantic version negotiation '
                                                      '(singleton: true) to avoid duplicate bundle bloat']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': 'Micro-frontends are tiny React components that fit inside smartwatch '
                                                'screens. Module Federation is an open-source treaty signed by tech '
                                                'companies. It requires using iframes for all UI elements to prevent '
                                                'memory leaks.',
                                 'missing_concepts': ['Micro-frontend architectural concept: Decomposes a large '
                                                      'monolithic frontend SPA into smaller, semi-autonomous '
                                                      'applications organized around business sub-domains (e.g., '
                                                      'checkout, search, account)',
                                                      'Independent lifecycle: Autonomous engineering teams can '
                                                      'develop, test, and deploy their sub-applications independently '
                                                      'without rebuilding or redeploying the entire host application',
                                                      'Webpack 5 Module Federation mechanism: Enables a JavaScript '
                                                      'application to dynamically load compiled chunks (remotes) from '
                                                      'other independent applications over the network at runtime '
                                                      'without npm package publishing',
                                                      'Shared dependencies management: Module Federation configures '
                                                      'shared libraries (e.g., sharing a single runtime instance of '
                                                      'React and React-DOM) with semantic version negotiation '
                                                      '(singleton: true) to avoid duplicate bundle bloat']}]},
            {'topic_tag': 'Fetch API vs Axios Interceptors',
             'question': 'Compare native Fetch API with Axios regarding automatic JSON parsing, request interceptors, '
                         'and error status handling.',
             'keywords': ['Fetch API',
                          'Axios',
                          'Request/Response Interceptors',
                          'Automatic JSON Parsing',
                          'Request Cancellation',
                          'Error Status Handling'],
             'expected_concepts': ['Error handling difference: Native fetch() only rejects its Promise on network '
                                   'failure or DNS errors; it treats HTTP 4xx and 5xx responses as successful '
                                   "resolves, requiring manual 'if (!response.ok)' checks; Axios automatically rejects "
                                   'promises for status codes outside 2xx',
                                   "Data serialization/parsing: Fetch requires manual two-step stream reading ('await "
                                   "response.json()') and manual 'JSON.stringify(body)'; Axios automatically "
                                   'serializes request payloads to JSON and automatically parses response JSON into '
                                   "'response.data'",
                                   'Interceptors: Axios provides native request and response interceptors '
                                   '(axios.interceptors.request.use) to inject auth tokens and handle global errors '
                                   'centrally; native fetch requires writing custom wrapper functions',
                                   'Request cancellation: Fetch uses AbortController (signal: controller.signal); '
                                   'modern Axios supports both AbortController and legacy CancelToken'],
             'model_answer': "When making HTTP requests in modern JavaScript, developers choose between the browser's "
                             "native 'fetch()' API and the popular third-party library 'Axios', which exhibit "
                             'fundamental architectural differences: 1. HTTP Error Status Handling: - Native Fetch: A '
                             "'fetch()' Promise only rejects on actual network failures (e.g., DNS lookup failure, "
                             'complete loss of internet, CORS block). It does NOT reject on HTTP error statuses like '
                             "404 Not Found or 500 Internal Server Error. Developers must manually inspect 'if "
                             "(!response.ok)' (checking whether status is in the 200-299 range) and manually throw an "
                             'error. - Axios: Automatically treats any HTTP status code outside the 2xx range as an '
                             'error, rejecting the Promise and allowing errors to be caught directly in standard '
                             "'catch' blocks or try/catch statements with rich 'error.response' metadata. 2. Data "
                             'Parsing & Serialization: - Native Fetch: Involves a manual two-step process: you must '
                             "first await the Response object, then call 'await response.json()' to read the body "
                             "stream. For outgoing POST requests, you must manually serialize 'body: "
                             "JSON.stringify(data)' and explicitly set 'headers: { 'Content-Type': 'application/json' "
                             "}'. - Axios: Handles JSON transformation automatically. Passing a JavaScript object into "
                             "'axios.post(url, data)' automatically serializes it to JSON and sets the Content-Type "
                             "header. Incoming JSON is automatically parsed into 'response.data'. 3. Interceptors: - "
                             "Axios provides first-class Interceptors: 'axios.interceptors.request.use()' and "
                             "'axios.interceptors.response.use()'. This allows developers to centrally attach "
                             'Authorization Bearer tokens, log telemetry, or handle 401 token refresh rotations in one '
                             'place. - Native Fetch lacks native interceptors; achieving similar behavior requires '
                             'authoring custom wrapper functions or monkey-patching global fetch. 4. Request '
                             "Cancellation: Both modern Fetch and Axios utilize the standardized 'AbortController' "
                             "interface ('signal: controller.signal').",
             'sample_answers': [{'quality_level': 'excellent',
                                 'human_score': 96,
                                 'answer_text': 'While native fetch() is built into all modern browsers and requires '
                                                'zero dependencies, Axios is widely favored in production apps because '
                                                'of three huge ergonomics differences: 1. Error Status Handling: The '
                                                'biggest gotcha with native fetch is that it does NOT reject the '
                                                'promise on HTTP error codes like 404 or 500. A fetch promise only '
                                                'rejects on network failures or CORS errors. If a server returns a 500 '
                                                'error, fetch still resolves successfully, meaning you must manually '
                                                "check 'if (!response.ok) throw new Error(...)'. In contrast, Axios "
                                                'automatically rejects any response with a status code outside the 2xx '
                                                'range, so 404s and 500s land straight into your catch block. 2. '
                                                'Automatic JSON Transformation: Native fetch requires a manual '
                                                'two-step dance: you receive the response stream, and you have to call '
                                                "'await response.json()'. For POST requests, you must do 'body: "
                                                "JSON.stringify(payload)' and set the 'Content-Type: application/json' "
                                                'header manually. Axios handles all of this automatically: you pass an '
                                                'object, it serializes it to JSON, and incoming responses are already '
                                                "parsed on 'response.data'. 3. Interceptors: Axios has built-in "
                                                'request and response interceptors. You can write an interceptor to '
                                                'automatically attach a Bearer token to every outgoing request, or '
                                                'catch 401 errors globally to refresh an expired JWT and retry the '
                                                'failed request. With fetch, you have to write your own custom wrapper '
                                                'utility around the fetch API. 4. For cancellation, modern versions of '
                                                'both use AbortController with an abort signal.',
                                 'missing_concepts': []},
                                {'quality_level': 'good',
                                 'human_score': 83,
                                 'answer_text': 'Native fetch is built into the browser, while Axios is a third-party '
                                                'library. The most critical difference is error handling: fetch does '
                                                'not reject on 404 or 500 HTTP errors—you have to check response.ok '
                                                'yourself. Axios automatically rejects the promise if the status is '
                                                'outside 200-299. Axios also handles JSON automatically: it parses '
                                                'incoming data into response.data and stringifies outgoing POST data, '
                                                'whereas fetch requires calling response.json() and JSON.stringify(). '
                                                'Finally, Axios has request and response interceptors to inject auth '
                                                'tokens globally, which native fetch lacks without custom wrappers.',
                                 'missing_concepts': ['Request cancellation: Fetch uses AbortController (signal: '
                                                      'controller.signal); modern Axios supports both AbortController '
                                                      'and legacy CancelToken']},
                                {'quality_level': 'average',
                                 'human_score': 61,
                                 'answer_text': 'Fetch is built into JavaScript and Axios is an npm package you have '
                                                'to install. Fetch requires you to do res.json() to get the data, '
                                                'while Axios automatically parses the JSON into res.data. Also, if a '
                                                "server returns a 404 error, fetch doesn't throw an error, but Axios "
                                                'does throw an error so you can catch it in a try/catch block. Axios '
                                                'also has interceptors to add authorization headers to all API '
                                                'requests.',
                                 'missing_concepts': ['Data serialization/parsing: Fetch requires manual two-step '
                                                      "stream reading ('await response.json()') and manual "
                                                      "'JSON.stringify(body)'; Axios automatically serializes request "
                                                      'payloads to JSON and automatically parses response JSON into '
                                                      "'response.data'",
                                                      'Request cancellation: Fetch uses AbortController (signal: '
                                                      'controller.signal); modern Axios supports both AbortController '
                                                      'and legacy CancelToken']},
                                {'quality_level': 'poor',
                                 'human_score': 25,
                                 'answer_text': 'Fetch only works on Android devices, while Axios only works on Apple '
                                                'devices. Axios is synchronous and blocks the thread, while fetch is '
                                                'asynchronous. Interceptors are used to block pop-up ads in the '
                                                'browser.',
                                 'missing_concepts': ['Error handling difference: Native fetch() only rejects its '
                                                      'Promise on network failure or DNS errors; it treats HTTP 4xx '
                                                      "and 5xx responses as successful resolves, requiring manual 'if "
                                                      "(!response.ok)' checks; Axios automatically rejects promises "
                                                      'for status codes outside 2xx',
                                                      'Data serialization/parsing: Fetch requires manual two-step '
                                                      "stream reading ('await response.json()') and manual "
                                                      "'JSON.stringify(body)'; Axios automatically serializes request "
                                                      'payloads to JSON and automatically parses response JSON into '
                                                      "'response.data'",
                                                      'Interceptors: Axios provides native request and response '
                                                      'interceptors (axios.interceptors.request.use) to inject auth '
                                                      'tokens and handle global errors centrally; native fetch '
                                                      'requires writing custom wrapper functions',
                                                      'Request cancellation: Fetch uses AbortController (signal: '
                                                      'controller.signal); modern Axios supports both AbortController '
                                                      'and legacy CancelToken']}]}],
 'hard': [{'topic_tag': 'Browser Rendering Engine Pipeline',
           'question': 'Analyze the step-by-step browser rendering pipeline from HTML parsing to composite GPU layer '
                       'rendering.',
           'keywords': ['Browser Rendering Pipeline',
                        'DOM Tree',
                        'CSSOM',
                        'Render Tree',
                        'Layout/Reflow',
                        'Composite Layers'],
           'expected_concepts': ['Parsing & Tree Construction: HTML parser streams bytes -> characters -> tokens -> '
                                 'nodes -> DOM tree; concurrently, CSS parser builds the CSSOM (CSS Object Model)',
                                 'Render Tree construction: Combines DOM and CSSOM into the Render Tree, computing '
                                 'matching styles for every visible node while omitting invisible nodes (display: '
                                 'none, <head>, <script>)',
                                 'Layout (Reflow): Calculates the exact physical geometry, coordinates (x, y), and '
                                 'dimensions (width, height) for each render object on the viewport canvas',
                                 'Painting, Rasterization & GPU Compositing: Paint generates drawing commands; raster '
                                 'threads convert drawing commands into bitmap tiles; the Compositor thread sends '
                                 'layers (promoted via will-change, transform, opacity) to the GPU to composite on '
                                 'screen without triggering layout or paint'],
           'model_answer': 'The browser rendering engine (e.g., Blink in Chrome, Gecko in Firefox) converts raw HTML, '
                           'CSS, and JavaScript into interactive screen pixels across a rigorous multi-stage pipeline: '
                           '1. DOM and CSSOM Construction: The browser decodes raw bytes into characters, tokens, and '
                           'DOM nodes to build the Document Object Model (DOM) tree. Concurrently, CSS style sheets '
                           "are parsed into the CSS Object Model (CSSOM) tree. Because standard '<script>' tags block "
                           "the HTML parser (unless marked with 'async' or 'defer'), JavaScript execution pauses DOM "
                           'construction. 2. Render Tree Generation: The engine merges the DOM and CSSOM trees into '
                           'the Render Tree. The Render Tree contains only visible elements; non-visual elements (such '
                           "as '<head>', '<meta>', '<script>') and elements styled with 'display: none' are omitted "
                           "entirely (unlike 'visibility: hidden', which reserves layout space). 3. Layout (Reflow): "
                           'The engine traverses the Render Tree to compute the exact geometric position, bounding box '
                           'coordinates (x, y), and dimensions of every visible box relative to the viewport. '
                           'Modifying geometric properties (width, padding, margin, font-size) triggers a full '
                           'Layout/Reflow, which is computationally expensive. 4. Paint: The engine traverses the '
                           'layout tree and generates a display list—a sequence of draw operations recording '
                           'backgrounds, borders, text, and shadows in proper stacking order (z-index). 5. '
                           'Rasterization and Layer Compositing: The engine divides the page into layers (promoted via '
                           "'will-change', 3D transforms, or fixed position). Raster threads convert drawing commands "
                           'into bitmap tiles (often GPU-accelerated). Finally, the Compositor thread uploads these '
                           'layer tiles to the GPU and coordinates their final composition onto the screen. Animating '
                           "properties like 'transform' and 'opacity' bypasses Layout and Paint entirely, executing "
                           'purely on the Compositor thread at 60/120 fps.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 97,
                               'answer_text': 'The critical rendering path in modern browser engines follows five '
                                              'distinct stages: 1. DOM & CSSOM Construction: The browser parses '
                                              'incoming HTML bytes through tokenization and tree construction to build '
                                              'the DOM. In parallel, it parses CSS into the CSSOM. Standard <script> '
                                              'tags block DOM parsing unless marked async or defer, and CSS is '
                                              'render-blocking because rendering cannot begin without the CSSOM. 2. '
                                              'Render Tree Construction: The browser merges the DOM and CSSOM into the '
                                              'Render Tree. This tree only includes elements that will actually be '
                                              "painted on screen. Elements with 'display: none' and non-visual tags "
                                              "like <head> are omitted completely, whereas 'visibility: hidden' "
                                              'elements are included because they still take up spatial geometry. 3. '
                                              'Layout (or Reflow): The browser calculates the exact geometry, '
                                              'coordinates, and dimensions of every box on the viewport. Changing '
                                              'width, margin, or font sizes invalidates layout and triggers an '
                                              'expensive reflow. 4. Paint: The layout tree is converted into drawing '
                                              'instructions—filling colors, drawing borders, rendering text, and '
                                              'drawing shadows. 5. Rasterization and GPU Compositing: The page is '
                                              'divided into layers. The rasterizer turns paint instructions into pixel '
                                              'bitmaps in tile memory, often leveraging GPU rasterization. Finally, '
                                              'the Compositor thread takes these layers and draws them to the screen. '
                                              'The golden rule of web performance is animating properties like '
                                              "'transform' and 'opacity' because they can be handled entirely by the "
                                              'GPU compositor thread without triggering layout or paint passes.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'The browser rendering pipeline starts by parsing HTML into the DOM tree '
                                              'and parsing CSS into the CSSOM tree. Next, it combines them into the '
                                              'Render Tree, which leaves out hidden elements like display: none. Then '
                                              'it performs Layout, which calculates the exact physical coordinates and '
                                              'dimensions of every element on screen. After layout, the browser Paints '
                                              'the elements by drawing text, colors, and borders. Finally, during '
                                              'Compositing, the browser splits elements into layers and sends them to '
                                              'the GPU to be drawn to the display. Animating transform and opacity is '
                                              'fastest because it skips layout and paint.',
                               'missing_concepts': ['Painting, Rasterization & GPU Compositing: Paint generates '
                                                    'drawing commands; raster threads convert drawing commands into '
                                                    'bitmap tiles; the Compositor thread sends layers (promoted via '
                                                    'will-change, transform, opacity) to the GPU to composite on '
                                                    'screen without triggering layout or paint']},
                              {'quality_level': 'average',
                               'human_score': 61,
                               'answer_text': 'The browser takes HTML and builds the DOM tree, and takes CSS to build '
                                              'the CSSOM. Then it combines them into a render tree. After that, it '
                                              'does layout which figures out where elements go on the page, and then '
                                              'it paints the colors and fonts. Finally, the GPU composites the layers '
                                              'onto the screen. If you change a layout property like width, the '
                                              'browser has to reflow the whole page which makes it laggy.',
                               'missing_concepts': ['Parsing & Tree Construction: HTML parser streams bytes -> '
                                                    'characters -> tokens -> nodes -> DOM tree; concurrently, CSS '
                                                    'parser builds the CSSOM (CSS Object Model)',
                                                    'Painting, Rasterization & GPU Compositing: Paint generates '
                                                    'drawing commands; raster threads convert drawing commands into '
                                                    'bitmap tiles; the Compositor thread sends layers (promoted via '
                                                    'will-change, transform, opacity) to the GPU to composite on '
                                                    'screen without triggering layout or paint']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'The browser rendering engine runs WebGL shaders to compile HTML into '
                                              'C++ machine code. Layout and Paint happen simultaneously on the CPU '
                                              'cache. The render tree includes all HTML comments and hidden CSS rules '
                                              'so the user can inspect them.',
                               'missing_concepts': ['Parsing & Tree Construction: HTML parser streams bytes -> '
                                                    'characters -> tokens -> nodes -> DOM tree; concurrently, CSS '
                                                    'parser builds the CSSOM (CSS Object Model)',
                                                    'Render Tree construction: Combines DOM and CSSOM into the Render '
                                                    'Tree, computing matching styles for every visible node while '
                                                    'omitting invisible nodes (display: none, <head>, <script>)',
                                                    'Layout (Reflow): Calculates the exact physical geometry, '
                                                    'coordinates (x, y), and dimensions (width, height) for each '
                                                    'render object on the viewport canvas',
                                                    'Painting, Rasterization & GPU Compositing: Paint generates '
                                                    'drawing commands; raster threads convert drawing commands into '
                                                    'bitmap tiles; the Compositor thread sends layers (promoted via '
                                                    'will-change, transform, opacity) to the GPU to composite on '
                                                    'screen without triggering layout or paint']}]},
          {'topic_tag': 'React 18 Concurrent Rendering',
           'question': 'Explain how React 18 Concurrent Rendering features like Suspense, useTransition, and Server '
                       'Components change UI rendering priority.',
           'keywords': ['Concurrent React',
                        'Suspense',
                        'useTransition',
                        'useDeferredValue',
                        'Server Components',
                        'Non-blocking Rendering'],
           'expected_concepts': ['Concurrent rendering paradigm: Rendering becomes interruptible and non-blocking; '
                                 'React can pause long render passes, yield to high-priority browser input (typing, '
                                 'clicking), and resume or discard work in progress',
                                 'Urgent vs Transition updates: useTransition separates urgent updates (e.g., '
                                 'immediate input text reflection) from non-urgent transitions (e.g., filtering a list '
                                 'of 10,000 items), keeping the UI responsive without jank',
                                 'useDeferredValue hook: Defers re-rendering of expensive child subtrees until urgent '
                                 'updates complete, acting like a concurrent debounce tied directly to device CPU '
                                 'capacity',
                                 'Suspense & React Server Components (RSC): Suspense coordinates asynchronous '
                                 'data/code streaming without cascading spinners; RSC renders components exclusively '
                                 'on the server, streaming a lightweight virtual DOM wire-format with zero client '
                                 'bundle footprint'],
           'model_answer': 'In React 18, Concurrent Rendering marks a fundamental architectural shift from '
                           'synchronous, blocking rendering to cooperative, interruptible rendering: 1. Core '
                           'Concurrency Mechanism: Previously, once React began reconciling a component tree, it '
                           'monopolized the JavaScript main thread until complete. A complex tree update would drop '
                           'frames, causing text inputs to lag. In Concurrent React, rendering is interruptible. React '
                           'builds a work-in-progress Fiber tree in memory; if a high-priority event arrives '
                           '(keystroke, click), React pauses the render pass, yields the main thread to the browser to '
                           'handle the event, and resumes or abandons the background work. 2. useTransition: React '
                           'introduces a formal distinction between Urgent and Transition updates: - Urgent updates '
                           '(typing in an input, clicking a toggle) require immediate visual feedback. - Transitions '
                           '(filtering search results, switching tabs) represent secondary UI transitions. By wrapping '
                           "state setters in 'startTransition(() => setSearchQuery(e.target.value))', developers "
                           'instruct React that the update is non-blocking. The input field updates instantly at '
                           "60fps, while the expensive search results render in the background. An 'isPending' boolean "
                           'provides loading indicators without unmounting the existing UI. 3. useDeferredValue: '
                           "Defers recalculating derived values: 'const deferredQuery = useDeferredValue(query)'. If "
                           'new urgent updates arrive while the deferred subtree is rendering, React interrupts the '
                           'deferred render and prioritizes the new input. 4. Suspense and Server Components (RSC): - '
                           'Suspense lets components declare async data dependencies, streaming HTML from the server '
                           'and hydrating components incrementally. - React Server Components execute exclusively on '
                           'the server, streaming serialized JSON UI trees to the client with zero bundle impact, '
                           'eliminating client-side data waterfall requests.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'Prior to React 18, rendering was strictly synchronous and '
                                              'uninterruptible—once React started rendering a component tree, it '
                                              'locked the main thread until it was completely finished. If you had a '
                                              'large list or chart, typing in an input felt sluggish because the '
                                              "browser couldn't process keypresses until React finished. React 18 "
                                              'Concurrent Rendering changes this by making rendering interruptible and '
                                              'prioritizing updates. React can prepare a new screen in memory behind '
                                              'the scenes, yield execution to let the browser handle urgent user '
                                              'interactions, and then resume rendering. 1. useTransition introduces an '
                                              'explicit priority split: Urgent updates (like typing in a text field) '
                                              'execute immediately. Non-urgent updates (like filtering 5,000 items in '
                                              "a list) are wrapped in 'startTransition(() => setFilter(val))'. React "
                                              'treats the filter update as low priority—it renders the list in the '
                                              'background, but if the user types another letter, React interrupts the '
                                              'transition and processes the new keystroke first. The hook also returns '
                                              "'isPending' to show an inline loading state. 2. useDeferredValue works "
                                              'similarly for props or state: it lets you defer re-rendering an '
                                              'expensive child component until urgent renders finish. 3. Suspense and '
                                              'React Server Components (RSC): Suspense allows components to wait for '
                                              'async data without freezing the page or causing cascading layout '
                                              'shifts. Server Components take this to the next level by executing '
                                              "exclusively on the server. They have direct database access, don't ship "
                                              'any JavaScript to the client bundle, and stream their rendered UI into '
                                              'the Suspense tree progressively.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'React 18 Concurrent Rendering makes rendering interruptible rather than '
                                              'blocking. In previous versions, rendering a large component tree would '
                                              'freeze user input. With useTransition, you can separate urgent updates '
                                              'from non-urgent transitions: typing in an input is urgent, while '
                                              'updating search results can be wrapped in startTransition so it renders '
                                              'in the background without blocking the input. useDeferredValue allows '
                                              'you to defer expensive calculations. Suspense handles loading states '
                                              'for asynchronous data, and React Server Components run on the server to '
                                              'reduce bundle sizes.',
                               'missing_concepts': ['Suspense & React Server Components (RSC): Suspense coordinates '
                                                    'asynchronous data/code streaming without cascading spinners; RSC '
                                                    'renders components exclusively on the server, streaming a '
                                                    'lightweight virtual DOM wire-format with zero client bundle '
                                                    'footprint']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'React 18 concurrent mode makes React faster by rendering in the '
                                              'background. It adds the useTransition hook which lets you mark some '
                                              "state updates as low priority so the user's typing doesn't lag. "
                                              'useDeferredValue is used to debounce values. Server Components run on '
                                              "the server and don't add to the client bundle size, which makes the "
                                              'initial page load faster. Suspense is used to show spinners while '
                                              'components load.',
                               'missing_concepts': ['Concurrent rendering paradigm: Rendering becomes interruptible '
                                                    'and non-blocking; React can pause long render passes, yield to '
                                                    'high-priority browser input (typing, clicking), and resume or '
                                                    'discard work in progress',
                                                    'useDeferredValue hook: Defers re-rendering of expensive child '
                                                    'subtrees until urgent updates complete, acting like a concurrent '
                                                    'debounce tied directly to device CPU capacity']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'Concurrent rendering means React runs on multiple threads in the '
                                              'browser using WebAssembly. useTransition is a CSS animation hook like '
                                              'transition: all 0.3s. Server Components are deprecated and were '
                                              'replaced by Redux.',
                               'missing_concepts': ['Concurrent rendering paradigm: Rendering becomes interruptible '
                                                    'and non-blocking; React can pause long render passes, yield to '
                                                    'high-priority browser input (typing, clicking), and resume or '
                                                    'discard work in progress',
                                                    'Urgent vs Transition updates: useTransition separates urgent '
                                                    'updates (e.g., immediate input text reflection) from non-urgent '
                                                    'transitions (e.g., filtering a list of 10,000 items), keeping the '
                                                    'UI responsive without jank',
                                                    'useDeferredValue hook: Defers re-rendering of expensive child '
                                                    'subtrees until urgent updates complete, acting like a concurrent '
                                                    'debounce tied directly to device CPU capacity',
                                                    'Suspense & React Server Components (RSC): Suspense coordinates '
                                                    'asynchronous data/code streaming without cascading spinners; RSC '
                                                    'renders components exclusively on the server, streaming a '
                                                    'lightweight virtual DOM wire-format with zero client bundle '
                                                    'footprint']}]},
          {'topic_tag': 'SharedArrayBuffer & Atomics in JS',
           'question': 'How do SharedArrayBuffer and the Atomics API facilitate multithreaded shared memory operations '
                       'in JavaScript without race conditions?',
           'keywords': ['SharedArrayBuffer',
                        'Atomics API',
                        'Shared Memory',
                        'Thread Synchronization',
                        'Race Conditions',
                        'Locking Mechanics'],
           'expected_concepts': ['SharedArrayBuffer memory model: Unlike standard postMessage structured cloning '
                                 '(which copies data), SharedArrayBuffer allocates a shared raw memory buffer '
                                 'accessible concurrently by main thread and Web Workers',
                                 'Race conditions & torn reads/writes: Concurrent unsynchronized read/write operations '
                                 'across threads produce non-deterministic data corruption and torn memory states',
                                 'Atomics primitive operations: Atomics methods (Atomics.load, Atomics.store, '
                                 'Atomics.add, Atomics.compareExchange) execute indivisible hardware-level '
                                 'read-modify-write operations that cannot be interrupted',
                                 'Thread synchronization & sleep/wake: Atomics.wait() and Atomics.notify() provide '
                                 'low-level blocking synchronization (wait sleeps a worker thread until a condition '
                                 'changes or timeout occurs, notify wakes sleeping threads), allowing construction of '
                                 'mutexes and semaphores'],
           'model_answer': 'Standard JavaScript Web Workers operate with isolated memory spaces; passing data via '
                           "'postMessage()' utilizes the Structured Clone Algorithm, which copies entire memory "
                           'buffers (or transfers ownership via Transferable Objects). When multiple threads must '
                           'collaborate on large shared datasets (such as 3D WebGL physics, audio DSP pipelines, or '
                           'game engines), copying creates prohibitive overhead. JavaScript resolves this via '
                           "'SharedArrayBuffer' and the 'Atomics' API: 1. SharedArrayBuffer: A SharedArrayBuffer is a "
                           'contiguous block of raw binary memory that can be referenced simultaneously by the main '
                           'thread and multiple Web Workers. Threads read and write directly to the same underlying '
                           'physical RAM address without data duplication. 2. The Concurrency Hazard (Race '
                           'Conditions): Because threads execute asynchronously on multi-core processors, '
                           "unsynchronized access leads to data races and 'torn writes' (where one thread overwrites "
                           'half an integer while another thread is reading it), corrupting application state. 3. The '
                           "Atomics API: The global 'Atomics' object provides primitive operations that are guaranteed "
                           'by underlying CPU architecture (lock-free assembly instructions) to be indivisible and '
                           "atomic: - Atomic Memory Operations: 'Atomics.load(typedArray, index)' and "
                           "'Atomics.store(typedArray, index, value)' enforce sequential consistency. - Atomic "
                           "Read-Modify-Write: 'Atomics.add()', 'Atomics.sub()', 'Atomics.and()', and "
                           "'Atomics.compareExchange()' (which sets a new value only if the current value matches an "
                           'expected value, foundational for lock-free data structures). 4. Thread Synchronization '
                           "(Wait and Notify): 'Atomics.wait(int32Array, index, expectedValue, timeout)' puts a "
                           "background worker thread to sleep if 'array[index] === expectedValue'. "
                           "'Atomics.notify(int32Array, index, count)' wakes up sleeping worker threads. Note: "
                           'Atomics.wait is prohibited on the main browser thread to prevent UI deadlocks.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'Normally in JavaScript, when you send data to a Web Worker via '
                                              'postMessage, the browser uses the structured clone algorithm to create '
                                              "a full deep copy of the data in the worker's separate memory space. For "
                                              'high-performance applications like game engines, 3D physics, or '
                                              'WebAudio DSP, copying multi-megabyte buffers back and forth creates '
                                              'massive garbage collection and latency bottlenecks. SharedArrayBuffer '
                                              'solves this by allocating a single shared memory block in RAM that both '
                                              'the main thread and multiple Web Workers can read and write to '
                                              'concurrently without copying. But shared memory immediately introduces '
                                              'race conditions and torn reads/writes: if Thread A and Thread B both do '
                                              "'sharedArray[0]++', they might read the same value simultaneously, "
                                              'resulting in lost updates. The Atomics API solves this by providing '
                                              'hardware-level atomic operations that cannot be interrupted midway. For '
                                              'example: 1. Atomics.add() or Atomics.sub() performs an atomic '
                                              'read-modify-write in a single CPU instruction. 2. '
                                              'Atomics.compareExchange() checks if the memory cell matches an expected '
                                              'value before swapping it, which is the foundational building block for '
                                              'lock-free concurrency. 3. Atomics.wait() and Atomics.notify() provide '
                                              'true thread synchronization: a worker can call Atomics.wait() to put '
                                              'its thread to sleep until a specific memory cell changes, and another '
                                              'thread calls Atomics.notify() to wake it up. This allows developers to '
                                              'build mutual exclusion locks (mutexes) and semaphores in JavaScript. '
                                              'Note that Atomics.wait() cannot be called on the main thread to prevent '
                                              'locking up the browser UI.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'SharedArrayBuffer allows the main JavaScript thread and Web Workers to '
                                              'share the same block of memory directly, avoiding the need to copy data '
                                              'using postMessage. However, multiple threads writing to the same memory '
                                              'can cause race conditions where data gets corrupted. The Atomics API '
                                              'provides methods like Atomics.add, Atomics.load, and '
                                              'Atomics.compareExchange that perform atomic operations guaranteed to '
                                              'execute without interruption. It also provides Atomics.wait and '
                                              'Atomics.notify, which allow worker threads to sleep and wake up when '
                                              'signaled, letting you build locks and semaphores without freezing the '
                                              'main thread.',
                               'missing_concepts': ['Race conditions & torn reads/writes: Concurrent unsynchronized '
                                                    'read/write operations across threads produce non-deterministic '
                                                    'data corruption and torn memory states']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'SharedArrayBuffer is shared memory between Web Workers and the main '
                                              "thread so you don't have to copy data back and forth. The problem is "
                                              'race conditions where two threads try to write to the same number at '
                                              'the same time. The Atomics API fixes this by making operations atomic, '
                                              'meaning only one thread can modify the memory at a time. It has methods '
                                              'like Atomics.add and Atomics.wait to synchronize threads.',
                               'missing_concepts': ['Race conditions & torn reads/writes: Concurrent unsynchronized '
                                                    'read/write operations across threads produce non-deterministic '
                                                    'data corruption and torn memory states',
                                                    'Thread synchronization & sleep/wake: Atomics.wait() and '
                                                    'Atomics.notify() provide low-level blocking synchronization (wait '
                                                    'sleeps a worker thread until a condition changes or timeout '
                                                    'occurs, notify wakes sleeping threads), allowing construction of '
                                                    'mutexes and semaphores']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'SharedArrayBuffer is a cloud storage service provided by AWS for '
                                              'sharing arrays between different websites. Atomics API is a nuclear '
                                              'simulation library written in JavaScript. Race conditions happen when '
                                              'the internet speed is faster than the GPU.',
                               'missing_concepts': ['SharedArrayBuffer memory model: Unlike standard postMessage '
                                                    'structured cloning (which copies data), SharedArrayBuffer '
                                                    'allocates a shared raw memory buffer accessible concurrently by '
                                                    'main thread and Web Workers',
                                                    'Race conditions & torn reads/writes: Concurrent unsynchronized '
                                                    'read/write operations across threads produce non-deterministic '
                                                    'data corruption and torn memory states',
                                                    'Atomics primitive operations: Atomics methods (Atomics.load, '
                                                    'Atomics.store, Atomics.add, Atomics.compareExchange) execute '
                                                    'indivisible hardware-level read-modify-write operations that '
                                                    'cannot be interrupted',
                                                    'Thread synchronization & sleep/wake: Atomics.wait() and '
                                                    'Atomics.notify() provide low-level blocking synchronization (wait '
                                                    'sleeps a worker thread until a condition changes or timeout '
                                                    'occurs, notify wakes sleeping threads), allowing construction of '
                                                    'mutexes and semaphores']}]},
          {'topic_tag': 'HTTP/2 Multiplexing & HTTP/3 QUIC',
           'question': 'Contrast HTTP/2 multiplexing over TCP with HTTP/3 QUIC transport over UDP regarding '
                       'Head-of-Line blocking.',
           'keywords': ['HTTP/2', 'HTTP/3', 'Multiplexing', 'Head-of-Line Blocking', 'QUIC Protocol', 'UDP Transport'],
           'expected_concepts': ['HTTP/1.1 vs HTTP/2 multiplexing: HTTP/1.1 suffered from application-layer '
                                 'Head-of-Line (HoL) blocking (one request per TCP connection at a time); HTTP/2 '
                                 'introduced binary framing to multiplex multiple independent request/response streams '
                                 'over a single TCP connection',
                                 'TCP-level Head-of-Line blocking in HTTP/2: Because TCP guarantees strict in-order '
                                 'packet delivery, dropping a single TCP packet halts processing of ALL multiplexed '
                                 'HTTP/2 streams on that connection until the lost packet is retransmitted',
                                 'HTTP/3 QUIC architecture over UDP: HTTP/3 abandons TCP in favor of QUIC running over '
                                 'UDP, moving reliable stream multiplexing and encryption (TLS 1.3) into the transport '
                                 'layer',
                                 'Zero HoL blocking and Connection Migration: In QUIC, a dropped packet on Stream A '
                                 'delays only Stream A; Streams B, C, and D continue unhindered; QUIC Connection IDs '
                                 'enable seamless roaming across Wi-Fi and mobile networks without connection drops'],
           'model_answer': 'The evolution from HTTP/1.1 to HTTP/2 and HTTP/3 represents a progressive battle against '
                           'Head-of-Line (HoL) blocking: 1. HTTP/1.1: Suffered from Application-Layer HoL blocking: an '
                           'HTTP connection can only process one request-response cycle at a time. If request 1 is '
                           'slow, all subsequent requests in that socket must wait. Browsers mitigated this by opening '
                           'up to 6 parallel TCP connections per domain, creating high connection overhead. 2. HTTP/2 '
                           'over TCP: Introduced the Binary Framing Layer, which splits messages into frames and '
                           'multiplexes multiple independent request/response streams across a single persistent TCP '
                           'connection. This eliminated application-layer HoL blocking. However, it introduced a '
                           'severe lower-level flaw: TCP-Layer Head-of-Line Blocking. Because TCP enforces strict, '
                           'sequential byte-stream delivery at the OS transport layer, if a single IP packet belonging '
                           'to Stream 1 is lost or corrupted over a lossy network (e.g., mobile 4G/5G), the operating '
                           "system's TCP stack halts delivery of all subsequent packets—freezing all concurrent "
                           'streams (Streams 2, 3, 4) until the lost packet is retransmitted and acknowledged. On '
                           'networks with 2% packet loss, HTTP/2 can perform worse than HTTP/1.1. 3. HTTP/3 over QUIC '
                           '(UDP): HTTP/3 eliminates TCP completely, running over the QUIC transport protocol built on '
                           'top of UDP. QUIC integrates TLS 1.3 encryption and stream multiplexing directly into the '
                           'transport layer: - Zero Transport HoL Blocking: In QUIC, streams are independent transport '
                           'entities. If a packet on Stream A is dropped, only Stream A is paused for retransmission; '
                           'Streams B and C continue uninterrupted. - 0-RTT Connection Establishment: Combines the '
                           'transport handshake and TLS 1.3 cryptographic handshake, allowing repeat connections to '
                           'send encrypted data on the very first network flight. - Connection Migration: QUIC uses '
                           '64-bit Connection IDs rather than (IP, Port) 4-tuples, allowing users switching from Wi-Fi '
                           'to cellular data to maintain active video streams and downloads without reconnecting.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 97,
                               'answer_text': 'The transition from HTTP/1.1 to HTTP/2 and HTTP/3 is all about solving '
                                              'Head-of-Line (HoL) blocking at different layers of the networking '
                                              'stack: In HTTP/1.1, HoL blocking was at the application layer. A single '
                                              'TCP connection could only process one HTTP request at a time—if the '
                                              'first request stalled, every request behind it was blocked, forcing '
                                              'browsers to open 6 separate TCP connections per domain. HTTP/2 solved '
                                              'this by introducing binary framing and multiplexing: multiple '
                                              'independent request and response streams could now travel '
                                              'simultaneously over a single shared TCP connection. This eliminated '
                                              'application-level HoL blocking. However, HTTP/2 created a new '
                                              'bottleneck: TCP-layer Head-of-Line blocking. Because TCP is '
                                              'fundamentally a reliable, in-order byte stream protocol, the operating '
                                              'system kernel will not release subsequent packets to the application if '
                                              'a preceding packet is missing. If even a single packet from Stream 1 is '
                                              'dropped on a lossy cellular network, ALL other multiplexed streams '
                                              '(Stream 2, 3, 4) on that TCP connection freeze completely until that '
                                              'lost packet is retransmitted. On lossy Wi-Fi or mobile connections, '
                                              'HTTP/2 is often slower than HTTP/1.1. HTTP/3 completely solves this by '
                                              'abandoning TCP and running over QUIC on top of UDP. QUIC brings stream '
                                              'multiplexing and TLS 1.3 encryption directly into the transport layer. '
                                              'In QUIC, each stream is handled independently: if a packet on Stream A '
                                              'is lost, only Stream A is delayed, while Streams B and C continue '
                                              'streaming smoothly with zero HoL blocking. Furthermore, QUIC supports '
                                              '0-RTT handshakes and Connection IDs, meaning when a mobile user walks '
                                              'out of their house and switches from Wi-Fi to cellular, their downloads '
                                              'and video calls continue without dropping.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'HTTP/2 uses multiplexing over a single TCP connection, allowing '
                                              'multiple requests and responses to be sent simultaneously in binary '
                                              "frames, solving HTTP/1.1's application-level head-of-line blocking. But "
                                              'because TCP requires all packets to be received in order, if one packet '
                                              'is dropped on the network, all multiplexed streams are blocked until '
                                              'that packet is retransmitted. This is TCP head-of-line blocking. HTTP/3 '
                                              'solves this by replacing TCP with QUIC over UDP. In QUIC, streams are '
                                              'truly independent, so a lost packet on one stream does not block any of '
                                              'the other streams. QUIC also integrates TLS 1.3 for faster connection '
                                              'setup and supports connection migration.',
                               'missing_concepts': ['Zero HoL blocking and Connection Migration: In QUIC, a dropped '
                                                    'packet on Stream A delays only Stream A; Streams B, C, and D '
                                                    'continue unhindered; QUIC Connection IDs enable seamless roaming '
                                                    'across Wi-Fi and mobile networks without connection drops']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'HTTP/2 introduced multiplexing which lets you send multiple files over '
                                              'one TCP connection instead of opening 6 connections like in HTTP/1.1. '
                                              'But if one packet gets lost in TCP, everything stops which is '
                                              'head-of-line blocking. HTTP/3 fixes this by using QUIC which runs on '
                                              "UDP instead of TCP. Because UDP doesn't enforce ordering between "
                                              "streams, lost packets on one file don't slow down the other files. It "
                                              'also has faster connection handshakes.',
                               'missing_concepts': ['HTTP/1.1 vs HTTP/2 multiplexing: HTTP/1.1 suffered from '
                                                    'application-layer Head-of-Line (HoL) blocking (one request per '
                                                    'TCP connection at a time); HTTP/2 introduced binary framing to '
                                                    'multiplex multiple independent request/response streams over a '
                                                    'single TCP connection',
                                                    'Zero HoL blocking and Connection Migration: In QUIC, a dropped '
                                                    'packet on Stream A delays only Stream A; Streams B, C, and D '
                                                    'continue unhindered; QUIC Connection IDs enable seamless roaming '
                                                    'across Wi-Fi and mobile networks without connection drops']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'HTTP/2 is an unencrypted protocol, while HTTP/3 is encrypted. QUIC is a '
                                              'compression algorithm like GZIP that makes images smaller. Head-of-line '
                                              'blocking means that the head tag of the HTML must load before the body '
                                              'tag.',
                               'missing_concepts': ['HTTP/1.1 vs HTTP/2 multiplexing: HTTP/1.1 suffered from '
                                                    'application-layer Head-of-Line (HoL) blocking (one request per '
                                                    'TCP connection at a time); HTTP/2 introduced binary framing to '
                                                    'multiplex multiple independent request/response streams over a '
                                                    'single TCP connection',
                                                    'TCP-level Head-of-Line blocking in HTTP/2: Because TCP guarantees '
                                                    'strict in-order packet delivery, dropping a single TCP packet '
                                                    'halts processing of ALL multiplexed HTTP/2 streams on that '
                                                    'connection until the lost packet is retransmitted',
                                                    'HTTP/3 QUIC architecture over UDP: HTTP/3 abandons TCP in favor '
                                                    'of QUIC running over UDP, moving reliable stream multiplexing and '
                                                    'encryption (TLS 1.3) into the transport layer',
                                                    'Zero HoL blocking and Connection Migration: In QUIC, a dropped '
                                                    'packet on Stream A delays only Stream A; Streams B, C, and D '
                                                    'continue unhindered; QUIC Connection IDs enable seamless roaming '
                                                    'across Wi-Fi and mobile networks without connection drops']}]},
          {'topic_tag': 'WebRTC Peer-to-Peer Architecture',
           'question': 'Detail the WebRTC peer-to-peer signaling sequence, including STUN/TURN servers, SDP exchange, '
                       'and ICE candidates.',
           'keywords': ['WebRTC',
                        'P2P Connection',
                        'STUN/TURN Servers',
                        'ICE Candidates',
                        'SDP Offer/Answer',
                        'DataChannel'],
           'expected_concepts': ['Signaling mechanism: WebRTC requires an out-of-band signaling mechanism (WebSockets, '
                                 'SIP) to coordinate connection setup before direct peer-to-peer media transmission '
                                 'begins',
                                 'SDP (Session Description Protocol) Offer/Answer: Peers exchange media capabilities, '
                                 'codecs, resolutions, and encryption keys via an SDP Offer and SDP Answer',
                                 'NAT traversal via STUN: STUN (Session Traversal Utilities for NAT) servers discover '
                                 "a peer's public reflexive IP and port to bypass symmetric/cone NATs",
                                 'ICE candidates & TURN fallback: ICE (Interactive Connectivity Establishment) '
                                 'collects candidate network paths (host, srflx, relay); if direct P2P fails due to '
                                 'strict firewalls/symmetric NAT, traffic falls back to a TURN (Traversal Using Relays '
                                 'around NAT) relay server'],
           'model_answer': 'WebRTC (Web Real-Time Communication) provides real-time, encrypted, low-latency audio, '
                           'video, and data streaming directly between browser peers. Because user devices reside '
                           'behind NATs, firewalls, and dynamic IP routers, establishing a direct peer-to-peer '
                           'connection requires an orchestrated signaling and connection sequence: 1. Out-of-Band '
                           'Signaling: WebRTC does NOT define a signaling protocol. Peers use an external '
                           'communication channel (typically WebSockets or HTTP) to exchange connection metadata. 2. '
                           "SDP Offer/Answer Exchange: - Peer A creates an SDP (Session Description Protocol) 'Offer' "
                           'containing media capabilities (audio/video codecs, resolutions, DTLS cryptographic '
                           "fingerprints). Peer A sets this as its 'localDescription' and transmits it to Peer B via "
                           "the signaling server. - Peer B receives the offer, sets it as its 'remoteDescription', "
                           "generates an SDP 'Answer', sets it as its 'localDescription', and sends it back to Peer A "
                           "via the signaling server. Peer A sets it as its 'remoteDescription'. 3. ICE Candidates and "
                           'NAT Traversal: In parallel with SDP exchange, the ICE (Interactive Connectivity '
                           'Establishment) framework gathers candidate network paths: - Host candidates: Direct local '
                           'IP addresses on the LAN. - Server Reflexive (srflx) candidates: Obtained by contacting a '
                           'STUN (Session Traversal Utilities for NAT) server. The STUN server reflects back the '
                           "peer's public IP address and port mapping through the NAT router. 4. TURN Relay Fallback: "
                           'If both peers reside behind strict, symmetric NATs or corporate enterprise firewalls that '
                           'prohibit direct peer-to-peer UDP packet traversal, ICE falls back to a TURN (Traversal '
                           'Using Relays around NAT) server. The TURN server acts as an encrypted media relay, '
                           'streaming packets between peers at the expense of server bandwidth. 5. Secure Channel '
                           'Established: Once ICE finds the optimal viable candidate pair, peers establish an '
                           'encrypted DTLS-SRTP connection for media and SCTP for RTCDataChannel.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'Establishing a WebRTC peer-to-peer connection requires solving two '
                                              'problems: negotiating media codecs and traversing NAT firewalls. Here '
                                              'is the exact step-by-step sequence: 1. Signaling: WebRTC does not '
                                              'specify how peers find each other, so you use an out-of-band signaling '
                                              'channel, typically a WebSocket server. 2. SDP Offer and Answer: Peer A '
                                              "calls 'createOffer()' to generate an SDP (Session Description Protocol) "
                                              'string that lists its supported codecs (e.g., VP8/Opus), encryption '
                                              'keys, and media streams. Peer A sets this as its localDescription and '
                                              'sends it via WebSocket to Peer B. Peer B sets it as its '
                                              "remoteDescription, calls 'createAnswer()', sets its localDescription, "
                                              'and sends the answer back. Peer A sets it as its remoteDescription. 3. '
                                              'NAT Traversal with STUN: Most users are behind home NAT routers with '
                                              'private IPs (192.168.x.x). To find their public-facing IP and port, '
                                              'each peer contacts a STUN server. The STUN server inspects the incoming '
                                              'packet and tells the browser its public IP:port mapping '
                                              '(server-reflexive candidate). 4. ICE Candidates: As network paths are '
                                              'discovered (host LAN, STUN public reflexive, or relay), the browser '
                                              "fires 'onicecandidate' events. The peers exchange these ICE candidates "
                                              "across the signaling channel and add them via 'addIceCandidate()'. 5. "
                                              'TURN Relay Fallback: If both peers are behind strict symmetric NATs or '
                                              'enterprise firewalls where direct P2P UDP packet traversal is blocked, '
                                              'the ICE framework automatically falls back to a TURN server. The TURN '
                                              'server acts as a relay, routing all encrypted audio/video traffic '
                                              'through its public server. Once candidate pairs connect, the peers '
                                              'establish DTLS-SRTP encryption for audio/video and SCTP for the '
                                              'DataChannel.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'WebRTC establishes peer-to-peer connections using signaling, SDP, and '
                                              'ICE. First, peers use an external signaling server like WebSockets to '
                                              'exchange an SDP Offer and SDP Answer describing codecs and media '
                                              'capabilities. Next, because peers are behind NAT routers, they use STUN '
                                              'servers to discover their public IP and port addresses, which are '
                                              'exchanged as ICE candidates. If direct peer-to-peer connection fails '
                                              'due to symmetric NAT or firewalls, traffic falls back to a TURN relay '
                                              'server that proxies the video stream. Once connected, media flows '
                                              'directly peer-to-peer over encrypted UDP.',
                               'missing_concepts': ['Signaling mechanism: WebRTC requires an out-of-band signaling '
                                                    'mechanism (WebSockets, SIP) to coordinate connection setup before '
                                                    'direct peer-to-peer media transmission begins']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'WebRTC is used for video calls in the browser like Google Meet. It uses '
                                              'a signaling server to connect two users. The two browsers exchange SDP '
                                              'offers and answers to agree on video resolution and audio codecs. STUN '
                                              "servers are used to find the user's public IP address through their "
                                              "home router. If STUN doesn't work because of a firewall, it uses a TURN "
                                              'server to relay the video call. Once connected, it streams video '
                                              'directly between users.',
                               'missing_concepts': ['ICE candidates & TURN fallback: ICE (Interactive Connectivity '
                                                    'Establishment) collects candidate network paths (host, srflx, '
                                                    'relay); if direct P2P fails due to strict firewalls/symmetric '
                                                    'NAT, traffic falls back to a TURN (Traversal Using Relays around '
                                                    'NAT) relay server',
                                                    'Signaling mechanism: WebRTC requires an out-of-band signaling '
                                                    'mechanism (WebSockets, SIP) to coordinate connection setup before '
                                                    'direct peer-to-peer media transmission begins']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'WebRTC is a plugin installed in Chrome to download torrent files. STUN '
                                              'servers stun the firewall by sending high-voltage electrical signals '
                                              'over the ethernet cable. SDP is a database where user passwords are '
                                              'encrypted.',
                               'missing_concepts': ['Signaling mechanism: WebRTC requires an out-of-band signaling '
                                                    'mechanism (WebSockets, SIP) to coordinate connection setup before '
                                                    'direct peer-to-peer media transmission begins',
                                                    'SDP (Session Description Protocol) Offer/Answer: Peers exchange '
                                                    'media capabilities, codecs, resolutions, and encryption keys via '
                                                    'an SDP Offer and SDP Answer',
                                                    'NAT traversal via STUN: STUN (Session Traversal Utilities for '
                                                    "NAT) servers discover a peer's public reflexive IP and port to "
                                                    'bypass symmetric/cone NATs',
                                                    'ICE candidates & TURN fallback: ICE (Interactive Connectivity '
                                                    'Establishment) collects candidate network paths (host, srflx, '
                                                    'relay); if direct P2P fails due to strict firewalls/symmetric '
                                                    'NAT, traffic falls back to a TURN (Traversal Using Relays around '
                                                    'NAT) relay server']}]},
          {'topic_tag': 'OAuth 2.0 PKCE Flow',
           'question': 'Explain why Proof Key for Code Exchange (PKCE) is required for OAuth 2.0 authorization flows '
                       'in Single Page Applications.',
           'keywords': ['OAuth 2.0',
                        'PKCE',
                        'Code Verifier',
                        'Code Challenge',
                        'Authorization Code Flow',
                        'Single Page Apps'],
           'expected_concepts': ['Public client limitation: SPAs and mobile apps cannot securely protect a '
                                 'client_secret because all compiled JavaScript and binary assets are exposed to '
                                 'client-side inspection and decompilation',
                                 'Authorization code interception attack: In standard Authorization Code flow without '
                                 'PKCE, an attacker on the same device or malicious browser extension can intercept '
                                 'the authorization code at the redirect URI and exchange it for access tokens',
                                 'PKCE cryptographic mechanism: Client generates a cryptographically random '
                                 "'code_verifier' and derives a 'code_challenge' = SHA256(code_verifier); client sends "
                                 'code_challenge in the initial /authorize request',
                                 'Token exchange validation: When exchanging the code at /token, client sends the '
                                 'plaintext code_verifier; the authorization server hashes it and verifies it matches '
                                 'the original code_challenge before issuing tokens, rendering intercepted codes '
                                 'useless'],
           'model_answer': 'In OAuth 2.0 (RFC 6749 and RFC 7636), client applications are categorized as either '
                           "'Confidential Clients' (traditional backend servers that can securely store a "
                           "client_secret) or 'Public Clients' (Single Page Applications and mobile apps where all "
                           'source code, memory, and storage are fully accessible to the end user). 1. The '
                           'Vulnerability in Standard Authorization Code Flow: In the traditional authorization code '
                           'flow, the client redirects the user to the authorization server, receives an authorization '
                           "code at its redirect URI, and exchanges that code alongside a 'client_secret' for an "
                           'access token. Because an SPA cannot securely store a client_secret (anyone can open '
                           'DevTools and view it in JavaScript), public clients originally either omitted the secret '
                           'or used the insecure Implicit Flow (which returned tokens directly in URL hash fragments, '
                           'exposing them to browser history and referer leaks). Without a secret, any attacker or '
                           'malicious browser extension that intercepts the authorization code at the redirect URI can '
                           'immediately exchange it for an access token. 2. The PKCE (Proof Key for Code Exchange) '
                           "Solution: PKCE (pronounced 'pixy') dynamically binds the authorization code request to the "
                           'token exchange request using cryptographic challenge verification: - Step 1: When '
                           'initiating login, the SPA generates a cryptographically random string called the '
                           "'code_verifier' (43-128 characters) and computes the 'code_challenge': code_challenge = "
                           'Base64URL(SHA256(code_verifier)). - Step 2: The SPA redirects the user to the auth server '
                           "with 'code_challenge' and 'code_challenge_method=S256'. The server records the challenge "
                           'and issues an authorization code. - Step 3: When exchanging the authorization code at the '
                           "'/token' endpoint, the SPA sends the original plaintext 'code_verifier'. - Step 4: The "
                           'auth server computes SHA256(code_verifier) and verifies that it exactly matches the stored '
                           "'code_challenge'. 3. Security Guarantee: If a malicious actor intercepts the authorization "
                           'code, they cannot exchange it for an access token because they do not possess the original '
                           "'code_verifier', which never left the victim's client memory.",
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'PKCE (Proof Key for Code Exchange) is required for Single Page '
                                              "Applications because SPAs are 'public clients' that cannot securely "
                                              'hold a secret. In traditional OAuth 2.0 Authorization Code flow used by '
                                              'backend servers, the server presents a client_secret to exchange the '
                                              'authorization code for an access token. But in an SPA, all JavaScript '
                                              'code runs in the browser—if you hardcode a client_secret, any user or '
                                              'attacker can open DevTools and steal it. Historically, SPAs used the '
                                              'Implicit Flow to bypass this, but that returned access tokens directly '
                                              'in URL hash fragments, which leaked into browser history and access '
                                              'logs. In standard auth code flow without a secret, an attacker using a '
                                              'malicious browser extension or custom URL scheme could intercept the '
                                              'authorization code at the redirect URI and exchange it for a token. '
                                              'PKCE solves this using dynamic cryptographic proof: 1. When the user '
                                              'clicks login, the SPA generates a cryptographically random string '
                                              "called the 'code_verifier'. 2. It hashes this verifier using SHA-256 to "
                                              "create the 'code_challenge'. 3. It redirects the user to the "
                                              "authorization server, passing the 'code_challenge' and "
                                              "'code_challenge_method=S256'. The auth server saves the challenge and "
                                              'returns an authorization code. 4. When the SPA calls the token endpoint '
                                              "to exchange the code, it sends the original plaintext 'code_verifier'. "
                                              '5. The auth server hashes the verifier with SHA-256 and verifies that '
                                              'it matches the challenge it received earlier. If an attacker intercepts '
                                              'the authorization code, it is completely useless to them because they '
                                              'do not have the code_verifier, which was kept safely in browser memory.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'PKCE is required for SPAs because they are public clients that cannot '
                                              'securely store a client_secret in frontend JavaScript without it being '
                                              'exposed. In the PKCE flow, the client generates a random code_verifier '
                                              'and creates a code_challenge by hashing it with SHA-256. It sends the '
                                              'code_challenge to the authorization server during the initial login '
                                              'redirect. When the server returns the authorization code, the SPA sends '
                                              'the plaintext code_verifier to the token endpoint. The server hashes it '
                                              'to verify it matches the code_challenge before returning access tokens. '
                                              'This prevents attackers from stealing the authorization code and using '
                                              'it.',
                               'missing_concepts': ['Authorization code interception attack: In standard Authorization '
                                                    'Code flow without PKCE, an attacker on the same device or '
                                                    'malicious browser extension can intercept the authorization code '
                                                    'at the redirect URI and exchange it for access tokens']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'PKCE stands for Proof Key for Code Exchange. It is used in React and '
                                              'mobile apps because they cannot store a client secret safely. Instead '
                                              'of a client secret, the app generates a code verifier and code '
                                              'challenge using SHA-256. The server checks the code verifier when '
                                              'exchanging the authorization code for an access token. This replaced '
                                              'the insecure OAuth implicit flow and prevents hackers from stealing '
                                              'authorization codes.',
                               'missing_concepts': ['Public client limitation: SPAs and mobile apps cannot securely '
                                                    'protect a client_secret because all compiled JavaScript and '
                                                    'binary assets are exposed to client-side inspection and '
                                                    'decompilation',
                                                    'Token exchange validation: When exchanging the code at /token, '
                                                    'client sends the plaintext code_verifier; the authorization '
                                                    'server hashes it and verifies it matches the original '
                                                    'code_challenge before issuing tokens, rendering intercepted codes '
                                                    'useless']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'PKCE is an encryption protocol that encrypts passwords in the browser '
                                              'before sending them over HTTP. It is used because SPAs do not support '
                                              'HTTPS certificates. The code verifier is an SMS two-factor '
                                              "authentication code texted to the user's phone.",
                               'missing_concepts': ['Public client limitation: SPAs and mobile apps cannot securely '
                                                    'protect a client_secret because all compiled JavaScript and '
                                                    'binary assets are exposed to client-side inspection and '
                                                    'decompilation',
                                                    'Authorization code interception attack: In standard Authorization '
                                                    'Code flow without PKCE, an attacker on the same device or '
                                                    'malicious browser extension can intercept the authorization code '
                                                    'at the redirect URI and exchange it for access tokens',
                                                    'PKCE cryptographic mechanism: Client generates a '
                                                    "cryptographically random 'code_verifier' and derives a "
                                                    "'code_challenge' = SHA256(code_verifier); client sends "
                                                    'code_challenge in the initial /authorize request',
                                                    'Token exchange validation: When exchanging the code at /token, '
                                                    'client sends the plaintext code_verifier; the authorization '
                                                    'server hashes it and verifies it matches the original '
                                                    'code_challenge before issuing tokens, rendering intercepted codes '
                                                    'useless']}]},
          {'topic_tag': 'SPA Client Routing & History API',
           'question': 'How do Single Page Application client-side routers implement deep linking using the HTML5 '
                       'History API without triggering page reloads?',
           'keywords': ['Single Page Application',
                        'HTML5 History API',
                        'pushState()',
                        'popstate Event',
                        'Client-side Router',
                        'Fallback Routing'],
           'expected_concepts': ['HTML5 History API: history.pushState(state, title, url) and history.replaceState() '
                                 'update the browser URL and history stack programmatically without initiating a full '
                                 'page reload',
                                 'Event interception: Client router intercepts internal link clicks (e.g. <Link '
                                 "to='/about'>), calls e.preventDefault() to block default browser GET navigation, "
                                 'invokes pushState(), and matches current path against route components',
                                 "Handling browser Back/Forward: The browser fires the 'popstate' event on window when "
                                 "the user navigates browser history; the router listens for 'popstate' to synchronize "
                                 'UI state with the current URL',
                                 'Server-side fallback configuration: Deep linking requires configuring the web server '
                                 '(Nginx, Netlify, Apache) with a wildcard fallback redirecting all unmatched requests '
                                 '(/* -> index.html) to serve the SPA shell instead of 404s'],
           'model_answer': 'In Single Page Applications (SPAs), client-side routing libraries (like React Router or '
                           'Vue Router) decouple navigation from server requests by leveraging the HTML5 History API '
                           '(RFC standard): 1. HTML5 History API Mechanics: In traditional multi-page apps, clicking '
                           'an anchor tag \'<a href="/profile">\' triggers an HTTP GET request to the server, '
                           'discarding the current DOM and reloading the entire page. The HTML5 History API introduces '
                           "'history.pushState(state, unused, url)' and 'history.replaceState()'. These methods "
                           "programmatically update the URL displayed in the browser's address bar and push a new "
                           "entry onto the browser's session history stack without prompting the browser to send a "
                           'network request or reload the page. 2. Link Interception & Route Matching: Client-side '
                           'routing components (e.g., \'<Link to="/dashboard">\') intercept click events via an event '
                           "listener. When clicked, the router invokes 'event.preventDefault()' to cancel the native "
                           "browser navigation, calls 'history.pushState(null, '', '/dashboard')', updates internal "
                           'router state, matches the new pathname against declared route definitions, and swaps the '
                           'rendered component subtree in place. 3. Handling Back / Forward Navigation: Calling '
                           "'pushState' does not trigger an event. However, when the user clicks the browser's native "
                           "Back or Forward buttons, the browser dispatches the 'popstate' event on the global "
                           '\'window\' object. The client router listens for \'window.addEventListener("popstate", '
                           "...)', extracts 'window.location.pathname', and re-renders the matching route components. "
                           '4. Server-Side Fallback Routing: When a user directly enters a deep link (e.g., '
                           "'https://app.com/users/42') or refreshes the page, the browser issues a standard HTTP GET "
                           "request directly to the web server. If the server only hosts a static 'index.html', it "
                           'returns a 404 Not Found error. To support deep linking, the web server (Nginx, Caddy, '
                           "Cloudflare) must be configured with a fallback rewrite: 'try_files $uri $uri/ "
                           "/index.html;', serving the SPA shell for all routes so client-side JavaScript can take "
                           'over.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'Single Page Application client-side routers achieve deep linking '
                                              'without full page reloads through the HTML5 History API and server '
                                              'fallback routing: 1. The History API: Traditionally, changing the '
                                              "browser's URL triggered an HTTP GET request to the server, reloading "
                                              "the page. The HTML5 History API introduced 'history.pushState(state, "
                                              "'', url)' and 'history.replaceState()'. These APIs update the URL in "
                                              "the address bar and push a new entry onto the browser's session history "
                                              'stack completely client-side, without the browser making a network '
                                              'request or reloading the DOM. 2. Link Interception: Routers like React '
                                              'Router provide a <Link> component that wraps an <a> tag. When clicked, '
                                              "the router calls 'e.preventDefault()' to stop native browser "
                                              "navigation. It then calls 'history.pushState()' to update the URL, "
                                              'matches the new path against its route configuration table, and updates '
                                              'its internal React state to re-render only the new route component. 3. '
                                              "Handling Browser Back/Forward: When the user clicks the browser's Back "
                                              "or Forward buttons, the browser fires the 'popstate' event on the "
                                              'window object. The router listens for '
                                              "'window.addEventListener('popstate')', reads the new location.pathname, "
                                              'and re-renders the corresponding view. 4. Server-Side Fallback: The '
                                              'critical production hurdle with client routing is deep linking on hard '
                                              "refresh. If a user visits 'mysite.com/dashboard/settings' directly or "
                                              'refreshes the page, the browser sends an HTTP GET request to the web '
                                              "server for that exact file path. If the server doesn't have a physical "
                                              'file at that path, it returns a 404 error. The web server (like Nginx '
                                              "or Netlify) must be configured with a wildcard rewrite: 'try_files $uri "
                                              "$uri/ /index.html', ensuring the main index.html SPA shell is always "
                                              'served so client-side routing can take over.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'SPA routers use the HTML5 History API methods history.pushState and '
                                              'history.replaceState to change the browser URL without triggering a '
                                              'full page reload. When a user clicks a router Link, the router '
                                              'intercepts the click with event.preventDefault(), calls pushState to '
                                              'update the URL in the address bar, and renders the matching component '
                                              'in the virtual DOM. It also listens to the window popstate event to '
                                              'handle when the user clicks the browser Back and Forward buttons. On '
                                              'the server side, you have to configure Nginx to redirect all unmatched '
                                              "routes back to index.html so refreshing a deep link doesn't result in a "
                                              '404.',
                               'missing_concepts': ['Event interception: Client router intercepts internal link clicks '
                                                    "(e.g. <Link to='/about'>), calls e.preventDefault() to block "
                                                    'default browser GET navigation, invokes pushState(), and matches '
                                                    'current path against route components']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': "Client-side routers like React Router work using the browser's History "
                                              'API. When you click a link, it uses pushState to change the URL without '
                                              'reloading the page, and loads the new component. When you click the '
                                              'back button, it listens for the popstate event to go back. If you '
                                              'refresh the page on a deep link, the server will give a 404 error '
                                              'unless you configure your server to redirect all requests to '
                                              'index.html.',
                               'missing_concepts': ['HTML5 History API: history.pushState(state, title, url) and '
                                                    'history.replaceState() update the browser URL and history stack '
                                                    'programmatically without initiating a full page reload',
                                                    'Event interception: Client router intercepts internal link clicks '
                                                    "(e.g. <Link to='/about'>), calls e.preventDefault() to block "
                                                    'default browser GET navigation, invokes pushState(), and matches '
                                                    'current path against route components']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': "SPA routing works by storing all web pages in the browser's cookies. "
                                              "The History API is an automated backup tool that downloads the user's "
                                              'browsing history to a text file. Deep linking only works if the user '
                                              'installs a Chrome extension.',
                               'missing_concepts': ['HTML5 History API: history.pushState(state, title, url) and '
                                                    'history.replaceState() update the browser URL and history stack '
                                                    'programmatically without initiating a full page reload',
                                                    'Event interception: Client router intercepts internal link clicks '
                                                    "(e.g. <Link to='/about'>), calls e.preventDefault() to block "
                                                    'default browser GET navigation, invokes pushState(), and matches '
                                                    'current path against route components',
                                                    "Handling browser Back/Forward: The browser fires the 'popstate' "
                                                    'event on window when the user navigates browser history; the '
                                                    "router listens for 'popstate' to synchronize UI state with the "
                                                    'current URL',
                                                    'Server-side fallback configuration: Deep linking requires '
                                                    'configuring the web server (Nginx, Netlify, Apache) with a '
                                                    'wildcard fallback redirecting all unmatched requests (/* -> '
                                                    'index.html) to serve the SPA shell instead of 404s']}]},
          {'topic_tag': 'Custom Virtual DOM Diffing Mechanics',
           'question': 'Formulate an O(N) heuristic diffing algorithm for Virtual DOM reconciliation, detailing '
                       'key-based list re-ordering.',
           'keywords': ['Virtual DOM Diffing',
                        'Heuristic O(N) Algorithm',
                        'Keyed Elements',
                        'Tree Traversal',
                        'Patch Generation',
                        'Reconciliation'],
           'expected_concepts': ['Tree comparison complexity: Computing the true minimum edit distance between two '
                                 'arbitrary trees has an intractable O(n^3) complexity; React/Vue solve this with '
                                 'heuristic O(n) assumptions',
                                 'Heuristic assumptions: 1. Two elements of different types produce entirely different '
                                 'trees (unmount old subtree, mount new subtree); 2. Elements are diffed '
                                 'level-by-level (breadth-first / preorder without cross-level subtree moves)',
                                 'Key-based list reconciliation: Without keys, list updates compare by index, causing '
                                 'inefficient DOM element thrashing or lost state when items are prepended; Keys '
                                 'provide unique identities across renders',
                                 'List diffing algorithm & LIS: Algorithms construct a key-to-index map, identify '
                                 'insertions and deletions, and compute the Longest Increasing Subsequence (LIS) of '
                                 'indices to minimize actual physical DOM node movements'],
           'model_answer': 'Reconciling two arbitrary hierarchical trees mathematically requires solving the tree edit '
                           'distance problem, which operates at O(n^3) complexity (e.g., Zhang-Shasha algorithm). For '
                           'an application with 1,000 nodes, 10^9 operations would paralyze the browser. Virtual DOM '
                           'engines achieve linear O(n) diffing through practical heuristics and key-based list '
                           'reconciliation: 1. Two Foundational Heuristic Rules: - Rule 1 (Different Types): If two '
                           "VNodes have different types (e.g., '<div>' changes to '<span>', or '<ComponentA>' changes "
                           "to '<ComponentB>'), the reconciler does not attempt to diff their children. It unmounts "
                           'the old subtree completely (triggering cleanups) and mounts the new subtree from scratch. '
                           '- Rule 2 (Level-by-Level Traversal): The diffing algorithm compares trees level-by-level. '
                           'It assumes components rarely migrate across completely different branches of the '
                           'hierarchy; if a child moves to a different parent, it is treated as a deletion and '
                           'insertion rather than a subtree relocation. 2. Diffing Same-Type Nodes: When two nodes '
                           'have the same type, the algorithm computes a minimal patch: it diffs their '
                           'attributes/props, updates changed properties, removes deleted ones, and then recursively '
                           'reconciles their children. 3. Key-Based List Reconciliation: Diffing child lists is where '
                           'naive algorithms fail: without keys, comparing children by index when an item is prepended '
                           'causes every existing item to appear mutated. Keys provide persistent identity: - Step 1: '
                           "Create a hash map of 'key -> oldIndex' from the old children list. - Step 2: Traverse new "
                           "children. For each new child, look up its key in the map. If missing, generate an 'insert' "
                           'patch. If present, mark it as retained and diff their props. Any old keys unvisited are '
                           "marked for 'deletion'. - Step 3 (Longest Increasing Subsequence - LIS): In modern engines "
                           'like Vue 3 and Inferno, the algorithm builds an array mapping new indices to old positions '
                           'and computes the Longest Increasing Subsequence (LIS). Items within the LIS do not need to '
                           'move; only elements outside the LIS are physically relocated in the DOM via '
                           "'Node.insertBefore()', minimizing real DOM operations to the mathematical optimum.",
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'The classic tree edit distance algorithm has an O(n^3) time '
                                              'complexity—for a UI with just 1,000 nodes, a single render would '
                                              'require a billion operations. React and Vue achieve an O(n) linear '
                                              'diffing algorithm through two heuristic assumptions and key-based list '
                                              'reconciliation: 1. Heuristic 1: Elements of different types produce '
                                              "different trees. If a <div> turns into a <p>, the reconciler doesn't "
                                              'bother diffing children; it tears down the entire old subtree and '
                                              'mounts the new one from scratch. 2. Heuristic 2: Traversal is done '
                                              'strictly level-by-level. The algorithm assumes components rarely jump '
                                              'across completely different parent branches. 3. Same-type diffing: If '
                                              'elements have the same tag, it diffs attributes, updates modified '
                                              'props, and moves on to reconciling the children array. 4. Key-based '
                                              'list reconciliation: The hardest problem is reconciling lists of '
                                              'children. If you insert a new item at the beginning of an unkeyed list, '
                                              'an index-based comparison will think every single item changed its '
                                              "text, causing 1,000 DOM mutations. Stable 'key' props give each VNode a "
                                              'persistent identity. The algorithm works in three steps: First, it '
                                              "builds a hash map of 'key -> oldIndex' for the old children. Second, it "
                                              'loops through the new children, matching keys to detect insertions and '
                                              'deletions. Third, to minimize DOM node movements, modern engines like '
                                              'Vue 3 compute the Longest Increasing Subsequence (LIS) of the '
                                              'old-to-new index mappings. Nodes belonging to the LIS remain stationary '
                                              'in the DOM, and only the remaining nodes are moved using '
                                              'insertBefore(). This guarantees the minimum physical DOM mutations '
                                              'possible in O(n) time.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'Finding the minimum difference between two trees normally takes O(n^3) '
                                              'time, which is too slow for UI rendering. Virtual DOM diffing reduces '
                                              'this to O(n) by using two heuristics: first, if two nodes have '
                                              'different types, it replaces the entire tree without diffing children; '
                                              "second, it assumes components don't move across different levels of the "
                                              'tree. When diffing arrays of children, it uses unique key props. '
                                              'Without keys, adding an item to the start of a list forces React to '
                                              'mutate every item by index. With keys, the algorithm builds a map of '
                                              'keys, matches old and new elements, and only moves, inserts, or deletes '
                                              'elements that actually changed.',
                               'missing_concepts': ['List diffing algorithm & LIS: Algorithms construct a key-to-index '
                                                    'map, identify insertions and deletions, and compute the Longest '
                                                    'Increasing Subsequence (LIS) of indices to minimize actual '
                                                    'physical DOM node movements']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'Standard tree diffing takes O(n cubed) time, but React uses an O(n) '
                                              'heuristic diffing algorithm. If two elements have different tags, React '
                                              'destroys the old one and creates a new one. In lists, you have to use '
                                              'key props so React knows which items were added, deleted, or moved. If '
                                              "you don't use keys, React compares items by their array index which is "
                                              'slow and causes bugs when you reorder items.',
                               'missing_concepts': ['Heuristic assumptions: 1. Two elements of different types produce '
                                                    'entirely different trees (unmount old subtree, mount new '
                                                    'subtree); 2. Elements are diffed level-by-level (breadth-first / '
                                                    'preorder without cross-level subtree moves)',
                                                    'List diffing algorithm & LIS: Algorithms construct a key-to-index '
                                                    'map, identify insertions and deletions, and compute the Longest '
                                                    'Increasing Subsequence (LIS) of indices to minimize actual '
                                                    'physical DOM node movements']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': "Virtual DOM diffing uses Dijkstra's shortest path algorithm to sort DOM "
                                              'nodes alphabetically by class name. Keys must always be Math.random() '
                                              'so React regenerates every component on every frame. O(N) means the '
                                              'algorithm takes N gigabytes of RAM.',
                               'missing_concepts': ['Tree comparison complexity: Computing the true minimum edit '
                                                    'distance between two arbitrary trees has an intractable O(n^3) '
                                                    'complexity; React/Vue solve this with heuristic O(n) assumptions',
                                                    'Heuristic assumptions: 1. Two elements of different types produce '
                                                    'entirely different trees (unmount old subtree, mount new '
                                                    'subtree); 2. Elements are diffed level-by-level (breadth-first / '
                                                    'preorder without cross-level subtree moves)',
                                                    'Key-based list reconciliation: Without keys, list updates compare '
                                                    'by index, causing inefficient DOM element thrashing or lost state '
                                                    'when items are prepended; Keys provide unique identities across '
                                                    'renders',
                                                    'List diffing algorithm & LIS: Algorithms construct a key-to-index '
                                                    'map, identify insertions and deletions, and compute the Longest '
                                                    'Increasing Subsequence (LIS) of indices to minimize actual '
                                                    'physical DOM node movements']}]},
          {'topic_tag': 'Database Connection Pooling & Isolation',
           'question': 'Explain how backend database connection pools optimize socket re-use and compare SQL '
                       'transaction isolation levels under concurrent access.',
           'keywords': ['Connection Pooling',
                        'ACID Transactions',
                        'Isolation Levels',
                        'Read Committed',
                        'Serializable',
                        'Deadlock Handling'],
           'expected_concepts': ['Connection pooling mechanics: Establishing database connections incurs heavy TCP '
                                 '3-way handshakes, TLS negotiation, and backend process spawning; connection pools '
                                 'maintain a pre-allocated pool of warm socket connections, leasing and reclaiming '
                                 'them to prevent DB exhaustion',
                                 'Concurrency anomalies: Dirty Reads (reading uncommitted data), Non-Repeatable Reads '
                                 '(re-reading a row returns altered data), and Phantom Reads (re-running a range query '
                                 'returns newly inserted rows)',
                                 'Four ANSI SQL Isolation Levels: 1. Read Uncommitted (dirty reads allowed); 2. Read '
                                 'Committed (prevents dirty reads via MVCC snapshots, standard default in Postgres); '
                                 '3. Repeatable Read (prevents non-repeatable reads, snapshot isolation); 4. '
                                 'Serializable (strict serializability via two-phase locking or SSI, completely '
                                 'eliminating all anomalies at the cost of concurrency aborts)',
                                 'Performance trade-off: Higher isolation guarantees mathematical consistency but '
                                 'increases lock contention, transaction latency, and deadlock risk, requiring '
                                 'application retry loops'],
           'model_answer': 'In high-throughput web backends, managing database access requires connection pooling and '
                           'configuring appropriate transaction isolation levels: 1. Database Connection Pooling: '
                           'Opening a database connection (PostgreSQL, MySQL) is an expensive operation: it requires a '
                           'TCP three-way handshake, TLS encryption setup, authentication validation, and in '
                           'PostgreSQL, spawning a dedicated backend operating system process (~10-20MB RAM per '
                           'connection). Under high traffic (thousands of concurrent requests), opening a connection '
                           'per request crashes the database with connection starvation. A Connection Pool (e.g., '
                           'HikariCP, pgBouncer, node-postgres Pool) maintains a warm pool of pre-established '
                           'connections (e.g., 20-50 connections). When a request needs to query the database, it '
                           'checks out an idle connection from the pool, executes queries, and returns it to the pool '
                           'in microseconds. 2. Concurrency Anomalies & SQL Isolation Levels: Transactions execute '
                           "under ACID constraints, where 'I' (Isolation) determines how concurrent transactions "
                           'interact. ANSI SQL defines four isolation levels addressing specific anomalies: - Read '
                           'Uncommitted: Transactions can read uncommitted data written by other in-flight '
                           'transactions (Dirty Reads). Almost never used. - Read Committed (Default in '
                           'PostgreSQL/Oracle): Prevents Dirty Reads. A query only reads data committed prior to that '
                           'query starting. However, Non-Repeatable Reads can occur (if Transaction A reads a row, '
                           'Transaction B commits an update to that row, and Transaction A re-reads the row, it sees '
                           'the new values). - Repeatable Read (Default in MySQL InnoDB): Prevents Dirty and '
                           'Non-Repeatable Reads. Uses Multi-Version Concurrency Control (MVCC) snapshots; Transaction '
                           'A sees an immutable snapshot of data as it existed when the transaction began. In ANSI '
                           'SQL, Phantom Reads (new rows inserted matching a range query) are possible, though InnoDB '
                           'prevents phantoms via Next-Key locking. - Serializable: The highest isolation level. '
                           'Guarantees transactions execute as if strictly serialized one after another. Prevents all '
                           'anomalies (Dirty, Non-repeatable, and Phantom reads) using two-phase locking or '
                           'Serializable Snapshot Isolation (SSI). Trade-off: Severe lock contention, serialization '
                           "failures ('could not serialize access'), and deadlocks that require application-level "
                           'retry logic.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'Connection pooling and transaction isolation are fundamental to '
                                              'scalable backend databases: 1. Connection Pooling: Establishing a new '
                                              'database connection is very expensive—it requires a TCP handshake, TLS '
                                              'negotiation, authentication, and in engines like PostgreSQL, forking a '
                                              'dedicated backend OS process. If a web server with 1,000 concurrent '
                                              'requests tried to open 1,000 connections, the database would exhaust '
                                              'RAM and crash. A connection pool (like pgBouncer or HikariCP) maintains '
                                              'a fixed pool of warm, authenticated connections (say 20 to 50). '
                                              'Requests borrow a connection from the pool, execute their query, and '
                                              'release it back to the pool in milliseconds, preventing database '
                                              'overload. 2. Transaction Isolation Levels: When multiple transactions '
                                              'run concurrently, three main anomalies can occur: Dirty Reads (reading '
                                              'uncommitted data that might be rolled back), Non-Repeatable Reads '
                                              '(reading the same row twice in one transaction and getting different '
                                              'values because another transaction committed an update), and Phantom '
                                              'Reads (re-running a range query and getting new rows inserted by '
                                              'another transaction). The four ANSI SQL isolation levels handle these '
                                              'progressively: - Read Uncommitted allows dirty reads. - Read Committed '
                                              "prevents dirty reads using MVCC snapshots; it's the default in "
                                              'Postgres. - Repeatable Read prevents dirty and non-repeatable reads by '
                                              'providing an immutable snapshot of the data from the start of the '
                                              'transaction. - Serializable is the strictest level. It guarantees that '
                                              'concurrent transactions produce the exact same outcome as if they ran '
                                              'sequentially one after another, eliminating all anomalies. The '
                                              'trade-off is performance: Serializable creates high lock contention and '
                                              'transaction serialization failures, meaning your backend must implement '
                                              'retry loops to handle aborted transactions.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'Connection pooling keeps a reusable pool of active database connections '
                                              "open so that backend requests don't have to perform an expensive TCP "
                                              'handshake and authentication on every query. When an API request needs '
                                              'to query the database, it borrows a connection from the pool and '
                                              'returns it when done. Transaction isolation controls how concurrent '
                                              "transactions see each other's changes. Read Committed prevents dirty "
                                              'reads by only reading committed data. Repeatable Read ensures that '
                                              'reading the same row multiple times returns the same data. Serializable '
                                              'is the highest level that completely prevents all concurrency anomalies '
                                              'like phantom reads by running transactions as if they were serial, '
                                              'though it can cause deadlocks and transaction aborts.',
                               'missing_concepts': ['Concurrency anomalies: Dirty Reads (reading uncommitted data), '
                                                    'Non-Repeatable Reads (re-reading a row returns altered data), and '
                                                    'Phantom Reads (re-running a range query returns newly inserted '
                                                    'rows)']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'Connection pooling is a cache of database connections that speeds up '
                                              'backend applications. Opening a new database connection takes time, so '
                                              'the pool reuses existing connections. SQL isolation levels define how '
                                              'safe transactions are. Read committed only reads data that has been '
                                              'committed, while serializable is the strictest level where transactions '
                                              'are executed one at a time so there are no conflicts. Higher isolation '
                                              'levels are safer but slower because of database locking.',
                               'missing_concepts': ['Concurrency anomalies: Dirty Reads (reading uncommitted data), '
                                                    'Non-Repeatable Reads (re-reading a row returns altered data), and '
                                                    'Phantom Reads (re-running a range query returns newly inserted '
                                                    'rows)',
                                                    'Four ANSI SQL Isolation Levels: 1. Read Uncommitted (dirty reads '
                                                    'allowed); 2. Read Committed (prevents dirty reads via MVCC '
                                                    'snapshots, standard default in Postgres); 3. Repeatable Read '
                                                    '(prevents non-repeatable reads, snapshot isolation); 4. '
                                                    'Serializable (strict serializability via two-phase locking or '
                                                    'SSI, completely eliminating all anomalies at the cost of '
                                                    'concurrency aborts)']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'Connection pooling is when multiple databases share the same hard '
                                              'drive. Isolation levels are firewall settings on AWS RDS. Read '
                                              'uncommitted is the best level because it has the fastest performance '
                                              'and zero bugs.',
                               'missing_concepts': ['Connection pooling mechanics: Establishing database connections '
                                                    'incurs heavy TCP 3-way handshakes, TLS negotiation, and backend '
                                                    'process spawning; connection pools maintain a pre-allocated pool '
                                                    'of warm socket connections, leasing and reclaiming them to '
                                                    'prevent DB exhaustion',
                                                    'Concurrency anomalies: Dirty Reads (reading uncommitted data), '
                                                    'Non-Repeatable Reads (re-reading a row returns altered data), and '
                                                    'Phantom Reads (re-running a range query returns newly inserted '
                                                    'rows)',
                                                    'Four ANSI SQL Isolation Levels: 1. Read Uncommitted (dirty reads '
                                                    'allowed); 2. Read Committed (prevents dirty reads via MVCC '
                                                    'snapshots, standard default in Postgres); 3. Repeatable Read '
                                                    '(prevents non-repeatable reads, snapshot isolation); 4. '
                                                    'Serializable (strict serializability via two-phase locking or '
                                                    'SSI, completely eliminating all anomalies at the cost of '
                                                    'concurrency aborts)',
                                                    'Performance trade-off: Higher isolation guarantees mathematical '
                                                    'consistency but increases lock contention, transaction latency, '
                                                    'and deadlock risk, requiring application retry loops']}]},
          {'topic_tag': 'Node.js V8 Heap & Garbage Collection',
           'question': 'Analyze V8 engine memory allocation (New Space vs Old Space) and explain how Scavenger and '
                       'Mark-Sweep garbage collectors operate.',
           'keywords': ['V8 Heap',
                        'Garbage Collection',
                        'Scavenger Algorithm',
                        'Mark-Sweep-Compact',
                        'Memory Leak Debugging',
                        'Generational Hypothesis'],
           'expected_concepts': ['Generational hypothesis: The majority of allocated objects die young (short '
                                 'lifecycle), leading V8 to bifurcate heap memory into New Space (Young Generation) '
                                 'and Old Space (Old Generation)',
                                 'New Space & Scavenger (Minor GC): Divided into two equal semi-spaces (From-space and '
                                 "To-space); Cheney's copying algorithm copies live objects from From to To space, "
                                 'swapping them in O(live) time; surviving objects are promoted (tenured) to Old Space',
                                 'Old Space & Mark-Sweep-Compact (Major GC): Handles long-lived objects; Mark phase '
                                 'traverses object graph from GC roots; Sweep phase frees unreferenced memory cells; '
                                 'Compact phase defragments heap to eliminate memory fragmentation',
                                 'Minimizing stop-the-world latency: V8 utilizes incremental marking, concurrent '
                                 'marking, and parallel scavenging on worker threads to avoid blocking the JavaScript '
                                 'main thread'],
           'model_answer': "Google's V8 engine (powers Node.js and Chrome) executes automatic memory management based "
                           "on the 'Weak Generational Hypothesis'—the empirical observation that the vast majority of "
                           'allocated objects are short-lived and die shortly after creation. To optimize garbage '
                           'collection latency, V8 partitions its heap into distinct memory generations: 1. New Space '
                           '(Young Generation): Dedicated to newly allocated objects (typically 1MB - 64MB). - '
                           "Scavenger Collector (Minor GC): Implements Cheney's Copying Algorithm. New space is split "
                           "into two equal-sized semi-spaces: 'From-space' and 'To-space'. All new allocations occur "
                           'in From-space. - When From-space fills, a Minor GC triggers: the Scavenger traces live '
                           'objects from roots, copies them contiguously into To-space (compacting them '
                           'automatically), and discards all dead objects in From-space. The roles of From-space and '
                           'To-space are then swapped. - Object Promotion (Tenuring): If an object survives two '
                           'successive Scavenger cycles, or if To-space becomes more than 25% full during copying, the '
                           'object is promoted (tenured) to Old Space. 2. Old Space (Old Generation): Dedicated to '
                           'long-lived objects, surviving closures, and promoted data structures. - Mark-Sweep-Compact '
                           '(Major GC): Because Old Space is large (up to several gigabytes), copying algorithms are '
                           'too expensive. Major GC operates in three phases: - Marking: Traces references from roots '
                           '(window/global, call stack, DOM) and marks all reachable live objects. - Sweeping: Walks '
                           'the heap memory addresses, adding non-marked (dead) memory segments to free lists for '
                           'future allocations. - Compacting: Defragments the heap by shifting surviving live objects '
                           'together, resolving external memory fragmentation. 3. Concurrency Innovations: '
                           "Historically, Major GC caused 'stop-the-world' freezes of several hundred milliseconds. "
                           'Modern V8 implements Incremental Marking (interleaving small marking slices with '
                           'JavaScript execution), Concurrent Marking (running marking on background worker threads '
                           'while JavaScript executes), and Parallel Sweeping to keep GC pauses under 5ms.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 97,
                               'answer_text': "V8's memory management is founded on the Weak Generational Hypothesis: "
                                              'the empirical rule that most objects die very young. To optimize '
                                              'performance, V8 divides its heap into New Space (the Young Generation) '
                                              'and Old Space (the Old Generation): 1. New Space and the Scavenger '
                                              '(Minor GC): New Space is small (usually 16MB to 64MB) and divided into '
                                              "two equal semi-spaces: 'From-space' and 'To-space'. All new objects are "
                                              "allocated in From-space. When it fills up, Minor GC runs Cheney's "
                                              'copying algorithm: it traverses live objects, copies them into To-space '
                                              '(which automatically defragments them), and immediately clears '
                                              'From-space. Then the spaces swap. Because most objects are already '
                                              'dead, this Scavenger step is extremely fast (proportional only to '
                                              'surviving objects). If an object survives two Scavenger cycles, it gets '
                                              'promoted (tenured) into Old Space. 2. Old Space and Mark-Sweep-Compact '
                                              '(Major GC): Old Space holds long-lived objects like singletons, global '
                                              'state, and persistent closures. Because Old Space can be gigabytes in '
                                              'size, a copying algorithm would waste half the memory. Instead, V8 uses '
                                              'Mark-Sweep-Compact: First, it Marks all reachable objects starting from '
                                              'root pointers. Second, it Sweeps the dead objects and adds their memory '
                                              'addresses to free lists. Third, it Compacts surviving objects together '
                                              'to eliminate memory fragmentation. 3. Preventing latency pauses: To '
                                              "avoid 'stop-the-world' main thread freezes, modern V8 uses Concurrent "
                                              'Marking and Parallel Sweeping on background helper threads, keeping '
                                              'main thread GC pauses down to a few milliseconds.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'V8 splits heap memory into New Space for short-lived objects and Old '
                                              'Space for long-lived objects. New Space is split into two semi-spaces: '
                                              'From-space and To-space. When From-space is full, the Scavenger '
                                              'collector copies the live objects into To-space and frees dead objects. '
                                              'Objects that survive multiple garbage collection cycles are promoted to '
                                              'Old Space. Old Space uses Mark-Sweep-Compact: it marks all reachable '
                                              'objects, sweeps dead memory, and compacts remaining objects to avoid '
                                              'fragmentation. V8 uses incremental and concurrent marking to minimize '
                                              'main-thread pauses.',
                               'missing_concepts': ['Generational hypothesis: The majority of allocated objects die '
                                                    'young (short lifecycle), leading V8 to bifurcate heap memory into '
                                                    'New Space (Young Generation) and Old Space (Old Generation)']},
                              {'quality_level': 'average',
                               'human_score': 61,
                               'answer_text': 'V8 has two main memory spaces: New space and Old space. New objects are '
                                              'created in New space, and if they survive garbage collection, they move '
                                              'to Old space. The Scavenger algorithm cleans New space by copying '
                                              'objects between two buffers. Old space uses Mark and Sweep, where it '
                                              'marks all active objects and sweeps away the unused memory. Compacting '
                                              'moves objects closer together to prevent memory fragmentation. This '
                                              'prevents Node.js from running out of memory.',
                               'missing_concepts': ['Generational hypothesis: The majority of allocated objects die '
                                                    'young (short lifecycle), leading V8 to bifurcate heap memory into '
                                                    'New Space (Young Generation) and Old Space (Old Generation)',
                                                    'Minimizing stop-the-world latency: V8 utilizes incremental '
                                                    'marking, concurrent marking, and parallel scavenging on worker '
                                                    'threads to avoid blocking the JavaScript main thread']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'V8 heap is allocated directly in the CPU L1 cache. The Scavenger '
                                              'algorithm is an open-source tool for finding security vulnerabilities '
                                              'in npm packages. Mark-Sweep is used to sweep deleted database records '
                                              'from MongoDB.',
                               'missing_concepts': ['Generational hypothesis: The majority of allocated objects die '
                                                    'young (short lifecycle), leading V8 to bifurcate heap memory into '
                                                    'New Space (Young Generation) and Old Space (Old Generation)',
                                                    'New Space & Scavenger (Minor GC): Divided into two equal '
                                                    "semi-spaces (From-space and To-space); Cheney's copying algorithm "
                                                    'copies live objects from From to To space, swapping them in '
                                                    'O(live) time; surviving objects are promoted (tenured) to Old '
                                                    'Space',
                                                    'Old Space & Mark-Sweep-Compact (Major GC): Handles long-lived '
                                                    'objects; Mark phase traverses object graph from GC roots; Sweep '
                                                    'phase frees unreferenced memory cells; Compact phase defragments '
                                                    'heap to eliminate memory fragmentation',
                                                    'Minimizing stop-the-world latency: V8 utilizes incremental '
                                                    'marking, concurrent marking, and parallel scavenging on worker '
                                                    'threads to avoid blocking the JavaScript main thread']}]},
          {'topic_tag': 'Module Bundling AST & Vite HMR Engine',
           'question': 'How does Vite leverage native ES modules and Hot Module Replacement (HMR) to provide instant '
                       'dev server updates compared to Webpack bundle graphs?',
           'keywords': ['Abstract Syntax Tree',
                        'Module Graph',
                        'Hot Module Replacement',
                        'Vite ESM Server',
                        'Rollup/Webpack',
                        'Bundle Chunks'],
           'expected_concepts': ['Traditional bundler (Webpack) dev bottleneck: Webpack must parse every source file, '
                                 'construct an in-memory Abstract Syntax Tree (AST) module graph, and bundle '
                                 'everything into memory before the dev server can start, scaling O(N) with codebase '
                                 'size',
                                 "Vite's unbundled native ESM dev server: Vite serves source code over native browser "
                                 "ES Modules (<script type='module'>); the dev server starts in O(1) instant time "
                                 'without pre-bundling user code',
                                 'On-demand compilation via esbuild: When the browser requests an imported module, '
                                 'Vite compiles that single file on the fly using esbuild (written in Go, 10-100x '
                                 'faster than JS compilers); heavy node_modules dependencies are pre-bundled once',
                                 'Granular Hot Module Replacement (HMR): When a file changes, Vite invalidates only '
                                 'that specific module in its module graph and pushes an update over WebSockets; the '
                                 'browser re-fetches only that single module, updating state instantly without page '
                                 'reloads'],
           'model_answer': 'Traditional JavaScript bundlers (Webpack, Parcel) face a fundamental scalability '
                           'limitation during local development: before serving a single web page, the bundler must '
                           'crawl the entire application entry point, parse every single file into an Abstract Syntax '
                           'Tree (AST), resolve all dependencies, construct a complete in-memory module graph, and '
                           'bundle the code into executable chunks. In large codebases (thousands of modules), '
                           'starting the dev server takes minutes, and Hot Module Replacement (HMR) edits take several '
                           'seconds because the bundler must re-bundle and re-evaluate dependent chunk graphs. Vite '
                           'completely re-engineers this dev experience by decoupling development from production '
                           'bundling: 1. Native ES Modules (ESM) Architecture: Modern browsers natively support ES '
                           'Modules (\'<script type="module">\' and native browser \'import\' statements). Vite takes '
                           "advantage of this by running an unbundled dev server. When you run 'vite', the dev server "
                           'starts instantly in O(1) time because it does NOT bundle application source code at all. '
                           '2. On-Demand Compilation with esbuild: When a browser navigates to the page, it requests '
                           'the root module over HTTP. The browser reads \'import Button from "./Button.jsx"\' and '
                           'issues a network request for that specific file. Vite intercepts the request, transforms '
                           "that single file on the fly (transpiling JSX/TypeScript via 'esbuild', which is written in "
                           'Go and operates 10-100x faster than Node-based compilers), and serves it. Modules for '
                           "other routes are never parsed until navigated to. Dependencies in 'node_modules' (which "
                           'rarely change) are pre-bundled once during cold start using esbuild into cached native '
                           'ESM. 3. Precision HMR Engine: When a developer edits a file, Vite updates only that single '
                           'node in its lightweight in-memory module graph. It dispatches a lightweight WebSocket '
                           'payload to the browser. The browser re-fetches only that single modified module via native '
                           'ESM, swapping the component in place via React Fast Refresh with zero page reload and '
                           'sub-50ms latency regardless of application size.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 97,
                               'answer_text': 'The fundamental difference between Vite and Webpack during development '
                                              'is that Webpack is a bundle-based dev server, while Vite is an '
                                              'unbundled, native ES Module (ESM) dev server. In Webpack, before the '
                                              'local server can serve anything, it has to crawl your entire '
                                              'application, parse every file into an Abstract Syntax Tree (AST), '
                                              'construct a complete dependency graph, and compile everything into '
                                              "in-memory bundles. In a codebase with 5,000 components, running 'npm "
                                              "run dev' can take two minutes, and editing a file requires re-bundling "
                                              'affected chunks. Vite solves this by letting modern browsers do the '
                                              'module resolution. Browsers support native ESM with <script '
                                              "type='module'>. When you run 'vite', the dev server starts instantly in "
                                              'O(1) time because it does not bundle your source code. When the browser '
                                              'loads index.html, it requests files as native ES module imports over '
                                              'HTTP. Vite intercepts each request and compiles that individual file on '
                                              'the fly using esbuild—which is written in Go and compiles '
                                              'TypeScript/JSX 10 to 100 times faster than Babel or Webpack. Only the '
                                              'files actually needed for the current screen are compiled. For '
                                              'third-party npm dependencies in node_modules, Vite pre-bundles them '
                                              'once using esbuild so they are served as single, cached ESM files. '
                                              'Finally, for Hot Module Replacement (HMR): when you edit a file, Vite '
                                              'uses a WebSocket to tell the browser to re-import just that one module. '
                                              'The browser fetches the updated file via native ESM, and React Fast '
                                              'Refresh swaps the component in place in under 50ms, completely '
                                              'independent of how huge the project is.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'Webpack has to bundle the entire project into memory before starting '
                                              'the dev server, which scales poorly and becomes very slow as the '
                                              'application grows. Vite solves this by using native ES modules in the '
                                              "browser. The dev server starts instantly because it doesn't pre-bundle "
                                              'your source code. When the browser requests a file via an import '
                                              'statement, Vite compiles that single file on the fly using esbuild, '
                                              "which is written in Go and extremely fast. When you edit a file, Vite's "
                                              'HMR updates only that exact file via WebSockets, allowing instant '
                                              'updates without full page reloads.',
                               'missing_concepts': ['Traditional bundler (Webpack) dev bottleneck: Webpack must parse '
                                                    'every source file, construct an in-memory Abstract Syntax Tree '
                                                    '(AST) module graph, and bundle everything into memory before the '
                                                    'dev server can start, scaling O(N) with codebase size']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'Vite is much faster than Webpack because it uses native ES modules in '
                                              'the browser instead of bundling everything together. Webpack takes a '
                                              'long time to start because it has to compile all files first. Vite '
                                              'starts immediately and only compiles files when the browser asks for '
                                              "them. It uses esbuild which is written in Go so it's super fast. Vite "
                                              'also has Hot Module Replacement so when you save a file, it updates in '
                                              'the browser instantly without refreshing the page.',
                               'missing_concepts': ['Traditional bundler (Webpack) dev bottleneck: Webpack must parse '
                                                    'every source file, construct an in-memory Abstract Syntax Tree '
                                                    '(AST) module graph, and bundle everything into memory before the '
                                                    'dev server can start, scaling O(N) with codebase size',
                                                    'Granular Hot Module Replacement (HMR): When a file changes, Vite '
                                                    'invalidates only that specific module in its module graph and '
                                                    'pushes an update over WebSockets; the browser re-fetches only '
                                                    'that single module, updating state instantly without page '
                                                    'reloads']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'Vite is an AI coding assistant that writes JavaScript for you. It is '
                                              'faster than Webpack because Vite deletes all node_modules before '
                                              'starting. Hot Module Replacement means replacing broken CPU chips on '
                                              'the server while the website is running.',
                               'missing_concepts': ['Traditional bundler (Webpack) dev bottleneck: Webpack must parse '
                                                    'every source file, construct an in-memory Abstract Syntax Tree '
                                                    '(AST) module graph, and bundle everything into memory before the '
                                                    'dev server can start, scaling O(N) with codebase size',
                                                    "Vite's unbundled native ESM dev server: Vite serves source code "
                                                    "over native browser ES Modules (<script type='module'>); the dev "
                                                    'server starts in O(1) instant time without pre-bundling user code',
                                                    'On-demand compilation via esbuild: When the browser requests an '
                                                    'imported module, Vite compiles that single file on the fly using '
                                                    'esbuild (written in Go, 10-100x faster than JS compilers); heavy '
                                                    'node_modules dependencies are pre-bundled once',
                                                    'Granular Hot Module Replacement (HMR): When a file changes, Vite '
                                                    'invalidates only that specific module in its module graph and '
                                                    'pushes an update over WebSockets; the browser re-fetches only '
                                                    'that single module, updating state instantly without page '
                                                    'reloads']}]},
          {'topic_tag': 'WebAssembly Integration & Memory Bridge',
           'question': 'How does WebAssembly execute compiled C++/Rust binaries at near-native speed, and how does '
                       'data pass across the JS linear memory bridge?',
           'keywords': ['WebAssembly',
                        'Wasm Binary',
                        'Linear Memory',
                        'JS WebAssembly Bridge',
                        'C++/Rust Compilation',
                        'Near-Native Speed'],
           'expected_concepts': ['WebAssembly architectural format: A low-level, binary bytecode format designed as an '
                                 'open W3C standard compilation target for C++, Rust, and Go, executing inside a '
                                 'sandboxed stack-based virtual machine at near-native speed',
                                 'Determinism and speed factors: Pre-compiled binary bytecode bypasses JavaScript '
                                 'parse/compile and JIT de-optimization phases, executing directly via hardware-mapped '
                                 'instructions with predictable memory layouts',
                                 'Linear memory bridge: WebAssembly does not directly access JS garbage-collected '
                                 'objects; it operates on a contiguous, resizable array of raw bytes represented as a '
                                 'WebAssembly.Memory instance wrapping an ArrayBuffer',
                                 'Data serialization across the FFI: Complex data (strings, structs, arrays) are '
                                 'transferred by passing pointer addresses (byte offsets) and lengths into linear '
                                 'memory; JavaScript decodes them using TypedArray views (Uint8Array) and TextDecoder, '
                                 'often automated via wasm-bindgen'],
           'model_answer': 'WebAssembly (Wasm) is an open W3C standard defining a portable, compact binary bytecode '
                           'format that executes at near-native speed (typically within 1.1x - 1.2x of native C/C++ '
                           'execution) inside browser engines: 1. Execution Speed & Predictability: JavaScript '
                           'execution in modern JIT engines involves multi-tiered compilation: source code parsing, '
                           'bytecode interpretation (Ignition), profile gathering, and speculative optimization '
                           '(TurboFan). If object shapes or types change dynamically, the JIT de-optimizes back to the '
                           'interpreter, causing unpredictable latency spikes. In contrast, WebAssembly is '
                           'pre-compiled ahead-of-time (AOT) from languages like Rust or C++ into compact binary '
                           "bytecode ('.wasm'). The browser validates and compiles Wasm into native machine code in a "
                           "single linear pass (often streaming compilation via 'WebAssembly.instantiateStreaming()') "
                           'with predictable memory layouts, structured control flow, and zero JIT de-optimizations. '
                           '2. The Linear Memory Bridge: WebAssembly executes inside a memory-safe sandbox and has no '
                           "direct access to the browser DOM or JavaScript's garbage-collected heap. Instead, "
                           "communication relies on 'Linear Memory'—a contiguous, resizable array of raw bytes "
                           "represented in JavaScript as an instance of 'WebAssembly.Memory' (wrapping an underlying "
                           'ArrayBuffer). Both the Wasm instance and JavaScript hold references to this identical '
                           'physical memory block. 3. Passing Data Across the FFI: WebAssembly functions natively '
                           'support only primitive numeric types: i32, i64, f32, and f64. Passing complex data '
                           'structures (strings, JSON objects, image pixel arrays) requires crossing the Foreign '
                           'Function Interface (FFI) via pointers: - Passing a String from JS to Wasm: JavaScript '
                           "encodes the string into UTF-8 bytes using 'TextEncoder', allocates memory inside Wasm (via "
                           "an exported malloc function), writes the bytes into Wasm's linear memory buffer using a "
                           "'Uint8Array' view, and passes the memory pointer (byte offset) and length (i32 integers) "
                           'to the Wasm function. - Returning Data: Wasm writes the result to linear memory and '
                           "returns a pointer/length; JS uses 'TextDecoder' to construct a JavaScript string. "
                           "High-level tools like 'wasm-bindgen' (Rust) automate this serialization choreography "
                           'seamlessly.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 97,
                               'answer_text': 'WebAssembly (Wasm) allows compiled languages like Rust and C++ to '
                                              'execute inside the browser at near-native speeds. The reason Wasm is so '
                                              'much faster and more predictable than JavaScript comes down to its '
                                              'format: JavaScript is a dynamic, interpreted language where the JIT '
                                              'compiler has to parse text, generate bytecode, profile types at '
                                              'runtime, optimize via TurboFan, and de-optimize when assumptions fail. '
                                              'WebAssembly is pre-compiled binary bytecode. The browser validates it '
                                              'in a single fast streaming pass (using '
                                              'WebAssembly.instantiateStreaming) and converts it directly into machine '
                                              'code with zero JIT de-optimization risk and strict memory layout. The '
                                              'core architectural challenge is the boundary between JavaScript and '
                                              'WebAssembly. Wasm runs in a secure sandbox and cannot touch '
                                              "JavaScript's garbage-collected heap or the DOM directly. It operates "
                                              "exclusively on 'Linear Memory'—a flat, contiguous block of bytes "
                                              "represented in JavaScript as a 'WebAssembly.Memory' object wrapping an "
                                              'ArrayBuffer. At the raw FFI level, Wasm functions only accept and '
                                              'return 32-bit and 64-bit integers and floats. If you want to pass a '
                                              'string or an image buffer from JS to Wasm, you have to use a memory '
                                              'bridge: JavaScript uses TextEncoder to turn the string into UTF-8 '
                                              "bytes, writes those bytes into Wasm's linear memory at a specific byte "
                                              'offset pointer, and calls the Wasm function passing that pointer '
                                              'address and byte length as integers. When Wasm finishes, it returns a '
                                              'pointer to the result in linear memory, which JS reads using a '
                                              'Uint8Array view and TextDecoder. Tools like wasm-bindgen in Rust '
                                              "generate this glue code automatically so you don't have to manage raw "
                                              'pointers manually.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'WebAssembly executes compiled C++ and Rust code at near-native speeds '
                                              "because it is a binary bytecode format that bypasses JavaScript's "
                                              'parsing and JIT de-optimization phases. The browser can compile Wasm '
                                              'binary directly into machine code. WebAssembly does not have direct '
                                              'access to JavaScript objects or the DOM; instead, it uses Linear '
                                              'Memory, which is a shared ArrayBuffer. To pass strings or complex data, '
                                              'JavaScript writes the data into linear memory using TypedArray views, '
                                              'passes the memory pointer and length to the Wasm function, and reads '
                                              'back the result from that memory address.',
                               'missing_concepts': ['Data serialization across the FFI: Complex data (strings, '
                                                    'structs, arrays) are transferred by passing pointer addresses '
                                                    '(byte offsets) and lengths into linear memory; JavaScript decodes '
                                                    'them using TypedArray views (Uint8Array) and TextDecoder, often '
                                                    'automated via wasm-bindgen']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'WebAssembly lets you run C++ and Rust code inside web browsers. It runs '
                                              'faster than JavaScript because it is compiled into binary bytecode '
                                              'before running. JavaScript and WebAssembly share memory using a linear '
                                              'memory buffer which is an ArrayBuffer. To pass data like strings '
                                              'between JS and Wasm, you write the bytes to linear memory and pass the '
                                              'memory address. This is used for heavy tasks like game engines, video '
                                              'editing in Figma, and cryptography.',
                               'missing_concepts': ['Determinism and speed factors: Pre-compiled binary bytecode '
                                                    'bypasses JavaScript parse/compile and JIT de-optimization phases, '
                                                    'executing directly via hardware-mapped instructions with '
                                                    'predictable memory layouts',
                                                    'Data serialization across the FFI: Complex data (strings, '
                                                    'structs, arrays) are transferred by passing pointer addresses '
                                                    '(byte offsets) and lengths into linear memory; JavaScript decodes '
                                                    'them using TypedArray views (Uint8Array) and TextDecoder, often '
                                                    'automated via wasm-bindgen']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'WebAssembly is an assembly language created by Microsoft that replaces '
                                              'HTML and CSS. It executes at near-native speed because it disables the '
                                              "browser's security sandbox. Data is passed between JavaScript and Wasm "
                                              'using SQL database queries.',
                               'missing_concepts': ['WebAssembly architectural format: A low-level, binary bytecode '
                                                    'format designed as an open W3C standard compilation target for '
                                                    'C++, Rust, and Go, executing inside a sandboxed stack-based '
                                                    'virtual machine at near-native speed',
                                                    'Determinism and speed factors: Pre-compiled binary bytecode '
                                                    'bypasses JavaScript parse/compile and JIT de-optimization phases, '
                                                    'executing directly via hardware-mapped instructions with '
                                                    'predictable memory layouts',
                                                    'Linear memory bridge: WebAssembly does not directly access JS '
                                                    'garbage-collected objects; it operates on a contiguous, resizable '
                                                    'array of raw bytes represented as a WebAssembly.Memory instance '
                                                    'wrapping an ArrayBuffer',
                                                    'Data serialization across the FFI: Complex data (strings, '
                                                    'structs, arrays) are transferred by passing pointer addresses '
                                                    '(byte offsets) and lengths into linear memory; JavaScript decodes '
                                                    'them using TypedArray views (Uint8Array) and TextDecoder, often '
                                                    'automated via wasm-bindgen']}]},
          {'topic_tag': 'Core Web Vitals Deep Dive (LCP, INP, CLS)',
           'question': 'Analyze the technical factors that cause poor LCP, INP, and CLS scores, and detail specific '
                       'engineering fixes for each metric.',
           'keywords': ['Core Web Vitals',
                        'Largest Contentful Paint',
                        'Interaction to Next Paint',
                        'Cumulative Layout Shift',
                        'Performance Budget',
                        'Field Data'],
           'expected_concepts': ['Largest Contentful Paint (LCP <= 2.5s): Measures perceived loading speed of the '
                                 'largest visual element (hero image, video poster, text block); degraded by slow '
                                 'server TTFB, render-blocking CSS/JS, and unoptimized images; fixed by CDN edge '
                                 "caching, preloading hero assets (<link rel='preload' as='image'>), "
                                 "fetchpriority='high', and modern image formats (WebP/AVIF)",
                                 'Interaction to Next Paint (INP <= 200ms): Replaced FID in 2024 to measure overall '
                                 'page responsiveness across all clicks, taps, and keypresses; degraded by long tasks '
                                 '(>50ms) blocking the main thread during input handling; fixed by yielding to the '
                                 'main thread (scheduler.yield(), setTimeout), web workers for heavy math, and '
                                 'debouncing handlers',
                                 'Cumulative Layout Shift (CLS <= 0.1): Measures visual layout stability; caused by '
                                 'images, videos, or ads loading without explicit width/height or aspect-ratio '
                                 'attributes, injecting dynamic content above existing elements, or FOUT/FOIT font '
                                 'swapping; fixed by reserving dimensional bounding boxes (CSS aspect-ratio) and '
                                 'font-display: optional',
                                 'Lab data vs Field data: Lab tools (Lighthouse) simulate controlled conditions; '
                                 'Google search ranking and Core Web Vitals evaluate real-world 75th percentile field '
                                 'telemetry (Chrome User Experience Report - CrUX)'],
           'model_answer': "Google's Core Web Vitals are user-centric performance metrics evaluated at the 75th "
                           'percentile of real-world user field data (Chrome User Experience Report - CrUX) that '
                           'directly impact Google search rankings: 1. Largest Contentful Paint (LCP) - Target <= '
                           '2.5s: - Definition: Measures the time elapsed until the largest visible content element '
                           'within the initial viewport (typically a hero image, video thumbnail, or large heading '
                           'block) has finished rendering. - Root Causes: Slow server Time to First Byte (TTFB), '
                           "render-blocking external CSS/JS in '<head>', client-side render waterfalls, and "
                           'unoptimized high-resolution images. - Engineering Fixes: Preload the hero image using '
                           '\'<link rel="preload" as="image" href="hero.webp" fetchpriority="high">\'; optimize images '
                           "with modern formats (AVIF/WebP) and responsive 'srcset'; inline critical path CSS and "
                           "defer non-critical JavaScript ('defer' / 'async'); implement CDN edge caching to drive "
                           'TTFB under 200ms. 2. Interaction to Next Paint (INP) - Target <= 200ms: - Definition: '
                           'Formally replaced First Input Delay (FID) in March 2024. Measures page responsiveness '
                           'throughout the entire user session, capturing the longest latency between a user '
                           'interaction (click, tap, keypress) and the next rendered visual frame. - Root Causes: Long '
                           'JavaScript tasks (>50ms) monopolizing the main thread; massive React component re-renders '
                           'during input events; expensive synchronous event handlers. - Engineering Fixes: Break up '
                           "long tasks by yielding to the main thread via 'await scheduler.yield()' or "
                           "'setTimeout(..., 0)'; offload heavy computations (filtering, parsing) to Web Workers; "
                           "optimize framework rendering using React 18 'useTransition' or 'useDeferredValue' to "
                           'prevent blocking keystrokes. 3. Cumulative Layout Shift (CLS) - Target <= 0.1: - '
                           'Definition: Quantifies unexpected visual layout shifts that occur while reading or '
                           'interacting (e.g., clicking the wrong button because a banner banner popped in). - Root '
                           'Causes: Images and iframe ads inserted without explicit dimensional attributes; dynamic '
                           'DOM injections above existing content; Flash of Unstyled/Invisible Text (FOUT/FOIT) during '
                           "web font loading. - Engineering Fixes: Always declare explicit 'width' and 'height' "
                           "attributes or CSS 'aspect-ratio' on images and embeds; reserve bounding box containers for "
                           "dynamic banners; use 'font-display: optional' or 'font-display: swap' with font metric "
                           'overrides to prevent text reflow.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': "Core Web Vitals represent Google's user experience metrics, measured at "
                                              'the 75th percentile of real-world user telemetry via the Chrome User '
                                              'Experience Report (CrUX). Here is a technical breakdown of the three '
                                              'metrics: 1. Largest Contentful Paint (LCP <= 2.5s): Measures when the '
                                              'largest visual block in the viewport (hero image or big heading) is '
                                              'rendered. Poor LCP is caused by slow server response times (TTFB), '
                                              'render-blocking CSS/JS, and unoptimized images. Fixes: Use a global CDN '
                                              'to lower TTFB, inline critical CSS, defer non-critical scripts, and '
                                              'explicitly preload the hero image with \'<link rel="preload" as="image" '
                                              'href="hero.webp" fetchpriority="high">\' while converting images to '
                                              'AVIF/WebP with responsive srcsets. 2. Interaction to Next Paint (INP <= '
                                              '200ms): In March 2024, INP officially replaced FID. While FID only '
                                              'measured the first click, INP measures the worst interaction latency '
                                              "across the user's entire session—from click or keypress to the next "
                                              'visual paint. Poor INP is caused by long tasks (>50ms) monopolizing the '
                                              'main thread. Fixes: Break up long tasks by yielding control back to the '
                                              "main thread using modern 'scheduler.yield()' or setTimeout, move heavy "
                                              "computation to Web Workers, and use React 18's useTransition so "
                                              "expensive renders don't block user typing. 3. Cumulative Layout Shift "
                                              '(CLS <= 0.1): Measures unexpected visual jumping of content. It happens '
                                              'when images or ad banners load without dimensions, pushing text down '
                                              'while someone is reading. Fixes: Always provide explicit width and '
                                              'height attributes on <img> and <iframe> tags or use the CSS '
                                              "'aspect-ratio' property so the browser reserves space before the asset "
                                              "loads. Also, use 'font-display: optional' with font-metric overrides to "
                                              'prevent layout shifts when web fonts load.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': "Core Web Vitals are Google's metrics for real-world user experience. "
                                              'LCP measures how fast the largest visible element loads, which should '
                                              'be under 2.5 seconds. You fix it by preloading hero images with '
                                              "fetchpriority='high', using modern WebP formats, and caching HTML on a "
                                              'CDN. INP measures interaction latency across the entire visit, needing '
                                              'to be under 200ms. You fix it by breaking up long tasks that block the '
                                              'main thread and using Web Workers. CLS measures layout shifts and must '
                                              'be under 0.1. You fix CLS by setting width and height attributes or '
                                              "aspect-ratio on all images and ad containers so they don't push content "
                                              'down when loading.',
                               'missing_concepts': ['Lab data vs Field data: Lab tools (Lighthouse) simulate '
                                                    'controlled conditions; Google search ranking and Core Web Vitals '
                                                    'evaluate real-world 75th percentile field telemetry (Chrome User '
                                                    'Experience Report - CrUX)']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'Core Web Vitals are three performance metrics tracked by Google for SEO '
                                              'rankings. LCP is Largest Contentful Paint, which measures when the main '
                                              'image or text loads, fixed by optimizing images and using a CDN. INP is '
                                              'Interaction to Next Paint, which replaced FID to measure how fast the '
                                              'page responds when you click buttons, fixed by reducing JavaScript '
                                              'execution time. CLS is Cumulative Layout Shift, which measures if '
                                              'elements jump around on screen, fixed by adding width and height to '
                                              'images so space is reserved.',
                               'missing_concepts': ['Interaction to Next Paint (INP <= 200ms): Replaced FID in 2024 to '
                                                    'measure overall page responsiveness across all clicks, taps, and '
                                                    'keypresses; degraded by long tasks (>50ms) blocking the main '
                                                    'thread during input handling; fixed by yielding to the main '
                                                    'thread (scheduler.yield(), setTimeout), web workers for heavy '
                                                    'math, and debouncing handlers',
                                                    'Lab data vs Field data: Lab tools (Lighthouse) simulate '
                                                    'controlled conditions; Google search ranking and Core Web Vitals '
                                                    'evaluate real-world 75th percentile field telemetry (Chrome User '
                                                    'Experience Report - CrUX)']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'Core Web Vitals are health monitors that check the temperature of web '
                                              'hosting servers. LCP means Low CPU Processing. INP means Internet '
                                              'Network Protocol. CLS means Cascading Layout Sheets. You improve these '
                                              'scores by paying Google for search ads.',
                               'missing_concepts': ['Largest Contentful Paint (LCP <= 2.5s): Measures perceived '
                                                    'loading speed of the largest visual element (hero image, video '
                                                    'poster, text block); degraded by slow server TTFB, '
                                                    'render-blocking CSS/JS, and unoptimized images; fixed by CDN edge '
                                                    "caching, preloading hero assets (<link rel='preload' "
                                                    "as='image'>), fetchpriority='high', and modern image formats "
                                                    '(WebP/AVIF)',
                                                    'Interaction to Next Paint (INP <= 200ms): Replaced FID in 2024 to '
                                                    'measure overall page responsiveness across all clicks, taps, and '
                                                    'keypresses; degraded by long tasks (>50ms) blocking the main '
                                                    'thread during input handling; fixed by yielding to the main '
                                                    'thread (scheduler.yield(), setTimeout), web workers for heavy '
                                                    'math, and debouncing handlers',
                                                    'Cumulative Layout Shift (CLS <= 0.1): Measures visual layout '
                                                    'stability; caused by images, videos, or ads loading without '
                                                    'explicit width/height or aspect-ratio attributes, injecting '
                                                    'dynamic content above existing elements, or FOUT/FOIT font '
                                                    'swapping; fixed by reserving dimensional bounding boxes (CSS '
                                                    'aspect-ratio) and font-display: optional',
                                                    'Lab data vs Field data: Lab tools (Lighthouse) simulate '
                                                    'controlled conditions; Google search ranking and Core Web Vitals '
                                                    'evaluate real-world 75th percentile field telemetry (Chrome User '
                                                    'Experience Report - CrUX)']}]},
          {'topic_tag': 'Web Cryptography API Zero-Knowledge',
           'question': 'How can the Web Cryptography API implement end-to-end zero-knowledge client-side encryption '
                       'using SubtleCrypto?',
           'keywords': ['Web Cryptography API',
                        'SubtleCrypto',
                        'Client-Side Encryption',
                        'AES-GCM',
                        'Zero-Knowledge Architecture',
                        'Key Generation'],
           'expected_concepts': ['Zero-Knowledge security model: The backend server stores and routes only ciphertext; '
                                 'encryption keys are derived and held strictly on client devices, preventing '
                                 'server-side data compromise or insider snooping',
                                 'Key derivation via PBKDF2: window.crypto.subtle.deriveKey uses PBKDF2 or Argon2 with '
                                 'high iteration counts (>=100,000) and unique salt to derive symmetric encryption '
                                 'keys from user passphrases',
                                 'Symmetric encryption via AES-GCM: window.crypto.subtle.encrypt with AES-GCM (256-bit '
                                 'key) and cryptographically random 12-byte Initialization Vector (IV) provides '
                                 'authenticated encryption preventing ciphertext tampering',
                                 'Asymmetric key exchange for sharing: Uses RSA-OAEP or ECDH (Elliptic Curve '
                                 'Diffie-Hellman) to exchange symmetric data encryption keys (DEKs) between different '
                                 'users without revealing master keys'],
           'model_answer': 'In a Zero-Knowledge architecture (e.g., 1Password, Signal, ProtonMail), sensitive data is '
                           'encrypted on the client device before transmission, ensuring the backend server acts as a '
                           'blind data store possessing zero access to plaintext or encryption keys. The W3C Web '
                           "Cryptography API ('window.crypto.subtle') provides hardware-accelerated, "
                           'timing-attack-resistant cryptographic primitives directly in the browser: 1. Passphrase '
                           "Key Derivation (PBKDF2): The client must never transmit the user's raw master passphrase. "
                           "The browser uses 'crypto.subtle.importKey' to ingest the passphrase as raw key material, "
                           "and then calls 'crypto.subtle.deriveKey' using PBKDF2 (with HMAC-SHA-256, a minimum of "
                           '100,000 iterations, and a unique cryptographic salt obtained via '
                           "'crypto.getRandomValues(new Uint8Array(16))') to derive a 256-bit Key Encryption Key "
                           '(KEK). 2. Symmetric Data Encryption (AES-GCM): For encrypting documents or payloads: - '
                           'Generate a unique 12-byte Initialization Vector (IV) per encryption operation using '
                           "'crypto.getRandomValues(new Uint8Array(12))'. (Reusing an IV in AES-GCM fatally destroys "
                           'confidentiality). - Execute \'crypto.subtle.encrypt({ name: "AES-GCM", iv }, derivedKey, '
                           "plaintextBuffer)'. AES-GCM is an Authenticated Encryption with Associated Data (AEAD) "
                           'cipher: it produces both ciphertext and an authentication tag that detects any ciphertext '
                           'tampering. 3. Zero-Knowledge Key Exchange (ECDH / RSA-OAEP): When sharing encrypted data '
                           'between users, the client generates an ephemeral symmetric Data Encryption Key (DEK). The '
                           'data is encrypted with the DEK via AES-GCM. The DEK itself is encrypted using the '
                           "recipient's public key (via ECDH or RSA-OAEP) and stored on the server. The recipient "
                           'decrypts the DEK using their private key and subsequently decrypts the data payload, '
                           'preserving zero-knowledge guarantees end-to-end.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'Implementing a zero-knowledge architecture using the Web Cryptography '
                                              'API (window.crypto.subtle) means the backend server never sees the '
                                              'plaintext or the master encryption key—it only stores encrypted blobs. '
                                              'Here is the technical implementation using SubtleCrypto: 1. Key '
                                              "Derivation from User Password: You must never send the user's password "
                                              'to the server. Instead, you import the password as raw key material '
                                              "with 'crypto.subtle.importKey()'. Then you derive a 256-bit AES key "
                                              "using 'crypto.subtle.deriveKey()' with PBKDF2, using a unique "
                                              "cryptographic salt from 'crypto.getRandomValues()' and at least 100,000 "
                                              'iterations of SHA-256. This protects against brute-force attacks. 2. '
                                              'Symmetric Encryption with AES-GCM: To encrypt data, you generate a '
                                              'fresh 12-byte Initialization Vector (IV) for every single encryption '
                                              "operation using 'crypto.getRandomValues(new Uint8Array(12))'. Never "
                                              'reuse an IV with AES-GCM because it completely breaks the cipher. You '
                                              "then call 'crypto.subtle.encrypt({ name: 'AES-GCM', iv }, key, "
                                              "dataBuffer)'. AES-GCM is an authenticated cipher, so it generates an "
                                              "authentication tag that guarantees the data hasn't been tampered with. "
                                              '3. Storing and Sharing: The client sends the ciphertext, salt, and IV '
                                              'to the server. Because the server has no key, even a complete database '
                                              'breach leaks nothing. When sharing data between users, you generate a '
                                              'random Data Encryption Key (DEK) for the document, encrypt the document '
                                              "with the DEK, and then encrypt that DEK with the recipient's public key "
                                              'using ECDH or RSA-OAEP, preserving zero-knowledge guarantees across '
                                              'multiple users.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'Zero-knowledge encryption means the server only receives and stores '
                                              'encrypted ciphertext and has no ability to decrypt it. Using the Web '
                                              "Cryptography API's SubtleCrypto, you derive an encryption key on the "
                                              "client side from the user's master password using PBKDF2 with a salt "
                                              'and 100,000 iterations of SHA-256. Then, you encrypt the data using '
                                              'AES-GCM 256-bit with a unique random initialization vector (IV) '
                                              'generated with crypto.getRandomValues. The client sends the ciphertext, '
                                              'IV, and salt to the backend. Because the encryption happens entirely in '
                                              'the browser using SubtleCrypto, the server never sees the plaintext or '
                                              'key.',
                               'missing_concepts': ['Asymmetric key exchange for sharing: Uses RSA-OAEP or ECDH '
                                                    '(Elliptic Curve Diffie-Hellman) to exchange symmetric data '
                                                    'encryption keys (DEKs) between different users without revealing '
                                                    'master keys']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': "Zero-knowledge architecture means the server doesn't know the user's "
                                              'password or data. You use window.crypto.subtle to do client-side '
                                              'encryption in the browser before making an API call. You take the '
                                              "user's password, use PBKDF2 to create an AES-GCM key, and encrypt the "
                                              'text. Then you send the encrypted string to the database. The server '
                                              'cannot read the data, so even if the database is hacked, user data is '
                                              'safe.',
                               'missing_concepts': ['Symmetric encryption via AES-GCM: window.crypto.subtle.encrypt '
                                                    'with AES-GCM (256-bit key) and cryptographically random 12-byte '
                                                    'Initialization Vector (IV) provides authenticated encryption '
                                                    'preventing ciphertext tampering',
                                                    'Asymmetric key exchange for sharing: Uses RSA-OAEP or ECDH '
                                                    '(Elliptic Curve Diffie-Hellman) to exchange symmetric data '
                                                    'encryption keys (DEKs) between different users without revealing '
                                                    'master keys']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'Zero-knowledge encryption means the web browser uses zero megabytes of '
                                              'RAM. SubtleCrypto is a third-party jQuery plugin. You encrypt data by '
                                              'converting characters to Base64 and sending the Base64 string over '
                                              'plain HTTP.',
                               'missing_concepts': ['Zero-Knowledge security model: The backend server stores and '
                                                    'routes only ciphertext; encryption keys are derived and held '
                                                    'strictly on client devices, preventing server-side data '
                                                    'compromise or insider snooping',
                                                    'Key derivation via PBKDF2: window.crypto.subtle.deriveKey uses '
                                                    'PBKDF2 or Argon2 with high iteration counts (>=100,000) and '
                                                    'unique salt to derive symmetric encryption keys from user '
                                                    'passphrases',
                                                    'Symmetric encryption via AES-GCM: window.crypto.subtle.encrypt '
                                                    'with AES-GCM (256-bit key) and cryptographically random 12-byte '
                                                    'Initialization Vector (IV) provides authenticated encryption '
                                                    'preventing ciphertext tampering',
                                                    'Asymmetric key exchange for sharing: Uses RSA-OAEP or ECDH '
                                                    '(Elliptic Curve Diffie-Hellman) to exchange symmetric data '
                                                    'encryption keys (DEKs) between different users without revealing '
                                                    'master keys']}]},
          {'topic_tag': 'Microservices API Gateway & Circuit Breakers',
           'question': 'How does an API Gateway integrate with Circuit Breakers to prevent cascading failures across '
                       'microservice clusters?',
           'keywords': ['API Gateway',
                        'Rate Limiting',
                        'Circuit Breaker Pattern',
                        'Hystrix/Resilience4j',
                        'Service Mesh',
                        'Reverse Proxy'],
           'expected_concepts': ['API Gateway core responsibilities: Acts as single reverse proxy entry point for all '
                                 'client traffic, handling route discovery, SSL termination, rate limiting, and '
                                 'centralized authentication',
                                 'Cascading failure problem: When a downstream microservice hangs or fails, upstream '
                                 'caller threads block waiting for timeouts, exhausting thread pools and socket '
                                 'connections across the entire cluster',
                                 'Circuit Breaker three-state finite state machine: 1. Closed (normal operation; '
                                 'tracks failure rate); 2. Open (failure threshold exceeded; trips open, fails fast '
                                 'immediately without forwarding requests); 3. Half-Open (after sleep cooldown, allows '
                                 'canary trial requests; resets to Closed on success or trips back to Open on failure)',
                                 'Fallback mechanisms and resiliency: Circuit breakers return degraded fallback data '
                                 '(cached responses or graceful empty sets), isolating failures to protect cluster '
                                 'health'],
           'model_answer': 'In microservice architectures, an API Gateway (e.g., Kong, Envoy, Zuul) serves as the '
                           'centralized reverse proxy and entry point for all incoming client traffic. It manages '
                           'authentication, SSL termination, request routing, and rate limiting. However, in '
                           'distributed topologies, a failure in a single deep dependency (e.g., an inventory '
                           "microservice experiencing database lockups) can trigger a catastrophic 'cascading "
                           "failure': upstream services block their worker threads waiting for network timeouts. "
                           'Within seconds, thread pools, file descriptors, and socket buffers across the entire '
                           'cluster are exhausted, bringing down completely unrelated services. Integrating the '
                           'Circuit Breaker Pattern (formalized by Michael Nygard and implemented in libraries like '
                           'Resilience4j and Envoy) prevents cascading collapse through a three-state finite state '
                           'machine: 1. Closed State: Normal operation. Requests pass through to downstream services. '
                           'The circuit breaker continuously monitors request volume, error percentages (5xx status '
                           'codes), and latency timeouts over a rolling statistical sliding window. 2. Open State: If '
                           'the failure rate breaches a configured threshold (e.g., >50% failures over 10 seconds), '
                           "the circuit breaker 'trips' into the Open state. For the duration of a configured sleep "
                           'window (e.g., 30 seconds), the API Gateway immediately rejects incoming requests to that '
                           "service without forwarding any network traffic ('fail-fast'). This shields the struggling "
                           'downstream service, allowing its CPU, database, and connection pools to recover. '
                           'Concurrently, the gateway returns a predefined Fallback response (e.g., serving cached '
                           'recommendations or an empty search list) rather than throwing a 500 error to the client. '
                           '3. Half-Open State: When the sleep window expires, the breaker transitions to Half-Open. '
                           "It permits a limited number of 'canary' probe requests to pass through. If all canary "
                           'requests succeed, the breaker resets to Closed and resumes normal traffic. If any canary '
                           'fails, it trips back to Open for another cooldown period.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'An API Gateway serves as the single reverse-proxy entry point for '
                                              'client traffic, handling routing, auth token validation, rate limiting, '
                                              'and SSL termination. In a microservices cluster, the greatest danger is '
                                              'cascading failures: if Service C hangs due to a database deadlock, '
                                              "Service B's worker threads block waiting for Service C's timeout. Soon "
                                              'Service B exhausts its thread pool and crashes, which cascades to '
                                              "Service A and the API Gateway, bringing down the entire company's "
                                              'infrastructure. We solve this by implementing Circuit Breakers (using '
                                              'tools like Resilience4j, Envoy, or Kong). A Circuit Breaker is a state '
                                              'machine with three states: 1. Closed: Normal operation. All requests '
                                              'pass through to the downstream service. The breaker monitors error '
                                              'rates and timeouts over a rolling window. 2. Open: If the error rate '
                                              'crosses a threshold—say, 50% failures over a 10-second window—the '
                                              'circuit trips Open. For a configured cooldown period (like 30 seconds), '
                                              'the API Gateway completely stops sending requests to that service. It '
                                              "immediately 'fails fast' without opening network sockets, giving the "
                                              'failing service room to recover and restart. The gateway can also '
                                              'return an immediate graceful fallback, like cached product data or a '
                                              'default UI message. 3. Half-Open: After the cooldown timer expires, the '
                                              'breaker enters Half-Open. It allows a small batch of canary requests to '
                                              'go through. If they succeed, it resets to Closed and resumes full '
                                              'traffic. If they fail, it trips back to Open. This protects thread '
                                              'pools and isolates faults completely.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'An API Gateway handles routing, authentication, and rate limiting for '
                                              'microservices. When a downstream service fails, it can cause cascading '
                                              'failures where upstream services run out of threads waiting for '
                                              'timeouts. Circuit breakers prevent this by monitoring error rates. When '
                                              'errors exceed a threshold, the circuit breaker opens and immediately '
                                              'fails fast without calling the downstream service, protecting the '
                                              'cluster. After a cooldown, it goes to Half-Open to test canary '
                                              'requests, resetting to Closed if they succeed. The gateway can also '
                                              'return fallback responses like cached data.',
                               'missing_concepts': ['Cascading failure problem: When a downstream microservice hangs '
                                                    'or fails, upstream caller threads block waiting for timeouts, '
                                                    'exhausting thread pools and socket connections across the entire '
                                                    'cluster']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'An API gateway is a reverse proxy that directs client requests to '
                                              'different microservices. Circuit breakers are used to stop one failing '
                                              'service from crashing the whole system. A circuit breaker has three '
                                              'states: closed, open, and half-open. When a service is returning too '
                                              'many errors, the circuit trips open and returns an error immediately or '
                                              'returns cached data. Later it tries again in half-open state. This '
                                              'prevents server crashes.',
                               'missing_concepts': ['API Gateway core responsibilities: Acts as single reverse proxy '
                                                    'entry point for all client traffic, handling route discovery, SSL '
                                                    'termination, rate limiting, and centralized authentication',
                                                    'Cascading failure problem: When a downstream microservice hangs '
                                                    'or fails, upstream caller threads block waiting for timeouts, '
                                                    'exhausting thread pools and socket connections across the entire '
                                                    'cluster']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'An API Gateway is a physical router installed in the server rack. A '
                                              "circuit breaker is an electrical switch that shuts off the building's "
                                              'electricity if the server gets too hot. Cascading failure is when a '
                                              'server falls off the shelf and breaks other servers.',
                               'missing_concepts': ['API Gateway core responsibilities: Acts as single reverse proxy '
                                                    'entry point for all client traffic, handling route discovery, SSL '
                                                    'termination, rate limiting, and centralized authentication',
                                                    'Cascading failure problem: When a downstream microservice hangs '
                                                    'or fails, upstream caller threads block waiting for timeouts, '
                                                    'exhausting thread pools and socket connections across the entire '
                                                    'cluster',
                                                    'Circuit Breaker three-state finite state machine: 1. Closed '
                                                    '(normal operation; tracks failure rate); 2. Open (failure '
                                                    'threshold exceeded; trips open, fails fast immediately without '
                                                    'forwarding requests); 3. Half-Open (after sleep cooldown, allows '
                                                    'canary trial requests; resets to Closed on success or trips back '
                                                    'to Open on failure)',
                                                    'Fallback mechanisms and resiliency: Circuit breakers return '
                                                    'degraded fallback data (cached responses or graceful empty sets), '
                                                    'isolating failures to protect cluster health']}]},
          {'topic_tag': 'CDN Edge Computing & Edge SSR',
           'question': 'How do Edge Workers execute serverless code at CDN edge locations to achieve ultra-low latency '
                       'Edge SSR?',
           'keywords': ['Edge Computing',
                        'Cloudflare Workers',
                        'Edge SSR',
                        'Global Latency',
                        'Vary Headers',
                        'Stale-While-Revalidate'],
           'expected_concepts': ['Edge computing architecture: Deploys serverless compute to hundreds of globally '
                                 'distributed CDN Point-of-Presence (PoP) locations within 10-50ms of users, rather '
                                 'than routing all requests to a centralized origin data center (e.g. us-east-1)',
                                 'V8 Isolates vs Docker containers: Edge platforms (Cloudflare Workers, Fastly '
                                 'Compute, Vercel Edge) use lightweight V8 isolates running in a shared process, '
                                 'achieving sub-millisecond cold starts (~5ms) and tiny memory footprints compared to '
                                 'heavy Node/Docker containers',
                                 'Edge SSR mechanics: HTML rendering (React SSR, SvelteKit) executes directly at the '
                                 'edge PoP, fetching localized data from edge KV/D1/Redis stores and streaming HTML to '
                                 'the user with near-zero TTFB',
                                 'Edge caching coordination: Leverages Cache-Control with stale-while-revalidate and '
                                 'surrogate-keys to serve cached HTML instantly while refreshing in the background at '
                                 'the edge'],
           'model_answer': 'Traditional Server-Side Rendering (SSR) executes in centralized cloud data centers (e.g., '
                           "AWS 'us-east-1'). When a user in Sydney or Tokyo accesses a website, their HTTP request "
                           'must travel halfway around the globe through multiple fiber hops, incurring 200ms+ '
                           'round-trip latency (RTT) before the server even begins rendering the page. Edge Computing '
                           'and Edge SSR resolve this geographic latency bottleneck by relocating compute directly to '
                           'the network perimeter: 1. The CDN Edge Architecture: Modern edge platforms (Cloudflare '
                           'Workers, Fastly Compute@Edge, Vercel Edge Runtime) run code inside hundreds of distributed '
                           'CDN Points of Presence (PoPs) worldwide, placing execution within 10-30 milliseconds of '
                           "95% of the world's population. 2. V8 Isolates vs Containers: Traditional serverless "
                           'functions (like AWS Lambda) spin up individual Linux microVMs or Docker containers. This '
                           'architecture causes heavy cold starts (200ms to 2 seconds) and large memory footprints. '
                           "Edge workers operate using Google V8 'Isolates'—the same security boundary Chrome uses to "
                           'isolate browser tabs. Hundreds of thousands of isolated V8 contexts run concurrently '
                           'within a single shared native process. Starting a V8 isolate takes under 5 milliseconds '
                           'with near-zero cold start overhead. 3. Edge SSR Execution: In Edge SSR (supported by '
                           'Next.js App Router, Remix, and SvelteKit), the entire component rendering pipeline '
                           "executes right at the user's nearest edge PoP. The edge worker receives the request, "
                           'queries low-latency distributed edge data stores (e.g., Cloudflare D1, KV, Upstash Redis), '
                           'and begins streaming the rendered HTML response via chunked transfer encoding '
                           "('Transfer-Encoding: chunked'). 4. Edge Caching Synergy: Edge workers intercept and "
                           "coordinate caching at the edge using 'Cache-Control: s-maxage=60, "
                           "stale-while-revalidate=600' and cache tagging. The edge PoP serves cached HTML instantly "
                           'to visitors while background workers fetch and re-render dynamic content, achieving '
                           'sub-50ms global TTFB.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'Traditional SSR runs in centralized cloud data centers, like AWS '
                                              'us-east-1. If a user in Tokyo visits your site, their request travels '
                                              'thousands of miles across the Pacific, adding 150ms to 200ms of pure '
                                              'speed-of-light network latency before your server even starts rendering '
                                              'HTML. Edge Computing and Edge SSR solve this by moving execution '
                                              "directly to the CDN's global Point of Presence (PoP) edge "
                                              'servers—meaning code runs within 10ms to 30ms of the user, whether they '
                                              'are in Tokyo, London, or New York. The technical breakthrough that '
                                              'makes Edge SSR practical is V8 Isolates. Traditional serverless '
                                              'platforms like AWS Lambda spin up Docker containers or Firecracker '
                                              'microVMs, which take hundreds of milliseconds to boot (cold starts) and '
                                              'consume lots of memory. Edge platforms like Cloudflare Workers and '
                                              "Vercel Edge Runtime don't use containers—they run lightweight V8 "
                                              'Isolates inside a single shared process, the exact same sandboxing '
                                              'mechanism Chrome uses to isolate browser tabs. A V8 isolate starts in '
                                              'under 5 milliseconds with almost zero cold start penalty. In an Edge '
                                              'SSR setup with Next.js or Remix, the edge server renders the React '
                                              'component tree into an HTML stream right at the edge, pulls data from '
                                              'low-latency edge databases like Cloudflare D1 or Upstash Redis, and '
                                              'streams the HTML to the user with sub-50ms Time to First Byte (TTFB). '
                                              'Combined with edge caching directives like stale-while-revalidate, it '
                                              'gives you the speed of static CDN hosting with the power of dynamic '
                                              'server rendering.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'Edge SSR executes server-side rendering code at CDN edge locations '
                                              'close to the user rather than in a single centralized data center, '
                                              'drastically reducing network latency and TTFB worldwide. Platforms like '
                                              'Cloudflare Workers and Vercel Edge use V8 isolates instead of heavy '
                                              'Docker containers, which eliminates cold starts and allows code to boot '
                                              'in under 5 milliseconds. The edge worker renders the HTML dynamically '
                                              'and streams it to the user while using edge KV stores for data and '
                                              'stale-while-revalidate caching to keep responses fast.',
                               'missing_concepts': ['Edge computing architecture: Deploys serverless compute to '
                                                    'hundreds of globally distributed CDN Point-of-Presence (PoP) '
                                                    'locations within 10-50ms of users, rather than routing all '
                                                    'requests to a centralized origin data center (e.g. us-east-1)']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'Edge SSR is server-side rendering that runs on CDN edge servers like '
                                              'Cloudflare Workers instead of an AWS origin server. This makes websites '
                                              'load much faster because the server is geographically closer to the '
                                              'user. Edge workers use V8 isolates which start instantly without the '
                                              'cold start delays of normal serverless functions. It renders the HTML '
                                              'at the edge and caches it so users get fast page loads anywhere in the '
                                              'world.',
                               'missing_concepts': ['V8 Isolates vs Docker containers: Edge platforms (Cloudflare '
                                                    'Workers, Fastly Compute, Vercel Edge) use lightweight V8 isolates '
                                                    'running in a shared process, achieving sub-millisecond cold '
                                                    'starts (~5ms) and tiny memory footprints compared to heavy '
                                                    'Node/Docker containers',
                                                    'Edge caching coordination: Leverages Cache-Control with '
                                                    'stale-while-revalidate and surrogate-keys to serve cached HTML '
                                                    'instantly while refreshing in the background at the edge']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'Edge computing means running JavaScript inside the Microsoft Edge web '
                                              'browser. Edge SSR downloads all server database tables into the '
                                              "browser's local cache. It eliminates cold starts by keeping the user's "
                                              'laptop fan running constantly.',
                               'missing_concepts': ['Edge computing architecture: Deploys serverless compute to '
                                                    'hundreds of globally distributed CDN Point-of-Presence (PoP) '
                                                    'locations within 10-50ms of users, rather than routing all '
                                                    'requests to a centralized origin data center (e.g. us-east-1)',
                                                    'V8 Isolates vs Docker containers: Edge platforms (Cloudflare '
                                                    'Workers, Fastly Compute, Vercel Edge) use lightweight V8 isolates '
                                                    'running in a shared process, achieving sub-millisecond cold '
                                                    'starts (~5ms) and tiny memory footprints compared to heavy '
                                                    'Node/Docker containers',
                                                    'Edge SSR mechanics: HTML rendering (React SSR, SvelteKit) '
                                                    'executes directly at the edge PoP, fetching localized data from '
                                                    'edge KV/D1/Redis stores and streaming HTML to the user with '
                                                    'near-zero TTFB',
                                                    'Edge caching coordination: Leverages Cache-Control with '
                                                    'stale-while-revalidate and surrogate-keys to serve cached HTML '
                                                    'instantly while refreshing in the background at the edge']}]},
          {'topic_tag': 'Serverless Cold Start Mitigation',
           'question': 'What causes serverless cold starts in AWS Lambda/Vercel functions, and how can architecture '
                       'patterns mitigate them?',
           'keywords': ['Serverless',
                        'Cold Start',
                        'Execution Context Reuse',
                        'Provisioned Concurrency',
                        'Function Size',
                        'Stateless Functions'],
           'expected_concepts': ['Cold start anatomy: Occurs when an incoming request hits an un-initialized '
                                 'serverless worker, requiring the cloud provider to download the code package, spin '
                                 'up a microVM/container (Firecracker), initialize the runtime (Node.js/Python), and '
                                 'execute top-level initialization code',
                                 'Root causes of high cold start latency: Large deployment bundle size, heavy '
                                 'dependencies (e.g., loading huge SDKs or ORMs), VPC attachment overhead (ENI '
                                 'creation), and excessive top-level database connections',
                                 'Architectural mitigation strategies: Tree-shaking and bundling with esbuild to '
                                 'minimize bundle size; lazy loading heavy modules inside the handler; moving database '
                                 'connections and SDK clients to global scope for execution context reuse',
                                 'Cloud provider solutions: Provisioned Concurrency (AWS keeps pre-initialized '
                                 'execution environments warm 24/7 at fixed cost) and switching to lightweight Edge '
                                 'runtimes (V8 isolates)'],
           'model_answer': 'In serverless computing (e.g., AWS Lambda, Google Cloud Functions, Vercel Serverless), '
                           'instances scale dynamically from zero to thousands based on traffic. While this provides '
                           "optimal cost efficiency and elasticity, it introduces the 'cold start' latency penalty: 1. "
                           'Anatomy of a Cold Start: When a request arrives and no idle container is available, the '
                           'cloud platform must: - Step 1: Provision a microVM or container (e.g., AWS Firecracker). - '
                           'Step 2: Download the zipped code artifact from S3. - Step 3: Boot the runtime environment '
                           '(Node.js, Python, or JVM). - Step 4: Execute top-level / global module code (importing '
                           'libraries, initializing SDKs, establishing DB pools). Only after Steps 1-4 finish does the '
                           'platform invoke the actual handler function. This initialization latency adds 200ms to '
                           'over 5 seconds to the request. Subsequent requests hitting that active container '
                           "experience a 'warm start' (<10ms) by reusing the existing execution context. 2. Primary "
                           "Causes of Severe Cold Starts: - Giant bundle sizes containing bloated 'node_modules'. - "
                           'Initializing heavy ORMs (like Prisma) or large AWS SDK bundles synchronously at the global '
                           'level. - VPC Attachment: Placing Lambda inside a private VPC historically required dynamic '
                           'Elastic Network Interface (ENI) provisioning, adding multi-second latency (though '
                           'mitigated by AWS Hyperplane). 3. Architectural Mitigation Strategies: - Tree Shaking & '
                           'Minification: Use esbuild or Rollup to bundle only required code, stripping unused '
                           'dependencies and reducing zip packages from 50MB down to <2MB. - Execution Context Reuse: '
                           'Initialize database clients (e.g., Prisma, MongoDB client) and AWS SDK clients in the '
                           'global scope OUTSIDE the handler function. During warm starts, global variables remain in '
                           'memory, allowing instant reuse of open TCP connection pools. - Lazy Loading: Dynamically '
                           'import heavy libraries inside conditional branches (\'await import("heavy-lib")\') so they '
                           "are only initialized when actually executed. - Cloud Solutions: Use AWS 'Provisioned "
                           "Concurrency' to maintain a pool of permanently warm, pre-initialized containers for "
                           'latency-critical API routes.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'A serverless cold start occurs when an incoming request arrives and the '
                                              "cloud provider doesn't have an existing container ready to process it. "
                                              'The platform has to: 1. Download your code package from storage, 2. '
                                              'Provision a new microVM or container (like AWS Firecracker), 3. '
                                              'Initialize the language runtime (like booting Node.js), and 4. Execute '
                                              'all global code outside the handler (importing npm packages, parsing '
                                              'config, and setting up clients). Only then can your handler execute. '
                                              'This initial setup can add anywhere from 200ms to 3+ seconds of '
                                              'latency. Subsequent requests that hit the active container reuse the '
                                              "execution context and experience a 'warm start' in under 10ms. The main "
                                              'culprits behind long cold starts are huge bundle sizes with unbundled '
                                              'node_modules, synchronous initialization of heavy ORMs or SDKs, and '
                                              'JVM/Java runtimes. We mitigate cold starts through several key '
                                              'engineering practices: 1. Bundle optimization: Use bundlers like '
                                              'esbuild to tree-shake and minify your lambda code, stripping unneeded '
                                              'dependencies and keeping the artifact under a few megabytes. 2. '
                                              'Execution context reuse: Initialize database connection pools and SDK '
                                              'clients in the global scope OUTSIDE the handler function. That way, on '
                                              'warm invocations, the function reuses the existing open database '
                                              'sockets without reconnecting. 3. Lazy loading: If you have an expensive '
                                              "module that's only used in one specific if-branch, dynamically import "
                                              "it with 'await import()' inside the handler rather than at the top of "
                                              'the file. 4. Provisioned Concurrency: For mission-critical endpoints '
                                              '(like checkout APIs), you can configure AWS Provisioned Concurrency to '
                                              'keep a set number of execution environments pre-warmed 24/7.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'A cold start happens in serverless when a new container must be spun up '
                                              'because no idle instances exist. The cloud provider has to provision '
                                              'the microVM, start the Node.js runtime, download the code, and execute '
                                              'all top-level imports before the handler function can run, adding '
                                              'latency to the request. You can mitigate cold starts by bundling and '
                                              'tree-shaking your code with esbuild to keep package sizes small, '
                                              'lazy-loading heavy libraries inside the handler, and defining database '
                                              'connection pools outside the handler so warm starts reuse open sockets. '
                                              'You can also use AWS Provisioned Concurrency to keep instances '
                                              'permanently warm.',
                               'missing_concepts': ['Root causes of high cold start latency: Large deployment bundle '
                                                    'size, heavy dependencies (e.g., loading huge SDKs or ORMs), VPC '
                                                    'attachment overhead (ENI creation), and excessive top-level '
                                                    'database connections']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'Cold start is the delay when a serverless function like AWS Lambda runs '
                                              'for the first time after being idle. The server has to start up a new '
                                              'virtual container and load your code into memory, which makes the first '
                                              'API call slow. To fix it, you should keep your code bundle small using '
                                              'Webpack or esbuild, avoid importing unnecessary npm packages, and put '
                                              'your database connections outside the main handler so they can be '
                                              'reused. AWS also has provisioned concurrency to keep functions warm.',
                               'missing_concepts': ['Cold start anatomy: Occurs when an incoming request hits an '
                                                    'un-initialized serverless worker, requiring the cloud provider to '
                                                    'download the code package, spin up a microVM/container '
                                                    '(Firecracker), initialize the runtime (Node.js/Python), and '
                                                    'execute top-level initialization code',
                                                    'Root causes of high cold start latency: Large deployment bundle '
                                                    'size, heavy dependencies (e.g., loading huge SDKs or ORMs), VPC '
                                                    'attachment overhead (ENI creation), and excessive top-level '
                                                    'database connections']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'Cold starts happen when the server room temperature drops below 0 '
                                              'degrees Celsius in the winter. You mitigate cold starts by setting up a '
                                              'cron job that sends ping requests to the server every millisecond. '
                                              'Serverless functions run on bare metal computers without '
                                              'virtualization.',
                               'missing_concepts': ['Cold start anatomy: Occurs when an incoming request hits an '
                                                    'un-initialized serverless worker, requiring the cloud provider to '
                                                    'download the code package, spin up a microVM/container '
                                                    '(Firecracker), initialize the runtime (Node.js/Python), and '
                                                    'execute top-level initialization code',
                                                    'Root causes of high cold start latency: Large deployment bundle '
                                                    'size, heavy dependencies (e.g., loading huge SDKs or ORMs), VPC '
                                                    'attachment overhead (ENI creation), and excessive top-level '
                                                    'database connections',
                                                    'Architectural mitigation strategies: Tree-shaking and bundling '
                                                    'with esbuild to minimize bundle size; lazy loading heavy modules '
                                                    'inside the handler; moving database connections and SDK clients '
                                                    'to global scope for execution context reuse',
                                                    'Cloud provider solutions: Provisioned Concurrency (AWS keeps '
                                                    'pre-initialized execution environments warm 24/7 at fixed cost) '
                                                    'and switching to lightweight Edge runtimes (V8 isolates)']}]},
          {'topic_tag': 'GraphQL DataLoader N+1 Solution',
           'question': 'Explain the GraphQL N+1 query problem and derive the batching/caching mechanics of the '
                       'DataLoader pattern.',
           'keywords': ['GraphQL N+1 Problem',
                        'DataLoader',
                        'Batching Requests',
                        'Caching per Request',
                        'Query Complexity',
                        'Resolver Tree'],
           'expected_concepts': ['Root cause of N+1 problem: GraphQL resolver functions execute independently and '
                                 'naively per field; fetching a list of N authors and their books results in 1 query '
                                 "for authors followed by N separate queries for each author's books (1 + N queries), "
                                 'overwhelming databases',
                                 'DataLoader core mechanism: Developed by Facebook to solve N+1 queries through two '
                                 'primary features: Batching (coalescing multiple load calls into a single batched '
                                 'operation) and Caching (per-request memoization)',
                                 'Event Loop microtask batching trick: When loader.load(key) is invoked in individual '
                                 'resolvers, it queues the key into a batch array and returns a pending Promise; on '
                                 'the next tick (microtask drain via process.nextTick / Promise.resolve), the batch '
                                 "function executes a single SQL query ('SELECT * FROM books WHERE author_id IN "
                                 "(...)')",
                                 'Request-scoped caching: DataLoader caches loaded instances by key within a single '
                                 'HTTP request context, preventing duplicate queries if multiple parts of the GraphQL '
                                 'tree request the identical entity'],
           'model_answer': 'In GraphQL, the flexibility of nesting relational queries creates a notorious database '
                           'performance anti-pattern known as the N+1 Query Problem: 1. The Anatomy of the N+1 '
                           'Problem: GraphQL executes queries via a recursive resolver tree. Consider a query fetching '
                           "100 recent blog posts and their authors: 'query { posts { id title author { name } } }'. - "
                           "First, the root resolver 'Query.posts' runs a single database query: 'SELECT * FROM posts "
                           "LIMIT 100' (1 query). - Then, for each of the 100 returned post objects, the field "
                           "resolver 'Post.author' is invoked independently. If written naively: 'author: (post) => "
                           "db.getAuthor(post.authorId)'. - The database receives 100 individual queries: 'SELECT * "
                           "FROM authors WHERE id = 1', 'SELECT * FROM authors WHERE id = 2', etc. - Total queries "
                           'executed: 1 + 100 = 101 queries (N + 1). For nested structures (posts -> authors -> '
                           'comments -> users), queries grow exponentially, crippling relational databases. 2. The '
                           'DataLoader Solution (Batching & Caching): Created by Lee Byron at Facebook, DataLoader '
                           'resolves this by intercepting and batching load requests using the JavaScript Event Loop: '
                           "- Step 1 (Queueing Keys): When 'authorLoader.load(post.authorId)' is called inside a "
                           "resolver, DataLoader adds 'post.authorId' to an internal batch queue and returns an "
                           'unresolved Promise. It does NOT hit the database immediately. - Step 2 (Microtask '
                           "Batching): DataLoader leverages the JavaScript Event Loop's microtask queue (via "
                           "'process.nextTick()' in Node or 'Promise.resolve()'). As synchronous resolver execution "
                           'finishes for all 100 posts within the current tick, DataLoader flushes the batch queue. - '
                           'Step 3 (Single Coalesced Query): DataLoader passes the unique deduplicated array of 100 '
                           "author IDs to a user-defined batch function: 'const authors = await db.authors.findMany({ "
                           "where: { id: { in: ids } } })'. This executes a single SQL query ('SELECT * FROM authors "
                           "WHERE id IN (...)'). - Step 4 (Resolution): The batch function returns an array of author "
                           'objects of the same length and in the exact same order as the requested IDs. DataLoader '
                           'resolves each pending Promise with its corresponding author. 3. Per-Request Caching: '
                           'DataLoader caches resolved values in an in-memory Map for the duration of a single GraphQL '
                           'request, ensuring the same author is never queried twice across the entire query tree.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 97,
                               'answer_text': 'The N+1 problem in GraphQL stems from the way GraphQL resolvers execute '
                                              "independently. Suppose you query for 50 posts and each post's author: "
                                              "'query { posts { title author { name } } }'. The root resolver runs one "
                                              "query: 'SELECT * FROM posts' (1 query). Then, for each of the 50 posts, "
                                              "the 'Post.author' field resolver runs separately: 'SELECT * FROM "
                                              "authors WHERE id = post.authorId'. That executes 50 individual database "
                                              "queries. 1 initial query plus 50 child queries equals 51 queries—that's "
                                              'the N+1 problem, and it will destroy database performance at scale. '
                                              'Facebook created DataLoader to solve this using two mechanisms: '
                                              'batching and request-scoped memoization. Here is the brilliant way '
                                              'batching works under the hood: When your resolver calls '
                                              "'authorLoader.load(post.authorId)', DataLoader doesn't execute a "
                                              'database query right away. Instead, it pushes the authorId into an '
                                              'internal array and returns an unresolved Promise. Because all 50 '
                                              'resolvers run synchronously in the same tick of the JavaScript event '
                                              'loop, DataLoader waits for the synchronous execution to finish. On the '
                                              'next tick—specifically when the microtask queue drains—DataLoader takes '
                                              'all 50 collected IDs, deduplicates them, and passes them to a batch '
                                              'function you define. Your batch function executes a single SQL query: '
                                              "'SELECT * FROM authors WHERE id IN (1, 2, 3...)'. DataLoader then maps "
                                              'each returned author back to its matching pending Promise and resolves '
                                              'them. Furthermore, DataLoader includes per-request caching: if five '
                                              'different posts share the same author ID, it only fetches that author '
                                              'once and reuses the cached object from an internal Map. DataLoader '
                                              'instances should always be created per-request in the GraphQL context '
                                              "so that cache data doesn't leak across different users.",
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'The N+1 problem happens in GraphQL because field resolvers execute '
                                              'independently. If you fetch 20 posts and their authors, it runs 1 query '
                                              'to get the posts, and then 20 individual queries to fetch the author '
                                              'for each post, making 21 queries total. DataLoader fixes this through '
                                              'batching and caching. When you call dataLoader.load(id), it buffers the '
                                              'IDs and returns a Promise. When the current tick of the event loop '
                                              'finishes, it calls your batch loading function with all the IDs at '
                                              "once, executing a single 'SELECT * FROM authors WHERE id IN (...)' "
                                              'query. It then resolves each Promise with the correct author object, '
                                              'turning N+1 queries into just 2 queries.',
                               'missing_concepts': ['Request-scoped caching: DataLoader caches loaded instances by key '
                                                    'within a single HTTP request context, preventing duplicate '
                                                    'queries if multiple parts of the GraphQL tree request the '
                                                    'identical entity']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'The N+1 problem is when GraphQL runs one query for a parent item and '
                                              'then runs N queries for each of its children in a loop, which overloads '
                                              'the database. DataLoader is a library from Facebook that fixes this by '
                                              'batching all the IDs together into a single SQL query using an IN '
                                              "clause. It also caches the results so you don't fetch the same data "
                                              'twice in the same request. This speeds up GraphQL resolvers '
                                              'significantly.',
                               'missing_concepts': ['Event Loop microtask batching trick: When loader.load(key) is '
                                                    'invoked in individual resolvers, it queues the key into a batch '
                                                    'array and returns a pending Promise; on the next tick (microtask '
                                                    'drain via process.nextTick / Promise.resolve), the batch function '
                                                    "executes a single SQL query ('SELECT * FROM books WHERE author_id "
                                                    "IN (...)')",
                                                    'Request-scoped caching: DataLoader caches loaded instances by key '
                                                    'within a single HTTP request context, preventing duplicate '
                                                    'queries if multiple parts of the GraphQL tree request the '
                                                    'identical entity']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'The N+1 problem is when a database table has N columns plus 1 primary '
                                              'key. DataLoader is an ETL pipeline in Python used to upload CSV files '
                                              'into PostgreSQL. It batches requests by compressing them into a ZIP '
                                              'archive.',
                               'missing_concepts': ['Root cause of N+1 problem: GraphQL resolver functions execute '
                                                    'independently and naively per field; fetching a list of N authors '
                                                    'and their books results in 1 query for authors followed by N '
                                                    "separate queries for each author's books (1 + N queries), "
                                                    'overwhelming databases',
                                                    'DataLoader core mechanism: Developed by Facebook to solve N+1 '
                                                    'queries through two primary features: Batching (coalescing '
                                                    'multiple load calls into a single batched operation) and Caching '
                                                    '(per-request memoization)',
                                                    'Event Loop microtask batching trick: When loader.load(key) is '
                                                    'invoked in individual resolvers, it queues the key into a batch '
                                                    'array and returns a pending Promise; on the next tick (microtask '
                                                    'drain via process.nextTick / Promise.resolve), the batch function '
                                                    "executes a single SQL query ('SELECT * FROM books WHERE author_id "
                                                    "IN (...)')",
                                                    'Request-scoped caching: DataLoader caches loaded instances by key '
                                                    'within a single HTTP request context, preventing duplicate '
                                                    'queries if multiple parts of the GraphQL tree request the '
                                                    'identical entity']}]},
          {'topic_tag': 'Real-Time Collaboration: OT vs CRDTs',
           'question': 'Contrast Operational Transformation (OT) and Conflict-Free Replicated Data Types (CRDTs) in '
                       'building real-time collaborative editors.',
           'keywords': ['Operational Transformation',
                        'CRDTs',
                        'Conflict-Free Replicated Data Types',
                        'Eventual Consistency',
                        'Collaborative Editing',
                        'Peer Synchronization'],
           'expected_concepts': ['Operational Transformation (OT): Client-server model (e.g. Google Docs) where '
                                 'concurrent editing operations (Insert, Delete, Retain) are transformed against each '
                                 'other based on character offsets to maintain consistency',
                                 'Centralized server requirement in OT: Requires an authoritative central server to '
                                 'establish total operation order and transform concurrent operations; complex '
                                 'transformation functions with brittle combinatorial edge cases',
                                 'Conflict-Free Replicated Data Types (CRDTs): Decentralized mathematical data '
                                 'structures (Yjs, Automerge, LWW-Element-Set) where operations commute and merge '
                                 'deterministically into identical states across all peers without a central '
                                 'coordinator',
                                 'CRDT trade-offs & memory overhead: CRDTs support true peer-to-peer (P2P) and '
                                 'offline-first collaboration, but incur higher memory and storage overhead due to '
                                 'unique character IDs,Lamport timestamps, and deletion tombstones'],
           'model_answer': 'Real-time collaborative editing (e.g., Google Docs, Figma, Notion) requires multiple '
                           'distributed clients to edit a shared document concurrently while converging '
                           'deterministically to identical state. Two foundational algorithms solve this concurrent '
                           'consistency challenge: 1. Operational Transformation (OT): - Architecture: OT (pioneered '
                           'in the 1980s and popularized by Google Wave/Docs) relies on an authoritative central '
                           "server. Document changes are modeled as positional operations: 'Insert(text, pos)' and "
                           "'Delete(length, pos)'. - Transformation Mechanism: When Peer A inserts 'x' at index 2 "
                           'while Peer B concurrently deletes at index 1, the operations conflict. The central server '
                           "acts as a sequencer, ordering operations. When Peer B's operation reaches Peer A, a "
                           "transformation function 'T(opA, opB)' recalculates character indices so both clients "
                           'achieve convergence. - Limitations: OT requires an authoritative central server '
                           '(precluding pure peer-to-peer or offline-first architectures). Designing transformation '
                           'matrices that satisfy algebraic transformation properties (TP1 and TP2) across rich-text '
                           'formats is notoriously difficult, bug-prone, and mathematically brittle. 2. Conflict-Free '
                           'Replicated Data Types (CRDTs): - Architecture: CRDTs (developed by Shapiro et al. and '
                           'implemented in libraries like Yjs and Automerge) are mathematically proven data structures '
                           'that achieve Strong Eventual Consistency without any central coordinator. - Mechanism: In '
                           'a text CRDT (e.g., RGA, Fugue), characters are not addressed by transient array indices. '
                           'Instead, every single character is assigned a globally unique, immutable ID composed of a '
                           'Lamport timestamp and client ID, along with positional ordering relations. CRDT operations '
                           'are commutative and associative; operations can be received out of order, over '
                           'peer-to-peer WebRTC connections, or merged after months of offline editing, and are '
                           'mathematically guaranteed to converge to the exact same state on all devices. - '
                           'Trade-offs: CRDTs carry memory and network overhead: tracking unique IDs and keeping '
                           "'tombstones' for deleted characters increases document metadata sizes, though modern "
                           'libraries (Yjs) use binary encoding and run-length compression to minimize overhead.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'Operational Transformation (OT) and Conflict-Free Replicated Data Types '
                                              '(CRDTs) are the two primary algorithms for handling real-time '
                                              'collaborative text editing. 1. Operational Transformation (OT) is what '
                                              'powers Google Docs. It models edits as operations based on character '
                                              'indices—like \'Insert "A" at position 5\'. If two users type at the '
                                              'same time, their character positions will clash. OT relies on an '
                                              'authoritative central server to establish a strict ordering of events. '
                                              'The server transforms incoming operations against concurrent operations '
                                              'using transformation functions so that when operations are applied to '
                                              'the document, both clients reach the same text. The main limitation of '
                                              'OT is that it requires a central server to mediate edits, and writing '
                                              'bug-free transformation functions for complex rich-text structures is '
                                              'notoriously difficult and brittle. 2. Conflict-Free Replicated Data '
                                              'Types (CRDTs) are a decentralized, mathematically proven alternative '
                                              'used by modern tools like Figma and libraries like Yjs and Automerge. '
                                              'In a text CRDT, characters are not referenced by index. Instead, every '
                                              'character receives a globally unique, immutable identifier containing a '
                                              'client ID and a Lamport logical timestamp. Edits are commutative and '
                                              'associative: operations can arrive in any order, over peer-to-peer '
                                              'WebRTC connections, or after hours of offline work, and every node is '
                                              'mathematically guaranteed to merge them into the exact same document '
                                              'state without a central server. The trade-off with CRDTs is memory '
                                              'overhead: storing unique metadata for every character and keeping '
                                              "'tombstones' for deleted characters makes memory usage higher than OT, "
                                              'though modern implementations like Yjs use binary delta encoding to '
                                              'make this negligible in production.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'Operational Transformation (OT) is used by Google Docs and requires a '
                                              'central server to coordinate edits. It represents changes by character '
                                              'index and transforms concurrent operations against each other to keep '
                                              'documents in sync. The downside is that writing OT transformation logic '
                                              'is very complex, and it cannot work peer-to-peer without a server. '
                                              'CRDTs (Conflict-Free Replicated Data Types) use decentralized data '
                                              'structures where each character has a unique ID and timestamp. CRDT '
                                              'operations can be merged in any order without a central server, making '
                                              'them ideal for offline-first and peer-to-peer collaboration, though '
                                              'they have higher memory overhead to store character IDs and tombstones.',
                               'missing_concepts': ['Operational Transformation (OT): Client-server model (e.g. Google '
                                                    'Docs) where concurrent editing operations (Insert, Delete, '
                                                    'Retain) are transformed against each other based on character '
                                                    'offsets to maintain consistency']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'OT is what Google Docs uses for real-time collaboration. It uses a '
                                              'central server to order edits and transforms character positions so '
                                              "text doesn't get messed up when two people type together. CRDTs are "
                                              "newer and don't need a central server because the data structure "
                                              'automatically resolves conflicts mathematically. Libraries like Yjs use '
                                              'CRDTs. CRDTs are great for offline-first apps, but they use more memory '
                                              'because they store extra metadata for each character.',
                               'missing_concepts': ['Operational Transformation (OT): Client-server model (e.g. Google '
                                                    'Docs) where concurrent editing operations (Insert, Delete, '
                                                    'Retain) are transformed against each other based on character '
                                                    'offsets to maintain consistency',
                                                    'CRDT trade-offs & memory overhead: CRDTs support true '
                                                    'peer-to-peer (P2P) and offline-first collaboration, but incur '
                                                    'higher memory and storage overhead due to unique character '
                                                    'IDs,Lamport timestamps, and deletion tombstones']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'Operational Transformation is an Agile management framework for '
                                              'software teams. CRDT is a blockchain cryptocurrency token used to pay '
                                              'for Google Docs subscriptions. Collaborative editors work by streaming '
                                              'MP4 video of the document between users.',
                               'missing_concepts': ['Operational Transformation (OT): Client-server model (e.g. Google '
                                                    'Docs) where concurrent editing operations (Insert, Delete, '
                                                    'Retain) are transformed against each other based on character '
                                                    'offsets to maintain consistency',
                                                    'Centralized server requirement in OT: Requires an authoritative '
                                                    'central server to establish total operation order and transform '
                                                    'concurrent operations; complex transformation functions with '
                                                    'brittle combinatorial edge cases',
                                                    'Conflict-Free Replicated Data Types (CRDTs): Decentralized '
                                                    'mathematical data structures (Yjs, Automerge, LWW-Element-Set) '
                                                    'where operations commute and merge deterministically into '
                                                    'identical states across all peers without a central coordinator',
                                                    'CRDT trade-offs & memory overhead: CRDTs support true '
                                                    'peer-to-peer (P2P) and offline-first collaboration, but incur '
                                                    'higher memory and storage overhead due to unique character '
                                                    'IDs,Lamport timestamps, and deletion tombstones']}]},
          {'topic_tag': 'CSS Containment & Layout Thrashing',
           'question': 'How does the CSS contain property prevent layout thrashing and forced synchronous reflows in '
                       'complex web applications?',
           'keywords': ['CSS contain Property',
                        'Layout Thrashing',
                        'FastDOM',
                        'Forced Synchronous Layout',
                        'Composite Layers',
                        'Will-Change Property'],
           'expected_concepts': ['Layout Thrashing & Forced Synchronous Layout: Occurs when JavaScript alternates '
                                 'between writing to the DOM (invalidating layout) and reading geometric properties '
                                 '(offsetWidth, clientHeight, getBoundingClientRect()), forcing the browser to execute '
                                 'synchronous reflows in a tight loop',
                                 "CSS contain property: Tells the browser engine that an element's subtree is isolated "
                                 'from the rest of the document across specific boundaries: size, layout, style, and '
                                 'paint (or contain: strict / content)',
                                 'Layout containment mechanics: contain: layout guarantees that internal DOM/CSS '
                                 'mutations inside the element never trigger layout reflow of external ancestor or '
                                 'sibling elements, confining layout computation to the component subtree',
                                 'Performance impact on complex apps: Combining containment with virtualized lists or '
                                 'complex widget dashboards reduces reflow times from tens of milliseconds down to '
                                 'sub-millisecond local updates'],
           'model_answer': 'In complex web applications with thousands of DOM nodes, maintaining 60fps responsiveness '
                           'requires eliminating Layout Thrashing and utilizing CSS Containment: 1. Layout Thrashing '
                           '(Forced Synchronous Reflow): Browsers naturally batch DOM mutations and schedule layout '
                           'recalculations at the end of the frame. Layout thrashing occurs when JavaScript '
                           "interleaves DOM writes and DOM reads in a loop: 'for (let el of elements) { el.style.width "
                           '= el.offsetWidth + 10 + "px"; }\'. - In this snippet, setting \'el.style.width\' '
                           "invalidates the layout. - Reading 'el.offsetWidth' on the next iteration forces the "
                           'browser to flush the queued mutations and execute a synchronous layout/reflow immediately '
                           'to calculate the exact pixel width. Doing this 100 times forces 100 synchronous layouts in '
                           'a single frame, causing severe dropped frames and UI jank. Solved by batching reads first, '
                           "then writes (using FastDOM or requestAnimationFrame). 2. The CSS 'contain' Property: "
                           "Normally, modifying a single element's DOM or dimensions can cause the browser to "
                           're-layout the entire document tree because elements can influence ancestor or sibling '
                           "geometries. The 'contain' property informs the rendering engine that an element's internal "
                           "subtree is completely decoupled and isolated from the rest of the page: - 'contain: "
                           "layout': Guarantees that internal layout changes inside the element never affect elements "
                           'outside its boundary, and external layout changes do not affect its internal formatting '
                           "context. Reflows are strictly localized. - 'contain: paint': Guarantees that child "
                           "elements cannot paint outside the containing box boundaries (acting like 'overflow: "
                           "hidden' with GPU optimizations). Offscreen elements can skip painting. - 'contain: size': "
                           "The element's size can be computed without examining its children (requires explicit "
                           "width/height). - 'contain: content': Combines 'layout' and 'paint'. - 'contain: strict': "
                           "Combines 'size', 'layout', and 'paint'. 3. Performance Impact: Applying 'contain: content' "
                           "or 'contain: strict' to complex widgets (cards, infinite feed items, charts) reduces "
                           'layout calculation times by up to 90%, preventing global cascading reflows.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'Layout thrashing and CSS containment are two critical concepts in web '
                                              'rendering performance: 1. Layout Thrashing (Forced Synchronous Layout): '
                                              'Normally, browsers batch DOM writes and wait until the end of the frame '
                                              'to perform layout and reflow. Layout thrashing happens when JavaScript '
                                              'interleaves DOM writes and DOM reads in a loop: for example, setting an '
                                              "element's height with el.style.height, and then immediately reading "
                                              "el.offsetHeight on the next line. Because you asked for the element's "
                                              'actual geometry, the browser cannot wait—it is forced to stop '
                                              'JavaScript execution, flush all pending DOM mutations, and run a full '
                                              'synchronous reflow immediately. Doing this repeatedly inside a loop '
                                              'completely freezes the main thread. We fix this by batching all reads '
                                              'first and all writes second, often using requestAnimationFrame or '
                                              'libraries like FastDOM. 2. The CSS contain property: Normally, when you '
                                              'change a single DOM element inside a component, the browser has to '
                                              'traverse up to the root and reflow the entire page because that element '
                                              "could affect its parent or siblings. The 'contain' property tells the "
                                              "browser: 'This component's subtree is completely isolated from the rest "
                                              "of the page'. - 'contain: layout' ensures that changes inside the "
                                              'element never trigger reflows outside the element, confining the layout '
                                              "pass to just that subtree. - 'contain: paint' ensures children never "
                                              "paint outside the container's bounds, allowing the browser to skip "
                                              "painting if the element is offscreen. - 'contain: size' means the "
                                              "container's dimensions don't depend on its children. - 'contain: "
                                              "content' combines layout and paint. In complex applications with "
                                              "infinite feeds, virtualized tables, or dashboards, applying 'contain: "
                                              "content' to cards or rows cuts layout computation times from 30ms down "
                                              'to less than 1ms because reflows are contained locally.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'Layout thrashing happens when JavaScript alternates between reading and '
                                              'writing DOM properties in a loop—like writing to style.width and then '
                                              'immediately reading offsetWidth. This forces the browser to calculate a '
                                              'synchronous layout on every iteration, causing severe lag. The CSS '
                                              'contain property helps performance by isolating parts of the DOM. For '
                                              'instance, contain: layout tells the browser that layout changes inside '
                                              'an element will never affect elements outside of it, so the browser '
                                              'only reflows that single component instead of the entire page. contain: '
                                              'content combines layout and paint containment, significantly speeding '
                                              'up complex pages like feeds and dashboards.',
                               'missing_concepts': ['Performance impact on complex apps: Combining containment with '
                                                    'virtualized lists or complex widget dashboards reduces reflow '
                                                    'times from tens of milliseconds down to sub-millisecond local '
                                                    'updates']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'Layout thrashing is when your JavaScript forces the browser to reflow '
                                              'the page repeatedly because you read properties like offsetHeight right '
                                              'after changing a style in a loop. It slows down the website. The CSS '
                                              'contain property tells the browser that a div is self-contained so that '
                                              "changes inside it don't force a layout on the rest of the page. You can "
                                              'use contain: layout or contain: content on items in a list to make '
                                              'rendering faster.',
                               'missing_concepts': ['Layout Thrashing & Forced Synchronous Layout: Occurs when '
                                                    'JavaScript alternates between writing to the DOM (invalidating '
                                                    'layout) and reading geometric properties (offsetWidth, '
                                                    'clientHeight, getBoundingClientRect()), forcing the browser to '
                                                    'execute synchronous reflows in a tight loop',
                                                    'Performance impact on complex apps: Combining containment with '
                                                    'virtualized lists or complex widget dashboards reduces reflow '
                                                    'times from tens of milliseconds down to sub-millisecond local '
                                                    'updates']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'Layout thrashing is when an angry user clicks buttons too fast and '
                                              'crashes the browser. The CSS contain property is used to contain images '
                                              'inside a div like object-fit: contain. It prevents the website from '
                                              'crashing when viewed on an iPad.',
                               'missing_concepts': ['Layout Thrashing & Forced Synchronous Layout: Occurs when '
                                                    'JavaScript alternates between writing to the DOM (invalidating '
                                                    'layout) and reading geometric properties (offsetWidth, '
                                                    'clientHeight, getBoundingClientRect()), forcing the browser to '
                                                    'execute synchronous reflows in a tight loop',
                                                    "CSS contain property: Tells the browser engine that an element's "
                                                    'subtree is isolated from the rest of the document across specific '
                                                    'boundaries: size, layout, style, and paint (or contain: strict / '
                                                    'content)',
                                                    'Layout containment mechanics: contain: layout guarantees that '
                                                    'internal DOM/CSS mutations inside the element never trigger '
                                                    'layout reflow of external ancestor or sibling elements, confining '
                                                    'layout computation to the component subtree',
                                                    'Performance impact on complex apps: Combining containment with '
                                                    'virtualized lists or complex widget dashboards reduces reflow '
                                                    'times from tens of milliseconds down to sub-millisecond local '
                                                    'updates']}]},
          {'topic_tag': 'Enterprise SSO: SAML vs OIDC Federation',
           'question': 'Compare SAML 2.0 XML assertions with OpenID Connect JWT tokens for enterprise Single Sign-On '
                       'federation.',
           'keywords': ['Single Sign-On',
                        'SAML 2.0',
                        'OpenID Connect',
                        'Identity Provider',
                        'Service Provider',
                        'JWT Assertions'],
           'expected_concepts': ['SAML 2.0 architecture: Enterprise XML-based OASIS standard connecting Identity '
                                 'Providers (IdP: Okta, Azure AD) with Service Providers (SP); uses XML digital '
                                 'signatures (XMLDSig) and Base64-encoded XML assertions routed via browser HTTP POST '
                                 'bindings',
                                 'OpenID Connect (OIDC) architecture: Modern identity layer built on top of OAuth 2.0; '
                                 'delivers identity claims as compact, digitally signed JSON Web Tokens (ID Token) via '
                                 'RESTful endpoints',
                                 'Security & implementation comparison: SAML XML parsing is notoriously complex and '
                                 'vulnerable to XML External Entity (XXE) and signature wrapping attacks; OIDC uses '
                                 'standard JWT cryptographic libraries, eliminating XML complexity',
                                 'Platform compatibility: SAML 2.0 is deeply entrenched in legacy enterprise web '
                                 'applications; OIDC is ubiquitous for modern SPAs, mobile apps, native applications, '
                                 'and microservice APIs'],
           'model_answer': 'Enterprise Single Sign-On (SSO) federation enables employees to authenticate once through '
                           'a centralized Identity Provider (IdP, such as Okta, Ping Identity, or Microsoft Entra ID) '
                           'and gain seamless, authenticated access to multiple internal and third-party SaaS Service '
                           'Providers (SPs). Two major protocols dominate enterprise federation: 1. SAML 2.0 (Security '
                           'Assertion Markup Language): - Format: An XML-based standard standardized by OASIS in 2005. '
                           'Identity assertions are formulated as verbose XML documents signed using XMLDSig (XML '
                           'Digital Signature) containing public X.509 certificates. - Transport: SAML assertions are '
                           "typically Base64-encoded and transmitted through the user's browser via an automated HTTP "
                           "POST form binding ('SAMLResponse') directly to the SP's Assertion Consumer Service (ACS) "
                           'endpoint. - Pros & Cons: Heavily entrenched in enterprise legacy systems, government '
                           'infrastructure, and legacy corporate intranets. However, XML parsing is computationally '
                           'heavy, and XMLDSig is notoriously vulnerable to canonicalization bugs, XML External Entity '
                           '(XXE) injection, and XML Signature Wrapping (XSW) attacks. Moreover, SAML is virtually '
                           'unusable for mobile native apps or SPAs due to heavy browser-redirect assumptions. 2. '
                           'OpenID Connect (OIDC): - Format: Standardized in 2014 by the OpenID Foundation as an '
                           'identity layer built on OAuth 2.0. Identity assertions are delivered as compact, standard '
                           "JSON Web Tokens (JWT) called 'ID Tokens', signed using JWS (JSON Web Signature, e.g., "
                           "RS256) and verified using public keys exposed at the IdP's JWKS endpoint "
                           "('.well-known/jwks.json'). - Transport: Operates over modern RESTful JSON/HTTPS endpoints "
                           'via the Authorization Code Flow with PKCE. - Pros & Cons: Lightweight, highly secure, '
                           'easily parsed in any language without complex XML libraries, and natively designed for '
                           'Single Page Applications (SPAs), mobile apps, and microservice mesh authorization. OIDC '
                           'has become the modern standard for new enterprise integrations.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'SAML 2.0 and OpenID Connect (OIDC) are the two primary federation '
                                              'protocols used for enterprise Single Sign-On (SSO): 1. SAML 2.0 is an '
                                              'enterprise standard established in 2005 based on XML. In SAML, the '
                                              'Identity Provider (like Okta or Azure AD) authenticates the user and '
                                              'generates a signed XML assertion containing user attributes. This '
                                              'assertion is Base64-encoded and transmitted through the browser via an '
                                              "auto-submitting HTTP POST form to the Service Provider's Assertion "
                                              'Consumer Service endpoint. SAML is deeply entrenched in enterprise B2B '
                                              'SaaS and legacy software. However, SAML has significant drawbacks: XML '
                                              'parsing is heavy, and XML Digital Signatures (XMLDSig) are notoriously '
                                              'difficult to implement securely, leading to high-profile '
                                              'vulnerabilities like XML Signature Wrapping (XSW) and XXE attacks. '
                                              'Furthermore, SAML is completely unsuited for native mobile apps or '
                                              'single-page apps. 2. OpenID Connect (OIDC) is the modern identity layer '
                                              'built directly on top of OAuth 2.0. Instead of heavy XML, OIDC '
                                              'represents identity claims using compact JSON Web Tokens '
                                              '(JWTs)—specifically the ID Token. The token is cryptographically signed '
                                              'using standard JSON Web Signatures (JWS) and verified using public keys '
                                              "published at the IdP's JWKS endpoint. OIDC uses standard OAuth 2.0 "
                                              'flows, making it lightweight, developer-friendly, and natively '
                                              'compatible with modern SPAs, mobile applications, and microservices. '
                                              'Today, enterprise applications use SAML when integrating with legacy '
                                              'enterprise identity systems, but prefer OIDC for all modern web and '
                                              'mobile architectures.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'SAML 2.0 and OpenID Connect are protocols for enterprise Single '
                                              'Sign-On. SAML uses XML assertions signed with digital certificates to '
                                              'pass authentication data from an Identity Provider like Okta to a '
                                              'Service Provider, typically using browser HTTP POST redirects. It is '
                                              'widely used in legacy enterprise systems, but XML parsing is complex '
                                              'and prone to security vulnerabilities. OpenID Connect is built on OAuth '
                                              '2.0 and uses JSON Web Tokens (ID Tokens) signed with public keys. OIDC '
                                              'is much simpler, uses RESTful endpoints, and is ideal for modern SPAs '
                                              'and mobile applications.',
                               'missing_concepts': ['Security & implementation comparison: SAML XML parsing is '
                                                    'notoriously complex and vulnerable to XML External Entity (XXE) '
                                                    'and signature wrapping attacks; OIDC uses standard JWT '
                                                    'cryptographic libraries, eliminating XML complexity']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'SAML and OIDC are used for corporate Single Sign-On so employees can '
                                              'log into tools like Salesforce using their Okta account. SAML 2.0 is an '
                                              'older protocol that uses XML messages to send login assertions. OIDC is '
                                              'newer and uses JSON Web Tokens (JWT) on top of OAuth 2.0. OIDC is '
                                              'preferred for modern web apps because JSON is easier to work with than '
                                              'XML, but many big enterprises still use SAML because of existing '
                                              'systems.',
                               'missing_concepts': ['SAML 2.0 architecture: Enterprise XML-based OASIS standard '
                                                    'connecting Identity Providers (IdP: Okta, Azure AD) with Service '
                                                    'Providers (SP); uses XML digital signatures (XMLDSig) and '
                                                    'Base64-encoded XML assertions routed via browser HTTP POST '
                                                    'bindings',
                                                    'Security & implementation comparison: SAML XML parsing is '
                                                    'notoriously complex and vulnerable to XML External Entity (XXE) '
                                                    'and signature wrapping attacks; OIDC uses standard JWT '
                                                    'cryptographic libraries, eliminating XML complexity']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'SAML 2.0 is an encryption standard used to store passwords in MySQL. '
                                              'OpenID Connect is an open-source browser like Firefox. Enterprise SSO '
                                              'means users must type their password twice to ensure high security.',
                               'missing_concepts': ['SAML 2.0 architecture: Enterprise XML-based OASIS standard '
                                                    'connecting Identity Providers (IdP: Okta, Azure AD) with Service '
                                                    'Providers (SP); uses XML digital signatures (XMLDSig) and '
                                                    'Base64-encoded XML assertions routed via browser HTTP POST '
                                                    'bindings',
                                                    'OpenID Connect (OIDC) architecture: Modern identity layer built '
                                                    'on top of OAuth 2.0; delivers identity claims as compact, '
                                                    'digitally signed JSON Web Tokens (ID Token) via RESTful endpoints',
                                                    'Security & implementation comparison: SAML XML parsing is '
                                                    'notoriously complex and vulnerable to XML External Entity (XXE) '
                                                    'and signature wrapping attacks; OIDC uses standard JWT '
                                                    'cryptographic libraries, eliminating XML complexity',
                                                    'Platform compatibility: SAML 2.0 is deeply entrenched in legacy '
                                                    'enterprise web applications; OIDC is ubiquitous for modern SPAs, '
                                                    'mobile apps, native applications, and microservice APIs']}]},
          {'topic_tag': 'Web Push Architecture & VAPID Protocol',
           'question': 'Detail the architecture of Web Push Notifications, explaining VAPID key authentication and '
                       'Service Worker push payloads.',
           'keywords': ['Web Push API',
                        'VAPID Keys',
                        'Push Service',
                        'Service Worker Listener',
                        'Encrypted Payload',
                        'Notification Triggers'],
           'expected_concepts': ['Three-party architecture: Web Push involves three distinct actors: 1. User Agent '
                                 '(Browser & Service Worker); 2. App Server (backend); 3. Browser Vendor Push Service '
                                 '(e.g., Google FCM, Mozilla Autopush, Apple Web Push)',
                                 'PushSubscription creation: Client browser calls registration.pushManager.subscribe() '
                                 'with applicationServerKey (public VAPID key); receives unique PushSubscription '
                                 'endpoint URL and encryption keys (p256dh, auth)',
                                 'VAPID (Voluntary Application Server Identification) protocol: Backend signs a JWT '
                                 'with its private VAPID key and attaches it to the Authorization header when sending '
                                 'messages to the Push Service, verifying server identity without proprietary vendor '
                                 'accounts',
                                 'End-to-end payload encryption & display: Backend encrypts notification payload using '
                                 "recipient's p256dh public key (AES-128-GCM); Push Service wakes sleeping Service "
                                 "Worker via 'push' event; Service Worker decrypts payload and calls "
                                 'self.registration.showNotification()'],
           'model_answer': 'Web Push Notifications allow web backends to deliver timely updates to users even when the '
                           'web application is completely closed. The architecture relies on three coordinated actors, '
                           'the VAPID authentication standard, and encrypted message delivery: 1. The Three-Party '
                           "Architecture: - The User Agent: The client's browser and its registered background Service "
                           "Worker. - The Application Server: The company's backend server sending notifications. - "
                           'The Push Service: A cloud gateway operated by the browser vendor (e.g., Google Firebase '
                           'Cloud Messaging for Chrome, Mozilla Autopush for Firefox, Apple Push Notification service '
                           'for Safari). 2. Subscription Generation: - The client browser requests notification '
                           "permission ('Notification.requestPermission()'). - Upon approval, the client registers "
                           "with the Push Service via 'registration.pushManager.subscribe({ userVisibleOnly: true, "
                           "applicationServerKey: urlBase64ToUint8Array(VAPID_PUBLIC_KEY) })'. - The Push Service "
                           "generates a unique 'PushSubscription' object containing an endpoint URL (e.g., "
                           "'https://fcm.googleapis.com/fcm/send/...') and two client cryptographic keys: 'p256dh' "
                           "(client public key) and 'auth' (authentication secret). The client transmits this "
                           'subscription object to the application backend to store in its database. 3. VAPID Protocol '
                           '(RFC 8292): Voluntary Application Server Identification (VAPID) allows the application '
                           'server to authenticate itself directly to the vendor Push Service without needing '
                           'proprietary developer accounts. The backend generates a public/private keypair using '
                           'Elliptic Curve cryptography (NIST P-256 curve). When sending a notification, the backend '
                           "signs a JWT with its private VAPID key, placing it in the 'Authorization: vapid t=...' "
                           'header. 4. Encrypted Payload Delivery & Display: - The backend encrypts the notification '
                           "payload (title, body, icon, URL) using the client's 'p256dh' key via AES-128-GCM (RFC "
                           '8291). The Push Service itself cannot decrypt or inspect this payload. - The Push Service '
                           "routes the message to the user's device, waking the dormant Service Worker in the "
                           'background. - The Service Worker intercepts the message: \'self.addEventListener("push", '
                           'event => { const data = event.data.json(); '
                           "event.waitUntil(self.registration.showNotification(data.title, data.options)); })'.",
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'Web Push Notifications work across a three-party architecture: the '
                                              'Client Browser (with a Service Worker), your Application Backend '
                                              "Server, and the Browser Vendor's Push Service (like Google FCM for "
                                              'Chrome, Mozilla Autopush, or Apple APNs). Here is the complete '
                                              'lifecycle: 1. Subscription: The user grants notification permission in '
                                              "the browser. The frontend calls 'registration.pushManager.subscribe()', "
                                              "passing your backend's public VAPID key as the 'applicationServerKey'. "
                                              'The browser connects to its vendor Push Service and receives a '
                                              'PushSubscription object containing an endpoint URL and two '
                                              "cryptographic keys: 'p256dh' (public key) and 'auth' (shared secret). "
                                              'The frontend sends this subscription object to your backend database. '
                                              '2. VAPID Protocol: VAPID stands for Voluntary Application Server '
                                              'Identification (RFC 8292). It allows your backend to prove its identity '
                                              "to Google or Mozilla's Push Service using an asymmetric elliptic curve "
                                              'keypair (P-256). When your backend wants to trigger a notification, it '
                                              'signs a JWT using its private VAPID key and sends it in the '
                                              'Authorization header to the Push Service endpoint. 3. End-to-End '
                                              'Encryption: Web push payloads must be encrypted before sending. The '
                                              "backend encrypts the notification JSON using the client's p256dh public "
                                              'key and auth secret with AES-128-GCM. Because it is encrypted '
                                              'end-to-end, the vendor Push Service acts as a blind relay and cannot '
                                              'read the notification content. 4. Displaying the notification: The Push '
                                              "Service sends the encrypted packet to the user's device, which wakes up "
                                              'the dormant Service Worker in the background. The Service Worker '
                                              "listens to the 'push' event, decrypts the payload, and calls "
                                              "'self.registration.showNotification(data.title, data.options)' to "
                                              'display the native OS notification even if the browser tab is '
                                              'completely closed.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'Web Push Notifications involve the browser, your backend server, and '
                                              "the browser vendor's Push Service like Google FCM. When the user "
                                              "subscribes, the browser calls pushManager.subscribe with the backend's "
                                              'public VAPID key to get a PushSubscription containing an endpoint URL '
                                              'and encryption keys. When your backend wants to send a notification, it '
                                              'uses VAPID to sign a JWT proving its identity, encrypts the '
                                              "notification payload using the client's public key with AES-128-GCM, "
                                              'and POSTs it to the push service endpoint. The push service wakes up '
                                              'the Service Worker, which handles the push event and calls '
                                              'showNotification to display the popup.',
                               'missing_concepts': ['VAPID (Voluntary Application Server Identification) protocol: '
                                                    'Backend signs a JWT with its private VAPID key and attaches it to '
                                                    'the Authorization header when sending messages to the Push '
                                                    'Service, verifying server identity without proprietary vendor '
                                                    'accounts']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'Web Push lets you send notifications to users even when your website is '
                                              'closed. The frontend registers a Service Worker and gets a push '
                                              'subscription from the browser. The backend uses VAPID keys to '
                                              'authenticate with push services like Firebase. When the backend sends a '
                                              'push message, it sends it to the push service endpoint, which routes it '
                                              "to the user's computer. The Service Worker listens to the push event "
                                              'and shows the notification popup on the screen.',
                               'missing_concepts': ['PushSubscription creation: Client browser calls '
                                                    'registration.pushManager.subscribe() with applicationServerKey '
                                                    '(public VAPID key); receives unique PushSubscription endpoint URL '
                                                    'and encryption keys (p256dh, auth)',
                                                    'End-to-end payload encryption & display: Backend encrypts '
                                                    "notification payload using recipient's p256dh public key "
                                                    '(AES-128-GCM); Push Service wakes sleeping Service Worker via '
                                                    "'push' event; Service Worker decrypts payload and calls "
                                                    'self.registration.showNotification()']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'Web Push Notifications are SMS text messages sent directly from the '
                                              "server to the user's mobile SIM card. VAPID keys are credit card "
                                              'authorization tokens. Service Workers must keep an open WebSocket '
                                              'connection active 24/7 or the notification will fail.',
                               'missing_concepts': ['Three-party architecture: Web Push involves three distinct '
                                                    'actors: 1. User Agent (Browser & Service Worker); 2. App Server '
                                                    '(backend); 3. Browser Vendor Push Service (e.g., Google FCM, '
                                                    'Mozilla Autopush, Apple Web Push)',
                                                    'PushSubscription creation: Client browser calls '
                                                    'registration.pushManager.subscribe() with applicationServerKey '
                                                    '(public VAPID key); receives unique PushSubscription endpoint URL '
                                                    'and encryption keys (p256dh, auth)',
                                                    'VAPID (Voluntary Application Server Identification) protocol: '
                                                    'Backend signs a JWT with its private VAPID key and attaches it to '
                                                    'the Authorization header when sending messages to the Push '
                                                    'Service, verifying server identity without proprietary vendor '
                                                    'accounts',
                                                    'End-to-end payload encryption & display: Backend encrypts '
                                                    "notification payload using recipient's p256dh public key "
                                                    '(AES-128-GCM); Push Service wakes sleeping Service Worker via '
                                                    "'push' event; Service Worker decrypts payload and calls "
                                                    'self.registration.showNotification()']}]},
          {'topic_tag': 'V8 JIT Compiler Ignition & TurboFan',
           'question': 'Explain how the V8 JavaScript engine transitions code from the Ignition interpreter to the '
                       'TurboFan JIT compiler using hidden classes and inline caches.',
           'keywords': ['V8 Engine',
                        'Ignition Interpreter',
                        'TurboFan Compiler',
                        'Hidden Classes',
                        'Inline Caches',
                        'Deoptimization'],
           'expected_concepts': ['Two-tier execution pipeline: V8 parses JS into an AST; Ignition (register-based '
                                 'bytecode interpreter) executes code immediately with low memory and start-up latency '
                                 'while gathering runtime type feedback',
                                 'Hidden Classes (Shapes/Maps): JavaScript objects are dynamically typed, so V8 '
                                 "creates internal static 'Shapes' (hidden classes) that track property offsets in "
                                 'memory; objects initialized with identical properties in the same order share the '
                                 'same hidden class',
                                 'Inline Caches (ICs): Code call sites record property access feedback in Feedback '
                                 'Vectors; Monomorphic calls (always encountering 1 shape) optimize to single pointer '
                                 'comparisons; Polymorphic (2-4 shapes) and Megamorphic (5+ shapes) degrade '
                                 'performance',
                                 'TurboFan optimization and De-optimization (Bailout): Hot functions with stable '
                                 'monomorphic type feedback are compiled by TurboFan into highly optimized machine '
                                 'code; if an unexpected type/shape arrives, TurboFan de-optimizes and bails out back '
                                 'to Ignition'],
           'model_answer': "Google's V8 engine executes JavaScript at high performance through a sophisticated "
                           'multi-tiered Just-In-Time (JIT) execution pipeline driven by Ignition and TurboFan: 1. '
                           'Ignition (Bytecode Interpreter): When JavaScript code loads, V8 parses the source into an '
                           'Abstract Syntax Tree (AST). Rather than compiling directly to machine code (which consumes '
                           "massive memory), the 'Ignition' interpreter compiles the AST into concise bytecode in "
                           'milliseconds. Ignition executes the bytecode immediately, ensuring instant page startup. '
                           "As it executes, Ignition records runtime execution statistics in a 'Feedback "
                           "Vector'—tracking invocation frequency and the types of arguments passing through every "
                           'operation. 2. Hidden Classes (Shapes / Maps): JavaScript is dynamically typed, meaning '
                           'object properties can be added or deleted at runtime. In languages like C++, property '
                           "offsets are known at compile time. V8 bridges this gap by creating internal 'Hidden "
                           "Classes' (also called Shapes or Maps). When an object '{ x: 1, y: 2 }' is created, V8 "
                           "assigns it a Shape tracking the exact byte offset of 'x' and 'y'. If another object is "
                           'initialized with the same properties in the exact same order, it shares the identical '
                           "Shape. 3. Inline Caches (ICs): When code accesses 'point.x', V8 uses an Inline Cache. On "
                           "first execution, it performs an expensive dictionary lookup and caches the result: 'If "
                           "object.shape === Shape_A, property x is at offset 0'. - Monomorphic: The site always sees "
                           'the same Shape. Fast-path machine code directly reads offset 0. - Polymorphic: Sees 2-4 '
                           'shapes. Uses a small branch table. - Megamorphic: Sees 5+ shapes. Degrades to a slow hash '
                           "table lookup. 4. TurboFan JIT Compiler: When a function becomes 'hot' (executed thousands "
                           "of times), V8 passes the bytecode and the feedback vector to the 'TurboFan' optimizing "
                           'compiler. TurboFan uses speculative optimization: it assumes the types recorded in the ICs '
                           'will continue to hold true, inlines functions, and generates stripped-down, lightning-fast '
                           'native machine code. 5. De-optimization (Bailout): If an assumption is violated—e.g., '
                           'passing a string into a math function previously optimized strictly for integers—TurboFan '
                           "cannot execute the machine code. It triggers a 'De-optimization' (bailout), invalidating "
                           'the machine code, restoring the stack frame, and dropping back down to Ignition bytecode '
                           'interpretation.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 97,
                               'answer_text': 'V8 executes JavaScript through a two-tier JIT pipeline composed of the '
                                              'Ignition interpreter and the TurboFan optimizing compiler, powered by '
                                              'Hidden Classes and Inline Caches: 1. Ignition Interpreter: When code '
                                              'loads, V8 parses it into an AST and compiles it into bytecode using '
                                              'Ignition. Ignition starts executing immediately with almost zero '
                                              'startup latency. As it executes, it records type feedback in a Feedback '
                                              'Vector at every operation site. 2. Hidden Classes (Shapes): In C++, '
                                              'object properties have fixed memory offsets, but in JavaScript, objects '
                                              'are dynamic dictionaries. V8 solves this by dynamically assigning an '
                                              "internal 'Hidden Class' or Shape to every object. If you create two "
                                              "objects with the exact same properties in the exact same order ('{ x: "
                                              "1, y: 2 }'), V8 assigns them the same hidden class, which records the "
                                              "exact memory offset of 'x' and 'y'. 3. Inline Caches (ICs): An Inline "
                                              'Cache memorizes property access locations. The first time a function '
                                              "runs 'obj.x', it looks up the offset and remembers: 'if the input "
                                              "object has Shape_1, property x is at offset 0'. A call site that only "
                                              "ever sees one shape is 'Monomorphic', which is the fastest possible "
                                              "state. If it sees 2 to 4 shapes it becomes 'Polymorphic', and if it "
                                              "sees 5+ shapes it becomes 'Megamorphic' and falls back to a slow "
                                              'dictionary lookup. 4. TurboFan Compilation: When a function becomes '
                                              "'hot' (invoked thousands of times), V8 sends its bytecode and type "
                                              'feedback to TurboFan. TurboFan makes speculative optimizations: '
                                              'assuming the monomorphic types will never change, it eliminates type '
                                              'checks, inlines code, and emits blistering-fast native machine code. 5. '
                                              'De-optimization (Bailout): If you suddenly pass an object with a '
                                              'different shape or pass a string into a function optimized for '
                                              "integers, TurboFan's assumptions fail. V8 executes a 'de-optimization' "
                                              'bailout: it discards the optimized machine code, reconstructs the call '
                                              'frame, and drops back to Ignition bytecode interpretation.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'V8 uses Ignition to interpret JavaScript into bytecode quickly for fast '
                                              'startup, while collecting type feedback during execution. Because '
                                              'JavaScript objects are dynamic, V8 creates Hidden Classes (Shapes) '
                                              'behind the scenes that track property memory offsets. Inline caches '
                                              'record which hidden classes appear at each property access site. When a '
                                              'function is called frequently, TurboFan compiles the bytecode into '
                                              'optimized machine code based on the assumption that object shapes will '
                                              'stay the same (monomorphic). If an unexpected object shape is passed, '
                                              'TurboFan triggers a de-optimization bailout and drops back to the '
                                              'Ignition interpreter.',
                               'missing_concepts': ['Inline Caches (ICs): Code call sites record property access '
                                                    'feedback in Feedback Vectors; Monomorphic calls (always '
                                                    'encountering 1 shape) optimize to single pointer comparisons; '
                                                    'Polymorphic (2-4 shapes) and Megamorphic (5+ shapes) degrade '
                                                    'performance']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'V8 is the engine inside Chrome and Node.js. It has two parts: Ignition '
                                              'and TurboFan. Ignition compiles code to bytecode so it runs right away. '
                                              'When a function runs a lot, TurboFan takes over and turns it into '
                                              'optimized machine code. It uses hidden classes to remember where object '
                                              "properties are stored in memory. If you change an object's properties "
                                              'dynamically, it causes de-optimization which slows down the code '
                                              'because TurboFan has to fall back to the interpreter.',
                               'missing_concepts': ['Inline Caches (ICs): Code call sites record property access '
                                                    'feedback in Feedback Vectors; Monomorphic calls (always '
                                                    'encountering 1 shape) optimize to single pointer comparisons; '
                                                    'Polymorphic (2-4 shapes) and Megamorphic (5+ shapes) degrade '
                                                    'performance',
                                                    'TurboFan optimization and De-optimization (Bailout): Hot '
                                                    'functions with stable monomorphic type feedback are compiled by '
                                                    'TurboFan into highly optimized machine code; if an unexpected '
                                                    'type/shape arrives, TurboFan de-optimizes and bails out back to '
                                                    'Ignition']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'Ignition is a car engine spark plug simulator written in JavaScript. '
                                              'TurboFan is a cooling fan script that prevents laptops from overheating '
                                              'during heavy loops. Hidden classes are private CSS classes that cannot '
                                              'be inspected in Chrome DevTools.',
                               'missing_concepts': ['Two-tier execution pipeline: V8 parses JS into an AST; Ignition '
                                                    '(register-based bytecode interpreter) executes code immediately '
                                                    'with low memory and start-up latency while gathering runtime type '
                                                    'feedback',
                                                    'Hidden Classes (Shapes/Maps): JavaScript objects are dynamically '
                                                    "typed, so V8 creates internal static 'Shapes' (hidden classes) "
                                                    'that track property offsets in memory; objects initialized with '
                                                    'identical properties in the same order share the same hidden '
                                                    'class',
                                                    'Inline Caches (ICs): Code call sites record property access '
                                                    'feedback in Feedback Vectors; Monomorphic calls (always '
                                                    'encountering 1 shape) optimize to single pointer comparisons; '
                                                    'Polymorphic (2-4 shapes) and Megamorphic (5+ shapes) degrade '
                                                    'performance',
                                                    'TurboFan optimization and De-optimization (Bailout): Hot '
                                                    'functions with stable monomorphic type feedback are compiled by '
                                                    'TurboFan into highly optimized machine code; if an unexpected '
                                                    'type/shape arrives, TurboFan de-optimizes and bails out back to '
                                                    'Ignition']}]},
          {'topic_tag': 'Web Application Firewall Rules',
           'question': 'How do Web Application Firewalls (WAF) inspect incoming HTTP payloads to block SQL injection, '
                       'XSS, and layer 7 DDoS attacks?',
           'keywords': ['WAF',
                        'DDoS Mitigation',
                        'SQL Injection Filtering',
                        'Rate Limiting Rules',
                        'IP Reputation',
                        'Packet Inspection'],
           'expected_concepts': ['Layer 7 application-level inspection: Unlike network firewalls (Layer 3/4 inspecting '
                                 'IP/port), a WAF inspects full HTTP/HTTPS application payloads (headers, cookies, '
                                 'URIs, query parameters, POST JSON/form bodies)',
                                 'SQL Injection (SQLi) & XSS inspection: Uses signature matching, regex heuristics, '
                                 'and lexical tokenization (e.g. ModSecurity Core Rule Set) to detect SQL constructs '
                                 '(UNION SELECT, OR 1=1) and script injection (<script>, javascript:, onerror=)',
                                 'Layer 7 DDoS & bot mitigation: Enforces rate-limiting rules (e.g. max 100 requests '
                                 'per 10s per IP), IP reputation scoring, behavioral anomaly detection, and automated '
                                 'challenges (CAPTCHA / JavaScript cryptographic proof-of-work)',
                                 'Virtual patching capability: Allows security teams to deploy immediate edge WAF '
                                 'rules to neutralize zero-day CVEs across all backend services in minutes before '
                                 'source code fixes can be deployed'],
           'model_answer': 'A Web Application Firewall (WAF)—such as AWS WAF, Cloudflare WAF, or ModSecurity—operates '
                           'at Layer 7 (the Application Layer) of the OSI model. Unlike network-layer firewalls that '
                           'filter traffic based on IP addresses and TCP/UDP ports, a WAF decrypts TLS traffic and '
                           'performs deep inspection of the entire HTTP/HTTPS request before it reaches application '
                           'servers: 1. SQL Injection (SQLi) & XSS Inspection: - The WAF inspects request URLs, query '
                           'parameters, headers, cookies, and POST request bodies (including JSON, XML, and multipart '
                           'forms). - Rule engines (like OWASP ModSecurity Core Rule Set) use tokenizers and regular '
                           'expressions to parse payloads into abstract syntax elements. - For SQLi, it detects '
                           "suspicious SQL grammar (e.g., 'UNION SELECT', 'OR 1=1 --', 'WAITFOR DELAY', hex-encoded "
                           'SQL commands). - For XSS, it detects HTML tag injections, malicious JavaScript protocols '
                           "('javascript:'), DOM event handlers ('onload=', 'onerror='), and encoded variations "
                           'designed to bypass basic filters. 2. Layer 7 DDoS and Bot Mitigation: - Layer 7 DDoS '
                           'attacks attempt to exhaust server CPU or database connection pools by flooding expensive '
                           'endpoints (e.g., search queries or login APIs) with seemingly legitimate HTTP GET/POST '
                           'requests. - WAFs mitigate this through Rate Limiting Rules (e.g., blocking or challenging '
                           'an IP exceeding 200 requests per 10 seconds), IP Reputation filtering (blocking known '
                           'botnet ranges and Tor exit nodes), and automated Managed Challenges (issuing silent '
                           'JavaScript cryptographic proof-of-work challenges that standard bot scripts cannot '
                           'execute). 3. Virtual Patching: When a critical zero-day vulnerability is announced (e.g., '
                           'Log4j / Log4Shell), patching source code and redeploying microservices takes days. '
                           "Security teams deploy a 'Virtual Patch' on the WAF within minutes: a custom regex rule "
                           "that inspects all headers and drops requests containing '${jndi:...}', shielding the "
                           'entire infrastructure instantly.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'A Web Application Firewall (WAF) operates at Layer 7—the Application '
                                              'Layer—unlike traditional network firewalls that only look at Layer 3 '
                                              'and 4 IP addresses and ports. A WAF terminates TLS and performs deep '
                                              'inspection of the entire HTTP request, including query parameters, '
                                              'headers, cookies, and JSON/form bodies, to protect backends in three '
                                              'major ways: 1. Detecting SQL Injection and XSS: WAFs use rule engines '
                                              'like the OWASP Core Rule Set combined with lexical tokenization. For '
                                              'SQL injection, the WAF analyzes incoming payloads for SQL syntax '
                                              "patterns like 'UNION SELECT', `' OR 1=1 --`, comment delimiters, and "
                                              'sleep functions. For XSS, it scans for script tags, javascript: '
                                              "pseudo-protocols, and inline event handlers like 'onerror=' or "
                                              "'onload=', even if they are obfuscated using URL encoding or hex "
                                              'encoding. 2. Layer 7 DDoS and Bot Mitigation: Unlike volumetric Layer 4 '
                                              'floods (SYN floods), Layer 7 DDoS attacks flood resource-intensive '
                                              'endpoints—like a complex search query or checkout API—with valid HTTP '
                                              'requests to exhaust database connections. A WAF enforces granular '
                                              'rate-limiting rules (e.g., capping requests at 100 per minute per IP), '
                                              'analyzes IP reputation against known malicious botnets, and issues '
                                              'silent JavaScript cryptographic proof-of-work challenges that headless '
                                              'scrapers fail. 3. Virtual Patching: When a critical zero-day '
                                              'vulnerability like Log4Shell or a zero-day in an npm package is '
                                              'published, rewriting and testing backend code can take days. A WAF '
                                              "allows security engineers to deploy a 'Virtual Patch' at the edge in "
                                              'five minutes—creating a rule that drops any request matching the '
                                              'exploit pattern across the entire company infrastructure instantly '
                                              'while developers work on the permanent code fix.',
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'A Web Application Firewall operates at Layer 7 of the OSI model, '
                                              'inspecting full HTTP request data including URLs, headers, and request '
                                              'bodies. To stop SQL Injection and XSS, it uses rules and regular '
                                              'expressions from the OWASP Core Rule Set to detect SQL syntax like '
                                              "'UNION SELECT' or script tags like '<script>'. To stop Layer 7 DDoS "
                                              'attacks, it enforces rate-limiting rules to block IPs making too many '
                                              'requests to expensive endpoints, and uses IP reputation and CAPTCHA '
                                              'challenges to block automated bots. WAFs also allow virtual patching to '
                                              'block zero-day exploits at the edge.',
                               'missing_concepts': ['Layer 7 application-level inspection: Unlike network firewalls '
                                                    '(Layer 3/4 inspecting IP/port), a WAF inspects full HTTP/HTTPS '
                                                    'application payloads (headers, cookies, URIs, query parameters, '
                                                    'POST JSON/form bodies)']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'A WAF is a web application firewall that protects websites from '
                                              "hackers. It checks incoming HTTP requests for SQL injection like 'OR "
                                              "1=1' and XSS attacks like script tags in form fields. It also stops "
                                              'DDoS attacks by rate limiting IPs that send too many requests so the '
                                              "server doesn't crash. Cloudflare and AWS WAF are common examples. WAFs "
                                              'can block attacks before the request reaches your backend code.',
                               'missing_concepts': ['Layer 7 application-level inspection: Unlike network firewalls '
                                                    '(Layer 3/4 inspecting IP/port), a WAF inspects full HTTP/HTTPS '
                                                    'application payloads (headers, cookies, URIs, query parameters, '
                                                    'POST JSON/form bodies)',
                                                    'Virtual patching capability: Allows security teams to deploy '
                                                    'immediate edge WAF rules to neutralize zero-day CVEs across all '
                                                    'backend services in minutes before source code fixes can be '
                                                    'deployed']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': "A WAF is an antivirus software installed on the developer's laptop. It "
                                              'blocks SQL injection by deleting all SQL databases on the server. Layer '
                                              "7 DDoS attacks are mitigated by turning off the server's power switch.",
                               'missing_concepts': ['Layer 7 application-level inspection: Unlike network firewalls '
                                                    '(Layer 3/4 inspecting IP/port), a WAF inspects full HTTP/HTTPS '
                                                    'application payloads (headers, cookies, URIs, query parameters, '
                                                    'POST JSON/form bodies)',
                                                    'SQL Injection (SQLi) & XSS inspection: Uses signature matching, '
                                                    'regex heuristics, and lexical tokenization (e.g. ModSecurity Core '
                                                    'Rule Set) to detect SQL constructs (UNION SELECT, OR 1=1) and '
                                                    'script injection (<script>, javascript:, onerror=)',
                                                    'Layer 7 DDoS & bot mitigation: Enforces rate-limiting rules (e.g. '
                                                    'max 100 requests per 10s per IP), IP reputation scoring, '
                                                    'behavioral anomaly detection, and automated challenges (CAPTCHA / '
                                                    'JavaScript cryptographic proof-of-work)',
                                                    'Virtual patching capability: Allows security teams to deploy '
                                                    'immediate edge WAF rules to neutralize zero-day CVEs across all '
                                                    'backend services in minutes before source code fixes can be '
                                                    'deployed']}]},
          {'topic_tag': 'Module Federation Runtime Orchestration',
           'question': 'How does Webpack 5 Module Federation dynamically load remote micro-frontend containers at '
                       'runtime while sharing singleton dependencies?',
           'keywords': ['Module Federation',
                        'Webpack 5',
                        'Remote Containers',
                        'Shared Dependencies',
                        'Dynamic Imports',
                        'Runtime Script Loading'],
           'expected_concepts': ['Runtime container orchestration: Webpack 5 Module Federation allows a Host '
                                 'application to dynamically fetch and execute compiled code modules from independent '
                                 'Remote containers over HTTP at runtime without build-time coupling',
                                 'remoteEntry.js entry point: Each Remote exposes a lightweight manifest '
                                 "('remoteEntry.js') defining an interface with container.init() and container.get() "
                                 'to resolve exposed components',
                                 'Shared scope initialization: Host initializes a global shared scope '
                                 "(__webpack_init_sharing__('default')) and passes it to the remote container via "
                                 'container.init(), establishing a unified shared dependency pool',
                                 'Semantic version negotiation & Singletons: The shared scope evaluates semantic '
                                 "versioning rules; libraries configured with 'singleton: true' (such as React and "
                                 'React-DOM) guarantee that only a single instance exists at runtime, warning or '
                                 'failing on incompatible version drift'],
           'model_answer': 'Webpack 5 Module Federation enables multiple independent builds to form a single cohesive '
                           'application at runtime without sharing build processes or publishing private npm packages: '
                           '1. Architectural Concepts: - Host: The application that consumes remote modules. - Remote: '
                           'An independent build that exposes modules (components, utilities) to other applications. '
                           "An app can act as both Host and Remote simultaneously. 2. The 'remoteEntry.js' Manifest: "
                           "Each Remote build generates a lightweight entry manifest named 'remoteEntry.js'. When the "
                           "Host needs a remote component, it dynamically injects a '<script "
                           'src="https://remote.com/remoteEntry.js">\' tag into the document head. The script '
                           'registers a global container object exposing two core methods: - '
                           "'container.init(sharedScope)': Connects the remote container to the host's shared "
                           "dependency pool. - 'container.get(modulePath)': Returns a factory function that resolves "
                           'the requested component module asynchronously. 3. Shared Scope Orchestration: Before '
                           'consuming remotes, the Host executes \'__webpack_init_sharing__("default")\' to '
                           "instantiate an internal shared dependency scope ('__webpack_share_scopes__.default'). When "
                           "'container.init()' is called, the Remote registers its own available versions of shared "
                           'libraries into this shared scope. 4. Singleton Resolution and SemVer Negotiation: The '
                           'greatest challenge in micro-frontends is dependency duplication and multi-instance crashes '
                           '(e.g., two copies of React in memory breaks React Hooks). Module Federation solves this '
                           "via its 'shared' configuration: - 'shared: { react: { singleton: true, requiredVersion: "
                           '"^18.0.0" } }\'. - When both Host and Remote declare React as a shared singleton, the '
                           'runtime compares semantic versions: the highest compatible version available in the shared '
                           'pool is selected, and all sub-applications bind to that single shared in-memory instance, '
                           'eliminating duplicate downloads and preventing runtime crashes.',
           'sample_answers': [{'quality_level': 'excellent',
                               'human_score': 96,
                               'answer_text': 'Webpack 5 Module Federation enables independent micro-frontend builds '
                                              'to dynamically share code at runtime across the network. Here is how '
                                              'the runtime orchestration works under the hood: 1. The remoteEntry.js '
                                              'Container: Each remote application compiles a lightweight manifest '
                                              'called remoteEntry.js. When the host app loads a remote component—like '
                                              "'import('cartApp/Cart')'—Webpack dynamically injects a <script> tag to "
                                              "load 'cartApp's remoteEntry.js over HTTP. The remote entry script "
                                              "exposes a global container object with two vital methods: 'init()' and "
                                              "'get()'. 2. Initializing the Shared Scope: Before loading the "
                                              'component, the host initializes a global shared dependency pool using '
                                              "'__webpack_init_sharing__('default')'. It then calls "
                                              "'container.init(__webpack_share_scopes__.default)', passing its shared "
                                              'scope into the remote container. Both host and remote now share the '
                                              'same registry of loaded libraries. 3. Singleton and SemVer Negotiation: '
                                              'The hardest problem in micro-frontends is avoiding duplicate '
                                              'dependencies, especially React. If an app loads two separate copies of '
                                              'React, React Hooks will crash immediately because the internal '
                                              'dispatcher state is split. Module Federation solves this through its '
                                              "shared configuration: you set 'shared: { react: { singleton: true, "
                                              "requiredVersion: '^18.0.0' } }'. The Module Federation runtime inspects "
                                              'the shared scope, checks semantic versions, and ensures that only one '
                                              'single instance of React is ever instantiated in memory. 4. Component '
                                              "Instantiation: Finally, the host calls 'container.get('./Cart')', which "
                                              'returns a factory function that resolves the compiled component and '
                                              "renders it seamlessly into the host's virtual DOM.",
                               'missing_concepts': []},
                              {'quality_level': 'good',
                               'human_score': 83,
                               'answer_text': 'Webpack 5 Module Federation allows a host application to dynamically '
                                              'import components from remote micro-frontends at runtime over HTTP. '
                                              'Each remote build produces a remoteEntry.js file that exposes an init() '
                                              'and get() method. When the host imports a remote component, it '
                                              'downloads remoteEntry.js, initializes a shared scope with '
                                              'container.init(), and fetches the component with container.get(). For '
                                              "dependencies like React, you configure them with 'singleton: true' in "
                                              'the shared configuration, which ensures that only one instance of React '
                                              'is loaded in memory across all micro-frontends to prevent React Hooks '
                                              'from crashing.',
                               'missing_concepts': ['Shared scope initialization: Host initializes a global shared '
                                                    "scope (__webpack_init_sharing__('default')) and passes it to the "
                                                    'remote container via container.init(), establishing a unified '
                                                    'shared dependency pool']},
                              {'quality_level': 'average',
                               'human_score': 60,
                               'answer_text': 'Module Federation in Webpack 5 lets different React apps share '
                                              'components at runtime without using npm packages. The remote app '
                                              'creates a remoteEntry.js file that the host app downloads. It has a '
                                              'shared dependencies feature where you can mark React as a singleton so '
                                              'both apps use the same copy of React, preventing errors. When the user '
                                              'navigates to a page, the host app downloads the remote component over '
                                              'HTTP and renders it on screen.',
                               'missing_concepts': ['remoteEntry.js entry point: Each Remote exposes a lightweight '
                                                    "manifest ('remoteEntry.js') defining an interface with "
                                                    'container.init() and container.get() to resolve exposed '
                                                    'components',
                                                    'Shared scope initialization: Host initializes a global shared '
                                                    "scope (__webpack_init_sharing__('default')) and passes it to the "
                                                    'remote container via container.init(), establishing a unified '
                                                    'shared dependency pool']},
                              {'quality_level': 'poor',
                               'human_score': 25,
                               'answer_text': 'Module Federation is a government regulatory body for npm packages. It '
                                              'works by converting all React components into iframes at runtime. '
                                              'Singleton dependencies mean that only one user can visit the website at '
                                              'a time.',
                               'missing_concepts': ['Runtime container orchestration: Webpack 5 Module Federation '
                                                    'allows a Host application to dynamically fetch and execute '
                                                    'compiled code modules from independent Remote containers over '
                                                    'HTTP at runtime without build-time coupling',
                                                    'remoteEntry.js entry point: Each Remote exposes a lightweight '
                                                    "manifest ('remoteEntry.js') defining an interface with "
                                                    'container.init() and container.get() to resolve exposed '
                                                    'components',
                                                    'Shared scope initialization: Host initializes a global shared '
                                                    "scope (__webpack_init_sharing__('default')) and passes it to the "
                                                    'remote container via container.init(), establishing a unified '
                                                    'shared dependency pool',
                                                    'Semantic version negotiation & Singletons: The shared scope '
                                                    'evaluates semantic versioning rules; libraries configured with '
                                                    "'singleton: true' (such as React and React-DOM) guarantee that "
                                                    'only a single instance exists at runtime, warning or failing on '
                                                    'incompatible version drift']}]}]}

