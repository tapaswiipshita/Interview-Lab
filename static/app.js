/**
 * INTERVIEW LAB — Pure Monochrome Single-Page Application
 * Minimalist, precise, developer-focused interview evaluation engine.
 * Adheres strictly to zero gradients, zero emojis, and zero non-functional decoration.
 */

(() => {
  'use strict';

  // ============================================================================
  // CONFIGURATION & DEMO BENCHMARK DATA
  // ============================================================================

  const CONFIG = {
    apiBaseUrl: window.location.origin,
    defaultDomain: 'Web Development',
    defaultDifficulty: 'medium',
    defaultQuestionCount: 5,
    maxRecordingSeconds: 180
  };

  // Curated demo profile for offline testing and quick onboarding
  const DEMO_PROFILE = {
    is_demo: true,
    candidate_name: 'Alex Rivera',
    email: 'alex.rivera@example.com',
    phone: '+1 (555) 019-2834',
    filename: 'alex_rivera_resume.pdf',
    suggested_domain: 'Web Development',
    extracted_skills: [
      'React', 'TypeScript', 'FastAPI', 'Node.js', 'PostgreSQL',
      'Docker', 'Redis', 'REST API', 'GraphQL', 'Git', 'Tailwind'
    ],
    projects: [
      'Real-Time Collaborative Code Editor (WebSockets, FastAPI, React)',
      'Distributed Task Processing Pipeline (Redis, Celery, PostgreSQL)'
    ],
    education: [
      'B.S. in Computer Science — University of California, Berkeley'
    ]
  };

  // Demo fallback questions for offline or simulated mode
  const DEMO_QUESTIONS = [
    {
      question_id: 'demo_q_web_001',
      question: "Explain how React's Fiber reconciliation algorithm schedules updates and prioritizes work.",
      topic: 'React Virtual DOM & Fiber',
      domain: 'Web Development',
      difficulty: 'medium',
      reference_answer: 'React Fiber breaks reconciliation into incremental units of work. It splits execution into an interruptible render/reconciliation phase that builds an alternate fiber tree with time-slicing, and a synchronous commit phase that updates the DOM.',
      expected_concepts: [
        'Fiber tree decomposition into incremental work units',
        'Two-phase execution: interruptible render phase vs synchronous commit phase',
        'Time-slicing and cooperative scheduling via requestIdleCallback or MessageChannel',
        'Priority assignment for user interactions over background updates'
      ]
    },
    {
      question_id: 'demo_q_web_002',
      question: "Why is the cleanup function essential in React's useEffect hook?",
      topic: 'React useEffect Hook Cleanup',
      domain: 'Web Development',
      difficulty: 'medium',
      reference_answer: 'The cleanup function in useEffect runs before the component unmounts and before re-running the effect on dependency change. It prevents memory leaks from uncancelled subscriptions, timers, or event listeners.',
      expected_concepts: [
        'Executes before unmounting and prior to re-execution when dependencies change',
        'Prevents memory leaks from orphaned event listeners or pending async requests',
        'Cancels stale API subscriptions and invalidates in-flight abort controllers',
        'Avoids race conditions where slow network responses overwrite newer state'
      ]
    },
    {
      question_id: 'demo_q_web_003',
      question: 'Compare Redux Toolkit, Context API, and Zustand for state management.',
      topic: 'State Management Comparison',
      domain: 'Web Development',
      difficulty: 'medium',
      reference_answer: 'Context API is built-in for low-frequency global data but causes re-renders in all consuming components. Redux Toolkit provides predictable centralized state with DevTools and middleware but requires boilerplate. Zustand offers a minimal store based on hooks with selector subscriptions preventing unnecessary renders.',
      expected_concepts: [
        'Context API re-renders all consumers without granular selector subscriptions',
        'Redux Toolkit provides centralized immutable state with devtools and middleware',
        'Zustand utilizes hook-based selective subscription to prevent unnecessary renders',
        'Trade-off between architectural boilerplate and fine-grained re-render control'
      ]
    }
  ];

  // ============================================================================
  // APPLICATION STATE
  // ============================================================================

  const AppState = {
    currentView: 'landing', // 'landing' | 'setup' | 'interview' | 'report'
    
    // Setup state
    candidateProfile: null,
    selectedDomain: 'Web Development',
    selectedDifficulty: 'medium',
    selectedCount: 5,

    // Active session state
    sessionId: null,
    isDemoSession: false,
    questions: [],
    currentIndex: 0,
    answers: [],
    latestEvaluation: null,
    finalReport: null,

    // Voice & Media state
    isRecording: false,
    mediaRecorder: null,
    audioChunks: [],
    recordedBlob: null,
    recordedAudioUrl: null,
    recordingTimer: null,
    recordingSeconds: 0,
    speechRecognition: null,
    transcriptText: '',
    waveformInterval: null
  };

  // ============================================================================
  // API SERVICE LAYER
  // ============================================================================

  const ApiService = {
    async checkHealth() {
      try {
        const res = await fetch(`${CONFIG.apiBaseUrl}/api/health`, { method: 'GET' });
        if (!res.ok) throw new Error('Health check returned non-200');
        return await res.json();
      } catch (err) {
        console.warn('API health check offline, fallback enabled:', err.message);
        return { status: 'offline', transcription_provider: 'Native Browser Web Speech API' };
      }
    },

    async uploadResume(file) {
      const formData = new FormData();
      formData.append('file', file);

      const res = await fetch(`${CONFIG.apiBaseUrl}/api/resume/upload`, {
        method: 'POST',
        body: formData
      });

      if (!res.ok) {
        const errData = await res.json().catch(() => ({}));
        throw new Error(errData.detail || 'Failed to upload and parse resume.');
      }
      return await res.json();
    },

    async startInterview({ domain, difficulty, question_count, candidate_profile }) {
      const res = await fetch(`${CONFIG.apiBaseUrl}/api/interview/start`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          domain,
          difficulty,
          question_count,
          candidate_profile
        })
      });

      if (!res.ok) {
        const errData = await res.json().catch(() => ({}));
        throw new Error(errData.detail || 'Failed to initialize interview session.');
      }
      return await res.json();
    },

    async submitAnswer(sessionId, transcribedAnswer) {
      const res = await fetch(`${CONFIG.apiBaseUrl}/api/interview/${sessionId}/answer`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ transcribed_answer: transcribedAnswer })
      });

      if (!res.ok) {
        const errData = await res.json().catch(() => ({}));
        throw new Error(errData.detail || 'Evaluation failed on submission.');
      }
      return await res.json();
    },

    async getFinalReport(sessionId) {
      const res = await fetch(`${CONFIG.apiBaseUrl}/api/interview/${sessionId}/report`, {
        method: 'GET'
      });

      if (!res.ok) {
        const errData = await res.json().catch(() => ({}));
        throw new Error(errData.detail || 'Failed to retrieve final report.');
      }
      return await res.json();
    }
  };

  // ============================================================================
  // DOM REFERENCES
  // ============================================================================

  const DOM = {
    // Nav & System
    systemHealthBadge: document.getElementById('systemHealthBadge'),
    systemHealthDot: document.getElementById('systemHealthDot'),
    systemHealthText: document.getElementById('systemHealthText'),
    navBrandLink: document.getElementById('navBrandLink'),
    navStartBtn: document.getElementById('navStartBtn'),
    heroStartBtn: document.getElementById('heroStartBtn'),
    closingStartBtn: document.getElementById('closingStartBtn'),

    // Views
    viewLanding: document.getElementById('viewLanding'),
    viewSetup: document.getElementById('viewSetup'),
    viewInterview: document.getElementById('viewInterview'),
    viewReport: document.getElementById('viewReport'),

    // Setup: Resume
    setupBackToLandingBtn: document.getElementById('setupBackToLandingBtn'),
    uploadDropzone: document.getElementById('uploadDropzone'),
    resumeFileInput: document.getElementById('resumeFileInput'),
    browseFileBtn: document.getElementById('browseFileBtn'),
    fileUploadedCard: document.getElementById('fileUploadedCard'),
    uploadedFileName: document.getElementById('uploadedFileName'),
    uploadedFileSize: document.getElementById('uploadedFileSize'),
    replaceFileBtn: document.getElementById('replaceFileBtn'),
    removeFileBtn: document.getElementById('removeFileBtn'),
    parsedProfilePanel: document.getElementById('parsedProfilePanel'),
    profileCandidateName: document.getElementById('profileCandidateName'),
    profileProvenanceTag: document.getElementById('profileProvenanceTag'),
    profileSuggestedDomain: document.getElementById('profileSuggestedDomain'),
    profileSkillsCount: document.getElementById('profileSkillsCount'),
    profileSkillsContainer: document.getElementById('profileSkillsContainer'),
    profileProjectsSection: document.getElementById('profileProjectsSection'),
    profileProjectsList: document.getElementById('profileProjectsList'),
    useDemoProfileBtn: document.getElementById('useDemoProfileBtn'),
    profileStatusBadge: document.getElementById('profileStatusBadge'),
    setupErrorNotice: document.getElementById('setupErrorNotice'),

    // Setup: Configuration
    domainSelector: document.getElementById('domainSelector'),
    difficultySelector: document.getElementById('difficultySelector'),
    questionCountSelector: document.getElementById('questionCountSelector'),
    summaryDomain: document.getElementById('summaryDomain'),
    summaryDifficulty: document.getElementById('summaryDifficulty'),
    summaryQuestions: document.getElementById('summaryQuestions'),
    summaryPersonalization: document.getElementById('summaryPersonalization'),
    generateInterviewBtn: document.getElementById('generateInterviewBtn'),

    // Interview Room
    roomDomainBadge: document.getElementById('roomDomainBadge'),
    roomDifficultyBadge: document.getElementById('roomDifficultyBadge'),
    exitInterviewBtn: document.getElementById('exitInterviewBtn'),
    interviewProgressThumb: document.getElementById('interviewProgressThumb'),
    questionCounterText: document.getElementById('questionCounterText'),
    questionTopicTag: document.getElementById('questionTopicTag'),
    interviewQuestionText: document.getElementById('interviewQuestionText'),
    recStatusDot: document.getElementById('recStatusDot'),
    recStatusText: document.getElementById('recStatusText'),
    recTimerClock: document.getElementById('recTimerClock'),
    recWaveformContainer: document.getElementById('recWaveformContainer'),
    micErrorNotice: document.getElementById('micErrorNotice'),
    micErrorMsg: document.getElementById('micErrorMsg'),
    startRecordingBtn: document.getElementById('startRecordingBtn'),
    stopRecordingBtn: document.getElementById('stopRecordingBtn'),
    retryRecordingBtn: document.getElementById('retryRecordingBtn'),
    audioPlayerWrap: document.getElementById('audioPlayerWrap'),
    recordedAudioElement: document.getElementById('recordedAudioElement'),
    sttProviderBadge: document.getElementById('sttProviderBadge'),
    answerTranscriptInput: document.getElementById('answerTranscriptInput'),
    submitAnswerBtn: document.getElementById('submitAnswerBtn'),

    // Post-Submission Feedback
    questionFeedbackCard: document.getElementById('questionFeedbackCard'),
    fbScoreTag: document.getElementById('fbScoreTag'),
    fbCoverageVal: document.getElementById('fbCoverageVal'),
    fbSimilarityVal: document.getElementById('fbSimilarityVal'),
    fbCoveredList: document.getElementById('fbCoveredList'),
    fbMissingList: document.getElementById('fbMissingList'),
    fbMisconceptionsSection: document.getElementById('fbMisconceptionsSection'),
    fbMisconceptionsText: document.getElementById('fbMisconceptionsText'),
    fbModelAnswerText: document.getElementById('fbModelAnswerText'),
    nextQuestionBtn: document.getElementById('nextQuestionBtn'),
    nextQuestionBtnText: document.getElementById('nextQuestionBtnText'),

    // Final Report
    reportCandidateName: document.getElementById('reportCandidateName'),
    reportDomain: document.getElementById('reportDomain'),
    reportDifficulty: document.getElementById('reportDifficulty'),
    reportSessionId: document.getElementById('reportSessionId'),
    reportOverallScore: document.getElementById('reportOverallScore'),
    reportOverallTier: document.getElementById('reportOverallTier'),
    reportCompletedCount: document.getElementById('reportCompletedCount'),
    reportTopicBars: document.getElementById('reportTopicBars'),
    reportStrongAreas: document.getElementById('reportStrongAreas'),
    reportWeakAreas: document.getElementById('reportWeakAreas'),
    reportRecommendationsList: document.getElementById('reportRecommendationsList'),
    reportHistoryTableBody: document.getElementById('reportHistoryTableBody'),
    reportPrintBtn: document.getElementById('reportPrintBtn'),
    reportRestartBtn: document.getElementById('reportRestartBtn'),

    // Modal
    questionDetailModal: document.getElementById('questionDetailModal'),
    modalQuestionTitle: document.getElementById('modalQuestionTitle'),
    modalPrompt: document.getElementById('modalPrompt'),
    modalTranscribed: document.getElementById('modalTranscribed'),
    modalModelAnswer: document.getElementById('modalModelAnswer'),
    modalConceptsBreakdown: document.getElementById('modalConceptsBreakdown'),
    closeModalBtn: document.getElementById('closeModalBtn'),
    modalCloseActionBtn: document.getElementById('modalCloseActionBtn')
  };

  // ============================================================================
  // NAVIGATION & VIEW SWITCHING
  // ============================================================================

  function switchView(viewName) {
    AppState.currentView = viewName;
    const views = [
      { name: 'landing', el: DOM.viewLanding },
      { name: 'setup', el: DOM.viewSetup },
      { name: 'interview', el: DOM.viewInterview },
      { name: 'report', el: DOM.viewReport }
    ];

    views.forEach(v => {
      if (v.name === viewName) {
        v.el.classList.add('active');
      } else {
        v.el.classList.remove('active');
      }
    });

    // Window scroll reset for clean view transition
    window.scrollTo({ top: 0, behavior: 'instant' });
  }

  // ============================================================================
  // WAVEFORM GENERATOR & SIMULATION (MONOCHROME)
  // ============================================================================

  function buildWaveformBars() {
    DOM.recWaveformContainer.innerHTML = '';
    const barCount = 36;
    for (let i = 0; i < barCount; i++) {
      const bar = document.createElement('div');
      bar.className = 'waveform-bar';
      DOM.recWaveformContainer.appendChild(bar);
    }
  }

  function startWaveformAnimation() {
    stopWaveformAnimation();
    const bars = DOM.recWaveformContainer.querySelectorAll('.waveform-bar');
    AppState.waveformInterval = setInterval(() => {
      bars.forEach(bar => {
        const height = Math.floor(Math.random() * 24) + 4;
        bar.style.height = `${height}px`;
        bar.classList.add('live-active');
      });
    }, 100);
  }

  function stopWaveformAnimation() {
    if (AppState.waveformInterval) {
      clearInterval(AppState.waveformInterval);
      AppState.waveformInterval = null;
    }
    const bars = DOM.recWaveformContainer.querySelectorAll('.waveform-bar');
    bars.forEach(bar => {
      bar.style.height = '4px';
      bar.classList.remove('live-active');
    });
  }

  // ============================================================================
  // RESUME UPLOAD & PROFILE MANAGEMENT
  // ============================================================================

  function displayProfile(profile) {
    AppState.candidateProfile = profile;
    DOM.profileCandidateName.textContent = profile.candidate_name || 'Candidate';
    
    // Distinguish actual extracted info from demo data
    if (profile.is_demo) {
      DOM.profileProvenanceTag.textContent = 'Sample Demo Profile';
      DOM.profileStatusBadge.textContent = 'Demo Profile Active';
    } else {
      DOM.profileProvenanceTag.textContent = `Extracted from ${profile.filename || 'uploaded document'}`;
      DOM.profileStatusBadge.textContent = 'Resume Attached';
    }

    // Suggested Domain
    const suggested = profile.suggested_domain || 'Web Development';
    DOM.profileSuggestedDomain.textContent = suggested;
    
    // Auto-select suggested domain in config
    selectDomain(suggested);

    // Skills
    const skills = profile.extracted_skills || [];
    DOM.profileSkillsCount.textContent = skills.length;
    DOM.profileSkillsContainer.innerHTML = '';
    
    if (skills.length > 0) {
      skills.forEach(skill => {
        const tag = document.createElement('span');
        tag.className = 'tag-item';
        tag.textContent = skill;
        DOM.profileSkillsContainer.appendChild(tag);
      });
    } else {
      DOM.profileSkillsContainer.innerHTML = '<span style="font-size: 0.75rem; color: var(--text-muted);">No specific technical keywords isolated.</span>';
    }

    // Projects
    const projects = profile.projects || [];
    if (projects.length > 0) {
      DOM.profileProjectsSection.style.display = 'block';
      DOM.profileProjectsList.innerHTML = projects.map(p => `• ${escapeHtml(p)}`).join('<br>');
    } else {
      DOM.profileProjectsSection.style.display = 'none';
    }

    // Update Dropzone / Card state
    DOM.uploadDropzone.style.display = 'none';
    DOM.fileUploadedCard.classList.add('active');
    DOM.uploadedFileName.textContent = profile.filename || 'resume.pdf';
    DOM.uploadedFileSize.textContent = profile.file_size || (profile.is_demo ? 'Demo Asset' : 'Verified');
    DOM.parsedProfilePanel.classList.add('active');

    // Update Summary
    DOM.summaryPersonalization.textContent = profile.is_demo
      ? `Tailored to ${profile.candidate_name} (Sample)`
      : `Tailored to ${profile.candidate_name}`;
  }

  function clearProfile() {
    AppState.candidateProfile = null;
    DOM.uploadDropzone.style.display = 'block';
    DOM.fileUploadedCard.classList.remove('active');
    DOM.parsedProfilePanel.classList.remove('active');
    DOM.profileStatusBadge.textContent = 'No Resume Attached';
    DOM.summaryPersonalization.textContent = 'General Benchmark';
    DOM.resumeFileInput.value = '';
  }

  async function handleFileUpload(file) {
    if (!file) return;

    // Validate size (10MB)
    if (file.size > 10 * 1024 * 1024) {
      showSetupError('File exceeds 10MB limit. Please upload a smaller document.');
      return;
    }

    hideSetupError();
    DOM.uploadDropzone.style.opacity = '0.5';

    try {
      const parsedData = await ApiService.uploadResume(file);
      parsedData.file_size = `${(file.size / 1024).toFixed(1)} KB`;
      parsedData.is_demo = false;
      displayProfile(parsedData);
    } catch (err) {
      console.warn('Backend parse failed, offering fallback:', err.message);
      showSetupError(`Upload note: ${err.message}. You may use the sample profile or proceed directly.`);
    } finally {
      DOM.uploadDropzone.style.opacity = '1';
    }
  }

  function showSetupError(msg) {
    DOM.setupErrorNotice.textContent = msg;
    DOM.setupErrorNotice.style.display = 'block';
  }

  function hideSetupError() {
    DOM.setupErrorNotice.style.display = 'none';
    DOM.setupErrorNotice.textContent = '';
  }

  // ============================================================================
  // INTERVIEW SETUP CONFIGURATION
  // ============================================================================

  function selectDomain(domainName) {
    AppState.selectedDomain = domainName;
    const buttons = DOM.domainSelector.querySelectorAll('.segment-btn');
    buttons.forEach(btn => {
      if (btn.getAttribute('data-domain').toLowerCase() === domainName.toLowerCase()) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });
    DOM.summaryDomain.textContent = domainName;
  }

  function selectDifficulty(diff) {
    AppState.selectedDifficulty = diff;
    const buttons = DOM.difficultySelector.querySelectorAll('.segment-btn');
    buttons.forEach(btn => {
      if (btn.getAttribute('data-difficulty') === diff) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });
    DOM.summaryDifficulty.textContent = diff.charAt(0).toUpperCase() + diff.slice(1);
  }

  function selectQuestionCount(cnt) {
    AppState.selectedCount = parseInt(cnt, 10);
    const buttons = DOM.questionCountSelector.querySelectorAll('.segment-btn');
    buttons.forEach(btn => {
      if (parseInt(btn.getAttribute('data-count'), 10) === AppState.selectedCount) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });
    DOM.summaryQuestions.textContent = `${AppState.selectedCount} Questions`;
  }

  async function generateInterviewSession() {
    hideSetupError();
    DOM.generateInterviewBtn.disabled = true;
    DOM.generateInterviewBtn.innerHTML = '<span>Configuring Assessment...</span>';

    try {
      const payload = {
        domain: AppState.selectedDomain,
        difficulty: AppState.selectedDifficulty,
        question_count: AppState.selectedCount,
        candidate_profile: AppState.candidateProfile || {}
      };

      let startRes;
      try {
        startRes = await ApiService.startInterview(payload);
        AppState.sessionId = startRes.session_id;
        AppState.isDemoSession = false;
        
        // Populate session questions
        AppState.currentIndex = 0;
        AppState.answers = [];
        
        // Load initial question
        setupInterviewRoom(startRes.current_question, startRes.total_questions);
      } catch (err) {
        console.warn('Real backend unavailable, starting clearly labelled demo mode:', err.message);
        // Fallback to Demo Mode
        AppState.sessionId = `demo_${Date.now().toString(36)}`;
        AppState.isDemoSession = true;
        AppState.questions = DEMO_QUESTIONS.slice(0, AppState.selectedCount);
        AppState.currentIndex = 0;
        AppState.answers = [];

        const q1 = AppState.questions[0];
        setupInterviewRoom({
          question_index: 1,
          total_questions: AppState.questions.length,
          question: q1.question,
          topic: q1.topic,
          domain: AppState.selectedDomain,
          difficulty: AppState.selectedDifficulty
        }, AppState.questions.length);
      }

      switchView('interview');
    } catch (finalErr) {
      showSetupError(`Interview generation failed: ${finalErr.message}`);
    } finally {
      DOM.generateInterviewBtn.disabled = false;
      DOM.generateInterviewBtn.innerHTML = `
        <span>Generate Interview</span>
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M5 12h14M12 5l7 7-7 7"/>
        </svg>
      `;
    }
  }

  // ============================================================================
  // INTERVIEW ROOM & VOICE RECORDING
  // ============================================================================

  function setupInterviewRoom(questionData, totalCount) {
    DOM.roomDomainBadge.textContent = AppState.selectedDomain;
    DOM.roomDifficultyBadge.textContent = AppState.selectedDifficulty.toUpperCase();

    const currIdx = questionData.question_index || (AppState.currentIndex + 1);
    const total = totalCount || AppState.selectedCount;

    DOM.questionCounterText.textContent = `Question ${currIdx} of ${total}`;
    DOM.questionTopicTag.textContent = questionData.topic || 'General Architecture';
    DOM.interviewQuestionText.textContent = questionData.question;

    // Progress bar calculation
    const progressPct = Math.round(((currIdx - 1) / total) * 100);
    DOM.interviewProgressThumb.style.width = `${progressPct}%`;

    // Reset recording workspace for the new question
    resetRecordingWorkspace();
  }

  function resetRecordingWorkspace() {
    stopRecording(true);
    AppState.transcriptText = '';
    AppState.audioChunks = [];
    AppState.recordedBlob = null;
    if (AppState.recordedAudioUrl) {
      URL.revokeObjectURL(AppState.recordedAudioUrl);
      AppState.recordedAudioUrl = null;
    }

    DOM.answerTranscriptInput.value = '';
    DOM.recTimerClock.textContent = '00:00';
    DOM.recStatusDot.className = 'status-pulsing-dot';
    DOM.recStatusText.textContent = 'Microphone Ready';
    DOM.startRecordingBtn.style.display = 'inline-flex';
    DOM.stopRecordingBtn.style.display = 'none';
    DOM.retryRecordingBtn.style.display = 'none';
    DOM.audioPlayerWrap.classList.remove('active');
    DOM.micErrorNotice.classList.remove('active');
    DOM.questionFeedbackCard.classList.remove('active');
    DOM.submitAnswerBtn.disabled = false;
    DOM.submitAnswerBtn.style.display = 'inline-flex';
    
    stopWaveformAnimation();
  }

  async function startRecording() {
    DOM.micErrorNotice.classList.remove('active');

    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      AppState.audioChunks = [];

      // Initialize MediaRecorder
      const options = MediaRecorder.isTypeSupported('audio/webm')
        ? { mimeType: 'audio/webm' }
        : {};
      AppState.mediaRecorder = new MediaRecorder(stream, options);

      AppState.mediaRecorder.ondataavailable = (e) => {
        if (e.data && e.data.size > 0) {
          AppState.audioChunks.push(e.data);
        }
      };

      AppState.mediaRecorder.onstop = () => {
        AppState.recordedBlob = new Blob(AppState.audioChunks, { type: 'audio/webm' });
        AppState.recordedAudioUrl = URL.createObjectURL(AppState.recordedBlob);
        DOM.recordedAudioElement.src = AppState.recordedAudioUrl;
        DOM.audioPlayerWrap.classList.add('active');
        
        // Stop all audio tracks to release microphone cleanly
        stream.getTracks().forEach(track => track.stop());
      };

      AppState.mediaRecorder.start(250);
      AppState.isRecording = true;

      // Initialize Web Speech API for real-time client transcription
      initSpeechRecognition();

      // UI state
      DOM.startRecordingBtn.style.display = 'none';
      DOM.stopRecordingBtn.style.display = 'inline-flex';
      DOM.retryRecordingBtn.style.display = 'none';
      DOM.recStatusDot.className = 'status-pulsing-dot active-recording';
      DOM.recStatusText.textContent = 'Recording in Progress';

      startTimer();
      startWaveformAnimation();
    } catch (err) {
      console.warn('Microphone access denied or unsupported:', err);
      DOM.micErrorMsg.textContent = 'Microphone access is blocked or unavailable. You can type your answer directly into the response box below.';
      DOM.micErrorNotice.classList.add('active');
      DOM.recStatusText.textContent = 'Manual Text Mode';
    }
  }

  function initSpeechRecognition() {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
      DOM.sttProviderBadge.textContent = 'Speech API Unavailable — Manual Input Active';
      return;
    }

    try {
      AppState.speechRecognition = new SpeechRecognition();
      AppState.speechRecognition.continuous = true;
      AppState.speechRecognition.interimResults = true;
      AppState.speechRecognition.lang = 'en-US';

      AppState.speechRecognition.onresult = (event) => {
        let interim = '';
        let final = '';

        for (let i = 0; i < event.results.length; ++i) {
          if (event.results[i].isFinal) {
            final += event.results[i][0].transcript + ' ';
          } else {
            interim += event.results[i][0].transcript;
          }
        }

        const combined = (final + interim).trim();
        if (combined) {
          DOM.answerTranscriptInput.value = combined;
          AppState.transcriptText = combined;
        }
      };

      AppState.speechRecognition.onerror = (e) => {
        console.warn('SpeechRecognition event:', e.error);
      };

      AppState.speechRecognition.start();
      DOM.sttProviderBadge.textContent = 'Speech API Transcribing Live';
    } catch (e) {
      console.warn('Could not launch SpeechRecognition:', e);
    }
  }

  function stopRecording(cancelled = false) {
    if (!AppState.isRecording) return;
    AppState.isRecording = false;

    if (AppState.mediaRecorder && AppState.mediaRecorder.state !== 'inactive') {
      AppState.mediaRecorder.stop();
    }

    if (AppState.speechRecognition) {
      try { AppState.speechRecognition.stop(); } catch (_) {}
      AppState.speechRecognition = null;
    }

    stopTimer();
    stopWaveformAnimation();

    if (!cancelled) {
      DOM.stopRecordingBtn.style.display = 'none';
      DOM.retryRecordingBtn.style.display = 'inline-flex';
      DOM.startRecordingBtn.style.display = 'none';
      DOM.recStatusDot.className = 'status-pulsing-dot';
      DOM.recStatusText.textContent = 'Recording Complete — Review Transcript';
    }
  }

  function startTimer() {
    stopTimer();
    AppState.recordingSeconds = 0;
    DOM.recTimerClock.textContent = '00:00';

    AppState.recordingTimer = setInterval(() => {
      AppState.recordingSeconds++;
      const mins = String(Math.floor(AppState.recordingSeconds / 60)).padStart(2, '0');
      const secs = String(AppState.recordingSeconds % 60).padStart(2, '0');
      DOM.recTimerClock.textContent = `${mins}:${secs}`;

      if (AppState.recordingSeconds >= CONFIG.maxRecordingSeconds) {
        stopRecording();
      }
    }, 1000);
  }

  function stopTimer() {
    if (AppState.recordingTimer) {
      clearInterval(AppState.recordingTimer);
      AppState.recordingTimer = null;
    }
  }

  // ============================================================================
  // EVALUATION & FEEDBACK RENDERING
  // ============================================================================

  async function submitAnswer() {
    // If currently recording, stop it first
    if (AppState.isRecording) {
      stopRecording();
    }

    const answerText = (DOM.answerTranscriptInput.value || '').trim();
    if (!answerText) {
      DOM.micErrorMsg.textContent = 'Please record or type a technical answer before submitting for evaluation.';
      DOM.micErrorNotice.classList.add('active');
      return;
    }

    DOM.submitAnswerBtn.disabled = true;
    DOM.submitAnswerBtn.innerHTML = '<span>Evaluating Response...</span>';

    try {
      let evalData;

      if (!AppState.isDemoSession && AppState.sessionId) {
        // Real Backend submission
        const res = await ApiService.submitAnswer(AppState.sessionId, answerText);
        evalData = res.evaluation;
        AppState.latestEvaluation = evalData;
        AppState.answers.push({
          question_index: res.question_index,
          score: evalData.score,
          quality_level: evalData.quality_level,
          evaluation: evalData,
          transcribed_answer: answerText
        });

        renderFeedback(evalData, res.has_next_question);
      } else {
        // Demo session simulated evaluation (accurate schema matching)
        evalData = simulateDemoEvaluation(answerText, AppState.currentIndex);
        AppState.latestEvaluation = evalData;
        AppState.answers.push({
          question_index: AppState.currentIndex + 1,
          score: evalData.score,
          quality_level: evalData.quality_level,
          evaluation: evalData,
          transcribed_answer: answerText
        });

        const hasNext = (AppState.currentIndex + 1) < AppState.selectedCount;
        renderFeedback(evalData, hasNext);
      }

      // Smooth scroll to feedback card
      DOM.questionFeedbackCard.scrollIntoView({ behavior: 'smooth', block: 'start' });
    } catch (err) {
      DOM.micErrorMsg.textContent = `Evaluation failed: ${err.message}`;
      DOM.micErrorNotice.classList.add('active');
      DOM.submitAnswerBtn.disabled = false;
      DOM.submitAnswerBtn.innerHTML = '<span>Submit Answer for Evaluation</span>';
    }
  }

  function simulateDemoEvaluation(candidateText, qIndex) {
    const q = DEMO_QUESTIONS[qIndex % DEMO_QUESTIONS.length];
    const words = candidateText.toLowerCase().split(/\s+/);
    
    // Heuristic concept matching
    const covered = [];
    const missing = [];

    q.expected_concepts.forEach(concept => {
      const conceptTokens = concept.toLowerCase().split(/\s+/);
      const matchCount = conceptTokens.filter(t => t.length > 3 && words.includes(t)).length;
      if (matchCount >= 2 || words.length > 50) {
        covered.push(concept);
      } else {
        missing.push(concept);
      }
    });

    if (covered.length === 0 && q.expected_concepts.length > 0) {
      covered.push(q.expected_concepts[0]);
      missing.shift();
    }

    const coverageRatio = covered.length / Math.max(1, q.expected_concepts.length);
    const score = Math.min(100, Math.round(coverageRatio * 85 + (words.length > 30 ? 12 : 5)));
    const tier = score >= 90 ? 'excellent' : (score >= 70 ? 'good' : (score >= 50 ? 'average' : 'poor'));

    return {
      score: score,
      quality_level: tier,
      coverage_score: coverageRatio,
      covered_concepts: covered,
      missing_concepts: missing,
      misconceptions: [],
      warnings: [],
      strengths: [`Covered ${covered.length} key concept(s) cleanly.`],
      improvements: missing.length > 0 ? [`Omitted ${missing.length} expected assertion(s).`] : ['Excellent breadth of coverage.'],
      reference_answer: q.reference_answer
    };
  }

  function renderFeedback(evalData, hasNextQuestion) {
    DOM.questionFeedbackCard.classList.add('active');

    // Score & Quality Badge
    const score = evalData.score || 0;
    const tier = (evalData.quality_level || 'average').toUpperCase();
    DOM.fbScoreTag.textContent = `${score} / 100 · ${tier}`;

    // Coverage & Similarity
    const cov = Math.round((evalData.coverage_score || 0) * 100);
    DOM.fbCoverageVal.textContent = `${cov}%`;
    const sim = evalData.semantic_similarity
      ? Math.round(evalData.semantic_similarity * 100)
      : Math.min(95, Math.round(cov * 0.9 + 8));
    DOM.fbSimilarityVal.textContent = `${sim}%`;

    // What You Got Right (Covered Concepts)
    DOM.fbCoveredList.innerHTML = '';
    const covered = evalData.covered_concepts || [];
    if (covered.length > 0) {
      covered.forEach(item => {
        const text = typeof item === 'object' ? item.concept : item;
        const li = document.createElement('li');
        li.className = 'concept-bullet-item';
        li.innerHTML = `
          <svg class="icon-bullet" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2">
            <polyline points="3 8.5 6.5 12 13 4.5"></polyline>
          </svg>
          <span>${escapeHtml(text)}</span>
        `;
        DOM.fbCoveredList.appendChild(li);
      });
    } else {
      DOM.fbCoveredList.innerHTML = '<li class="concept-bullet-item"><span>No required technical assertions were addressed.</span></li>';
    }

    // What Needs Improvement (Missing Concepts)
    DOM.fbMissingList.innerHTML = '';
    const missing = evalData.missing_concepts || [];
    if (missing.length > 0) {
      missing.forEach(text => {
        const li = document.createElement('li');
        li.className = 'concept-bullet-item missing';
        li.innerHTML = `
          <svg class="icon-bullet" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2">
            <line x1="3" y1="8" x2="13" y2="8"></line>
          </svg>
          <span>${escapeHtml(text)}</span>
        `;
        DOM.fbMissingList.appendChild(li);
      });
    } else {
      DOM.fbMissingList.innerHTML = '<li class="concept-bullet-item"><span>All expected concepts successfully covered.</span></li>';
    }

    // Misconceptions
    const misconceptions = evalData.misconceptions || [];
    if (misconceptions.length > 0) {
      DOM.fbMisconceptionsSection.style.display = 'block';
      DOM.fbMisconceptionsText.textContent = misconceptions.join('; ');
    } else {
      DOM.fbMisconceptionsSection.style.display = 'none';
    }

    // Reference Model Answer
    DOM.fbModelAnswerText.textContent = evalData.reference_answer || 'Reference answer archived in syllabus.';

    // Next Question Button state
    if (hasNextQuestion) {
      DOM.nextQuestionBtnText.textContent = 'Proceed to Next Question';
    } else {
      DOM.nextQuestionBtnText.textContent = 'View Final Assessment Report';
    }

    DOM.submitAnswerBtn.style.display = 'none';
  }

  async function handleNextQuestion() {
    AppState.currentIndex++;
    const total = AppState.selectedCount;

    if (AppState.currentIndex < total) {
      if (!AppState.isDemoSession && AppState.sessionId) {
        // Fetch next question from server
        try {
          const res = await fetch(`${CONFIG.apiBaseUrl}/api/interview/${AppState.sessionId}/question`);
          const qData = await res.json();
          setupInterviewRoom(qData, total);
        } catch (e) {
          console.warn('Failed to load next question from server, generating next:', e);
          const fallbackQ = DEMO_QUESTIONS[AppState.currentIndex % DEMO_QUESTIONS.length];
          setupInterviewRoom(fallbackQ, total);
        }
      } else {
        const nextQ = DEMO_QUESTIONS[AppState.currentIndex % DEMO_QUESTIONS.length];
        setupInterviewRoom({
          question_index: AppState.currentIndex + 1,
          total_questions: total,
          question: nextQ.question,
          topic: nextQ.topic,
          domain: AppState.selectedDomain,
          difficulty: AppState.selectedDifficulty
        }, total);
      }

      window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
      // Completed interview, show Final Report
      await loadFinalReport();
    }
  }

  // ============================================================================
  // FINAL INTERVIEW REPORT
  // ============================================================================

  async function loadFinalReport() {
    let report;

    if (!AppState.isDemoSession && AppState.sessionId) {
      try {
        report = await ApiService.getFinalReport(AppState.sessionId);
      } catch (err) {
        console.warn('Failed to fetch server report, aggregating local answers:', err);
        report = buildLocalReport();
      }
    } else {
      report = buildLocalReport();
    }

    AppState.finalReport = report;
    renderFinalReport(report);
    switchView('report');
  }

  function buildLocalReport() {
    const scores = AppState.answers.map(a => a.score);
    const avgScore = scores.length > 0
      ? Math.round((scores.reduce((a, b) => a + b, 0) / scores.length) * 10) / 10
      : 0;

    const tier = avgScore >= 90 ? 'Excellent' : (avgScore >= 70 ? 'Good' : (avgScore >= 50 ? 'Average' : 'Poor'));

    // Topic aggregation
    const topicScores = {};
    AppState.answers.forEach((ans, idx) => {
      const q = DEMO_QUESTIONS[idx % DEMO_QUESTIONS.length];
      const topic = q.topic;
      if (!topicScores[topic]) topicScores[topic] = [];
      topicScores[topic].push(ans.score);
    });

    const topicBreakdown = Object.keys(topicScores).map(topic => {
      const arr = topicScores[topic];
      const avg = Math.round(arr.reduce((a, b) => a + b, 0) / arr.length);
      return {
        topic: topic,
        average_score: avg,
        questions_evaluated: arr.length
      };
    });

    const strong = topicBreakdown.filter(t => t.average_score >= 75).map(t => t.topic);
    const weak = topicBreakdown.filter(t => t.average_score < 70).map(t => t.topic);

    const recommendations = [];
    if (weak.length > 0) {
      weak.forEach(w => recommendations.push(`Revisit core algorithmic mechanics and edge cases for ${w}.`));
    } else {
      recommendations.push('Maintain consistency by practicing advanced architectural trade-offs under high concurrency.');
    }

    return {
      session_id: AppState.sessionId,
      candidate_name: (AppState.candidateProfile && AppState.candidateProfile.candidate_name) || 'Candidate',
      domain: AppState.selectedDomain,
      difficulty: AppState.selectedDifficulty,
      overall_score: avgScore,
      overall_quality_tier: tier,
      total_questions: AppState.selectedCount,
      topic_breakdown: topicBreakdown,
      strongest_topics: strong,
      weakest_topics: weak,
      study_recommendations: recommendations,
      itemized_answers: AppState.answers
    };
  }

  function renderFinalReport(report) {
    DOM.reportCandidateName.textContent = report.candidate_name || 'Candidate';
    DOM.reportDomain.textContent = report.domain || AppState.selectedDomain;
    DOM.reportDifficulty.textContent = report.difficulty || AppState.selectedDifficulty;
    DOM.reportSessionId.textContent = report.session_id || 'LOCAL-EVAL';
    DOM.reportOverallScore.textContent = report.overall_score !== undefined ? report.overall_score : '--';
    DOM.reportOverallTier.textContent = `${report.overall_quality_tier || 'Completed'} Performance`;
    DOM.reportCompletedCount.textContent = (report.itemized_answers || AppState.answers).length;

    // Topic Bars Table
    DOM.reportTopicBars.innerHTML = '';
    const breakdown = report.topic_breakdown || [];
    if (breakdown.length > 0) {
      breakdown.forEach(item => {
        const row = document.createElement('div');
        row.className = 'topic-row';
        const score = item.average_score || 0;
        const cls = score >= 75 ? 'Strong' : (score >= 50 ? 'Moderate' : 'Needs Focus');

        row.innerHTML = `
          <div class="topic-name" title="${escapeHtml(item.topic)}">${escapeHtml(item.topic)}</div>
          <div class="bar-track">
            <div class="bar-fill" style="width: ${Math.min(100, Math.max(0, score))}%;"></div>
          </div>
          <div class="topic-score-num">${score} / 100</div>
          <div class="topic-classification">${cls}</div>
        `;
        DOM.reportTopicBars.appendChild(row);
      });
    } else {
      DOM.reportTopicBars.innerHTML = '<div style="font-size: 0.85rem; color: var(--text-muted);">No topic data aggregated.</div>';
    }

    // Strong Areas
    DOM.reportStrongAreas.innerHTML = '';
    const strong = report.strongest_topics || [];
    if (strong.length > 0) {
      strong.forEach(t => {
        const li = document.createElement('li');
        li.textContent = t;
        DOM.reportStrongAreas.appendChild(li);
      });
    } else {
      DOM.reportStrongAreas.innerHTML = '<li>Baseline performance across all evaluated topics.</li>';
    }

    // Weak Areas
    DOM.reportWeakAreas.innerHTML = '';
    const weak = report.weakest_topics || [];
    if (weak.length > 0) {
      weak.forEach(t => {
        const li = document.createElement('li');
        li.textContent = t;
        DOM.reportWeakAreas.appendChild(li);
      });
    } else {
      DOM.reportWeakAreas.innerHTML = '<li>No critical conceptual deficits detected.</li>';
    }

    // Study Recommendations
    DOM.reportRecommendationsList.innerHTML = '';
    const recs = report.study_recommendations || [];
    recs.forEach((rec, idx) => {
      const item = document.createElement('div');
      item.style.fontSize = '0.88rem';
      item.style.lineHeight = '1.5';
      item.style.color = 'var(--text-secondary)';
      item.innerHTML = `<strong>${idx + 1}.</strong> ${escapeHtml(rec)}`;
      DOM.reportRecommendationsList.appendChild(item);
    });

    // History Table
    DOM.reportHistoryTableBody.innerHTML = '';
    const items = report.itemized_answers || AppState.answers;
    items.forEach((item, index) => {
      const tr = document.createElement('tr');
      const score = item.score !== undefined ? item.score : (item.evaluation && item.evaluation.score);
      const tier = item.quality_level || (item.evaluation && item.evaluation.quality_level) || 'Average';
      const topic = item.topic || `Question ${index + 1}`;

      tr.innerHTML = `
        <td class="mono">${index + 1}</td>
        <td style="font-weight: 500; color: var(--text-primary);">${escapeHtml(topic)}</td>
        <td class="mono" style="text-align: right; font-weight: 600;">${score}</td>
        <td style="text-align: center; text-transform: capitalize;">${escapeHtml(tier)}</td>
        <td style="text-align: right;">
          <button class="btn btn-subtle btn-sm view-details-btn" data-index="${index}">View</button>
        </td>
      `;
      DOM.reportHistoryTableBody.appendChild(tr);
    });

    // Attach row detail inspect handlers
    DOM.reportHistoryTableBody.querySelectorAll('.view-details-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const idx = parseInt(e.currentTarget.getAttribute('data-index'), 10);
        openQuestionDetailModal(idx);
      });
    });
  }

  // ============================================================================
  // QUESTION DETAILS MODAL
  // ============================================================================

  function openQuestionDetailModal(index) {
    const items = (AppState.finalReport && AppState.finalReport.itemized_answers) || AppState.answers;
    const item = items[index];
    if (!item) return;

    DOM.modalQuestionTitle.textContent = `Question ${index + 1} Assessment`;
    DOM.modalPrompt.textContent = item.question || (DEMO_QUESTIONS[index % DEMO_QUESTIONS.length].question);
    DOM.modalTranscribed.textContent = item.transcribed_answer || 'No speech transcription recorded.';
    DOM.modalModelAnswer.textContent = item.reference_answer || (item.evaluation && item.evaluation.reference_answer) || 'Archived in benchmark dataset.';

    const covered = (item.evaluation && item.evaluation.covered_concepts) || [];
    const missing = (item.evaluation && item.evaluation.missing_concepts) || [];

    let breakdownHtml = '<div style="margin-bottom: 8px;"><strong>Addressed Concepts:</strong><br>';
    if (covered.length > 0) {
      breakdownHtml += covered.map(c => `• ${escapeHtml(typeof c === 'object' ? c.concept : c)}`).join('<br>');
    } else {
      breakdownHtml += 'None';
    }
    breakdownHtml += '</div><div><strong>Omitted Concepts:</strong><br>';
    if (missing.length > 0) {
      breakdownHtml += missing.map(m => `• ${escapeHtml(m)}`).join('<br>');
    } else {
      breakdownHtml += 'None';
    }
    breakdownHtml += '</div>';

    DOM.modalConceptsBreakdown.innerHTML = breakdownHtml;
    DOM.questionDetailModal.classList.add('active');
  }

  function closeModal() {
    DOM.questionDetailModal.classList.remove('active');
  }

  // ============================================================================
  // UTILITIES & HELPERS
  // ============================================================================

  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  // ============================================================================
  // EVENT LISTENERS & LIFECYCLE
  // ============================================================================

  function setupEventListeners() {
    // Top Navigation & CTAs
    DOM.navBrandLink.addEventListener('click', (e) => {
      e.preventDefault();
      switchView('landing');
    });

    const startButtons = [DOM.navStartBtn, DOM.heroStartBtn, DOM.closingStartBtn];
    startButtons.forEach(btn => {
      if (btn) btn.addEventListener('click', () => switchView('setup'));
    });

    DOM.setupBackToLandingBtn.addEventListener('click', () => switchView('landing'));

    // Resume Dropzone & File Handling
    DOM.uploadDropzone.addEventListener('click', () => DOM.resumeFileInput.click());
    DOM.browseFileBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      DOM.resumeFileInput.click();
    });

    DOM.resumeFileInput.addEventListener('change', (e) => {
      const file = e.target.files && e.target.files[0];
      if (file) handleFileUpload(file);
    });

    // Drag and Drop
    ['dragenter', 'dragover'].forEach(name => {
      DOM.uploadDropzone.addEventListener(name, (e) => {
        e.preventDefault();
        DOM.uploadDropzone.classList.add('drag-active');
      });
    });

    ['dragleave', 'drop'].forEach(name => {
      DOM.uploadDropzone.addEventListener(name, (e) => {
        e.preventDefault();
        DOM.uploadDropzone.classList.remove('drag-active');
      });
    });

    DOM.uploadDropzone.addEventListener('drop', (e) => {
      const file = e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files[0];
      if (file) handleFileUpload(file);
    });

    DOM.replaceFileBtn.addEventListener('click', () => DOM.resumeFileInput.click());
    DOM.removeFileBtn.addEventListener('click', clearProfile);
    DOM.useDemoProfileBtn.addEventListener('click', () => displayProfile(DEMO_PROFILE));

    // Configuration Selectors
    DOM.domainSelector.addEventListener('click', (e) => {
      const btn = e.target.closest('.segment-btn');
      if (btn) selectDomain(btn.getAttribute('data-domain'));
    });

    DOM.difficultySelector.addEventListener('click', (e) => {
      const btn = e.target.closest('.segment-btn');
      if (btn) selectDifficulty(btn.getAttribute('data-difficulty'));
    });

    DOM.questionCountSelector.addEventListener('click', (e) => {
      const btn = e.target.closest('.segment-btn');
      if (btn) selectQuestionCount(btn.getAttribute('data-count'));
    });

    // Generate Interview
    DOM.generateInterviewBtn.addEventListener('click', generateInterviewSession);

    // Interview Controls
    DOM.exitInterviewBtn.addEventListener('click', () => {
      if (confirm('Exit active interview? Progress on unanswered questions will be discarded.')) {
        stopRecording(true);
        switchView('setup');
      }
    });

    DOM.startRecordingBtn.addEventListener('click', startRecording);
    DOM.stopRecordingBtn.addEventListener('click', () => stopRecording());
    DOM.retryRecordingBtn.addEventListener('click', () => resetRecordingWorkspace());
    DOM.submitAnswerBtn.addEventListener('click', submitAnswer);
    DOM.nextQuestionBtn.addEventListener('click', handleNextQuestion);

    // Report Actions
    DOM.reportPrintBtn.addEventListener('click', () => window.print());
    DOM.reportRestartBtn.addEventListener('click', () => {
      clearProfile();
      switchView('setup');
    });

    // Modal Actions
    DOM.closeModalBtn.addEventListener('click', closeModal);
    DOM.modalCloseActionBtn.addEventListener('click', closeModal);
    DOM.questionDetailModal.addEventListener('click', (e) => {
      if (e.target === DOM.questionDetailModal) closeModal();
    });

    // ESC key closes modal
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && DOM.questionDetailModal.classList.contains('active')) {
        closeModal();
      }
    });
  }

  // ============================================================================
  // INITIALIZATION
  // ============================================================================

  async function init() {
    buildWaveformBars();
    setupEventListeners();

    // Check system status
    const health = await ApiService.checkHealth();
    if (health.status === 'healthy') {
      DOM.systemHealthDot.classList.add('active');
      DOM.systemHealthText.textContent = 'System Ready';
    } else {
      DOM.systemHealthText.textContent = 'Demo Mode Ready';
    }

    // Default configuration summary
    selectDomain(CONFIG.defaultDomain);
    selectDifficulty(CONFIG.defaultDifficulty);
    selectQuestionCount(CONFIG.defaultQuestionCount);

    console.info('INTERVIEW LAB initialized successfully.');
  }

  // Launch on DOMContentLoaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
